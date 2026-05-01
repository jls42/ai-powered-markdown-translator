#!/usr/bin/env bash
# Garde-fou cyclomatic complexity via Lizard sur le code Python du repo.
#
# Threshold : 12 au démarrage (à durcir progressivement vers 8 — Codacy/EurekAI).
# Scope : translate.py + scripts/*.py (les tests sont exclus, leur complexité
# reflète la couverture, pas une dette de design).
#
# Lizard est installé dans le venv via requirements-dev.txt.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh

# MODE STRICT : `-i 0` bloque sur la première violation. CCN 12 au démarrage,
# durcir à 8 progressivement (cohérent Codacy/EurekAI).
#
# translate.py est temporairement EXCLU **par scope** : la commande ne reçoit
# que `scripts/` en argument. La baseline de translate.py dépasse 12 sur
# 4 fonctions (translate=25, translate_markdown_file=47, translate_directory=21,
# main=32). Le refactor est planifié dans une PR dédiée (TODO CLAUDE.md).
# Quand translate.py repassera sous le seuil, ajouter `translate.py` au scope
# (pas à `-x`). Le gate s'applique strictement aux nouveaux scripts pour
# empêcher la régression.
exec "$PY" -m lizard \
  --CCN 12 \
  --warnings_only \
  -i 0 \
  -l python \
  -x "tests/*" \
  -x "scripts/tests/*" \
  -x "translate.py.old" \
  scripts/
