#!/usr/bin/env bash
# Découvre les tests dans tests/ ET scripts/tests/.
# On agrège les rc pour que la 2ème suite tourne même si la 1ère échoue,
# sinon le hook pre-push masquerait silencieusement les régressions de
# scripts/tests/ derrière un échec dans tests/.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 2
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh
rc=0
"$PY" -m unittest discover -s tests/ -v || rc=$?
"$PY" -m unittest discover -s scripts/tests/ -v || rc=$?
exit "$rc"
