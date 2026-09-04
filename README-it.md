# Traduttore di Markdown basato su AI

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

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** e **Grok (xAI)** — tramite API, sul quota di un abbonamento ChatGPT (Codex) o Grok senza fatturazione a consumo, oppure tramite **OpenCode**, l'agente open source, verso il provider desiderato: modello locale (Ollama), gratuito, in abbonamento (GitHub Copilot…) o con chiave.

Questo script Python traduce file Markdown da una lingua sorgente a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche principali

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI in abbonamento, senza fatturazione a consumo — Codex (ChatGPT) e Grok — + OpenCode (open source, MIT) verso qualsiasi provider configurato in OpenCode, incluso un modello locale
- **Modelli 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modalità economica**: Opzione `--eco` per utilizzare modelli più rapidi e meno costosi
- **File singolo**: Opzione `--file` per tradurre un solo file
- **Segmentazione intelligente**: Gestione dei testi lunghi con limiti di token per modello
- **Preservazione del codice**: I blocchi di codice E il codice inline (`` `...` ``) vengono preservati
- **Nome del file**: Opzione `--keep_filename` per mantenere il nome originale
- **Modalità News**: Opzione `--news` per proteggere le citazioni inglesi e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: Supporto del file `.env` per le chiavi API
- **Nota di traduzione**: Aggiunta opzionale di una nota alla fine del documento

## Installazione

### Per utilizzare lo strumento

```bash
pip install ai-powered-markdown-translator
```

Il comando `aipmt` è quindi disponibile ovunque. Se la directory degli script
di Python non si trova nel `PATH`, `python -m aipmt` fa esattamente la stessa
cosa. Python 3.10 o versione più recente.

Per un'installazione isolata dal resto dei pacchetti:

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

`requirements.txt` è un **lock completamente bloccato**, riproduzione esatta
dell'ambiente testato. I vincoli pubblicati in `pyproject.toml` sono
volutamente più ampi: non impongono nulla agli altri pacchetti.

### Strumenti per la qualità (facoltativi ma consigliati)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire di effettuare commit di codice mal formattato, vulnerabile o contenente un segreto. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (dipendenze CVE), unittest. Vedere la sezione _Quality / pre-commit_ di `CLAUDE.md` per i dettagli.

## Configurazione

Le chiavi vengono cercate in **tre posizioni**, dalla più prioritaria alla meno prioritaria.
Ciascuna si limita a colmare ciò che quella precedente lascia vuoto.

|     | Dove                                            | A cosa serve                             |
| --- | ----------------------------------------------- | ---------------------------------------- |
| 1   | Variabili d'ambiente                            | CI, container, deroga puntuale           |
| 2   | `.env` della directory corrente (o di un genitore) | una chiave propria del progetto |
| 3   | `~/.config/aipmt/.env`                                  | **installato una volta, vale ovunque**   |

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

La seconda rimane utile quando un repository ha una propria chiave: un `.env` nella radice
ha allora la precedenza sulla configurazione dell'utente, senza modificarla. E una variabile
già definita nell'ambiente ha la precedenza su entrambe:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Se non viene trovata alcuna chiave, il comando non mostra tracce delle chiamate: elenca
le tre posizioni con il relativo percorso esatto.

