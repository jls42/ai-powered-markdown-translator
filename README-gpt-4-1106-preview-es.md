# Traductor de Markdown con OpenAI y Mistral AI

Este proyecto es un script de Python que utiliza la API de OpenAI o la API de Mistral AI para traducir archivos Markdown de un idioma fuente a un idioma objetivo.
Más información en [Traducción IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).

## Prerrequisitos

Para usar este script, necesitarás:

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

Para usar este script con OpenAI, primero debes definir tu clave API de OpenAI como una variable de entorno:

   ```bash
   export OPENAI_API_KEY='tu-clave-api'
   ```

Después, puedes ejecutar el script utilizando el siguiente comando:

   ```bash
   python translate.py --source_dir 'camino/a/tu/directorio/fuente' --target_dir 'camino/a/tu/directorio/objetivo'
   ```

### Con Mistral AI

Para usar este script con Mistral AI, primero debes definir tu clave API de Mistral AI como una variable de entorno:

   ```bash
   export MISTRAL_API_KEY='tu-clave-api-mistral'
   ```

Luego, ejecuta el script con la opción `--use_mistral`:

   ```bash
   python translate.py --use_mistral --source_dir 'camino/a/tu/directorio/fuente' --target_dir 'camino/a/tu/directorio/objetivo' --model 'mistral-small'
   ```

### Opciones Comunes

También puedes especificar el modelo a usar, el idioma fuente y el idioma objetivo:

   ```bash
   python translate.py --source_dir 'camino/a/tu/directorio/fuente' --target_dir 'camino/a/tu/directorio/objetivo' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
   ```

## Ejemplos de uso

   ```bash
   ################################################
   # Solicitud de traducción a IA hacia el español #
   ################################################
   jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traducciones_es --target_lang es
   Procesando archivo: content/posts/ia/stable-difusion-aws-ec2.md
   Traducción finalizada en 33.19 segundos.
   Archivo 'stable-difusion-aws-ec2.md' procesado.
   # ... otras líneas de resultado ...
   ```

## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Consulta el archivo [LICENSE](LICENSE) para más detalles.

**Este documento ha sido traducido de la versión francesa del blog por el modelo gpt-4-1106-preview**

