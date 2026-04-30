# shellcheck shell=bash
# Source-only. Exporte $PY pointant sur l'interpréteur du venv.
# Pas de shebang : ce fichier ne doit jamais être exécuté directement.

# Guard early : refuse l'exécution directe (évite SC2317 sur return||exit)
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  echo "error: source this file; do not execute it directly" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -x "${VIRTUAL_ENV:-$ROOT/venv}/bin/python" ]]; then
  PY="${VIRTUAL_ENV:-$ROOT/venv}/bin/python"
  export PY
else
  echo "error: venv introuvable à ${VIRTUAL_ENV:-$ROOT/venv}" >&2
  echo "       Lance: python3 -m venv venv && source venv/bin/activate \\" >&2
  echo "             && pip install -r requirements.txt -r requirements-dev.txt" >&2
  return 1
fi
