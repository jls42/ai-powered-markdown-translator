"""Providers Grok : l'API xAI (`--use_grok`) et le CLI d'abonnement (`--use_grok_cli`).

Le mode API est un endpoint compatible OpenAI : même client, même appel, seul
le `base_url` change. Le mode CLI pilote le binaire `grok` ; son confinement
repose sur `--deny` (seule couche mesurée fail-closed), jamais sur un profil de
sandbox qui échoue en silence.
"""

import json
import os
import shutil
import subprocess  # nosec B404 — pilote le CLI Grok, cf. _grok_preflight
import sys
import tempfile
from dataclasses import dataclass

from openai import OpenAI

from ..config import _missing_key_message
from .base import (
    _CliCallError,
    _codex_reject_ci_environment,
    _codex_run_process,
    _retry_on_rate_limit,
    _stderr_tail,
    _strip_secret_env,
)

DEFAULT_XAI_API_KEY = "votre-cle-api-xai-par-defaut"  # pragma: allowlist secret


# Volontairement écrit en toutes lettres ici, dans DEFAULT_MODEL_GROK_CLI et
# dans MODEL_TOKEN_LIMITS, plutôt que factorisé (SonarCloud python:S1192).
# Les catalogues API et CLI de Grok sont indépendants — le CLI n'expose pas
# grok-4.3, palier éco de l'API — et la coïncidence actuelle des valeurs
# qualité est un hasard de calendrier. Un alias ferait suivre silencieusement
# le défaut CLI à toute évolution du défaut API. Même raisonnement pour
# ECO_MODEL_OPENAI / ECO_MODEL_CODEX, et pour les clés de MODEL_TOKEN_LIMITS,
# qui est un catalogue destiné à être lu, pas un jeu de références.
DEFAULT_MODEL_GROK = "grok-4.6"  # NOSONAR python:S1192


# xAI n'a aucun palier mini/flash/lite : l'« éco » est une génération
# antérieure, pas une variante allégée. `grok-4.3` (1M ctx, $1.25/$2.50) reste
# nettement plus cher que l'éco des autres providers — mistral-small-latest est
# à $0.15/$0.60. Grok se choisit pour la diversité de modèle, pas pour le prix.
ECO_MODEL_GROK = "grok-4.3"


# Le CLI d'abonnement n'expose que grok-4.6 et grok-4.5 (`grok models`) :
# grok-4.3, le palier économique de l'API, n'y est pas disponible.
DEFAULT_MODEL_GROK_CLI = "grok-4.6"


ECO_MODEL_GROK_CLI = "grok-4.5"


# --- Provider Grok (API xAI, facturé à l'usage) -----------------------------
# Endpoint compatible OpenAI : le SDK `openai` fonctionne avec ce base_url.
XAI_BASE_URL = "https://api.x.ai/v1"


# --- Provider Grok CLI (Grok Build, quota d'abonnement Grok) ----------------
# Même principe que Codex : on pilote le binaire officiel `grok` en mode
# headless, donc la traduction est décomptée de l'abonnement au lieu d'être
# facturée au token. xAI documente ce mode pour « CI pipelines, cron jobs, and
# scripts », et il est ouvert aux abonnés SuperGrok et X Premium+.
GROK_TIMEOUT = int(os.getenv("GROK_TIMEOUT", "900"))


# Le prompt part par fichier, jamais par argv : un segment de 16 000 caractères
# serait visible dans `ps` et flirterait avec ARG_MAX. Le CLI ne lit pas stdin.
GROK_PROMPT_FILENAME = "prompt.md"


# Confinement. `--deny` est la seule couche mesurée fail-closed : une règle au
# préfixe inconnu fait REFUSER le démarrage, donc une évolution du vocabulaire
# casse la traduction au lieu de retirer la protection en silence. La règle `*`
# est le catch-all documenté ; les préfixes nommés restent pour que l'intention
# soit lisible et pour survivre à une éventuelle disparition du catch-all.
# Forme `Prefix(*)` et non le nom nu : mesuré sur grok 1.0.13, le CLI ne valide
# QUE la forme parenthésée. `--deny 'CeciNestPasUnOutil(*)'` refuse le démarrage
# (« unknown tool prefix »), tandis que `--deny 'CeciNestPasUnOutil'` est accepté
# en silence. Avec les noms nus, un renommage d'outil côté xAI aurait donc retiré
# la protection sans le moindre signal — exactement le fail-open que ce
# confinement existe pour éviter, et sur un poste où le sandbox OS ne s'applique
# déjà pas. Les huit préfixes ci-dessous ont été vérifiés un à un comme connus du
# CLI ; le catch-all `*` reste sous sa forme littérale, seule acceptée.
GROK_DENY_RULES = (
    "*",
    "Bash(*)",
    "Edit(*)",
    "Write(*)",
    "Read(*)",
    "Grep(*)",
    "WebFetch(*)",
    "WebSearch(*)",
    "MCPTool(*)",
)


