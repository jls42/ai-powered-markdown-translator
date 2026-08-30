#!/usr/bin/env bash
# Verdict binaire « prêt à annoncer / prêt à releaser ».
#
# Raison d'être : remplacer une affirmation ("c'est bon") par une preuve
# reproductible. Tant que ce script n'est pas vert, le travail n'est pas
# terminé — quelle que soit l'impression laissée par les étapes précédentes.
#
# Usage :
#   ./scripts/check-release-ready.sh            # tout sauf les hooks lents
#   ./scripts/check-release-ready.sh --full     # + hooks pre-push (mypy, SAST, audit)
#
# Sortie : 0 si tout est vert, 1 sinon. Chaque échec est expliqué.

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

FULL=false
[[ "${1:-}" == "--full" ]] && FULL=true

FAILURES=0
# Compteur dérivé des pass() réellement émis : le total était codé en dur
# (« 12 »), donc faux dès qu'une vérification était ajoutée.
CHECKS=0
# `local msg="$1"` et `return 0` explicites : sans eux, le statut de sortie de
# ces helpers est celui de leur dernière commande, ce qui les rend fragiles dès
# qu'on les enchaîne (`pass "x" && …`). Le script existant pour produire un
# verdict fiable, autant que ses primitives en aient un.
pass() { local msg="$1"; printf '  \033[32m✓\033[0m %s\n' "$msg"; CHECKS=$((CHECKS + 1)); return 0; }
fail() { local msg="$1"; printf '  \033[31m✗\033[0m %s\n' "$msg"; FAILURES=$((FAILURES + 1)); return 0; }
section() { local title="$1"; printf '\n\033[1m%s\033[0m\n' "$title"; return 0; }

PY=./venv/bin/python
[[ -x "$PY" ]] || { echo "venv absent : python -m venv venv && pip install -r requirements.txt"; exit 1; }

PROBE_ERR=$(mktemp)
trap 'rm -f "$PROBE_ERR"' EXIT

# Exécute une sonde Python (script sur stdin) et impose DEUX conditions avant
# que sa sortie soit exploitable : code retour nul, et sentinelle `PROBE_OK`
# émise en dernière ligne.
#
# Sans cela, une sonde qui plante (fichier renommé, SyntaxError après édition,
# FileNotFoundError) écrivait sur stderr et sortait en erreur — mais seul son
# stdout était testé, et un stdout vide se lit « rien à signaler ». Quatre
# vérifications passaient donc au vert en n'ayant rien vérifié : le piège
# « un exit 0 ne prouve rien » reproduit à l'intérieur du script écrit pour
# l'empêcher. Les sondes qui construisent une liste de repères refusent en
# outre de conclure sur un ensemble vide (une assertion sur ensemble vide est
# toujours vraie), en sortant en erreur — rattrapé ici.
#
# Résultat exploitable dans $PROBE_OUT ; retourne 1 si la sonde est invalide.
probe() {
  local label="$1" rc
  PROBE_OUT=$($PY - 2>"$PROBE_ERR")
  rc=$?
  if [[ $rc -ne 0 ]]; then
    fail "$label — sonde en échec (rc=$rc) : $(tail -1 "$PROBE_ERR")"
    return 1
  fi
  if [[ "${PROBE_OUT##*$'\n'}" != "PROBE_OK" ]]; then
    fail "$label — sonde interrompue avant sa fin (sentinelle absente)"
    return 1
  fi
  PROBE_OUT="${PROBE_OUT%$'\n'PROBE_OK}"
  [[ "$PROBE_OUT" == "PROBE_OK" ]] && PROBE_OUT=""
  return 0
}

section "1. Tests"
if $PY -m unittest discover tests/ >/dev/null 2>&1; then
  pass "tests/ ($($PY -m unittest discover tests/ 2>&1 | grep -oE 'Ran [0-9]+' | grep -oE '[0-9]+') tests)"
else
  fail "tests/ en échec — lancer: $PY -m unittest discover tests/"
fi
if $PY -m unittest discover scripts/tests/ >/dev/null 2>&1; then
  pass "scripts/tests/"
else
  fail "scripts/tests/ en échec"
fi

section "2. Qualité"
if pre-commit run --all-files >/dev/null 2>&1; then
  pass "hooks pre-commit"
else
  fail "hooks pre-commit — lancer: pre-commit run --all-files"
fi
if $FULL; then
  if pre-commit run --hook-stage pre-push --all-files >/dev/null 2>&1; then
    pass "hooks pre-push (mypy, SAST, pip-audit, tests)"
  else
    fail "hooks pre-push — lancer: pre-commit run --hook-stage pre-push --all-files"
  fi
else
  printf '  \033[33m~\033[0m hooks pre-push non exécutés (utiliser --full)\n'
fi

