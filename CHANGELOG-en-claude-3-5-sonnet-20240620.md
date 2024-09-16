### Changelog

- **1.0** Initial version - OpenAI API support
- **1.1** Added Mistral AI API support
- **1.2** Fixed changelog
- **1.3** Improvements and new features:
    - Improved code block handling
    - Improved output file handling
    - Improved existing file detection
    - `--force` option to force translation
    - Reversed model and language in output filename
- **1.4** New features:
    - Support for Anthropic's Claude API for translation
    - Optimization of prompts for increased clarity and efficiency
    - Minor adjustments to improve code maintenance
- **1.5** Improvements:
    - **Updated API keys and default models:**
        - **OpenAI:** Updated `DEFAULT_MODEL_OPENAI` to `"gpt-4o"`.
        - **Mistral AI:** Updated `DEFAULT_MODEL_MISTRAL` to `"mistral-large-latest"`.
        - **Anthropic's Claude:** Added `DEFAULT_ANTHROPIC_API_KEY` and updated `DEFAULT_MODEL_CLAUDE` to `"claude-3-5-sonnet-20240620"`.
    - **Optimization of translation prompts:**
        - Prompts for direct translations and translation notes have been enriched for better clarity and efficiency, including detailed instructions on preserving metadata and specific formatting elements.
    - **Code refactoring:**
        - Replaced `MistralClient` with the `Mistral` class for Mistral AI client initialization.
        - Reorganized imports for better readability and maintenance.
        - Improved text segmentation and code block handling to preserve original formatting during translation.
    - **Output file management:**
        - Reversed model and language in output filenames (e.g., `f"{base}-{args.target_lang}-{args.model}.md"`), thus facilitating organization and search of translations.
    - **Various improvements:**
        - Cleaned up code by removing unnecessary blank lines.
        - Minor adjustments to improve script structure and readability.

**This document was translated from the fr version to the en language using the claude-3-5-sonnet-20240620 model. For more information on the translation process, see https://gitlab.com/jls42/ai-powered-markdown-translator**

