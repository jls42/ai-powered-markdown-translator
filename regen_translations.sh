#!/bin/bash
set -euo pipefail
# Regenerate README and CHANGELOG translations in parallel.
# Concurrence : 10 jobs par défaut, 4 pour Codex, 2 pour Grok CLI (quotas
# d'abonnement, cf. main()).
#
# Usage:
#   ./regen_translations.sh           # skip si fichier existe
#   ./regen_translations.sh --force   # réécrit les fichiers existants
#
# Provider auto-détecté via detect_provider, dans cet ordre :
#   - OPENAI_API_KEY valide (env ou .env)  → OpenAI --eco (gpt-5.6-luna)
#   - sinon GOOGLE/GEMINI_API_KEY valide   → Gemini Flash (--use_gemini --eco)
#   - sinon                                → abort (aucune clé exploitable)
#
# REGEN_PROVIDER force le choix : gemini | openai | codex | grok | grok_cli | opencode.
# REGEN_MODEL force un modèle par-dessus le défaut du provider (obligatoire
# avec opencode, au format provider/modèle).

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Détection du provider de traduction selon les clés d'API disponibles.
# Stdout : flags à injecter dans `python -m aipmt` (ex: "--eco" ou "--use_gemini --eco").
# Stderr : message de log (info ou warning).
# Le caller utilise: PROVIDER_FLAGS=$(detect_provider)
#
# Priorité par défaut : OpenAI en --eco. Fallback Gemini Flash si
# OPENAI_API_KEY absente/placeholder mais GOOGLE_API_KEY valide. L'utilisateur
# peut forcer Gemini avec REGEN_PROVIDER=gemini./regen_translations.sh.
# Charge .env si présent. set -a/+a exporte toutes les variables assignées pour
# qu'elles soient héritées par les sous-processus (python -m aipmt).
#
# Appelé DEUX fois volontairement : depuis detect_provider (que les tests
# sourcent et invoquent isolément) et depuis main(). detect_provider est
# appelée en substitution de commande — donc dans un sous-shell — si bien que
# ses exports ne remontaient pas : un GROK_BIN ou un REGEN_MODEL défini dans
# .env restait invisible aux lectures faites dans main(), qui concluait
# « binaire Grok introuvable » sur une configuration pourtant correcte.
# Sourcer un fichier d'affectations deux fois est idempotent.
load_env() {
  if [[ -f .env ]]; then
    set -a
    # shellcheck disable=SC1091
    source .env
    set +a
  fi
}

