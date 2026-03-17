#!/usr/bin/env python3

import os
import argparse
import time
import re
import glob

from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from mistralai import Mistral
import google.generativeai as genai

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
DEFAULT_MODEL_OPENAI = "gpt-5.4"
DEFAULT_MODEL_MISTRAL = "mistral-large-latest"
DEFAULT_MODEL_CLAUDE = "claude-sonnet-4-5-20250929"
DEFAULT_MODEL_GEMINI = "gemini-3.1-pro-preview"

# Modèles économiques (--eco)
ECO_MODEL_OPENAI = "gpt-5.4-mini"
ECO_MODEL_MISTRAL = "mistral-small-latest"
ECO_MODEL_CLAUDE = "claude-haiku-4-5-20251001"
ECO_MODEL_GEMINI = "gemini-3-flash-preview"

# Limite de tokens par défaut pour les modèles non listés
DEFAULT_TOKEN_LIMIT = 128000

DEFAULT_SOURCE_LANG = "fr"
DEFAULT_TARGET_LANG = "en"
DEFAULT_SOURCE_DIR = "content/posts"
DEFAULT_TARGET_DIR = "traductions_en"
MODEL_TOKEN_LIMITS = {
    # OpenAI GPT-5.4 series (mars 2026)
    "gpt-5.4": 400000,
    "gpt-5.4-mini": 400000,
    "gpt-5.4-nano": 400000,
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
    "gemini-3-pro-preview": 1000000,
    "gemini-3-flash-preview": 1000000,
    "gemini-2.5-pro": 1000000,
    "gemini-2.5-flash": 1000000,
    "gemini-2.0-flash": 1000000,
    "gemini-2.0-pro-exp-02-05": 1000000,
}


