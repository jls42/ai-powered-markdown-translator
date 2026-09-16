#!/usr/bin/env bash
# Gate de fraîcheur des dépendances DIRECTES.
#
# Raison d'être : Dependabot propose, il ne garantit pas. Ses PR peuvent
# s'empiler sans être mergées, et sans `.github/dependabot.yml` il ne proposait
# même rien hors CVE — c'est ainsi qu'`openai` a dérivé de 2.54 à 3.6 et
# `anthropic` de 0.125 à 1.2 sans que personne ne le voie, `certifi` accumulant
# deux ans de retard sur son magasin de certificats racine.
#
# Ce script rend le retard VISIBLE dans le verdict du projet, pas seulement
# dans une liste de PR ouvertes.
#
# Un retard ne compte qu'au-delà du DÉLAI D'ABSORPTION (GRACE_DAYS). Les
# mineures et correctifs sont désormais proposés chaque jour par Dependabot,
# trois jours après leur publication, puis fusionnés automatiquement quand la
# CI est verte. Comparer l'épinglage à la toute dernière version de PyPI
# signalait donc comme « en retard » des versions que Dependabot n'avait pas
# encore le droit de proposer — mesuré le 2026-09-16 sur trois versions
# publiées depuis moins de deux jours. Un avertissement qui crie au loup
# apprend à ne plus lire les vrais. Avant le délai, une version est « en
# route » ; après, c'est que l'automatisation est bloquée, et là il faut le
# savoir.
#
# Politique de sévérité, choisie pour que le signal reste lisible :
#   - retard de MAJEURE  -> échec. C'est le cas qui casse le code en silence
#     (anthropic >= 1.0 refuse un appel non-streamé à max_tokens élevé ;
#     google-genai a changé toute la surface d'appel) et celui qui s'est
#     réellement produit. Dependabot ouvre la PR, mais une majeure n'est
#     jamais fusionnée automatiquement : elle se valide par un appel réel.
#   - retard de mineure/correctif -> avertissement. Au-delà du délai, c'est
#     une fusion automatique qui n'a pas eu lieu. Avec `--strict` (contrôle
#     quotidien en CI), c'est un échec : l'échec d'un workflow planifié envoie
#     un mail, une alerte plutôt qu'une découverte.
#
# Le retard s'accompagne des NOTES DE VERSION, parce qu'un numéro ne dit pas ce
# qui change. Une mineure de SDK a déjà modifié des choses dont ce projet
# dépend : la tolérance des modèles aux champs inconnus, sans laquelle le
# `error` qu'OpenRouter ajoute à un choix disparaît en silence, ou la règle
# côté client qui refuse un appel non streamé trop long. Lire l'entrée avant de
# figer coûte deux minutes ; ne pas la lire a déjà coûté davantage.
#
# Usage : ./scripts/check-deps-fresh.sh [--strict] [--grace-days N]

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Délai d'absorption, en jours : refroidissement de Dependabot (3 j,
# `cooldown.default-days`) + cadence de ses passages (1 j, `interval: daily`)
# + 1 j de marge. Une version publiée depuis moins longtemps n'est pas en
# retard : l'automatisation a encore le temps de l'absorber. L'égalité avec
# `.github/dependabot.yml` est vérifiée par scripts/tests/test_pypi_versions.py.
GRACE_DAYS=5
STRICT=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --strict)
      STRICT=true
      shift
      ;;
    --grace-days)
      GRACE_DAYS="${2:-}"
      shift 2 || { echo "--grace-days attend un nombre de jours" >&2; exit 2; }
      ;;
    *)
      echo "option inconnue : $1 (usage : $0 [--strict] [--grace-days N])" >&2
      exit 2
      ;;
  esac
done

if [[ ! "$GRACE_DAYS" =~ ^[0-9]+$ ]]; then
  echo "--grace-days attend un entier positif, reçu : '$GRACE_DAYS'" >&2
  exit 2
