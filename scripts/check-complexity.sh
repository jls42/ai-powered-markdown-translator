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

# `-i 0` : bloque dès la 1re violation.
#
# translate.py est DANS le scope depuis que le refactor des providers l'a fait
# repasser sous le seuil : 155 fonctions, CCN moyen 3,3, **zéro dépassement à
# 12** (le maximum est 7). L'exclusion datait d'une époque où quatre fonctions
# dépassaient, et CLAUDE.md prévoyait explicitement de la lever à cette
# condition. Le gate protège désormais le fichier le plus exposé du dépôt
# contre une régression de complexité, au lieu de la découvrir via SonarCloud
# après le push.
exec "$PY" -m lizard \
  --CCN 12 \
  --warnings_only \
  -i 0 \
  -l python \
  -x "tests/*" \
  -x "scripts/tests/*" \
  -x "translate.py.old" \
  translate.py \
  scripts/
