"""Protection et restauration des fragments qui ne se traduisent pas.

Blocs de code, code en ligne, URL, ancres de titres, labels de références :
chacun est remplacé par un placeholder avant l'appel au modèle et restauré
après, avec une validation d'intégrité entre les deux — un placeholder perdu ou
altéré par le modèle est une erreur, jamais rattrapée en silence.
"""

import re
import unicodedata

from .markdown import (
    _HTML_TAG_REGEX,
)

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


# HTML anchor reference `<a href="#X">...</a>`. Capture le `href="#X"` complet
# (avec quote = guillemet ou apostrophe) pour pouvoir reconstruire la même
# syntaxe en restoration. cf. caveman README qui utilise des `<a href="#install">`
# au lieu des `[link](#install)` markdown.
_HTML_HREF_ANCHOR_REGEX = re.compile(r'href=(["\'])#([^"\'#?]+)\1')


# `[ \t]+` (non `\s+`) : whitespace intra-ligne, strictement non-ambigu.
# `[^\n]+` greedy borné par le `\n` final, pas de backtracking polynomial.
# `.strip()` côté Python pour trimmer les espaces finaux capturés.
# fmt: off
_HEADING_REGEX = re.compile(r"^(#{1,6})[ \t]+([^\n]+)$", re.MULTILINE)  # NOSONAR S5852


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


def _classify_anchor_target(fragment, explicit_targets, heading_slugs, html_quote=None):
    """Détermine le type d'un fragment d'anchor : terraform (matche `<a name>`)
    ou heading (matche un slug source). Retourne `None` si aucun match (l'anchor
    n'est pas protégé pour éviter les faux positifs sur des liens externes)."""
    is_terraform = fragment in explicit_targets
    if is_terraform:
        kind = "terraform_html" if html_quote else "terraform"
    elif fragment in heading_slugs:
        kind = "heading_html" if html_quote else "heading"
    else:
        return None
    meta = {"type": kind, "slug": fragment}
    if html_quote is not None:
        meta["quote"] = html_quote
    return meta


def _collect_md_anchor_links(content, explicit_targets, heading_slugs):
    """Anchors `(#X)` Markdown : déséchape les `\\_` / `\\-` avant matching."""
    out = []
    for m in _ANCHOR_LINK_REGEX.finditer(content):
        fragment = m.group(1).replace(r"\_", "_").replace(r"\-", "-")
        meta = _classify_anchor_target(fragment, explicit_targets, heading_slugs)
        if meta is not None:
            out.append((m.group(0), meta))
    return out


def _collect_html_href_anchors(content, explicit_targets, heading_slugs):
    """Anchors `href="#X"` HTML : capture le quote pour restoration syntaxique."""
    out = []
    for m in _HTML_HREF_ANCHOR_REGEX.finditer(content):
        meta = _classify_anchor_target(
            m.group(2), explicit_targets, heading_slugs, html_quote=m.group(1)
        )
        if meta is not None:
            out.append((m.group(0), meta))
    return out


def _protect_anchors(content):
    explicit_targets = {m.group(1) for m in _ANCHOR_NAME_REGEX.finditer(content)}
    heading_slugs = set(_extract_heading_slugs(content))
    anchors = []
    metadata = []

    # 1. <a name="X"></a> (toujours protégés byte-identical).
    for m in _ANCHOR_NAME_REGEX.finditer(content):
        anchors.append(m.group(0))
        metadata.append({"type": "explicit", "slug": None})

    # 2. (#X) Markdown : terraform OU heading-derived.
    for anchor, meta in _collect_md_anchor_links(content, explicit_targets, heading_slugs):
        anchors.append(anchor)
        metadata.append(meta)

    # 3. `href="#X"` HTML : terraform OU heading-derived (avec quote pour restoration).
    for anchor, meta in _collect_html_href_anchors(content, explicit_targets, heading_slugs):
        anchors.append(anchor)
        metadata.append(meta)

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
            new_anchor = f"(#{slug_map[meta['slug']]})"
            translated_content = translated_content.replace(placeholder, new_anchor)
        elif meta["type"] == "heading_html" and meta["slug"] in slug_map:
            new_anchor = f"href={meta['quote']}#{slug_map[meta['slug']]}{meta['quote']}"
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


def _restore_code(
    translated_content, inline_codes, inline_placeholders, code_blocks, block_placeholders
):
    # Restore inline first, then fenced (matches extraction order).
    for placeholder, inline in zip(inline_placeholders, inline_codes, strict=False):
        translated_content = translated_content.replace(placeholder, inline)
    for placeholder, block in zip(block_placeholders, code_blocks, strict=False):
        translated_content = translated_content.replace(placeholder, block)
    return translated_content


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
