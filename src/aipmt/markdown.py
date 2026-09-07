"""Lexique Markdown partagé : expressions régulières et tables d'écritures.

Ce module n'a aucune dépendance interne et n'en aura jamais : c'est le socle
que la segmentation, les gardes de sortie, la protection des placeholders et
le mode `--news` consultent tous. Il porte aussi les plages Unicode des
écritures non latines et la forme des placeholders de citation (`news_quote_
placeholder`), parce que plusieurs modules doivent reconnaître exactement le
même motif.
"""

import re


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
