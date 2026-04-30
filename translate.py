#!/usr/bin/env python3

import os
import sys
import argparse
import time
import re
import glob

from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from mistralai import Mistral
import google.generativeai as genai
from langdetect import detect_langs, LangDetectException, DetectorFactory

# Détection de langue déterministe (évite les variations entre runs sur des textes courts)
DetectorFactory.seed = 0

# Charger les variables d'environnement depuis .env si présent
load_dotenv()

EXCLUDE_PATTERNS = ["traductions_", "venv", "PRIVACY.md"]

# Mapping langue → emoji drapeau pour les citations news (--news)
LANG_FLAGS = {
    "en": "🇬🇧", "es": "🇪🇸", "de": "🇩🇪", "it": "🇮🇹", "pt": "🇵🇹",
    "nl": "🇳🇱", "pl": "🇵🇱", "sv": "🇸🇪", "ro": "🇷🇴", "ja": "🇯🇵",
    "ko": "🇰🇷", "zh": "🇨🇳", "ar": "🇸🇦", "hi": "🇮🇳", "fr": "🇫🇷",
}

# Initialisation de la configuration avec les valeurs par défaut
DEFAULT_OPENAI_API_KEY = "votre-cle-api-openai-par-defaut"
DEFAULT_MISTRAL_API_KEY = "votre-cle-api-mistral-par-defaut"
DEFAULT_ANTHROPIC_API_KEY = "votre-cle-api-anthropic-par-defaut"
DEFAULT_GEMINI_API_KEY = "votre-cle-api-gemini-par-defaut"
# Modèles par défaut (mis à jour mars 2026) - Qualité
DEFAULT_MODEL_OPENAI = "gpt-5.5"
DEFAULT_MODEL_MISTRAL = "mistral-large-latest"
DEFAULT_MODEL_CLAUDE = "claude-sonnet-4-6"
DEFAULT_MODEL_GEMINI = "gemini-3.1-pro-preview"

# Modèles économiques (--eco)
ECO_MODEL_OPENAI = "gpt-5.4-mini"
ECO_MODEL_MISTRAL = "mistral-small-latest"
ECO_MODEL_CLAUDE = "claude-haiku-4-5-20251001"
ECO_MODEL_GEMINI = "gemini-3.1-flash-lite-preview"

# Limite de tokens par défaut pour les modèles non listés
DEFAULT_TOKEN_LIMIT = 128000

DEFAULT_SOURCE_LANG = "fr"
DEFAULT_TARGET_LANG = "en"
DEFAULT_SOURCE_DIR = "content/posts"
DEFAULT_TARGET_DIR = "traductions_en"
MODEL_TOKEN_LIMITS = {
    # OpenAI GPT-5.5 series (avril 2026, 1M+ context)
    "gpt-5.5": 1050000,
    "gpt-5.5-pro": 1050000,
    # OpenAI GPT-5.4 series (mars 2026)
    "gpt-5.4": 400000,
    "gpt-5.4-mini": 400000,
    "gpt-5.4-nano": 400000,
    "gpt-5.4-pro": 400000,
    # OpenAI GPT-5 series (2026)
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
    # Anthropic Claude 4.6+ (avril 2026, 1M context au prix standard
    # selon doc Anthropic — "Claude Mythos Preview, Opus 4.7, Opus 4.6,
    # and Sonnet 4.6 include the full 1M token context window at standard pricing").
    # Haiku 4.5 reste sur 200K (pas listé dans les modèles 1M).
    "claude-opus-4-7": 1000000,
    "claude-opus-4-6": 1000000,
    "claude-sonnet-4-6": 1000000,
    # Anthropic Claude 4.5 (2026)
    "claude-opus-4-5-20251101": 200000,
    "claude-sonnet-4-5-20250929": 200000,
    "claude-haiku-4-5-20251001": 200000,
    # Anthropic Claude 4.x
    "claude-opus-4-1-20250805": 200000,
    "claude-sonnet-4-20250514": 200000,
    # Anthropic Claude 3.x (legacy)
    "claude-3-5-sonnet-20240620": 200000,
    "claude-3-7-sonnet-20250219": 200000,
    # Mistral (2026)
    "mistral-large-latest": 128000,
    "mistral-small-latest": 128000,
    "magistral-medium-latest": 40000,
    "magistral-small-latest": 40000,
    # Google Gemini (2026)
    "gemini-3.1-pro-preview": 1000000,
    "gemini-3.1-flash-lite-preview": 1000000,
    "gemini-3-pro-preview": 1000000,
    "gemini-3-flash-preview": 1000000,
    "gemini-2.5-pro": 1000000,
    "gemini-2.5-flash": 1000000,
    "gemini-2.5-flash-lite": 1000000,
    "gemini-2.0-flash": 1000000,
    "gemini-2.0-flash-lite": 1000000,
    "gemini-2.0-pro-exp-02-05": 1000000,
}


def news_quote_placeholder(index):
    """Placeholder canonique pour les citations EN protégées en mode --news."""
    return f'<NEWSQUOTE id="{index}"/>'


def news_quote_placeholder_regex(index):
    """Accepte le XML canonique et la variante auto-formatée avec espace avant />."""
    return re.compile(rf'<NEWSQUOTE\s+id=["\']{index}["\']\s*/>')


