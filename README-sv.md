# AI-driven Markdown-översättare

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>

Markdownfilöversättare som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdownfiler från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Flera leverantörer**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini)
- **Modeller 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Ekonomiläge**: Alternativ `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativ `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokenbegränsningar per modell
- **Kodbevarande**: Kodblock OCH inlinekod (`` `...` ``) bevaras
- **Filnamn**: Alternativ `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativ `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnotering**: Valfri tilläggsnotering i slutet av dokumentet

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kvalitetsverktyg (valfritt men rekommenderat)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra att kod med felaktig formatering, sårbarheter eller hemligheter committas. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (gradvis typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet `CLAUDE.md` _Kvalitet / pre-commit_ för detaljer.

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

Använder snabbare och billigare modeller (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ              | Beskrivning                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| `--file`                 | Enskild Markdownfil att översätta                                      |
| `--source_dir`           | Källkatalog som innehåller Markdownfilerna                            |
| `--target_dir`           | Utdatakatalog för de översatta filerna                                 |
| `--source_lang`          | Källspråk (standard: `fr`)                                    |
| `--target_lang`          | Målspråk (standard: `en`)                                    |
| `--model`                | Specifik modell att använda                                            |
| `--eco`                  | Använd de ekonomiska modellerna                                        |
| `--use_mistral`          | Använd Mistral AI:s API                                                |
| `--use_claude`           | Använd Claudes API                                                      |
| `--use_gemini`           | Använd Gemini:s API                                                    |
| `--force`                | Tvinga omöversättning                                                  |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                       |
| `--news`                 | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk               |
| `--add_translation_note` | Lägg till en översättningsnotering                                       |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                    |

### Standardmodeller (2026)

| Leverantör | Kvalitet (standard)      | Ekonomi (`--eco`)           |
| ---------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Rekommendation för långa översättningar**: `--use_gemini` (standard = `gemini-3.1-pro-preview` kvalitet, `--eco` = `gemini-3.1-flash-lite-preview`) tenderar att bättre bevara markdownstrukturen i icke-latinska skript (PL, JA, ZH, AR, HI), särskilt i `--news`-läge där troheten mot platshållare är viktig. OpenAI förblir standard för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](LICENSE).

**Detta dokument har översatts från versionen fr till språket sv med hjälp av modellen gpt-5.4-mini. För mer information om översättningsprocessen, se https://github.com/jls42/ai-powered-markdown-translator**
