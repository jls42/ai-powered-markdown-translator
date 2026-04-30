#!/usr/bin/env bash
# Wrapper mypy via venv (mode lax au démarrage, cf. pyproject.toml).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh
exec "$PY" -m mypy translate.py tests/ scripts/
