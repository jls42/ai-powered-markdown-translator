# Traductor de Markdown Potenciado por IA con OpenAI y Mistral AI

Este proyecto es un script avanzado de Python que utiliza la API de OpenAI o la API de Mistral AI para traducir archivos Markdown de un idioma fuente a un idioma objetivo. Está diseñado para ser flexible y fácil de usar, ofreciendo opciones adicionales como la adición de una nota de traducción y el soporte de varios idiomas y modelos de traducción.

Para una demostración y explicaciones detalladas, visite [Traducción IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/) o en versión traducida: [English](/traductions_en/), [Español](/traductions_es/) y [中文中文](/traductions_zh/).

## Características Principales

- **Traducción Potenciada por IA**: Utilice las últimas tecnologías de IA para la traducción de sus documentos.
- **Soporte Multilingüe**: Traduzca sus documentos en varios idiomas con soporte para diferentes modelos de lenguaje.
- **Segmentación Inteligente**: Gestione de manera eficiente textos largos gracias a una segmentación automatizada.
- **Nota de Traducción**: Añada automáticamente una nota de traducción para informar a los lectores sobre el proceso utilizado.
- **Flexible y Extensible**: El código está estructurado para permitir una fácil adición de nuevas funcionalidades.

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

- **OpenAI**: Establezca su clave API de OpenAI como variable de entorno:
  ```
  export OPENAI_API_KEY='su-clave-api-openai'
  ```
- **Mistral AI**: Establezca su clave API de Mistral AI como variable de entorno:
  ```
  export MISTRAL_API_KEY='su-clave-api-mistral'
  ```

## Uso

Para traducir archivos Markdown:

- **Con OpenAI**:
  ```
  python translate.py --source_dir 'ruta/fuente' --target_dir 'ruta/destino'
  ```
- **Con Mistral AI** (y opción de nota de traducción):
  ```
  python translate.py --use_mistral --source_dir 'ruta/fuente' --target_dir 'ruta/destino' --model 'mistral-small' --add_translation_note
  ```

### Opciones Comunes

- Especifique el modelo, el idioma fuente y el idioma objetivo:
  ```
  python translate.py --source_dir 'ruta/fuente' --target_dir 'ruta/destino' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## Ejemplos de Uso

- Ejemplo de solicitud de traducción al español:
  ```
  python translate.py --source_dir content/ --target_dir content/traducciones_es --target_lang es
  ```

## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Vea el archivo [LICENSE](LICENSE) para más detalles.

**Este documento ha sido traducido de la versión fr por el modelo gpt-4-1106-preview.**

