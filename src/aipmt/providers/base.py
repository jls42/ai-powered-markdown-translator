"""Socle commun des providers : sous-processus, secrets, back-off, erreurs.

Les trois CLI d'abonnement (Codex, Grok, OpenCode) partagent le même pilote de
sous-processus — groupe de processus propre, `SIGTERM` puis `SIGKILL` au
timeout, stdin toujours fermé — le même filtrage des variables d'environnement
secrètes, la même relance sur limitation de débit et la même hiérarchie
d'erreurs. Les noms `_codex_*` sont historiques : ces fonctions sont nées avec
le provider Codex, puis ont été partagées ; elles gardent leur nom ici pour
que ce découpage reste un déplacement pur.
"""

import os
import re
import signal
import subprocess  # nosec B404 — pilote les CLI Codex, Grok et OpenCode, cf. _codex_run_process
import sys
import time

# Délai laissé au CLI pour propager SIGTERM à son petit-fils avant le SIGKILL.
CODEX_TERM_GRACE = 5


# `provider/modèle`, coupé au premier « / » par OpenCode ; le reste peut en
# contenir d'autres (lmstudio/google/gemma-3n-e4b) ou un deux-points
# (ollama/qwen2.5:7b). Le premier caractère exclut une valeur commençant par
# « - », qu'un parseur d'argv pourrait relire comme un drapeau.
_NAMESPACED_MODEL_REGEX = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._:/-]*$")


def _reason_name(reason):
    """Normalise un finish_reason/stop_reason : extrait .name si enum, sinon retourne tel quel."""
    return getattr(reason, "name", reason)


# Motifs de noms de variables retirés de l'environnement des sous-processus
# agentiques, en plus des listes explicites par provider.
#
# Les deny-lists nommées ne protégeaient que l'invariant de FACTURATION (Codex
# sans OPENAI_API_KEY, Grok sans XAI_API_KEY). Mesuré : sept autres secrets
# entraient quand même dans le sous-processus — les clés Anthropic, Mistral,
# Google, Gemini, plus celle de l'autre CLI. Or ces deux CLI sont des agents :
# Codex tourne en `--sandbox read-only`, mais le sandbox de Grok est
# inapplicable sur beaucoup de postes Linux et la protection y repose sur les
# seules règles `--deny`. Aucun des deux n'a besoin de la clé d'un autre
# fournisseur — l'authentification vit dans ~/.codex et ~/.grok, jamais dans
# l'environnement.
#
# Le filtrage est par motif et non par liste nominative, pour couvrir les
# variables qu'un utilisateur ajoute dans son `.env` sans que ce code le sache.
_SECRET_ENV_NAME_PATTERNS = ("API_KEY", "_TOKEN", "SECRET", "PASSWORD", "CREDENTIALS")


def _strip_secret_env(env, keep=()):
    """Retire de `env` toute variable dont le nom évoque un secret.

    `keep` permet de conserver explicitement une variable nécessaire au CLI ;
    aucune ne l'est aujourd'hui, l'auth des deux providers étant sur disque.
    """
    for name in [k for k in env if k not in keep]:
        if any(pattern in name.upper() for pattern in _SECRET_ENV_NAME_PATTERNS):
            del env[name]
    return env


def _codex_kill_group(proc):
    """Tue tout le groupe de process. Le `codex` installé par npm est un shim
    Node qui `spawn` le vrai binaire Rust : celui-ci est un petit-fils et
    survit à un kill du fils direct, où il continuerait à consommer du quota."""
    # ProcessLookupError est une sous-classe d'OSError : la capture est écrite
    # `except OSError` partout, sans la mentionner séparément.
    try:
        pgid = os.getpgid(proc.pid)
    except OSError:
        return
    try:
        os.killpg(pgid, signal.SIGTERM)
        proc.wait(timeout=CODEX_TERM_GRACE)
    except subprocess.TimeoutExpired:
        # Le SIGKILL a son propre try : une exception levée DEPUIS une clause
        # except n'est pas rattrapée par les clauses sœurs. Si le groupe meurt
        # entre l'expiration du délai de grâce et cet appel, le
        # ProcessLookupError remontait tel quel — l'appelant recevait une trace
        # opaque au lieu du RuntimeError « timeout après Ns » qui nomme la
        # cause et la variable d'environnement à augmenter.
        try:
            os.killpg(pgid, signal.SIGKILL)
            proc.wait()
        except OSError:
            pass
    except OSError:
        pass


# Variable à augmenter, citée dans le message de timeout de chaque CLI.
_CLI_TIMEOUT_ENV_VARS = {
    "Codex": "CODEX_TIMEOUT",
    "Grok": "GROK_TIMEOUT",
    "OpenCode": "OPENCODE_TIMEOUT",
}


