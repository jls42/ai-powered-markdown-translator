# Traducteur de Markdown avec OpenAI et Mistral AI

Ce projet est un script Python qui utilise l'API OpenAI ou l'API Mistral AI pour traduire des fichiers Markdown d'une langue source vers une langue cible.
Plus d'information sur [Traduction IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).  

## Prérequis

Pour utiliser ce script, vous aurez besoin de :

- Python 3.6 ou supérieur
- Un compte OpenAI avec une clé API ou un compte Mistral AI avec une clé API

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en utilisant pip :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Avec OpenAI

Pour utiliser ce script avec OpenAI, vous devez d'abord définir votre clé API OpenAI comme variable d'environnement :

   ```bash
   export OPENAI_API_KEY='votre-clé-api'
   ```

Ensuite, vous pouvez exécuter le script en utilisant la commande suivante :

   ```bash
   python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible'
   ```

### Avec Mistral AI

Pour utiliser ce script avec Mistral AI, vous devez d'abord définir votre clé API Mistral AI comme variable d'environnement :

   ```bash
   export MISTRAL_API_KEY='votre-clé-api-mistral'
   ```

Ensuite, exécutez le script avec l'option `--use_mistral` :

   ```bash
   python translate.py --use_mistral --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible' --model 'mistral-small'
   ```

### Options Communes

Vous pouvez également spécifier le modèle à utiliser, la langue source et la langue cible :

   ```bash
   python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
   ```

## Exemples d'usage

   ```bash
   ################################################
   # Demande de traduction à l'IA vers l'espagnol #
   ################################################
   jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
   Traitement du fichier : content/posts/ia/stable-difusion-aws-ec2.md
   Traduction terminée en 33.19 secondes.
   Fichier 'stable-difusion-aws-ec2.md' traité.
   # ... autres lignes de résultat ...
   ```

## Licence

Ce projet est sous licence GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Voir le fichier [LICENSE](LICENSE) pour plus de détails.