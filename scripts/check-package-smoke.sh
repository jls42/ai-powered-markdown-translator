#!/usr/bin/env bash
# Vérifie le PAQUET tel qu'un utilisateur le reçoit, pas l'arbre de travail.
#
# Raison d'être : la suite de tests s'exécute sur les sources, et elle reste
# verte alors même que le paquet distribué est cassé — un module oublié dans
# `[tool.setuptools]`, un point d'entrée qui ne résout pas, une dépendance
# absente de `requirements.txt` mais présente dans le venv de travail. Le seul
# moyen de le savoir est d'installer le paquet ailleurs et de s'en servir.
#
# Deux moments, deux modes :
#
#   --wheel          AVANT la release : construit la roue depuis l'arbre et
#                    l'installe dans un venv jetable. C'est là que le gros du
#                    travail se fait, parce qu'un défaut trouvé ici se corrige
#                    par un commit.
#   --pypi [VERSION] APRÈS la release : installe depuis PyPI. Vérification
#                    légère, tout ayant déjà été éprouvé avant — mais elle
#                    seule prouve que ce sont bien ces octets-là qui sont
#                    partis, et PyPI n'autorise jamais de republier une
#                    version.
#
# Options :
#   --no-translation  s'arrête après les contrôles hors ligne (aucun appel de
#                     modèle, aucun coût). C'est ce que fait le gate.
#
# La traduction réelle utilise Gemini s'il y a une clé, sinon OpenAI ; sans
# clé, elle est SAUTÉE explicitement — un contrôle qui ne s'est pas exécuté
# n'est pas un succès. `SMOKE_PROVIDER_FLAGS` force un autre chemin.

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

MODE="wheel"
VERSION=""
TRANSLATE=1
while [[ $# -gt 0 ]]; do
  case "$1" in
    --wheel)          MODE="wheel"; shift ;;
    --pypi)           MODE="pypi"; shift; [[ ${1:-} =~ ^[0-9] ]] && { VERSION="$1"; shift; } ;;
    --no-translation) TRANSLATE=0; shift ;;
    *) echo "option inconnue : $1" >&2; exit 2 ;;
  esac
done

PKG="ai-powered-markdown-translator"
EXPECTED=$(grep -m1 '^version' pyproject.toml | cut -d'"' -f2)
[[ -z "$VERSION" ]] && VERSION="$EXPECTED"

FAILURES=0
pass() { printf '  \033[32m✓\033[0m %s\n' "$1"; }
fail() { printf '  \033[31m✗\033[0m %s\n' "$1"; FAILURES=$((FAILURES + 1)); }
skip() { printf '  \033[33m~\033[0m %s\n' "$1"; }

TMP=$(mktemp -d) || exit 1
trap 'rm -rf "$TMP"' EXIT

printf '\033[1mPaquet %s %s — mode %s\033[0m\n' "$PKG" "$VERSION" "$MODE"

python3 -m venv "$TMP/venv" >/dev/null 2>&1 || { fail "création du venv jetable"; exit 1; }
PY="$TMP/venv/bin/python"
BIN="$TMP/venv/bin/aipmt"

