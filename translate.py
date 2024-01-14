#!/usr/bin/env python3

import os
import argparse
import time
from openai import OpenAI
import re

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

# Fonction de traduction
def translate_with_openai(text, client, args):
    """
    Traduit le texte donné du langage source au langage cible en utilisant l'API OpenAI.
    
    Args:
        text (str) : Le texte à traduire.
        client : L'objet client OpenAI.
        args : Les arguments contenant les informations sur le langage source, le langage cible et le modèle.
        
    Returns:
        str : Le texte traduit.
    """
    # Détecter et stocker les blocs de code
    code_blocks = re.findall(r'(^```[a-zA-Z]*\n.*?\n^```)', text, flags=re.MULTILINE | re.DOTALL)
    placeholders = [f"#CODEBLOCK{index}#" for index, _ in enumerate(code_blocks)]
    
    # Remplacer les blocs de code par des placeholders
    for placeholder, code_block in zip(placeholders, code_blocks):
        text = text.replace(code_block, placeholder)
    
    # Création du message pour l'API
    messages = [
        {"role": "system", "content": f"Translate the following text from {args.source_lang} to {args.target_lang}, ensuring that elements such as URLs, image paths, and code blocks (delimited by ```) are not translated. Leave these elements unchanged."},
        {"role": "user", "content": text}
    ]
    
    # Envoi de la demande de traduction
    response = client.chat.completions.create(
        model=args.model,
        messages=messages
    )
    
    # Obtenir le texte traduit et remplacer les placeholders par les blocs de code originaux
    translated_text = response.choices[0].message.content.strip()
    for placeholder, code_block in zip(placeholders, code_blocks):
        translated_text = translated_text.replace(placeholder, code_block)

    return translated_text

def add_translation_note(client, args):
    """
    Ajoute une note de traduction à un document.

    Args:
        client : Le client de traduction.
        args : Arguments supplémentaires.

    Returns:
        La note de traduction formatée.
    """
    # Note de traduction en français
    translation_note_fr = "Ce document a été traduit de la version française du blog par le modèle "
    # Traduire la note en langue cible
    translated_note = translate_with_openai(translation_note_fr + args.model, client, args)
    # Formatage de la note de traduction
    return f"\n\n**{translated_note}**\n\n"

# Traitement des fichiers Markdown
def translate_markdown_file(file_path, output_path, client, args):
    """
    Traduit le contenu d'un fichier markdown en utilisant l'API de traduction OpenAI et écrit le contenu traduit dans un nouveau fichier.

    Args:
        file_path (str): Chemin vers le fichier markdown d'entrée.
        output_path (str): Chemin vers le fichier de sortie où le contenu traduit sera écrit.
        client: Client de traduction OpenAI.
        args: Arguments supplémentaires pour le processus de traduction.

    Returns:
        None
    """
    print(f"Traitement du fichier : {file_path}")
    start_time = time.time()

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    translated_content = translate_with_openai(content, client, args)
    
    # Ajouter la note de traduction à la fin du contenu traduit
    translation_note = add_translation_note(client, args)
    translated_content_with_note = translated_content + translation_note

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content_with_note)

    end_time = time.time()
    print(f"Traduction terminée en {end_time - start_time:.2f} secondes.")

def translate_directory(input_dir, output_dir, client, args):
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
                    translate_markdown_file(file_path, output_path, client, args)
                    print(f"Fichier '{file}' traité.")


def main():
    """
    Fonction principale pour traduire les fichiers Markdown.

    Args:
        --source_dir (str): Répertoire source contenant les fichiers Markdown.
        --target_dir (str): Répertoire cible pour sauvegarder les traductions.
        --model (str): Modèle GPT à utiliser.
        --target_lang (str): Langue cible pour la traduction.
        --source_lang (str): Langue source pour la traduction.
    """
    parser = argparse.ArgumentParser(description="Traduit les fichiers Markdown.")
    parser.add_argument('--source_dir', type=str, default=DEFAULT_SOURCE_DIR, help='Répertoire source contenant les fichiers Markdown')
    parser.add_argument('--target_dir', type=str, default=DEFAULT_TARGET_DIR, help='Répertoire cible pour sauvegarder les traductions')
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL, help='Modèle GPT à utiliser')
    parser.add_argument('--target_lang', type=str, default=DEFAULT_TARGET_LANG, help='Langue cible pour la traduction')
    parser.add_argument('--source_lang', type=str, default=DEFAULT_SOURCE_LANG, help='Langue source pour la traduction')

    args = parser.parse_args()

    openai_api_key = os.getenv('OPENAI_API_KEY', DEFAULT_API_KEY)
    with OpenAI(api_key=openai_api_key) as client:
        translate_directory(args.source_dir, args.target_dir, client, args)

if __name__ == "__main__":
    main()
