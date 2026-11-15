"""Provider Gemini (API Google, SDK `google-genai`).

Le niveau de réflexion accepté varie d'un modèle à l'autre ; le premier
niveau accepté est mémorisé par modèle, pour ne pas repayer la cascade de
refus à chaque segment.
"""

import logging
import os
import re
import sys

from google import genai
from google.genai import errors as genai_errors
from google.genai import types as genai_types

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_GEMINI_API_KEY = "votre-cle-api-gemini-par-defaut"  # pragma: allowlist secret


# Gemini 4 Hydrogen, sorti le 2026-11-12 : le seul Gemini 4 du niveau gratuit,
# vers lequel Google publie un guide de migration depuis 3.8 Flash, sans avoir
# déprécié ce dernier. Choix du propriétaire
# le 2026-11-15, sur mesure : le README en japonais, structure identique pour
# les deux, en 72 s contre 108 s pour 3.8 Flash, à la même heure sur le niveau
# payant. Prix : $1.50/$7.50 par million de tokens, celui que 3.8 Flash
# prendra à la fin de sa promotion, le 2026-12-31 ($0.75/$3.75 d'ici là).
# Mêmes niveaux de raisonnement que 3.8 Flash : `minimal` refusé par un 400.
#
# Le défaut précédent, gemini-3.8-flash, avait remplacé gemini-3.7-flash à la
# 1.18.0 : Google a déprécié 3.7 Flash le 2026-10-08 et route ses appels vers
# 3.8 Flash, dont ils consomment le quota (mesuré le 2026-11-14 sur le niveau
# gratuit). Les deux restent acceptés par `--model`.
DEFAULT_MODEL_GEMINI = "gemini-4-hydrogen"


# Arrêt annoncé le 2027-05-07, remplaçant désigné : gemini-3.5-flash-lite
# (même page). À mesurer avant de basculer, cf. docs/modeles.md.
ECO_MODEL_GEMINI = "gemini-3.1-flash-lite"


# Le SDK google-genai ne réessaie RIEN et n'attend SANS LIMITE par défaut : sans
# `retry_options`, un seul essai ; sans `timeout`, le client HTTP est construit
# avec `timeout=None`. Mesuré le 2026-11-14 sur le niveau gratuit, où Gemini
# Flash répondait « 503 high demand » ou pas du tout : aipmt abandonnait le
# fichier au premier 503, et un appel muet le bloquait plus de cinq minutes,
# jusqu'à ce qu'on l'arrête. Antigravity relance déjà ces pannes depuis la 1.17.1.
#
# Délai : 300 s par tentative, transmis aussi au serveur (`X-Server-Timeout`),
# qui l'applique : il répond « 504 DEADLINE_EXCEEDED » à l'échéance. Par
# Antigravity, un segment de 16 000 caractères prend de l'ordre de 40 s à un
# Gemini Flash (le CHANGELOG de la 1.14.1 en hindi : 273 s pour 7 segments).
# Mais le niveau gratuit de l'API, en « high demand », est bien plus lent :
# mesuré le 2026-11-15 sur 3.8 Flash avec un fichier de 444 octets, traduit
# en 245 s à 9 h 20 ; à 9 h 31, une tentative coupée par ce plafond au bout de
# 298 s, puis une relance réussie en 194 s. Le plafond reste à 300 s tant
# qu'aucune mesure ne montre qu'une tentative coupée aurait abouti.
#
# Réessais : les codes que le SDK juge passagers (408, 429, 500, 502, 503, 504),
# plus les délais dépassés et les connexions refusées, que le SDK réessaie
# d'office dès que `retry_options` est fourni. Quatre tentatives, séparées de
# 10, 20 puis 40 s (plus une gigue d'au plus 1 s) : 70 s d'attente cumulée,
# assez pour qu'une fenêtre de débit d'une minute se libère. Un 400 (niveau de
# raisonnement refusé, requête invalide) ou un 402 (crédit prépayé épuisé) ne
# sont jamais réessayés. Pire cas d'un serveur muet : quatre fois 300 s, puis
# l'erreur remonte au lieu d'attendre indéfiniment.
GEMINI_TIMEOUT_MS = 300_000
GEMINI_RETRY_STATUS_CODES = (408, 429, 500, 502, 503, 504)
GEMINI_HTTP_OPTIONS = genai_types.HttpOptions(
    timeout=GEMINI_TIMEOUT_MS,
    retry_options=genai_types.HttpRetryOptions(
        attempts=4,
        initial_delay=10.0,
        exp_base=2.0,
        max_delay=60.0,
        jitter=1.0,
        http_status_codes=list(GEMINI_RETRY_STATUS_CODES),
    ),
)


