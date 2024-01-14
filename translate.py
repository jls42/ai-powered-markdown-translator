#!/usr/bin/env python3

import os
import argparse
import time
from openai import OpenAI
import re
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


# Initialisation de la configuration avec les valeurs par défaut
DEFAULT_API_KEY = 'votre-clé-api-par-défaut'
DEFAULT_MODEL = "gpt-4-1106-preview"
DEFAULT_SOURCE_LANG = 'fr'
DEFAULT_TARGET_LANG = 'en'
DEFAULT_SOURCE_DIR = 'content/posts'
DEFAULT_TARGET_DIR = 'traductions_en'

MODEL_TOKEN_LIMITS = {
    "gpt-4-1106-preview": 4096,
    "gpt-4-vision-preview": 4096,
    "gpt-4": 8192,
    "gpt-4-32k": 32768,
    "gpt-4-0613": 8192,
    "gpt-4-32k-0613": 32768
}


# Fonction de traduction adaptée pour utiliser soit OpenAI soit Mistral AI
def translate(text, client, args, use_mistral=False):
    # Détecter et stocker les blocs de code
    code_blocks = re.findall(r'(^```[a-zA-Z]*\n.*?\n^```)', text, flags=re.MULTILINE | re.DOTALL)
    placeholders = [f"#CODEBLOCK{index}#" for index, _ in enumerate(code_blocks)]

    # Remplacer les blocs de code par des placeholders
    for placeholder, code_block in zip(placeholders, code_blocks):
        text = text.replace(code_block, placeholder)

    if use_mistral:
        messages = [ChatMessage(role="user", content=f"Translate the following text from {args.source_lang} to {args.target_lang}, ensuring that elements such as URLs, image paths, and code blocks (delimited by ```) are not translated. Leave these elements unchanged. : '{text}'")]
        response = client.chat(model=args.model, messages=messages)
        translated_text = response.choices[0].message.content.strip()
    else:
        messages = [
            {"role": "system", "content": f"Translate the following text from {args.source_lang} to {args.target_lang}, ensuring that elements such as URLs, image paths, and code blocks (delimited by ```) are not translated. Leave these elements unchanged."},
            {"role": "user", "content": text}
        ]
        response = client.chat.completions.create(
            model=args.model,
            messages=messages
        )
        translated_text = response.choices[0].message.content.strip()

    # Remplacer les placeholders par les blocs de code originaux
    for placeholder, code_block in zip(placeholders, code_blocks):
        translated_text = translated_text.replace(placeholder, code_block)

    return translated_text


def add_translation_note(client, args, use_mistral):
    translation_note_fr = "Ce document a été traduit de la version française du blog par le modèle "
    translated_note = translate(translation_note_fr + args.model, client, args, use_mistral)
    return f"\n\n**{translated_note}**\n\n"


# Traitement des fichiers Markdown
def translate_markdown_file(file_path, output_path, client, args, use_mistral):
    print(f"Traitement du fichier : {file_path}")
    start_time = time.time()

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    translated_content = translate(content, client, args, use_mistral)
    
    translation_note = add_translation_note(client, args, use_mistral)
    translated_content_with_note = translated_content + translation_note

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content_with_note)

    end_time = time.time()
    print(f"Traduction terminée en {end_time - start_time:.2f} secondes.")


def translate_directory(input_dir, output_dir, client, args, use_mistral):
    """
    Traduit tous les fichiers markdown dans le répertoire d'entrée et ses sous-répertoires.

    Args:
        input_dir (str): Chemin vers le répertoire d'entrée.
        output_dir (str): Chemin vers le répertoire de sortie.
        client: Objet client de traduction.
        args: Arguments supplémentaires pour la traduction.

    Returns:
        None
    """
    for root, dirs, files in os.walk(input_dir, topdown=True):
        # Exclure les dossiers qui commencent par "traductions_"
        dirs[:] = [d for d in dirs if not d.startswith("traductions_")]

        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                base, _ = os.path.splitext(file)
                # Ajouter le nom du modèle utilisé dans le nom du fichier de sortie
                output_file = f"{base}-{args.model}-{args.target_lang}.md"
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path, output_file)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                if not os.path.exists(output_path):
                    translate_markdown_file(file_path, output_path, client, args, use_mistral)
                    print(f"Fichier '{file}' traité.")


def main():
    parser = argparse.ArgumentParser(description="Traduit les fichiers Markdown.")
    parser.add_argument('--source_dir', type=str, default=DEFAULT_SOURCE_DIR, help='Répertoire source contenant les fichiers Markdown')
    parser.add_argument('--target_dir', type=str, default=DEFAULT_TARGET_DIR, help='Répertoire cible pour sauvegarder les traductions')
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL, help='Modèle GPT à utiliser')
    parser.add_argument('--target_lang', type=str, default=DEFAULT_TARGET_LANG, help='Langue cible pour la traduction')
    parser.add_argument('--source_lang', type=str, default=DEFAULT_SOURCE_LANG, help='Langue source pour la traduction')
    parser.add_argument('--use_mistral', action='store_true', help="Utiliser l'API Mistral AI pour la traduction")

    args = parser.parse_args()

    if args.use_mistral:
        api_key = os.getenv('MISTRAL_API_KEY', 'votre-clé-api-mistral')
        client = MistralClient(api_key=api_key)
    else:
        openai_api_key = os.getenv('OPENAI_API_KEY', DEFAULT_API_KEY)
        client = OpenAI(api_key=openai_api_key)

    translate_directory(args.source_dir, args.target_dir, client, args, args.use_mistral)

    if args.use_mistral:
        try:
            del client
        except TypeError:
            pass

if __name__ == "__main__":
    main()