# Lignes vraiment structurelles → à JETER (pas de contenu textuel utile)
# Inclut: code fence (```), hr/frontmatter delimiters (---), table separators (|),
# placeholders (#CODEBLOCK1#, <NEWSQUOTE id="1"/>…), YAML frontmatter keys (heroImage:, tags:, …),
# blockquotes (> …) car les citations protégées par --news y sont conservées
# verbatim source/cible, et continuations de liste/dict YAML (crochets, accolades,
# strings 'item' ou 'item', sur leur propre ligne après reformatage prettier).
_STRUCTURAL_LINE = re.compile(
    r"^\s*(?:"
    r"```"                                  # code fence
    r"|---"                                 # hr / frontmatter delimiter
    r"|\|"                                  # table separator
    r"|#[A-Z]+\d+#"                         # placeholder (#CODEBLOCK1#, etc.)
    r"|<NEWSQUOTE\s+id=['\"]\d+['\"]\s*/>"  # placeholder news XML
    r"|[A-Za-z_][\w-]*:(?:\s|$)"            # YAML key: (title:, tags:, …)
    r"|>"                                   # blockquote
    r"|[\[\]{}]"                            # YAML list/dict bracket on own line
    r"|['\"][^'\"\n]+['\"]\s*,?\s*$"        # YAML string item ('item' or "item", possibly with trailing comma)
    r")"
)
# Préfixes Markdown inline → à STRIPPER (on garde le texte derrière)
_INLINE_MD_PREFIX = re.compile(r"^\s*(?:[-*+]\s+|#{1,6}\s+|\d+\.\s+)")
_URL_OR_PLACEHOLDER = re.compile(
    r"https?://\S+|#(?:CODEBLOCK|INLINECODE)\d+#|<NEWSQUOTE\s+id=['\"]\d+['\"]\s*/>"
)
def segment_text(text, max_length):
    """
    Divise un texte Markdown en segments ne dépassant pas la longueur maximale spécifiée.

    Priorité sémantique stricte pour le point de coupure (dans la 2nde moitié du segment) :
      1. Heading H2 ou H3 (\\n## ou \\n### ) — préserve un contexte sémantique complet
      2. Paragraphe (\\n\\n)
      3. Heading niveau quelconque (\\n#)
      4. Fin de phrase (. )
      5. Hard cut (max_length) si rien au-delà du seuil min_pos

    Args:
        text (str): Texte Markdown à diviser.
        max_length (int): Longueur maximale de chaque segment.

    Returns:
        list[str]: Liste des segments de texte Markdown.
    """

    segments = []
    while text:
        if len(text) <= max_length:
            segments.append(text)
            break
        segment = text[:max_length]
        next_index = max_length
        # Seuil pour éviter coupures trop précoces
        min_pos = max_length // 2

        # Priorité 1: dernier heading H2/H3 dans la 2nde moitié
        heading_match = None
        for m in re.finditer(r"\n#{2,3} ", segment):
            if m.start() >= min_pos:
                heading_match = m
        if heading_match:
            next_index = heading_match.start() + 1
        else:
            # Priorité 2-4: paragraphe, heading quelconque, fin de phrase
            for candidate in (
                segment.rfind("\n\n"),
                segment.rfind("\n#"),
                segment.rfind(". "),
            ):
                if candidate >= min_pos:
                    next_index = candidate + 1
                    break
            # else: hard cut à max_length (next_index inchangé)

        segments.append(text[:next_index])
        text = text[next_index:]

    return segments


def _reason_name(reason):
    """Normalise un finish_reason/stop_reason : extrait .name si enum, sinon retourne tel quel."""
    return getattr(reason, "name", reason)


def _extract_source_windows(segment):
    """Retourne des fenêtres textuelles 'saines' (≥120 chars) issues du segment source,
    en regroupant les paragraphes wrappés. Pour les paragraphes longs (≥600 chars), extrait
    3 fenêtres (début/milieu/fin) pour couvrir le cas où le source non-traduit serait au milieu."""
    windows = []
    for para in re.split(r"\n\s*\n", segment):
        kept_lines = []
        for line in para.split("\n"):
            if _STRUCTURAL_LINE.match(line):
                continue
            kept_lines.append(_INLINE_MD_PREFIX.sub("", line))
        if not kept_lines:
            continue
        joined = " ".join(kept_lines)
        cleaned = _URL_OR_PLACEHOLDER.sub("", joined)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        n = len(cleaned)
        if n < 120:
            continue
        if n >= 600:
            mid = n // 2
            windows.extend([
                cleaned[:200],
                cleaned[mid - 100 : mid + 100],
                cleaned[-200:],
            ])
        else:
            windows.append(cleaned[:200])
    return windows


def _validate_translation_output(segment, translated_text, args, is_translation_note):
    """Vérifie que la sortie n'est pas le segment source retourné brut (bug silent-failure)
    ou une traduction qui serait restée dans la langue source.

    Couche 1 (toujours active): fenêtres source retrouvées verbatim dans la sortie.
    Couche 2 (≥100 chars): langdetect probabiliste sur la langue de sortie.
    """
    if is_translation_note:
        return
    if args.source_lang == args.target_lang:
        return
    stripped = translated_text.strip()
    if not stripped:
        return

    out_norm = re.sub(r"\s+", " ", stripped).casefold()
    for window in _extract_source_windows(segment):
        window_norm = re.sub(r"\s+", " ", window).casefold()
        if window_norm in out_norm:
            raise RuntimeError(
                f"Output contains untranslated source excerpt "
                f"(model={args.model}, target={args.target_lang}, "
                f"matched window: {window_norm[:100]!r})"
            )

    if len(stripped) < 100:
        return
    try:
        probas = {p.lang: p.prob for p in detect_langs(stripped)}
    except LangDetectException:
        return
    src_p = probas.get(args.source_lang, 0.0)
    tgt_p = probas.get(args.target_lang, 0.0)
    if src_p > 0.80 and tgt_p < 0.20:
        raise RuntimeError(
            f"Output language mismatch: expected {args.target_lang} (p={tgt_p:.2f}), "
            f"got {args.source_lang} (p={src_p:.2f}), model={args.model}, "
            f"first 200 chars: {stripped[:200]!r}"
        )