# Le SDK annonce chaque relance au niveau INFO de son journal, que personne
# n'affiche : sans ce relais, une relance ne laisse aucune trace, et quatre
# minutes d'attente sur un petit fichier ne se distinguent pas d'un blocage.
# Le 2026-11-15, le relais a montré ce que le silence cachait : une tentative
# coupée par un 504 au bout de 298 s, puis une relance réussie.
#
# Un filtre plutôt qu'un handler : ajouter un handler à ce journal priverait
# ses avertissements du handler de dernier recours de Python, et l'avis « Both
# GOOGLE_API_KEY and GEMINI_API_KEY are set » disparaîtrait. Le filtre laisse
# passer exactement ce que le niveau d'avant laissait passer.
#
# Le motif suit le message de `tenacity.before_sleep_log` ; s'il change, le
# test de la relance d'un 503 échoue au lieu de laisser l'avis s'éteindre.
_GEMINI_SDK_LOGGER = "google_genai._api_client"
_SDK_RETRY_MESSAGE = re.compile(
    r"Retrying \S+ in (?P<delay>[\d.]+) seconds as it raised (?P<error>\w+): (?P<detail>.*)",
    re.DOTALL,
)


class _GeminiRetryNotice(logging.Filter):
    """Relaie sur stderr les relances que le SDK annonce au niveau INFO."""

    def __init__(self, previous_level: int) -> None:
        super().__init__()
        self.previous_level = previous_level

    def filter(self, record: logging.LogRecord) -> bool:
        match = _SDK_RETRY_MESSAGE.match(record.getMessage())
        if match:
            # Le corps d'erreur suit le statut (« 503 UNAVAILABLE. {…} ») : on
            # garde le statut, le corps JSON noierait la ligne.
            detail = match["detail"].split(". ", 1)[0].rstrip(".")[:120]
            print(
                f"⚠ Gemini : {match['error']}: {detail} — nouvelle tentative dans "
                f"{float(match['delay']):.0f} s",
                file=sys.stderr,
            )
        return record.levelno >= self.previous_level


def _install_gemini_retry_notice() -> None:
    """Branche le relais une seule fois, quel que soit le nombre de clients."""
    logger = logging.getLogger(_GEMINI_SDK_LOGGER)
    if any(isinstance(f, _GeminiRetryNotice) for f in logger.filters):
        return
    previous_level = logger.getEffectiveLevel()
    logger.addFilter(_GeminiRetryNotice(previous_level))
    logger.setLevel(min(previous_level, logging.INFO))


def _gemini_config(prompt, thinking_level):
    """Config d'un appel Gemini. Le niveau de raisonnement est explicite : les
    modèles Gemini 3.x raisonnent par défaut, ce qui se paie sur chaque segment
    de chaque fichier sans rien apporter à une traduction. L'ancien SDK ne
    savait pas piloter ce réglage."""
    config = genai_types.GenerateContentConfig(system_instruction=prompt)
    if thinking_level is not None:
        config.thinking_config = genai_types.ThinkingConfig(thinking_level=thinking_level)
    return config


# Du moins coûteux au plus permissif. `minimal` n'est accepté que par une
# partie du catalogue (flash-lite l'accepte ; 3.7-flash, 3.8-flash, 3.1-pro et
# les trois Gemini 4 le refusent par un 400, mesuré le 2026-11-15 pour ces
# derniers) ; `low` passe partout ; `None` = pas de thinking_config du tout,
# dernier recours si l'API change encore.
_GEMINI_THINKING_LEVELS = ("minimal", "low", None)


