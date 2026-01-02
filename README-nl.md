# AI-aangedreven Markdown-vertaler

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Vertaler van Markdown-bestanden die **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini** gebruikt.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, terwijl het de opmaak, codeblokken en front matter-metagegevens behoudt.

## Belangrijkste Kenmerken

- **Multi-provider**: Ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini)
- **Modellen 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Economische modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Eén enkel bestand**: Optie `--file` om één enkel bestand te vertalen
- **Intelligente segmentatie**: Beheer van lange teksten met tokenlimieten per model
- **Codebehoud**: Codeblokken worden niet vertaald
- **Vertaalnotitie**: Optioneel toevoegen van een notitie aan het einde van het document

## Installatie

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuratie

Stel de omgevingsvariabele in voor de API die u wilt gebruiken:

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Gebruik

### Een enkel bestand vertalen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Een map vertalen

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

### Economische modus

Gebruikt snellere en goedkopere modellen (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie | Beschrijving |
|--------|--------------|
| `--file` | Een enkel Markdown-bestand om te vertalen |
| `--source_dir` | Bronmap met de Markdown-bestanden |
| `--target_dir` | Doelmap voor de vertaalde bestanden |
| `--source_lang` | Brontaal (standaard: `fr`) |
| `--target_lang` | Doeltaal (standaard: `en`) |
| `--model` | Specifiek te gebruiken model |
| `--eco` | Economische modellen gebruiken |
| `--use_mistral` | De Mistral AI-API gebruiken |
| `--use_claude` | De Claude-API gebruiken |
| `--use_gemini` | De Gemini-API gebruiken |
| `--force` | Opnieuw vertalen forceren |
| `--add_translation_note` | Een vertaalnotitie toevoegen |

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard) | Economisch (`--eco`) |
|----------|------------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Auteur

Julien LE SAUX
E-mail : contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Versie 3. Zie [LICENSE](LICENSE).