`GEMINI_API_KEY` è accettato come alternativa a `GOOGLE_API_KEY` (convenzione AI
Studio). Variabili facoltative: `XAI_BASE_URL` (endpoint xAI, predefinito
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondi per chiamata Anthropic, predefinito
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (vedere la sezione Grok CLI) e `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (vedere la sezione OpenCode). Per
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` e
`REGEN_JOB_TIMEOUT` (limite per job, predefinito 600 s).

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Tradurre utilizzando il proprio abbonamento ChatGPT (`--use_codex`)

Questo provider non utilizza alcuna chiave API: controlla la CLI Codex ufficiale in modalità
non interattiva, quindi la traduzione viene scalata dal quota dell'abbonamento
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
utenti per un provider opzionale.

**Da sapere:**

- **Non viene utilizzata alcuna chiave API.** `OPENAI_API_KEY` e `CODEX_API_KEY` vengono
  rimossi dall'ambiente del sottoprocesso, garantendo così che una chiave presente in
  `.env` non trasformi mai la traduzione in una fatturazione a consumo.
- **Un segmento = un «messaggio locale»** della finestra di 5 ore del piano.
  Utilizzare `--eco` (modello `gpt-5.6-luna`, 250-2.000 messaggi/5 h su Plus)
  invece del modello di qualità (`gpt-5.6-sol`, 10-100 messaggi/5 h).
- **Più lento** di una chiamata API: considerare circa 45 s per un README completo, contro
  pochi secondi in diretta.
- **Rifiutato in CI** (`CI` o `GITHUB_ACTIONS` definito): l'autenticazione tramite
  abbonamento non è prevista per un runner condiviso e OpenAI sconsiglia questo
  workflow sui repository pubblici. Utilizzare una chiave API in questo percorso.
- Variabili d'ambiente: `CODEX_BIN` (percorso esplicito del binario) e
  `CODEX_TIMEOUT` (secondi per segmento, predefinito `600`).

### Tradurre utilizzando il proprio abbonamento Grok (`--use_grok_cli`)

Stesso principio di `--use_codex`, con la CLI ufficiale **Grok Build**: la
traduzione viene scalata dall'abbonamento Grok (SuperGrok / X Premium+) invece
di essere fatturata a token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — leggere prima dell'uso.** Questo provider è strutturalmente **più
debole** di `--use_codex`, ed è una scelta consapevole:

- Codex viene eseguito in `--sandbox read-only`, una frontiera imposta dal sistema.
- Il sandbox di Grok **non può essere applicato** su molti sistemi Linux recenti:
  AppArmor blocca gli user namespace non privilegiati da Ubuntu 24.04, e la deny-list
  dei socket di runtime dei container fallisce se `/run/podman` è
  `0700`. Ora, un profilo **integrato** che non può essere applicato viene
  avviato **senza confinamento, in silenzio**.
- Lo script quindi non richiede alcun profilo per impostazione predefinita e **non
  ricade mai silenziosamente**: mostra un avviso. Il confinamento si basa sulle
  regole `--deny` della CLI (incluso il catch-all `*`), l'unico livello
  misurato _fail-closed_ — una regola sconosciuta fa rifiutare l'avvio invece di
  rimuovere la protezione senza comunicarlo.
- Per **imporre** il sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`. L'avvio
  fallirà se la macchina non può rispettarlo, che è il comportamento desiderato.

**Quota**: il pool Grok è **settimanale e condiviso** con Chat, Imagine e
Voice, e nessun comando consente di leggerlo. Un'elaborazione in batch può quindi
consumare il tuo utilizzo conversazionale senza alcun segnale — da qui una
concorrenza limitata a 2 e un avviso in `regen_translations.sh`.

Altre variabili: `GROK_BIN` (percorso del binario), `GROK_TIMEOUT` (predefinito 900 s).

Per rigenerare le 28 traduzioni:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Tradurre con OpenCode, verso il provider desiderato (`--use_opencode`)

[OpenCode](https://opencode.ai) è un agente di codice **open source (MIT)** da
terminale. Non è un provider di modelli, ma un **router** verso quelli
configurati direttamente in OpenCode: una chiave API, un abbonamento
(GitHub Copilot, ChatGPT, SuperGrok), il gateway OpenCode Zen — che offre modelli
gratuiti **senza account** — oppure un modello **locale** (Ollama, LM Studio,
llama.cpp). Questo provider controlla `opencode run` in modalità non interattiva
e limita la chiamata a un solo andata e ritorno, senza alcuno strumento.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` è **obbligatorio**, nel formato `provider/modèle`. OpenCode non è
un provider e non viene scelto alcun valore predefinito al posto vostro: il suo
fallback interno sarebbe un modello gratuito le cui conversazioni potrebbero essere
utilizzate per l'addestramento.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamento — cosa fa lo script a ogni chiamata:**

- Una configurazione inline (`OPENCODE_CONFIG_CONTENT`), prioritaria rispetto alla vostra,
  definisce un agente `aipmt` i cui **strumenti sono tutti rifiutati**
  (`permission: { "*": "deny" }`): il modello non può né leggere, né scrivere, né
  eseguire comandi — nei test, non ci prova nemmeno. La condivisione della sessione
  è disattivata, `--pure` esclude i plugin esterni, mai `--auto`.
- La chiamata viene eseguita in una **directory temporanea e vuota**, con gli interruttori
  `OPENCODE_DISABLE_PROJECT_CONFIG` e `OPENCODE_DISABLE_CLAUDE_CODE`: senza di essi, OpenCode inserisce in ogni prompt
  l'`AGENTS.md` della directory corrente e il vostro `~/.claude/CLAUDE.md` — nei test, una
  direttiva «terminare ogni risposta con BANANA» inserita in un `AGENTS.md` veniva
  applicata alla traduzione. Le regole globali di `~/.config/opencode/AGENTS.md` restano invece
  applicate: OpenCode non consente di escluderle.
- Il contratto di output richiede contemporaneamente: codice di ritorno 0, nessun evento
  `error`, nessuna chiamata a strumenti, un ultimo passaggio terminato in
  `stop`, testo non vuoto e agente effettivamente caricato — un `--agent`
  sconosciuto non fa fallire OpenCode, ma **ricade silenziosamente** sull'agente di
  codifica, con gli strumenti attivi. Anche un `exit 0` non dimostra nulla qui.
- **Nessuna chiave di aipmt viene trasmessa** al sottoprocesso (stesso filtraggio
  utilizzato con Codex e Grok), con una sola eccezione nominativa: `OPENCODE_API_KEY`,
  la chiave di OpenCode stesso (Zen, Go). I provider vengono configurati in
  OpenCode (`opencode auth login`, `opencode.json`), non nel `.env` di aipmt.

**Da sapere:**

- **I modelli gratuiti di Zen sono modelli «stealth» o contributori**,
  variabili, con limiti non documentati, e le loro conversazioni potrebbero essere
  utilizzate per l'addestramento: perfetti per la documentazione pubblica, da evitare
  per i contenuti privati. Nei test: `opencode/mimo-v2.5-free` traduce questo README in un
  solo passaggio; `opencode/big-pickle` è più lento e due richieste simultanee sono rimaste
  senza risposta.
- **Un modello locale deve offrire almeno 16 k di contesto** — i segmenti arrivano
  fino a 16.000 caratteri — mentre Ollama spesso ne configura 4.096 per impostazione
  predefinita. Con Ollama: un `Modelfile` con `PARAMETER num_ctx 32768`, poi
  `ollama create`. La qualità dipende dal modello: un 7B ha invertito un elenco e
  danneggiato la chiusura di un blocco di codice in un file di prova, mentre un modello
  del gateway ha preservato tutto.
- `--eco` non ha effetto (il modello è quello di `--model`);
  `--reasoning_effort` viene trasmesso così com'è come `--variant` di OpenCode e va
  richiesto solo se il modello lo conosce.
- Le sessioni vengono registrate da OpenCode nel suo database
  (`~/.local/share/opencode/`), come ogni sessione OpenCode.
- Variabili d'ambiente: `OPENCODE_BIN` (percorso esplicito del binario,
  altrimenti `PATH` e poi `~/.opencode/bin/opencode`) e `OPENCODE_TIMEOUT`
  (secondi per segmento, predefinito `600`). `OPENCODE_CONFIG` viene
  rispettato se lo si esporta.