section "3. Documentation synchronisée avec le code"
# `\.add_argument\(` et non `parser\.add_argument\(` : les flags provider
# passent par un add_mutually_exclusive_group, donc par un objet `*_group`.
# Avec l'ancien ancrage, six flags — dont --use_codex et --use_grok_cli —
# sortaient du périmètre en silence et la vérification restait verte.
# EXPECTED_FLAGS interdit qu'un refactor d'argparse vide l'ensemble sans que
# personne ne le voie : une assertion sur ensemble vide est toujours vraie.
if probe "flags documentés" <<'PYEOF'
import re, sys
EXPECTED_FLAGS = 21
code = open("translate.py", encoding="utf-8").read()
readme = open("README.md", encoding="utf-8").read()
flags = set(re.findall(r'\.add_argument\(\s*"(--[a-z_]+)"', code))
if len(flags) < EXPECTED_FLAGS:
    sys.exit(f"{len(flags)} flags détectés, {EXPECTED_FLAGS} attendus — la regex "
             "de détection ne suit plus argparse, la vérification serait vide")
print(" ".join(sorted(f for f in flags if f"`{f}`" not in readme)))
print("PROBE_OK")
PYEOF
then
  if [[ -z "$PROBE_OUT" ]]; then
    pass "tous les flags argparse sont dans le README"
  else
    fail "flags absents du README : $PROBE_OUT"
  fi
fi

# Le second motif rattrape `os.getenv(NOM_DE_CONSTANTE, ...)` : la sonde ne
# lisait que les littéraux, donc GROK_TRANSLATE_SANDBOX — passé via la
# constante GROK_SANDBOX_ENV_VAR — échappait au filet alors que CLAUDE.md
# annonce « chaque os.getenv documenté ».
if probe "variables d'environnement" <<'PYEOF'
import re, sys
code = open("translate.py", encoding="utf-8").read()
docs = open("README.md", encoding="utf-8").read() + open("CLAUDE.md", encoding="utf-8").read()
env = set(re.findall(r'os\.getenv\(\s*"([A-Z_]+)"', code))
for const in re.findall(r'os\.getenv\(\s*([A-Z_]+)\s*[,)]', code):
    m = re.search(rf'^{const}\s*=\s*"([A-Z_]+)"', code, re.M)
    if m:
        env.add(m.group(1))
if not env:
    sys.exit("aucune variable détectée — la regex ne suit plus le code")
print(" ".join(sorted(v for v in env if v not in docs)))
print("PROBE_OK")
PYEOF
then
  if [[ -z "$PROBE_OUT" ]]; then
    pass "toutes les variables d'environnement sont documentées"
  else
    fail "variables non documentées : $PROBE_OUT"
  fi
fi

section "4. Traductions"
MISSING=0
for base in README CHANGELOG; do
  for lang in ar de en es hi it ja ko nl pl pt ro sv zh; do
    [[ -f "$base-$lang.md" ]] || { fail "$base-$lang.md absent"; MISSING=1; }
  done
done
if [[ $MISSING -eq 0 ]]; then pass "28/28 fichiers présents"; fi

if probe "structure des traductions" <<'PYEOF'
import re, sys
seen = 0
P = {"fence": r"^```", "head": r"^#{1,6} ", "list": r"^\s*[-*] ", "table": r"^\|",
     "a": r"<a\s+href=", "img": r"<img\s+src="}
URL = re.compile(r"https?://[^\s)\"'<>`,]+")
RES = re.compile(r"#(?:CODEBLOCK|INLINECODE|URL|ANCHOR|REFLABEL)\d+#|<NEWSQUOTE\s+id=")
bad = []
for base in ("README", "CHANGELOG"):
    src = open(f"{base}.md", encoding="utf-8").read()
    sp = {k: len(re.findall(v, src, re.M)) for k, v in P.items()}
    surls = {u for u in URL.findall(src) if "..." not in u}
    sres = len(RES.findall(src))
    for lang in "ar de en es hi it ja ko nl pl pt ro sv zh".split():
        try:
            t = open(f"{base}-{lang}.md", encoding="utf-8").read()
        except FileNotFoundError:
            continue
        seen += 1
        d = [k for k, v in P.items() if len(re.findall(v, t, re.M)) != sp[k]]
        miss = {u for u in surls if u not in t}
        res = len(RES.findall(t)) - sres
        if d or miss or res > 0:
            bad.append(f"{base}-{lang}({','.join(d) or ''}{f' {len(miss)}urls' if miss else ''}{f' {res}resid' if res > 0 else ''})")
if seen != 28:
    sys.exit(f"{seen} traductions lues sur 28 — la comparaison serait partielle")
print(" ".join(bad))
print("PROBE_OK")
PYEOF
then
  if [[ -z "$PROBE_OUT" ]]; then
    pass "structure, URLs et placeholders conformes sur les 28"
  else
    fail "traductions divergentes : $PROBE_OUT"
  fi
fi