fi

# Dépendances réellement importées par le module, plus certifi : celui-ci
# n'est pas importé mais embarque le magasin de CA qui valide TLS pour tous les
# appels providers. Un retard y est un problème de sécurité, pas de confort.
DIRECT_DEPS="openai anthropic mistralai google-genai langdetect python-dotenv certifi"

# Où lire ce qui change, par paquet. Les SDK des providers tiennent un
# CHANGELOG à la racine de leur dépôt ; pour les autres, la page des versions
# de PyPI est le point d'entrée le plus stable.
changelog_url() {
  local pkg="$1"
  case "$pkg" in
    openai)         echo "https://github.com/openai/openai-python/blob/main/CHANGELOG.md" ;;
    anthropic)      echo "https://github.com/anthropics/anthropic-sdk-python/blob/main/CHANGELOG.md" ;;
    mistralai)      echo "https://github.com/mistralai/client-python/releases" ;;
    google-genai)   echo "https://github.com/googleapis/python-genai/blob/main/CHANGELOG.md" ;;
    langdetect)     echo "https://pypi.org/project/langdetect/#history" ;;
    python-dotenv)  echo "https://github.com/theskumar/python-dotenv/blob/main/CHANGELOG.md" ;;
    certifi)        echo "https://github.com/certifi/python-certifi/releases" ;;
    *)              echo "https://pypi.org/project/$pkg/#history" ;;
  esac
  return 0
}

if [[ ! -f requirements.txt ]]; then
  echo "requirements.txt introuvable" >&2
  exit 1
fi

# Sans réseau, on ne peut rien affirmer. On skippe explicitement plutôt que de
# conclure au vert — un contrôle qui ne s'est pas exécuté n'est pas un succès.
if ! curl -sf --max-time 10 https://pypi.org/simple/ -o /dev/null 2>/dev/null; then
  echo "⚠ PyPI injoignable — contrôle de fraîcheur non exécuté." >&2
  if [[ -n "${CI:-}" || -n "${GITHUB_ACTIONS:-}" ]]; then
    echo "  Détecté CI → fail-closed." >&2
    exit 1
  fi
  exit 0
fi

OUTDATED_MAJOR=()
OUTDATED_MINOR=()
EN_ROUTE=()
# Compté explicitement : sauter en silence un paquet dont la requête PyPI a
# échoué laisserait le gate au vert en n'ayant pas vérifié ce paquet — le mode
# de défaillance que ce script dénonce en tête. On compare le compte final au
# nombre attendu.
CHECKED=0
EXPECTED=0
UNREACHABLE=""

for pkg in $DIRECT_DEPS; do
  EXPECTED=$((EXPECTED + 1))
  pinned=$(grep -iE "^${pkg}==" requirements.txt | head -1 | cut -d= -f3)
  if [[ -z "$pinned" ]]; then
    echo "⚠ $pkg absent de requirements.txt alors qu'il est déclaré direct" >&2
    OUTDATED_MAJOR+=("$pkg(non-épinglé)")
    # Compté comme vérifié : la question a bien été posée, et la réponse est
    # « non épinglé ». Sans ça, le message générique de couverture masquerait
    # le diagnostic précis.
    CHECKED=$((CHECKED + 1))
    continue
  fi
  # Le JSON complet, pas seulement `info.version` : le délai se juge sur la
  # date de publication de chaque version. Un JSON illisible compte comme
  # injoignable, jamais comme « à jour ».
  verdict=$(curl -sf --max-time 15 "https://pypi.org/pypi/${pkg}/json" 2>/dev/null \
    | python3 scripts/pypi_versions.py --pinned "$pinned" --grace-days "$GRACE_DAYS" 2>/dev/null)
  if [[ -z "$verdict" ]]; then
    UNREACHABLE="$UNREACHABLE $pkg"
    continue
  fi
  IFS=$'\t' read -r status _ eligible eligible_age newest newest_age <<< "$verdict"
  case "$status" in
    a-jour) ;;
    en-route) EN_ROUTE+=("${pkg} ${newest} (publiée il y a ${newest_age} j)") ;;
    mineure) OUTDATED_MINOR+=("${pkg}(${pinned}→${eligible}, publiée il y a ${eligible_age} j)") ;;
    majeure) OUTDATED_MAJOR+=("${pkg}(${pinned}→${eligible}, publiée il y a ${eligible_age} j)") ;;
    *)
      UNREACHABLE="$UNREACHABLE $pkg"
      continue
      ;;
  esac
  CHECKED=$((CHECKED + 1))
