"""Provider Codex : le CLI `codex` officiel sur le quota de l'abonnement ChatGPT.

Aucune facturation à l'usage. L'authentification est déléguée au CLI (jamais
lire ni écrire `~/.codex/auth.json`, dont le jeton est rotatif), les clés API
sont retirées de l'environnement du sous-processus, et un code retour nul ne
prouve rien : c'est la sortie JSONL et le fichier `-o` qui font foi.
"""

import json
import os
import shutil
import subprocess  # nosec B404 — pilote le CLI Codex, cf. _codex_preflight
import sys
import tempfile
from dataclasses import dataclass, field

from .base import (
    _CliCallError,
    _codex_reject_ci_environment,
    _codex_run_process,
    _retry_on_rate_limit,
    _stderr_tail,
    _strip_secret_env,
)
from .openai import _resolve_reasoning_effort

DEFAULT_MODEL_CODEX = "gpt-5.6-sol"


# Luna = modèle "fast, high-volume" du plan ChatGPT : 250-2000 messages/5h sur
# Plus contre 10-100 pour Sol. C'est le seul choix raisonnable pour du batch.
ECO_MODEL_CODEX = "gpt-5.6-luna"


# --- Provider Codex (CLI officiel, quota d'abonnement ChatGPT) --------------
# On pilote le binaire `codex` en mode non-interactif plutôt que d'appeler une
# API : c'est la seule voie documentée comme disponible sur un plan ChatGPT
# (learn.chatgpt.com/docs/pricing : "Codex SDK, `codex exec`, and scriptable
# workflows" → plus: available). Les tokens de ~/.codex/auth.json n'authentifient
# PAS les appels API Platform et ne sont jamais lus ici : l'auth et le refresh
# restent entièrement gérés par le CLI.
CODEX_TIMEOUT = int(os.getenv("CODEX_TIMEOUT", "600"))


# La famille gpt-5.6 est commune au CLI Codex et à l'API Platform, mais côté
# compte ChatGPT le serveur applique une allowlist plus étroite : un modèle
# valide sur l'API peut être refusé ici par un 400 ("model is not supported
# when using Codex with a ChatGPT account"), sans validation locale préalable.
CODEX_MODEL_PREFIXES = ("gpt-5.6-",)


# Variables retirées de l'env du sous-processus : sans ça, une clé API présente
# dans .env peut faire basculer Codex en facturation à l'usage — exactement ce
# que ce provider existe pour éviter.
CODEX_STRIPPED_ENV_VARS = ("OPENAI_API_KEY", "CODEX_API_KEY")


# Contrat imposé en plus du prompt système : `codex exec` est un agent, pas une
# API de complétion. Sans ça il peut préfixer sa réponse d'un commentaire.
CODEX_AGENT_CONTRACT = (
    "\n\nIMPORTANT (mode non-interactif) : ne lis aucun fichier, n'exécute aucune "
    "commande, ne pose aucune question. Le contenu à traduire est fourni dans le "
    "bloc <stdin>. Réponds UNIQUEMENT par le contenu traduit, sans préambule, "
    "sans commentaire, et sans l'entourer d'un bloc de code."
)


@dataclass
class _CodexClient:
    """« Client » du provider Codex. Il n'y a pas de session HTTP à tenir : on
    porte la config d'invocation du CLI. L'auth vit dans ~/.codex et n'est
    jamais lue ni écrite ici — le CLI gère le refresh (le refresh_token est à
    usage unique, toute manipulation externe casserait la session utilisateur)."""

    binary: str
    timeout: int = CODEX_TIMEOUT
    reasoning_effort: str = "medium"
    max_attempts: int = 3
    backoff_seconds: float = 30.0
    env_overrides: dict = field(default_factory=dict)


def _codex_env_base():
    """Environnement expurgé pour tout sous-processus Codex, préflight compris.

    Extrait de `_codex_env` parce que `_codex_preflight` appelait
    `subprocess.run` SANS `env=` : il transmettait donc `os.environ` entier —
    donc tout le `.env` chargé par `load_dotenv` — au binaire Codex. Mesuré :
    sept secrets atteignaient le préflight, contre zéro pour son homologue Grok
    qui passait bien `env=_grok_env()`. L'invariant que `_strip_secret_env`
    existe pour tenir était contredit à quelques lignes de là.
    """
    env = os.environ.copy()
    for var in CODEX_STRIPPED_ENV_VARS:
        env.pop(var, None)
    _strip_secret_env(env)
    # OPENAI_BASE_URL n'est pas un secret mais réoriente le trafic : hérité d'un
    # `.env`, il ferait sortir la traduction du chemin d'abonnement sans signal.
    env.pop("OPENAI_BASE_URL", None)
    return env