def _codex_run_process(argv, stdin_data, timeout, env, label, model):
    """Lance un CLI agentique dans son propre groupe de process et renvoie
    (returncode, stdout, stderr). Socle commun aux providers Codex, Grok et
    OpenCode.

    Le groupe de process n'est pas une précaution de principe : ces deux CLI
    sont des agents, qui lancent leurs propres sous-process. Codex ajoute un
    niveau — installé par npm, `codex` est un shim Node qui `spawn` le binaire
    Rust, petit-fils du process Python qui survivrait au kill du fils direct en
    continuant à consommer du quota (vérifié : shebang `#!/usr/bin/env node`).
    Le binaire Grok est en revanche un ELF natif, sans shim, et le binaire
    Codex installé par pip aussi — la raison « shim » ne vaut donc pas partout,
    contrairement à ce qu'affirmait une version antérieure de ce commentaire ;
    la raison « agent qui spawn » vaut pour les deux.

    `communicate(input=...)` ferme toujours stdin — obligatoire pour Codex, qui
    lit stdin même quand le prompt est passé en argument et attendrait sinon
    indéfiniment sans jamais appeler le modèle."""
    timeout_var = _CLI_TIMEOUT_ENV_VARS.get(label, "CODEX_TIMEOUT")
    # argv est une LISTE (jamais shell=True) construite par _codex_argv/_grok_argv :
    # binaire résolu et validé par le préflight, flags littéraux, et `args.model`
    # placé en valeur juste après `-m` — une valeur commençant par `--` y est donc
    # consommée comme valeur du flag, pas réinterprétée en drapeau. Le contenu du
    # document ne transite JAMAIS par argv : il part par stdin (Codex) ou par
    # fichier (Grok, --prompt-file). Le marqueur nosemgrep doit rester sur la
    # ligne immédiatement précédente : plus haut, il n'est pas pris en compte.
    # nosemgrep
    with subprocess.Popen(  # nosec B603
        argv,  # nosemgrep — la finding est ancrée sur l'argument, pas sur l'appel
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        env=env,
        start_new_session=True,
    ) as proc:
        try:
            stdout, stderr = proc.communicate(input=stdin_data, timeout=timeout)
        except subprocess.TimeoutExpired:
            _codex_kill_group(proc)
            raise RuntimeError(
                f"{label} CLI timeout après {timeout}s (model={model}). "
                f"Augmenter {timeout_var} si les segments sont longs."
            ) from None
        return proc.returncode, stdout, stderr


def _stderr_tail(stderr, lines=3):
    """Dernières lignes de stderr, jointes, pour un message d'erreur qui dit
    quelque chose — commun aux trois CLI."""
    return " | ".join((stderr or "").strip().splitlines()[-lines:]) or "(stderr vide)"


class _CliCallError(RuntimeError):
    """Échec d'une invocation d'un CLI agentique, porteur du caractère
    récupérable ou non. Aucun des trois CLI n'implémente de retry interne
    exploitable : le back-off est entièrement à notre charge."""

    def __init__(self, message, rate_limited=False):
        super().__init__(message)
        self.rate_limited = rate_limited


def _retry_on_rate_limit(label, client, attempt_once):
    """Boucle de back-off commune aux trois CLI : ne retente que sur rate
    limit, avec un délai croissant. Sur un plan ChatGPT, chaque tour consomme
    un « message local » de la fenêtre de 5 heures ; le quota Grok est partagé
    avec Chat/Imagine/Voice sans être lisible ; les modèles gratuits de la
    passerelle Zen n'annoncent aucune limite. Dans les trois cas, mieux vaut
    attendre que perdre le fichier en cours."""
    last_error = None
    for attempt in range(1, client.max_attempts + 1):
        try:
            return attempt_once()
        except _CliCallError as e:
            last_error = e
            if not e.rate_limited or attempt == client.max_attempts:
                raise
            delay = client.backoff_seconds * attempt
            print(
                f"⚠ {label} rate limit (tentative {attempt}/{client.max_attempts}) — "
                f"nouvelle tentative dans {delay:.0f}s",
                file=sys.stderr,
            )
            time.sleep(delay)
    raise last_error  # unreachable, garde de sécurité


# Voie de repli à conseiller quand le mode abonnement est refusé. Le message
# était codé en dur pour Codex : un utilisateur de --use_grok_cli lisait
# « L'auth d'abonnement ChatGPT » et se voyait orienté vers OPENAI_API_KEY,
# alors que son repli est XAI_API_KEY / --use_grok.
_CLI_PROVIDER_CI_FALLBACK = {
    "--use_codex": ("ChatGPT", "OPENAI_API_KEY", "l'API OpenAI"),
    "--use_grok_cli": ("Grok", "XAI_API_KEY", "--use_grok"),
}


def _codex_reject_ci_environment(flag="--use_codex"):
    """Refuse de tourner en CI. Le mode abonnement s'authentifie par un fichier
    de session personnel ; le porter sur un runner partagé revient à y déposer
    une identité réutilisable par tout ce qui s'y exécute. OpenAI déconseille
    d'injecter ce fichier dans une CI — la mise en garde vise ce dépôt de
    secret, non le caractère public du dépôt de code. Sur un runner, la voie
    supportée est une clé API."""
    ci_vars = [var for var in ("CI", "GITHUB_ACTIONS") if os.getenv(var)]
    if ci_vars:
        plan, env_var, fallback = _CLI_PROVIDER_CI_FALLBACK.get(
            flag, ("ChatGPT", "OPENAI_API_KEY", "l'API OpenAI")
        )
        raise ValueError(
            f"{flag} est refusé en environnement CI ({', '.join(ci_vars)} défini). "
            f"L'auth d'abonnement {plan} n'est pas prévue pour un runner partagé : "
            f"utiliser {fallback} avec une clé API ({env_var}) sur ce chemin."
        )
