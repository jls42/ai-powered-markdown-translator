#!/usr/bin/env bash
# Découvre les tests dans tests/ ET scripts/tests/.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh
"$PY" -m unittest discover -s tests/ -v
"$PY" -m unittest discover -s scripts/tests/ -v
