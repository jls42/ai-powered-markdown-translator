# Traduttore Markdown alimentato dall'AI

🌍 [Inglese](README-en.md) | [Spagnolo](README-es.md) | [Cinese](README-zh.md) | [Tedesco](README-de.md) | [Giapponese](README-ja.md) | [Coreano](README-ko.md) | [Arabo](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Olandese](README-nl.md) | [Polacco](README-pl.md) | [Portoghese](README-pt.md) | [Rumeno](README-ro.md) | [Svedese](README-sv.md)

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Questo script Python traduce file Markdown da una lingua di origine a una lingua di destinazione preservando il formato, i blocchi di codice e i metadati del front matter.

## Caratteristiche principali

- **Multi-Provider**: Supporto di 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modelli 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Modalità Economica**: Opzione `--eco` per utilizzare modelli più veloci e meno costosi
- **File singolo**: Opzione `--file` per tradurre un singolo file
- **Segmentazione intelligente**: Gestione di testi lunghi con limiti di token per modello
- **Preservazione del codice**: I blocchi di codice E il codice inline (`` `...` ``) sono preservati
- **Nome del file**: Opzione `--keep_filename` per conservare il nome originale
- **Configurazione .env**: Supporto del file `.env` per le chiavi API
- **Nota di traduzione**: Aggiunta opzionale di una nota alla fine del documento

## Installazione

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configurazione

Crea un file `.env` nella radice del progetto o imposta le variabili d'ambiente :

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

### Tradurre un singolo file

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tradurre una directory

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
| `--source_dir` | Directory di origine contenente i file Markdown |
| `--target_dir` | Directory di output per i file tradotti |
| `--source_lang` | Lingua sorgente (predefinita: `fr`) |
| `--target_lang` | Lingua di destinazione (predefinita: `en`) |
| `--model` | Modello specifico da utilizzare |
| `--eco` | Utilizzare i modelli economici |
| `--use_mistral` | Utilizzare l'API Mistral AI |
| `--use_claude` | Utilizzare l'API Claude |
| `--use_gemini` | Utilizzare l'API Gemini |
| `--force` | Forzare la retraduzione |
| `--keep_filename` | Conservare il nome file originale |
| `--add_translation_note` | Aggiungere una nota di traduzione |
| `--include_model` | Includere il nome del modello nel file di output |

### Modelli predefiniti (2026)

| Fornitore | Qualità (predefinita) | Economico (`--eco`) |
|----------|------------------|----------------------|
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

GNU GENERAL PUBLIC LICENSE Versione 3. Vedi [LICENZA](LICENSE).

**Questo documento è stato tradotto dalla versione fr alla lingua it utilizzando il modello gpt-5-mini. Per ulteriori informazioni sul processo di traduzione, consultare https://gitlab.com/jls42/ai-powered-markdown-translator**

