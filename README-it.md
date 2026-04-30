# Traduttore di Markdown AI-Powered

🌍 [Francese](README.md) | [Inglese](README-en.md) | [Spagnolo](README-es.md) | [Cinese](README-zh.md) | [Tedesco](README-de.md) | [Giapponese](README-ja.md) | [Coreano](README-ko.md) | [Arabo](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Olandese](README-nl.md) | [Polacco](README-pl.md) | [Portoghese](README-pt.md) | [Romeno](README-ro.md) | [Svedese](README-sv.md)

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Questo script Python traduce file Markdown da una lingua sorgente a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche Principali

- **Multi-Provider**: Supporto di 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modelli 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Modalità Economica**: Opzione `--eco` per usare modelli più veloci e meno costosi
- **File Singolo**: Opzione `--file` per tradurre un singolo file
- **Segmentazione Intelligente**: Gestione di testi lunghi con limiti di token per modello
- **Preservazione del Codice**: I blocchi di codice E il codice inline (`` `...` ``) sono preservati
- **Nome del File**: Opzione `--keep_filename` per mantenere il nome originale
- **Modalità News**: Opzione `--news` per proteggere le citazioni in inglese e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: Supporto del file `.env` per le chiavi API
- **Nota di Traduzione**: Aggiunta opzionale di una nota alla fine del documento

## Installazione

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Strumenti di qualità (opzionale ma consigliato)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire il commit di codice mal formattato, vulnerabile o contenente un segreto. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (CVE deps), unittest. Vedere la sezione `CLAUDE.md` _Quality / pre-commit_ per i dettagli.

## Configurazione

Create un file `.env` nella radice del progetto oppure definite le variabili d'ambiente:

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
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Modalità economica

Usa modelli più veloci e meno costosi (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Opzione                  | Descrizione                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | File Markdown singolo da tradurre                                       |
| `--source_dir`           | Directory sorgente contenente i file Markdown                        |
| `--target_dir`           | Directory di output per i file tradotti                          |
| `--source_lang`          | Lingua sorgente (predefinita: `fr`)                                             |
| `--target_lang`          | Lingua di destinazione (predefinita: `en`)                                              |
| `--model`                | Modello specifico da usare                                             |
| `--eco`                  | Usare i modelli economici                                         |
| `--use_mistral`          | Usare l'API Mistral AI                                                |
| `--use_claude`           | Usare l'API Claude                                                    |
| `--use_gemini`           | Usare l'API Gemini                                                    |
| `--force`                | Forzare la ritraduzione                                                  |
| `--keep_filename`        | Mantenere il nome originale del file                                     |
| `--news`                 | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua |
| `--add_translation_note` | Aggiungere una nota di traduzione                                           |
| `--include_model`        | Includere il nome del modello nel file di output                       |

### Modelli predefiniti (2026)

| Provider | Qualità (predefinita)         | Economica (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Raccomandazione per traduzioni long-form**: `--use_gemini` (predefinita = `gemini-3.1-pro-preview` qualità, `--eco` = `gemini-3-flash-preview`) tende a preservare meglio la struttura markdown su script non latini (PL, JA, ZH, AR, HI), in particolare in modalità `--news` dove la fedeltà dei placeholder conta. OpenAI resta il predefinito per la retrocompatibilità.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email : contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](LICENSE).

**Questo documento è stato tradotto dalla versione fr nella lingua it utilizzando il modello gpt-5.4-mini. Per ulteriori informazioni sul processo di traduzione, consulta https://gitlab.com/jls42/ai-powered-markdown-translator**

