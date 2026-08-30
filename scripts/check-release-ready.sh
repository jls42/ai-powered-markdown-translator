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
pass() { printf '  \033[32m✓\033[0m %s\n' "$1"; }
fail() { printf '  \033[31m✗\033[0m %s\n' "$1"; FAILURES=$((FAILURES + 1)); }
section() { printf '\n\033[1m%s\033[0m\n' "$1"; }

PY=./venv/bin/python
[[ -x "$PY" ]] || { echo "venv absent : python -m venv venv && pip install -r requirements.txt"; exit 1; }

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
UNDOC_FLAGS=$($PY - <<'PYEOF'
import re
code = open("translate.py", encoding="utf-8").read()
readme = open("README.md", encoding="utf-8").read()
# Flags déclarés dans argparse uniquement (pas ceux des CLI externes).
flags = set(re.findall(r'parser\.add_argument\(\s*"(--[a-z_]+)"', code))
print(" ".join(sorted(f for f in flags if f"`{f}`" not in readme)))
PYEOF
)
if [[ -z "$UNDOC_FLAGS" ]]; then
  pass "tous les flags argparse sont dans le README"
else
  fail "flags absents du README : $UNDOC_FLAGS"
fi

UNDOC_ENV=$($PY - <<'PYEOF'
import re
code = open("translate.py", encoding="utf-8").read()
docs = open("README.md", encoding="utf-8").read() + open("CLAUDE.md", encoding="utf-8").read()
env = set(re.findall(r'os\.getenv\(\s*"([A-Z_]+)"', code))
print(" ".join(sorted(v for v in env if v not in docs)))
PYEOF
)
if [[ -z "$UNDOC_ENV" ]]; then
  pass "toutes les variables d'environnement sont documentées"
else
  fail "variables non documentées : $UNDOC_ENV"
fi

section "4. Traductions"
MISSING=0
for base in README CHANGELOG; do
  for lang in ar de en es hi it ja ko nl pl pt ro sv zh; do
    [[ -f "$base-$lang.md" ]] || { fail "$base-$lang.md absent"; MISSING=1; }
  done
done
if [[ $MISSING -eq 0 ]]; then pass "28/28 fichiers présents"; fi

STRUCT=$($PY - <<'PYEOF'
import re
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
        d = [k for k, v in P.items() if len(re.findall(v, t, re.M)) != sp[k]]
        miss = {u for u in surls if u not in t}
        res = len(RES.findall(t)) - sres
        if d or miss or res > 0:
            bad.append(f"{base}-{lang}({','.join(d) or ''}{f' {len(miss)}urls' if miss else ''}{f' {res}resid' if res > 0 else ''})")
print(" ".join(bad))
PYEOF
)
if [[ -z "$STRUCT" ]]; then
  pass "structure, URLs et placeholders conformes sur les 28"
else
  fail "traductions divergentes : $STRUCT"
fi

# Fraîcheur par CONTENU et non par date : prettier réécrit la source sans en
# changer le sens, ce qui rendrait toute comparaison de timestamps trompeuse.
STALE=$($PY - <<'PYEOF'
import re
readme = open("README.md", encoding="utf-8").read()
# Repères : chaque flag documenté doit se retrouver dans les traductions.
keys = [f"`{f}`" for f in re.findall(r'parser\.add_argument\(\s*"(--[a-z_]+)"', open("translate.py", encoding="utf-8").read())]
keys = [k for k in keys if k in readme]
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
PYEOF
)
if [[ -z "$STALE" ]]; then
  pass "les traductions couvrent tous les flags documentés"
else
  fail "traductions périmées : $STALE — relancer ./regen_translations.sh --force"
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
if git diff --cached --name-only 2>/dev/null | grep -q '^\.env$'; then
  fail ".env est en staging — il ne doit JAMAIS être commité"
else
  pass ".env hors de l'index"
fi
LEAK=$(git grep -lE "(sk-[A-Za-z0-9]{20,}|xai-[A-Za-z0-9]{40,})" -- . 2>/dev/null | head -3)
if [[ -z "$LEAK" ]]; then
  pass "aucune clé API dans les fichiers suivis"
else
  fail "clé API potentielle dans : $LEAK"
fi

printf '\n'
if [[ $FAILURES -eq 0 ]]; then
  printf '\033[32m════ PRÊT : %s vérifications au vert ════\033[0m\n' "$($FULL && echo 13 || echo 12)"
  exit 0
fi
printf '\033[31m════ PAS PRÊT : %d vérification(s) en échec ════\033[0m\n' "$FAILURES"
exit 1
