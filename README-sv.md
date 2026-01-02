# AI-driven Markdown-översättare

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Översättare av Markdown-filer som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Multi-leverantör**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini)
- **2026-modeller**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Ekonomiläge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enstaka fil**: Alternativet `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med token-gränser per modell
- **Bevarande av kod**: Kodblock översätts inte
- **Översättningsanteckning**: Valfritt tillägg av en anteckning i slutet av dokumentet

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguration

Ställ in miljövariabeln för API:et du vill använda:

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Användning

### Översätt en enskild fil

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätt en katalog

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

### Ekonomiläge

Använder snabbare och billigare modeller (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ | Beskrivning |
|--------|-------------|
| `--file` | En enskild Markdown-fil att översätta |
| `--source_dir` | Källkatalog som innehåller Markdown-filerna |
| `--target_dir` | Utkatalog för de översatta filerna |
| `--source_lang` | Källspråk (standard: `fr`) |
| `--target_lang` | Målspråk (standard: `en`) |
| `--model` | Specifik modell att använda |
| `--eco` | Använd de ekonomiska modellerna |
| `--use_mistral` | Använd Mistral AI:s API |
| `--use_claude` | Använd Claude-API:et |
| `--use_gemini` | Använd Gemini-API:et |
| `--force` | Tvinga att översätta om |
| `--add_translation_note` | Lägg till en översättningsanteckning |

### Standardmodeller (2026)

| Leverantör | Kvalitet (standard) | Ekonomisk (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Författare

Julien LE SAUX
E-post : contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](LICENSE).