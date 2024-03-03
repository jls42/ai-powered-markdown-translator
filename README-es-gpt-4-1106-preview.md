# Traductor de Markdown Potenciado por IA con OpenAI y Mistral AI

Este proyecto es un script avanzado de Python que utiliza la API de OpenAI o la API de Mistral AI para traducir archivos Markdown de un idioma fuente a un idioma objetivo. Está diseñado para ser flexible y fácil de usar, ofreciendo opciones adicionales como la inclusión de una nota de traducción, una mejor gestión de archivos de salida, la detección de archivos existentes y el soporte para múltiples idiomas y modelos de traducción.

Para una demostración y explicaciones detalladas, visite [jls42.org](https://jls42.org/) o en versión traducida: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_en/) y [jls42.org 中文](https://jls42.org/traductions_zh/).

## Características Principales

- **Traducción Potenciada por IA**: Utiliza las últimas tecnologías de IA para la traducción de tus documentos.
- **Soporte Multilingüe**: Traduce tus documentos en múltiples idiomas con soporte para diferentes modelos de lenguaje.
- **Segmentación Inteligente**: Administra eficientemente textos largos gracias a una segmentación automatizada.
- **Nota de Traducción**: Añade automáticamente una nota de traducción para informar a los lectores sobre el proceso utilizado.
- **Mejor Gestión de Archivos de Salida**: Verifica si una traducción ya existe antes de iniciar la traducción.
- **Mejora en la Detección de Archivos Existentes**: Busca archivos correspondientes al nombre base del archivo original y al idioma objetivo.
- **Flexible y Extensible**: El código está estructurado para facilitar la adición de nuevas características.

## Prerrequisitos

- Python 3.6 o versiones posteriores.
- Una clave API válida para OpenAI o Mistral AI.

## Instalación

1. Clona el repositorio Git:
```
git clone https://github.com/tu-repositorio/translate-markdown.git
```
2. Instala las dependencias requeridas:
```
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el script, configura tu entorno:

- **OpenAI**: Define tu clave API de OpenAI como una variable de entorno:
```
export OPENAI_API_KEY='tu-clave-api-openai'
```
- **Mistral AI**: Define tu clave API de Mistral AI como una variable de entorno:
```
export MISTRAL_API_KEY='tu-clave-api-mistral'
```

## Uso

Para traducir archivos Markdown:

- **Con OpenAI**:
```
python translate.py --source_dir 'ruta/origen' --target_dir 'ruta/destino'
```
- **Con Mistral AI** (y opción de nota de traducción):
```
python translate.py --use_mistral --source_dir 'ruta/origen' --target_dir 'ruta/destino' --model 'mistral-small' --add_translation_note
```

### Opciones Comunes

- Especifica el modelo, el idioma fuente y el idioma objetivo:
```
python translate.py --source_dir 'ruta/origen' --target_dir 'ruta/destino' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
```

### Nuevas Opciones

- Forzar la traducción incluso si ya existe una traducción:
```
python translate.py --source_dir 'ruta/origen' --target_dir 'ruta/destino' --force
```

## Ejemplos de Uso

- Ejemplo de solicitud de traducción al español:
```
python translate.py --source_dir contenido/ --target_dir contenido/traducciones_es --target_lang es
```


## Autor

Julien LE SAUX  
Email: contact@jls42.org


## Licencia

Este proyecto está bajo la licencia GNU GENERAL PUBLIC LICENSE Versión 3, 29 de junio de 2007. Consulta el archivo [LICENSE](LICENSE) para más detalles.

**Este documento ha sido traducido de la versión fr a la lengua es utilizando el modelo gpt-4-1106-preview. Para más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**