if [[ "$MODE" == "wheel" ]]; then
  # `--wheel` seul : `python -m build` sans argument construit la roue DEPUIS la
  # sdist, ce qui exige d'extraire une archive tar — cassé sur le paquet python3
  # d'Ubuntu 24.04 (rétroportage de `tarfile` sans la constante de `posixpath`).
  if ! ./venv/bin/python -m build --wheel --outdir "$TMP/dist" >"$TMP/build.log" 2>&1; then
    fail "construction de la roue (cf. $TMP/build.log)"; exit 1
  fi
  WHEELS=("$TMP"/dist/*.whl)
  if [[ ${#WHEELS[@]} -ne 1 ]]; then
    fail "${#WHEELS[@]} roues construites, une seule attendue"; exit 1
  fi
  pass "roue construite : $(basename "${WHEELS[0]}")"
  # Le contenu de la roue : rien d'autre que le paquet, ses métadonnées et la
  # licence. Un fichier de test ou un `.env` embarqué se verrait ici.
  INTRUS=$("$PY" -c "
import sys, zipfile
noms = zipfile.ZipFile(sys.argv[1]).namelist()
intrus = [n for n in noms if not (n.startswith('aipmt/') or '.dist-info/' in n)]
print(' '.join(intrus))" "${WHEELS[0]}")
  if [[ -n "$INTRUS" ]]; then fail "fichiers étrangers dans la roue : $INTRUS"; else pass "la roue ne contient que le paquet"; fi
  INSTALL=("${WHEELS[0]}")
else
  INSTALL=("$PKG==$VERSION")
fi

if ! "$TMP/venv/bin/pip" install -q "${INSTALL[@]}" >"$TMP/pip.log" 2>&1; then
  fail "installation (cf. $TMP/pip.log)"; tail -3 "$TMP/pip.log" >&2; exit 1
fi
pass "installé dans un venv neuf"

# À partir d'ici, TOUT s'exécute hors du dépôt et sans PYTHONPATH : sinon
# l'arbre de travail serait importé à la place du paquet, et le contrôle
# vérifierait exactement ce qu'il est censé ignorer.
run_installed() { (cd / && env -u PYTHONPATH "$@"); }

INSTALLED=$(run_installed "$PY" -c "import importlib.metadata as m; print(m.version('$PKG'))" 2>/dev/null)
if [[ "$INSTALLED" == "$VERSION" ]]; then pass "version installée : $INSTALLED"; else fail "version installée $INSTALLED, attendue $VERSION"; fi

if run_installed "$BIN" --help 2>/dev/null | head -1 | grep -q '^usage: aipmt'; then
  pass "point d'entrée console : aipmt --help"
else
  fail "point d'entrée console cassé — c'est ce que casse un paquet homonyme sur PyPI"
fi

if run_installed "$PY" -m aipmt --help 2>/dev/null | head -1 | grep -q '^usage: aipmt'; then
  pass "python -m aipmt --help"
else
  fail "python -m aipmt cassé"
fi

MODULES=$(run_installed "$PY" - <<'PYEOF' 2>&1
import importlib, pkgutil
import aipmt, aipmt.providers
manquants = []
for paquet in (aipmt, aipmt.providers):
    for info in pkgutil.iter_modules(paquet.__path__, paquet.__name__ + "."):
        try:
            importlib.import_module(info.name)
        except Exception as e:  # noqa: BLE001 — on veut le nom du module fautif
            manquants.append(f"{info.name} ({type(e).__name__})")
print(" ".join(manquants) if manquants else "OK")
PYEOF
)
if [[ "$MODULES" == "OK" ]]; then pass "tous les modules du paquet s'importent"; else fail "modules en échec : $MODULES"; fi

if [[ "$TRANSLATE" -eq 0 ]]; then
  skip "traduction réelle non demandée (--no-translation)"
  printf '\n'
  [[ $FAILURES -eq 0 ]] && { printf '\033[32m════ paquet sain : contrôles hors ligne au vert ════\033[0m\n'; exit 0; }
  printf '\033[31m════ %d contrôle(s) en échec ════\033[0m\n' "$FAILURES"; exit 1
fi

# --- traduction réelle -------------------------------------------------------
# Un document court mais qui porte tout ce qu'une traduction peut perdre en
# silence : bloc de code, code en ligne, lien, URL nue, tableau, citation.
cat > "$TMP/source.md" <<'MDEOF'
---
title: "Contrôle de paquet"
---

# Un document d'essai

Ce paragraphe porte un [lien](https://example.com/doc) et du `code en ligne`.
L'URL nue https://example.com/nue doit survivre elle aussi.

```python
print("ce bloc ne doit pas être traduit")
```

| Colonne | Valeur |
| ------- | ------ |
| une     | 1      |

> "A translation that loses a link is not a translation."
> — quelqu'un

Du **gras** pour finir.
MDEOF

FLAGS="${SMOKE_PROVIDER_FLAGS:-}"
if [[ -z "$FLAGS" ]]; then
  if [[ -n "${GOOGLE_API_KEY:-}${GEMINI_API_KEY:-}" ]]; then FLAGS="--use_gemini"
  elif [[ -n "${OPENAI_API_KEY:-}" ]]; then FLAGS=""
  else
    skip "traduction réelle sautée : aucune clé (GOOGLE_API_KEY, GEMINI_API_KEY ou OPENAI_API_KEY)"
    printf '\n'
    [[ $FAILURES -eq 0 ]] && { printf '\033[32m════ paquet sain, traduction non éprouvée ════\033[0m\n'; exit 0; }
    printf '\033[31m════ %d contrôle(s) en échec ════\033[0m\n' "$FAILURES"; exit 1
  fi
fi

# La clé vient de l'environnement courant, pas d'un `.env` du dépôt : le
# répertoire de travail est `/`, et le paquet n'y trouvera aucun fichier.
mkdir -p "$TMP/out"
# shellcheck disable=SC2086  # FLAGS porte plusieurs mots par construction
if run_installed timeout 600 "$BIN" --file "$TMP/source.md" --target_dir "$TMP/out" \
     --source_lang fr --target_lang en --force $FLAGS >"$TMP/translate.log" 2>&1; then
  SORTIE=$(find "$TMP/out" -name '*.md' | head -1)
  if [[ -z "$SORTIE" ]]; then
    fail "traduction sortie en 0 sans écrire de fichier — exactement ce que ce dépôt traque"
  else
    ECARTS=$(./venv/bin/python scripts/compare_structure.py "$TMP/source.md" "$SORTIE" 2>&1)
    if [[ "$ECARTS" == "structure identique" ]]; then
      pass "traduction réelle ($FLAGS) : structure identique à la source"
    else
      fail "traduction réelle ($FLAGS) : $ECARTS"
    fi
  fi
else
  fail "traduction réelle en échec (cf. $TMP/translate.log)"
  tail -3 "$TMP/translate.log" >&2
fi

printf '\n'
if [[ $FAILURES -eq 0 ]]; then
  printf '\033[32m════ paquet sain, de l'"'"'installation à la traduction ════\033[0m\n'
  exit 0
fi
printf '\033[31m════ %d contrôle(s) en échec ════\033[0m\n' "$FAILURES"
exit 1
