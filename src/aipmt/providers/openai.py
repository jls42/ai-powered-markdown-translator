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


# GPT-6.1 Terra et GPT-6 Luna depuis le 2026-11-15, à moitié prix de leurs
# aînés ($1/$5 contre $2/$12 par million pour Terra, $0,10/$0,50 contre
# $0,20/$1,20 pour Luna). Mesuré ce jour-là sur le README en japonais, effort
# envoyé : structure identique quatre fois sur quatre pour chacun. Terra y met
# de 190 à 245 s, contre 116 s pour gpt-5.6-terra ; Luna 125 s, comme
# gpt-5.6-luna, qui a perdu un gras une fois sur six. OpenAI n'annonce aucun
# retrait des gpt-5.6, qui restent accessibles par `--model`.
DEFAULT_MODEL_OPENAI = "gpt-6.1-terra"


ECO_MODEL_OPENAI = "gpt-6-luna"  # NOSONAR python:S1192 — cf. DEFAULT_MODEL_GROK


_O1_SERIES = ("o1", "o1-mini", "o1-preview")


def _resolve_reasoning_effort(args, eco_default="none", floor=None, quality_default="medium"):
    """Effort de raisonnement effectif : la valeur explicite si l'utilisateur en
    a passé une, sinon `eco_default` en mode --eco et `quality_default`
    autrement.

    Mesuré sur le modèle éco d'alors : un `medium` implicite produit 45
    reasoning tokens et 65 tokens de sortie pour traduire une phrase de dix
    mots, contre 0 et 14 avec `none`. Sur de la traduction, ce raisonnement
    n'apporte rien — c'est de la dépense pure, payée sur chaque segment de
    chaque fichier.

    `floor` remonte une valeur que le provider n'accepte pas, y compris quand
    elle est passée explicitement : le CLI Codex refuse `none`, et la valeur
    explicite contournait jusqu'ici le repli sur `low`."""
    explicit = getattr(args, "reasoning_effort", None)
    effort = explicit or (eco_default if getattr(args, "eco", False) else quality_default)
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


# Familles qui reçoivent `reasoning_effort`, avec l'effort envoyé hors `--eco`.
# Mesuré le 2026-11-15.
# GPT-6 : sans le paramètre, `--eco` laissait gpt-6-luna raisonner à son niveau
# par défaut.
# Grok par clé API : sans lui, chaque segment payait le raisonnement par défaut
# du modèle — 695 tokens de raisonnement pour 113 de sortie sur grok-4.7, 373
# pour 103 sur grok-4.3, le palier éco, qui n'en dépense aucun avec `none`.
# `low` et non `medium` pour Grok : sur le README en japonais, grok-4.7 rend la
# même structure aux deux niveaux, en 190 s à `low` contre 711 s à `medium`.
_QUALITY_REASONING_EFFORT = {"gpt-5": "medium", "gpt-6": "medium", "grok-4": "low"}


def _openai_extra_kwargs(args, is_translation_note):
    if is_translation_note:
        return {}
    for family, quality_default in _QUALITY_REASONING_EFFORT.items():
        if args.model.startswith(family):
            effort = _resolve_reasoning_effort(args, quality_default=quality_default)
            return {"reasoning_effort": effort}
    return {}


def _rejects_reasoning_effort(error):
    """Le refus porte-t-il sur `reasoning_effort` ? OpenAI nomme le paramètre
    dans son message ; xAI réduit le sien à « Error code: 400 » et range le
    motif dans le corps, sous deux graphies (`reasoning_effort` pour une valeur
    refusée, `reasoningEffort` pour un modèle qui ignore le paramètre)."""
    text = f"{error} {getattr(error, 'body', None) or ''}".lower()
    return "reasoning_effort" in text or "reasoningeffort" in text


def _reasoning_effort_attempts(extra_kwargs):
    """Du réglage demandé au plus permissif. `none` refusé (grok-4.5 et
    suivants, gpt-6.1-sol) se replie d'abord sur `low`, le niveau le plus
    proche que ces modèles acceptent, avant l'appel sans le paramètre, qui
    rend au modèle son raisonnement par défaut, le plus coûteux."""
    attempts = [extra_kwargs]
    if extra_kwargs.get("reasoning_effort") == "none":
        attempts.append({"reasoning_effort": "low"})
    if extra_kwargs:
        attempts.append({})
    return attempts


def _openai_create_with_fallback(client, args, messages, extra_kwargs):
    """Un paramètre d'optimisation ne doit jamais faire échouer une traduction :
    un `reasoning_effort` refusé par le SDK local (TypeError) ou par le serveur
    (400) est rejoué au niveau suivant. Tout autre refus remonte tel quel."""
    attempts = _reasoning_effort_attempts(extra_kwargs)
    for kwargs, fallback in zip(attempts, [*attempts[1:], None], strict=True):
        try:
            return client.chat.completions.create(model=args.model, messages=messages, **kwargs)
        except (TypeError, BadRequestError) as e:
            if fallback is None or not _rejects_reasoning_effort(e):
                raise
            suite = f"avec {fallback['reasoning_effort']!r}" if fallback else "sans ce paramètre"
            print(
                f"⚠ reasoning_effort={kwargs['reasoning_effort']!r} refusé — nouvel essai "
                f"{suite} (model={args.model})",
                file=sys.stderr,
            )
    raise AssertionError("inatteignable : le dernier essai rend ou lève")  # pragma: no cover


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
