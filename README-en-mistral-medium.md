AI-Powered Markdown Translator with OpenAI, Mistral AI, and Claude from Anthropic

This project is an advanced Python script that uses OpenAI, Mistral AI, or Claude from Anthropic APIs to translate Markdown files from a source language to a target language. It is designed to be flexible and easy to use, offering additional options such as adding a translation note, enhanced output file management, detection of existing files, and support for multiple languages and translation models.

For a demonstration and detailed explanations, visit [jls42.org](https://jls42.org/) or translated versions: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) and [jls42.org 中文](https://jls42.org/traductions_zh/).

## Main Features

- **AI-Powered Translation**: Utilize the latest AI technologies for document translation using OpenAI, Mistral AI, or Claude from Anthropic.
- **Multilingual Support**: Translate your documents into several languages with support for different language models.
- **Smart Segmentation**: Handle long texts efficiently with automated segmentation.
- **Translation Note**: Automatically add a translation note to inform readers about the process used.
- **Enhanced Output File Management**: Check if a translation already exists before starting the translation.
- **Improved Existing File Detection**: Search for files corresponding to the original file's base name and target language.
- **Flexible and Extensible**: The code is structured to allow easy addition of new features.

## Prerequisites

- Python 3.6 or higher.
- A valid API key for OpenAI, Mistral AI, or Claude from Anthropic.

## Installation

1. Clone the Git repository:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Install the necessary dependencies:
```
pip install -r requirements.txt
```

## Configuration

Configure your environment by defining the environment variables for the necessary API keys:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Claude from Anthropic**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## Usage

The script offers several options to customize the translation process:

### General Options

- `--source_dir`: Directory containing the Markdown files to translate.
- `--target_dir`: Output directory for the translated files.
- `--model`: GPT translation model to use. The default model depends on the selected API.
- `--source_lang`: Source language of the documents. Important, notably for adding translation notes.
- `--target_lang`: Target language for the translation. Default is English.
- `--force`: Force translation even if a translation already exists for the file.

### Specific API Options

- `--use_mistral`: Use the Mistral AI API for translation.
- `--use_claude`: Use the Claude from Anthropic API for translation.
- `--add_translation_note`: Add a translation note to the translated content, specifying the method and tools used.

### Examples of Usage

- Translate from French to English with OpenAI, adding a translation note:
    ```
    python translate.py --use_openai --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Translate from French to Spanish with Mistral AI, without a translation note:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Author

Julien LE SAUX  
Email: contact@jls42.org

## License

This project is under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the [LICENSE](LICENSE) file for more details.

**This document has been translated from the fr version to the en language using the mistral-medium model. For more information about the translation process, visit <https://gitlab.com/jls42/ai-powered-markdown-translator>**

