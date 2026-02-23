### Registro de cambios

🌍 [Francés](CHANGELOG.md) | [Inglés](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [Chino](CHANGELOG-zh.md) | [Alemán](CHANGELOG-de.md) | [Japonés](CHANGELOG-ja.md) | [Coreano](CHANGELOG-ko.md) | [Árabe](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Neerlandés](CHANGELOG-nl.md) | [Polaco](CHANGELOG-pl.md) | [Portugués](CHANGELOG-pt.md) | [Rumano](CHANGELOG-ro.md) | [Sueco](CHANGELOG-sv.md)

- **1.7** Novedades :
    - Opción `--keep_filename` para conservar el nombre de archivo original durante la traducción
    - Soporte del archivo `.env` para cargar las claves API automáticamente
    - **Preservación del código inline** : los backticks (`` `...` ``) ahora están protegidos durante la traducción
    - Mejora del prompt del sistema :
        - Mejor gestión de las comillas en el YAML frontmatter
        - Protección de las variables de plantilla `{variable}`
        - Prohibición de notas del traductor no solicitadas
    - Probado con éxito en 364 archivos (migración del blog jls42.org)
- **1.6** Novedades :
    - Soporte de la API Google Gemini para la traducción (`--use_gemini`)
    - Actualización de los modelos por defecto 2026 :
        - OpenAI : `gpt-5` (calidad), `gpt-5-mini` (económico)
        - Claude : `claude-sonnet-4-5` (calidad), `claude-haiku-4-5` (económico)
        - Gemini : `gemini-3-pro-preview` (calidad), `gemini-3-flash-preview` (económico)
    - Modo económico (`--eco`) para usar modelos más rápidos y menos costosos
    - Traducción de archivo único (`--file`) sin recorrer un directorio
    - Nuevo patrón de nomenclatura simplificado : `{base}-{lang}.md`
    - Opción `--include_model` para conservar el formato antiguo con el nombre del modelo
    - Soporte para modelos no listados con límite de tokens por defecto (128k)
    - README traducido a 14 idiomas
- **1.5** Mejoras :
    - **Actualización de las claves API y de los modelos predeterminados :**
        - **OpenAI :** Actualización de `DEFAULT_MODEL_OPENAI` a `"gpt-4o"`.
        - **Mistral AI :** Actualización de `DEFAULT_MODEL_MISTRAL` a `"mistral-large-latest"`.
        - **Claude de Anthropic :** Añadido `DEFAULT_ANTHROPIC_API_KEY` y actualización de `DEFAULT_MODEL_CLAUDE` a `"claude-3-5-sonnet-20240620"`.
    - **Optimización de los prompts de traducción :**
        - Los prompts para las traducciones directas y las notas de traducción se han enriquecido para una mejor claridad y eficacia, incluyendo instrucciones detalladas sobre la preservación de metadatos y elementos de formato específicos.
    - **Refactorización del código :**
        - Reemplazo de `MistralClient` por la clase `Mistral` para la inicialización del cliente Mistral AI.
        - Reorganización de las importaciones para una mejor legibilidad y mantenimiento.
        - Mejora de la segmentación de textos y gestión de los bloques de código para preservar el formato original durante la traducción.
    - **Gestión de los archivos de salida :**
        - Inversión del modelo y del idioma en el nombre de los archivos de salida (por ejemplo, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitando así la organización y la búsqueda de las traducciones.
    - **Mejoras diversas :**
        - Limpieza del código eliminando las líneas vacías innecesarias.
        - Ajustes menores para mejorar la estructura y la legibilidad del script.
- **1.4** Novedades :
    - Soporte de la API Claude de Anthropic para la traducción
    - Optimización de los prompts para una mayor claridad y eficacia
    - Ajustes menores para mejorar el mantenimiento del código
- **1.3** Mejoras y nuevas funcionalidades :
    - Mejor gestión de los bloques de código
    - Mejor gestión de los archivos de salida
    - Mejora en la detección de archivos existentes
    - Opción `--force` para forzar la traducción
    - Inversión del modelo y del idioma en el nombre del archivo de salida
- **1.2** Corrección del changelog
- **1.1** Añadido soporte para la API Mistral IA
- **1.0** Versión inicial - Soporte de la API OpenAI

**Este documento ha sido traducido de la versión fr al idioma es utilizando el modelo gpt-5-mini. Para más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**

