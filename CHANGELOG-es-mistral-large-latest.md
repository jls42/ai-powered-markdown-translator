### Changelog

- **1.0** Versión inicial - Soporte de la API de OpenAI
- **1.1** Añadido soporte de la API de Mistral IA
- **1.2** Corrección del changelog
- **1.3** Mejoras y nuevas funcionalidades:
    - Gestión mejorada de los bloques de código
    - Gestión mejorada de los archivos de salida
    - Detección mejorada de archivos existentes
    - Opción `--force` para forzar la traducción
    - Inversión del modelo y del idioma en el nombre del archivo de salida
- **1.4** Novedades:
    - Soporte de la API Claude de Anthropic para la traducción
    - Optimización de los prompts para una mayor claridad y eficiencia
    - Ajustes menores para mejorar el mantenimiento del código
- **1.5** Mejoras:
    - **Actualización de las claves API y los modelos por defecto:**
        - **OpenAI:** Actualización de `DEFAULT_MODEL_OPENAI` a `"gpt-4o"`.
        - **Mistral AI:** Actualización de `DEFAULT_MODEL_MISTRAL` a `"mistral-large-latest"`.
        - **Claude de Anthropic:** Adición de `DEFAULT_ANTHROPIC_API_KEY` y actualización de `DEFAULT_MODEL_CLAUDE` a `"claude-3-5-sonnet-20240620"`.
    - **Optimización de los prompts de traducción:**
        - Los prompts para las traducciones directas y las notas de traducción han sido enriquecidos para una mejor claridad y eficiencia, incluyendo instrucciones detalladas sobre la preservación de los metadatos y los elementos de formato específicos.
    - **Refactorización del código:**
        - Reemplazo de `MistralClient` por la clase `Mistral` para la inicialización del cliente Mistral AI.
        - Reorganización de los imports para una mejor legibilidad y mantenimiento.
        - Mejora de la segmentación de los textos y gestión de los bloques de código para preservar el formato original durante la traducción.
    - **Gestión de los archivos de salida:**
        - Inversión del modelo y del idioma en el nombre de los archivos de salida (por ejemplo, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitando así la organización y búsqueda de las traducciones.
    - **Mejoras diversas:**
        - Limpieza del código eliminando líneas en blanco innecesarias.
        - Ajustes menores para mejorar la estructura y la legibilidad del script.

**Ce document a été traduit de la version fr vers la langue es en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**

