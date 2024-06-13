# Traductor de Markdown con IA de OpenAI, Mistral AI y Claude de Anthropic

Este proyecto es un guion de Python avanzado que utiliza las API de OpenAI, Mistral AI o Claude de Anthropic para traducir archivos Markdown de un idioma fuente a un idioma objetivo. Está diseñado para ser flexible y fácil de usar, ofreciendo opciones adicionales como añadir una nota de traducción, una mejor gestión de los archivos de salida, detección de archivos existentes y soporte para múltiples idiomas y modelos de traducción.

Para una demostración y explicaciones detalladas, visite [jls42.org](https://jls42.org/) o en versión traducida: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) y [jls42.org 中文](https://jls42.org/traductions_zh/).

## Características Principales

- **Traducción con IA**: Utilice las últimas tecnologías de inteligencia artificial para traducir sus documentos con OpenAI, Mistral AI o Claude de Anthropic.
- **Soporte Multilingüe**: Traduzca sus documentos en varios idiomas con soporte para diferentes modelos de lenguaje.
- **Segmentación Inteligente**: Administre eficazmente textos largos gracias a una segmentación automatizada.
- **Nota de Traducción**: Añada automáticamente una nota de traducción para informar a los lectores sobre el proceso utilizado.
- **Mejora en la Gestión de Archivos de Salida**: Verifique si ya existe una traducción antes de comenzar a traducir.
- **Detección Mejorada de Archivos Existentes**: Busque archivos que coincidan con el nombre base del archivo original y el idioma objetivo.
- **Flexible y Extensible**: El código está estructurado para permitir una fácil adición de nuevas funcionalidades.

## Requisitos Previos

- Python 3.6 o versión posterior.
- Una clave API válida para OpenAI, Mistral AI o Claude de Anthropic.

## Instalación

1. Clone el repositorio Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Instale las dependencias necesarias:
```
pip install -r requirements.txt
```

## Configuración

Configure su entorno definiendo las variables de ambiente para las claves API necesarias:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='su-clave-api-openai'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='su-clave-api-mistral'
    ```
- **Claude de Anthropic**:
    ```
    export ANTHROPIC_API_KEY='su-clave-api-anthropic'
    ```

## Uso

El guion ofrece varias opciones para personalizar el proceso de traducción:

### Opciones Generales

- `--source_dir`: Directorio que contiene los archivos Markdown a traducir.
- `--target_dir`: Directorio de salida para los archivos traducidos.
- `--model`: Modelo de traducción GPT a utilizar. El modelo predeterminado depende de la API seleccionada.
- `--source_lang`: Idioma fuente de los documentos. Importante en particular para añadir notas de traducción.
- `--target_lang`: Idioma objetivo para la traducción. Por defecto, es inglés.
- `--force`: Forzar la traducción incluso si ya existe una traducción para el archivo.

### Opciones Específicas de la API

- `--use_mistral`: Utilizar la API de Mistral AI para la traducción.
- `--use_claude`: Utilizar la API de Claude de Anthropic para la traducción.
- `--add_translation_note`: Añadir una nota de traducción al contenido traducido, especificando el método y las herramientas utilizadas.

### Ejemplos de Uso

- Traducir del francés al inglés con OpenAI, añadiendo una nota de traducción:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Traducir del francés al español con Mistral AI, sin nota de traducción:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX  
Correo electrónico: contact@jls42.org

## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Vea el archivo [LICENSE](LICENSE) para más detalles.

**Este documento ha sido traducido de la versión fr a la lengua es utilizando el modelo gpt-4-1106-preview. Para más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**

