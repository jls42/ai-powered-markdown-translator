# Traducteur de Markdown AI-Powered avec OpenAI, Mistral AI et Claude d'Anthropic

Ce projet est un script Python avancé qui utilise les API OpenAI, Mistral AI ou Claude d'Anthropic pour traduire des fichiers Markdown d'une langue source vers une langue cible. Il est conçu pour être flexible et facile à utiliser, offrant des options supplémentaires telles que l'ajout d'une note de traduction, la gestion améliorée des fichiers de sortie, la détection de fichiers existants, et le support de plusieurs langues et modèles de traduction.

Pour une démonstration et des explications détaillées, visitez [jls42.org](https://jls42.org/) ou en version traduite : [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) et [jls42.org 中文](https://jls42.org/traductions_zh/).

## Caractéristiques Principales

- **Traduction AI-Powered**: Utilisez les dernières technologies d'IA pour la traduction de vos documents avec OpenAI, Mistral AI ou Claude d'Anthropic.
- **Support Multilingue**: Traduisez vos documents dans plusieurs langues avec support pour différents modèles de langage.
- **Segmentation Intelligente**: Gérez efficacement les textes longs grâce à une segmentation automatisée.
- **Note de Traduction**: Ajoutez automatiquement une note de traduction pour informer les lecteurs sur le processus utilisé.
- **Gestion Améliorée des Fichiers de Sortie**: Vérifiez si une traduction existe déjà avant de lancer la traduction.
- **Détection de Fichiers Existants Améliorée**: Recherchez des fichiers correspondants au nom de base du fichier d'origine et à la langue cible.
- **Flexible et Extensible**: Le code est structuré pour permettre une facilité d'ajout de nouvelles fonctionnalités.

## Prérequis

- Python 3.6 ou version ultérieure.
- Une clé API valide pour OpenAI, Mistral AI ou Claude d'Anthropic.

## Installation

1. Clonez le dépôt Git :
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installez les dépendances nécessaires :
```
pip install -r requirements.txt
```

## Configuration

Configurez votre environnement en définissant les variables d'environnement pour les clés API nécessaires :

- **OpenAI** :
    ```
    export OPENAI_API_KEY='votre-clé-api-openai'
    ```
- **Mistral AI** :
    ```
    export MISTRAL_API_KEY='votre-clé-api-mistral'
    ```
- **Claude d'Anthropic** :
    ```
    export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
    ```

## Utilisation

Le script offre plusieurs options pour personnaliser le processus de traduction :

### Options Générales

- `--source_dir` : Répertoire contenant les fichiers Markdown à traduire.
- `--target_dir` : Répertoire de sortie pour les fichiers traduits.
- `--model` : Modèle de traduction GPT à utiliser. Le modèle par défaut dépend de l'API sélectionnée.
- `--source_lang` : Langue source des documents. Importante notamment pour l'ajout de notes de traduction.
- `--target_lang` : Langue cible pour la traduction. Par défaut, c'est l'anglais.
- `--force` : Forcer la traduction même si une traduction existe déjà pour le fichier.

### Options API Spécifiques

- `--use_mistral` : Utiliser l'API Mistral AI pour la traduction.
- `--use_claude` : Utiliser l'API Claude d'Anthropic pour la traduction.
- `--add_translation_note` : Ajouter une note de traduction au contenu traduit, spécifiant la méthode et les outils utilisés.

### Exemples d'Utilisation

- Traduire du français vers l'anglais avec OpenAI, en ajoutant une note de traduction :
    ```
    python translate.py --use_openai --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Traduire du français vers l'espagnol avec Mistral AI, sans note de traduction :
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Auteur

Julien LE SAUX  
Email : contact@jls42.org

## Licence

Ce projet est sous licence GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
