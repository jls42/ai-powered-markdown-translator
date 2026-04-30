# AI-driven Markdown-översättare

🌍 [Franska](README.md) | [Engelska](README-en.md) | [Spanska](README-es.md) | [Kinesiska](README-zh.md) | [Tyska](README-de.md) | [Japanska](README-ja.md) | [Koreanska](README-ko.md) | [Arabiska](README-ar.md) | [Hindi](README-hi.md) | [Italienska](README-it.md) | [Nederländska](README-nl.md) | [Polska](README-pl.md) | [Portugisiska](README-pt.md) | [Rumänska](README-ro.md) | [Svenska](README-sv.md)

Markdown-filöversättare som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Flera leverantörer**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini)
- **Modeller 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Ekonomiläge**: Alternativ `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativ `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokensgränser per modell
- **Kodbevarande**: Kodblock OCH inlinekod (`` `...` ``) bevaras
- **Filnamn**: Alternativ `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativ `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnotering**: Valfri tilläggsnotering i slutet av dokumentet

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kvalitetsverktyg (valfritt men rekommenderat)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra att dåligt formaterad kod, sårbar kod eller kod som innehåller hemligheter committas. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (gradvis typning), Opengrep (SAST), pip-audit (CVE-deps), unittest. Se avsnittet `CLAUDE.md` _Kvalitet / pre-commit_ för detaljer.

## Konfiguration

Skapa en fil `.env` i projektets rot eller definiera miljövariablerna:

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

### Översätta en katalog

```bash
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Ekonomiläge

Använder snabbare och billigare modeller (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ              | Beskrivning                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `--file`                 | Enkel Markdown-fil att översätta                                 |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna                      |
| `--target_dir`           | Utdatakatalog för de översatta filerna                           |
| `--source_lang`          | Källspråk (standard: `fr`)                                             |
| `--target_lang`          | Målspråk (standard: `en`)                                              |
| `--model`                | Specifik modell att använda                                      |
| `--eco`                  | Använd ekonomimodeller                                          |
| `--use_mistral`          | Använd Mistral AI API                                           |
| `--use_claude`           | Använd Claude API                                               |
| `--use_gemini`           | Använd Gemini API                                               |
| `--force`                | Tvinga omöversättning                                           |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                |
| `--news`                 | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk        |
| `--add_translation_note` | Lägg till en översättningsnotering                                 |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                             |

### Standardmodeller (2026)

| Leverantör | Kvalitet (standard)         | Ekonomi (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Rekommendation för långa översättningar**: `--use_gemini` (standard = `gemini-3.1-pro-preview` kvalitet, `--eco` = `gemini-3-flash-preview`) tenderar att bättre bevara markdown-strukturen på icke-latinska skript (PL, JA, ZH, AR, HI), särskilt i `--news`-läge där troheten mot platshållare spelar roll. OpenAI förblir standard för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENS](LICENSE).

**Detta dokument har översatts från versionen fr till språket sv med hjälp av modellen gpt-5.4-mini. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator**

