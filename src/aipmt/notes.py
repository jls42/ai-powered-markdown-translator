"""Note de traduction ajoutée en fin de document (`--add_translation_note`).

Constructeurs sans I/O ni appel au modèle : la phrase descriptive, les paragraphes invariants (titre
du dépôt, lien), la découpe du front matter et la composition finale. La
traduction de la phrase elle-même passe par le pipeline, qui appelle ce module,
jamais l'inverse.
"""

import datetime
import re

# Labels CTA "Voir le projet sur GitHub" localisés par target_lang.
# Assemblés côté Python (jamais envoyés au LLM) pour préserver l'URL et le
# slug du repo. Le label texte, lui, doit suivre la langue cible — sinon il
# fuite en français dans les versions traduites du marker top.
_VIEW_PROJECT_LABELS = {
    "fr": "Voir le projet sur GitHub ↗",
    "en": "View project on GitHub ↗",
    "de": "Projekt auf GitHub ansehen ↗",
    "es": "Ver proyecto en GitHub ↗",
    "it": "Vedi progetto su GitHub ↗",
    "pt": "Ver projeto no GitHub ↗",
    "nl": "Bekijk project op GitHub ↗",
    "pl": "Zobacz projekt na GitHubie ↗",
    "sv": "Visa projekt på GitHub ↗",
    "ro": "Vezi proiectul pe GitHub ↗",
    "ar": "عرض المشروع على GitHub ↗",
    "hi": "GitHub पर प्रोजेक्ट देखें ↗",
    "ja": "GitHub でプロジェクトを見る ↗",
    "ko": "GitHub에서 프로젝트 보기 ↗",
    "zh": "在 GitHub 上查看项目 ↗",
}


def _translation_note_invariants(target_lang="fr"):
    """Parties INVARIANTES de la note de traduction (jamais envoyées au LLM).

    Le titre du repo et l'URL GitHub ne doivent JAMAIS être altérés par le
    LLM (slug, casse, backticks, scheme), donc on les assemble côté Python
    après traduction de la phrase descriptive. Voir `_append_translation_note`.

    Le label CTA du lien suit `target_lang` via `_VIEW_PROJECT_LABELS` pour
    éviter une fuite FR dans les versions traduites. Fallback `fr` si la
    langue est inconnue.
    """
    title = "**`ai-powered-markdown-translator`**"
    label = _VIEW_PROJECT_LABELS.get(target_lang, _VIEW_PROJECT_LABELS["fr"])
    link = f"[{label}](https://github.com/jls42/ai-powered-markdown-translator)"
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


def _assemble_translation_note_paragraphs(phrase, target_lang="fr"):
    """Forme canonique 3-paragraphes : titre (Python) + phrase + lien (Python).

    Appelée à la fois par `_build_translation_note_source` (vue source pour
    documentation/tests) et par `_append_translation_note` (vue runtime avec
    la phrase déjà traduite). Garantit que les deux paths produisent un bloc
    structurellement identique. `target_lang` propagé pour localiser le label
    CTA du lien (cf. `_VIEW_PROJECT_LABELS`).
    """
    title, link = _translation_note_invariants(target_lang)
    return title + "\n\n" + phrase + "\n\n" + link


def _build_translation_note_source(args):
    """Émet la note source non traduite en 3 paragraphes (style "GitHub repo embed card") :

    1. Titre repo (nom du projet en code inline + gras) — invariant assemblé en Python.
    2. Description (phrase explicative) — seule partie traduite par le LLM.
    3. Lien CTA Markdown avec arrow visible — invariant assemblé en Python,
       label localisé selon `args.target_lang`.
    """
    return _assemble_translation_note_paragraphs(
        _build_translation_note_phrase(args), args.target_lang
    )


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
