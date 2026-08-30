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
# Politique de sévérité, choisie pour que le signal reste lisible :
#   - retard de MAJEURE  -> échec. C'est le cas qui casse le code en silence
#     (anthropic >= 1.0 refuse un appel non-streamé à max_tokens élevé ;
#     google-genai a changé toute la surface d'appel) et celui qui s'est
#     réellement produit.
#   - retard de mineure/correctif -> avertissement. Échouer sur chaque patch
#     rendrait le gate rouge en permanence, donc ignoré — exactement le mode de
#     défaillance qu'on cherche à éviter.
#
# Usage : ./scripts/check-deps-fresh.sh

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Dépendances réellement importées par translate.py, plus certifi : celui-ci
# n'est pas importé mais embarque le magasin de CA qui valide TLS pour tous les
# appels providers. Un retard y est un problème de sécurité, pas de confort.
DIRECT_DEPS="openai anthropic mistralai google-genai langdetect python-dotenv certifi"

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

OUTDATED_MAJOR=""
OUTDATED_MINOR=""
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
    OUTDATED_MAJOR="$OUTDATED_MAJOR $pkg(non-épinglé)"
    # Compté comme vérifié : la question a bien été posée, et la réponse est
    # « non épinglé ». Sans ça, le message générique de couverture masquerait
    # le diagnostic précis.
    CHECKED=$((CHECKED + 1))
    continue
  fi
  latest=$(curl -sf --max-time 15 "https://pypi.org/pypi/${pkg}/json" 2>/dev/null \
    | python3 -c 'import json,sys; print(json.load(sys.stdin)["info"]["version"])' 2>/dev/null)
  if [[ -z "$latest" ]]; then
    UNREACHABLE="$UNREACHABLE $pkg"
    continue
  fi
  CHECKED=$((CHECKED + 1))
  [[ "$pinned" == "$latest" ]] && continue

  # Comparaison sur le premier composant. Couvre le versionnage sémantique
  # (2.54.0 -> 3.6.0) comme le versionnage par date de certifi (2024.x -> 2026.x).
  if [[ "${pinned%%.*}" != "${latest%%.*}" ]]; then
    OUTDATED_MAJOR="$OUTDATED_MAJOR ${pkg}(${pinned}→${latest})"
  else
    OUTDATED_MINOR="$OUTDATED_MINOR ${pkg}(${pinned}→${latest})"
  fi
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

if [[ -n "$OUTDATED_MINOR" ]]; then
  printf '⚠ mineures en retard :%s\n' "$OUTDATED_MINOR" >&2
fi

if [[ -n "$OUTDATED_MAJOR" ]]; then
  printf '✗ MAJEURES en retard :%s\n' "$OUTDATED_MAJOR" >&2
  echo "  Une majeure de SDK peut casser le code sans que la doc le dise :" >&2
  echo "  valider par un appel RÉEL, provider par provider, avant de figer." >&2
  exit 1
fi

printf 'dépendances directes à jour (majeures) — %s/%s vérifiées\n' "$CHECKED" "$EXPECTED"
exit 0
