Voici le contenu du README en Markdown pour votre script de traduction :

# Traducteur de Markdown avec OpenAI

Ce projet est un script Python qui utilise l'API OpenAI pour traduire des fichiers Markdown d'une langue source vers une langue cible.
Plus d'information sur [Traduction IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).  

## Prérequis

Pour utiliser ce script, vous aurez besoin de :

- Python 3.6 ou supérieur
- Un compte OpenAI avec une clé API

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances nécessaires en utilisant pip :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour utiliser ce script, vous devez d'abord définir votre clé API OpenAI comme variable d'environnement :

```bash
export OPENAI_API_KEY='votre-clé-api'
```


En suite, vous pouvez exécuter le script en utilisant la commande suivante :

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible'
```

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

## Licence

Ce projet est sous licence GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
