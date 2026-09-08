"""Provider Claude (API Anthropic).

Le SDK refuse côté client un appel non streamé dont `max_tokens` laisse
présager plus de dix minutes — sa formule donne 921 s pour les 32 768 tokens
de `CLAUDE_MAX_TOKENS`. C'est le `timeout` explicite passé à l'appel qui l'en
dispense, pas un calibrage du plafond ; mesuré par un appel réel.
"""

import os

import anthropic

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_ANTHROPIC_API_KEY = "votre-cle-api-anthropic-par-defaut"  # pragma: allowlist secret


DEFAULT_MODEL_CLAUDE = "claude-sonnet-5"


ECO_MODEL_CLAUDE = "claude-haiku-4-5"


# 32768 : marge sur l'expansion cross-script (FR→JA/ZH/KO/AR/HI peuvent
# dépasser 16k tokens en sortie pour des segments source de 16k chars).
CLAUDE_MAX_TOKENS = 32768


# Plafond d'attente d'un appel Claude non-streamé. Doit rester SUPÉRIEUR à la
# durée d'un segment. (Le regen du dépôt n'a aucun chemin Claude : son
# REGEN_JOB_TIMEOUT ne s'applique pas ici.)
CLAUDE_TIMEOUT = float(os.getenv("CLAUDE_TIMEOUT", "900"))


# Types de blocs Anthropic qui ne portent pas de texte traduit. `thinking` et
# `redacted_thinking` apparaissent sur les modèles à raisonnement adaptatif.
_CLAUDE_NON_TEXT_BLOCK_TYPES = frozenset(
    {"thinking", "redacted_thinking", "tool_use", "tool_result"}
)


def _call_claude(client, args, prompt, segment):
    messages = [{"role": "user", "content": prompt + "\n\n" + segment}]
    # thinking désactivé explicitement : à partir de Sonnet 5, le raisonnement
    # adaptatif est actif par défaut. Il double les tokens de sortie facturés
    # et la latence sans rien apporter à une traduction.
    #
    # `timeout` explicite : depuis les SDK récents, un appel non-streamé dont
    # le `max_tokens` laisse présager plus de 10 minutes est refusé côté client
    # par un ValueError ("Streaming is required..."). Fournir un timeout revient
    # à assumer l'attente, et évite de passer au streaming pour un appel dont on
    # n'exploite que la réponse complète.
    response = client.messages.create(
        model=args.model,
        max_tokens=CLAUDE_MAX_TOKENS,
        thinking={"type": "disabled"},
        timeout=CLAUDE_TIMEOUT,
        messages=messages,
    )
    stop = _reason_name(response.stop_reason)
    if stop not in ("end_turn", "stop_sequence", None):
        raise RuntimeError(f"Claude abnormal stop_reason={stop!r} (model={args.model})")
    # Écarte les blocs non textuels : les modèles à raisonnement (Sonnet 5 et
    # au-delà, où la thinking adaptive est active par défaut) intercalent un
    # bloc `thinking` avant le bloc `text`. Un ThinkingBlock expose `.thinking`
    # et non `.text` — sans ce filtre, la traduction casserait sur un
    # AttributeError opaque au premier segment. On exclut par liste négative
    # plutôt que de n'accepter que `type == "text"` : un bloc au type absent ou
    # inconnu mais porteur de texte reste exploitable.
    text_blocks = [
        block
        for block in response.content
        if getattr(block, "type", None) not in _CLAUDE_NON_TEXT_BLOCK_TYPES
    ]
    if not text_blocks:
        types = [getattr(block, "type", "?") for block in response.content]
        raise RuntimeError(
            f"Claude n'a renvoyé aucun bloc de texte (model={args.model}, blocs={types})"
        )
    # Préserve la structure markdown entre blocs : pas de .strip() sur chaque
    # bloc (qui mangerait des newlines structurants), join avec "\n\n" entre
    # blocs distincts, et un seul .strip() global sur la sortie finale.
    return "\n\n".join(block.text for block in text_blocks).strip()


def _init_claude_client(args):
    args.model = args.model or (ECO_MODEL_CLAUDE if args.eco else DEFAULT_MODEL_CLAUDE)
    api_key = os.getenv("ANTHROPIC_API_KEY", DEFAULT_ANTHROPIC_API_KEY)
    if not api_key or api_key == DEFAULT_ANTHROPIC_API_KEY:
        raise ValueError(_missing_key_message("Claude", ["ANTHROPIC_API_KEY"]))
    return anthropic.Anthropic(api_key=api_key)