### Modalità economica

Utilizza modelli più rapidi e meno costosi (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opzioni

| Opzione                   | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | File Markdown singolo da tradurre                                                                            |
| `--source_dir`           | Directory sorgente contenente i file Markdown                                                             |
| `--target_dir`           | Directory di output per i file tradotti                                                               |
| `--source_lang`          | Lingua sorgente (predefinita: `fr`)                                                                                  |
| `--target_lang`          | Lingua di destinazione (predefinita: `en`)                                                                                   |
| `--model`                | Modello specifico da utilizzare                                                                                  |
| `--eco`                  | Utilizzare i modelli economici                                                                              |
| `--use_mistral`          | Utilizzare l'API Mistral AI                                                                                     |
| `--use_claude`           | Utilizzare l'API Claude                                                                                         |
| `--use_gemini`           | Utilizzare l'API Gemini                                                                                         |
| `--use_codex`            | Utilizzare la CLI Codex sulla quota dell'abbonamento ChatGPT                                                    |
| `--use_grok`             | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Utilizzare la CLI Grok sulla quota dell'abbonamento Grok                                                        |
| `--use_opencode`         | Utilizzare OpenCode (open source) con il provider configurato in OpenCode; richiede `--model provider/modèle` |
| `--force`                | Forzare la ritraduzione                                                                                       |
| `--keep_filename`        | Conservare il nome file originale                                                                          |
| `--news`                 | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua                                      |
| `--add_translation_note` | Aggiungere una nota di traduzione                                                                                |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinita) oppure `both`                                                     |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) oppure `marker`                                            |
| `--include_model`        | Includere il nome del modello nel file di output                                                            |
| `--reasoning_effort`     | Impegno di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **I sette flag dei provider sono mutuamente esclusivi.** In precedenza combinarne due era accettato silenziosamente e la risoluzione avveniva verso il primo verificato: una traduzione richiesta sulla quota dell'abbonamento (`--use_codex`, `--use_grok_cli`)
> poteva quindi essere addebitata a consumo senza alcun avviso.
> `argparse` ora rifiuta la combinazione.

