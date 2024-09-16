# AI-Powered Markdown Translator with OpenAI, Mistral AI, and Anthropic's Claude

This project is an advanced Python script that utilizes the OpenAI, Mistral AI, or Anthropic's Claude APIs to translate Markdown files from a source language to a target language. It is designed to be flexible and easy to use, offering additional options such as adding a translation note, enhanced output file management, existing file detection, and support for multiple languages and translation models.

For a demonstration and detailed explanations, visit [jls42.org](https://jls42.org/) or the translated versions: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/), and [jls42.org 中文](https://jls42.org/traductions_zh/).

## Key Features

- **AI-Powered Translation**: Use the latest AI technologies to translate your documents with OpenAI, Mistral AI, or Anthropic's Claude.
- **Multilingual Support**: Translate your documents into multiple languages with support for different language models.
- **Smart Segmentation**: Effectively manage long texts with automated segmentation.
- **Translation Note**: Automatically add a translation note to inform readers about the process used.
- **Enhanced Output File Management**: Check if a translation already exists before starting the translation.
- **Improved Existing File Detection**: Search for files matching the base name of the original file and the target language.
- **Flexible and Extensible**: The code is structured to allow easy addition of new features.

## Prerequisites

- Python 3.6 or later.
- A valid API key for OpenAI, Mistral AI, or Anthropic's Claude.

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

Set up your environment by defining the environment variables for the necessary API keys:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Anthropic's Claude**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## Usage

The script offers several options to customize the translation process:

### General Options

- `--source_dir`: Directory containing the Markdown files to be translated.
- `--target_dir`: Output directory for the translated files.
- `--model`: GPT translation model to use. The default model depends on the selected API.
- `--source_lang`: Source language of the documents. Important for adding translation notes.
- `--target_lang`: Target language for the translation. Default is English.
- `--force`: Force translation even if a translation already exists for the file.

### Specific API Options

- `--use_mistral`: Use the Mistral AI API for translation.
- `--use_claude`: Use the Anthropic's Claude API for translation.
- `--add_translation_note`: Add a translation note to the translated content, specifying the method and tools used.

### Usage Examples

- Translate from French to English with OpenAI, adding a translation note:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Translate from French to Spanish with Mistral AI, without a translation note:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Author

Julien LE SAUX  
Email: contact@jls42.org

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the [LICENSE](LICENSE) file for more details.

**This document was translated from the fr version to the en language using the gpt-4o model. For more information on the translation process, see https://gitlab.com/jls42/ai-powered-markdown-translator.**