def _codex_env(client):
    """Env du sous-processus, privé des clés API : la raison d'être de ce
    provider est de consommer l'abonnement ChatGPT, pas de facturer à l'usage.
    Une clé laissée dans l'env ferait basculer Codex en mode payant sans
    signal visible."""
    env = _codex_env_base()
    # Après le stripping : un override explicite doit rester souverain, mais
    # aucun appelant n'en fournit aujourd'hui.
    env.update(client.env_overrides)
    return env


def _codex_argv(client, args, prompt, workdir, output_file):
    """Argv de `codex exec`. `--ignore-user-config` neutralise les serveurs MCP
    et la personality de l'utilisateur : ils gonfleraient le contexte de chaque
    tour, donc la consommation de quota, sans servir la traduction."""
    return [
        client.binary,
        "exec",
        prompt + CODEX_AGENT_CONTRACT,
        "--cd",
        workdir,
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--color",
        "never",
        "--json",
        "-o",
        output_file,
        "-m",
        args.model,
        "-c",
        f"model_reasoning_effort={client.reasoning_effort}",
        "-c",
        "approval_policy=never",
    ]


def _codex_run(client, argv, segment):
    return _codex_run_process(
        argv, segment, client.timeout, _codex_env(client), "Codex", argv[argv.index("-m") + 1]
    )


def _codex_unwrap_error(payload):
    """Déplie le payload d'erreur, double-encodé par le CLI (une chaîne JSON
    dans le champ `message`). Renvoie un dict, éventuellement vide."""
    message = payload.get("message", payload) if isinstance(payload, dict) else payload
    if isinstance(message, str):
        try:
            message = json.loads(message)
        except (ValueError, TypeError):
            return {"message": message}
    return message if isinstance(message, dict) else {"message": str(message)}


def _codex_error_from_events(stdout):
    """Extrait le premier événement d'échec du JSONL. Renvoie `None` si le tour
    s'est bien terminé. Nécessaire car `codex exec` peut sortir en 0 tout en
    ayant émis un `turn.failed`."""
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") in ("error", "turn.failed"):
            return _codex_unwrap_error(event.get("error", event))
    return None


def _codex_is_rate_limited(error):
    """Classe sur la structure du payload, pas sur des sous-chaînes : le mot
    « quota » apparaît aussi bien dans un 429 récupérable que dans un
    `insufficient_quota` définitif, et confondre les deux rend le back-off
    soit inatteignable, soit infini."""
    if not error:
        return False
    if error.get("status") == 429:
        return True
    kind = error.get("error", {}) if isinstance(error.get("error"), dict) else {}
    return kind.get("type") == "rate_limit_exceeded"


def _codex_describe_error(error, returncode, stderr):
    """Message d'erreur exploitable : on cite le modèle et le détail serveur,
    parce que la cause la plus fréquente est un slug de modèle refusé pour un
    compte ChatGPT — un cas invisible sans le payload."""
    if error:
        detail = error.get("error", error)
        detail = detail.get("message", detail) if isinstance(detail, dict) else detail
        return f"Codex CLI a échoué : {detail}"
    return f"Codex CLI a quitté avec le code {returncode} : {_stderr_tail(stderr)}"


def _codex_read_output(output_file, args):
    """Lit le message final écrit par `-o`. Son absence avec un code retour 0
    est une silent failure : sans cette garde, le segment repartirait vide."""
    if not os.path.exists(output_file):
        raise RuntimeError(
            f"Codex CLI a retourné 0 sans écrire de message final (model={args.model}). "
            "Sortie inexploitable."
        )
    with open(output_file, encoding="utf-8") as f:
        return f.read()


def _codex_attempt(client, args, prompt, segment):
    """Une invocation complète du CLI, dans un workdir jetable pour qu'aucune
    action de l'agent ne puisse toucher au dépôt."""
    with tempfile.TemporaryDirectory(prefix="translate-codex-") as workdir:
        output_file = os.path.join(workdir, "codex-last-message.md")
        argv = _codex_argv(client, args, prompt, workdir, output_file)
        returncode, stdout, stderr = _codex_run(client, argv, segment)
        error = _codex_error_from_events(stdout)
        if returncode != 0 or error:
            raise _CodexCallError(
                _codex_describe_error(error, returncode, stderr),
                rate_limited=_codex_is_rate_limited(error),
            )
        return _codex_read_output(output_file, args)


