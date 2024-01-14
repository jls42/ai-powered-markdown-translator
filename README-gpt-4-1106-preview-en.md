# Markdown Translator with OpenAI and Mistral AI

This project is a Python script that uses the OpenAI API or the Mistral AI API to translate Markdown files from a source language to a target language.
More information at [IA Translation jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/).

## Prerequisites

To use this script, you will need:

- Python 3.6 or higher
- An OpenAI account with an API key or a Mistral AI account with an API key

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### With OpenAI

To use this script with OpenAI, you must first set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   ```

Then, you can run the script using the following command:

   ```bash
   python translate.py --source_dir 'path/to/your/source/directory' --target_dir 'path/to/your/target/directory'
   ```

### With Mistral AI

To use this script with Mistral AI, you must first set your Mistral AI API key as an environment variable:

   ```bash
   export MISTRAL_API_KEY='your-mistral-api-key'
   ```

Then, run the script with the `--use_mistral` option:

   ```bash
   python translate.py --use_mistral --source_dir 'path/to/your/source/directory' --target_dir 'path/to/your/target/directory' --model 'mistral-small'
   ```

### Common Options

You can also specify the model to use, the source language, and the target language:

   ```bash
   python translate.py --source_dir 'path/to/your/source/directory' --target_dir 'path/to/your/target/directory' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
   ```

## Usage Examples

   ```bash
   ################################################
   # AI translation request to Spanish            #
   ################################################
   jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
   Processing the file: content/posts/ia/stable-difusion-aws-ec2.md
   Translation completed in 33.19 seconds.
   File 'stable-difusion-aws-ec2.md' processed.
   # ... other result lines ...
   ```

## License

This project is under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the [LICENSE](LICENSE) file for more details.

**This document has been translated from the French version of the blog by the model gpt-4-1106-preview.**

