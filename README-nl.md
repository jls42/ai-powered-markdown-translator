# AI-aangedreven Markdown-vertaler

🌍 [Frans](README.md) | [Engels](README-en.md) | [Spaans](README-es.md) | [Chinees](README-zh.md) | [Duits](README-de.md) | [Japans](README-ja.md) | [Koreaans](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italiaans](README-it.md) | [Nederlands](README-nl.md) | [Pools](README-pl.md) | [Portugees](README-pt.md) | [Roemeens](README-ro.md) | [Zweeds](README-sv.md)

Markdown-bestandsvertaler met **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini**.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, terwijl de opmaak, codeblokken en front matter-metagegevens behouden blijven.

## Belangrijkste kenmerken

- **Multi-provider**: ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini)
- **Modellen 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Zuinigheidsmodus**: optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Enkel bestand**: optie `--file` om één enkel bestand te vertalen
- **Intelligente segmentatie**: verwerking van lange teksten met tokenlimieten per model
- **Behoud van code**: codeblokken EN inline code (`` `...` ``) worden behouden
- **Bestandsnaam**: optie `--keep_filename` om de oorspronkelijke naam te behouden
- **Nieuwsmodus**: optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te beheren
- **.env-configuratie**: ondersteuning voor bestand `.env` voor API-sleutels
- **Vertaalnotitie**: optionele toevoeging van een notitie aan het einde van het document

## Installatie

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kwaliteitsgereedschap (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat foutgeformatteerde, kwetsbare of geheimen bevattende code wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (progressieve typcontrole), Opengrep (SAST), pip-audit (CVE-afhankelijkheden), unittest. Zie `CLAUDE.md` sectie _Quality / pre-commit_ voor details.

## Configuratie

Maak een bestand `.env` aan in de root van het project of definieer de omgevingsvariabelen:

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

### Zuinigheidsmodus

Gebruikt snellere en goedkopere modellen (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie                   | Beschrijving                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Enkeld Markdown-bestand om te vertalen                                       |
| `--source_dir`           | Bronmap met de Markdown-bestanden                        |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                          |
| `--source_lang`          | Brontaal (standaard: `fr`)                                             |
| `--target_lang`          | Doeltaal (standaard: `en`)                                              |
| `--model`                | Specifiek te gebruiken model                                             |
| `--eco`                  | Gebruik de zuinige modellen                                         |
| `--use_mistral`          | Gebruik de Mistral AI-API                                                |
| `--use_claude`           | Gebruik de Claude-API                                                    |
| `--use_gemini`           | Gebruik de Gemini-API                                                    |
| `--force`                | Vertaling opnieuw forceren                                                  |
| `--keep_filename`        | Oorspronkelijke bestandsnaam behouden                                     |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten, beheert vlaggen per taal |
| `--add_translation_note` | Vertaalnotitie toevoegen                                           |
| `--include_model`        | Modelnaam opnemen in het uitvoerbestand                       |

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard)         | Zuinigheid (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Aanbeveling voor lange vertalingen**: `--use_gemini` (standaard = `gemini-3.1-pro-preview` kwaliteit, `--eco` = `gemini-3-flash-preview`) heeft de neiging de markdown-structuur beter te behouden bij niet-Latijnse scripts (PL, JA, ZH, AR, HI), vooral in `--news`-modus waar de nauwkeurigheid van placeholders telt. OpenAI blijft de standaard voor achterwaartse compatibiliteit.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail : contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE versie 3. Zie [LICENSE](LICENSE).

**Dit document is vertaald van de fr-versie naar de nl-taal met behulp van het model gpt-5.4-mini. Voor meer informatie over het vertaalproces, zie https://gitlab.com/jls42/ai-powered-markdown-translator**

