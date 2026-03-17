# AI-driven Markdown-översättare

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Markdown-fileröversättare som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Multi-Provider**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini)
- **Modeller 2026**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **Ekonomiläge**: Alternativ `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativ `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med modellernas tokenbegränsningar
- **Kodbevarande**: Kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativ `--keep_filename` för att behålla originalnamnet
- **Nyhetsläge**: Alternativ `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnot**: Valfri tillägg av en not i slutet av dokumentet

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguration

Skapa en fil `.env` i projektets rotkatalog eller definiera miljövariablerna:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Användning

### Översätt en enskild fil

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätt en katalog

```bash
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Ekonomiläge

Använder snabbare och billigare modeller (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ | Beskrivning |
|--------|-------------|
| `--file` | En enda Markdown-fil att översätta |
| `--source_dir` | Källkatalog som innehåller Markdown-filerna |
| `--target_dir` | Utdatakatalog för de översatta filerna |
| `--source_lang` | Källspråk (standard: `fr`) |
| `--target_lang` | Målspråk (standard: `en`) |
| `--model` | Specifik modell att använda |
| `--eco` | Använd ekonomimodellerna |
| `--use_mistral` | Använd Mistral AI:s API |
| `--use_claude` | Använd Claude-API:t |
| `--use_gemini` | Använd Gemini-API:t |
| `--force` | Tvinga omöversättning |
| `--keep_filename` | Behåll originalfilnamnet |
| `--news` | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk |
| `--add_translation_note` | Lägg till en översättningsnot |
| `--include_model` | Inkludera modellens namn i utdatafilen |

### Standardmodeller (2026)

| Provider | Kvalitet (standard) | Ekonomi (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](LICENSE).