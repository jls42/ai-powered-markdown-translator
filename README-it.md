# Traduttore di Markdown AI-Powered

🌍 [Francese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Inglese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spagnolo](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Cinese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Tedesco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Giapponese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabo](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Olandese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polacco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portoghese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Romeno](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svedese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code smell"></a>
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

Traduce file Markdown da una lingua a un'altra preservandone la
struttura: blocchi di codice, codice inline, URL, ancore, tabelle e front
matter. Nove modi per chiamare un modello — cinque API, due abbonamenti senza
fatturazione a consumo, due router — e una misurazione pubblicata di ciò che ogni
modello preserva realmente.

## In breve

- **Nove percorsi di provider**: API OpenAI, Mistral, Claude, Gemini e Grok;
  abbonamenti ChatGPT (Codex) e Grok senza fatturazione a consumo; router
  OpenCode (open source, gratuito o locale) e OpenRouter (più di 400 modelli).
- **Nessun risultato errato a causa di un token perso**: blocchi di codice, codice inline,
  URL, ancore e citazioni vengono sostituiti da token prima della chiamata e
  verificati al ritorno. Se ne manca uno, il file non viene scritto.
- **Documenti lunghi**: segmentazione in base alla finestra del modello.
- **Modalità `--news`**: citazioni inglesi protette e bandiere gestite per
  lingua, per gli articoli di monitoraggio.
- **Modalità `--eco`**: modelli più veloci e meno costosi.
- **Nota di traduzione** facoltativa, in alto, in basso o in entrambe le posizioni.

## Installazione

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 o versioni successive. Per installare dal repository, vedere
[Contribuire](#contribuire).

## Configurazione

Le chiavi vengono lette da tre posizioni, dalla priorità più alta alla più bassa; ciascuna
compila solo ciò che la precedente ha lasciato vuoto.

|     | Dove                                          | Per cosa                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabili d'ambiente                          | CI, container, eccezione occasionale  |
| 2   | `.env` della directory corrente (o di una directory superiore) | una chiave specifica per un progetto |
| 3   | `~/.config/aipmt/.env`                        | installato una volta, valido ovunque  |

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

`GEMINI_API_KEY` è accettato al posto di `GOOGLE_API_KEY`. Il file
utente segue `XDG_CONFIG_HOME` (solo percorso assoluto) e `%APPDATA%`
su Windows. Senza una chiave, il comando elenca le tre posizioni.

**Il `.env` di un progetto non può reindirizzare le chiamate.** Fornisce chiavi,
mai una destinazione: qualsiasi variabile in `_BASE_URL`, `_API_BASE` o
`_ENDPOINT`, i proxy (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), gli
archivi dei certificati (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` / `APPDATA` vengono ignorati, con un
avviso. Un repository clonato non deve poter dirottare la chiave. Questo
file viene inoltre letto senza interpolazione: `NOM=${OPENAI_API_KEY}` non vi copia
la chiave. Impostare queste variabili nell'ambiente o in
`~/.config/aipmt/.env`.

Variabili facoltative: `XAI_BASE_URL` (predefinito `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secondi per chiamata, predefinito 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predefinito 600), `GROK_BIN`, `GROK_HOME` (predefinito `~/.grok`), `GROK_TIMEOUT`
(predefinito 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(predefinito 600), `OPENROUTER_BASE_URL` (`https://` obbligatorio), `OPENROUTER_TIMEOUT`
(predefinito 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (predefinito 30). Ciascuna è descritta in dettaglio
nella sezione del relativo provider.

## Primi passi

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traduce in spagnolo producendo `document-es.md` in `--target_dir`;
con `--include_model`, `document-es-gpt-5.6-terra.md`. L'estensione diventa
sempre `.md` — `article.mdx` produce `article-en.md` — tranne con
`--keep_filename`, che conserva il nome originale. Una traduzione già presente
viene ignorata senza `--force`.

Codici di uscita: `0` se tutto è riuscito o è stato ignorato, `1` se rimane un file
non riuscito (elencato nell'output di errore), `2` se il problema riguarda la configurazione.
Un file non riuscito non viene mai scritto, anche se è la scrittura stessa a non riuscire:
il contenuto viene scritto accanto e poi rinominato. È sufficiente eseguire nuovamente il comando.

## Quale modello scegliere

Misurato su due documenti reali, tradotti nelle stesse quattordici lingue da
ciascun modello. **Il numero indica quante lingue, su quattordici, producono una
traduzione scritta in cui nulla differisce dalla fonte.**

| Modello               | Come accedervi                     | Articolo di monitoraggio denso | Questo README | Cosa differisce e in quante lingue                                                                                                    |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | chiave API Google                 | ✅ 14/14                | ⚠️ 13/14     | 1 lingua su 14: una parola in grassetto in più (ja)                                                                                   |
| **GPT-5.6 Sol**      | abbonamento ChatGPT o chiave OpenAI | ✅ 14/14              | ⚠️ 12/14     | 2 lingue su 14: una parola in grassetto in meno (ar, ja)                                                                              |
| **GLM-5.2**          | chiave OpenRouter                 | ✅ 14/14                | ⚠️ 11/14     | 3 lingue su 14: una parola in grassetto in meno (hi, ja, ko)                                                                          |
| Claude Sonnet 5      | chiave API Anthropic              | ⚠️ 11/14                | ⚠️ 12/14     | 3 lingue nell'articolo: è comparso un blocco di codice (es, de, hi); 2 in questo README: un link senza markup (sv), una parola in grassetto (zh) |
| Qwen 3.7 Flash       | chiave OpenRouter                 | ❌ 8/14                 | ⚠️ 10/14     | 1 lingua rifiutata nell'articolo, altre 5 differiscono; in questo README, una quarantina di parole inserite in `code` (ar)     |
| Grok 4.6             | abbonamento Grok                  | ❌ 8/14                 | non valutato  | 5 lingue rifiutate su 14 per l'assenza del codice inline e degli URL restituiti; l'olandese differisce in tutto                       |
| GPT-OSS 20B          | modello locale (Ollama)           | ❌ 7/14                 | non rimisurato | 4 lingue rifiutate su 14: il modello vi lasciava passaggi in francese e il controllo li ha bloccati                                  |
| MiMo v2.5 (gratuito) | OpenCode Zen, senza account       | ❌ 11/14                | non rimisurato | 1 lingua rifiutata; una sezione persa in polacco                                                                                     |
| Mistral Large        | chiave API Mistral                | ❌ 5/14                 | ❌ 1/14      | **scompare un'intera sezione**: 1 lingua nell'articolo (hi), 3 in questo README (ar, hi, ko) — e 3 lingue rifiutate nell'articolo     |
| DeepSeek V4 Flash    | chiave OpenRouter                 | ❌ 3/14                 | non rimisurato | 10 lingue rifiutate su 14; 37 minuti per lingua                                                                                      |

|     | Significato del simbolo                                                                                                                                                                               |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | tutte le quattordici lingue tradotte e nulla differisce dalla fonte                                                                                                                                   |
| ⚠️  | tutte le quattordici lingue tradotte; ciò che differisce è il **markup** — una parola in grassetto, un `code`, un link che perde le parentesi quadre. Non manca alcun testo, URL, blocco di codice o sezione |
| ❌  | almeno una lingua non ha potuto essere tradotta — il file viene rifiutato e non scritto — **oppure** manca del contenuto in un file scritto                                                           |

Cosa bisogna ricordare:

- **Una traduzione rifiutata non è una traduzione danneggiata.** Quando manca un token
  al ritorno, il file non viene scritto e la lingua viene conteggiata come
  rifiutata. È ciò che accade a Grok nell'articolo: quattro elementi di codice inline e
  tre URL persi già nel primo segmento, nelle cinque scritture non latine.
- **Questa rete di sicurezza non copre i titoli, le tabelle, il front matter né il
  testo.** Un modello che elimina una sezione restituisce un file che lo strumento scrive
  senza protestare — è il caso di Mistral. Questi elementi non possono essere
  sostituiti da un token e i controlli attuali non li verificano;
  `scripts/compare_structure.py` rileva una sezione persa, ma solo a posteriori.
- **Grok non ha una valutazione per questo README**: la sua sessione CLI è scaduta dopo dodici
  lingue, undici delle quali senza differenze. Una campagna interrotta non viene valutata.
- **La densità del documento conta più della lingua.** Grok funziona con i
  README ordinari e cede con un articolo ricco di link, anche in
  olandese.

Date e documenti: la colonna «Questo README» è stata misurata il 9 settembre 2026
su una revisione congelata di questo file (785 righe, 285 elementi di codice inline, 89 righe
di tabella), modificata successivamente. La colonna «Articolo di monitoraggio denso» deriva dalla
campagna del 4 e 5 settembre su un articolo di 589 righe, tranne la riga
Grok, rimisurata il 9 settembre su un'altra edizione dello stesso monitoraggio. Le
tabelle complete, le durate e il protocollo sono disponibili in
[Misurazioni dettagliate](#misurazioni-dettagliate).

## Tutte le opzioni

| Opzione                  | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Singolo file Markdown da tradurre (alternativa a `--source_dir`)                                              |
| `--source_dir`           | Directory sorgente contenente i file Markdown (predefinita: `content/posts`)                                   |
| `--target_dir`           | Directory di output per i file tradotti (predefinita: `traductions_en`)                                        |
| `--source_lang`           | Lingua sorgente (predefinita: `fr`)                                                                |
| `--target_lang`           | Lingua di destinazione (predefinita: `en`)                                                         |
| `--model`           | Modello specifico da utilizzare                                                                               |
| `--eco`           | Utilizzare i modelli economici                                                                                |
| `--use_mistral`           | Utilizzare l'API Mistral AI                                                                                   |
| `--use_claude`           | Utilizzare l'API Claude                                                                                       |
| `--use_gemini`           | Utilizzare l'API Gemini                                                                                       |
| `--use_grok`           | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                                                        |
| `--use_codex`           | Utilizzare il CLI Codex con la quota dell'abbonamento ChatGPT                                                 |
| `--use_grok_cli`           | Utilizzare il CLI Grok con la quota dell'abbonamento Grok                                                     |
| `--use_opencode`           | Utilizzare OpenCode (open source) con il provider configurato in OpenCode; richiede `--model provider/modèle`            |
| `--use_openrouter`           | Utilizzare OpenRouter — richiede `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                                              |
| `--force`           | Forzare una nuova traduzione                                                                                  |
| `--keep_filename`           | Conservare il nome originale del file                                                                         |
| `--news`           | Modalità notizie: protegge le citazioni EN e gestisce le bandiere per lingua                                 |
| `--add_translation_note`           | Aggiungere una nota di traduzione                                                                             |
| `--note_position`           | Posizione della nota: `top`, `bottom` (predefinita) o `both`                           |
| `--note_format`           | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) o `marker`                     |
| `--include_model`           | Includere il nome del modello nel file di output                                                              |
| `--reasoning_effort`           | Livello di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`   |

Gli otto flag `--use_*` si escludono a vicenda: combinarne due viene
rifiutato.

## Provider

### Tramite API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` passa al livello economico di ciascun provider.

| Provider   | Qualità (predefinito)                               | Economico (`--eco`) |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                       | `claude-haiku-4-5`            |
| Mistral    | `mistral-large-latest`                                       | `mistral-small-latest`            |
| Gemini     | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`            |
| Codex      | `gpt-5.6-sol` (anche `terra` e `luna` tramite `--model`) | `gpt-5.6-luna` |
| Grok API   | `grok-4.6`                                       | `grok-4.3`            |
| Grok CLI   | `grok-4.6`                                       | `grok-4.5`            |
| OpenCode   | `--model provider/modèle` obbligatorio                           | uguale — `--eco` senza effetto |
| OpenRouter | `--model fournisseur/modèle` obbligatorio                           | uguale — `--eco` senza effetto |
### Con l'abbonamento ChatGPT: `--use_codex`

Pilota la CLI ufficiale di Codex: la traduzione viene detratta dalla quota
dell'abbonamento ChatGPT, senza chiave API né fatturazione a consumo.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Il binario viene cercato in `CODEX_BIN`, poi nel `PATH`, quindi nel package
  `openai-codex-cli-bin`. `~/.codex/auth.json` non viene mai letto.
- `OPENAI_API_KEY` e `CODEX_API_KEY` vengono rimosse dall'ambiente del
  sottoprocesso: la presenza di una chiave non provoca mai il passaggio all'API.
- Ogni segmento costa almeno un «messaggio» della finestra di 5 ore — due
  se la convalida fallisce e viene ritentato. OpenAI indica, a titolo
  orientativo, 250-2.000 messaggi/5 h per `gpt-5.6-luna` (`--eco`) e
  10-100 per `gpt-5.6-sol` con un piano Plus.
- Anche `--model gpt-5.6-terra` e `--model gpt-5.6-luna` passano attraverso
  l'abbonamento. Un modello al quale l'account non ha diritto restituisce un errore 400 «model is
  not supported when using Codex with a ChatGPT account».
- Più lento di un'API, con una differenza che aumenta insieme al documento: su questo README,
  una mediana di 6 min 46 s per lingua con `gpt-5.6-sol`, contro 36 s con
  `gemini-3.7-flash`.
- Non consentito nella CI (se `CI` o `GITHUB_ACTIONS` sono definiti): l'abbonamento si autentica
  tramite un file di sessione personale, che non deve trovarsi su un runner
  condiviso.
- Variabili: `CODEX_BIN`, `CODEX_TIMEOUT` (secondi per segmento, valore predefinito 600).

### Con l'abbonamento Grok: `--use_grok_cli`

Lo stesso principio si applica alla CLI ufficiale Grok Build, con l'abbonamento SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Confinamento più debole rispetto a Codex.** Il sandbox del sistema operativo di Grok non si applica
  su molte postazioni Linux recenti (AppArmor, socket del runtime
  dei container) e un profilo che non può essere applicato viene avviato senza confinamento e senza
  avvisi. Lo script non richiede quindi alcun profilo per impostazione predefinita, lo segnala e
  si basa sulle regole `--deny` della CLI, incluso il catch-all `*` — l'unico
  livello che rifiuta l'avvio anziché rimuovere la protezione senza
  comunicarlo. `GROK_TRANSLATE_SANDBOX=read-only` richiede il sandbox del sistema operativo e l'avvio
  fallisce se la macchina non può garantirlo.
- La quota è settimanale, condivisa con Chat, Imagine e Voice, e nessun
  comando consente di consultarla: un'elaborazione in batch può consumare l'utilizzo conversazionale
  senza alcuna segnalazione.
- Variabili: `GROK_BIN`, `GROK_HOME` (directory della CLI, valore predefinito `~/.grok`),
  `GROK_TIMEOUT` (valore predefinito 900), `GROK_TRANSLATE_SANDBOX`.

### Verso il provider preferito: `--use_opencode`

[OpenCode](https://opencode.ai) è un agente di coding open source (MIT) che
instrada le richieste verso i provider configurati al suo interno: chiave API, abbonamento,
gateway OpenCode Zen (modelli gratuiti, senza account) o modello locale. Qui sono
state misurate end-to-end due modalità, Zen e Ollama.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` è obbligatorio: senza di esso, OpenCode ripiegherebbe su un modello gratuito
le cui conversazioni possono essere utilizzate per l'addestramento, e questa scelta non viene effettuata
al posto vostro.

Confinamento a ogni chiamata:

- una configurazione inline, con priorità sulla vostra, definisce un agente `aipmt`
  per il quale tutti gli strumenti sono vietati (`permission: { "*": "deny" }`), la condivisione della
  sessione è disattivata, `--pure`, mai `--auto`;
- directory di lavoro temporanea e vuota, con `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` impostati — senza di essi, OpenCode inserisce nel
  prompt l'`AGENTS.md` della directory corrente e `~/.claude/CLAUDE.md`. Il
  `~/.config/opencode/AGENTS.md` globale rimane inserito, poiché OpenCode non consente
  di escluderlo;
- contratto di output: codice di uscita 0, nessun evento `error`, nessuna chiamata
  a strumenti, ultimo passaggio in `stop`, testo non vuoto e agente `aipmt`
  effettivamente caricato — un `--agent` sconosciuto non causa il fallimento di OpenCode, che
  ripiega silenziosamente sull'agente di coding;
- non viene trasmessa alcuna chiave di `aipmt`, tranne `OPENCODE_API_KEY`, la chiave
  di OpenCode stesso. I provider si configurano in OpenCode, non nel
  `.env` di `aipmt`.

Da sapere:

- I modelli gratuiti di Zen cambiano nel tempo, hanno limiti non documentati e
  le loro conversazioni possono essere utilizzate per l'addestramento: sono adatti alla documentazione
  pubblica, non a contenuti privati.
- Un modello locale deve offrire almeno 16 k token di contesto, poiché i segmenti
  arrivano fino a 16.000 caratteri. Ollama ne configura spesso 4.096: occorre passare
  attraverso un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` non ha effetto; `--reasoning_effort` viene trasmesso così com'è come
  `--variant` di OpenCode.
- OpenCode registra ogni sessione in `~/.local/share/opencode/`.
- Variabili: `OPENCODE_BIN` (in caso contrario il `PATH`, quindi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secondi per segmento, valore predefinito 600). `OPENCODE_CONFIG`
  viene passato così com'è a OpenCode.

Esempio di un modello locale tramite Ollama, in `~/.config/opencode/opencode.json`:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` disattiva il ragionamento che Ollama abilita per impostazione predefinita su questi
modelli e che un Modelfile non può disattivare. Misurato su una frase di
sei parole: 919 token di ragionamento e 68 secondi senza l'opzione, 9 token con essa.

### Verso più di 400 modelli: `--use_openrouter`

OpenRouter è un router fatturato a consumo, tramite un credito unico, che dà accesso a
modelli ospitati da terze parti — inclusi i modelli cinesi aperti che nessun
altro provider espone qui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` è obbligatorio. Un preflight, eseguito prima di qualsiasi fatturazione, gestisce
due particolarità dell'instradamento:

- **Lo stesso modello viene servito da decine di host con limiti
  differenti** — per `z-ai/glm-5.3-flash`, 23 host, uno dei quali limitato a
  2.048 token di output. Il preflight legge `/api/v1/models/{modèle}/endpoints`,
  esclude gli host con meno di 8.000 token di output o con stato degradato e
  fissa gli altri tramite `allow_fallbacks: false`.
- **Il ragionamento viene fatturato alla tariffa dell'output** — 107 token contro 2 per
  una risposta «OK» di `z-ai/glm-5.2`. È disattivato per impostazione predefinita; i modelli
  che lo impongono ricevono il livello di effort più basso accettato, poiché il valore predefinito del
  catalogo potrebbe saturare l'output prima della fine della traduzione.
  `--reasoning_effort` mantiene la priorità.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La finestra di contesto proviene dal catalogo. Un modello con meno di 16.400 token viene
  rifiutato prima di qualsiasi chiamata: 8.400 per il prompt e il segmento, almeno 8.000
  per l'output.
- Uno slug assente dal catalogo, un catalogo irraggiungibile o l'assenza
  di un host in grado di rispettare il limite interrompono il comando.
- `finish_reason=length` con un output vuoto indica un budget consumato dal
  ragionamento, non un troncamento: il messaggio distingue i due casi.
- `--eco` non ha effetto.
- Variabili: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (valore predefinito `https://openrouter.ai/api/v1`, `https://`
  richiesto), `OPENROUTER_TIMEOUT` (valore predefinito 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (valore predefinito 30).

### Nota di traduzione

`--add_translation_note` aggiunge una nota, in `bottom` (valore predefinito), `top` (dopo il
front matter) oppure `both` (`--note_position`), nel formato `legacy` (paragrafo in
grassetto, valore predefinito) o `marker` (`--note_format`). Il formato `marker` è una
definizione di riferimento Markdown invisibile,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguita da una citazione in grassetto: leggibile su GitHub, utilizzabile durante la build da un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Misurazioni dettagliate

Tutte le misurazioni sono traduzioni realmente eseguite con `aipmt`, verso
quattordici lingue: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scritte** indica i file lasciati passare dai controlli; **Senza
differenze** quelli nei quali `scripts/compare_structure.py` non rileva nulla — stesso numero di
sezioni, sottotitoli, link, URL distinti, blocchi di codice,
codici inline, righe di tabella, blocchi di citazione e parole in grassetto.

«Senza differenze» significa «nulla di rilevato», non «identico»: il comparatore
conta gli elementi senza leggerne il contenuto. Non segnala né un titolo di
livello 4 eliminato, né il testo di un codice inline sostituito, né una bandiera
scambiata, e non valuta la lingua.

### Articolo di rassegna denso, modalità `--news`

Un'edizione della [rassegna sull'IA di jls42.org](https://jls42.org/fr/news):
589 righe, 140 link, 21 sezioni, 3 citazioni inglesi protette. Campagna
del 4 e 5 settembre 2026.

| Modello                            | Accesso              | Scritte | Senza differenze | Mediana/lingua |
| --------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | abbonamento ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                 | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | locale              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`            | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | abbonamento Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok è stato misurato nuovamente il 9 settembre su un'altra edizione della stessa rassegna
(356 righe): 9 lingue scritte su 14, 8 senza differenze. È questo il dato
riportato nella tabella riepilogativa. Tre campagne interrotte non sono
riportate: `qwen3.5-27b` (9 lingue) e `kimi-k2.6` (4) per mancanza di credito,
`z-ai/glm-5.3-flash`, i cui due errori derivavano da un'impostazione di ragionamento
che il provider sta correggendo. Le righe OpenRouter sono state misurate con le
impostazioni predefinite del router, prima di `--use_openrouter`; `z-ai/glm-5.2`,
misurato nuovamente con il provider fornito, restituisce lo stesso risultato di 14/14. I dati sono stati
ricalcolati il 10 settembre con il comparatore attuale: `qwen3.8-flash` e
`qwen3.7-flash` guadagnano ciascuno una lingua rispetto alla prima
pubblicazione, mentre gli altri rimangono invariati.

### README di questo progetto, Markdown standard

Revisione fissata al 9 settembre 2026: 785 righe, 285 codici inline, 40
chiusure di blocchi, 89 righe di tabella. Quattro traduzioni in parallelo.

| Modello                        | Scritte | Senza differenze | Mediana/lingua | Elementi differenti                                                        |
| ----------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14   | 36 s           | una parola in grassetto (ja)                                                |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14   | 2 min 56 s     | un link (sv), una parola in grassetto (zh)                                  |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14   | 6 min 46 s     | una parola in grassetto (ar, ja)                                            |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14   | 2 min 34 s     | una parola in grassetto (hi, ja, ko)                                        |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 codici inline aggiunti in arabo; grassetto (hi, ja, ko)                  |
| `mistral-large-latest`        | 14/14   | ❌ 1/14    | 2 min 44 s     | una sezione persa (ar, hi, ko); blocchi di codice aggiunti (ja, ko, ro, zh) |

Due campagne interrotte non sono riportate: Grok, sessione CLI scaduta
dopo dodici lingue (undici senza differenze), e `qwen3.8-flash`, HTTP 429 del suo
host dopo due. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
non sono stati misurati nuovamente su questa revisione; su quella del 4 e 5 settembre,
più corta di 277 righe, scrivevano ciascuno 9 traduzioni su 14, di cui rispettivamente 7
e 1 senza differenze.

### Quattro README di progetti noti

FastAPI, Ollama, tldr-pages e Vue.js, presi così come sono da GitHub — documenti
più semplici dei due precedenti. La campagna era rivolta ai modelli
in difficoltà; Gemini funge da termine di paragone.

| Modello                    | Ambito                     | Scritte | Senza differenze |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 progetti × 14 lingue      | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 progetti × 14 lingue      | 55/56   | ❌ 47/56     |
| `grok-4.6` (abbonamento)   | 4 progetti × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 progetti × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Cosa non rappresentano queste misurazioni

- **Non sono una classifica esaustiva**: solo OpenRouter offre più di quattrocento
  modelli, mentre ne sono stati misurati circa quindici.
- **Le durate sono indicative**: da tre a sei traduzioni in parallelo a seconda
  delle campagne, e il throughput di un provider varia nel corso della giornata.
- **Sono osservazioni datate**: i modelli cambiano pur mantenendo lo stesso nome e i vostri
  documenti non sono i nostri.

Per ripetere la misurazione sui vostri documenti, utilizzando una copia fissata del file:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contribuire

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Entrambe le righe sono necessarie: senza `pip install -e .`, `python -m aipmt`
risponde `No module named aipmt`.

Strumenti per la qualità, facoltativi ma consigliati:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Le 28 traduzioni del repository (README e CHANGELOG, quattordici lingue) vengono
rigenerate con `./regen_translations.sh --force` — Codex e `gpt-5.6-sol` tramite
l'abbonamento ChatGPT per impostazione predefinita, quattro in parallelo. `REGEN_PROVIDER` e
`REGEN_MODEL` modificano il percorso; un'API fatturata (`openai`, `gemini`,
`grok`, `openrouter`) viene rifiutata senza `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` imposta il limite di ogni job (600 s, 1.800 s su Codex). I dettagli
degli strumenti sono disponibili in `CLAUDE.md`.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** — blog personale pubblicato in 15 lingue. La sua
  [rassegna quotidiana sull'IA](https://jls42.org/fr/news) viene tradotta ogni giorno
  con questo strumento e funge da documento di riferimento per le misurazioni precedenti.

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avvertenza

Questo programma viene distribuito **senza alcuna garanzia**, secondo i termini delle
sezioni 15 e 16 della GPL v3: fornito «così com'è», senza garanzia di qualità
commerciale né di idoneità a uno scopo particolare, e il suo autore non può essere
ritenuto responsabile di eventuali danni derivanti dal suo utilizzo. Il testo della
licenza prevale su questo riepilogo.

- **Rileggete prima di pubblicare.** Le protezioni coprono i blocchi di codice, il
  codice inline, gli URL, le ancore e le citazioni della modalità `--news` — ma non i
  titoli, le tabelle, il front matter o il significato delle vostre frasi.
- **I vostri documenti vengono inviati al provider scelto**, secondo le sue condizioni
  d'uso e la sua politica sui dati. Alcuni modelli gratuiti possono
  riutilizzare le vostre conversazioni per l'addestramento; un modello locale è l'unica
  modalità che impedisce a qualsiasi dato di lasciare la vostra macchina.
- **Le chiamate API vi vengono fatturate.** Questo programma non impone alcun limite alla
  spesa: un documento lungo, un nuovo tentativo dopo un errore o un modello che ragiona
  molto costano di più.
- **Le misurazioni pubblicate sono osservazioni datate**, non garanzie.

I nomi dei prodotti e delle società citati appartengono ai rispettivi proprietari.
Questo progetto non è affiliato ad alcuno di essi.

**Articolo tradotto dal francese all'italiano con gpt-5.6-sol.**
