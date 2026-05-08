#!/usr/bin/env bash
# Garde-fou SAST via Opengrep (fork open-source de Semgrep CE).
# Couvre SSRF, injection de commandes, secrets hardcodés, path traversal,
# désérialisation non sûre, etc.
#
# Scope : translate.py + scripts/ (le code Python qui fait des appels externes).
# Severity : ERROR uniquement. Configs : security-audit + default + python.
#
# Si opengrep n'est pas dans le PATH, le hook se dégrade gracieusement
# (warn + exit 0). Install : curl -fsSL ... | sh ; binaire dans ~/.local/bin/.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

# Rend le binaire visible même si ~/.local/bin n'est pas dans PATH.
export PATH="$HOME/.local/bin:$PATH"

if ! command -v opengrep >/dev/null 2>&1; then
  echo ""
  echo "⚠ opengrep introuvable — SAST gate skip." >&2
  echo "  Install : curl -fsSL https://raw.githubusercontent.com/opengrep/opengrep/main/install.sh | sh" >&2
  # En CI, on échoue closed pour éviter de relâcher silencieusement le gate.
  # En local (hors CI), on tolère l'absence (skip non bloquant) le temps de l'install.
  if [[ -n "${CI:-}" || -n "${GITHUB_ACTIONS:-}" ]]; then
    echo "  Détecté CI → fail-closed (set CI=0 ou installer opengrep)." >&2
    exit 1
  fi
  exit 0
fi

exec opengrep scan \
  --config=p/security-audit \
  --config=p/default \
  --config=p/python \
  --severity=ERROR \
  --error \
  --exclude=venv \
  --exclude=traductions_ \
  --exclude=tests/fixtures \
  --exclude='*test*' \
  translate.py scripts/
