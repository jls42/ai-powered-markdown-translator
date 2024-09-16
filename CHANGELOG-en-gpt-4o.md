### Changelog

- **1.0** Initial version - Support for the OpenAI API
- **1.1** Added support for the Mistral AI API
- **1.2** Fix of the changelog
- **1.3** Improvements and new features:
    - Improved handling of code blocks
    - Improved handling of output files
    - Improved detection of existing files
    - `--force` option to force translation
    - Reversal of the model and language in the filename
- **1.4** New features:
    - Support for the Claude API from Anthropic for translation
    - Optimization of prompts for increased clarity and efficiency
    - Minor adjustments to improve code maintenance
- **1.5** Improvements:
    - **Update of default API keys and models:**
        - **OpenAI:** Update of `DEFAULT_MODEL_OPENAI` to `"gpt-4o"`.
        - **Mistral AI:** Update of `DEFAULT_MODEL_MISTRAL` to `"mistral-large-latest"`.
        - **Claude from Anthropic:** Addition of `DEFAULT_ANTHROPIC_API_KEY` and update of `DEFAULT_MODEL_CLAUDE` to `"claude-3-5-sonnet-20240620"`.
    - **Optimization of translation prompts:**
        - Prompts for direct translations and translation notes have been enriched for better clarity and efficiency, including detailed instructions on preserving metadata and specific formatting elements.
    - **Code refactoring:**
        - Replacement of `MistralClient` with the `Mistral` class for initializing the Mistral AI client.
        - Reorganization of imports for better readability and maintenance.
        - Improvement of text segmentation and handling of code blocks to preserve original formatting during translation.
    - **Handling of output files:**
        - Reversal of the model and language in the output file names (e.g., `f"{base}-{args.target_lang}-{args.model}.md"`), facilitating organization and search of translations.
    - **Various improvements:**
        - Code cleanup by removing unnecessary empty lines.
        - Minor adjustments to improve the structure and readability of the script.

**This document was translated from the fr version to the en language using the gpt-4o model. For more information on the translation process, visit https://gitlab.com/jls42/ai-powered-markdown-translator.**

