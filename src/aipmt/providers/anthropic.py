"""Provider Claude (API Anthropic).

Le SDK refuse côté client un appel non streamé dont `max_tokens` laisse
présager plus de dix minutes — sa formule donne 921 s pour les 32 768 tokens
de `CLAUDE_MAX_TOKENS`. C'est le `timeout` explicite passé à l'appel qui l'en
dispense, pas un calibrage du plafond ; mesuré par un appel réel.

Le réglage qui coupe la réflexion varie d'un modèle à l'autre ; le premier
réglage accepté est mémorisé par modèle, pour ne pas repayer la cascade de
refus à chaque segment.
"""

import os
import sys

import anthropic

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_ANTHROPIC_API_KEY = "votre-cle-api-anthropic-par-defaut"  # pragma: allowlist secret


# Mesuré le 2026-10-18 sur les deux documents des mesures du README, quatorze
# langues chacun : 28 traductions sur 28 écrites et sans écart de structure.
DEFAULT_MODEL_CLAUDE = "claude-sonnet-5-5"


# Mesuré le même jour sur les mêmes documents, réflexion adaptative (cf.
# `_CLAUDE_THINKING_BY_MODEL`) : 26 traductions écrites sur 28, dont 23 sans
# écart, pour 0,57 $ — contre 28 écrites, 21 sans écart et 3,67 $ pour
# claude-haiku-4-5, le défaut précédent.
ECO_MODEL_CLAUDE = "claude-haiku-5-5"


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


# Réglage de réflexion des modèles pour qui `disabled` ne convient pas, relevé
# dans les capacités de l'API Models (`capabilities.thinking.types`) puis
# vérifié par un appel réel le 2026-10-18. Sonnet 5.5 refuse `disabled` par un
# 400 et désigne `between_tools`, qui coupe la réflexion préalable ; Opus 5.5
# et Fable 5.x n'acceptent ni l'un ni l'autre : `None` n'envoie alors aucun
# champ `thinking`, et le modèle réfléchit à sa guise. Haiku 5.5 accepte
# `disabled`, mais laisse alors des paragraphes entiers en français, que la
# garde des extraits non traduits refuse : 9 traductions écrites sur 28, contre
# 26 avec sa réflexion adaptative. Sonnet 5 et Haiku 4.5 acceptent `disabled`.
# Sans cette table, un modèle par défaut qui refuse `disabled` repaierait un
# 400 et un avertissement à chaque exécution.
_CLAUDE_THINKING_BY_MODEL = {
    "claude-sonnet-5-5": "between_tools",
    "claude-haiku-5-5": None,
    "claude-opus-5-5": None,
    "claude-fable-5-1": None,
    "claude-fable-5": None,
}


# Du moins coûteux au plus permissif, pour un modèle absent de la table.
_CLAUDE_THINKING_CASCADE = ("disabled", "between_tools", None)


# Réglage accepté par modèle, mémorisé au premier segment (même logique que
# `_GEMINI_ACCEPTED_THINKING_LEVEL`) : sans ce cache, un modèle hors table
# repayerait la cascade de refus à chaque segment de chaque fichier.
_CLAUDE_ACCEPTED_THINKING: dict[str, str | None] = {}


def _claude_thinking_order(model):
    """Réglages à essayer, dans l'ordre : celui qui a déjà été accepté, puis
    celui de la table, puis le reste de la cascade."""
    order = list(_CLAUDE_THINKING_CASCADE)
    for known in (_CLAUDE_THINKING_BY_MODEL, _CLAUDE_ACCEPTED_THINKING):
        if model in known:
            order.remove(known[model])
            order.insert(0, known[model])
    return order


def _claude_create_with_fallback(client, args, messages):
    """Descend les réglages de réflexion jusqu'à en trouver un que le modèle
    accepte, puis le mémorise. Même logique que `_gemini_generate_with_fallback` :
    un paramètre d'optimisation ne doit jamais faire échouer une traduction.
    Seul un 400 qui parle de `thinking` fait passer au réglage suivant."""
    last_error = None
    for setting in _claude_thinking_order(args.model):
        thinking = {} if setting is None else {"thinking": {"type": setting}}
        try:
            # `timeout` explicite : depuis les SDK récents, un appel non-streamé
            # dont le `max_tokens` laisse présager plus de 10 minutes est refusé
            # côté client par un ValueError ("Streaming is required..."). Fournir
            # un timeout revient à assumer l'attente, et évite de passer au
            # streaming pour un appel dont on n'exploite que la réponse complète.
            response = client.messages.create(
                model=args.model,
                max_tokens=CLAUDE_MAX_TOKENS,
                timeout=CLAUDE_TIMEOUT,
                messages=messages,
                **thinking,
            )
        except anthropic.BadRequestError as e:
            if "thinking" not in str(e).lower():
                raise
            last_error = e
            # Un réglage mémorisé qui devient invalide (changement côté API) ne
            # doit pas resservir : le segment suivant repart de la table.
            _CLAUDE_ACCEPTED_THINKING.pop(args.model, None)
            print(
                f"⚠ Claude refuse thinking={setting!r} — retry au réglage suivant "
                f"(model={args.model})",
                file=sys.stderr,
            )
        else:
            _CLAUDE_ACCEPTED_THINKING[args.model] = setting
            return response
    raise RuntimeError(
        f"Claude a refusé tous les réglages de réflexion (model={args.model}): {last_error}"
    )


def _call_claude(client, args, prompt, segment):
    messages = [{"role": "user", "content": prompt + "\n\n" + segment}]
    # Réflexion coupée, sauf exception mesurée (`_CLAUDE_THINKING_BY_MODEL`) :
    # à partir de Sonnet 5, le raisonnement adaptatif est actif par défaut, et
    # il double d'ordinaire les tokens de sortie facturés et la latence sans
    # rien apporter à une traduction.
    response = _claude_create_with_fallback(client, args, messages)
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
