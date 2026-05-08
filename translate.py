#!/usr/bin/env python3

import argparse
import datetime
import glob
import os
import re
import sys
import time
import traceback
import unicodedata
from dataclasses import dataclass

import anthropic
import google.generativeai as genai
from dotenv import load_dotenv
from langdetect import DetectorFactory, LangDetectException, detect_langs
from mistralai import Mistral
from openai import BadRequestError, OpenAI

# Détection de langue déterministe (évite les variations entre runs sur des textes courts)
DetectorFactory.seed = 0

load_dotenv()

EXCLUDE_PATTERNS = ["traductions_", "venv", "PRIVACY.md"]

# Mapping langue → emoji drapeau pour les citations news (--news)
LANG_FLAGS = {
    "en": "🇬🇧",
    "es": "🇪🇸",
    "de": "🇩🇪",
    "it": "🇮🇹",
    "pt": "🇵🇹",
    "nl": "🇳🇱",
    "pl": "🇵🇱",
    "sv": "🇸🇪",
    "ro": "🇷🇴",
    "ja": "🇯🇵",
    "ko": "🇰🇷",
    "zh": "🇨🇳",
    "ar": "🇸🇦",
    "hi": "🇮🇳",
    "fr": "🇫🇷",
}

DEFAULT_OPENAI_API_KEY = "votre-cle-api-openai-par-defaut"
DEFAULT_MISTRAL_API_KEY = "votre-cle-api-mistral-par-defaut"
DEFAULT_ANTHROPIC_API_KEY = "votre-cle-api-anthropic-par-defaut"
DEFAULT_GEMINI_API_KEY = "votre-cle-api-gemini-par-defaut"

DEFAULT_MODEL_OPENAI = "gpt-5.5"
DEFAULT_MODEL_MISTRAL = "mistral-large-latest"
DEFAULT_MODEL_CLAUDE = "claude-sonnet-4-6"
DEFAULT_MODEL_GEMINI = "gemini-3.1-pro-preview"

ECO_MODEL_OPENAI = "gpt-5.4-mini"
ECO_MODEL_MISTRAL = "mistral-small-latest"
ECO_MODEL_CLAUDE = "claude-haiku-4-5-20251001"
ECO_MODEL_GEMINI = "gemini-3.1-flash-lite-preview"

# Fallback pour les modèles non listés dans MODEL_TOKEN_LIMITS.
DEFAULT_TOKEN_LIMIT = 128000

