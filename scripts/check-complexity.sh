#!/usr/bin/env bash
# Garde-fou cyclomatic complexity via Lizard sur le code Python du repo.
# Threshold 12 au démarrage, durcissement progressif vers 8 visé.
#
# Scope : le module principal + scripts/. Les tests sont exclus (leur
# complexité mesure la couverture, pas une dette de design).

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh

# Le module principal est DANS le scope depuis que le refactor des providers l'a
# fait repasser sous le seuil : 158 fonctions, CCN moyen 3,3, **zéro dépassement
# à 12**. Le gate protège le fichier le plus exposé du dépôt contre une
# régression de complexité, au lieu de la découvrir via SonarCloud après le push.
SCOPE=(
  translate.py
  scripts/
)

# Vérification d'existence AVANT l'analyse, parce que `lizard` ignore un chemin
# absent SANS RIEN DIRE : `lizard -l python fichier-inexistant.py` sort en 0 en
# annonçant « 0 file analyzed ». Mesuré sur une copie où le module principal
# était déplacé : le gate passait de 158 fonctions / 2247 nloc à 3 fonctions /
# 34 nloc, avec rc=0 et une sortie de ZÉRO octet. 98 % de la couverture perdue,
# aucun signal — un renommage de fichier désarmait le gate en silence.
for path in "${SCOPE[@]}"; do
  [[ -e "$path" ]] || {
    echo "✗ scope introuvable : $path" >&2
    echo "  Lizard l'ignorerait en silence et le gate passerait au vert en" >&2
    echo "  n'analysant plus rien. Corriger SCOPE dans ce script." >&2
    exit 1
  }
done

# `-i 0` : bloque dès la 1re violation.
exec "$PY" -m lizard \
  --CCN 12 \
  --warnings_only \
  -i 0 \
  -l python \
  -x "tests/*" \
  -x "scripts/tests/*" \
  -x "translate.py.old" \
  "${SCOPE[@]}"
