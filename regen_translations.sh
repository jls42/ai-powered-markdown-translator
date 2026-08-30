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
  # Accepte GOOGLE_API_KEY (SDK historique) ET GEMINI_API_KEY (convention AI Studio),
  # cohérent avec _init_gemini_client() dans translate.py.
  local gemini_key="${GOOGLE_API_KEY:-${GEMINI_API_KEY:-}}"

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
    grok_cli)
      # Quota d'abonnement Grok. Jamais auto-détecté, comme codex.
      echo "--use_grok_cli --eco"
      echo "[regen] REGEN_PROVIDER=grok_cli → --use_grok_cli --eco (quota abonnement Grok)" >&2
      return
      ;;
    grok)
      echo "--use_grok --eco"
      echo "[regen] REGEN_PROVIDER=grok → --use_grok --eco (API xAI, facturé à l'usage)" >&2
      return
      ;;
    codex)
      # Jamais auto-détecté : consomme le quota de l'abonnement ChatGPT, ce qui
      # doit rester un choix explicite. Opt-in uniquement.
      echo "--use_codex --eco"
      echo "[regen] REGEN_PROVIDER=codex → --use_codex --eco (quota abonnement ChatGPT)" >&2
      return
      ;;
    "")
      # Pas d'override → tomber dans l'auto-détection ci-dessous
      ;;
    *)
      echo "[regen] WARNING: REGEN_PROVIDER='${REGEN_PROVIDER}' inconnu (attendu: gemini|openai|codex|grok|grok_cli), auto-détection" >&2
      ;;
  esac

  # Auto-détection : OpenAI par défaut, fallback Gemini si OPENAI absent.
  # IMPORTANT : si aucune clé valide, on échoue ici (exit 1) plutôt que d'émettre
  # un flag bidon — sinon les jobs en aval tomberaient en 401 silencieusement et
  # release.sh validerait "28 fichiers présents" contre des traductions stales.
  if [[ -n "$openai_key" ]] && [[ "$openai_key" != "$openai_placeholder" ]]; then
    echo "--eco"
    echo "[regen] OpenAI gpt-5.4-mini détecté → --eco (par défaut)" >&2
  elif [[ -n "$gemini_key" ]] && [[ "$gemini_key" != "$gemini_placeholder" ]] && [[ "$gemini_key" != "your-google-api-key" ]]; then
    echo "--use_gemini --eco"
    echo "[regen] WARNING: OPENAI_API_KEY absent → fallback Gemini Flash --use_gemini --eco" >&2
  else
    echo "[regen] ERROR: aucune clé API valide (OPENAI_API_KEY, GOOGLE_API_KEY, GEMINI_API_KEY) dans .env/env" >&2
    echo "[regen] ERROR: abort — définir au moins une clé valide avant de relancer" >&2
    exit 1
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

  if [[ ! -f translate.py ]]; then
    echo "ERROR: translate.py not found in $SCRIPT_DIR" >&2
    exit 1
  fi

  local provider_flags
  provider_flags=$(detect_provider)

  # REGEN_MODEL force un modèle précis, par-dessus le défaut du provider.
  # Utile pour monter en gamme sur un provider dont le mode --eco vise le
  # volume (ex: REGEN_MODEL=gpt-5.6-sol avec REGEN_PROVIDER=codex).
  if [[ -n "${REGEN_MODEL:-}" ]]; then
    provider_flags="$provider_flags --model ${REGEN_MODEL}"
    echo "[regen] REGEN_MODEL=${REGEN_MODEL} → override du modèle par défaut" >&2
  fi

  local max_jobs=10
  if [[ "$provider_flags" == *--use_grok_cli* ]]; then
    # Le quota Grok est un pool hebdomadaire PARTAGÉ avec Chat, Imagine et
    # Voice, et aucune commande ne permet de le lire : un regen complet peut
    # donc entamer l'usage conversationnel sans que rien ne le signale.
    local grok_bin="${GROK_BIN:-$(command -v grok || echo "${GROK_HOME:-$HOME/.grok}/bin/grok")}"
    if [[ ! -x "$grok_bin" ]]; then
      echo "[regen] ERROR: binaire Grok introuvable ($grok_bin) — installer le CLI ou définir GROK_BIN" >&2
      exit 1
    fi
    if ! "$grok_bin" models 2>/dev/null | grep -qi "logged in"; then
      echo "[regen] ERROR: Grok CLI non authentifié — lancer 'grok login'" >&2
      exit 1
    fi
    echo "[regen] ATTENTION : le quota Grok est partagé avec Chat/Imagine/Voice et n'est pas mesurable."
    max_jobs=2
  fi
  if [[ "$provider_flags" == *--use_codex* ]]; then
    # Le refresh du token Codex est rotatif et à usage unique : si plusieurs
    # jobs le déclenchent en même temps, tous sauf un échouent et la session
    # `codex login` de l'utilisateur est invalidée. On le rafraîchit donc une
    # fois, séquentiellement, avant d'ouvrir le parallélisme — après quoi le
    # token est frais pour toute la durée du regen.
    echo "[regen] Codex : warm-up du token (évite les refresh concurrents)..."
    if ! codex login status >/dev/null 2>&1; then
      echo "[regen] ERROR: Codex CLI non authentifié — lancer 'codex login'" >&2
      exit 1
    fi
    # Chaque tour Codex consomme un message du plan et dure ~45s : on limite la
    # concurrence pour ne pas déclencher de rate limit sur la fenêtre 5h.
    max_jobs=4
  fi
  local langs="ar de en es hi it ja ko nl pl pt ro sv zh"
  # Volontairement global, pas `local` : le trap EXIT s'exécute APRÈS la sortie
  # de main(), où une variable locale n'existe plus. Avec `set -u`, le trap
  # levait alors "failed_log: unbound variable" et faisait sortir le script en 1
  # même quand les 28 traductions étaient correctes — ce qui interrompait
  # `release.sh --auto` (set -e) juste après la régénération.
  failed_log=$(mktemp)
  trap 'if [[ -n "${failed_log:-}" ]]; then rm -f "$failed_log"; fi' EXIT

  # Timeout par job : si un appel API hang, le job sort en 124 et est consigné
  # comme échec plutôt que de figer toute la release indéfiniment.
  local job_timeout="${REGEN_JOB_TIMEOUT:-600}"

  run_one() {
    local file="$1" lang="$2"
    # provider_flags et force_flag sont visibles ici via dynamic scoping bash
    # shellcheck disable=SC2086
    if ! timeout "$job_timeout" python translate.py --file "$file" --target_dir . \
        --source_lang fr --target_lang "$lang" \
        $provider_flags --add_translation_note $force_flag; then
      echo "$file -> $lang" >> "$failed_log"
    fi
  }

  for lang in $langs; do
    echo "[README] -> $lang"
    run_one README.md "$lang" &

    echo "[CHANGELOG] -> $lang"
    run_one CHANGELOG.md "$lang" &

    while [[ "$(jobs -r | wc -l)" -ge "$max_jobs" ]]; do
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