# Niveau accepté par modèle, mémorisé au premier segment. Sans ce cache, la
# cascade repartait de `minimal` pour CHAQUE segment de CHAQUE fichier — or le
# modèle par défaut (gemini-3.7-flash alors, Gemini 4 Hydrogen depuis) refuse
# `minimal` : le chemin nominal
# payait donc un aller-retour 400 par segment, et réimprimait le même
# avertissement à chaque fois. Un warning répété des centaines de fois sur un
# regen cesse d'être lu, et c'est ainsi qu'il devient un masque.
_GEMINI_ACCEPTED_THINKING_LEVEL: dict[str, str | None] = {}


def _gemini_generate_with_fallback(client, args, prompt, segment):
    """Descend la cascade des niveaux de raisonnement jusqu'à en trouver un que
    le modèle accepte, puis mémorise ce niveau pour les segments suivants. Même
    logique que `_openai_create_with_fallback` : un paramètre d'optimisation ne
    doit jamais faire échouer une traduction."""
    known = _GEMINI_ACCEPTED_THINKING_LEVEL.get(args.model)
    levels = (known,) if args.model in _GEMINI_ACCEPTED_THINKING_LEVEL else _GEMINI_THINKING_LEVELS
    last_error = None
    for level in levels:
        try:
            response = client.models.generate_content(
                model=args.model, contents=segment, config=_gemini_config(prompt, level)
            )
        except genai_errors.ClientError as e:
            if "thinking" not in str(e).lower():
                raise
            last_error = e
            print(
                f"⚠ Gemini refuse thinking_level={level!r} — retry au niveau suivant "
                f"(model={args.model})",
                file=sys.stderr,
            )
            # Un niveau mémorisé qui devient invalide (changement côté API) doit
            # rendre la main à la cascade complète plutôt que boucler dessus.
            _GEMINI_ACCEPTED_THINKING_LEVEL.pop(args.model, None)
        else:
            _GEMINI_ACCEPTED_THINKING_LEVEL[args.model] = level
            return response
    raise RuntimeError(
        f"Gemini a refusé tous les niveaux de raisonnement (model={args.model}): {last_error}"
    )


def _call_gemini(client, args, prompt, segment):
    response = _gemini_generate_with_fallback(client, args, prompt, segment)
    candidates = getattr(response, "candidates", None) or []
    if candidates:
        fr_name = _reason_name(getattr(candidates[0], "finish_reason", None))
        if fr_name not in ("STOP", "FINISH_REASON_STOP", None):
            raise RuntimeError(f"Gemini abnormal finish_reason={fr_name!r} (model={args.model})")
    else:
        # Pas de candidat = SAFETY/RECITATION/quota côté upstream. La cause
        # vit dans `prompt_feedback` ; sans ça, le RuntimeError final dirait
        # juste "blocked or empty" et masquerait le vrai motif.
        feedback = getattr(response, "prompt_feedback", None)
        raise RuntimeError(
            f"Gemini returned no candidates (model={args.model}, prompt_feedback={feedback!r})"
        )
    try:
        return response.text.strip()
    except (ValueError, AttributeError) as e:
        raise RuntimeError(
            f"Gemini response has no text (likely blocked or empty, model={args.model}): {e}"
        ) from e


def _init_gemini_client(args):
    args.model = args.model or (ECO_MODEL_GEMINI if args.eco else DEFAULT_MODEL_GEMINI)
    # Accepte GOOGLE_API_KEY et GEMINI_API_KEY (convention AI Studio). Le SDK
    # google-genai lirait GOOGLE_API_KEY tout seul, mais on la passe
    # explicitement pour conserver la garde sur la valeur placeholder.
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY") or DEFAULT_GEMINI_API_KEY
    if not api_key or api_key == DEFAULT_GEMINI_API_KEY:
        raise ValueError(_missing_key_message("Gemini", ["GOOGLE_API_KEY", "GEMINI_API_KEY"]))
    _install_gemini_retry_notice()
    return genai.Client(api_key=api_key, http_options=GEMINI_HTTP_OPTIONS)
