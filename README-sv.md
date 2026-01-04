# AI-drivet Markdown-översättningsverktyg

🌍 [Engelska](README-en.md) | [Spanska](README-es.md) | [Kinesiska](README-zh.md) | [Tyska](README-de.md) | [Japanska](README-ja.md) | [Koreanska](README-ko.md) | [Arabiska](README-ar.md) | [Hindi](README-hi.md) | [Italienska](README-it.md) | [Nederländska](README-nl.md) | [Polska](README-pl.md) | [Portugisiska](README-pt.md) | [Rumänska](README-ro.md) | [Svenska](README-sv.md)

Markdown-filöversättare som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Flera leverantörer**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini)
- **Modeller 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Sparläge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativ `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokengränser per modell
- **Bevarande av kod**: Kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativ `--keep_filename` för att behålla ursprungligt namn
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsanteckning**: Valfritt tillägg av en anteckning i slutet av dokumentet

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguration

Skapa en fil `.env` i projektets rot eller ange miljövariablerna:

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

### Översätta en enskild fil

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätta en mapp

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

### Sparläge

Använder snabbare och billigare modeller (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ | Beskrivning |
|-----------|-------------|
| `--file` | En enskild Markdown-fil som ska översättas |
| `--source_dir` | Källmapp som innehåller Markdown-filerna |
| `--target_dir` | Utdatakatalog för de översatta filerna |
| `--source_lang` | Källspråk (standard: `fr`) |
| `--target_lang` | Målspråk (standard: `en`) |
| `--model` | Specifik modell att använda |
| `--eco` | Använd sparmodeller |
| `--use_mistral` | Använd Mistral AI API |
| `--use_claude` | Använd Claude API |
| `--use_gemini` | Använd Gemini API |
| `--force` | Tvinga omöversättning |
| `--keep_filename` | Behåll originalfilnamnet |
| `--add_translation_note` | Lägg till en översättningsanteckning |
| `--include_model` | Inkludera modellnamnet i utdatafilen |

### Standardmodeller (2026)

| Leverantör | Kvalitet (standard) | Sparläge (`--eco`) |
|-----------|---------------------|---------------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Personlig blogg översatt till 15 språk 

## Författare

Julien LE SAUX  
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENS](LICENSE).

**Detta dokument har översatts från fr till sv med modellen gpt-5-mini. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator**