# Fraîcheur par CONTENU et non par date : prettier réécrit la source sans en
# changer le sens, ce qui rendrait toute comparaison de timestamps trompeuse.
if probe "fraîcheur des traductions" <<'PYEOF'
import re, sys
readme = open("README.md", encoding="utf-8").read()
# Repères : chaque flag documenté doit se retrouver dans les traductions.
keys = [f"`{f}`" for f in re.findall(r'\.add_argument\(\s*"(--[a-z_]+)"', open("translate.py", encoding="utf-8").read())]
keys = [k for k in keys if k in readme]
# Sans ce garde-fou, une regex qui cesse de matcher vide `keys` et rend
# l'assertion « aucun repère absent » vraie pour les 14 langues — vert en
# n'ayant rien vérifié.
if len(keys) < 15:
    sys.exit(f"{len(keys)} repères seulement — la détection des flags ne suit plus argparse")
stale = []
for lang in "ar de en es hi it ja ko nl pl pt ro sv zh".split():
    try:
        t = open(f"README-{lang}.md", encoding="utf-8").read()
    except FileNotFoundError:
        continue
    absent = [k for k in keys if k not in t]
    if absent:
        stale.append(f"{lang}({len(absent)} manquants)")
print(" ".join(stale))
print("PROBE_OK")
PYEOF
then
  if [[ -z "$PROBE_OUT" ]]; then
    pass "les traductions couvrent tous les flags documentés"
  else
    fail "traductions périmées : $PROBE_OUT — relancer ./regen_translations.sh --force"
  fi
fi

section "5. Cohérence de version"
CHANGELOG_VERSION=$(grep -m 1 -oE '\*\*[0-9]+\.[0-9]+(\.[0-9]+)?\*\*' CHANGELOG.md | head -1 | tr -d '*')
if [[ -n "$CHANGELOG_VERSION" ]]; then
  pass "version détectée dans le CHANGELOG : $CHANGELOG_VERSION"
  NOTES=$(awk -v v="${CHANGELOG_VERSION//./\\.}" '
    $0 ~ "^- \\*\\*" v "\\*\\*" { keep = 1 }
    keep && $0 ~ "^- \\*\\*[0-9]+\\.[0-9]+" && $0 !~ "^- \\*\\*" v "\\*\\*" { exit }
    keep { print }' CHANGELOG.md | wc -l)
  if [[ "$NOTES" -gt 3 ]]; then
    pass "notes de release extractibles ($NOTES lignes)"
  else
    fail "notes de release quasi vides ($NOTES lignes) — entrée mal formée ?"
  fi
  N=0
  for lang in ar de en es hi it ja ko nl pl pt ro sv zh; do
    grep -q "$CHANGELOG_VERSION" "CHANGELOG-$lang.md" 2>/dev/null && N=$((N + 1))
  done
  if [[ "$N" -eq 14 ]]; then
    pass "version $CHANGELOG_VERSION présente dans les 14 CHANGELOG traduits"
  else
    fail "version absente de $((14 - N)) CHANGELOG traduits"
  fi
else
  fail "aucune version lisible en tête du CHANGELOG"
fi

section "6. Hygiène du dépôt"
# `git diff --cached` ne compare que l'index à HEAD : un .env DÉJÀ commité
# n'y apparaît jamais, et le pire cas passait donc au vert. `git ls-files`
# interroge le suivi réel.
if git ls-files --error-unmatch .env >/dev/null 2>&1; then
  fail ".env est SUIVI par git — le retirer (git rm --cached .env) et rotater les clés"
elif git diff --cached --name-only 2>/dev/null | grep -q '^\.env$'; then
  fail ".env est en staging — il ne doit JAMAIS être commité"
else
  pass ".env ni suivi ni en staging"
fi
# La classe [A-Za-z0-9] exclut le tiret : `sk-proj-…` (format OpenAI actuel)
# et `sk-ant-api03-…` (Anthropic) cassaient sur leur second tiret et
# échappaient au scan, tout comme `AIza…` (Google). Le dépôt utilise six
# providers ; le motif en couvrait deux, dont un seul au format courant.
# Les placeholders `votre-cle-api-*` restent hors du motif par construction.
LEAK=$(git grep -lE "(sk-[A-Za-z0-9_-]{20,}|xai-[A-Za-z0-9_-]{40,}|AIza[A-Za-z0-9_-]{30,})" -- . ':(exclude).secrets.baseline' 2>/dev/null | head -3)
if [[ -z "$LEAK" ]]; then
  pass "aucune clé API dans les fichiers suivis"
else
  fail "clé API potentielle dans : $LEAK"
fi

printf '\n'
if [[ $FAILURES -eq 0 ]]; then
  printf '\033[32m════ PRÊT : %d vérifications au vert ════\033[0m\n' "$CHECKS"
  exit 0
fi
printf '\033[31m════ PAS PRÊT : %d vérification(s) en échec ════\033[0m\n' "$FAILURES"
exit 1
