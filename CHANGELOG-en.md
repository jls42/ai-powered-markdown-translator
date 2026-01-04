### Changelog

🌍 [English](CHANGELOG-en.md) | [Spanish](CHANGELOG-es.md) | [Chinese](CHANGELOG-zh.md) | [German](CHANGELOG-de.md) | [Japanese](CHANGELOG-ja.md) | [Korean](CHANGELOG-ko.md) | [Arabic](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italian](CHANGELOG-it.md) | [Dutch](CHANGELOG-nl.md) | [Polish](CHANGELOG-pl.md) | [Portuguese](CHANGELOG-pt.md) | [Romanian](CHANGELOG-ro.md) | [Swedish](CHANGELOG-sv.md)

- **1.7** What's new:
    - Option `--keep_filename` to keep the original filename when translating
    - Support for the `.env` file to automatically load API keys
    - **Inline code preservation**: backticks (`` `...` ``) are now protected during translation
    - System prompt improvements:
        - Better handling of quotes in the YAML frontmatter
        - Protection of template variables `{variable}`
        - Prohibition of unsolicited translator notes
    - Successfully tested on 364 files (jls42.org blog migration)
- **1.6** What's new:
    - Support for the Google Gemini API for translation (`--use_gemini`)
    - Updated default models for 2026:
        - OpenAI: `gpt-5` (quality), `gpt-5-mini` (eco)
        - Claude: `claude-sonnet-4-5` (quality), `claude-haiku-4-5` (eco)
        - Gemini: `gemini-3-pro-preview` (quality), `gemini-3-flash-preview` (eco)
    - Economy mode (`--eco`) to use faster and less expensive models
    - Single-file translation (`--file`) without walking a directory
    - New simplified naming pattern: `{base}-{lang}.md`
    - Option `--include_model` to keep the old format with the model name
    - Support for unlisted models with default token limit (128k)
    - README translated into 14 languages
- **1.5** Improvements:
    - **Updated API keys and default models:**
        - **OpenAI:** Updated from `DEFAULT_MODEL_OPENAI` to `"gpt-4o"`.
        - **Mistral AI:** Updated from `DEFAULT_MODEL_MISTRAL` to `"mistral-large-latest"`.
        - **Anthropic's Claude:** Added `DEFAULT_ANTHROPIC_API_KEY` and updated from `DEFAULT_MODEL_CLAUDE` to `"claude-3-5-sonnet-20240620"`.
    - **Optimization of translation prompts:**
        - Prompts for direct translations and translation notes have been enhanced for better clarity and efficiency, including detailed instructions on preserving metadata and specific formatting elements.
    - **Code refactoring:**
        - Replaced `MistralClient` with the class `Mistral` for Mistral AI client initialization.
        - Reorganized imports for better readability and maintenance.
        - Improved text segmentation and code block handling to preserve original formatting during translation.
    - **Output file handling:**
        - Swapped model and language in output file names (for example, `f"{base}-{args.target_lang}-{args.model}.md"`), making organization and searching for translations easier.
    - **Miscellaneous improvements:**
        - Code cleanup by removing unnecessary blank lines.
        - Minor adjustments to improve structure and readability of the script.
- **1.4** What's new:
    - Support for Anthropic's Claude API for translation
    - Prompt optimizations for increased clarity and efficiency
    - Minor adjustments to improve code maintainability
- **1.3** Improvements and new features:
    - Improved code block handling
    - Improved output file handling
    - Improved existing file detection
    - Option `--force` to force translation
    - Swapped model and language in the output filename
- **1.2** Changelog fix
- **1.1** Added support for the Mistral AI API
- **1.0** Initial release - Support for the OpenAI API

**This document was translated from the fr version into the en language using the gpt-5-mini model. For more information on the translation process, consult https://gitlab.com/jls42/ai-powered-markdown-translator**

