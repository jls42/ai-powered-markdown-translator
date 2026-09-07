#!/usr/bin/env bash
# Garde-fou cyclomatic complexity via Lizard sur le code Python du repo.
# Threshold 12 au démarrage, durcissement progressif vers 8 visé.
#
# Scope : src/ + scripts/. Les tests sont exclus (leur complexité mesure la
# couverture, pas une dette de design).

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh

# Le paquet entier est DANS le scope (192 fonctions, CCN moyen 3,5, **zéro
# dépassement à 12**) : le gate protège le code le plus exposé du dépôt contre
# une régression de complexité, au lieu de la découvrir via SonarCloud après le
# push. Des RÉPERTOIRES, pas des fichiers : un découpage du module principal ne
# doit pas pouvoir sortir du périmètre en silence — c'est le plancher ci-dessous
# qui rend cette promesse vérifiable.
SCOPE=(
  src/
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

# Plancher fail-closed sur le NOMBRE de fonctions analysées. L'existence d'un
# répertoire ne prouve pas qu'il contient quelque chose : `[[ -e src/ ]]` est
# vrai sur un répertoire vide, et lizard sort alors en 0 sans rien dire. Lu par
# l'API Python parce que `--warnings_only` n'imprime AUCUNE ligne de synthèse
# quand tout est vert (mesuré : zéro octet), donc rien à parser. 195 fonctions
# mesurées le 2026-09-07 (192 dans src/aipmt, 3 dans scripts/).
"$PY" - "${SCOPE[@]}" <<'PYEOF' || exit 1
import sys

import lizard

FLOOR = 185
files = lizard.analyze(
    sys.argv[1:], exclude_pattern=["tests/*", "scripts/tests/*", "translate.py.old"]
)
count = sum(len(f.function_list) for f in files)
if count < FLOOR:
    sys.exit(
        f"✗ {count} fonctions dans le périmètre Lizard (plancher {FLOOR}) : le périmètre "
        "s'est effondré, le gate ne protégerait plus rien. Corriger SCOPE dans ce script."
    )
print(f"  périmètre Lizard : {count} fonctions (plancher {FLOOR})")
PYEOF

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
