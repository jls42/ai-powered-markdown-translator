# Traducteur de Markdown AI-Powered avec OpenAI et Mistral AI

Ce projet est un script Python avancé qui utilise l'API OpenAI ou l'API Mistral AI pour traduire des fichiers Markdown d'une langue source vers une langue cible. Il est conçu pour être flexible et facile à utiliser, offrant des options supplémentaires telles que l'ajout d'une note de traduction et le support de plusieurs langues et modèles de traduction.

Pour une démonstration et des explications détaillées, visitez [jls42.org](https://jls42.org/) ou en version traduite : [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_en/) et [jls42.org 中文中文](https://jls42.org/traductions_zh/).

## Caractéristiques Principales

- **Traduction AI-Powered**: Utilisez les dernières technologies d'IA pour la traduction de vos documents.
- **Support Multilingue**: Traduisez vos documents dans plusieurs langues avec support pour différents modèles de langage.
- **Segmentation Intelligente**: Gérez efficacement les textes longs grâce à une segmentation automatisée.
- **Note de Traduction**: Ajoutez automatiquement une note de traduction pour informer les lecteurs sur le processus utilisé.
- **Flexible et Extensible**: Le code est structuré pour permettre une facilité d'ajout de nouvelles fonctionnalités.

## Prérequis

- Python 3.6 ou version ultérieure.
- Une clé API valide pour OpenAI ou Mistral AI.

## Installation

1. Clonez le dépôt Git :
   ```
   git clone https://github.com/votre-repertoire/translate-markdown.git
   ```
2. Installez les dépendances nécessaires :
   ```
   pip install -r requirements.txt
   ```

## Configuration

Avant de lancer le script, configurez votre environnement :

- **OpenAI** : Définissez votre clé API OpenAI comme variable d'environnement :
  ```
  export OPENAI_API_KEY='votre-clé-api-openai'
  ```
- **Mistral AI** : Définissez votre clé API Mistral AI comme variable d'environnement :
  ```
  export MISTRAL_API_KEY='votre-clé-api-mistral'
  ```

## Utilisation

Pour traduire des fichiers Markdown :

- **Avec OpenAI** :
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **Avec Mistral AI** (et option de note de traduction) :
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### Options Communes

- Spécifiez le modèle, la langue source, et la langue cible :
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## Exemples d'usage

- Exemple de demande de traduction en espagnol :
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## Licence

Ce projet est sous licence GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