### Nota di traduzione: posizioni e formati

Con `--add_translation_note`, il translator può inserire la nota in alto, in basso o in entrambe le posizioni e renderla in formato testo semplice (retrocompatibile) oppure in formato `marker` utilizzabile da un plugin Markdown.

**Posizione** (`--note_position`):

- `bottom` (predefinita): nota alla fine del file, come storicamente.
- `top`: nota inserita **dopo il frontmatter YAML** (compatibilità con Astro Content Collections, gray-matter, ecc.).
- `both`: nota inserita IN ALTO E IN BASSO (una sola chiamata LLM, contenuto riutilizzato per entrambe le posizioni).

**Formato** (`--note_format`):

- `legacy` (predefinito): paragrafo in grassetto `**...**` — comportamento strettamente identico a v1.8, byte-for-byte. Compatibile con Hugo, GitHub, GitLab e qualsiasi renderer Markdown.
- `marker`: definizione Markdown invisibile di un link reference (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguita da un blockquote in grassetto. Leggibile nativamente su GitHub/GitLab e utilizzabile in fase di build da un plugin remark lato Astro per produrre un banner stilizzato (vedere il blog jls42.org).

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

| Provider | Qualità (predefinita)                      | Economico (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obbligatorio | idem — `--eco` senza effetto |

> **Raccomandazione per le traduzioni long-form**: `--use_gemini` (predefinito = `gemini-3.7-flash`) preserva fedelmente la struttura Markdown negli script non latini (PL, JA, ZH, AR, HI), anche in modalità `--news`, dove la fedeltà dei placeholder è importante. Misurato su questo README tradotto in giapponese: struttura identica a `gemini-3.1-pro-preview` (21 elenchi, 18 blocchi di codice, 13 link HTML, 13 immagini, tutti gli URL preservati) con una latenza circa 6 volte inferiore. OpenAI rimane il valore predefinito per la retrocompatibilità.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articolo tradotto dal francese all’italiano con gpt-5.6-luna.**