class _CodexCallError(_CliCallError):
    """Échec d'une invocation du CLI Codex (max_retries=0 côté CLI)."""


def _call_codex(client, args, prompt, segment):
    """Traduit un segment via le CLI Codex, avec back-off sur rate limit."""
    return _retry_on_rate_limit(
        "Codex", client, lambda: _codex_attempt(client, args, prompt, segment)
    )


def _resolve_codex_binary():
    """Chemin du binaire `codex`, ou `None` s'il est introuvable.

    Trois sources, dans l'ordre : `CODEX_BIN` explicite, le `PATH`, puis le
    package Python officiel `openai-codex-cli-bin`. Ce dernier évite d'imposer
    une installation npm globale à un projet Python : `pip install
    openai-codex-cli-bin` suffit alors à rendre `--use_codex` utilisable.
    Il n'est pas dans requirements.txt à dessein — le binaire pèse ~250 Mo, ce
    qui serait imposé à tous les utilisateurs pour un provider optionnel."""
    explicit = os.getenv("CODEX_BIN")
    if explicit:
        return shutil.which(explicit) or (explicit if os.path.isfile(explicit) else None)
    found = shutil.which("codex")
    if found:
        return found
    try:
        from codex_cli_bin import bundled_codex_path

        return str(bundled_codex_path())
    except (ImportError, OSError):
        return None


def _codex_preflight(binary):
    """Valide binaire + auth AVANT le premier segment, pour échouer en 2s au
    lieu de découvrir le problème après plusieurs fichiers. `codex login
    status` ne consomme aucun quota."""
    if binary is None:
        raise ValueError(
            "Binaire Codex introuvable. L'installer par pip "
            "(`pip install openai-codex-cli-bin`) ou par npm "
            "(`npm install -g @openai/codex`), ou pointer CODEX_BIN dessus."
        )
    try:
        # Liste littérale ; même raisonnement que _grok_preflight pour CODEX_BIN.
        # nosemgrep
        result = subprocess.run(  # nosec B603
            [binary, "login", "status"],  # nosemgrep
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
            env=_codex_env_base(),
        )
    except (OSError, subprocess.SubprocessError) as e:
        raise ValueError(f"Impossible d'exécuter '{binary} login status' : {e}") from e
    if result.returncode != 0:
        raise ValueError(
            "Codex CLI n'est pas authentifié. Lancer `codex login` (connexion "
            "ChatGPT) pour utiliser --use_codex sur le quota de l'abonnement."
        )


def _codex_warn_unexpected_model(model):
    """L'allowlist des modèles utilisables sur un compte ChatGPT est appliquée
    côté serveur : un `gpt-5.4-mini` passé par mimétisme avec le mode --eco des
    autres providers échouerait en 400 après avoir consommé du temps. On
    prévient au lieu de bloquer, les slugs évoluant plus vite que cette liste."""
    if not model.startswith(CODEX_MODEL_PREFIXES):
        print(
            f"⚠ Modèle '{model}' inhabituel pour Codex (attendu : "
            f"{', '.join(p + '*' for p in CODEX_MODEL_PREFIXES)}). "
            "Les slugs Codex diffèrent des slugs API OpenAI.",
            file=sys.stderr,
        )


def _init_codex_client(args):
    """Provider Codex : traduit sur le quota de l'abonnement ChatGPT via le CLI
    officiel, sans facturation à l'usage. Aucune clé API n'est requise ni
    utilisée."""
    args.model = args.model or (ECO_MODEL_CODEX if args.eco else DEFAULT_MODEL_CODEX)
    _codex_reject_ci_environment()
    binary = _resolve_codex_binary()
    _codex_preflight(binary)
    _codex_warn_unexpected_model(args.model)
    return _CodexClient(
        binary=binary,
        timeout=CODEX_TIMEOUT,
        # Le CLI Codex n'accepte pas `none` pour model_reasoning_effort : on
        # retombe sur `low`, la valeur la plus basse qu'il connaisse.
        reasoning_effort=_resolve_reasoning_effort(args, eco_default="low", floor="low"),
    )
