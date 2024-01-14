Here is the content of the README in Markdown for your translation script:

# Markdown Translator with OpenAI

This project is a Python script that uses the OpenAI API to translate Markdown files from a source language to a target language.
More information available at [Traduction IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).

## Prerequisites

To use this script, you will need:

- Python 3.6 or higher
- An OpenAI account with an API key

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use this script, you first need to set your OpenAI API key as an environmental variable:

```bash
export OPENAI_API_KEY='votre-clé-api'
```


Then, you can execute the script using the following command:

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible'
```

You can also specify the model to use, the source language, and the target language:

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
```

## Usage Examples

```bash
################################################
# Demande de traduction à l'IA vers l'espagnol #
################################################
jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
Traitement du fichier : content/posts/ia/stable-difusion-aws-ec2.md
Traduction terminée en 33.19 secondes.
Fichier 'stable-difusion-aws-ec2.md' traité.
Traitement du fichier : content/posts/ia/poc-openai-api-gpt4.md
Traduction terminée en 25.24 secondes.
Fichier 'poc-openai-api-gpt4.md' traité.
Traitement du fichier : content/posts/ia/poc-mistral-ai-mixtral.md
Traduction terminée en 58.78 secondes.
Fichier 'poc-mistral-ai-mixtral.md' traité.
Traitement du fichier : content/posts/raspberry-pi/installation-de-kubernetes-sur-raspberry-pi-via-ansible.md
Traduction terminée en 17.64 secondes.
Fichier 'installation-de-kubernetes-sur-raspberry-pi-via-ansible.md' traité.
Traitement du fichier : content/posts/raspberry-pi/installation-de-docker-sur-raspberry-pi-via-ansible.md
Traduction terminée en 19.60 secondes.
Fichier 'installation-de-docker-sur-raspberry-pi-via-ansible.md' traité.
Traitement du fichier : content/posts/raspberry-pi/initialisation-auto-de-raspbian-sur-raspberry-pi.md
Traduction terminée en 37.12 secondes.
Fichier 'initialisation-auto-de-raspbian-sur-raspberry-pi.md' traité.
Traitement du fichier : content/posts/blog/nouveau-theme-logo.md
Traduction terminée en 18.91 secondes.
Fichier 'nouveau-theme-logo.md' traité.
Traitement du fichier : content/posts/infrastructure/infrastruture-as-code-serverless-ha-jls42-org.md
Traduction terminée en 30.73 secondes.
Fichier 'infrastruture-as-code-serverless-ha-jls42-org.md' traité.
Traitement du fichier : content/mentions/mentions-legales.md
Traduction terminée en 13.14 secondes.
Fichier 'mentions-legales.md' traité.
Traitement du fichier : content/about/a-propos-du-blog-jls42.md
Traduction terminée en 11.24 secondes.
Fichier 'a-propos-du-blog-jls42.md' traité.
```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the [LICENSE](LICENSE) file for more details.

**This document was translated from the French version of the blog by the gpt-4-1106-preview model.**

