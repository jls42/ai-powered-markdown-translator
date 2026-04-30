#!/usr/bin/env bash
# pip-audit avec capture sécurisée (tempfiles, pas de pipe direct).
# Classifie les erreurs réseau côté shell AVANT de parser le JSON, sinon
# un JSON vide tomberait sur parse-error et bloquerait à tort.
#
# Mode reporting initial (warn + exit 0 sur vulnerable:N). À durcir en
# bloquant (exit 1) après une PR de bump des deps obsolètes.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# shellcheck source=scripts/_venv_python.sh
source scripts/_venv_python.sh

audit_json="$(mktemp)"
audit_err="$(mktemp)"
trap 'rm -f "$audit_json" "$audit_err"' EXIT

# pip-audit retourne non-zéro sur vulns détectées → on capture sans
# laisser set -e nous tuer.
status=0
"$PY" -m pip_audit --format=json --requirement requirements.txt \
  >"$audit_json" 2>"$audit_err" || status=$?

# Classifier les erreurs réseau / PyPI down côté shell AVANT le parse JSON.
if grep -qiE '(connection refused|timeout|getaddrinfo|name or service not known|temporary failure|resolve|unreachable|ssl: |proxy|HTTPSConnectionPool)' "$audit_err"; then
  echo "⚠ pip-audit transport error (skip non bloquant) :" >&2
  cat "$audit_err" >&2
  exit 0
fi

# Si pip-audit a explosé sans produire de JSON (ni vulns ni erreur réseau)
if [[ ! -s "$audit_json" ]]; then
  echo "pip-audit n'a produit aucune sortie JSON (status=$status) :" >&2
  cat "$audit_err" >&2
  exit 1
fi

verdict="$("$PY" scripts/audit_verdict.py < "$audit_json")"

case "$verdict" in
  ok)
    exit 0
    ;;
  vulnerable:*)
    echo "pip-audit: $verdict (mode reporting initial — non bloquant)" >&2
    cat "$audit_err" >&2
    # Mode reporting initial : warn + exit 0. À durcir après PR de bump.
    exit 0
    ;;
  *)
    echo "pip-audit verdict inattendu : $verdict (status=$status)" >&2
    cat "$audit_err" >&2
    exit 1
    ;;
esac
