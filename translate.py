#!/usr/bin/env python3

import os
import argparse
import time
from openai import OpenAI
import re
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import glob


EXCLUDE_PATTERNS = ["traductions_"]

# Initialisation de la configuration avec les valeurs par défaut
DEFAULT_OPENAI_API_KEY = "votre-clé-api-openai-par-défaut"
DEFAULT_MISTRAL_API_KEY = "votre-clé-api-mistral-par-défaut"
DEFAULT_MODEL_OPENAI = "gpt-4-1106-preview"
DEFAULT_MODEL_MISTRAL = "mistral-medium"
DEFAULT_SOURCE_LANG = "fr"
DEFAULT_TARGET_LANG = "en"
DEFAULT_SOURCE_DIR = "content/posts"
DEFAULT_TARGET_DIR = "traductions_en"
MODEL_TOKEN_LIMITS = {
    "gpt-4-turbo-preview": 4096,
    "gpt-4-1106-preview": 4096,
    "gpt-4-vision-preview": 4096,
    "gpt-4": 8192,
    "gpt-4-32k": 32768,
    "gpt-4-0613": 8192,
    "gpt-4-32k-0613": 32768,
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


def translate(text, client, args, use_mistral=False, is_translation_note=False):
    """
    Traduit un texte en utilisant les services de traduction d'OpenAI ou Mistral AI.
    Cette fonction segmente d'abord le texte pour s'assurer qu'il respecte la limite de tokens du modèle.
    Elle utilise un argument optionnel 'is_translation_note' pour gérer différemment les notes de traduction.

    Args:
        text (str): Texte à traduire.
        client: Client de l'API de traduction (OpenAI ou Mistral AI).
        args: Arguments contenant les informations de configuration.
        use_mistral (bool): Indique si l'API Mistral AI doit être utilisée (True) ou l'API OpenAI (False).
        is_translation_note (bool): Indique si le texte est une note de traduction, ce qui nécessite un traitement spécial.

    Returns:
        str: Texte traduit.
    """
    model_limit = MODEL_TOKEN_LIMITS.get(args.model, 4096)

    segments = segment_text(text, model_limit)
    translated_segments = []

    for segment in segments:
        try:
            prompt_message = ""
            if is_translation_note:
                prompt_message = f"Translate this exact sentence to {args.target_lang}, without any additions or explanations: '{segment}'"
            else:
                prompt_message = f"Please translate this text from {args.source_lang} to {args.target_lang}, and do not translate or change URLs, image paths, special characters such as dashes (---) and code blocks (delimited by ```) : {segment}"
            if use_mistral:
                messages = [ChatMessage(role="user", content=prompt_message)]
                response = client.chat(model=args.model, messages=messages)
            else:
                messages = [
                    {"role": "system", "content": prompt_message},
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
    add_translation_note=False,
    force=False,
):
    """
    Traduit un fichier Markdown en utilisant les modèles de traitement du langage naturel de OpenAI ou Mistral AI.

    Args:
        file_path (str): Chemin complet vers le fichier d'entrée.
        output_path (str): Chemin complet vers le fichier de sortie.
        client: Objet client de traduction.
        args: Arguments supplémentaires pour la traduction.
        use_mistral (bool): Indique si l'API Mistral AI doit être utilisée pour la traduction.
        add_translation_note (bool): Indique si une note de traduction doit être ajoutée.
        force (bool): Indique si la traduction doit être forcée même si une traduction existe déjà.

    Returns:
        None
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

        # Extraction des blocs de code
        # Utilisation de placeholders pour préserver les blocs de code lors de la traduction
        regex = re.compile(
            r"(?P<start>^```(?P<block_language>(\w|-)+)\n)(?P<code>.*?\n)(?P<end>```)",
            re.DOTALL | re.MULTILINE,
        )
        code_blocks = [match.group("code") for match in regex.finditer(content)]
        placeholders = [f"#CODEBLOCK{index}#" for index, _ in enumerate(code_blocks)]
        for placeholder, code_block in zip(placeholders, code_blocks):
            content = content.replace(code_block, placeholder)

        # Traduction du contenu
        translated_content = translate(content, client, args, use_mistral)

        # Restauration des blocs de code dans le contenu traduit
        for placeholder, code_block in zip(placeholders, code_blocks):
            translated_content = translated_content.replace(placeholder, code_block)

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
            f"Une erreur inattendue est survenue lors de la traduction du fichier '{relative_file_path}': {e}"
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
        if os.path.join(path, pattern) in path:
            return True
    return False


def translate_directory(
    input_dir, output_dir, client, args, use_mistral, add_translation_note, force
):
    """
    Traduit tous les fichiers markdown dans le répertoire d'entrée et ses sous-répertoires.

    Args:
        input_dir (str): Chemin vers le répertoire d'entrée.
        output_dir (str): Chemin vers le répertoire de sortie.
        client: Objet client de traduction.
        args: Arguments supplémentaires pour la traduction.
        use_mistral (bool): Indique si l'API Mistral AI doit être utilisée pour la traduction.
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
            if file.endswith(".md") and not is_excluded(file):
                file_path = os.path.join(root, file)
                base, _ = os.path.splitext(file)
                output_file = f"{base}-{args.target_lang}-{args.model}.md"  # Inversion du modèle et de la langue
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, output_file)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Vérification si une traduction existe déjà, peu importe le modèle
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
    les services de traduction de l'API OpenAI ou Mistral AI. Il prend en charge la segmentation
    des textes longs et peut également ajouter une note de traduction en fin de document.

    Arguments du script:
    --source_dir: Répertoire contenant les fichiers Markdown à traduire.
    --target_dir: Répertoire de destination pour les fichiers traduits.
    --model: Modèle de traduction GPT à utiliser.
    --target_lang: Langue cible pour la traduction.
    --source_lang: Langue source des documents.
    --use_mistral: Indicateur pour utiliser l'API Mistral AI pour la traduction.
    --add_translation_note: Indicateur pour ajouter une note de traduction au contenu traduit.
    """
    parser = argparse.ArgumentParser(description="Traduit les fichiers Markdown.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Forcer la traduction même si une traduction existe déjà",
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
        "--model", type=str, help="Modèle GPT à utiliser pour la traduction"
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
        "--add_translation_note",
        action="store_true",
        help="Ajouter une note de traduction au contenu traduit",
    )

    args = parser.parse_args()

    if not os.path.isdir(args.source_dir):
        raise ValueError(
            f"Le répertoire source spécifié n'existe pas : {args.source_dir}"
        )
    if not os.path.exists(args.target_dir):
        os.makedirs(args.target_dir)

    if args.use_mistral:
        args.model = args.model if args.model else DEFAULT_MODEL_MISTRAL
        api_key = os.getenv("MISTRAL_API_KEY", DEFAULT_MISTRAL_API_KEY)
        if not api_key:
            raise ValueError("Clé API Mistral non spécifiée.")
        client = MistralClient(api_key=api_key)  # Supprimez l'argument model_limit
    else:
        args.model = args.model if args.model else DEFAULT_MODEL_OPENAI
        openai_api_key = os.getenv("OPENAI_API_KEY", DEFAULT_OPENAI_API_KEY)
        if not openai_api_key:
            raise ValueError("Clé API OpenAI non spécifiée.")
        client = OpenAI(api_key=openai_api_key)  # Supprimez l'argument model_limit

    translate_directory(
        args.source_dir,
        args.target_dir,
        client,
        args,
        args.use_mistral,
        args.add_translation_note,
        args.force,
    )

    if args.use_mistral:
        try:
            del client
        except TypeError:
            pass


if __name__ == "__main__":
    main()
