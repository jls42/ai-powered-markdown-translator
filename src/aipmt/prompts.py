"""Construction des instructions système envoyées au modèle.

Contrat Markdown, préservation des placeholders, cohérence des ancres de
titres, addenda pour le mode news et les écritures non latines. Le texte des
prompts est un contrat mesuré : chaque règle a été ajoutée après un échec
observé, et n'est pas reformulée sans contre-épreuve.
"""

from .markdown import (
    _LANG_SCRIPT_NAMES,
)
from .news import _build_news_addendum


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
