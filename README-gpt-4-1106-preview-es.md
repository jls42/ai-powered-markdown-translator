Aquí está el contenido del README en Markdown para su script de traducción:

# Traductor de Markdown con OpenAI

Este proyecto es un script de Python que utiliza la API de OpenAI para traducir archivos Markdown de un idioma fuente a un idioma objetivo.
Más información en [Traducción IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).

## Prerrequisitos

Para utilizar este script, necesitará:

- Python 3.6 o superior
- Una cuenta de OpenAI con una clave API

## Instalación

1. Clone este repositorio en su máquina local.
2. Instale las dependencias necesarias utilizando pip:

```bash
pip install -r requirements.txt
```

## Uso

Para usar este script, primero debe definir su clave API de OpenAI como variable de entorno:

```bash
export OPENAI_API_KEY='votre-clé-api'
```


Luego, puede ejecutar el script utilizando el siguiente comando:

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible'
```

También puede especificar el modelo a usar, el idioma fuente y el idioma objetivo:

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
```

## Ejemplos de uso

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

## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Vea el archivo [LICENSE](LICENSE) para más detalles.

**Este documento ha sido traducido de la versión francesa del blog por el modelo gpt-4-1106-preview**