def segment_text(text, max_length):
    """
    Divise un texte Markdown en segments ne dépassant pas la longueur maximale spécifiée,
    en essayant de conserver des points de coupure naturels.

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

        # Recherche de points de coupure naturels (fin de phrase, fin de paragraphe, fin de titre)
        last_good_break = max(
            segment.rfind(". "), segment.rfind("\n\n"), segment.rfind("\n#")
        )
        if last_good_break != -1:
            next_index = last_good_break + 1

        segments.append(text[:next_index])
        text = text[next_index:]

    return segments


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
                    f"Translate from {args.source_lang} to {args.target_lang}. "
                    "IMPORTANT RULES: "
                    "1) In YAML front matter (between ---): translate 'title' and 'description' values, "
                    f"change 'locale' to '{args.target_lang}'. Use double quotes for strings with apostrophes. "
                    "2) For Markdown links [text](url): translate link text, keep URL unchanged. "
                    "3) Do NOT modify: URLs, image paths, code blocks (including comments inside code). "
                    "4) Do NOT add translator notes, comments, or explanations. "
                    "5) Keep template variables like {variable} exactly as they are (inside backticks if present). "
                    "Preserve Markdown structure. Output ONLY the translation, nothing else."
                )

            # Ajout des instructions news si --news actif
            if not is_translation_note and args.news:
                target_flag = LANG_FLAGS.get(args.target_lang, "")
                if args.target_lang == "en":
                    news_rules = (
                        "\n\nNEWS CITATION RULES (CRITICAL — follow exactly): "
                        "- Placeholders like #NEWSQUOTE0#, #NEWSQUOTE1# etc. MUST remain EXACTLY as-is (do not translate, modify, or remove them). "
                        "- For citation blocks containing a #NEWSQUOTE placeholder followed by a flag+translation line (line starting with > and a flag emoji like 🇫🇷): "
                        "REMOVE the blank blockquote line (>) and the entire flag+translation line. "
                        "Keep ONLY the #NEWSQUOTE placeholder and the attribution line (> — [...](...)). "
                        "- Result format:\n#NEWSQUOTEn#\n> — [attribution text translated](url unchanged)"
                    )
                else:
                    news_rules = (
                        f"\n\nNEWS CITATION RULES (CRITICAL — follow exactly): "
                        f"- Placeholders like #NEWSQUOTE0#, #NEWSQUOTE1# etc. MUST remain EXACTLY as-is (do not translate, modify, or remove them). "
                        f"- For citation blocks containing a #NEWSQUOTE placeholder followed by a flag+translation line: "
                        f"Replace the flag emoji with {target_flag} and translate the italic text COMPLETELY to {args.target_lang}. "
                        f"COMPLETE means: same number of sentences, all concepts included, no truncation or summarization. "
                        f"Translate from the meaning of the text (the placeholder represents the original English quote). "
                        f"- Result format:\n#NEWSQUOTEn#\n>\n> {target_flag} _translated text in {args.target_lang}_\n> — [attribution text translated](url unchanged)"
                    )
                news_common = (
                    "\n- Keep English tech terms unchanged: Claude, API, CLI, SDK, MCP, benchmark, token, plugin"
                    "\n- Do NOT modify these frontmatter fields: pubDate, author, canonicalSlug, tags, draft, heroVideo, heroVideoMuted, heroImage"
                )
                system_instructions += news_rules + news_common

            if use_mistral:
                # Mistral - instructions + segment dans un seul message user
                messages = [{"role": "user", "content": system_instructions + "\n\n" + segment}]
                response = client.chat.complete(model=args.model, messages=messages)
                translated_text = response.choices[0].message.content.strip()

            elif use_claude:
                # Claude - instructions + segment dans un seul message user
                messages = [{"role": "user", "content": system_instructions + "\n\n" + segment}]
                response = client.messages.create(
                    model=args.model, max_tokens=4096, messages=messages
                )
                translated_texts = [
                    block.text.strip() for block in response.content
                ]
                translated_text = " ".join(translated_texts)

            elif use_gemini:
                # Gemini - instructions + segment
                model = client.GenerativeModel(args.model)
                response = model.generate_content(system_instructions + "\n\n" + segment)
                translated_text = response.text.strip()

            else:
                # OpenAI (ChatGPT, o1, etc.)
                # FIX: Le segment n'est plus inclus dans system_instructions (évite le doublon)
                if args.model in o1_series:
                    # Modèles o1 ne supportent pas le rôle system
                    messages = [
                        {"role": "user", "content": system_instructions + "\n\n" + segment},
                    ]
                else:
                    # Modèle GPT classique: system pour instructions, user pour contenu
                    messages = [
                        {"role": "system", "content": system_instructions},
                        {"role": "user", "content": segment},
                    ]

                response = client.chat.completions.create(
                    model=args.model, messages=messages
                )
                translated_text = response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la traduction : {e}")

        translated_segments.append(translated_text)

    return " ".join(translated_segments)


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
        None. Le résultat de la traduction est écrit dans le fichier de sortie spécifié.
        En cas d'échec, un message est imprimé pour indiquer une erreur et suggérer de relancer le traitement.
    """

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
            return

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
            # Pattern: > "EN quote" \n > \n > FLAG _translation_ \n > — [@account](url)
            citation_regex = re.compile(
                r'(^> ".+?")[ \t]*\n'             # Groupe 1: citation EN (entre guillemets)
                r'>[ \t]*\n'                        # ligne blockquote vide
                r'(^> .+_)[ \t]*\n'                # Groupe 2: drapeau + traduction italique
                r'(^> — \[.+?\]\(.+?\))[ \t]*$',   # Groupe 3: ligne d'attribution
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
                return f"#NEWSQUOTE{idx}#\n>\n{match.group(2)}\n{match.group(3)}"

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
                placeholder = f"#NEWSQUOTE{idx}#"
                if placeholder not in translated_content:
                    print(f"  ⚠ VALIDATION: Placeholder {placeholder} manquant dans la traduction (le LLM l'a supprimé)")

        # 4) Restaurer les citations EN news
        for idx, quote in enumerate(original_quotes):
            translated_content = translated_content.replace(f"#NEWSQUOTE{idx}#", quote)

        # 5) Validation post-restauration des citations news
        if args.news and original_quotes:
            for url in attribution_urls:
                if url not in translated_content:
                    print(f"  ⚠ VALIDATION: URL d'attribution '{url}' manquante dans la traduction")
            if args.target_lang == "en":
                for lang_code, flag in LANG_FLAGS.items():
                    if lang_code != "en" and flag in translated_content:
                        print(f"  ⚠ VALIDATION: Drapeau {flag} ({lang_code}) trouvé dans la traduction EN (devrait être absent)")
                        break
            else:
                target_flag = LANG_FLAGS.get(args.target_lang)
                if target_flag:
                    flag_count = translated_content.count(target_flag)
                    expected = len(original_quotes)
                    if flag_count != expected:
                        print(f"  ⚠ VALIDATION: Drapeau {target_flag} trouvé {flag_count} fois (attendu: {expected})")

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
            return
        with open(clean_output_path, "w", encoding="utf-8") as f:
            f.write(translated_content)

        end_time = time.time()
        print(
            f"Fichier '{relative_file_path}' traduit en {end_time - start_time:.2f} secondes et enregistré sous : {relative_output_path}"
        )
    except IOError as e:
        print(f"Erreur lors du traitement du fichier '{relative_file_path}': {e}")
    except Exception as e:
        print(
            f"Une erreur inattendue est survenue lors de la traduction du fichier '{relative_file_path}': {e}\n"
            "Veuillez relancer le traitement pour ce fichier."
        )


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
        None
    """

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
                # Pattern de nommage selon les options
                if args.keep_filename:
                    # Conserver le nom et l'extension originaux
                    output_file = file
                elif args.include_model:
                    output_file = f"{base}-{args.target_lang}-{args.model}.md"
                else:
                    output_file = f"{base}-{args.target_lang}.md"
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, output_file)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Vérification si une traduction existe déjà
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
                    translate_markdown_file(
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
                    print(f"Fichier '{file}' traité.")
                elif not force:
                    print(
                        f"La traduction de '{file}' existe déjà, aucune action effectuée."
                    )


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
        api_key = os.getenv("GOOGLE_API_KEY", DEFAULT_GEMINI_API_KEY)
        if not api_key:
            raise ValueError("Clé API Gemini non spécifiée.")
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
            # Conserver le nom et l'extension originaux
            output_file = os.path.basename(args.file)
        else:
            base = os.path.splitext(os.path.basename(args.file))[0]
            if args.include_model:
                output_file = f"{base}-{args.target_lang}-{args.model}.md"
            else:
                output_file = f"{base}-{args.target_lang}.md"
        output_path = os.path.join(args.target_dir, output_file)
        translate_markdown_file(
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
    else:
        # Traduction d'un répertoire
        translate_directory(
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

    if args.use_mistral or args.use_claude:
        try:
            del client
        except TypeError:
            pass


if __name__ == "__main__":
    main()
