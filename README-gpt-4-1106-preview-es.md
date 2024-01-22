# Traductor de Markdown con IA de OpenAI y Mistral AI

Este proyecto es un script de Python avanzado que utiliza la API de OpenAI o la API de Mistral AI para traducir archivos Markdown de un idioma de origen a un idioma objetivo. Está diseñado para ser flexible y fácil de usar, ofreciendo opciones adicionales como la inclusión de una nota de traducción y soporte para varios idiomas y modelos de traducción.

Para una demostración y explicaciones detalladas, visite [jls42.org](https://jls42.org/) o en versión traducida: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_en/) y [jls42.org 中文中文](https://jls42.org/traductions_zh/).

## Características Principales

- **Traducción potenciada por IA**: Utilice las últimas tecnologías de IA para la traducción de sus documentos.
- **Soporte Multilingüe**: Traduzca sus documentos a varios idiomas con soporte para diferentes modelos de lenguaje.
- **Segmentación Inteligente**: Maneje textos largos de manera eficiente gracias a una segmentación automatizada.
- **Nota de Traducción**: Añada automáticamente una nota de traducción para informar a los lectores sobre el proceso utilizado.
- **Flexible y Extensible**: El código está estructurado para permitir la facilidad de agregar nuevas características.

## Requisitos Previos

- Python 3.6 o una versión posterior.
- Una clave API válida para OpenAI o Mistral AI.

## Instalación

1. Clone el repositorio Git:
   ```
   git clone https://github.com/votre-repertoire/translate-markdown.git
   ```
2. Instale las dependencias necesarias:
   ```
   pip install -r requirements.txt
   ```

## Configuración

Antes de ejecutar el script, configure su entorno:

- **OpenAI**: Defina su clave API de OpenAI como una variable de entorno:
  ```
  export OPENAI_API_KEY='votre-clé-api-openai'
  ```
- **Mistral AI**: Defina su clave API de Mistral AI como una variable de entorno:
  ```
  export MISTRAL_API_KEY='votre-clé-api-mistral'
  ```

## Uso

Para traducir archivos Markdown:

- **Con OpenAI**:
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **Con Mistral AI** (y la opción de nota de traducción):
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### Opciones Comunes

- Especifique el modelo, el idioma de origen y el idioma objetivo:
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## Ejemplos de Uso

- Ejemplo de solicitud de traducción al español:
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

**Este documento ha sido traducido de la versión fr por el modelo gpt-4-1106-preview.**

