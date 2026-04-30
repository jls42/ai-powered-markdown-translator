#!/bin/bash
set -euo pipefail
# Regenerate README and CHANGELOG translations in parallel (10 jobs max).
#
# Usage:
#   ./regen_translations.sh           # skip si fichier existe
#   ./regen_translations.sh --force   # réécrit les fichiers existants
#
# Provider auto-détecté via detect_provider :
#   - GOOGLE_API_KEY valide (env ou .env)  → Gemini Flash (--use_gemini --eco)
#   - sinon                                → fallback OpenAI gpt-5.4-mini (--eco) avec WARNING

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Détection du provider de traduction selon les clés d'API disponibles.
# Stdout : flags à injecter dans `python translate.py` (ex: "--eco" ou "--use_gemini --eco").
# Stderr : message de log (info ou warning).
# Le caller utilise: PROVIDER_FLAGS=$(detect_provider)
#
# Priorité par défaut : OpenAI gpt-5.4-mini (--eco). Fallback Gemini Flash si
# OPENAI_API_KEY absente/placeholder mais GOOGLE_API_KEY valide. L'utilisateur
# peut forcer Gemini avec REGEN_PROVIDER=gemini./regen_translations.sh.
detect_provider() {
  # Charge .env si présent. set -a/+a exporte toutes les variables assignées
  # pour qu'elles soient héritées par les sous-processus (python translate.py).
  if [[ -f .env ]]; then
    set -a
    # shellcheck disable=SC1091
    source .env
    set +a
  fi

  # Placeholders exacts définis dans translate.py (DEFAULT_*_API_KEY)
  local openai_placeholder="votre-cle-api-openai-par-defaut"
  local gemini_placeholder="votre-cle-api-gemini-par-defaut"
  local openai_key="${OPENAI_API_KEY:-}"
  local gemini_key="${GOOGLE_API_KEY:-}"

  # Override explicite via REGEN_PROVIDER=gemini ou REGEN_PROVIDER=openai
  case "${REGEN_PROVIDER:-}" in
    gemini)
      echo "--use_gemini --eco"
      echo "[regen] REGEN_PROVIDER=gemini → --use_gemini --eco (Gemini Flash)" >&2
      return
      ;;
    openai)
      echo "--eco"
      echo "[regen] REGEN_PROVIDER=openai → --eco (OpenAI gpt-5.4-mini)" >&2
      return
      ;;
  esac

  # Auto-détection : OpenAI par défaut, fallback Gemini si OPENAI absent
  if [[ -n "$openai_key" ]] && [[ "$openai_key" != "$openai_placeholder" ]]; then
    echo "--eco"
    echo "[regen] OpenAI gpt-5.4-mini détecté → --eco (par défaut)" >&2
  elif [[ -n "$gemini_key" ]] && [[ "$gemini_key" != "$gemini_placeholder" ]] && [[ "$gemini_key" != "your-google-api-key" ]]; then
    echo "--use_gemini --eco"
    echo "[regen] WARNING: OPENAI_API_KEY absent → fallback Gemini Flash --use_gemini --eco" >&2
  else
    echo "--eco"
    echo "[regen] ERROR: ni OPENAI_API_KEY ni GOOGLE_API_KEY valide dans .env/env" >&2
  fi
}

main() {
  cd "$SCRIPT_DIR"

  local force_flag=""
  if [[ "${1:-}" == "--force" ]]; then
    force_flag="--force"
    echo "[regen] --force activé : les traductions existantes seront réécrites"
  fi

  # shellcheck disable=SC1091
  source venv/bin/activate

  if [ ! -f translate.py ]; then
    echo "ERROR: translate.py not found in $SCRIPT_DIR" >&2
    exit 1
  fi

  local provider_flags
  provider_flags=$(detect_provider)

  local max_jobs=10
  local langs="ar de en es hi it ja ko nl pl pt ro sv zh"
  local failed_log
  failed_log=$(mktemp)
  trap 'rm -f "$failed_log"' EXIT

  run_one() {
    local file="$1" lang="$2"
    # provider_flags et force_flag sont visibles ici via dynamic scoping bash
    # shellcheck disable=SC2086
    if ! python translate.py --file "$file" --target_dir . --source_lang fr --target_lang "$lang" \
        $provider_flags --add_translation_note $force_flag; then
      echo "$file -> $lang" >> "$failed_log"
    fi
  }

  for lang in $langs; do
    echo "[README] -> $lang"
    run_one README.md "$lang" &

    echo "[CHANGELOG] -> $lang"
    run_one CHANGELOG.md "$lang" &

    while [ "$(jobs -r | wc -l)" -ge "$max_jobs" ]; do
      sleep 1
    done
  done

  wait
  echo "=== DONE ==="

  local count
  count=$(find . -maxdepth 1 -type f \( -name 'README-*.md' -o -name 'CHANGELOG-*.md' \) | wc -l)
  echo "Fichiers de traduction présents: $count"

  if [[ -s "$failed_log" ]]; then
    echo "ERROR: certains fichiers ont échoué :" >&2
    cat "$failed_log" >&2
    exit 1
  fi
}

# Si exécuté directement (pas sourcé), lancer main.
# Permet aux tests de sourcer ce fichier pour tester detect_provider isolément.
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main "$@"
fi
