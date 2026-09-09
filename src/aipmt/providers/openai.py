"""Provider OpenAI (API), et l'appel partagé par les endpoints compatibles.

`_call_openai` sert aussi à Grok par clé API (endpoint compatible OpenAI, seul
le `base_url` change) ; OpenRouter réutilise `_build_openai_messages`. Le
niveau de raisonnement des modèles GPT-5.x est résolu ici, et Codex s'en sert.
"""

import os
import sys

from openai import BadRequestError, OpenAI

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_OPENAI_API_KEY = "votre-cle-api-openai-par-defaut"  # pragma: allowlist secret


DEFAULT_MODEL_OPENAI = "gpt-5.6-terra"


ECO_MODEL_OPENAI = "gpt-5.6-luna"  # NOSONAR python:S1192 — cf. DEFAULT_MODEL_GROK


_O1_SERIES = ("o1", "o1-mini", "o1-preview")


def _resolve_reasoning_effort(args, eco_default="none", floor=None):
    """Effort de raisonnement effectif : la valeur explicite si l'utilisateur en
    a passé une, sinon `eco_default` en mode --eco et `medium` autrement.

    Mesuré sur le modèle éco d'alors : un `medium` implicite produit 45
    reasoning tokens et 65 tokens de sortie pour traduire une phrase de dix
    mots, contre 0 et 14 avec `none`. Sur de la traduction, ce raisonnement
    n'apporte rien — c'est de la dépense pure, payée sur chaque segment de
    chaque fichier.

    `floor` remonte une valeur que le provider n'accepte pas, y compris quand
    elle est passée explicitement : le CLI Codex refuse `none`, et la valeur
    explicite contournait jusqu'ici le repli sur `low`."""
    explicit = getattr(args, "reasoning_effort", None)
    effort = explicit or (eco_default if getattr(args, "eco", False) else "medium")
    if floor and effort == "none":
        if explicit:
            print(
                f"⚠ reasoning_effort={explicit!r} n'est pas accepté par ce provider "
                f"— repli sur {floor!r}",
                file=sys.stderr,
            )
        return floor
    return effort


def _build_openai_messages(args, prompt, segment):
    if args.model in _O1_SERIES:
        return [{"role": "user", "content": prompt + "\n\n" + segment}]
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": segment},
    ]


def _openai_extra_kwargs(args, is_translation_note):
    # reasoning_effort sur GPT-5.x.
    if args.model.startswith("gpt-5") and not is_translation_note:
        return {"reasoning_effort": _resolve_reasoning_effort(args)}
    return {}


def _openai_create_with_fallback(client, args, messages, extra_kwargs):
    try:
        return client.chat.completions.create(model=args.model, messages=messages, **extra_kwargs)
    except TypeError as e:
        # Vieille version SDK locale qui ne connaît pas reasoning_effort.
        if "reasoning_effort" not in str(e) or not extra_kwargs:
            raise
        print(
            f"⚠ OpenAI SDK rejette reasoning_effort (TypeError) — retry sans (model={args.model})",
            file=sys.stderr,
        )
        return client.chat.completions.create(model=args.model, messages=messages)
    except BadRequestError as e:
        # Modèle qui ne supporte pas reasoning_effort côté serveur.
        if "reasoning_effort" not in str(e) or not extra_kwargs:
            raise
        print(
            f"⚠ OpenAI rejette reasoning_effort (400) — retry sans (model={args.model})",
            file=sys.stderr,
        )
        return client.chat.completions.create(model=args.model, messages=messages)


def _call_openai(client, args, prompt, segment, is_translation_note):
    messages = _build_openai_messages(args, prompt, segment)
    extra_kwargs = _openai_extra_kwargs(args, is_translation_note)
    response = _openai_create_with_fallback(client, args, messages, extra_kwargs)
    choice = response.choices[0]
    finish = _reason_name(choice.finish_reason)
    # `end_turn` est la forme émise par l'API xAI (endpoint compatible OpenAI)
    # là où OpenAI émet `stop` : sans elle, toute traduction Grok par clé API
    # serait rejetée comme un finish_reason anormal.
    if finish not in ("stop", "STOP", "end_turn", None):
        raise RuntimeError(f"OpenAI abnormal finish_reason={finish!r} (model={args.model})")
    content = choice.message.content
    if content is None:
        # SDK récents renvoient `content=None` quand la réponse contient
        # uniquement un refusal ou des tool_calls. Sans cette garde, .strip()
        # lèverait un AttributeError opaque qui noierait la vraie cause.
        refusal = getattr(choice.message, "refusal", None)
        tool_calls = getattr(choice.message, "tool_calls", None)
        raise RuntimeError(
            f"OpenAI returned message.content=None (model={args.model}, "
            f"refusal={refusal!r}, tool_calls={tool_calls!r})"
        )
    return content.strip()


def _init_openai_client(args):
    args.model = args.model or (ECO_MODEL_OPENAI if args.eco else DEFAULT_MODEL_OPENAI)
    openai_api_key = os.getenv("OPENAI_API_KEY", DEFAULT_OPENAI_API_KEY)
    if not openai_api_key or openai_api_key == DEFAULT_OPENAI_API_KEY:
        raise ValueError(_missing_key_message("OpenAI", ["OPENAI_API_KEY"]))
    return OpenAI(api_key=openai_api_key)
