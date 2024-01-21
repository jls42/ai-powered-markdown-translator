# Traductores de Markdown impulsados por IA con OpenAI y Mistral AI

Este proyecto es un script avanzado de Python que utiliza la API de OpenAI o la API de Mistral AI para traducir archivos Markdown de un idioma fuente a un idioma objetivo. Está diseñado para ser flexible y fácil de usar, ofreciendo opciones adicionales como la adición de una nota de traducción y el soporte de varios idiomas y modelos de traducción.

Para una demostración y explicaciones detalladas, visite [Traducción IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/) o en versión traducida: [English](/traductions_en/), [Español](/traductions_en/) y [中文中文](/traductions_zh/).

## Características Principales

- **Traducción impulsada por IA**: Utilice las últimas tecnologías de IA para la traducción de sus documentos.
- **Soporte Multilingüe**: Traduzca sus documentos a varios idiomas con soporte para diferentes modelos de idioma.
- **Segmentación Inteligente**: Administre eficazmente los textos largos gracias a una segmentación automatizada.
- **Nota de Traducción**: Agregue automáticamente una nota de traducción para informar a los lectores sobre el proceso utilizado.
- **Flexible y Extensible**: El código está estructurado para permitir una fácil adición de nuevas funciones.

## Requisitos Previos

- Python 3.6 o versión posterior.
- Una clave API válida para OpenAI o Mistral AI.

## Instalación

1. Clone el repositorio Git:
   ```
   git clone https://github.com/tu-directorio/translate-markdown.git
   ```
2. Instale las dependencias necesarias:
   ```
   pip install -r requirements.txt
   ```

## Configuración

Antes de ejecutar el script, configure su entorno:

- **OpenAI**: Defina su clave API de OpenAI como variable de entorno:
  ```
  export OPENAI_API_KEY='tu-clave-api-openai'
  ```
- **Mistral AI**: Defina su clave API de Mistral AI como variable de entorno:
  ```
  export MISTRAL_API_KEY='tu-clave-api-mistral'
  ```

## Uso

Para traducir archivos Markdown:

- **Con OpenAI**:
  ```
  python translate.py --source_dir 'ruta/fuente' --target_dir 'ruta/objetivo'
  ```
- **Con Mistral AI** (y opción de nota de traducción):
  ```
  python translate.py --use_mistral --source_dir 'ruta/fuente' --target_dir 'ruta/objetivo' --model 'mistral-small' --add_translation_note
  ```

### Opciones Comunes

- Especifique el modelo, el idioma fuente y el idioma objetivo:
  ```
  python translate.py --source_dir 'ruta/fuente' --target_dir 'ruta/objetivo' --model 'gpt-4-1106-preview' --source_lang 'es' --target_lang 'en'
  ```

## Ejemplos de Uso

- Ejemplo de solicitud de traducción al español:
  ```
  python translate.py --source_dir contenido/ --target_dir contenido/traducciones\_es --target\_lang es
  ```

## Licencia

Este proyecto está bajo licencia GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

**Este documento ha sido traducido desde la versión fr por el modelo mistral-medium.**

