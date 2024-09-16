### Changelog

- **1.0** Versión inicial - Soporte de la API OpenAI
- **1.1** Adición del soporte de la API Mistral IA
- **1.2** Corrección del changelog
- **1.3** Mejoras y nuevas funciones:
    - Gestión mejorada de bloques de código
    - Gestión mejorada de archivos de salida
    - Detección mejorada de archivos existentes
    - Opción `--force` para forzar la traducción
    - Inversión del modelo y el idioma en el nombre del archivo de salida
- **1.4** Novedades:
    - Soporte de la API Claude de Anthropic para la traducción
    - Optimización de los prompts para una mayor claridad y eficiencia
    - Ajustes menores para mejorar el mantenimiento del código
- **1.5** Mejoras:
    - **Actualización de las claves API y los modelos predeterminados:**
        - **OpenAI:** Actualización de `DEFAULT_MODEL_OPENAI` a `"gpt-4o"`.
        - **Mistral AI:** Actualización de `DEFAULT_MODEL_MISTRAL` a `"mistral-large-latest"`.
        - **Claude de Anthropic:** Adición de `DEFAULT_ANTHROPIC_API_KEY` y actualización de `DEFAULT_MODEL_CLAUDE` a `"claude-3-5-sonnet-20240620"`.
    - **Optimización de los prompts de traducción:**
        - Los prompts para las traducciones directas y las notas de traducción se han enriquecido para una mejor claridad y eficiencia, incluyendo instrucciones detalladas sobre la preservación de los metadatos y los elementos de formato específicos.
    - **Refactorización del código:**
        - Reemplazo de `MistralClient` por la clase `Mistral` para la inicialización del cliente Mistral AI.
        - Reorganización de las importaciones para una mejor legibilidad y mantenimiento.
        - Mejora en la segmentación de textos y gestión de bloques de código para preservar el formato original durante la traducción.
    - **Gestión de archivos de salida:**
        - Inversión del modelo y del idioma en el nombre de los archivos de salida (por ejemplo, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitando así la organización y búsqueda de las traducciones.
    - **Mejoras diversas:**
        - Limpieza del código eliminando las líneas vacías innecesarias.
        - Ajustes menores para mejorar la estructura y legibilidad del script.

**Este documento ha sido traducido de la versión fr a la lengua es utilizando el modelo gpt-4o. Para más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator.**

