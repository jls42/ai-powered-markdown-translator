# AI-gestuurde Markdownvertaler

🌍 [Engels](README-en.md) | [Spaans](README-es.md) | [Chinees](README-zh.md) | [Duits](README-de.md) | [Japans](README-ja.md) | [Koreaans](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italiaans](README-it.md) | [Nederlands](README-nl.md) | [Pools](README-pl.md) | [Portugees](README-pt.md) | [Roemeens](README-ro.md) | [Zweeds](README-sv.md)

Vertaler voor Markdown-bestanden die **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini** gebruikt.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal terwijl het de opmaak, codeblokken en front matter-metadata behoudt.

## Belangrijkste kenmerken

- **Multi-Provider**: Ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini)
- **Modellen 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Economymodus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Enkel bestand**: Optie `--file` om één enkel bestand te vertalen
- **Slimme segmentatie**: Beheer van lange teksten met tokenlimieten per model
- **Behoud van code**: Zowel codeblokken ALS inline-code (`` `...` ``) blijven behouden
- **Bestandsnaam**: Optie `--keep_filename` om de originele naam te behouden
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optionele toevoeging van een notitie aan het einde van het document

## Installatie

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuratie

Maak een bestand `.env` aan in de projectroot of stel de omgevingsvariabelen in :

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

### Vertaal één enkel bestand

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

### Economymodus

Gebruikt snellere en goedkopere modellen (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie | Beschrijving |
|--------|-------------|
| `--file` | Enkel Markdown-bestand om te vertalen |
| `--source_dir` | Bronmap met Markdown-bestanden |
| `--target_dir` | Doelmap voor de vertaalde bestanden |
| `--source_lang` | Brontaal (standaard: `fr`) |
| `--target_lang` | Doeltaal (standaard: `en`) |
| `--model` | Specifiek model om te gebruiken |
| `--eco` | Gebruik zuinige modellen |
| `--use_mistral` | Gebruik de Mistral AI API |
| `--use_claude` | Gebruik de Claude API |
| `--use_gemini` | Gebruik de Gemini API |
| `--force` | Forceer hervertaling |
| `--keep_filename` | Behoud de originele bestandsnaam |
| `--add_translation_note` | Voeg een vertaalnotitie toe |
| `--include_model` | Neem de modelnaam op in het uitvoerbestand |

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard) | Zuinig (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Persoonlijke blog vertaald in 15 talen 

## Auteur

Julien LE SAUX  
E-mail : contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Versie 3. Zie [Licentie](LICENSE).

**Dit document is vertaald van de Franse versie naar de Nederlandse taal met behulp van het model gpt-5-mini. Voor meer informatie over het vertaalproces, raadpleeg https://gitlab.com/jls42/ai-powered-markdown-translator**

