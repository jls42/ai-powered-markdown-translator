# Traduttore di Markdown AI-Powered

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Questo script Python traduce file Markdown da una lingua sorgente a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche Principali

- **Multi-Provider**: Supporto di 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modelli 2026**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **Modalità Economica**: Opzione `--eco` per utilizzare modelli più veloci e meno costosi
- **File Singolo**: Opzione `--file` per tradurre un singolo file
- **Segmentazione Intelligente**: Gestione dei testi lunghi con limiti di token per modello
- **Preservazione del Codice**: I blocchi di codice E il codice inline (`` `...` ``) sono preservati
- **Nome del File**: Opzione `--keep_filename` per conservare il nome originale
- **Modalità News**: Opzione `--news` per proteggere le citazioni inglesi e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: Supporto del file `.env` per le chiavi API
- **Nota di Traduzione**: Aggiunta opzionale di una nota alla fine del documento

## Installazione

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configurazione

Create un file `.env` alla radice del progetto oppure definite le variabili d'ambiente :

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Utilizzo

### Tradurre un file singolo

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tradurre una directory

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

### Modalità economica

Utilizza modelli più veloci e meno costosi (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Option | Description |
|--------|-------------|
| `--file` | File Markdown singolo da tradurre |
| `--source_dir` | Directory sorgente contenente i file Markdown |
| `--target_dir` | Directory di output per i file tradotti |
| `--source_lang` | Lingua sorgente (predefinita: `fr`) |
| `--target_lang` | Lingua di destinazione (predefinita: `en`) |
| `--model` | Modello specifico da utilizzare |
| `--eco` | Utilizzare i modelli economici |
| `--use_mistral` | Utilizzare l'API Mistral AI |
| `--use_claude` | Utilizzare l'API Claude |
| `--use_gemini` | Utilizzare l'API Gemini |
| `--force` | Forzare la ri-traduzione |
| `--keep_filename` | Conservare il nome del file originale |
| `--news` | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua |
| `--add_translation_note` | Aggiungere una nota di traduzione |
| `--include_model` | Includere il nome del modello nel file di output |

### Modelli predefiniti (2026)

| Provider | Qualità (predefinita) | Economica (`--eco`) |
|----------|----------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email : contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](LICENSE).