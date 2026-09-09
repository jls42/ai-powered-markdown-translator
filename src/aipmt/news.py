"""Mode `--news` : citations anglaises protégées et drapeaux par langue.

Les citations sont remplacées par `<NEWSQUOTE id="N"/>` avant traduction, et
la ligne de traduction source (`> 🇫🇷 _…_`) est gérée selon la langue cible :
le prompt demande de la retirer pour l'anglais et d'en permuter les drapeaux
sinon, et un nettoyage de repli applique ici la même règle quand le modèle l'a
ignorée. Les règles injectées dans le prompt vivent ici aussi, à côté des
validations qui les vérifient.
"""

import re

from .markdown import (
    news_quote_placeholder,
    news_quote_placeholder_regex,
)

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


_NEWS_FINAL_CHECKS = (
    "\n\n<news_final_checks>"
    "\nAdditional checks for news mode: every `<NEWSQUOTE` tag must be present in its original Latin form with the same id; the target flag emoji count must equal the citation count; no source flag (🇫🇷) remains anywhere."
    "\n</news_final_checks>"
)


def _build_news_addendum(args):
    target_flag = LANG_FLAGS.get(args.target_lang, "")
    placeholder_example = news_quote_placeholder(0)
    if args.target_lang == "en":
        rules = _build_news_rules_en(placeholder_example)
    else:
        rules = _build_news_rules_other(args, target_flag, placeholder_example)
    return rules + _NEWS_FINAL_CHECKS


# News citation pattern: 1+ EN quote lines `> X` (excluding `> — attribution`)
# then `>` empty separator, then `> FLAG _trad_`, optional `> — attribution`.
# Multi-line EN quote bodies (common on long social-media quotes) MUST be captured
# as a single group to be re-emitted verbatim — see _protect_news_quotes.
_NEWS_CITATION_REGEX = re.compile(
    # Corps de la citation EN. Il peut couvrir PLUSIEURS paragraphes, donc la
    # répétition accepte les lignes `>` vides qui les séparent — sans quoi seul
    # le dernier paragraphe serait protégé et les précédents, laissés au LLM,
    # reviendraient traduits, exactement ce que --news existe pour empêcher.
    #
    # `.*` consomme la ligne entière d'un seul tenant : chaque itération n'a
    # qu'une seule façon de matcher. Une forme antérieure découpait la ligne en
    # `(?:[ \t]*$|[ \t]+.*)`, ce qui rendait le partage des espaces ambigu et,
    # combiné à la répétition, faisait exploser le backtracking — mesuré à
    # 2,6 s sur 14 lignes `>   texte` (indentation Markdown légale) qui ne
    # matchent pas, contre 0,04 ms ici, avec un facteur ~9 par ligne ajoutée.
    # Toute réécriture doit préserver cette absence de point de découpe.
    #
    # La répétition est non-gourmande pour ne pas déborder sur la citation
    # suivante quand deux se suivent.
    r"(^> (?!— ).+(?:\n^>(?![ \t]*—).*)*?)\n"
    r"^>[ \t]*\n"
    r"(^> .+_)[ \t]*"
    r"(?:\n(^> — .+?)[ \t]*)?$",
    re.MULTILINE,
)


_RESIDUAL_NEWS_PLACEHOLDER_REGEX = re.compile(r'<NEWSQUOTE\s+id=["\']\d+["\']\s*/>|#NEWSQUOTE\d+#')


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
            # Cible le `](url)` du markdown link `[text](url)` :
            # robuste aux parenthèses imbriquées (ex: `(relayé par [text](url))`)
            # et n'inclut pas le préfixe FR ("relayé par", "via", etc.) qui
            # serait traduit et casserait `_validate_news_post`.
            # On stocke uniquement l'URL pure : c'est un invariant préservé
            # par les placeholders #URL{N}# pendant la traduction.
            url_match = re.search(r"\]\(([^)]+)\)", attribution)
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


def _validate_news_placeholders_intact(translated_content, n_quotes):
    for idx in range(n_quotes):
        if not news_quote_placeholder_regex(idx).search(translated_content):
            raise RuntimeError(
                f"VALIDATION: Placeholder {news_quote_placeholder(idx)} manquant "
                "dans la traduction (le LLM l'a supprimé ou modifié)"
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
