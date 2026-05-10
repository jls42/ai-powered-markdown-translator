# Traduttore Markdown potenziato dall'IA

🌍 [Francese](README.md) | [Inglese](README-en.md) | [Spagnolo](README-es.md) | [Cinese](README-zh.md) | [Tedesco](README-de.md) | [Giapponese](README-ja.md) | [Coreano](README-ko.md) | [Arabo](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Olandese](README-nl.md) | [Polacco](README-pl.md) | [Portoghese](README-pt.md) | [Romeno](README-ro.md) | [Svedese](README-sv.md)

<h4 align="center">📊 Qualità del codice</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Stato del Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Valutazione della sicurezza"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Valutazione dell'affidabilità"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Valutazione della manutenibilità"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Copertura"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilità"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bug"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Linee duplicate (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Debito tecnico"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linee di codice"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Badge Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Questo script Python traduce file Markdown da una lingua sorgente a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche principali

- **Multi-Provider**: supporto per 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modelli 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Modalità economica**: opzione `--eco` per usare modelli più veloci e meno costosi
- **File singolo**: opzione `--file` per tradurre un singolo file
- **Segmentazione intelligente**: gestione di testi lunghi con limiti di token per modello
- **Conservazione del codice**: i blocchi di codice E il codice inline (`` `...` ``) sono preservati
- **Nome del file**: opzione `--keep_filename` per mantenere il nome originale
- **Modalità News**: opzione `--news` per proteggere le citazioni in inglese e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: supporto del file `.env` per le chiavi API
- **Nota di traduzione**: aggiunta opzionale di una nota alla fine del documento

## Installazione

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Strumentazione qualità (opzionale ma consigliata)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire di fare commit di codice mal formattato, vulnerabile o contenente segreti. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (CVE deps), unittest. Vedi sezione `CLAUDE.md` _Qualità / pre-commit_ per i dettagli.

## Configurazione

Crea un file `.env` alla radice del progetto oppure definisci le variabili d'ambiente:

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

Utilizza modelli più veloci e meno costosi (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Opzione                   | Descrizione                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Singolo file Markdown da tradurre                                       |
| `--source_dir`           | Directory sorgente contenente i file Markdown                            |
| `--target_dir`           | Directory di output per i file tradotti                                 |
| `--source_lang`          | Lingua sorgente (predefinita: `fr`)                                             |
| `--target_lang`          | Lingua di destinazione (predefinita: `en`)                                              |
| `--model`                | Modello specifico da usare                                               |
| `--eco`                  | Usare i modelli economici                                               |
| `--use_mistral`          | Usare l'API Mistral AI                                                  |
| `--use_claude`           | Usare l'API Claude                                                     |
| `--use_gemini`           | Usare l'API Gemini                                                     |
| `--force`                | Forzare la ritraduzione                                                 |
| `--keep_filename`        | Mantenere il nome file originale                                        |
| `--news`                 | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua |
| `--add_translation_note` | Aggiungere una nota di traduzione                                           |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinito), oppure `both`                |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) oppure `marker`       |
| `--include_model`        | Includere il nome del modello nel file di output                       |

### Nota di traduzione: posizioni e formati

Con `--add_translation_note`, il traduttore può posizionare la nota in alto, in basso o in entrambi i punti, e renderla sia in formato testo semplice (retrocompatibile) sia in formato `marker` consumabile da un plugin Markdown.

**Posizione** (`--note_position`) :

- `bottom` (predefinito) : nota alla fine del file, come storicamente.
- `top` : nota inserita **dopo il frontmatter YAML** (sicurezza Astro Content Collections, gray-matter, ecc.).
- `both` : nota inserita in alto E in basso (un'unica chiamata LLM, contenuto riutilizzato per entrambi i posizionamenti).

**Formato** (`--note_format`) :

- `legacy` (predefinito) : paragrafo in grassetto `**...**` — comportamento rigorosamente identico alla v1.8, byte per byte. Compatibile con Hugo, GitHub, GitLab e qualsiasi renderer Markdown.
- `marker` : definizione invisibile di riferimento link Markdown `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` seguita da un blockquote in grassetto. Leggibile nativamente su GitHub/GitLab e sfruttabile in fase di build da un plugin remark lato Astro per produrre un banner stilizzato (cf. blog jls42.org).

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

### Modelli predefiniti (2026)

| Provider | Qualità (predefinita)         | Economico (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Raccomandazione per traduzioni long-form** : `--use_gemini` (predefinito = `gemini-3.1-pro-preview` qualità, `--eco` = `gemini-3.1-flash-lite-preview`) tende a preservare meglio la struttura markdown su script non latini (PL, JA, ZH, AR, HI), in particolare in modalità `--news` dove conta la fedeltà dei placeholder. OpenAI rimane il predefinito per la retrocompatibilità.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Versione 3. Vedere [LICENSE](LICENSE).

**Articolo tradotto dal fr all’it con gpt-5.4-mini.**
