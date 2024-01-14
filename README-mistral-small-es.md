'# Traductor de Markdown con OpenAI y Mistral AI

Este proyecto es un script de Python que utiliza la API de OpenAI o la API de Mistral AI para traducir archivos Markdown de un idioma fuente a un idioma objetivo.
Más información en [Traducción IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).  

## Prerequisitos

Para usar este script, necesitarás de:

- Python 3.6 o superior
- Una cuenta de OpenAI con una clave API o una cuenta de Mistral AI con una clave API

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias usando pip:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Con OpenAI

Para usar este script con OpenAI, primero debes definir tu clave API de OpenAI como variable de entorno:

   ```bash
   export OPENAI_API_KEY='tu-clave-api'
   ```

Después, puedes ejecutar el script usando el siguiente comando:

   ```bash
   python translate.py --source_dir 'ruta/hacia/tu/carpeta/fuente' --target_dir 'ruta/hacia/tu/carpeta/objetivo'
   ```

### Con Mistral AI

Para usar este script con Mistral AI, primero debes definir tu clave API de Mistral AI como variable de entorno:

   ```bash
   export MISTRAL_API_KEY='tu-clave-api-mistral'
   ```

Luego, ejecuta el script con la opción `--use_mistral`:

**"Este documento ha sido traducido de la versión francesa del blog por el modelo mistral-small"

Please note that the URLs, image paths, and code blocks, if any, should not be translated and should remain as they are.**

