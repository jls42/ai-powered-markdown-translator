#!/usr/bin/env bash
# Hook pre-commit : le découpage de src/aipmt/translate.py reste un déplacement
# pur (cf. scripts/check-split-purity.py). Outil temporaire, retiré avec la PR
# qui suit le découpage.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh
exec "$PY" scripts/check-split-purity.py "$@"
