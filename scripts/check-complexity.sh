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

# MODE STRICT : `-i 0` bloque sur la première violation. À durcir à --CCN 8
# une fois les fonctions de translate.py refactorées (TODO documenté dans
# CLAUDE.md, section Quality / pre-commit).
exec "$PY" -m lizard \
  --CCN 12 \
  --warnings_only \
  -i 0 \
  -l python \
  -x "tests/*" \
  -x "scripts/tests/*" \
  -x "translate.py.old" \
  translate.py scripts/