def translate(
    text, client, args, use_mistral=False, use_claude=False, use_gemini=False, is_translation_note=False
):
    """
    Traduit un texte à l'aide de l'API OpenAI, Mistral AI, Claude ou Gemini, selon les paramètres spécifiés.
    Cette fonction segmente d'abord le texte pour s'assurer qu'il respecte la limite de tokens du modèle.
    Elle utilise un argument optionnel 'is_translation_note' pour gérer différemment les notes de traduction.

    Args:
        text (str): Texte à traduire.
        client: Objet client de l'API de traduction (OpenAI, Mistral AI, Claude ou Gemini).
        args: Objet argparse contenant les arguments de la ligne de commande.
        use_mistral (bool): Si True, utilise l'API Mistral AI pour la traduction.
        use_claude (bool): Si True, utilise l'API Claude pour la traduction.
        use_gemini (bool): Si True, utilise l'API Gemini pour la traduction.
        is_translation_note (bool): Si True, le texte est une note de traduction.

    Returns:
        str: Texte traduit.
    """

    model_limit = MODEL_TOKEN_LIMITS.get(args.model, DEFAULT_TOKEN_LIMIT)

    # Liste pour repérer les modèles de la série o1 : "o1", "o1-mini", "o1-preview"
    o1_series = ["o1", "o1-mini", "o1-preview"]

    # Limite de segmentation raisonnable (16k caractères pour fiabilité)
    segments = segment_text(text, min(16000, model_limit))
    translated_segments = []

    for segment in segments:
        try:
            # FIX: Séparation des instructions (system) et du contenu (user)
            # Avant: le segment était inclus dans prompt_message ET envoyé en user (doublon)
            if is_translation_note:
                system_instructions = (
                    f"Translate directly to {args.target_lang} without any additions. "
                    "Do NOT modify URLs or image paths. "
                    "Output only the translation, nothing else."
                )
            else:
                system_instructions = (
                    f"Translate this Markdown document from {args.source_lang} to {args.target_lang}. "
                    "Output ONLY the translated Markdown, with no comments or explanations. "
                    "Preserve the complete Markdown structure: headings, lists, tables, blockquotes, "
                    "front matter, MDX/HTML tags, directives, comments, and blank-line separation. "
                    "For Markdown links [text](url), translate the visible link text and keep the URL unchanged. "
                    "For Markdown tables, preserve pipes, separator rows, alignment markers, numbers, units, "
                    "IDs, and model/product names; translate human-readable headers and cell labels. "
                    "Do NOT modify URLs, image paths, anchors, IDs, slugs, code blocks, inline code, "
                    "template variables like {variable}, or placeholders. "
                    "In YAML/TOML/JSON front matter, preserve keys, nesting, arrays, booleans, numbers, "
                    "dates, paths, file references, identifiers, and tag-like taxonomies. Translate only "
                    "human-readable prose string values. If a locale/lang/language field already exists "
                    f"and contains a language code, update that value to {args.target_lang}; do not add such "
                    "a field if it is absent. Use valid quoting when translated strings contain apostrophes."
                )

            # Ajout des instructions news si --news actif
            if not is_translation_note and args.news:
                target_flag = LANG_FLAGS.get(args.target_lang, "")
                placeholder_example = news_quote_placeholder(0)
                if args.target_lang == "en":
                    news_rules = (
                        "\n\n<news_citation_contract version=\"4\">"
                        "\n<placeholder_rule>"
                        f"\nNews quote placeholders are XML self-closing tags like `{placeholder_example}`."
                        "\nThey are protected technical tags, not translatable text."
                        "\nCopy every `<NEWSQUOTE id=\"N\"/>` tag exactly, preserving the Latin tag name, id number, quotes, and slash."
                        "\nDo not replace the XML tag with quote text. Do not translate, localize, rename, delete, or reorder it."
                        "\nAcceptable formatting is only the exact input tag; do not add explanations around it."
                        "\n</placeholder_rule>"
                        "\n<citation_rule target=\"en\">"
                        "\nFor each citation block, REMOVE the empty blockquote line (`>`) and REMOVE the whole source-translation line `> 🇫🇷 _..._`."
                        "\nKeep only the `<NEWSQUOTE id=\"N\"/>` tag and the attribution line `> — [...](url)`."
                        "\nTranslate attribution link text only; keep URL unchanged."
                        "\n</citation_rule>"
                        "\n<correct_output_shape>"
                        "\n<NEWSQUOTE id=\"N\"/>"
                        "\n> — [translated attribution text](url unchanged)"
                        "\n</correct_output_shape>"
                        "\n</news_citation_contract>"
                    )
                else:
                    news_rules = (
                        "\n\n<news_citation_contract version=\"4\">"
                        "\nThese rules are CRITICAL and override ordinary translation instincts."
                        "\n"
                        "\n<placeholder_rule>"
                        f"\nNews quote placeholders are XML self-closing tags like `{placeholder_example}`."
                        "\nThey are protected technical tags, not words and not content."
                        "\nEach `<NEWSQUOTE id=\"N\"/>` tag MUST appear in output with the same id number, in the same citation position."
                        "\nDo not translate the tag name. Do not localize NEWSQUOTE into Polish, Chinese, Korean, Arabic, Hindi, or any other language."
                        "\nDo not replace the XML tag with the quote text. Do not delete it. Do not wrap it in code fences."
                        "\nBefore finalizing output: count `<NEWSQUOTE` tags in the output. The count MUST equal the source input."
                        "\n</placeholder_rule>"
                        "\n"
                        "\n<flag_rule>"
                        f"For each citation block: replace the source flag 🇫🇷 with {target_flag} and translate the italic text COMPLETELY to {args.target_lang}."
                        "\nCOMPLETE = same number of sentences, all concepts included, no truncation or summarization. The placeholder represents the original English quote — translate FROM its meaning."
                        f"\nThe {target_flag} emoji MUST ONLY appear inside blockquote citation lines (starting with `> `), and ONLY ONCE per citation."
                        "\n</flag_rule>"
                        "\n"
                        "\n<examples>"
                        "\nExample 1 — Polish target (PL):"
                        "\nINPUT:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\n>"
                        "\n> 🇫🇷 _Une décennie de travail._"
                        "\n> — [@GoogleAI sur X](https://x.com/google)"
                        "\nCORRECT OUTPUT:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\n>"
                        "\n> 🇵🇱 _Dekada pracy._"
                        "\n> — [@GoogleAI na X](https://x.com/google)"
                        "\n"
                        "\nExample 2 — Chinese target (ZH), tag MUST stay in Latin script:"
                        "\nINPUT:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\n>"
                        "\n> 🇫🇷 _Une décennie de travail._"
                        "\n> — [@GoogleAI sur X](https://x.com/google)"
                        "\nCORRECT OUTPUT:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\n>"
                        "\n> 🇨🇳 _十年磨一剑。_"
                        "\n> — [@GoogleAI 在 X 上](https://x.com/google)"
                        "\nWRONG: `<新闻引用 id=\"0\"/>`, `<QUOTE id=\"0\"/>`, or replacing the tag with the quote."
                        "\n"
                        "\nExample 3 — Korean target (KO):"
                        "\nINPUT:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\n>"
                        "\n> 🇫🇷 _Une décennie de travail._"
                        "\n> — [@GoogleAI sur X](https://x.com/google)"
                        "\nCORRECT OUTPUT:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\n>"
                        "\n> 🇰🇷 _10년간의 작업._"
                        "\n> — [@GoogleAI X에서](https://x.com/google)"
                        "\nWRONG: `<뉴스인용 id=\"0\"/>` or any Korean tag name."
                        "\n"
                        "\nExample 4 — Arabic/Hindi scripts:"
                        "\nCORRECT OUTPUT tag line:"
                        "\n<NEWSQUOTE id=\"0\"/>"
                        "\nWRONG: translating NEWSQUOTE, changing quotes, changing id, or removing the slash."
                        "\n</examples>"
                        "\n"
                        f"\nResult format for {args.target_lang} target:\n<NEWSQUOTE id=\"N\"/>\n>\n> {target_flag} _translated italic text in {args.target_lang}_\n> — [attribution text translated](url unchanged)"
                        "\n</news_citation_contract>"
                    )
                news_common = (
                    "\n\n<markdown_translation_contract>"
                    "\n<completion_rules>"
                    "\n- The output MUST include EVERY part of the source document."
                    "\n- Preserve ALL headings (any level: `#`, `##`, `###`, `####`, etc.) at the SAME level and in the SAME order as the source."
                    "\n- Preserve ALL paragraphs, lists, code blocks, tables, and blockquotes from the source."
                    "\n- Translate the document FROM start TO end. The output must reach the same final element as the source (last paragraph, last list item, last section)."
                    "\n- DO NOT truncate, summarize, merge, or skip any element."
                    "\n</completion_rules>"
                    "\n<markdown_structure_rules>"
                    "\n- ALWAYS preserve a blank line between a horizontal rule `---` and any heading. They MUST NEVER be on the same line."
                    "\n  ❌ WRONG: '--- ## My Heading' (collapsed on single line)"
                    "\n  ✅ RIGHT: '---' on its own line, blank line, then '## My Heading' on its own line"
                    "\n- Same rule for inline links: a markdown link `](url)` must NEVER be on the same line as a following heading."
                    "\n- In Markdown tables, preserve pipes, separator rows, alignment markers, numbers, units, IDs, and product/model names. Translate human-readable table headers and cell labels."
                    "\n- Keep technical terms, acronyms, brand names, programming jargon, and product names in their original language (do not translate them)."
                    "\n- In front matter, translate only human-readable prose string values. Keep technical or structural fields unchanged: dates, slugs, paths, file references, tag arrays, ids, booleans, numbers, and identifier-like values. Update an existing locale/lang/language code to the target language; do not add one if absent."
                    "\n</markdown_structure_rules>"
                    "\n<final_checklist>"
                    "\nBefore returning, verify silently: all headings are present; all `<NEWSQUOTE` tags are present; all URLs are unchanged; the target flag count is correct; no source flag remains; the final section is complete."
                    "\nReturn ONLY the translated Markdown. No checklist, no commentary."
                    "\n</final_checklist>"
                    "\n</markdown_translation_contract>"
                )
                system_instructions += news_rules + news_common

            if use_mistral:
                messages = [{"role": "user", "content": system_instructions + "\n\n" + segment}]
                response = client.chat.complete(model=args.model, messages=messages)
                finish = _reason_name(response.choices[0].finish_reason)
                if finish not in ("stop", "STOP", None):
                    raise RuntimeError(f"Mistral abnormal finish_reason={finish!r} (model={args.model})")
                translated_text = response.choices[0].message.content.strip()

            elif use_claude:
                messages = [{"role": "user", "content": system_instructions + "\n\n" + segment}]
                response = client.messages.create(
                    model=args.model, max_tokens=16384, messages=messages
                )
                stop = _reason_name(response.stop_reason)
                if stop not in ("end_turn", "stop_sequence", None):
                    raise RuntimeError(f"Claude abnormal stop_reason={stop!r} (model={args.model})")
                translated_texts = [
                    block.text.strip() for block in response.content
                ]
                translated_text = " ".join(translated_texts)

            elif use_gemini:
                model = client.GenerativeModel(args.model)
                response = model.generate_content(system_instructions + "\n\n" + segment)
                candidates = getattr(response, "candidates", None) or []
                if candidates:
                    fr_name = _reason_name(getattr(candidates[0], "finish_reason", None))
                    if fr_name not in ("STOP", "FINISH_REASON_STOP", None):
                        raise RuntimeError(f"Gemini abnormal finish_reason={fr_name!r} (model={args.model})")
                try:
                    translated_text = response.text.strip()
                except (ValueError, AttributeError) as e:
                    raise RuntimeError(
                        f"Gemini response has no text (likely blocked or empty, model={args.model}): {e}"
                    )

            else:
                # OpenAI (ChatGPT, o1, etc.)
                if args.model in o1_series:
                    messages = [
                        {"role": "user", "content": system_instructions + "\n\n" + segment},
                    ]
                else:
                    messages = [
                        {"role": "system", "content": system_instructions},
                        {"role": "user", "content": segment},
                    ]

                # Active reasoning_effort pour la famille GPT-5.x. Le défaut medium
                # garde le coût bas ; le wrapper news peut demander high pour un retry
                # cheap-first avant fallback premium.
                # Fallback silencieux si le paramètre n'est pas supporté par le modèle.
                extra_kwargs = {}
                if args.model.startswith("gpt-5") and not is_translation_note:
                    extra_kwargs["reasoning_effort"] = getattr(args, "reasoning_effort", "medium")
                try:
                    response = client.chat.completions.create(
                        model=args.model, messages=messages, **extra_kwargs
                    )
                except TypeError:
                    # Vieille version SDK qui ne connaît pas reasoning_effort.
                    response = client.chat.completions.create(
                        model=args.model, messages=messages
                    )
                except Exception as e:
                    # API rejette le paramètre (modèle non éligible) → retry sans.
                    if "reasoning_effort" in str(e) and extra_kwargs:
                        response = client.chat.completions.create(
                            model=args.model, messages=messages
                        )
                    else:
                        raise
                finish = _reason_name(response.choices[0].finish_reason)
                if finish not in ("stop", "STOP", None):
                    raise RuntimeError(f"OpenAI abnormal finish_reason={finish!r} (model={args.model})")
                translated_text = response.choices[0].message.content.strip()

            _validate_translation_output(segment, translated_text, args, is_translation_note)
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la traduction : {e}")

        translated_segments.append(translated_text)

    return " ".join(translated_segments)  # TODO: cleaner segment join (espace après newline si coupure sur heading)


