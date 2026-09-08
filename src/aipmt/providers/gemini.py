"""Provider Gemini (API Google, SDK `google-genai`).

Le niveau de réflexion accepté varie d'un modèle à l'autre ; le premier
niveau accepté est mémorisé par modèle, pour ne pas repayer la cascade de
refus à chaque segment.
"""

import os
import sys

from google import genai
from google.genai import errors as genai_errors
from google.genai import types as genai_types

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_GEMINI_API_KEY = "votre-cle-api-gemini-par-defaut"  # pragma: allowlist secret


DEFAULT_MODEL_GEMINI = "gemini-3.7-flash"


ECO_MODEL_GEMINI = "gemini-3.1-flash-lite"


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
# partie du catalogue (flash-lite l'accepte, 3.7-flash et 3.1-pro le refusent
# par un 400) ; `low` passe partout ; `None` = pas de thinking_config du tout,
# dernier recours si l'API change encore.
_GEMINI_THINKING_LEVELS = ("minimal", "low", None)


# Niveau accepté par modèle, mémorisé au premier segment. Sans ce cache, la
# cascade repartait de `minimal` pour CHAQUE segment de CHAQUE fichier — or le
# modèle par défaut (gemini-3.7-flash) refuse `minimal` : le chemin nominal
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
    return genai.Client(api_key=api_key)