DEFAULT_SOURCE_LANG = "fr"
DEFAULT_TARGET_LANG = "en"
DEFAULT_SOURCE_DIR = "content/posts"
DEFAULT_TARGET_DIR = "traductions_en"
MODEL_TOKEN_LIMITS = {
    # OpenAI GPT-5.5 series (1M+ context)
    "gpt-5.5": 1050000,
    "gpt-5.5-pro": 1050000,
    # OpenAI GPT-5.4 series
    "gpt-5.4": 400000,
    "gpt-5.4-mini": 400000,
    "gpt-5.4-nano": 400000,
    "gpt-5.4-pro": 400000,
    # OpenAI GPT-5 series
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
    # Anthropic Claude 4.6+ : 1M context au prix standard (Opus 4.7, Opus 4.6,
    # Sonnet 4.6 explicitement listés dans la doc Anthropic).
    # Haiku 4.5 reste sur 200K (pas dans la liste 1M).
    "claude-opus-4-7": 1000000,
    "claude-opus-4-6": 1000000,
    "claude-sonnet-4-6": 1000000,
    # Anthropic Claude 4.5
    "claude-opus-4-5-20251101": 200000,
    "claude-sonnet-4-5-20250929": 200000,
    "claude-haiku-4-5-20251001": 200000,
    # Anthropic Claude 4.x
    "claude-opus-4-1-20250805": 200000,
    "claude-sonnet-4-20250514": 200000,
    # Anthropic Claude 3.x (legacy)
    "claude-3-5-sonnet-20240620": 200000,
    "claude-3-7-sonnet-20250219": 200000,
    # Mistral
    "mistral-large-latest": 128000,
    "mistral-small-latest": 128000,
    "magistral-medium-latest": 40000,
    "magistral-small-latest": 40000,
    # Google Gemini
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
# continuations de liste/dict YAML (crochets, accolades,
# strings 'item' ou 'item', sur leur propre ligne après reformatage prettier).
# Inclut aussi les barres de langues markdown (README/CHANGELOG/blog multilingue) :
# une ligne qui ne contient QUE des liens [label](file.md) séparés par `|`, avec
# un préfixe optionnel court (emoji 🌍, etc.). Les paths sont conservés à
# l'identique entre les langues par design, donc la ligne reste verbatim source
# dans la sortie traduite — ce qui ferait échouer le validateur sans cette
# exception. Le `$` final empêche le faux positif sur "Voir [a](x.md) | [b](y.md) ici."
_STRUCTURAL_LINE = re.compile(
    r"^\s*(?:"
    r"```"  # code fence
    r"|---"  # hr / frontmatter delimiter
    r"|\|"  # table separator
    r"|#[A-Z]+\d+#"  # placeholder (#CODEBLOCK1#, etc.)
    r"|<NEWSQUOTE\s+id=['\"]\d+['\"]\s*/>"  # placeholder news XML
    r"|[A-Za-z_][\w-]*:(?:\s|$)"  # YAML key: (title:, tags:, …)
    r"|[\[\]{}]"  # YAML list/dict bracket on own line
    r"|['\"][^'\"\n]+['\"]\s*,?\s*$"  # YAML string item ('item' or "item", possibly with trailing comma)
    r"|(?:\S+\s+)?\[[^\]]+\]\([^)]+\.md\)(?:\s*\|\s*\[[^\]]+\]\([^)]+\.md\))+\s*$"  # markdown language/nav bar
    r"|</?[a-zA-Z][^>]*>(?:\s*</?[a-zA-Z][^>]*>)*\s*$"  # ligne composée uniquement de balises HTML (<p align="center">, </p>, <br/>, etc.) — `[^>]*>` borne strictement, pas d'ambigüité avec un `/?` final qui ferait backtracker (CodeQL py/redos-trailing-quantifier)
    r"|(?:\S+\s+)?<a\s+href=['\"][^'\"]+['\"][^>]*>[^<]*</a>(?:\s*[·•|·‧]\s*<a\s+href=['\"][^'\"]+['\"][^>]*>[^<]*</a>)+(?:\s*<br\s*/?>)?\s*$"  # html language/nav bar (≥2 <a href> séparés par · • ‧ |)
    r")"
)
# Préfixes Markdown inline → à STRIPPER (on garde le texte derrière)
_INLINE_MD_PREFIX = re.compile(r"^\s*(?:[-*+]\s+|#{1,6}\s+|\d+\.\s+)")
_EMPTY_BLOCKQUOTE_LINE = re.compile(r"^\s*>\s*$")
_BLOCKQUOTE_PREFIX = re.compile(r"^\s*>\s?")
# Split en 2 regex pour rester sous le seuil Sonar S5843 (complexity ≤20).
# `_URL_OR_PLACEHOLDER` couvre URLs absolues + placeholders ; les news quotes
# XML self-closing ont leur propre regex, appliquée séparément quand utile.
_URL_OR_PLACEHOLDER = re.compile(r"https?://\S+|#(?:CODEBLOCK|INLINECODE|URL|ANCHOR|REFLABEL)\d+#")
_NEWSQUOTE_PLACEHOLDER_REGEX = re.compile(r"<NEWSQUOTE\s+id=['\"]\d+['\"]\s*/>")
_MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
# Constante factorée pour Sonar S1192 (literal "<[^>]+>" dupliqué 3 fois).
_HTML_TAG_REGEX = re.compile(r"<[^>]+>")
_LANG_SCRIPT_RANGES = {
    "ar": (("\u0600", "\u06ff"),),
    "hi": (("\u0900", "\u097f"),),
    "ja": (("\u3040", "\u30ff"), ("\u4e00", "\u9fff")),
    "ko": (("\uac00", "\ud7af"),),
    "zh": (("\u4e00", "\u9fff"),),
}

# Pour les targets non-latins, l'instruction explicite sur le script attendu
# est n\u00e9cessaire : sans \u00e7a, certains LLMs (gpt-5.4-mini eco notamment) font
# du Hinglish/Spanglish technique et ne transcrivent qu'une partie en script
# cible (cf. caveman EN\u2192HI qui sortait \u00e0 ~31% Devanagari sans cette instruction).
_LANG_SCRIPT_NAMES = {
    "ar": "Arabic (\u0627\u0644\u0639\u0631\u0628\u064a\u0629)",
    "hi": "Hindi (\u0939\u093f\u0928\u094d\u0926\u0940, Devanagari)",
    "ja": "Japanese (\u65e5\u672c\u8a9e, Hiragana/Katakana/Kanji)",
    "ko": "Korean (\ud55c\uad6d\uc5b4, Hangul)",
    "zh": "Chinese (\u4e2d\u6587, Hanzi)",
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


def _reason_name(reason):
    """Normalise un finish_reason/stop_reason : extrait .name si enum, sinon retourne tel quel."""
    return getattr(reason, "name", reason)


def _looks_like_proper_noun_list(window):
    """Heuristique : la fenêtre est dominée par des mots commençant par
    majuscule (>70% des mots ≥3 chars), suggérant une liste de noms propres /
    marques / produits qui restent identiques source/cible légitimement
    (ex. `opencode, Roo, Amp, Goose, Kiro CLI, …`). Un match verbatim de ces
    fenêtres dans la sortie n'indique PAS un passthrough — le LLM ne traduit
    pas un nom de produit. On les exclut donc de la garde anti-passthrough.

    Seuil min 5 mots pour ne pas skip à tort des fenêtres trop courtes ;
    seuil 70% pour préserver la détection sur des phrases title-case
    (`The API uses HTTP for Communication`) qui restent légitimes à matcher.
    """
    words = re.findall(r"[A-Za-z][A-Za-z'-]{2,}", window)
    if len(words) < 5:
        return False
    upper_starts = sum(1 for w in words if w[0].isupper())
    return upper_starts / len(words) > 0.7


def _clean_for_language_detection(text):
    """Réduit le bruit structurel avant langdetect/script checks.

    Les README techniques contiennent beaucoup de HTML, URLs, placeholders,
    liens Markdown, anchors et code. Les laisser dans le corpus pousse
    langdetect vers `en`, surtout pour HI où le texte traduit garde souvent des
    noms de produits/flags CLI en latin.
    """
    text = _MARKDOWN_LINK.sub(r"\1", text)
    text = _URL_OR_PLACEHOLDER.sub(" ", text)
    text = _NEWSQUOTE_PLACEHOLDER_REGEX.sub(" ", text)
    text = _HTML_TAG_REGEX.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def _count_chars_in_ranges(text, ranges):
    count = 0
    for ch in text:
        if any(start <= ch <= end for start, end in ranges):
            count += 1
    return count


def _has_target_script_signal(text, target_lang):
    ranges = _LANG_SCRIPT_RANGES.get(target_lang)
    if not ranges:
        return False
    cleaned = _clean_for_language_detection(text)
    target_chars = _count_chars_in_ranges(cleaned, ranges)
    latin_chars = len(re.findall(r"[A-Za-z]", cleaned))
    total_alpha = target_chars + latin_chars
    if total_alpha == 0:
        return False
    ratio = target_chars / total_alpha
    # README techniques traduits vers HI/AR/JA/KO/ZH ont 2 patterns valides :
    # - prose dense (≥400 chars cible et ratio ≥20%) : sections de docs.
    # - section "liste de ressources" (≥150 chars cible et ratio ≥30%) : titres
    #   traduits + liens latin où le LLM ne peut pas traduire les noms de
    #   packages (Pacman, Homebrew, Helm…) ; le ratio reste fort sur la prose
    #   réelle (cleaned), mais le volume absolu est mécaniquement bas.
    return (target_chars >= 400 and ratio >= 0.20) or (target_chars >= 150 and ratio >= 0.30)


def _line_is_droppable(line, ignore_blockquotes):
    """Vrai si la ligne est purement structurelle (pas de prose à comparer)."""
    if _EMPTY_BLOCKQUOTE_LINE.match(line):
        return True
    if ignore_blockquotes and _BLOCKQUOTE_PREFIX.match(line):
        return True
    return bool(_STRUCTURAL_LINE.match(line))


def _clean_paragraph_for_window(para, ignore_blockquotes):
    """Retourne la prose normalisée d'un paragraphe (chaîne vide si rien d'utile).

    Strip blockquotes empty/structurelles, préfixes Markdown inline, URLs,
    balises HTML inline (<strong>, <a>, etc.) qui restent identiques source/cible
    et créeraient des faux positifs de passthrough.
    """
    kept_lines = []
    for line in para.split("\n"):
        if _line_is_droppable(line, ignore_blockquotes):
            continue
        unquoted = _BLOCKQUOTE_PREFIX.sub("", line)
        kept_lines.append(_INLINE_MD_PREFIX.sub("", unquoted))
    if not kept_lines:
        return ""
    joined = " ".join(kept_lines)
    cleaned = _URL_OR_PLACEHOLDER.sub("", joined)
    cleaned = _HTML_TAG_REGEX.sub(" ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def _windows_from_clean_text(cleaned):
    """Retourne 0/1/3 fenêtres selon la longueur (paragraphe long = début/milieu/fin)."""
    n = len(cleaned)
    if n < 120:
        return []
    if n >= 600:
        mid = n // 2
        return [cleaned[:200], cleaned[mid - 100 : mid + 100], cleaned[-200:]]
    return [cleaned[:200]]


def _extract_source_windows(segment, ignore_blockquotes=False):
    """Retourne des fenêtres textuelles 'saines' (≥120 chars) issues du segment source,
    en regroupant les paragraphes wrappés. Pour les paragraphes longs (≥600 chars), extrait
    3 fenêtres (début/milieu/fin) pour couvrir le cas où le source non-traduit serait au milieu."""
    windows = []
    for para in re.split(r"\n\s*\n", segment):
        cleaned = _clean_paragraph_for_window(para, ignore_blockquotes)
        windows.extend(_windows_from_clean_text(cleaned))
    return windows


def _check_output_short_ratio(segment, stripped, args):
    """Sanity ratio : sortie disproportionnellement courte vs source (refus type
    "OK" / "Sorry, I can't do that" / troncature). Activé pour source >= 500
    chars, seuil 5% avec floor 50 chars (cross-script FR→ZH ~30%, FR→AR ~60-80%)."""
    source_len = len(segment.strip())
    if source_len >= 500 and len(stripped) < max(50, source_len // 20):
        raise RuntimeError(
            f"Output suspiciously short for source: source={source_len} chars, "
            f"output={len(stripped)} chars, ratio={len(stripped) / source_len:.1%} "
            f"(model={args.model}, target={args.target_lang}, "
            f"first 200 chars: {stripped[:200]!r})"
        )


def _check_passthrough_excerpt(segment, stripped, args):
    """Couche 1 : vérifie qu'aucune fenêtre source ≥120 chars (cleaned) n'apparaît
    verbatim dans la sortie (bug silent-failure typique : LLM renvoie le source brut)."""
    out_norm = re.sub(r"\s+", " ", stripped).casefold()
    for window in _extract_source_windows(segment, ignore_blockquotes=args.news):
        if _looks_like_proper_noun_list(window):
            continue
        window_norm = re.sub(r"\s+", " ", window).casefold()
        if window_norm in out_norm:
            raise RuntimeError(
                f"Output contains untranslated source excerpt "
                f"(model={args.model}, target={args.target_lang}, "
                f"matched window: {window_norm[:100]!r})"
            )


def _check_output_language(stripped, args):
    """Couche 2 : langdetect probabiliste sur la langue de sortie. Court-circuite
    si target script (HI/AR/ZH/JA/KO) déjà détecté en quantité suffisante (le
    code-switching technique fait que langdetect peut sous-estimer la cible).
    """
    if _has_target_script_signal(stripped, args.target_lang):
        return
    langdetect_text = _clean_for_language_detection(stripped)
    if len(langdetect_text) < 100:
        return
    try:
        probas = {p.lang: p.prob for p in detect_langs(langdetect_text)}
    except LangDetectException as e:
        print(
            f"⚠ langdetect failed on output (model={args.model}, "
            f"target={args.target_lang}, len={len(langdetect_text)}): {e}",
            file=sys.stderr,
        )
        return
    src_p = probas.get(args.source_lang, 0.0)
    tgt_p = probas.get(args.target_lang, 0.0)
    if src_p > 0.80 and tgt_p < 0.20:
        raise RuntimeError(
            f"Output language mismatch: expected {args.target_lang} (p={tgt_p:.2f}), "
            f"got {args.source_lang} (p={src_p:.2f}), model={args.model}, "
            f"first 200 chars: {stripped[:200]!r}"
        )


def _validate_translation_output(segment, translated_text, args, is_translation_note):
    """Vérifie que la sortie LLM n'est pas un silent-failure. Dispatch :
    ratio guard → passthrough check → langdetect/script check."""
    if is_translation_note or args.source_lang == args.target_lang:
        return
    stripped = translated_text.strip()
    if not stripped:
        return
    _check_output_short_ratio(segment, stripped, args)
    _check_passthrough_excerpt(segment, stripped, args)
    _check_output_language(stripped, args)


_O1_SERIES = ("o1", "o1-mini", "o1-preview")


def _build_translation_note_prompt(args):
    return (
        f"Translate directly to {args.target_lang} without any additions. "
        "Do NOT modify URLs or image paths. "
        "Output only the translation, nothing else."
    )


def _build_base_markdown_prompt(args):
    return (
        f"Translate this Markdown document from {args.source_lang} to {args.target_lang}. "
        "Output ONLY the translated Markdown, with no comments or explanations. "
        "Preserve the complete Markdown structure: headings, lists, tables, blockquotes, "
        "front matter, MDX/HTML tags, directives, comments, and blank-line separation. "
        "Translate human-readable text inside blockquotes while preserving the `>` markers. "
        "For non-Latin target languages, write prose in the natural native script; keep Latin "
        "script only for code, URLs, anchors, product/model names, CLI flags, and unavoidable "
        "technical identifiers. "
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


def _build_news_rules_en(placeholder_example):
    return (
        '\n\n<news_citation_contract version="4">'
        "\n<placeholder_rule>"
        f"\nNews quote placeholders are XML self-closing tags like `{placeholder_example}`."
        "\nThey are protected technical tags, not translatable text."
        '\nCopy every `<NEWSQUOTE id="N"/>` tag exactly, preserving the Latin tag name, id number, quotes, and slash.'
        "\nDo not replace the XML tag with quote text. Do not translate, localize, rename, delete, or reorder it."
        "\nAcceptable formatting is only the exact input tag; do not add explanations around it."
        "\n</placeholder_rule>"
        '\n<citation_rule target="en">'
        "\nFor each citation block, REMOVE the empty blockquote line (`>`) and REMOVE the whole source-translation line `> 🇫🇷 _..._`."
        '\nKeep only the `<NEWSQUOTE id="N"/>` tag and the attribution line `> — [...](url)`.'
        "\nTranslate attribution link text only; keep URL unchanged."
        "\n</citation_rule>"
        "\n<correct_output_shape>"
        '\n<NEWSQUOTE id="N"/>'
        "\n> — [translated attribution text](url unchanged)"
        "\n</correct_output_shape>"
        "\n</news_citation_contract>"
    )


def _build_news_placeholder_rule(placeholder_example):
    return (
        "\n<placeholder_rule>"
        f"\nNews quote placeholders are XML self-closing tags like `{placeholder_example}`."
        "\nThey are protected technical tags, not words and not content."
        '\nEach `<NEWSQUOTE id="N"/>` tag MUST appear in output with the same id number, in the same citation position.'
        "\nDo not translate the tag name. Do not localize NEWSQUOTE into Polish, Chinese, Korean, Arabic, Hindi, or any other language."
        "\nDo not replace the XML tag with the quote text. Do not delete it. Do not wrap it in code fences."
        "\nBefore finalizing output: count `<NEWSQUOTE` tags in the output. The count MUST equal the source input."
        "\n</placeholder_rule>"
    )


def _build_news_flag_rule(args, target_flag):
    return (
        "\n<flag_rule>"
        f"For each citation block: replace the source flag 🇫🇷 with {target_flag} and translate the italic text COMPLETELY to {args.target_lang}."
        "\nCOMPLETE = same number of sentences, all concepts included, no truncation or summarization. The placeholder represents the original English quote — translate FROM its meaning."
        f"\nThe {target_flag} emoji MUST ONLY appear inside blockquote citation lines (starting with `> `), and ONLY ONCE per citation."
        "\n</flag_rule>"
    )


_NEWS_RULES_EXAMPLES = (
    "\n<examples>"
    "\nExample 1 — Polish target (PL):"
    "\nINPUT:"
    '\n<NEWSQUOTE id="0"/>'
    "\n>"
    "\n> 🇫🇷 _Une décennie de travail._"
    "\n> — [@GoogleAI sur X](https://x.com/google)"
    "\nCORRECT OUTPUT:"
    '\n<NEWSQUOTE id="0"/>'
    "\n>"
    "\n> 🇵🇱 _Dekada pracy._"
    "\n> — [@GoogleAI na X](https://x.com/google)"
    "\n"
    "\nExample 2 — Chinese target (ZH), tag MUST stay in Latin script:"
    "\nINPUT:"
    '\n<NEWSQUOTE id="0"/>'
    "\n>"
    "\n> 🇫🇷 _Une décennie de travail._"
    "\n> — [@GoogleAI sur X](https://x.com/google)"
    "\nCORRECT OUTPUT:"
    '\n<NEWSQUOTE id="0"/>'
    "\n>"
    "\n> 🇨🇳 _十年磨一剑。_"
    "\n> — [@GoogleAI 在 X 上](https://x.com/google)"
    '\nWRONG: `<新闻引用 id="0"/>`, `<QUOTE id="0"/>`, or replacing the tag with the quote.'
    "\n"
    "\nExample 3 — Korean target (KO):"
    "\nINPUT:"
    '\n<NEWSQUOTE id="0"/>'
    "\n>"
    "\n> 🇫🇷 _Une décennie de travail._"
    "\n> — [@GoogleAI sur X](https://x.com/google)"
    "\nCORRECT OUTPUT:"
    '\n<NEWSQUOTE id="0"/>'
    "\n>"
    "\n> 🇰🇷 _10년간의 작업._"
    "\n> — [@GoogleAI X에서](https://x.com/google)"
    '\nWRONG: `<뉴스인용 id="0"/>` or any Korean tag name.'
    "\n"
    "\nExample 4 — Arabic/Hindi scripts:"
    "\nCORRECT OUTPUT tag line:"
    '\n<NEWSQUOTE id="0"/>'
    "\nWRONG: translating NEWSQUOTE, changing quotes, changing id, or removing the slash."
    "\n</examples>"
)


def _build_news_result_format(args, target_flag):
    return (
        f'\nResult format for {args.target_lang} target:\n<NEWSQUOTE id="N"/>\n>\n'
        f"> {target_flag} _translated italic text in {args.target_lang}_\n"
        "> — [attribution text translated](url unchanged)"
    )


def _build_news_rules_other(args, target_flag, placeholder_example):
    return (
        '\n\n<news_citation_contract version="4">'
        "\nThese rules are CRITICAL and override ordinary translation instincts."
        "\n"
        + _build_news_placeholder_rule(placeholder_example)
        + "\n"
        + _build_news_flag_rule(args, target_flag)
        + "\n"
        + _NEWS_RULES_EXAMPLES
        + "\n"
        + _build_news_result_format(args, target_flag)
        + "\n</news_citation_contract>"
    )


_MARKDOWN_TRANSLATION_CONTRACT = (
    "\n\n<markdown_translation_contract>"
    "\n<completion_rules>"
    "\n- The output MUST include EVERY part of the source document."
    "\n- Preserve ALL headings (any level: `#`, `##`, `###`, `####`, etc.) at the SAME level and in the SAME order as the source."
    "\n- Preserve ALL paragraphs, lists, code blocks, tables, and blockquotes from the source."
    "\n- Translate the document FROM start TO end. The output must reach the same final element as the source (last paragraph, last list item, last section)."
    "\n- DO NOT truncate, summarize, merge, or skip any element."
    "\n- Translate ALL prose into the target language. Do NOT leave any sentence, paragraph, list item, table cell, blockquote, image alt text, or HTML attribute value (alt=, title=, aria-label=) in the source language. Each prose string must be fully rendered in the target language."
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
    "\nBefore returning, verify silently: all headings are present; all URLs are unchanged; the final section is complete; nothing has been truncated or summarized; EVERY prose paragraph has been translated to the target language (no source-language sentences remain)."
    "\nReturn ONLY the translated Markdown. No checklist, no commentary."
    "\n</final_checklist>"
    "\n</markdown_translation_contract>"
)

_NEWS_FINAL_CHECKS = (
    "\n\n<news_final_checks>"
    "\nAdditional checks for news mode: every `<NEWSQUOTE` tag must be present in its original Latin form with the same id; the target flag emoji count must equal the citation count; no source flag (🇫🇷) remains anywhere."
    "\n</news_final_checks>"
)

_PLACEHOLDER_PRESERVATION_CONTRACT = (
    "\n\n<placeholder_preservation_contract>"
    "\nThe input may contain placeholders like `#INLINECODE0#`, `#INLINECODE1#`, `#CODEBLOCK0#`, `#URL0#`, `#ANCHOR0#`, `#REFLABEL0#`, etc. These represent code blocks, inline code, URLs, explicit HTML anchors, and Markdown reference-style link labels extracted before translation."
    "\nEVERY such placeholder present in the input MUST appear in the output exactly as-is: same prefix (`#INLINECODE`, `#CODEBLOCK`, `#URL`, `#ANCHOR`, `#REFLABEL`), same digit, same trailing `#`. Do not rename, translate, transliterate, drop, or merge them. Do not add new ones."
    "\nWhen the target language reorders sentence components (e.g. English SVO → Chinese/Japanese/Korean SOV, or relative clause repositioning in Hindi/Arabic), move the placeholder to its grammatically correct position — but keep it intact."
    "\nFor reference-style links of the form `[visible text][#REFLABEL0#]` or `![alt text][#REFLABEL0#]`, translate the visible text/alt freely but keep the `[#REFLABEL0#]` part exactly as-is — it is the technical key Markdown uses to find the matching definition."
    "\nBefore returning, count `#INLINECODE`, `#CODEBLOCK`, `#URL`, `#ANCHOR`, and `#REFLABEL` occurrences in your output. The count MUST equal the count in the input. If a placeholder fell into a table cell or list item that you rephrased, double-check it survived the rewrite."
    "\n</placeholder_preservation_contract>"
)

_HEADING_ANCHOR_CONSISTENCY_CONTRACT = (
    "\n\n<heading_anchor_consistency_contract>"
    "\nFor Markdown anchor links `[text](#fragment)` where `fragment` is a slug derived from a heading in the same document (lowercase, spaces replaced by `-`), translate `fragment` TOGETHER with the heading it points to. GitHub regenerates the anchor slug from the translated heading, so an unchanged fragment breaks the link if the heading is translated."
    "\nExample EN→FR:"
    "\n  WRONG (link breaks): output keeps `See [the cache section](#caching-strategy)` while the heading becomes `## Stratégie de mise en cache`."
    "\n  RIGHT (link works): output is `Voir [la section sur la mise en cache](#stratégie-de-mise-en-cache)` paired with `## Stratégie de mise en cache`."
    '\nIf a `(#fragment)` is already replaced by an `#ANCHOR0#` (or similar) placeholder, leave that placeholder alone — it represents an explicit `<a name="..."></a>` declaration whose identifier is technical and must NOT be translated. Only `(#X)` fragments still visible in the input fall under this consistency rule.'
    "\n</heading_anchor_consistency_contract>"
)


def _build_news_addendum(args):
    target_flag = LANG_FLAGS.get(args.target_lang, "")
    placeholder_example = news_quote_placeholder(0)
    if args.target_lang == "en":
        rules = _build_news_rules_en(placeholder_example)
    else:
        rules = _build_news_rules_other(args, target_flag, placeholder_example)
    return rules + _NEWS_FINAL_CHECKS


def _build_non_latin_script_addendum(target_lang):
    """Instruction explicite quand le script cible est non-latin (HI, AR, ZH, JA, KO).
    Sans ça, les LLMs (en particulier les modèles eco) écrivent souvent une
    fraction de la prose en latin transliteration / English, ce qui produit
    une traduction "Hinglish technique" sous-utilisable."""
    script_name = _LANG_SCRIPT_NAMES.get(target_lang)
    if not script_name:
        return ""
    return (
        "\n\n<target_script_contract>"
        f"\nALL human-readable prose MUST be written in {script_name}."
        "\nKeep latin script ONLY for: code blocks, inline code, URLs, file paths, "
        "anchors, brand and product names (e.g. React, useMemo, Mistral), CLI flags "
        "(e.g. --eco, --news), model identifiers, and YAML/TOML structural keys."
        "\nDo NOT write prose paragraphs, sentences, or list items in latin "
        f"transliteration or in source language. Every paragraph of natural language "
        f"must be rendered natively in {script_name}."
        "\n</target_script_contract>"
    )


def _build_system_instructions(args, is_translation_note):
    if is_translation_note:
        return _build_translation_note_prompt(args)
    # Le contrat de complétude/structure markdown s'applique à TOUTES les
    # traductions (news ou non) — sans cette instruction explicite, certains
    # LLMs (gpt-5.x compris) "résument" les longs documents techniques en
    # traduisant uniquement le header et en laissant le body en source_lang
    # (cf. caveman EN→HI : header HI + body EN, détecté par la garde layer 2).
    base = _build_base_markdown_prompt(args) + _MARKDOWN_TRANSLATION_CONTRACT
    base += _PLACEHOLDER_PRESERVATION_CONTRACT
    base += _HEADING_ANCHOR_CONSISTENCY_CONTRACT
    base += _build_non_latin_script_addendum(args.target_lang)
    if args.news:
        base += _build_news_addendum(args)
    return base


def _call_mistral(client, args, prompt, segment):
    messages = [{"role": "user", "content": prompt + "\n\n" + segment}]
    response = client.chat.complete(model=args.model, messages=messages)
    finish = _reason_name(response.choices[0].finish_reason)
    if finish not in ("stop", "STOP", None):
        raise RuntimeError(f"Mistral abnormal finish_reason={finish!r} (model={args.model})")
    return response.choices[0].message.content.strip()


def _call_claude(client, args, prompt, segment):
    messages = [{"role": "user", "content": prompt + "\n\n" + segment}]
    # 32768 : marge sur l'expansion cross-script (FR→JA/ZH/KO/AR/HI peuvent
    # dépasser 16k tokens en sortie pour des segments source de 16k chars).
    # Sonnet 4.6 et Opus 4.6+ supportent au moins 64k output tokens.
    response = client.messages.create(model=args.model, max_tokens=32768, messages=messages)
    stop = _reason_name(response.stop_reason)
    if stop not in ("end_turn", "stop_sequence", None):
        raise RuntimeError(f"Claude abnormal stop_reason={stop!r} (model={args.model})")
    # Préserve la structure markdown entre blocs : pas de .strip() sur chaque
    # bloc (qui mangerait des newlines structurants), join avec "\n\n" entre
    # blocs distincts, et un seul .strip() global sur la sortie finale.
    return "\n\n".join(block.text for block in response.content).strip()


def _call_gemini(client, args, prompt, segment):
    model = client.GenerativeModel(args.model)
    response = model.generate_content(prompt + "\n\n" + segment)
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


def _build_openai_messages(args, prompt, segment):
    if args.model in _O1_SERIES:
        return [{"role": "user", "content": prompt + "\n\n" + segment}]
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": segment},
    ]


def _openai_extra_kwargs(args, is_translation_note):
    # reasoning_effort sur GPT-5.x ; default medium pour rester pas cher.
    if args.model.startswith("gpt-5") and not is_translation_note:
        return {"reasoning_effort": getattr(args, "reasoning_effort", "medium")}
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
    if finish not in ("stop", "STOP", None):
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


def _dispatch_provider_call(
    client, args, prompt, segment, use_mistral, use_claude, use_gemini, is_translation_note
):
    if use_mistral:
        text, provider = _call_mistral(client, args, prompt, segment), "mistral"
    elif use_claude:
        text, provider = _call_claude(client, args, prompt, segment), "claude"
    elif use_gemini:
        text, provider = _call_gemini(client, args, prompt, segment), "gemini"
    else:
        text, provider = _call_openai(client, args, prompt, segment, is_translation_note), "openai"
    # Empty-content guard : un provider qui retourne "" avec finish_reason="stop"
    # produirait sinon un fichier vide marqué success.
    if not text.strip():
        raise RuntimeError(f"{provider.capitalize()} returned empty content (model={args.model})")
    return text


_SEGMENT_PLACEHOLDER_REGEX = re.compile(r"#(?:CODEBLOCK|INLINECODE|URL|ANCHOR|REFLABEL)\d+#")


def _validate_segment_placeholders(input_segment, output_text):
    """Vérifie que tous les placeholders #CODEBLOCKn# / #INLINECODEn# présents
    dans le segment d'entrée sont aussi dans la sortie LLM. Détecte au niveau
    segment ce que `_validate_code_placeholders_present` détecterait au niveau
    pipeline — utile pour permettre un retry ciblé sur le segment fautif."""
    in_phs = set(_SEGMENT_PLACEHOLDER_REGEX.findall(input_segment))
    out_phs = set(_SEGMENT_PLACEHOLDER_REGEX.findall(output_text))
    missing = in_phs - out_phs
    if missing:
        raise RuntimeError(
            f"Placeholder(s) {sorted(missing)} manquant(s) dans la sortie segment "
            "(le LLM les a supprimés ou modifiés)"
        )


@dataclass
class _LLMCallSpec:
    """Regroupe les paramètres d'un appel LLM (provider + flags) pour réduire
    la signature de `_translate_segment_with_retry` et `_dispatch_provider_call`."""

    client: object
    args: object
    system_instructions: str
    use_mistral: bool = False
    use_claude: bool = False
    use_gemini: bool = False
    is_translation_note: bool = False


def _translate_segment_with_retry(segment, idx, total, spec, max_retries=1):
    """Appelle le LLM puis valide placeholders + langue/passthrough. En cas de
    fail récupérable (non-déterminisme LLM), retry 1 fois max. Les fails non-
    récupérables (finish_reason anormal, sortie vide) ne sont pas retryés —
    ils indiquent un problème API, pas un problème de qualité de traduction."""
    last_exc = None
    for attempt in range(max_retries + 1):
        translated_text = _dispatch_provider_call(
            spec.client,
            spec.args,
            spec.system_instructions,
            segment,
            spec.use_mistral,
            spec.use_claude,
            spec.use_gemini,
            spec.is_translation_note,
        )
        try:
            _validate_segment_placeholders(segment, translated_text)
            _validate_translation_output(
                segment, translated_text, spec.args, spec.is_translation_note
            )
            if attempt > 0:
                print(
                    f"✓ Segment {idx}/{total} validated on retry {attempt}/{max_retries}",
                    file=sys.stderr,
                )
            return translated_text
        except RuntimeError as e:
            last_exc = e
            if attempt >= max_retries:
                raise
            print(
                f"⚠ Segment {idx}/{total} validation failed "
                f"(attempt {attempt + 1}/{max_retries + 1}): {e}. Retrying...",
                file=sys.stderr,
            )
    raise last_exc  # unreachable, garde de sécurité


def translate(
    text,
    client,
    args,
    use_mistral=False,
    use_claude=False,
    use_gemini=False,
    is_translation_note=False,
):
    """Segmente puis traduit le texte, et lève RuntimeError si une garde de
    silent-failure se déclenche (finish_reason anormal, sortie vide, extrait
    source verbatim, ratio source/output trop faible, langue source détectée).
    """
    model_limit = MODEL_TOKEN_LIMITS.get(args.model, DEFAULT_TOKEN_LIMIT)
    segments = segment_text(text, min(16000, model_limit))
    system_instructions = _build_system_instructions(args, is_translation_note)

    spec = _LLMCallSpec(
        client=client,
        args=args,
        system_instructions=system_instructions,
        use_mistral=use_mistral,
        use_claude=use_claude,
        use_gemini=use_gemini,
        is_translation_note=is_translation_note,
    )
    translated_segments = []
    for idx, segment in enumerate(segments, start=1):
        try:
            translated_text = _translate_segment_with_retry(segment, idx, len(segments), spec)
        except Exception as e:
            # On préserve le type d'origine dans le message ET la chaîne via `from e`
            # (le traceback complet reste accessible par traceback.print_exc en haut).
            raise RuntimeError(
                f"Erreur lors de la traduction (segment {idx}/{len(segments)}, "
                f"{type(e).__name__}): {e}"
            ) from e
        translated_segments.append(translated_text)

    # Jonction par "\n" : les segments coupés sur "\n\n" / "\n## " préservent
    # leur newline structurant, et les coupures sur ". " ou hard-cut (max_length)
    # ne sont pas garanties de finir/commencer par "\n" — un "\n" explicite ici
    # évite de coller deux paragraphes ou de fusionner un heading avec sa prose.
    return "\n".join(translated_segments)


_FENCED_CODE_REGEX = re.compile(
    # Info-string CommonMark : tout texte jusqu'au newline après les ``` (pas
    # juste un identifiant `[\w-]*`). Les README utilisent souvent des attributs
    # (e.g. ` ```Python hl_lines="7  12" ` chez FastAPI, ` ```py title="..." ` chez
    # MkDocs) — sans cette tolérance, le bloc n'est pas protégé, le code part au
    # LLM comme prose, et la garde anti-passthrough lève un faux positif.
    r"(^```[^\n]*\n)(.*?)(^```[ \t]*$)",
    re.DOTALL | re.MULTILINE,
)
_INLINE_CODE_REGEX = re.compile(r"(?<!`)(`[^`\n]+?`)(?!`)")
# News citation pattern: 1+ EN quote lines `> X` (excluding `> — attribution`)
# then `>` empty separator, then `> FLAG _trad_`, optional `> — attribution`.
# Multi-line EN quote bodies (common on long social-media quotes) MUST be captured
# as a single group to be re-emitted verbatim — see _protect_news_quotes.
_NEWS_CITATION_REGEX = re.compile(
    r"(^> (?!— ).+(?:[ \t]*\n^> (?!— ).+)*)[ \t]*\n"
    r"^>[ \t]*\n"
    r"(^> .+_)[ \t]*"
    r"(?:\n(^> — .+?)[ \t]*)?$",
    re.MULTILINE,
)
_RESIDUAL_NEWS_PLACEHOLDER_REGEX = re.compile(r'<NEWSQUOTE\s+id=["\']\d+["\']\s*/>|#NEWSQUOTE\d+#')


def _protect_code_blocks(content):
    code_blocks = [m.group(0) for m in _FENCED_CODE_REGEX.finditer(content)]
    placeholders = [f"#CODEBLOCK{i}#" for i in range(len(code_blocks))]
    # Replace one occurrence at a time : deux blocs byte-identical doivent recevoir
    # des placeholders distincts (sinon #CODEBLOCK1# n'apparaît jamais et le validateur
    # déclenche après l'appel API alors qu'on aurait pu détecter avant).
    for placeholder, code_block in zip(placeholders, code_blocks, strict=False):
        content = content.replace(code_block, placeholder, 1)
    return content, code_blocks, placeholders


def _protect_inline_code(content):
    inline_codes = [m.group(0) for m in _INLINE_CODE_REGEX.finditer(content)]
    placeholders = [f"#INLINECODE{i}#" for i in range(len(inline_codes))]
    # Replace one at a time to handle duplicate snippets correctly.
    for placeholder, inline in zip(placeholders, inline_codes, strict=False):
        content = content.replace(inline, placeholder, 1)
    return content, inline_codes, placeholders


# URLs (http/https) sont byte-identical entre source et cible : les filer au LLM
# en clair l'incite parfois à traduire le texte qu'elles contiennent (badges
# shields.io avec `?text=Voir_la_démo`, ancres `#section-name`) ou à les drop
# en rephrasant une phrase qui les portait (`<a href="…">Trio</a>` → "Trio").
# On les remplace par `#URL{n}#` avant l'appel LLM, comme on le fait pour les
# code blocks. Bornes : tout sauf whitespace, balises HTML, guillemets, et
# parenthèses Markdown (qui clôturent `[text](url)`).
_URL_PROTECTION_REGEX = re.compile(r"https?://[^\s<>\"'()\[\]{}]+")


def _protect_urls(content):
    urls = [m.group(0) for m in _URL_PROTECTION_REGEX.finditer(content)]
    placeholders = [f"#URL{i}#" for i in range(len(urls))]
    # Replace one at a time : deux URLs byte-identical doivent recevoir des
    # placeholders distincts (cohérent avec _protect_code_blocks).
    for placeholder, url in zip(placeholders, urls, strict=False):
        content = content.replace(url, placeholder, 1)
    return content, urls, placeholders


def _restore_urls(translated_content, urls, placeholders):
    for placeholder, url in zip(placeholders, urls, strict=False):
        translated_content = translated_content.replace(placeholder, url)
    return translated_content


# Anchors locales : 3 patterns à protéger
# 1. `<a name="X"></a>` explicite (destination Terraform-style, jamais traduit)
# 2. `[text](#X)` où X correspond à un `<a name>` (référence Terraform, byte-identical)
# 3. `[text](#X)` où X correspond au slug d'un heading du document (TOC) :
#    on protège la paire (heading, fragment) pendant l'appel LLM, puis on
#    regénère le fragment avec le slug du heading TRADUIT post-restore. Ainsi
#    le TOC pointe TOUJOURS vers le bon heading, peu importe ce que le LLM
#    fait au heading et au TOC indépendamment (cf. express-zh : LLM traduit
#    le TOC mais pas le heading → fragment et heading se désynchronisent).
_ANCHOR_NAME_REGEX = re.compile(r'<a\s+name=["\']([^"\']+)["\']\s*></a>')
_ANCHOR_LINK_REGEX = re.compile(r"\(#([^)\s]+)\)")
# `[ \t]+` (non `\s+`) : whitespace intra-ligne, strictement non-ambigu.
# `[^\n]+` greedy borné par le `\n` final, pas de backtracking polynomial.
# `.strip()` côté Python pour trimmer les espaces finaux capturés.
# fmt: off
_HEADING_REGEX = re.compile(r"^(#{1,6})[ \t]+([^\n]+)$", re.MULTILINE)  # NOSONAR S5852
# fmt: on


def _github_slug(heading_text):
    """Approximation du slug GitHub d'un heading.

    Règles GitHub : strip markdown emphasis, lowercase, espaces → `-`,
    suppression de la ponctuation sauf `-` `_` et chars Unicode utiles.
    On conserve aussi les marques combinantes Unicode (`Mn`, `Mc`, `Me`) :
    sans elles, les anchors Devanagari perdent leurs voyelles
    (`विषय-सूची` → `वषय-सच`) et ne correspondent plus aux slugs GitHub.
    Pas exhaustif (github-slugger gère aussi les emojis, doublons d'id, etc.)
    mais suffisant pour matcher les TOC vers les headings dans la majorité des cas.
    """
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading_text)  # markdown links
    text = _HTML_TAG_REGEX.sub("", text)  # HTML tags
    text = re.sub(r"[*_`~]+", "", text)  # emphasis
    text = text.lower()
    text = re.sub(r"\s+", "-", text)
    kept = []
    for char in text:
        category = unicodedata.category(char)
        if char in {"-", "_"} or category[0] in {"L", "M", "N"}:
            kept.append(char)
    return "".join(kept).strip("-")


def _extract_heading_slugs(content):
    """Liste ordonnée des slugs des headings (par position dans le doc)."""
    return [_github_slug(m.group(2).strip()) for m in _HEADING_REGEX.finditer(content)]


def _protect_anchors(content):
    explicit_targets = {m.group(1) for m in _ANCHOR_NAME_REGEX.finditer(content)}
    heading_slugs = set(_extract_heading_slugs(content))
    anchors = []
    metadata = []  # parallèle à anchors : {"type": "explicit"|"terraform"|"heading", "slug": str|None}

    # 1. Tous les <a name="X"></a> (toujours protégés byte-identical).
    for m in _ANCHOR_NAME_REGEX.finditer(content):
        anchors.append(m.group(0))
        metadata.append({"type": "explicit", "slug": None})

    # 2. (#X) où X correspond à un target explicite OU à un slug de heading source.
    for m in _ANCHOR_LINK_REGEX.finditer(content):
        fragment_unescaped = m.group(1).replace(r"\_", "_").replace(r"\-", "-")
        if fragment_unescaped in explicit_targets:
            anchors.append(m.group(0))
            metadata.append({"type": "terraform", "slug": fragment_unescaped})
        elif fragment_unescaped in heading_slugs:
            anchors.append(m.group(0))
            metadata.append({"type": "heading", "slug": fragment_unescaped})

    placeholders = [f"#ANCHOR{i}#" for i in range(len(anchors))]
    for placeholder, anchor in zip(placeholders, anchors, strict=False):
        content = content.replace(anchor, placeholder, 1)
    return content, anchors, placeholders, metadata


def _restore_anchors(
    translated_content, anchors, placeholders, metadata, source_heading_slugs, target_heading_slugs
):
    """Restaure chaque placeholder par son anchor original.
    Pour les heading-derived (`type="heading"`), regénère le fragment avec le
    slug du heading TRADUIT correspondant (mapping par position) — ainsi le
    TOC pointe vers le heading traduit même si LLM a divergé entre eux.
    """
    slug_map = _build_heading_slug_map(source_heading_slugs, target_heading_slugs)
    for placeholder, anchor, meta in zip(placeholders, anchors, metadata, strict=False):
        if meta["type"] == "heading" and meta["slug"] in slug_map:
            new_slug = slug_map[meta["slug"]]
            new_anchor = f"(#{new_slug})"
            translated_content = translated_content.replace(placeholder, new_anchor)
        else:
            translated_content = translated_content.replace(placeholder, anchor)
    return translated_content


def _build_heading_slug_map(source_slugs, target_slugs):
    """Mapping source_slug → target_slug par position. Retourne {} si les
    listes ont des longueurs différentes (impossible de matcher fiablement)."""
    if len(source_slugs) != len(target_slugs):
        return {}
    return {src: tgt for src, tgt in zip(source_slugs, target_slugs, strict=False) if src != tgt}


# Reference-style links Markdown : `[![alt][label1]][label2]` + définitions
# `[label1]: URL` et `[label2]: URL` séparées en bas du document. Le LLM
# traduit naturellement les `alt` text et les link text visibles, mais oublie
# parfois de propager le changement aux LABELS (clés techniques utilisées par
# Markdown pour matcher inline ↔ definition). Cas concret deno-hi :
#   header: [![Twitter बैज][]][Twitter link]   ← label image traduit en HI
#   bottom: [Twitter badge]: URL                ← label PAS traduit (toujours EN)
# → Markdown ne fait pas le lien `Twitter बैज` ↔ `Twitter badge` → badge cassé.
#
# Solution pipeline : protéger TOUS les labels (clés techniques, jamais traduits)
# en placeholders `#REFLABEL{n}#` avant l'appel LLM. Le LLM traduit les textes
# visibles mais ne touche pas aux clés. Restoration byte-identical.
_REF_DEFINITION_REGEX = re.compile(r"^(\[)([^\]\n]+)(\]:\s+\S[^\n]*)$", re.MULTILINE)


def _protect_ref_labels(content):
    labels = []
    label_to_idx = {}
    for m in _REF_DEFINITION_REGEX.finditer(content):
        label = m.group(2)
        if label not in label_to_idx:
            label_to_idx[label] = len(labels)
            labels.append(label)
    if not labels:
        return content, [], []

    placeholders = [f"#REFLABEL{i}#" for i in range(len(labels))]

    def replace_def(m):
        return m.group(1) + placeholders[label_to_idx[m.group(2)]] + m.group(3)

    content = _REF_DEFINITION_REGEX.sub(replace_def, content)

    # Collapsed form `[label][]` (Markdown utilise `label` comme clé) → `[label][#PH#]`.
    # Full reference `][label]` (suit la fermeture d'un autre `[...]`) → `][#PH#]`.
    # Shortcut form `[label]` (pas suivi de `(`, `[`, `:` → utilise `label` comme
    # clé) → `[label][#PH#]`. Skip si c'est en fait un titre `[label]:` (def).
    for label, ph in zip(labels, placeholders, strict=False):
        esc = re.escape(label)
        content = re.sub(rf"\[({esc})\]\[\]", rf"[\1][{ph}]", content)
        content = re.sub(rf"\]\[{esc}\]", f"][{ph}]", content)
        # Shortcut : `[label]` non suivi de `(`, `[`, `:` (= def)
        content = re.sub(
            rf"\[({esc})\](?![\(\[:])(?![^\n]*\]:)",
            rf"[\1][{ph}]",
            content,
        )

    return content, labels, placeholders


def _restore_ref_labels(translated_content, labels, placeholders):
    for placeholder, label in zip(placeholders, labels, strict=False):
        translated_content = translated_content.replace(placeholder, label)
    return translated_content


def _protect_news_quotes(content, args):
    if not args.news:
        return content, [], []

    original_quotes = []
    attribution_urls = []

    def citation_replacer(match):
        idx = len(original_quotes)
        original_quotes.append(match.group(1))
        attribution = match.group(3)
        if attribution:
            url_match = re.search(r"\((.+?)\)", attribution)
            if url_match:
                attribution_urls.append(url_match.group(1))
        protected = f"{news_quote_placeholder(idx)}\n>\n{match.group(2)}"
        if attribution:
            protected += f"\n{attribution}"
        return protected

    content = _NEWS_CITATION_REGEX.sub(citation_replacer, content)
    if original_quotes:
        print(f"  → {len(original_quotes)} citation(s) EN protégée(s)")
    return content, original_quotes, attribution_urls


def _restore_code(
    translated_content, inline_codes, inline_placeholders, code_blocks, block_placeholders
):
    # Restore inline first, then fenced (matches extraction order).
    for placeholder, inline in zip(inline_placeholders, inline_codes, strict=False):
        translated_content = translated_content.replace(placeholder, inline)
    for placeholder, block in zip(block_placeholders, code_blocks, strict=False):
        translated_content = translated_content.replace(placeholder, block)
    return translated_content


def _validate_news_placeholders_intact(translated_content, n_quotes):
    for idx in range(n_quotes):
        if not news_quote_placeholder_regex(idx).search(translated_content):
            raise RuntimeError(
                f"VALIDATION: Placeholder {news_quote_placeholder(idx)} manquant "
                "dans la traduction (le LLM l'a supprimé ou modifié)"
            )


_CODE_PLACEHOLDER_LEFTOVER_REGEX = re.compile(r"#(?:CODEBLOCK|INLINECODE|URL|ANCHOR|REFLABEL)\d+#")


def _check_placeholders_present(translated_content, placeholders, kind_label=""):
    """Vérifie qu'un set de placeholders est intact dans la sortie LLM. `kind_label`
    enrichit le message d'erreur (e.g. 'l'URL', 'l'ancre locale')."""
    suffix = f" ({kind_label})" if kind_label else ""
    for placeholder in placeholders:
        if placeholder not in translated_content:
            raise RuntimeError(
                f"VALIDATION: Placeholder {placeholder} manquant dans la traduction "
                f"(le LLM l'a supprimé ou modifié{suffix})"
            )


def _validate_code_placeholders_present(
    translated_content,
    block_placeholders,
    inline_placeholders,
    url_placeholders=(),
    anchor_placeholders=(),
    ref_label_placeholders=(),
):
    """Vérifie que chaque placeholder émis (code blocks, inline code, URLs, anchors,
    reference labels) est bien présent dans la sortie LLM avant la restauration."""
    groups = (
        (block_placeholders, ""),
        (inline_placeholders, ""),
        (url_placeholders, "URL"),
        (anchor_placeholders, "ancre locale"),
        (ref_label_placeholders, "label reference-style"),
    )
    for placeholders, kind_label in groups:
        _check_placeholders_present(translated_content, placeholders, kind_label)


def _validate_ref_label_placeholders_present(translated_content, placeholders):
    """Validation explicite pre-restoration des reference-link labels (alias avec
    message dédié pour faciliter le debug)."""
    for placeholder in placeholders:
        if placeholder not in translated_content:
            raise RuntimeError(
                f"VALIDATION: Placeholder {placeholder} manquant dans la traduction "
                "(le LLM a supprimé ou modifié un label reference-style)"
            )


def _validate_no_code_placeholder_leftover(translated_content):
    """Vérifie qu'aucun placeholder #CODEBLOCKn# / #INLINECODEn# ne subsiste après
    restauration (sinon il fuirait verbatim dans le fichier de sortie)."""
    leftover = _CODE_PLACEHOLDER_LEFTOVER_REGEX.search(translated_content)
    if leftover:
        raise RuntimeError(
            f"VALIDATION: Placeholder de code {leftover.group(0)!r} non restauré "
            "(décalage d'index entre extraction et restauration)"
        )


def _restore_news_quotes(translated_content, original_quotes):
    for idx, quote in enumerate(original_quotes):
        translated_content, restored_count = news_quote_placeholder_regex(idx).subn(
            quote, translated_content
        )
        if restored_count != 1:
            raise RuntimeError(
                f"VALIDATION: Placeholder {news_quote_placeholder(idx)} restauré "
                f"{restored_count} fois (attendu: 1)"
            )
    return translated_content


def _normalize_collapsed_markdown(translated_content):
    """Sépare HR/lien collés à un heading sur la même ligne (post-LLM cleanup).

    Patterns toujours invalides en markdown standard :
      "--- ## Title"      → "---\\n\\n## Title"
      "](url) ## Title"   → "](url)\\n\\n## Title"
    """
    translated_content = re.sub(
        r"^--- (##+ )", r"---\n\n\1", translated_content, flags=re.MULTILINE
    )
    translated_content = re.sub(r"(\]\([^)]+\)) (##+ )", r"\1\n\n\2", translated_content)
    if re.search(r"^---[ \t]+##+ ", translated_content, flags=re.MULTILINE):
        raise RuntimeError("VALIDATION: séparateur markdown collé à un heading (`--- ##`)")
    if re.search(r"\]\([^)]+\)[ \t]+##+ ", translated_content):
        raise RuntimeError("VALIDATION: lien markdown collé à un heading (`](url) ##`)")
    return translated_content


def _cleanup_source_flag_for_en(translated_content, source_flag):
    """Cas target=en : supprime la ligne `> 🇫🇷 _..._` orpheline (citation FR
    annotée que le mode news copie pour les autres targets, mais redondante en EN)."""
    pattern = re.compile(
        r"(^|\n)>\s*\n(>\s*" + re.escape(source_flag) + r"[^\n]*\n)",
        flags=re.MULTILINE,
    )
    new_content, n = pattern.subn(r"\1", translated_content)
    if n > 0:
        print(f"  → {n} ligne(s) `> {source_flag} _trad_` supprimée(s) en cible EN (cleanup)")
        return new_content
    return translated_content


def _cleanup_source_flag_swap(translated_content, source_flag, target_flag):
    """Cas target≠en : swap drapeau source → drapeau cible dans les lignes
    citation `> 🇫🇷 …` (scope strict ; un replace global toucherait aussi les
    citations EN restaurées citant nommément une source FR — cas rare mais réel)."""
    pattern = re.compile(rf"^(>[ \t]+){re.escape(source_flag)}", flags=re.MULTILINE)
    translated_content, count = pattern.subn(rf"\g<1>{target_flag}", translated_content)
    if count:
        print(
            f"  → {count} drapeau(x) source {source_flag} remplacé(s) par {target_flag} (cleanup)"
        )
    return translated_content


def _cleanup_source_flag(translated_content, args):
    """Source-flag cleanup en --news quand source != target. Dispatch sur les
    deux variantes : cas A (target=en, drop) ou cas B (target≠en, swap)."""
    if not (args.news and args.source_lang != args.target_lang):
        return translated_content
    source_flag = LANG_FLAGS.get(args.source_lang)
    if not (source_flag and source_flag in translated_content):
        return translated_content
    if args.target_lang == "en":
        return _cleanup_source_flag_for_en(translated_content, source_flag)
    target_flag = LANG_FLAGS.get(args.target_lang)
    if target_flag:
        return _cleanup_source_flag_swap(translated_content, source_flag, target_flag)
    return translated_content


def _validate_news_flags_for_en(translated_content):
    for lang_code, flag in LANG_FLAGS.items():
        if lang_code != "en" and flag in translated_content:
            raise RuntimeError(
                f"VALIDATION: Drapeau {flag} ({lang_code}) trouvé dans la traduction EN "
                "(devrait être absent)"
            )


def _validate_news_flags_for_other(translated_content, args, expected_target_count):
    target_flag = LANG_FLAGS.get(args.target_lang)
    if target_flag:
        flag_count = translated_content.count(target_flag)
        if flag_count != expected_target_count:
            raise RuntimeError(
                f"VALIDATION: Drapeau {target_flag} trouvé {flag_count} fois "
                f"(attendu: {expected_target_count})"
            )
    source_flag = LANG_FLAGS.get(args.source_lang)
    if source_flag and source_flag in translated_content:
        raise RuntimeError(
            f"VALIDATION: Drapeau source {source_flag} encore présent dans la traduction"
        )


def _validate_news_post(translated_content, original_quotes, attribution_urls, args):
    for quote in original_quotes:
        if quote not in translated_content:
            raise RuntimeError("VALIDATION: citation EN brute non restaurée dans la traduction")
    for url in attribution_urls:
        if url not in translated_content:
            raise RuntimeError(
                f"VALIDATION: URL d'attribution '{url}' manquante dans la traduction"
            )
    if _RESIDUAL_NEWS_PLACEHOLDER_REGEX.search(translated_content):
        raise RuntimeError("VALIDATION: placeholder news résiduel après restauration")
    if args.target_lang == "en":
        _validate_news_flags_for_en(translated_content)
    else:
        _validate_news_flags_for_other(translated_content, args, len(original_quotes))


def _translation_note_invariants():
    """Parties INVARIANTES de la note de traduction (jamais envoyées au LLM).

    Le titre du repo et l'URL GitHub ne doivent JAMAIS être altérés par le
    LLM (slug, casse, backticks, scheme), donc on les assemble côté Python
    après traduction de la phrase descriptive. Voir `_append_translation_note`.
    """
    title = "**`ai-powered-markdown-translator`**"
    link = "[Voir le projet sur GitHub ↗](https://github.com/jls42/ai-powered-markdown-translator)"
    return title, link


def _build_translation_note_phrase(args):
    """Phrase descriptive — SEULE partie envoyée au LLM pour traduction."""
    return (
        "Article traduit du "
        + args.source_lang
        + " vers le "
        + args.target_lang
        + " avec "
        + args.model
        + "."
    )


def _assemble_translation_note_paragraphs(phrase):
    """Forme canonique 3-paragraphes : titre (Python) + phrase + lien (Python).

    Appelée à la fois par `_build_translation_note_source` (vue source pour
    documentation/tests) et par `_append_translation_note` (vue runtime avec
    la phrase déjà traduite). Garantit que les deux paths produisent un bloc
    structurellement identique.
    """
    title, link = _translation_note_invariants()
    return title + "\n\n" + phrase + "\n\n" + link


def _build_translation_note_source(args):
    """Émet la note source non traduite en 3 paragraphes (style "GitHub repo embed card") :

    1. Titre repo (nom du projet en code inline + gras) — invariant assemblé en Python.
    2. Description (phrase explicative) — seule partie traduite par le LLM.
    3. Lien CTA Markdown avec arrow visible — invariant assemblé en Python.
    """
    return _assemble_translation_note_paragraphs(_build_translation_note_phrase(args))


def _sanitize_model(model):
    cleaned = re.sub(r"[^A-Za-z0-9._:/-]+", "_", model).strip("_")
    return cleaned or "unknown"


def _quote_lines(text):
    """Préfixe chaque ligne par '> ', en préservant les lignes vides comme '>'.

    La préservation d'une ligne vide en `>` est cruciale : elle permet à mdast
    de voir deux paragraphes distincts dans le même blockquote (sentence + CTA),
    plutôt qu'un seul paragraphe avec un line-break interne.
    """
    out = []
    for ln in text.strip().splitlines():
        stripped = ln.rstrip()
        if stripped:
            out.append(f"> {stripped}")
        else:
            out.append(">")
    return "\n".join(out)


def _split_frontmatter(content):
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return "", content
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter = "".join(lines[: index + 1]).rstrip("\n")
            body = "".join(lines[index + 1 :]).lstrip("\n")
            return frontmatter, body
    # Opening `---` sans fence de fermeture : insérer la note sans erreur
    # produirait un fichier mal formé (note placée au-dessus d'un `---`
    # orphelin). On préfère faire échouer le fichier (failed_files dans
    # translate_markdown_file) plutôt qu'écrire silencieusement un output
    # cassé.
    raise RuntimeError("malformed frontmatter: opening '---' without closing fence")


def _build_translation_note_block(args, translated_note, placement, fmt):
    if fmt == "legacy":
        return "**" + translated_note.strip() + "**"
    safe_model = _sanitize_model(args.model)
    title = (
        f"v=1 source={args.source_lang} target={args.target_lang} "
        f"model={safe_model} date={datetime.date.today().isoformat()}"
    )
    # 3+ paragraphes : forme canonique titre/desc/lien — on garde tel quel.
    # 2 paragraphes : wrap UNIQUEMENT la phrase en gras, le lien reste hors
    #   du `<strong>` (rendu fragile dans certains renderers).
    # 1 paragraphe : fallback emphase, sauf si la chaîne contient un lien
    #   Markdown `](` — la mise en gras d'un lien est fragile, on émet brut.
    parts = re.split(r"\n\s*\n", translated_note.strip())
    if len(parts) >= 3:
        body = "\n\n".join(p.strip() for p in parts)
    elif len(parts) == 2:
        body = "**" + parts[0].strip() + "**\n\n" + parts[1].strip()
    else:
        raw = translated_note.strip()
        body = raw if "](" in raw else "**" + raw + "**"
    quoted = _quote_lines(body)
    # Blank line between definition and blockquote keeps the output Prettier-friendly
    # (Prettier MDX inserts one anyway). The remark plugin still detects the adjacent
    # blockquote — mdast does not nodify the blank-line separator.
    return f'[ai-translation-note-{placement}]: <> "{title}"\n\n{quoted}'


def _compose_with_notes(content, args, translated_note, fmt):
    pos = getattr(args, "note_position", "bottom")
    base = content.rstrip("\n")
    blocks = {
        "top": _build_translation_note_block(args, translated_note, "top", fmt),
        "bottom": _build_translation_note_block(args, translated_note, "bottom", fmt),
    }

    if pos == "bottom":
        return base + "\n\n" + blocks["bottom"] + "\n"

    # Frontmatter parsing only when the layout actually inserts above the body :
    # un opening `---` sans fence de fermeture lève RuntimeError, et on ne veut
    # pas faire échouer un fichier dont la note ne touche que le bas.
    frontmatter, body = _split_frontmatter(base)

    if pos == "top":
        if frontmatter:
            return frontmatter + "\n\n" + blocks["top"] + "\n\n" + body.rstrip("\n") + "\n"
        return blocks["top"] + "\n\n" + base + "\n"

    if pos == "both":
        if frontmatter:
            return (
                frontmatter
                + "\n\n"
                + blocks["top"]
                + "\n\n"
                + body.rstrip("\n")
                + "\n\n"
                + blocks["bottom"]
                + "\n"
            )
        return blocks["top"] + "\n\n" + base + "\n\n" + blocks["bottom"] + "\n"

    raise ValueError(f"unknown note_position: {pos}")


def _append_translation_note(translated_content, client, args, use_mistral, use_claude, use_gemini):
    # On ne soumet au LLM QUE la phrase descriptive : titre du repo et lien
    # GitHub sont assemblés côté Python pour garantir l'invariance du slug
    # `ai-powered-markdown-translator` et de l'URL (que la fonction
    # `translate()` n'aurait protégés ni via `_protect_inline_code`, ni via
    # `_protect_code_blocks` — ces protections vivent dans `_translate_pipeline`).
    fmt = getattr(args, "note_format", "legacy")
    phrase_source = _build_translation_note_phrase(args)
    translated_phrase = translate(
        phrase_source, client, args, use_mistral, use_claude, use_gemini, True
    ).strip()
    if fmt == "marker":
        translation_note = _assemble_translation_note_paragraphs(translated_phrase)
    else:
        translation_note = translated_phrase
    return _compose_with_notes(translated_content, args, translation_note, fmt)


def _resolve_relative_paths(file_path, output_path, args):
    relative_file_path = os.path.join(
        args.source_dir, os.path.relpath(file_path, start=args.source_dir)
    )
    relative_output_path = os.path.join(
        args.target_dir, os.path.relpath(output_path, start=args.target_dir)
    )
    return relative_file_path, relative_output_path


def _write_output_file(output_path, translated_content, force, relative_output_path):
    """Écrit le fichier ou skippe si destination existe sans --force.

    Returns "success" si écrit, "skipped" si destination déjà présente.
    """
    clean_output_path = os.path.normpath(output_path)
    if os.path.exists(clean_output_path) and not force:
        print(
            f"Le fichier '{relative_output_path}' existe déjà, aucune traduction n'est effectuée."
        )
        return "skipped"
    with open(clean_output_path, "w", encoding="utf-8") as f:
        f.write(translated_content)
    return "success"


@dataclass
class _PipelineState:
    """Artefacts collectés lors de la phase `protect` du pipeline, conservés
    pour la phase `restore` post-LLM."""

    code_blocks: list
    block_placeholders: list
    inline_codes: list
    inline_placeholders: list
    original_quotes: list
    attribution_urls: list
    source_heading_slugs: list
    anchors: list
    anchor_placeholders: list
    anchor_metadata: list
    ref_labels: list
    ref_label_placeholders: list
    urls: list
    url_placeholders: list


def _protect_pipeline_inputs(content, args):
    """Phase `protect` du pipeline : extrait dans l'ordre code/news/anchors/
    ref-labels/urls. L'ordre est critique (cf. commentaires inline) — toute
    inversion casse soit la capture des `attribution_urls` news, soit le
    matching des regex de placeholder qui peuvent se confondre."""
    content, code_blocks, block_placeholders = _protect_code_blocks(content)
    content, inline_codes, inline_placeholders = _protect_inline_code(content)
    # News quotes AVANT URLs : capture les `attribution_urls` réelles avant
    # qu'elles ne soient remplacées par `#URL{n}#`.
    content, original_quotes, attribution_urls = _protect_news_quotes(content, args)
    # Capture les slugs des headings source pour resync TOC post-LLM.
    source_heading_slugs = _extract_heading_slugs(content)
    # Anchors AVANT urls : éviter que `\(#[^)\s]+\)` matche `(#URL\d+#)`.
    content, anchors, anchor_placeholders, anchor_metadata = _protect_anchors(content)
    # Reference-style labels avant URLs : la def `[label]: URL` doit garder
    # sa structure `[#REFLABEL{n}#]: #URL{n}#`.
    content, ref_labels, ref_label_placeholders = _protect_ref_labels(content)
    content, urls, url_placeholders = _protect_urls(content)

    state = _PipelineState(
        code_blocks=code_blocks,
        block_placeholders=block_placeholders,
        inline_codes=inline_codes,
        inline_placeholders=inline_placeholders,
        original_quotes=original_quotes,
        attribution_urls=attribution_urls,
        source_heading_slugs=source_heading_slugs,
        anchors=anchors,
        anchor_placeholders=anchor_placeholders,
        anchor_metadata=anchor_metadata,
        ref_labels=ref_labels,
        ref_label_placeholders=ref_label_placeholders,
        urls=urls,
        url_placeholders=url_placeholders,
    )
    return content, state


def _restore_pipeline_outputs(translated_content, state, args):
    """Phase `restore` du pipeline : valide placeholders → restore en ordre
    inverse (urls → ref_labels → anchors → code) → news/cleanup → validate."""
    _validate_code_placeholders_present(
        translated_content,
        state.block_placeholders,
        state.inline_placeholders,
        state.url_placeholders,
        state.anchor_placeholders,
        state.ref_label_placeholders,
    )
    target_heading_slugs = _extract_heading_slugs(translated_content)
    translated_content = _restore_urls(translated_content, state.urls, state.url_placeholders)
    translated_content = _restore_ref_labels(
        translated_content, state.ref_labels, state.ref_label_placeholders
    )
    translated_content = _restore_anchors(
        translated_content,
        state.anchors,
        state.anchor_placeholders,
        state.anchor_metadata,
        state.source_heading_slugs,
        target_heading_slugs,
    )
    translated_content = _restore_code(
        translated_content,
        state.inline_codes,
        state.inline_placeholders,
        state.code_blocks,
        state.block_placeholders,
    )
    _validate_no_code_placeholder_leftover(translated_content)

    if args.news and state.original_quotes:
        _validate_news_placeholders_intact(translated_content, len(state.original_quotes))
    translated_content = _restore_news_quotes(translated_content, state.original_quotes)
    translated_content = _normalize_collapsed_markdown(translated_content)
    translated_content = _cleanup_source_flag(translated_content, args)

    if args.news and state.original_quotes:
        _validate_news_post(translated_content, state.original_quotes, state.attribution_urls, args)
    return translated_content


@dataclass
class _TranslationConfig:
    """Regroupe les paramètres de traduction (client + flags providers + flags
    fonctionnels) pour réduire les signatures publiques `translate_markdown_file`,
    `translate_directory` et helpers internes (passaient 7-9 params positionnels)."""

    client: object
    args: object
    use_mistral: bool = False
    use_claude: bool = False
    use_gemini: bool = False
    add_translation_note: bool = False
    force: bool = False


def _translate_pipeline(content, config):
    """Pipeline complet : protect → translate → restore → validate."""
    content, state = _protect_pipeline_inputs(content, config.args)
    translated_content = translate(
        content,
        config.client,
        config.args,
        config.use_mistral,
        config.use_claude,
        config.use_gemini,
    )
    return _restore_pipeline_outputs(translated_content, state, config.args)


def _read_translatable_source(file_path, relative_file_path):
    """Lit le fichier source. Retourne (content, status) où status est `None`
    si OK, `"skipped"` si vide (le caller propage)."""
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    if not content:
        print(f"Le fichier '{relative_file_path}' est vide, aucune traduction n'est effectuée.")
        return content, "skipped"
    return content, None


def _translate_one_file(file_path, output_path, config):
    """Cœur de `translate_markdown_file` sans la gestion d'erreurs externes.
    Lève toute exception au caller, qui la convertit en status `"failure"`."""
    relative_file_path, relative_output_path = _resolve_relative_paths(
        file_path, output_path, config.args
    )
    print(f"Traitement du fichier : {relative_file_path}")
    start_time = time.time()

    content, status = _read_translatable_source(file_path, relative_file_path)
    if status is not None:
        return status

    translated_content = _translate_pipeline(content, config)
    if config.add_translation_note:
        translated_content = _append_translation_note(
            translated_content,
            config.client,
            config.args,
            config.use_mistral,
            config.use_claude,
            config.use_gemini,
        )

    status = _write_output_file(output_path, translated_content, config.force, relative_output_path)
    if status == "success":
        print(
            f"Fichier '{relative_file_path}' traduit en {time.time() - start_time:.2f} secondes "
            f"et enregistré sous : {relative_output_path}"
        )
    return status


def translate_markdown_file(file_path, output_path, config):
    """Retourne "success" / "skipped" (vide ou déjà traduit) / "failure"
    (toute exception est attrapée et propagée par status, sans écrire le fichier)."""
    relative_file_path = file_path
    try:
        return _translate_one_file(file_path, output_path, config)
    except OSError as e:
        print(f"Erreur lors du traitement du fichier '{relative_file_path}': {e}", file=sys.stderr)
        traceback.print_exc()
        return "failure"
    except Exception as e:
        print(
            f"Une erreur inattendue est survenue lors de la traduction du fichier "
            f"'{relative_file_path}' ({type(e).__name__}): {e}\n"
            "Veuillez relancer le traitement pour ce fichier.",
            file=sys.stderr,
        )
        traceback.print_exc()
        return "failure"


def is_excluded(path):
    return any(pattern in path for pattern in EXCLUDE_PATTERNS)


def _should_skip_walk_dir(root, output_dir, output_base_dir, input_dir):
    if is_excluded(root) or root.startswith(output_dir):
        return True
    # Skip un sous-répertoire direct d'input qui porte le même nom que le dossier de sortie.
    return (
        os.path.basename(root) == output_base_dir
        and os.path.abspath(os.path.join(root, "..")) == input_dir
    )


def _resolve_output_filename(file, base, args):
    if args.keep_filename:
        return file
    if args.include_model:
        return f"{base}-{args.target_lang}-{args.model}.md"
    return f"{base}-{args.target_lang}.md"


def _existing_translation_exists(output_path, output_dir, base, args):
    if args.keep_filename:
        return os.path.exists(output_path)
    target_language_files = glob.glob(
        f"{output_dir}/**/{base}-{args.target_lang}*.md", recursive=True
    ) + glob.glob(f"{output_dir}/**/{base}-*{args.target_lang}.md", recursive=True)
    return any(os.path.exists(f) for f in target_language_files)


def _record_translation_status(status, file, file_path, failed_files, skipped_files):
    if status == "success":
        print(f"Fichier '{file}' traité.")
    elif status == "skipped":
        skipped_files.append(file_path)
    elif status == "failure":
        failed_files.append(file_path)
    else:
        # Default-fail sur statut inattendu (régression future).
        print(
            f"WARNING: Statut inattendu pour '{file}': {status!r} -> traité comme échec",
            file=sys.stderr,
        )
        failed_files.append(file_path)


@dataclass
class _DirectoryWalkContext:
    """Contexte d'un walk récursif `translate_directory` : config + chemins
    racines + accumulateurs. Réduit la signature de `_process_one_markdown_file`
    à 3 params (file, root, ctx)."""

    input_dir: str
    output_dir: str
    config: _TranslationConfig
    failed_files: list
    skipped_files: list


def _process_one_markdown_file(file, root, ctx):
    file_path = os.path.join(root, file)
    base, _ext = os.path.splitext(file)
    output_file = _resolve_output_filename(file, base, ctx.config.args)
    relative_path = os.path.relpath(root, ctx.input_dir)
    output_path = os.path.join(ctx.output_dir, relative_path, output_file)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    already_exists = _existing_translation_exists(
        output_path, ctx.output_dir, base, ctx.config.args
    )
    if already_exists and not ctx.config.force:
        print(f"La traduction de '{file}' existe déjà, aucune action effectuée.")
        ctx.skipped_files.append(file_path)
        return

    status = translate_markdown_file(file_path, output_path, ctx.config)
    _record_translation_status(status, file, file_path, ctx.failed_files, ctx.skipped_files)


def _is_translatable_markdown(file):
    return (file.endswith(".md") or file.endswith(".mdx")) and not is_excluded(file)


def translate_directory(input_dir, output_dir, config):
    """Walk récursif. Retourne {"failed": [...], "skipped": [...]} avec les
    chemins absolus des fichiers ; le caller agrège pour décider de exit(1)."""
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_base_dir = os.path.basename(output_dir)

    ctx = _DirectoryWalkContext(
        input_dir=input_dir,
        output_dir=output_dir,
        config=config,
        failed_files=[],
        skipped_files=[],
    )

    for root, _dirs, files in os.walk(input_dir, topdown=True):
        if _should_skip_walk_dir(root, output_dir, output_base_dir, input_dir):
            continue
        for file in files:
            if not _is_translatable_markdown(file):
                continue
            _process_one_markdown_file(file, root, ctx)

    return {"failed": ctx.failed_files, "skipped": ctx.skipped_files}


def _add_io_args(parser):
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


def _add_lang_args(parser):
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


def _add_provider_args(parser):
    parser.add_argument(
        "--model",
        type=str,
        help="Modèle GPT à utiliser pour la traduction, la valeur par défaut dépend de l'API sélectionnée",
    )
    parser.add_argument(
        "--use_mistral", action="store_true", help="Utiliser l'API Mistral AI pour la traduction"
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
        "--eco",
        action="store_true",
        help="Utiliser les modèles économiques (mini/flash) au lieu des modèles qualité",
    )
    parser.add_argument(
        "--reasoning_effort",
        choices=("low", "medium", "high"),
        default="medium",
        help="Effort de raisonnement OpenAI GPT-5.x (défaut: medium)",
    )


def _add_output_naming_args(parser):
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


def _add_note_args(parser):
    parser.add_argument(
        "--add_translation_note",
        action="store_true",
        help="Ajouter une note de traduction au contenu traduit",
    )
    parser.add_argument(
        "--note_position",
        choices=["top", "bottom", "both"],
        default="bottom",
        help="Position de la note de traduction (défaut: bottom). Requiert --add_translation_note.",
    )
    parser.add_argument(
        "--note_format",
        choices=["legacy", "marker"],
        default="legacy",
        help=(
            "Format de la note de traduction (défaut: legacy = paragraphe gras compatible v1.9). "
            "'marker' produit une link reference definition + blockquote (consommable par un plugin "
            "Markdown comme remark-translation-banner)."
        ),
    )


def _add_news_args(parser):
    parser.add_argument(
        "--news",
        action="store_true",
        help="Active les règles de traduction des citations news (drapeaux + quotes EN protégées)",
    )


def _build_arg_parser():
    parser = argparse.ArgumentParser(description="Traduit les fichiers Markdown.")
    _add_io_args(parser)
    _add_lang_args(parser)
    _add_provider_args(parser)
    _add_output_naming_args(parser)
    _add_note_args(parser)
    _add_news_args(parser)
    return parser


def _validate_input_paths(args):
    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError(f"Le fichier spécifié n'existe pas : {args.file}")
    elif not os.path.isdir(args.source_dir):
        raise ValueError(f"Le répertoire source spécifié n'existe pas : {args.source_dir}")
    if not os.path.exists(args.target_dir):
        os.makedirs(args.target_dir)


def _init_mistral_client(args):
    args.model = args.model or (ECO_MODEL_MISTRAL if args.eco else DEFAULT_MODEL_MISTRAL)
    api_key = os.getenv("MISTRAL_API_KEY", DEFAULT_MISTRAL_API_KEY)
    if not api_key or api_key == DEFAULT_MISTRAL_API_KEY:
        raise ValueError(
            "Clé API Mistral non spécifiée. Définir MISTRAL_API_KEY dans l'environnement ou .env."
        )
    return Mistral(api_key=api_key)


def _init_claude_client(args):
    args.model = args.model or (ECO_MODEL_CLAUDE if args.eco else DEFAULT_MODEL_CLAUDE)
    api_key = os.getenv("ANTHROPIC_API_KEY", DEFAULT_ANTHROPIC_API_KEY)
    if not api_key or api_key == DEFAULT_ANTHROPIC_API_KEY:
        raise ValueError(
            "Clé API Claude non spécifiée. Définir ANTHROPIC_API_KEY dans l'environnement ou .env."
        )
    return anthropic.Anthropic(api_key=api_key)


def _init_gemini_client(args):
    args.model = args.model or (ECO_MODEL_GEMINI if args.eco else DEFAULT_MODEL_GEMINI)
    # Accepte GOOGLE_API_KEY (SDK historique google.generativeai) et GEMINI_API_KEY
    # (convention AI Studio, cohérent avec @google/genai côté JS/TS).
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY") or DEFAULT_GEMINI_API_KEY
    if not api_key or api_key == DEFAULT_GEMINI_API_KEY:
        raise ValueError(
            "Clé API Gemini non spécifiée. Définir GOOGLE_API_KEY ou "
            "GEMINI_API_KEY dans l'environnement ou .env."
        )
    genai.configure(api_key=api_key)
    return genai


def _init_openai_client(args):
    args.model = args.model or (ECO_MODEL_OPENAI if args.eco else DEFAULT_MODEL_OPENAI)
    openai_api_key = os.getenv("OPENAI_API_KEY", DEFAULT_OPENAI_API_KEY)
    if not openai_api_key or openai_api_key == DEFAULT_OPENAI_API_KEY:
        raise ValueError(
            "Clé API OpenAI non spécifiée. Définir OPENAI_API_KEY dans l'environnement ou .env."
        )
    return OpenAI(api_key=openai_api_key)


def _select_provider_client(args):
    if args.use_mistral:
        return _init_mistral_client(args)
    if args.use_claude:
        return _init_claude_client(args)
    if args.use_gemini:
        return _init_gemini_client(args)
    return _init_openai_client(args)


def _resolve_single_output_filename(args):
    if args.keep_filename:
        return os.path.basename(args.file)
    base = os.path.splitext(os.path.basename(args.file))[0]
    if args.include_model:
        return f"{base}-{args.target_lang}-{args.model}.md"
    return f"{base}-{args.target_lang}.md"


def _build_translation_config(args, client):
    return _TranslationConfig(
        client=client,
        args=args,
        use_mistral=args.use_mistral,
        use_claude=args.use_claude,
        use_gemini=args.use_gemini,
        add_translation_note=args.add_translation_note,
        force=args.force,
    )


def _run_single_file(args, client):
    output_file = _resolve_single_output_filename(args)
    output_path = os.path.join(args.target_dir, output_file)
    config = _build_translation_config(args, client)
    status = translate_markdown_file(args.file, output_path, config)
    # default-fail: tout statut hors {"success", "skipped"} compte comme échec
    return [] if status in ("success", "skipped") else [args.file]


def _run_directory(args, client):
    config = _build_translation_config(args, client)
    result = translate_directory(args.source_dir, args.target_dir, config)
    # default-fail jusqu'au bout : dict mal formé → traiter comme échec.
    return result.get("failed", ["<unexpected translate_directory result>"])


def main():
    """Entrée CLI : exit(1) si au moins un fichier a échoué, exit(0) sinon."""
    args = _build_arg_parser().parse_args()
    _validate_input_paths(args)
    client = _select_provider_client(args)

    if args.model not in MODEL_TOKEN_LIMITS:
        print(
            f"⚠ Modèle '{args.model}' non listé, utilisation de la limite par défaut ({DEFAULT_TOKEN_LIMIT} tokens)"
        )

    failed_files = _run_single_file(args, client) if args.file else _run_directory(args, client)

    if failed_files:
        print(
            f"ERROR: {len(failed_files)} file(s) failed: {failed_files}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
