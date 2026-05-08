#!/usr/bin/env bash
# Garde-fou cyclomatic complexity via Lizard sur le code Python du repo.
# Threshold 12 au démarrage, durcissement progressif vers 8 visé.
#
# Scope volontairement réduit à scripts/ : translate.py a une baseline
# au-dessus du seuil sur quelques fonctions et sera réintégré au scope
# une fois refactoré. Les tests sont exclus (complexité = couverture, pas
# dette de design).

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh

# `-i 0` : bloque dès la 1re violation. Quand translate.py repassera sous
# le seuil, l'ajouter au scope (pas à `-x`).
exec "$PY" -m lizard \
  --CCN 12 \
  --warnings_only \
  -i 0 \
  -l python \
  -x "tests/*" \
  -x "scripts/tests/*" \
  -x "translate.py.old" \
  scripts/
