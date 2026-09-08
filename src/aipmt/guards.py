"""Gardes de sortie : une traduction qui ressemble à la source est un échec.

Détection de langue déterministe, extraits source repris verbatim, ratio de
longueur anormal, écriture cible absente sur un alphabet non latin. Trois
gardes lèvent `RuntimeError`, et le pipeline décide alors d'un second essai ;
le signal d'écriture cible, lui, court-circuite la détection de langue. La
graine de `langdetect` est fixée ici, à l'import, parce que ce module est le
seul à l'appeler.
"""

import re
import sys

from langdetect import DetectorFactory, LangDetectException, detect_langs

from .markdown import (
    _BLOCKQUOTE_PREFIX,
    _EMPTY_BLOCKQUOTE_LINE,
    _HTML_TAG_REGEX,
    _INLINE_MD_PREFIX,
    _LANG_SCRIPT_RANGES,
    _MARKDOWN_LINK,
    _NEWSQUOTE_PLACEHOLDER_REGEX,
    _STRUCTURAL_LINE,
    _URL_OR_PLACEHOLDER,
)

# Détection de langue déterministe (évite les variations entre runs sur des textes courts)
DetectorFactory.seed = 0


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