def translate_markdown_file(
    file_path,
    output_path,
    client,
    args,
    use_mistral,
    use_claude,
    use_gemini,
    add_translation_note=False,
    force=False,
):
    """
    Traduit un fichier Markdown en utilisant les modèles de traitement du langage naturel de OpenAI, Mistral AI, Claude ou Gemini.

    Args:
        file_path (str): Chemin complet vers le fichier d'entrée.
        output_path (str): Chemin complet vers le fichier de sortie.
        client: Objet client de traduction.
        args: Arguments supplémentaires pour la traduction.
        use_mistral (bool): Indique si l'API Mistral AI doit être utilisée pour la traduction.
        use_claude (bool): Indique si l'API Claude doit être utilisée pour la traduction.
        use_gemini (bool): Indique si l'API Gemini doit être utilisée pour la traduction.
        add_translation_note (bool): Indique si une note de traduction doit être ajoutée.
        force (bool): Indique si la traduction doit être forcée même si une traduction existe déjà.

    Returns:
        str: "success" si la traduction a été écrite, "skipped" si le fichier était vide ou
             si la sortie existait déjà sans --force, "failure" si une exception a été levée.
    """

    # Fallback pour le handler d'exception : si os.path.join lève, le except a un nom valide
    relative_file_path = file_path
    try:
        # Calcul des chemins relatifs pour un affichage plus lisible
        relative_file_path = os.path.join(
            args.source_dir, os.path.relpath(file_path, start=args.source_dir)
        )
        relative_output_path = os.path.join(
            args.target_dir, os.path.relpath(output_path, start=args.target_dir)
        )

        print(f"Traitement du fichier : {relative_file_path}")
        start_time = time.time()

        # Lecture du contenu du fichier
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if not content:
            print(
                f"Le fichier '{relative_file_path}' est vide, aucune traduction n'est effectuée."
            )
            return "skipped"

        # Extraction et remplacement des blocs de code pour les préserver pendant la traduction
        # 1) Blocs de code fencés (``` ... ```)
        fenced_regex = re.compile(
            r"(^```(?:[\w-]*)?\n)(.*?)(^```$)",
            re.DOTALL | re.MULTILINE,
        )
        code_blocks = [match.group(0) for match in fenced_regex.finditer(content)]
        block_placeholders = [f"#CODEBLOCK{index}#" for index, _ in enumerate(code_blocks)]
        for placeholder, code_block in zip(block_placeholders, code_blocks):
            content = content.replace(code_block, placeholder)

        # 2) Code inline (` ... `) - protège aussi les backticks
        # Regex: matche `contenu` mais pas les blocs déjà remplacés ni les doubles backticks ``
        inline_regex = re.compile(r"(?<!`)(`[^`\n]+?`)(?!`)")
        inline_codes = [match.group(0) for match in inline_regex.finditer(content)]
        inline_placeholders = [f"#INLINECODE{index}#" for index, _ in enumerate(inline_codes)]
        for placeholder, inline_code in zip(inline_placeholders, inline_codes):
            content = content.replace(inline_code, placeholder, 1)  # Replace one at a time to handle duplicates

        # 3) Citations news (--news mode) : protéger les quotes EN originales
        original_quotes = []
        attribution_urls = []
        if args.news:
            # Pattern: > EN quote \n > \n > FLAG _translation_ \n > — [@account](url)
            # La citation EN peut être entre guillemets ou non selon la source X/blog.
            citation_regex = re.compile(
                r'(^> (?!— ).+?)[ \t]*\n'         # Groupe 1: citation EN brute
                r'>[ \t]*\n'                        # ligne blockquote vide
                r'(^> .+_)[ \t]*\n'                # Groupe 2: drapeau + traduction italique
                r'(^> — .+?)[ \t]*$',              # Groupe 3: ligne d'attribution
                re.MULTILINE,
            )

            def citation_replacer(match):
                idx = len(original_quotes)
                original_quotes.append(match.group(1))
                # Extraire l'URL d'attribution pour validation
                url_match = re.search(r'\((.+?)\)', match.group(3))
                if url_match:
                    attribution_urls.append(url_match.group(1))
                # Remplacer la quote EN par un placeholder, garder le reste pour le LLM
                return f"{news_quote_placeholder(idx)}\n>\n{match.group(2)}\n{match.group(3)}"

            content = citation_regex.sub(citation_replacer, content)
            if original_quotes:
                print(f"  → {len(original_quotes)} citation(s) EN protégée(s)")

        # Traduction du contenu
        translated_content = translate(content, client, args, use_mistral, use_claude, use_gemini)

        # Restauration des blocs de code et code inline dans le contenu traduit
        # 1) Restaurer le code inline d'abord (ordre inverse de l'extraction)
        for placeholder, inline_code in zip(inline_placeholders, inline_codes):
            translated_content = translated_content.replace(placeholder, inline_code)
        # 2) Restaurer les blocs fencés
        for placeholder, code_block in zip(block_placeholders, code_blocks):
            translated_content = translated_content.replace(placeholder, code_block)

        # 3) Validation AVANT restauration : vérifier que les placeholders sont intacts
        if args.news and original_quotes:
            for idx in range(len(original_quotes)):
                placeholder = news_quote_placeholder(idx)
                if not news_quote_placeholder_regex(idx).search(translated_content):
                    raise RuntimeError(
                        f"VALIDATION: Placeholder {placeholder} manquant dans la traduction "
                        "(le LLM l'a supprimé ou modifié)"
                    )

        # 4) Restaurer les citations EN news
        for idx, quote in enumerate(original_quotes):
            translated_content, restored_count = news_quote_placeholder_regex(idx).subn(quote, translated_content)
            if restored_count != 1:
                raise RuntimeError(
                    f"VALIDATION: Placeholder {news_quote_placeholder(idx)} restauré "
                    f"{restored_count} fois (attendu: 1)"
                )

        # 4b) Normalisation des séparateurs markdown collés (post-LLM cleanup)
        # Certains LLMs (gpt-5.4-mini notamment) collent des éléments de structure
        # sur la même ligne au point de jonction des segments. Ces patterns sont
        # toujours invalides en markdown standard (un heading doit être en début
        # de ligne, précédé d'une ligne vide).
        #
        #   Pattern 1 (générique) : "--- ## Title" → "---\n\n## Title"
        #     Un séparateur HR (---) immédiatement suivi d'un heading sur la même
        #     ligne. Toujours invalide quel que soit le document markdown.
        #
        #   Pattern 2 (générique) : "](url) ## Title" → "](url)\n\n## Title"
        #     Une fin de lien markdown ](url) immédiatement suivie d'un heading
        #     sur la même ligne. Toujours invalide quel que soit le document.
        #
        # Cas réels documentés : ia-actualites-29-apr-2026.mdx (PL/JA/ZH/9 langues),
        # ia-actualites-11-mar-2026.mdx (PL). Aucun de ces patterns n'a de cas
        # d'usage légitime dans un document markdown bien formé.
        translated_content = re.sub(r'^--- (##+ )', r'---\n\n\1', translated_content, flags=re.MULTILINE)
        translated_content = re.sub(r'(\]\([^)]+\)) (##+ )', r'\1\n\n\2', translated_content)
        if re.search(r'^---[ \t]+##+ ', translated_content, flags=re.MULTILINE):
            raise RuntimeError("VALIDATION: séparateur markdown collé à un heading (`--- ##`)")
        if re.search(r'\]\([^)]+\)[ \t]+##+ ', translated_content):
            raise RuntimeError("VALIDATION: lien markdown collé à un heading (`](url) ##`)")

        # 4c) Source-flag cleanup (post-LLM, --news only)
        # En mode --news avec source=FR et target≠FR, le drapeau 🇫🇷 ne devrait
        # jamais apparaître dans la sortie (on traduit DEPUIS le FR). Deux cas
        # de "résidu 🇫🇷" sont à corriger :
        #
        #   Cas A — target == "en" : la ligne `> 🇫🇷 _trad FR_` aurait dû être
        #   SUPPRIMÉE par le LLM (la quote EN au-dessus suffit). Elle reste
        #   parfois en place (LLM EN oublie l'instruction du system prompt).
        #   On supprime alors la ligne entière + la ligne `>` vide qui précède.
        #
        #   Cas B — target != "en" : la ligne `> 🇫🇷 _trad target_` a été TRADUITE
        #   correctement par le LLM mais le drapeau n'a pas été échangé en
        #   `> {flag_target} _trad_`. Vu sur PL (run du 29 avr 2026, citation TPU
        #   8e gen). On échange juste le drapeau, le contenu est OK.
        if args.news and args.source_lang != args.target_lang:
            source_flag = LANG_FLAGS.get(args.source_lang)
            target_flag = LANG_FLAGS.get(args.target_lang)
            if source_flag and source_flag in translated_content:
                if args.target_lang == "en":
                    # Cas A : supprimer la ligne entière `> 🇫🇷 _..._` ainsi que la
                    # ligne blockquote vide précédente (`>`) qui devient orpheline.
                    pattern = re.compile(
                        r'(^|\n)>\s*\n(>\s*' + re.escape(source_flag) + r'[^\n]*\n)',
                        flags=re.MULTILINE
                    )
                    new_content, n = pattern.subn(r'\1', translated_content)
                    if n > 0:
                        translated_content = new_content
                        print(f"  → {n} ligne(s) `> {source_flag} _trad_` supprimée(s) en cible EN (cleanup)")
                elif target_flag:
                    # Cas B : swap drapeau source → drapeau cible
                    count = translated_content.count(source_flag)
                    translated_content = translated_content.replace(source_flag, target_flag)
                    print(f"  → {count} drapeau(x) source {source_flag} remplacé(s) par {target_flag} (cleanup)")

        # 5) Validation post-restauration des citations news
        if args.news and original_quotes:
            for quote in original_quotes:
                if quote not in translated_content:
                    raise RuntimeError("VALIDATION: citation EN brute non restaurée dans la traduction")
            for url in attribution_urls:
                if url not in translated_content:
                    raise RuntimeError(f"VALIDATION: URL d'attribution '{url}' manquante dans la traduction")
            if re.search(r'<NEWSQUOTE\s+id=["\']\d+["\']\s*/>|#NEWSQUOTE\d+#', translated_content):
                raise RuntimeError("VALIDATION: placeholder news résiduel après restauration")
            if args.target_lang == "en":
                for lang_code, flag in LANG_FLAGS.items():
                    if lang_code != "en" and flag in translated_content:
                        raise RuntimeError(
                            f"VALIDATION: Drapeau {flag} ({lang_code}) trouvé dans la traduction EN "
                            "(devrait être absent)"
                        )
            else:
                target_flag = LANG_FLAGS.get(args.target_lang)
                if target_flag:
                    flag_count = translated_content.count(target_flag)
                    expected = len(original_quotes)
                    if flag_count != expected:
                        raise RuntimeError(
                            f"VALIDATION: Drapeau {target_flag} trouvé {flag_count} fois "
                            f"(attendu: {expected})"
                        )
                source_flag = LANG_FLAGS.get(args.source_lang)
                if source_flag and source_flag in translated_content:
                    raise RuntimeError(
                        f"VALIDATION: Drapeau source {source_flag} encore présent dans la traduction"
                    )

        # Ajout de la note de traduction si nécessaire
        if add_translation_note:
            translation_note = translate(
                "Ce document a été traduit de la version "
                + args.source_lang
                + " vers la langue "
                + args.target_lang
                + " en utilisant le modèle "
                + args.model
                + ". Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator",
                client,
                args,
                use_mistral,
                use_claude,
                use_gemini,
                True,
            )
            translated_content += "\n\n**" + translation_note + "**\n\n"

        # Écriture du contenu traduit dans le fichier de sortie
        clean_output_path = os.path.normpath(output_path)
        if os.path.exists(clean_output_path) and not force:
            print(
                f"Le fichier '{relative_output_path}' existe déjà, aucune traduction n'est effectuée."
            )
            return "skipped"
        with open(clean_output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

        end_time = time.time()
        print(
            f"Fichier '{relative_file_path}' traduit en {end_time - start_time:.2f} secondes et enregistré sous : {relative_output_path}"
        )
        return "success"
    except IOError as e:
        print(f"Erreur lors du traitement du fichier '{relative_file_path}': {e}")
        return "failure"
    except Exception as e:
        print(
            f"Une erreur inattendue est survenue lors de la traduction du fichier '{relative_file_path}': {e}\n"
            "Veuillez relancer le traitement pour ce fichier."
        )
        return "failure"


def is_excluded(path):
    """
    Vérifie si le chemin donné correspond à l'un des motifs d'exclusion.

    Cette fonction parcourt la liste des motifs d'exclusion définis dans EXCLUDE_PATTERNS.
    Si l'un de ces motifs est trouvé dans le chemin fourni, la fonction renvoie True,
    indiquant que le chemin doit être exclu du processus de traduction.

    Args:
        path (str): Le chemin du fichier ou du répertoire à vérifier.

    Returns:
        bool: True si le chemin correspond à l'un des motifs d'exclusion, False sinon.
    """

    for pattern in EXCLUDE_PATTERNS:
        if pattern in path:
            return True
    return False


def translate_directory(
    input_dir,
    output_dir,
    client,
    args,
    use_mistral,
    use_claude,
    use_gemini,
    add_translation_note,
    force,
):
    """
    Traduit tous les fichiers markdown dans le répertoire d'entrée et ses sous-répertoires.

    Args:
        input_dir (str): Chemin vers le répertoire d'entrée.
        output_dir (str): Chemin vers le répertoire de sortie.
        client: Objet client de traduction.
        args: Arguments supplémentaires pour la traduction.
        use_mistral (bool): Indique si l'API Mistral AI doit être utilisée pour la traduction.
        use_claude (bool): Indique si l'API Claude doit être utilisée pour la traduction.
        use_gemini (bool): Indique si l'API Gemini doit être utilisée pour la traduction.
        add_translation_note (bool): Indique si une note de traduction doit être ajoutée.
        force (bool): Indique si la traduction doit être forcée même si une traduction existe déjà.

    Returns:
        dict: {"failed": list[str], "skipped": list[str]} — chemins des fichiers qui ont
        échoué et ceux qui ont été skipped (déjà traduits, fichier vide, etc.).
    """

    failed_files = []
    skipped_files = []

    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_base_dir = os.path.basename(output_dir)

    for root, dirs, files in os.walk(input_dir, topdown=True):
        if is_excluded(root) or root.startswith(output_dir):
            continue

        if (
            os.path.basename(root) == output_base_dir
            and os.path.abspath(os.path.join(root, "..")) == input_dir
        ):
            continue

        for file in files:
            if (file.endswith(".md") or file.endswith(".mdx")) and not is_excluded(file):
                file_path = os.path.join(root, file)
                base, ext = os.path.splitext(file)
                if args.keep_filename:
                    output_file = file
                elif args.include_model:
                    output_file = f"{base}-{args.target_lang}-{args.model}.md"
                else:
                    output_file = f"{base}-{args.target_lang}.md"
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, output_file)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                if args.keep_filename:
                    existing_translation = os.path.exists(output_path)
                else:
                    target_language_files = glob.glob(
                        f"{output_dir}/**/{base}-{args.target_lang}*.md", recursive=True
                    ) + glob.glob(
                        f"{output_dir}/**/{base}-*{args.target_lang}.md", recursive=True
                    )
                    existing_translation = any(
                        [os.path.exists(file) for file in target_language_files]
                    )
                if not existing_translation or force:
                    status = translate_markdown_file(
                        file_path,
                        output_path,
                        client,
                        args,
                        use_mistral,
                        use_claude,
                        use_gemini,
                        add_translation_note,
                        force,
                    )
                    if status == "success":
                        print(f"Fichier '{file}' traité.")
                    elif status == "skipped":
                        skipped_files.append(file_path)
                    elif status == "failure":
                        failed_files.append(file_path)
                    else:
                        # Default-fail sur statut inattendu (régression future)
                        print(
                            f"WARNING: Statut inattendu pour '{file}': {status!r} -> traité comme échec",
                            file=sys.stderr,
                        )
                        failed_files.append(file_path)
                elif not force:
                    print(
                        f"La traduction de '{file}' existe déjà, aucune action effectuée."
                    )
                    skipped_files.append(file_path)

    return {"failed": failed_files, "skipped": skipped_files}


