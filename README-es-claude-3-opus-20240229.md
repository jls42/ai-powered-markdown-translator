# Traductor de Markdown con Inteligencia Artificial impulsado por OpenAI, Mistral AI y Claude de Anthropic

Este proyecto es un script de Python avanzado que utiliza las API de OpenAI, Mistral AI o Claude de Anthropic para traducir archivos Markdown de un idioma de origen a un idioma de destino. Está diseñado para ser flexible y fácil de usar, ofreciendo opciones adicionales como añadir una nota de traducción, gestión mejorada de archivos de salida, detección de archivos existentes y soporte para múltiples idiomas y modelos de traducción.

Para una demostración y explicaciones detalladas, visite [jls42.org](https://jls42.org/) o en versión traducida: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) y [jls42.org 中文](https://jls42.org/traductions_zh/).

## Características Principales

- **Traducción impulsada por IA**: Utilice las últimas tecnologías de IA para la traducción de sus documentos con OpenAI, Mistral AI o Claude de Anthropic.
- **Soporte multilingüe**: Traduzca sus documentos en varios idiomas con soporte para diferentes modelos de lenguaje.
- **Segmentación inteligente**: Gestione eficazmente textos largos mediante una segmentación automatizada.
- **Nota de traducción**: Añada automáticamente una nota de traducción para informar a los lectores sobre el proceso utilizado.
- **Gestión mejorada de archivos de salida**: Compruebe si ya existe una traducción antes de iniciar la traducción.
- **Detección mejorada de archivos existentes**: Busque archivos que coincidan con el nombre base del archivo original y el idioma de destino.
- **Flexible y extensible**: El código está estructurado para permitir la facilidad de añadir nuevas funcionalidades.

## Requisitos previos

- Python 3.6 o una versión posterior.
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

Configure su entorno definiendo las variables de entorno para las claves API necesarias:

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

El script ofrece varias opciones para personalizar el proceso de traducción:

### Opciones Generales

- `--source_dir`: Directorio que contiene los archivos Markdown a traducir.
- `--target_dir`: Directorio de salida para los archivos traducidos.
- `--model`: Modelo de traducción GPT a utilizar. El modelo predeterminado depende de la API seleccionada.
- `--source_lang`: Idioma de origen de los documentos. Importante especialmente para añadir notas de traducción.
- `--target_lang`: Idioma de destino para la traducción. Por defecto, es el inglés.
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
Email: contact@jls42.org

## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Consulte el archivo [LICENSE](LICENSE) para más detalles.

**Este documento fue traducido de la versión fr al idioma es usando el modelo claude-3-opus-20240229. Para obtener más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**

