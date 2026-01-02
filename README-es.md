# Traductor de Markdown impulsado por IA

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Traductor de archivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** y **Google Gemini**.

Este script de Python traduce archivos Markdown de un idioma fuente a un idioma objetivo preservando el formato, los bloques de código y los metadatos de front matter.

## Características principales

- **Multi-Proveedor**: Soporte de 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Modo económico**: Opción `--eco` para utilizar modelos más rápidos y menos costosos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del código**: Los bloques de código no se traducen
- **Nota de traducción**: Adición opcional de una nota al final del documento

## Instalación

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuración

Defina la variable de entorno para la API que desea utilizar :

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Uso

### Traducir un solo archivo

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducir un directorio

```bash
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Modo económico

Utiliza modelos más rápidos y menos costosos (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción | Descripción |
|--------|-------------|
| `--file` | Archivo Markdown único a traducir |
| `--source_dir` | Directorio de origen que contiene los archivos Markdown |
| `--target_dir` | Directorio de salida para los archivos traducidos |
| `--source_lang` | Idioma de origen (predeterminado: `fr`) |
| `--target_lang` | Idioma de destino (predeterminado: `en`) |
| `--model` | Modelo específico a utilizar |
| `--eco` | Utilizar los modelos económicos |
| `--use_mistral` | Utilizar la API Mistral AI |
| `--use_claude` | Utilizar la API Claude |
| `--use_gemini` | Utilizar la API Gemini |
| `--force` | Forzar la retraducción |
| `--add_translation_note` | Añadir una nota de traducción |

### Modelos por defecto (2026)

| Proveedor | Calidad (por defecto) | Económico (`--eco`) |
|----------|------------------------|---------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Autor

Julien LE SAUX
Correo electrónico : contact@jls42.org

## Licencia

LICENCIA PÚBLICA GENERAL DE GNU Versión 3. Ver [LICENSE](LICENSE).