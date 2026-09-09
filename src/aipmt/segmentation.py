"""Segmentation d'un document en morceaux traduisibles.

`segment_text` coupe aux frontières naturelles (paragraphes, titres, phrases)
sous une taille maximale en caractères, que le pipeline dérive de la fenêtre
du modèle. `MODEL_TOKEN_LIMITS` vit ici parce que la fenêtre d'un modèle est
une donnée de segmentation ; le provider OpenRouter y ÉCRIT la
fenêtre lue au préflight, d'où l'importance que tous les modules partagent le
même objet dictionnaire, jamais une copie.
"""

import re

# Fallback pour les modèles non listés dans MODEL_TOKEN_LIMITS.
DEFAULT_TOKEN_LIMIT = 128000


MODEL_TOKEN_LIMITS = {
    # OpenAI GPT-5.6 (génération courante). Contexte 1.05M, mais palier
    # tarifaire à 272K tokens d'input : au-delà, 2x input / 1.5x output sur
    # la requête entière.
    "gpt-5.6": 1050000,
    "grok-4.6": 500000,
    "grok-4.5": 500000,
    "grok-4.3": 1000000,
    "grok-build-0.1": 256000,
    "gpt-5.6-sol": 1050000,
    "gpt-5.6-terra": 1050000,
    "gpt-5.6-luna": 1050000,
    # OpenAI GPT-5.5 series (1M+ context)
    "gpt-5.5": 1050000,
    "gpt-5.5-pro": 1050000,
    # OpenAI GPT-5.4 series
    "gpt-5.4": 400000,
    "gpt-5.4-mini": 400000,
    "gpt-5.4-nano": 400000,
    "gpt-5.4-pro": 400000,
    # OpenAI GPT-5 series — retrait annoncé au 2026-12-11 (gpt-5*, o3*),
    # 2026-10-23 pour o1*/o3-mini/o4-mini/gpt-4.1-nano/gpt-4o.
    "gpt-5.2": 400000,
    "gpt-5.1": 400000,
    "gpt-5": 400000,
    "gpt-5-mini": 400000,
    "gpt-5-nano": 400000,
    "gpt-5.2-pro": 400000,
    "gpt-5-pro": 400000,
    # OpenAI GPT-4.1 series (1M context)
    "gpt-4.1": 1000000,
    "gpt-4.1-mini": 1000000,
    "gpt-4.1-nano": 1000000,
    # OpenAI O-series reasoning
    "o3": 200000,
    "o3-pro": 200000,
    "o3-mini": 200000,
    "o4-mini": 200000,
    "o1": 200000,
    "o1-pro": 200000,
    "o1-mini": 128000,
    "o1-preview": 128000,
    # OpenAI GPT-4o (legacy)
    "gpt-4o": 128000,
    "gpt-4o-mini": 128000,
    "chatgpt-4o-latest": 128000,
    # Anthropic Claude 5
    "claude-fable-5": 1000000,
    "claude-opus-5": 1000000,
    "claude-sonnet-5": 1000000,
    # Anthropic Claude 4.6+ : 1M context au prix standard (Opus 4.8, 4.7, 4.6,
    # Sonnet 4.6). Haiku 4.5 reste sur 200K (pas dans la liste 1M).
    "claude-opus-4-8": 1000000,
    "claude-opus-4-7": 1000000,
    "claude-opus-4-6": 1000000,
    "claude-sonnet-4-6": 1000000,
    # Anthropic Claude 4.5
    "claude-opus-4-5": 1000000,
    "claude-opus-4-5-20251101": 1000000,
    "claude-sonnet-4-5-20250929": 200000,
    "claude-haiku-4-5": 200000,
    "claude-haiku-4-5-20251001": 200000,
    # Mistral — 256K depuis la génération Large 3 / Small 4. La gamme
    # Magistral a été retirée le 2026-07-31. Les alias `-latest` fonctionnent
    # (vérifié par appel réel) mais leur résolution vers une version n'est pas
    # publiée : les IDs datés sont là pour qui veut épingler.
    "mistral-large-latest": 256000,
    "mistral-large-2512": 256000,
    "mistral-small-2603": 256000,
    "mistral-medium-latest": 256000,
    "mistral-small-latest": 256000,
    "ministral-14b-latest": 256000,
    "ministral-8b-latest": 256000,
    "ministral-3b-latest": 256000,
    # Google Gemini — la limite d'input exacte est 1048576, pas 1000000.
    # gemini-2.0-* et gemini-3-pro-preview ont été arrêtés en 2026.
    "gemini-3.7-flash": 1048576,
    "gemini-3.6-flash": 1048576,
    "gemini-3.5-flash": 1048576,
    "gemini-3.5-flash-lite": 1048576,
    "gemini-3.1-flash-lite": 1048576,
    "gemini-3.1-pro-preview": 1048576,
    "gemini-3.1-flash-lite-preview": 1048576,
    "gemini-3-flash-preview": 1048576,
    "gemini-2.5-pro": 1048576,
    "gemini-2.5-flash": 1048576,
    "gemini-2.5-flash-lite": 1048576,
}


def _find_last_h2_h3_match(segment, min_pos):
    """Retourne le dernier match \\n## ou \\n### à partir de min_pos, ou None."""
    last = None
    for m in re.finditer(r"\n#{2,3} ", segment):
        if m.start() >= min_pos:
            last = m
    return last


def _find_segment_breakpoint(segment, max_length):
    """Index de coupure dans la 2nde moitié du segment.

    Priorité : H2/H3, paragraphe, heading quelconque, fin de phrase, hard cut.
    """
    min_pos = max_length // 2

    heading_match = _find_last_h2_h3_match(segment, min_pos)
    if heading_match:
        return heading_match.start() + 1

    for candidate in (
        segment.rfind("\n\n"),
        segment.rfind("\n#"),
        segment.rfind(". "),
    ):
        if candidate >= min_pos:
            return candidate + 1

    return max_length


def segment_text(text, max_length):
    """Coupure sémantique dans la 2nde moitié de chaque segment, par priorité :
    H2/H3 > paragraphe > heading quelconque > fin de phrase > hard cut.
    Garde une section sémantique complète au début de chaque segment suivant.
    """
    segments = []
    while text:
        if len(text) <= max_length:
            segments.append(text)
            break
        next_index = _find_segment_breakpoint(text[:max_length], max_length)
        segments.append(text[:next_index])
        text = text[next_index:]
    return segments