# Le compteur de tours est incrémenté APRÈS le tour d'outils : `--max-turns 1`
# tronquerait la sortie (stopReason=cancelled). Le plancher mesuré est 2 même
# sur un segment trivial ; 6 laisse de la marge sans lever la borne de coût.
GROK_MAX_TURNS = 6


# Variables retirées de l'env du sous-processus. XAI_API_KEY d'abord : la
# présence d'une clé ferait basculer en facturation à l'usage, ce que ce
# provider existe pour éviter. GROK_SANDBOX ensuite : héritée d'un shell, elle
# imposerait un profil que cette machine ne peut pas appliquer, rendant le
# provider inutilisable avec un message trompeur.
GROK_STRIPPED_ENV_VARS = ("XAI_API_KEY", "GROK_API_KEY", "GROK_SANDBOX")


# Réduction de surface, jamais une garantie : ces interrupteurs sont
# contournables par une politique managée. Le confinement repose sur --deny.
GROK_ENV_KILL_SWITCHES = {
    "GROK_CLAUDE_MCPS_ENABLED": "false",
    "GROK_CLAUDE_HOOKS_ENABLED": "false",
    "GROK_CLAUDE_SKILLS_ENABLED": "false",
    "GROK_CLAUDE_AGENTS_ENABLED": "false",
}


# Profil sandbox OS, en opt-in explicite via GROK_TRANSLATE_SANDBOX. Sur cette
# machine aucun profil ne s'applique (AppArmor bloque les user namespaces non
# privilégiés, et la deny-list runtime-socket échoue sur /run/podman en 0700) :
# on ne le tente donc pas par défaut, mais on ne retombe JAMAIS silencieusement
# non plus — un profil demandé et non applicable fait échouer le démarrage.
GROK_SANDBOX_ENV_VAR = "GROK_TRANSLATE_SANDBOX"


GROK_AGENT_CONTRACT = (
    "\n\nIMPORTANT (mode non-interactif) : ne lis aucun fichier, n'exécute aucune "
    "commande, n'utilise aucun outil. Réponds UNIQUEMENT par le contenu traduit, "
    "sans préambule, sans commentaire, et sans l'entourer d'un bloc de code."
)


@dataclass
class _GrokCliClient:
    """« Client » du provider Grok CLI : comme pour Codex, il n'y a pas de
    session HTTP à tenir. L'auth vit dans ~/.grok et n'est jamais lue ici."""

    binary: str
    timeout: int = GROK_TIMEOUT
    max_attempts: int = 3
    backoff_seconds: float = 30.0
    sandbox_profile: str = ""


def _grok_env():
    """Env du sous-processus : sans clé API (sinon facturation à l'usage) et
    sans GROK_SANDBOX hérité, plus les interrupteurs de réduction de surface."""
    env = os.environ.copy()
    for var in GROK_STRIPPED_ENV_VARS:
        env.pop(var, None)
    _strip_secret_env(env)
    env.pop("OPENAI_BASE_URL", None)
    env.update(GROK_ENV_KILL_SWITCHES)
    return env


