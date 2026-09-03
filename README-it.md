# Traduttore di Markdown basato sull'AI

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Righe duplicate (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Debito tecnico"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Righe di codice"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Badge Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** e **Grok (xAI)** — tramite API, oppure utilizzando la quota di un abbonamento ChatGPT (Codex) o Grok, senza fatturazione a consumo.

Questo script Python traduce file Markdown da una lingua di origine a una lingua di destinazione, preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche principali

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI su abbonamento, senza fatturazione a consumo — Codex (ChatGPT) e Grok
- **Modelli 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modalità economica**: opzione `--eco` per utilizzare modelli più rapidi e meno costosi
- **File singolo**: opzione `--file` per tradurre un solo file
- **Segmentazione intelligente**: gestione dei testi lunghi con limiti di token per modello
- **Conservazione del codice**: i blocchi di codice E il codice inline (`` `...` ``) vengono preservati
- **Nome file**: opzione `--keep_filename` per conservare il nome originale
- **Modalità News**: opzione `--news` per proteggere le citazioni inglesi e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: supporto per il file `.env` per le chiavi API
- **Nota di traduzione**: aggiunta facoltativa di una nota alla fine del documento

## Installazione

### Per utilizzare lo strumento

```bash
pip install ai-powered-markdown-translator
```

Il comando `aipmt` è quindi disponibile ovunque. Se la directory degli script
Python non è presente nel tuo `PATH`, `python -m aipmt` fa esattamente la stessa
cosa. Python 3.10 o versioni successive.

Per un'installazione isolata dal resto dei tuoi pacchetti:

```bash
pipx install ai-powered-markdown-translator
```

### Per contribuire al progetto

Il repository clonato rimane necessario per lo sviluppo: è lì che si trovano i test,
le 28 traduzioni e tutti gli strumenti per la qualità.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` è un **lock completamente bloccato**, riproduzione esatta dell'
ambiente testato. I vincoli pubblicati in `pyproject.toml` sono
volutamente più ampi: non impongono nulla agli altri pacchetti.

### Strumenti per la qualità (facoltativi ma consigliati)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire il commit di codice non formattato correttamente, vulnerabile o contenente un segreto. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (dipendenze CVE), unittest. Consulta la sezione _Quality / pre-commit_ di `CLAUDE.md` per i dettagli.

## Configurazione

Le chiavi vengono cercate in **tre posizioni**, dalla più prioritaria alla meno prioritaria.
Ognuna si limita a colmare ciò che la precedente lascia vuoto.

|     | Dove                                            | Per cosa                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabili d'ambiente                     | CI, container, deroga puntuale |
| 2   | `.env` della directory corrente (o di un genitore) | una chiave specifica per un progetto            |
| 3   | `~/.config/aipmt/.env`                        | **installato una volta, vale ovunque**   |

La soluzione più semplice dopo un `pip install` è la terza:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

Questo file segue `XDG_CONFIG_HOME` quando la variabile indica un percorso assoluto
(altrimenti viene ignorata, come prescritto dalla specifica), e `%APPDATA%`
su Windows.

La seconda rimane utile quando un repository ha una propria chiave: un `.env` nella sua radice
ha allora la precedenza sulla configurazione utente, senza modificarla. E una
variabile già definita nell'ambiente ha la precedenza su entrambe:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Se non viene trovata alcuna chiave, il comando non visualizza alcuna traccia di chiamata:
elenca le tre posizioni con il relativo percorso esatto.

`GEMINI_API_KEY` è accettato come alternativa a `GOOGLE_API_KEY` (convenzione AI
Studio). Variabili facoltative: `XAI_BASE_URL` (endpoint xAI, valore predefinito
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondi per chiamata Anthropic, valore predefinito
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
e `GROK_TRANSLATE_SANDBOX` (consulta la sezione Grok CLI). Per
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` e
`REGEN_JOB_TIMEOUT` (limite per job, valore predefinito 600 s).

## Utilizzo

### Tradurre un singolo file

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tradurre una directory

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Tradurre con il proprio abbonamento ChatGPT (`--use_codex`)

Questo provider non utilizza alcuna chiave API: controlla il CLI Codex ufficiale in modalità
non interattiva, quindi la traduzione viene conteggiata nella quota dell'abbonamento
ChatGPT (Plus, Pro, Business…) già pagato. È l'unico percorso documentato da
OpenAI per questo utilizzo — i token di `~/.codex/auth.json` non autenticano
le chiamate all'API Platform e, del resto, non vengono mai letti da questo script.

**Prerequisiti:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Il binario viene cercato in quest'ordine: la variabile `CODEX_BIN`, il `PATH`,
poi il pacchetto Python `openai-codex-cli-bin`. Quest'ultimo non è volutamente
in `requirements.txt`: pesa circa 250 MB, che verrebbero imposti a tutti gli
utenti per un provider facoltativo.

**Da sapere:**

- **Non viene utilizzata alcuna chiave API.** `OPENAI_API_KEY` e `CODEX_API_KEY` vengono
  rimossi dall'ambiente del sottoprocesso, garantendo che una chiave presente in
  `.env` non faccia mai passare la traduzione alla fatturazione
  a consumo.
- **Un segmento = un «messaggio locale»** della finestra di 5 ore del piano.
  Utilizza `--eco` (modello `gpt-5.6-luna`, 250-2.000 messaggi/5 h su Plus)
  invece del modello di qualità (`gpt-5.6-sol`, 10-100 messaggi/5 h).
- **Più lento** di una chiamata API: considera circa 45 s per un README completo, contro
  pochi secondi in diretta.
- **Rifiutato in CI** (`CI` o `GITHUB_ACTIONS` definito): l'autenticazione tramite
  abbonamento non è prevista per un runner condiviso e OpenAI sconsiglia questo
  workflow sui repository pubblici. Utilizza una chiave API per questo percorso.
- Variabili d'ambiente: `CODEX_BIN` (percorso esplicito del binario) e
  `CODEX_TIMEOUT` (secondi per segmento, valore predefinito `600`).

### Tradurre con il proprio abbonamento Grok (`--use_grok_cli`)

Stesso principio di `--use_codex`, con il CLI ufficiale **Grok Build**:
la traduzione viene conteggiata nell'abbonamento Grok (SuperGrok / X Premium+) invece
di essere fatturata a token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — da leggere prima dell'uso.** Questo provider è strutturalmente **più
debole** di `--use_codex` e ciò è intenzionale:

- Codex funziona in `--sandbox read-only`, una frontiera imposta dal sistema.
- Il sandbox di Grok **non può essere applicato** su molti sistemi Linux recenti:
  AppArmor blocca gli user namespace non privilegiati da Ubuntu 24.04 e la deny-list dei socket
  del runtime dei container fallisce se `/run/podman` è `0700`. Ma un profilo
  **integrato** che non può essere applicato si avvia **silenziosamente senza confinamento**.
- Lo script quindi non richiede alcun profilo per impostazione predefinita e **non ricade mai
  silenziosamente**: visualizza un avvertimento. Il confinamento si basa sulle regole
  `--deny` del CLI (tra cui il catch-all `*`), l'unico livello misurato
  _fail-closed_ — una regola sconosciuta fa rifiutare l'avvio invece di rimuovere la
  protezione senza comunicarlo.
- Per **richiedere** il sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`. L'avvio
  fallirà se la macchina non può rispettarlo, che è il comportamento voluto.

**Quota**: il pool Grok è **settimanale e condiviso** con Chat, Imagine e
Voice, e nessun comando consente di leggerlo. Un'elaborazione batch può quindi
consumare il tuo utilizzo conversazionale senza che nulla lo segnali — da qui una
concorrenza limitata a 2 e un avvertimento in `regen_translations.sh`.

Altre variabili: `GROK_BIN` (percorso del binario), `GROK_TIMEOUT` (valore predefinito 900 s).

Per rigenerare le 28 traduzioni:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Modalità economica

Utilizza modelli più rapidi e meno costosi (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Opzione                   | Descrizione                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Singolo file Markdown da tradurre                                       |
| `--source_dir`           | Directory sorgente contenente i file Markdown                        |
| `--target_dir`           | Directory di output per i file tradotti                          |
| `--source_lang`          | Lingua di origine (predefinita: `fr`)                                             |
| `--target_lang`          | Lingua di destinazione (predefinita: `en`)                                              |
| `--model`                | Modello specifico da utilizzare                                             |
| `--eco`                  | Utilizzare i modelli economici                                         |
| `--use_mistral`          | Utilizzare l'API Mistral AI                                                |
| `--use_claude`           | Utilizzare l'API Claude                                                    |
| `--use_gemini`           | Utilizzare l'API Gemini                                                    |
| `--use_codex`            | Utilizzare il CLI Codex sulla quota dell'abbonamento ChatGPT               |
| `--use_grok`             | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utilizzare il CLI Grok sulla quota dell'abbonamento Grok                   |
| `--force`                | Forzare la ritraduzione                                                  |
| `--keep_filename`        | Conservare il nome file originale                                     |
| `--news`                 | Modalità notizie: protegge le citazioni EN e gestisce le bandiere per lingua |
| `--add_translation_note` | Aggiungere una nota di traduzione                                           |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinita) o `both`                |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) o `marker`       |
| `--include_model`        | Includere il nome del modello nel file di output                       |
| `--reasoning_effort`     | Sforzo di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

> **I sei flag dei provider sono reciprocamente esclusivi.** In precedenza combinarne due
> era accettato silenziosamente e la risoluzione avveniva a favore del primo testato: una
> traduzione richiesta sulla quota dell'abbonamento (`--use_codex`, `--use_grok_cli`)
> poteva quindi passare alla fatturazione a consumo senza alcun avvertimento.
> `argparse` rifiuta ora la combinazione.

### Nota di traduzione: posizioni e formati

Con `--add_translation_note`, il translator può collocare la nota in alto, in basso o in entrambe le posizioni, e renderla in formato testo semplice (retrocompatibile) oppure in formato `marker` utilizzabile da un plugin Markdown.

**Posizione** (`--note_position`):

- `bottom` (predefinita): nota alla fine del file, come in passato.
- `top`: nota inserita **dopo il frontmatter YAML** (sicurezza per Astro Content Collections, gray-matter, ecc.).
- `both`: nota inserita IN ALTO E IN BASSO (una sola chiamata LLM, contenuto riutilizzato per entrambe le posizioni).

**Formato** (`--note_format`):

- `legacy` (predefinito): paragrafo in grassetto `**...**` — comportamento strettamente identico a v1.8, byte-for-byte. Compatibile con Hugo, GitHub, GitLab e qualsiasi renderer Markdown.
- `marker`: definizione Markdown invisibile di un link reference (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguita da un blockquote in grassetto. Leggibile nativamente su GitHub/GitLab e utilizzabile in fase di build da un plugin remark lato Astro per produrre un banner stilizzato (cfr. blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Modelli predefiniti (2026)

| Provider | Qualità (predefinita)       | Economico (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Raccomandazione per le traduzioni long-form**: `--use_gemini` (predefinito = `gemini-3.7-flash`) preserva fedelmente la struttura Markdown negli script non latini (PL, JA, ZH, AR, HI), anche in modalità `--news` in cui la fedeltà dei placeholder è importante. Misurato su questo README tradotto in giapponese: struttura identica a `gemini-3.1-pro-preview` (21 liste, 18 blocchi di codice, 13 link HTML, 13 immagini, tutti gli URL preservati) con una latenza circa 6 volte inferiore. OpenAI rimane il valore predefinito per la retrocompatibilità.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedi [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articolo tradotto dal francese all’italiano con gpt-5.6-luna.**
