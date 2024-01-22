# AI-Powered Markdown Translator with OpenAI and Mistral AI

This project is an advanced Python script that uses the OpenAI API or the Mistral AI API to translate Markdown files from a source language to a target language. It is designed to be flexible and easy to use, offering additional options such as adding a translation note and supporting multiple languages and translation models.

For a demonstration and detailed explanations, visit [jls42.org](https://jls42.org/) or in translated versions: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_en/), and [jls42.org 中文中文](https://jls42.org/traductions_zh/).

## Main Features

- **AI-Powered Translation**: Use the latest AI technology for document translation.
- **Multilingual Support**: Translate your documents into multiple languages with support for different language models.
- **Intelligent Segmentation**: Manage long texts efficiently through automatic segmentation.
- **Translation Note**: Automatically add a translation note to inform readers about the process used.
- **Flexible and Extensible**: The code is structured to allow easy addition of new features.

## Prerequisites

- Python 3.6 or later.
- A valid API key for OpenAI or Mistral AI.

## Installation

1. Clone the Git repository:
   ```
   git clone https://github.com/your-directory/translate-markdown.git
   ```
2. Install the necessary dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, configure your environment:

- **OpenAI**: Set your OpenAI API key as an environment variable:
  ```
  export OPENAI_API_KEY='your-openai-api-key'
  ```
- **Mistral AI**: Set your Mistral AI API key as an environment variable:
  ```
  export MISTRAL_API_KEY='your-mistral-api-key'
  ```

## Usage

To translate Markdown files:

- **With OpenAI**:
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **With Mistral AI** (and translation note option):
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### Common Options

- Specify the model, source language, and target language:
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## Examples of Usage

- Example of a translation request in Spanish:
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## License

This project is licensed under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the [LICENSE](LICENSE) file for more details.

**This document has been translated from the fr version by the mistral-medium model.**

