# Traduttore di Markdown potenziato dall'IA

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Questo script Python traduce file Markdown da una lingua sorgente a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche principali

- **Multi-provider**: supporto di 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modelli 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Modalità economica**: opzione `--eco` per utilizzare modelli più veloci e meno costosi
- **File singolo**: opzione `--file` per tradurre un solo file
- **Segmentazione intelligente**: gestione dei testi lunghi con limiti di token per modello
- **Preservazione del codice**: i blocchi di codice non vengono tradotti
- **Nota di traduzione**: aggiunta opzionale di una nota alla fine del documento

## Installazione

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configurazione

Definisci la variabile d'ambiente per l'API che desideri utilizzare :

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Utilizzo

### Tradurre un file singolo

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tradurre un directory

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

### Modalità economica

Utilizza modelli più veloci e meno costosi (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Opzione | Descrizione |
|--------|-------------|
| `--file` | File Markdown singolo da tradurre |
| `--source_dir` | Directory sorgente contenente i file Markdown |
| `--target_dir` | Directory di destinazione per i file tradotti |
| `--source_lang` | Lingua sorgente (predefinita: `fr`) |
| `--target_lang` | Lingua di destinazione (predefinita: `en`) |
| `--model` | Modello specifico da utilizzare |
| `--eco` | Usare i modelli economici |
| `--use_mistral` | Usare l'API Mistral AI |
| `--use_claude` | Usare l'API Claude |
| `--use_gemini` | Usare l'API Gemini |
| `--force` | Forzare la ritraduzione |
| `--add_translation_note` | Aggiungere una nota di traduzione |

### Modelli predefiniti (2026)

| Provider | Qualità (predefinita) | Economico (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Autore

Julien LE SAUX
Email : contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Versione 3. Vedi [LICENSE](LICENSE).