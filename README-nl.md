# AI-aangedreven Markdown-vertaler

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Markdown-bestandsvertaler met **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini**.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, terwijl de opmaak, codeblokken en front matter-metagegevens behouden blijven.

## Belangrijkste kenmerken

- **Multi-Provider**: Ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini)
- **Modellen 2026**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **Economische modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Enkel bestand**: Optie `--file` om één enkel bestand te vertalen
- **Intelligente segmentatie**: Verwerking van lange teksten met tokenlimieten per model
- **Behoud van code**: Codeblokken EN inline code (`` `...` ``) blijven behouden
- **Bestandsnaam**: Optie `--keep_filename` om de originele naam te behouden
- **Nieuwsmodus**: Optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te beheren
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optionele toevoeging van een notitie aan het einde van het document

## Installatie

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuratie

Maak een bestand `.env` aan in de hoofdmap van het project of definieer de omgevingsvariabelen:

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

### Eén bestand vertalen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Een map vertalen

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

### Economische modus

Gebruikt snellere en goedkopere modellen (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie | Beschrijving |
|--------|-------------|
| `--file` | Enkel Markdown-bestand om te vertalen |
| `--source_dir` | Bronmap met Markdown-bestanden |
| `--target_dir` | Uitvoermap voor vertaalde bestanden |
| `--source_lang` | Brontaal (standaard: `fr`) |
| `--target_lang` | Doeltaal (standaard: `en`) |
| `--model` | Specifiek model om te gebruiken |
| `--eco` | Economische modellen gebruiken |
| `--use_mistral` | De Mistral AI-API gebruiken |
| `--use_claude` | De Claude-API gebruiken |
| `--use_gemini` | De Gemini-API gebruiken |
| `--force` | Hertoekennen forceren |
| `--keep_filename` | De originele bestandsnaam behouden |
| `--news` | Nieuwsmodus: beschermt EN-citaten, beheert vlaggen per taal |
| `--add_translation_note` | Een vertaalnotitie toevoegen |
| `--include_model` | De modelnaam in het uitvoerbestand opnemen |

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard) | Economisch (`--eco`) |
|----------|----------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
Email : contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE versie 3. Zie [LICENSE](LICENSE).