done

if [[ -n "$UNREACHABLE" ]]; then
  printf '✗ version PyPI non obtenue pour :%s\n' "$UNREACHABLE" >&2
  echo "  Ces paquets n'ont pas été vérifiés : le contrôle n'est pas concluant." >&2
  exit 1
fi

if [[ "$CHECKED" -ne "$EXPECTED" ]]; then
  printf '✗ %s paquets vérifiés sur %s attendus — contrôle incomplet\n' "$CHECKED" "$EXPECTED" >&2
  exit 1
fi

# Les notes de version des paquets en retard, majeures et mineures confondues :
# c'est ce qu'il faut lire avant de figer une version, et le retrouver soi-même
# est la friction qui fait sauter l'étape.
print_changelogs() {
  local entry pkg
  for entry in "$@"; do
    pkg="${entry%%(*}"
    printf '    %-14s %s\n' "$pkg" "$(changelog_url "$pkg")" >&2
  done
  return 0
}

join_entries() {
  local separator=" " entry
  for entry in "$@"; do
    printf '%s%s' "$separator" "$entry"
    separator=", "
  done
  return 0
}

# Information seule, sans symbole d'avertissement : check-release-ready.sh ne
# compte que les lignes ⚠ et ✗, et une version dans son délai n'est pas un
# problème.
if [[ ${#EN_ROUTE[@]} -gt 0 ]]; then
  printf '↻ en route, publiées depuis moins de %s j :%s\n' "$GRACE_DAYS" "$(join_entries "${EN_ROUTE[@]}")" >&2
fi

if [[ ${#OUTDATED_MINOR[@]} -gt 0 ]]; then
  printf '⚠ mineures en retard de plus de %s j :%s\n' "$GRACE_DAYS" "$(join_entries "${OUTDATED_MINOR[@]}")" >&2
  echo "  La fusion automatique n'a pas eu lieu : chercher la PR Dependabot et son" >&2
  echo "  check en échec (par exemple la fermeture du lock, quand une dépendance" >&2
  echo "  transitive doit bouger). Lire les notes de version avant de figer :" >&2
  print_changelogs "${OUTDATED_MINOR[@]}"
fi

if [[ ${#OUTDATED_MAJOR[@]} -gt 0 ]]; then
  printf '✗ MAJEURES en retard de plus de %s j :%s\n' "$GRACE_DAYS" "$(join_entries "${OUTDATED_MAJOR[@]}")" >&2
  echo "  Une majeure n'est jamais fusionnée automatiquement : elle peut casser le" >&2
  echo "  code sans que la doc le dise. Lire les notes de version, puis valider par" >&2
  echo "  un appel RÉEL, provider par provider, avant de merger la PR Dependabot :" >&2
  print_changelogs "${OUTDATED_MAJOR[@]}"
  exit 1
fi

if [[ "$STRICT" == true && ${#OUTDATED_MINOR[@]} -gt 0 ]]; then
  echo "✗ mode strict : une mineure bloquée au-delà du délai est un échec" >&2
  exit 1
fi

printf "dépendances directes à jour (majeures) — %s/%s vérifiées, délai d'absorption %s j\n" "$CHECKED" "$EXPECTED" "$GRACE_DAYS"
exit 0
