# AI-aangedreven Markdown-vertaler

🌍 [Frans](README.md) | [Engels](README-en.md) | [Spaans](README-es.md) | [Chinees](README-zh.md) | [Duits](README-de.md) | [Japans](README-ja.md) | [Koreaans](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italiaans](README-it.md) | [Nederlands](README-nl.md) | [Pools](README-pl.md) | [Portugees](README-pt.md) | [Roemeens](README-ro.md) | [Zweeds](README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

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

Markdown-bestandsvertaler met **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini**.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, terwijl de opmaak, codeblokken en front-mattermetadata behouden blijven.

## Belangrijkste kenmerken

- **Multi-Provider**: Ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini)
- **Modellen 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Economische modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Enkel bestand**: Optie `--file` om één enkel bestand te vertalen
- **Intelligente segmentatie**: Verwerking van lange teksten met tokenlimieten per model
- **Codebehoud**: Codeblokken EN inline code (`` `...` ``) blijven behouden
- **Bestandsnaam**: Optie `--keep_filename` om de oorspronkelijke naam te behouden
- **Nieuwsmodus**: Optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te beheren
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optioneel toevoegen van een notitie aan het einde van het document

## Installatie

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kwaliteitstools (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat slecht opgemaakte, kwetsbare of geheimen bevattende code wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (geleidelijke typecontrole), Opengrep (SAST), pip-audit (CVE-afhankelijkheden), unittest. Zie sectie `CLAUDE.md` _Quality / pre-commit_ voor details.

## Configuratie

Maak een bestand `.env` aan in de projectroot of definieer de omgevingsvariabelen:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Gebruik

### Een enkel bestand vertalen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Een map vertalen

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

### Economische modus

Gebruikt snellere en goedkopere modellen (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie                   | Beschrijving                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Eén Markdown-bestand om te vertalen                                       |
| `--source_dir`           | Brondirectory met de Markdown-bestanden                        |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                          |
| `--source_lang`          | Brontaal (standaard: `fr`)                                             |
| `--target_lang`          | Doeltaal (standaard: `en`)                                              |
| `--model`                | Specifiek model om te gebruiken                                             |
| `--eco`                  | Gebruik de economische modellen                                         |
| `--use_mistral`          | Gebruik de Mistral AI-API                                                |
| `--use_claude`           | Gebruik de Claude-API                                                    |
| `--use_gemini`           | Gebruik de Gemini-API                                                  |
| `--force`                | Vertaling opnieuw afdwingen                                                  |
| `--keep_filename`        | Oorspronkelijke bestandsnaam behouden                                     |
| `--news`                 | Nieuwsmode: beschermt EN-citaten, beheert vlaggen per taal |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                           |
| `--include_model`        | De modelnaam opnemen in het uitvoerbestand                       |

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard)         | Economisch (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Aanbeveling voor langvormvertalingen**: `--use_gemini` (standaard = `gemini-3.1-pro-preview` kwaliteit, `--eco` = `gemini-3.1-flash-lite-preview`) heeft de neiging de markdown-structuur beter te behouden op niet-Latijnse scripts (PL, JA, ZH, AR, HI), vooral in `--news`-modus waar de betrouwbaarheid van placeholders belangrijk is. OpenAI blijft de standaard voor achterwaartse compatibiliteit.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail : contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Versie 3. Zie [LICENSE](LICENSE).

**Dit document is vertaald van de fr-versie naar de nl-taal met behulp van het model gpt-5.4-mini. Voor meer informatie over het vertaalproces, raadpleeg https://github.com/jls42/ai-powered-markdown-translator**