def _grok_write_prompt(workdir, prompt, segment):
    """Écrit le prompt complet dans un fichier : le CLI ne lit pas stdin, et
    passer 16 000 caractères par argv les exposerait dans `ps`."""
    path = os.path.join(workdir, GROK_PROMPT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(prompt + GROK_AGENT_CONTRACT + "\n\n" + segment)
    return path


def _grok_argv(client, args, prompt_file, workdir):
    argv = [
        client.binary,
        "--prompt-file",
        prompt_file,
        "--output-format",
        "json",
        "--cwd",
        workdir,
        "--no-subagents",
        "--no-plan",
        "--disable-web-search",
        "--max-turns",
        str(GROK_MAX_TURNS),
        "-m",
        args.model,
    ]
    for rule in GROK_DENY_RULES:
        argv += ["--deny", rule]
    if client.sandbox_profile:
        argv += ["--sandbox", client.sandbox_profile]
    return argv


def _grok_parse_payload(stdout, args):
    """Le CLI écrit un unique objet JSON sur stdout. Une sortie non-JSON est un
    échec en soi : on ne devine pas, on lève."""
    text = (stdout or "").strip()
    if not text:
        raise _GrokCallError(f"Grok CLI n'a rien écrit sur stdout (model={args.model})")
    try:
        payload = json.loads(text)
    except ValueError as e:
        raise _GrokCallError(
            f"Sortie Grok CLI illisible (model={args.model}) : {text[:200]!r}"
        ) from e
    # Une liste ou une chaîne sont du JSON parfaitement valide : sans ce
    # contrôle, `_grok_check_payload` levait un AttributeError sur `.get()`,
    # hors du type d'erreur que la boucle de back-off sait interpréter.
    if not isinstance(payload, dict):
        raise _GrokCallError(
            f"Sortie Grok CLI de type inattendu ({type(payload).__name__}, "
            f"model={args.model}) : {text[:200]!r}"
        )
    return payload


# `quota` en est volontairement absent, pour la raison que le docstring de
# `_codex_is_rate_limited` explique déjà : le mot apparaît aussi bien dans un
# 429 récupérable que dans un « quota exhausted, upgrade your plan » définitif.
# Le garder faisait attendre 90 s avant d'échouer quand même sur une erreur
# irrécupérable. Le CLI Grok n'exposant pas de champ structuré dans son payload
# d'erreur, l'inspection de chaînes reste ici contrainte — d'où le choix de
# marqueurs non ambigus uniquement.
_GROK_RATE_LIMIT_MARKERS = ("rate limit", "rate_limit", "too many requests", "429")


def _grok_check_payload(payload, args):
    """Contrat de sortie à quatre conditions. `exit == 0` ne prouve rien : une
    erreur d'authentification, un refus ou un dépassement de tours sortent tous
    en 0 avec un JSON d'apparence normale."""
    if payload.get("type") == "error":
        message = str(payload.get("message", payload))
        raise _GrokCallError(
            f"Grok CLI a échoué : {message}",
            rate_limited=any(m in message.lower() for m in _GROK_RATE_LIMIT_MARKERS),
        )
    # Un `stopReason` ABSENT est un échec, pas un succès : la version
    # précédente sautait la vérification dans ce cas (`if stop is not None`),
    # si bien qu'un payload `{"text": "..."}` — champ jamais émis, ou renommé
    # par une mise à jour du CLI — passait le contrat sans que rien ne le
    # signale. La garde serait alors devenue un no-op silencieux, et une
    # réponse tronquée sur dépassement de tours serait partie sur disque.
    stop = payload.get("stopReason")
    if stop is None:
        raise _GrokCallError(
            f"Grok CLI n'a pas émis de stopReason (model={args.model}) — "
            "contrat de sortie non vérifiable, réponse refusée"
        )
    if str(stop).lower() not in ("end_turn", "endturn"):
        raise _GrokCallError(
            f"Grok CLI stopReason anormal={stop!r} (model={args.model}) — "
            "réponse potentiellement tronquée",
            # `max_turn_requests` n'est PAS un rate limit : c'est le budget de
            # tours (--max-turns) qui est épuisé. Retenter avec la même borne
            # reproduit le résultat à l'identique, au prix de 90 s d'attente
            # sur une erreur déterministe.
            rate_limited=str(stop).lower() == "rate_limited",
        )


def _grok_extract_text(payload, args):
    structured = payload.get("structuredOutput")
    if isinstance(structured, dict) and structured.get("markdown"):
        return structured["markdown"]
    text = payload.get("text")
    if not text:
        raise _GrokCallError(
            f"Grok CLI n'a renvoyé aucun texte (model={args.model}, "
            f"stopReason={payload.get('stopReason')!r})"
        )
    return text


class _GrokCallError(_CliCallError):
    """Échec d'une invocation du CLI Grok, porteur du caractère récupérable."""


def _grok_attempt(client, args, prompt, segment):
    with tempfile.TemporaryDirectory(prefix="translate-grok-") as workdir:
        prompt_file = _grok_write_prompt(workdir, prompt, segment)
        argv = _grok_argv(client, args, prompt_file, workdir)
        returncode, stdout, stderr = _codex_run_process(
            argv, None, client.timeout, _grok_env(), "Grok", args.model
        )
        if returncode != 0:
            message = _stderr_tail(stderr)
            raise _GrokCallError(
                f"Grok CLI a quitté avec le code {returncode} : {message}",
                rate_limited=any(m in message.lower() for m in _GROK_RATE_LIMIT_MARKERS),
            )
        payload = _grok_parse_payload(stdout, args)
        _grok_check_payload(payload, args)
        return _grok_extract_text(payload, args)


def _call_grok_cli(client, args, prompt, segment):
    """Traduit un segment via le CLI Grok, avec back-off sur rate limit."""
    return _retry_on_rate_limit(
        "Grok", client, lambda: _grok_attempt(client, args, prompt, segment)
    )


def _resolve_grok_binary():
    """Chemin du binaire `grok` : GROK_BIN, puis le PATH, puis l'emplacement
    d'installation par défaut (~/.grok/bin/grok), que l'installeur officiel
    n'ajoute pas systématiquement au PATH."""
    explicit = os.getenv("GROK_BIN")
    if explicit:
        return shutil.which(explicit) or (explicit if os.path.isfile(explicit) else None)
    found = shutil.which("grok")
    if found:
        return found
    home = os.path.join(os.path.expanduser(os.getenv("GROK_HOME", "~/.grok")), "bin", "grok")
    return home if os.path.isfile(home) else None


def _grok_preflight(binary):
    """Valide binaire et authentification sans consommer un seul token.
    `grok models` sort en 0 même déconnecté, en écrivant « You are not
    authenticated. » sur stdout : le code retour ne suffit donc pas."""
    if binary is None:
        raise ValueError(
            "Binaire Grok introuvable. L'installer "
            "(`curl -fsSL https://x.ai/cli/install.sh | bash`) ou pointer GROK_BIN dessus."
        )
    try:
        # Liste littérale ; `binary` vient de GROK_BIN/PATH, donc d'un
        # environnement qui a déjà l'exécution de code sur cette machine.
        # nosemgrep
        result = subprocess.run(  # nosec B603
            [binary, "models"],  # nosemgrep
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
            env=_grok_env(),
        )
    except (OSError, subprocess.SubprocessError) as e:
        raise ValueError(f"Impossible d'exécuter '{binary} models' : {e}") from e
    if result.returncode != 0:
        raise ValueError(
            f"'{binary} models' a échoué (code {result.returncode}) : "
            f"{(result.stderr or '').strip()[:200]}"
        )
    if "not authenticated" in (result.stdout or "").lower():
        raise ValueError(
            "Grok CLI n'est pas authentifié. Lancer `grok login` (ou "
            "`grok login --device-code`) pour utiliser --use_grok_cli sur le "
            "quota de l'abonnement."
        )


def _grok_sandbox_profile():
    """Profil sandbox demandé par l'utilisateur, ou chaîne vide.

    Non activé par défaut, et jamais de repli silencieux : sur beaucoup de
    postes Linux récents aucun profil ne peut s'appliquer (AppArmor bloque les
    user namespaces non privilégiés depuis Ubuntu 24.04, et la deny-list des
    sockets de runtime conteneur échoue si /run/podman est en 0700). Un profil
    intégré qui ne peut pas s'appliquer démarre NON CONFINÉ en silence — d'où
    l'opt-in explicite, qui fait alors échouer le démarrage plutôt que de
    laisser croire à une protection absente."""
    return os.getenv(GROK_SANDBOX_ENV_VAR, "").strip()


def _init_grok_cli_client(args):
    """Provider Grok CLI : traduit sur le quota de l'abonnement Grok via le
    binaire officiel, sans clé API."""
    args.model = args.model or (ECO_MODEL_GROK_CLI if args.eco else DEFAULT_MODEL_GROK_CLI)
    _codex_reject_ci_environment(flag="--use_grok_cli")
    binary = _resolve_grok_binary()
    _grok_preflight(binary)
    profile = _grok_sandbox_profile()
    if not profile:
        print(
            "⚠ Grok CLI lancé sans sandbox OS : le confinement repose sur les "
            "règles --deny du CLI, pas sur une frontière noyau. Définir "
            f"{GROK_SANDBOX_ENV_VAR}=read-only pour l'exiger (le démarrage "
            "échouera si la machine ne peut pas l'appliquer).",
            file=sys.stderr,
        )
    return _GrokCliClient(binary=binary, timeout=GROK_TIMEOUT, sandbox_profile=profile)


def _init_grok_client(args):
    """Provider Grok par clé API xAI (facturé à l'usage). L'endpoint est
    compatible OpenAI, donc le client et `_call_openai` sont réutilisés tels
    quels — seul le `base_url` change."""
    args.model = args.model or (ECO_MODEL_GROK if args.eco else DEFAULT_MODEL_GROK)
    api_key = os.getenv("XAI_API_KEY", DEFAULT_XAI_API_KEY)
    if not api_key or api_key == DEFAULT_XAI_API_KEY:
        raise ValueError(
            _missing_key_message("xAI", ["XAI_API_KEY"], hint=" Clé à obtenir sur console.x.ai.")
        )
    return OpenAI(api_key=api_key, base_url=os.getenv("XAI_BASE_URL", XAI_BASE_URL))