def main():
    """
    Point d'entrée principal du script de traduction de fichiers Markdown.

    Ce script traduit des fichiers Markdown d'une langue source à une langue cible en utilisant
    les services de traduction de l'API OpenAI, Mistral AI, Claude ou Gemini. Il prend en charge la segmentation
    des textes longs et peut également ajouter une note de traduction en fin de document.

    Arguments du script:
    --source_dir: Répertoire contenant les fichiers Markdown à traduire.
    --target_dir: Répertoire de destination pour les fichiers traduits.
    --model: Modèle de traduction à utiliser.
    --target_lang: Langue cible pour la traduction.
    --source_lang: Langue source des documents.
    --use_mistral: Indicateur pour utiliser l'API Mistral AI pour la traduction.
    --use_claude: Indicateur pour utiliser l'API Claude pour la traduction.
    --use_gemini: Indicateur pour utiliser l'API Gemini pour la traduction.
    --add_translation_note: Indicateur pour ajouter une note de traduction au contenu traduit.
    """

    parser = argparse.ArgumentParser(description="Traduit les fichiers Markdown.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Forcer la traduction même si une traduction existe déjà",
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Fichier Markdown unique à traduire (alternative à --source_dir)",
    )
    parser.add_argument(
        "--source_dir",
        type=str,
        default=DEFAULT_SOURCE_DIR,
        help="Répertoire source contenant les fichiers Markdown",
    )
    parser.add_argument(
        "--target_dir",
        type=str,
        default=DEFAULT_TARGET_DIR,
        help="Répertoire cible pour sauvegarder les traductions",
    )
    parser.add_argument(
        "--model",
        type=str,
        help="Modèle GPT à utiliser pour la traduction, la valeur par défaut dépend de l'API sélectionnée",
    )
    parser.add_argument(
        "--target_lang",
        type=str,
        default=DEFAULT_TARGET_LANG,
        help="Langue cible pour la traduction",
    )
    parser.add_argument(
        "--source_lang",
        type=str,
        default=DEFAULT_SOURCE_LANG,
        help="Langue source pour la traduction",
    )
    parser.add_argument(
        "--use_mistral",
        action="store_true",
        help="Utiliser l'API Mistral AI pour la traduction",
    )
    parser.add_argument(
        "--use_claude",
        action="store_true",
        help="Utiliser l'API Claude d'Anthropic pour la traduction",
    )
    parser.add_argument(
        "--use_gemini",
        action="store_true",
        help="Utiliser l'API Gemini de Google pour la traduction",
    )
    parser.add_argument(
        "--add_translation_note",
        action="store_true",
        help="Ajouter une note de traduction au contenu traduit",
    )
    parser.add_argument(
        "--eco",
        action="store_true",
        help="Utiliser les modèles économiques (mini/flash) au lieu des modèles qualité",
    )
    parser.add_argument(
        "--include_model",
        action="store_true",
        help="Inclure le nom du modèle dans le fichier de sortie (ex: README-en-gpt-5.md)",
    )
    parser.add_argument(
        "--keep_filename",
        action="store_true",
        help="Conserver le nom et l'extension du fichier original (pour Astro, Hugo, etc.)",
    )
    parser.add_argument(
        "--news",
        action="store_true",
        help="Active les règles de traduction des citations news (drapeaux + quotes EN protégées)",
    )
    parser.add_argument(
        "--reasoning_effort",
        choices=("low", "medium", "high"),
        default="medium",
        help="Effort de raisonnement OpenAI GPT-5.x (défaut: medium)",
    )

    args = parser.parse_args()

    # Validation des sources
    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError(f"Le fichier spécifié n'existe pas : {args.file}")
    elif not os.path.isdir(args.source_dir):
        raise ValueError(
            f"Le répertoire source spécifié n'existe pas : {args.source_dir}"
        )
    if not os.path.exists(args.target_dir):
        os.makedirs(args.target_dir)

    if args.use_mistral:
        default_model = ECO_MODEL_MISTRAL if args.eco else DEFAULT_MODEL_MISTRAL
        args.model = args.model if args.model else default_model
        api_key = os.getenv("MISTRAL_API_KEY", DEFAULT_MISTRAL_API_KEY)
        if not api_key:
            raise ValueError("Clé API Mistral non spécifiée.")
        client = Mistral(api_key=api_key)
    elif args.use_claude:
        default_model = ECO_MODEL_CLAUDE if args.eco else DEFAULT_MODEL_CLAUDE
        args.model = args.model if args.model else default_model
        api_key = os.getenv("ANTHROPIC_API_KEY", DEFAULT_ANTHROPIC_API_KEY)
        if not api_key:
            raise ValueError("Clé API Claude non spécifiée.")
        client = anthropic.Anthropic(api_key=api_key)
    elif args.use_gemini:
        default_model = ECO_MODEL_GEMINI if args.eco else DEFAULT_MODEL_GEMINI
        args.model = args.model if args.model else default_model
        # Accepte les deux conventions de nommage couramment rencontrées :
        # - GOOGLE_API_KEY (convention historique du SDK google.generativeai)
        # - GEMINI_API_KEY (convention récente d'AI Studio + cohérence avec
        #   les SDKs JS/TS comme @google/genai utilisé pour la génération
        #   d'images dans les blogs Astro/Next).
        api_key = (
            os.getenv("GOOGLE_API_KEY")
            or os.getenv("GEMINI_API_KEY")
            or DEFAULT_GEMINI_API_KEY
        )
        if not api_key or api_key == DEFAULT_GEMINI_API_KEY:
            raise ValueError(
                "Clé API Gemini non spécifiée. Définir GOOGLE_API_KEY ou "
                "GEMINI_API_KEY dans l'environnement ou .env."
            )
        genai.configure(api_key=api_key)
        client = genai
    else:
        default_model = ECO_MODEL_OPENAI if args.eco else DEFAULT_MODEL_OPENAI
        args.model = args.model if args.model else default_model
        openai_api_key = os.getenv("OPENAI_API_KEY", DEFAULT_OPENAI_API_KEY)
        if not openai_api_key:
            raise ValueError("Clé API OpenAI non spécifiée.")
        client = OpenAI(api_key=openai_api_key)

    # Avertissement pour les modèles non listés
    if args.model not in MODEL_TOKEN_LIMITS:
        print(f"⚠ Modèle '{args.model}' non listé, utilisation de la limite par défaut ({DEFAULT_TOKEN_LIMIT} tokens)")

    if args.file:
        # Traduction d'un fichier unique
        if args.keep_filename:
            output_file = os.path.basename(args.file)
        else:
            base = os.path.splitext(os.path.basename(args.file))[0]
            if args.include_model:
                output_file = f"{base}-{args.target_lang}-{args.model}.md"
            else:
                output_file = f"{base}-{args.target_lang}.md"
        output_path = os.path.join(args.target_dir, output_file)
        status = translate_markdown_file(
            args.file,
            output_path,
            client,
            args,
            args.use_mistral,
            args.use_claude,
            args.use_gemini,
            args.add_translation_note,
            args.force,
        )
        # default-fail: tout statut hors {"success", "skipped"} compte comme échec
        failed_files = [] if status in ("success", "skipped") else [args.file]
    else:
        # Traduction d'un répertoire
        result = translate_directory(
            args.source_dir,
            args.target_dir,
            client,
            args,
            args.use_mistral,
            args.use_claude,
            args.use_gemini,
            args.add_translation_note,
            args.force,
        )
        # default-fail jusqu'au bout: si dict mal formé (régression future), traiter comme échec
        failed_files = result.get("failed", ["<unexpected translate_directory result>"])

    if args.use_mistral or args.use_claude:
        try:
            del client
        except TypeError:
            pass

    if failed_files:
        print(
            f"ERROR: {len(failed_files)} file(s) failed: {failed_files}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