detect_provider() {
  load_env

  # Placeholders exacts définis dans le module (DEFAULT_*_API_KEY)
  local openai_placeholder="votre-cle-api-openai-par-defaut"
  local gemini_placeholder="votre-cle-api-gemini-par-defaut"
  local openai_key="${OPENAI_API_KEY:-}"
  # Accepte GOOGLE_API_KEY (SDK historique) ET GEMINI_API_KEY (convention AI Studio),
  # cohérent avec _init_gemini_client() dans le module.
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
      echo "[regen] REGEN_PROVIDER=openai → --eco (OpenAI, modèle éco courant)" >&2
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
    opencode)
      # Routeur open source vers le fournisseur configuré dans OpenCode (local,
      # gratuit, abonnement ou clé). Aucun défaut n'est choisi à la place de
      # l'utilisateur, ni ici ni dans le module : REGEN_MODEL est obligatoire.
      if [[ -z "${REGEN_MODEL:-}" ]]; then
        echo "[regen] ERROR: REGEN_PROVIDER=opencode exige REGEN_MODEL=provider/modèle (ex. ollama/qwen2.5:7b, opencode/mimo-v2.5-free)" >&2
        exit 1
      fi
      echo "--use_opencode"
      echo "[regen] REGEN_PROVIDER=opencode → --use_opencode --model ${REGEN_MODEL} (routeur OpenCode)" >&2
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
      echo "[regen] WARNING: REGEN_PROVIDER='${REGEN_PROVIDER}' inconnu (attendu: gemini|openai|codex|grok|grok_cli|opencode), auto-détection" >&2
      ;;
  esac

  # Auto-détection : OpenAI par défaut, fallback Gemini si OPENAI absent.
  # IMPORTANT : si aucune clé valide, on échoue ici (exit 1) plutôt que d'émettre
  # un flag bidon — sinon les jobs en aval tomberaient en 401 silencieusement et
  # release.sh validerait "28 fichiers présents" contre des traductions stales.
  if [[ -n "$openai_key" ]] && [[ "$openai_key" != "$openai_placeholder" ]]; then
    echo "--eco"
    echo "[regen] OpenAI détecté (OPENAI_API_KEY) → --eco (par défaut)" >&2
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

  # Avant toute lecture de GROK_BIN / GROK_HOME / REGEN_MODEL ci-dessous :
  # detect_provider tourne dans un sous-shell et ne peut pas les exporter ici.
  load_env

  if [[ ! -f src/aipmt/translate.py ]]; then
    echo "ERROR: src/aipmt/translate.py not found in $SCRIPT_DIR" >&2
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
  if [[ "$provider_flags" == *--use_opencode* ]]; then
    # Le binaire est cherché comme dans le module : OPENCODE_BIN, le PATH, puis
    # l'emplacement de l'installeur officiel. Pas de contrôle d'auth : il n'y a
    # rien d'unique à contrôler (Ollama ne demande rien, Zen sert des modèles
    # gratuits sans compte), un fournisseur absent échoue au premier segment.
    local opencode_bin="${OPENCODE_BIN:-$(command -v opencode || echo "$HOME/.opencode/bin/opencode")}"
    if [[ ! -x "$opencode_bin" ]]; then
      echo "[regen] ERROR: binaire OpenCode introuvable ($opencode_bin) — l'installer ou définir OPENCODE_BIN" >&2
      exit 1
    fi
    # Backend inconnu d'ici : un GPU local sérialise de toute façon, et deux
    # requêtes simultanées sur un modèle gratuit Zen ont été mesurées bloquées
    # sans réponse pendant 5 minutes là où chacune seule répond en 40 s.
    max_jobs=2
  fi
  if [[ "$provider_flags" == *--use_codex* ]]; then
    # Contrôle d'authentification avant d'ouvrir le parallélisme, pour échouer
    # en 2 s plutôt qu'après plusieurs fichiers.
    #
    # Ce n'est PAS un warm-up de token, contrairement à ce qu'affirmait la
    # version précédente : mesuré, `codex login status` ne touche pas à
    # ~/.codex/auth.json (mtime et taille inchangés), son aide dit « Show login
    # status ». Le risque de refresh concurrents — le token est rotatif et à
    # usage unique — reste donc entier, et c'est la raison de max_jobs=4 plutôt
    # qu'un simple contrôle d'auth. Un vrai warm-up demanderait une traduction
    # séquentielle avant d'ouvrir le parallélisme (coût : 1 message de quota).
    #
    # Le binaire est résolu comme dans le module (CODEX_BIN puis PATH) :
    # invoquer `codex` nu faisait échouer le regen avec « non authentifié » sur
    # un poste où seul CODEX_BIN est défini — un diagnostic trompeur.
    local codex_bin="${CODEX_BIN:-$(command -v codex || true)}"
    if [[ -z "$codex_bin" || ! -x "$codex_bin" ]]; then
      echo "[regen] ERROR: binaire Codex introuvable (${codex_bin:-aucun}) — l'installer ou définir CODEX_BIN" >&2
      exit 1
    fi
    echo "[regen] Codex : contrôle d'authentification..."
    if ! "$codex_bin" login status >/dev/null 2>&1; then
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
    if ! PYTHONPATH="$SCRIPT_DIR/src" timeout "$job_timeout" python -m aipmt \
        --file "$file" --target_dir . \
        --source_lang fr --target_lang "$lang" \
        $provider_flags --add_translation_note $force_flag; then
      echo "$file -> $lang" >> "$failed_log"
    fi
  }

  # La garde est AVANT chaque lancement, et non après la paire : placée après,
  # elle laissait relancer deux jobs dès qu'il n'en restait qu'un, soit un pic
  # mesuré de 3 pour max_jobs=2. Sur Grok, dont le quota hebdomadaire est
  # partagé avec Chat/Imagine/Voice et non mesurable, dépasser de 50 % la borne
  # que le script s'impose n'est pas anodin.
  for lang in $langs; do
    while [[ "$(jobs -r | wc -l)" -ge "$max_jobs" ]]; do sleep 1; done
    echo "[README] -> $lang"
    run_one README.md "$lang" &

    while [[ "$(jobs -r | wc -l)" -ge "$max_jobs" ]]; do sleep 1; done
    echo "[CHANGELOG] -> $lang"
    run_one CHANGELOG.md "$lang" &
  done

  wait
  echo "=== DONE ==="

  # Le compte était affiché sans jamais être comparé à 28 : un fichier manquant
  # passait donc inaperçu. Le motif exclut aussi les artefacts `--include_model`
  # (README-en-gpt-5.6-luna.md), qui gonflaient le total sans être des cibles.
  local count expected=28
  count=$(find . -maxdepth 1 -type f \
    \( -name 'README-??.md' -o -name 'CHANGELOG-??.md' \) | wc -l)
  echo "Fichiers de traduction présents: $count/$expected"

  if [[ -s "$failed_log" ]]; then
    echo "ERROR: certains fichiers ont échoué :" >&2
    cat "$failed_log" >&2
    exit 1
  fi
  if [[ "$count" -ne "$expected" ]]; then
    echo "ERROR: $count fichiers de traduction au lieu de $expected" >&2
    exit 1
  fi
}

# Si exécuté directement (pas sourcé), lancer main.
# Permet aux tests de sourcer ce fichier pour tester detect_provider isolément.
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main "$@"
fi
