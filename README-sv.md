# AI-driven Markdown-översättare

🌍 [Franska](README.md) | [Engelska](README-en.md) | [Spanska](README-es.md) | [Kinesiska](README-zh.md) | [Tyska](README-de.md) | [Japanska](README-ja.md) | [Koreanska](README-ko.md) | [Arabiska](README-ar.md) | [Hindi](README-hi.md) | [Italienska](README-it.md) | [Nederländska](README-nl.md) | [Polska](README-pl.md) | [Portugisiska](README-pt.md) | [Rumänska](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status för kvalitetsgrinden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Säkerhetsbedömning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Tillförlitlighetsbedömning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Underhållsbarhetsbedömning"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Täckning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Sårbarheter"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Buggar"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Kodlukt"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicerade rader (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Teknisk skuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Kodrader"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-märke"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdown-filöversättare som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som det bevarar formatering, kodblock och front matter-metadata.

## Huvudfunktioner

- **Multi-Provider**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini)
- **Modeller 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Ekonomiläge**: Alternativ `--eco` för att använda snabbare och billigare modeller
- **Enstaka fil**: Alternativ `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokenbegränsningar per modell
- **Kodbevarande**: Kodblock OCH inlinekod (`` `...` ``) bevaras
- **Filnamn**: Alternativ `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativ `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnotis**: Valfri tilläggsnotis i slutet av dokumentet

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kvalitetsverktyg (valfritt men rekommenderas)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra att kod som är felaktigt formaterad, sårbar eller innehåller en hemlighet committas. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (progressiv typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet `CLAUDE.md` _Quality / pre-commit_ för detaljer.

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

### Översätt en enda fil

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätt en katalog

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

| Alternativ              | Beskrivning                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| `--file`                 | En enda Markdown-fil att översätta                                    |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna                           |
| `--target_dir`           | Utkatalog för de översatta filerna                                    |
| `--source_lang`          | Källspråk (standard: `fr`)                                   |
| `--target_lang`          | Målspråk (standard: `en`)                                    |
| `--model`                | Specifik modell att använda                                            |
| `--eco`                  | Använd ekonomimodellerna                                               |
| `--use_mistral`          | Använd Mistral AI-API:n                                                |
| `--use_claude`           | Använd Claude-API:n                                                   |
| `--use_gemini`           | Använd Gemini-API:n                                                   |
| `--force`                | Tvinga omöversättning                                                  |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                      |
| `--news`                 | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk               |
| `--add_translation_note` | Lägg till en översättningsnotis                                       |
| `--note_position`        | Notisens placering: `top`, `bottom` (standard) eller `both` |
| `--note_format`          | Notisens format: `legacy` (standard, fet paragraf) eller `marker` |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                   |

### Översättningsnotis: placering och format

Med `--add_translation_note` kan translatorn placera notisen överst, nederst eller på båda platserna, och göra den antingen i vanligt textformat (bakåtkompatibelt) eller i `marker`-format som kan användas av ett Markdown-plugin.

**Placering** (`--note_position`) :

- `bottom` (standard): notis i slutet av filen, som historiskt.
- `top` : notis infogad **efter YAML-frontmatter** (säkerhet för Astro Content Collections, gray-matter, etc.).
- `both` : notis infogad både överst OCH nederst (ett enda LLM-anrop, innehåll som återanvänds för båda placeringarna).

**Format** (`--note_format`) :

- `legacy` (standard): fet paragraf `**...**` — beteendet är strikt identiskt med v1.8, byte för byte. Kompatibelt med Hugo, GitHub, GitLab och alla Markdown-renderare.
- `marker` : osynlig Markdown-länkreferensdefinition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) följd av ett blockquote i fet stil. Nativt läsbar på GitHub/GitLab, och kan användas vid build av ett remark-plugin i Astro för att skapa en stiliserad banner (jfr. bloggen jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Standardmodeller (2026)

| Leverantör | Kvalitet (standard)     | Ekonomi (`--eco`)        |
| --------- | ------------------------ | ------------------------------- |
| OpenAI    | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude    | `claude-sonnet-4-6`            | `claude-haiku-4-5-20251001`                 |
| Mistral   | `mistral-large-latest`           | `mistral-small-latest`                |
| Gemini    | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Rekommendation för långa översättningar** : `--use_gemini` (standard = `gemini-3.1-pro-preview` kvalitet, `--eco` = `gemini-3.1-flash-lite-preview`) tenderar att bättre bevara markdown-strukturen på icke-latinska skript (PL, JA, ZH, AR, HI), särskilt i `--news`-läge där placeholder-trogenhet är viktig. OpenAI förblir standard för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX  
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](LICENSE).

**Artikel översatt från fr till sv med gpt-5.4-mini.**
