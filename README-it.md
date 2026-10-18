# Traduttore di Markdown AI-Powered

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smell"></a>
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
matter. Undici modi per chiamare un modello — cinque API, quattro abbonamenti senza
fatturazione a consumo, due router — e una misurazione pubblicata di ciò che ciascun
modello preserva realmente.

## In breve

- **Undici percorsi di provider**: API OpenAI, Mistral, Claude, Gemini e Grok;
  abbonamenti ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) senza fatturazione a consumo; router OpenCode (open source, gratuito o locale) e OpenRouter
  (più di 400 modelli).
- **Nessun risultato errato a causa di un token perso**: blocchi di codice, codice inline,
  URL, ancore e citazioni vengono sostituiti da token prima della chiamata e
  verificati al ritorno. Se ne manca uno, il file non viene scritto.
- **Documenti lunghi**: segmentazione in base alla finestra del modello.
- **Modalità `--news`**: citazioni inglesi protette e flag gestiti per
  lingua, per gli articoli di monitoraggio.
- **Modalità `--eco`**: modelli più rapidi e meno costosi.
- **Nota di traduzione** facoltativa, in alto, in basso o in entrambe le posizioni.

## Installazione

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 o versione successiva. Per installare dal repository, vedere
[Contribuire](#contribuire).

## Configurazione

Le chiavi vengono lette in tre posizioni, dalla priorità più alta alla più bassa; ciascuna
colma solo ciò che la precedente lascia vuoto.

|     | Dove                                          | Per cosa                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabili d'ambiente                          | CI, container, deroga occasionale     |
| 2   | `.env` della directory corrente (o di una directory superiore) | una chiave specifica di un progetto   |
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
su Windows. Senza chiave, il comando elenca le tre posizioni.

**Il `.env` di un progetto non può né reindirizzare le chiamate né scegliere il programma
eseguito.** Fornisce chiavi, mai una destinazione o un binario: qualsiasi
variabile in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, i proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), gli archivi dei certificati (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` vengono ignorati, con un avviso. Un repository clonato non deve
poter deviare la vostra chiave, né farvi eseguire il proprio programma alla
prima traduzione. Questo file viene inoltre letto senza interpolazione:
`NOM=${OPENAI_API_KEY}` non vi copia la chiave. Impostate queste variabili
nell'ambiente o in `~/.config/aipmt/.env`.

Variabili facoltative: `XAI_BASE_URL` (predefinito `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secondi per chiamata, predefinito 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predefinito 600), `GROK_BIN`, `GROK_HOME` (predefinito `~/.grok`), `GROK_TIMEOUT`
(predefinito 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (predefinito 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (predefinito 600), `OPENROUTER_BASE_URL`
(`https://` obbligatorio), `OPENROUTER_TIMEOUT` (predefinito 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (predefinito 30). Ciascuna è descritta in dettaglio nella
sezione del relativo provider.

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
viene saltata senza `--force`.

Codici di uscita: `0` se tutto è riuscito o è stato saltato, `1` se rimane un file
non riuscito (elenco nell'output di errore), `2` se il problema riguarda la configurazione.
Un file non riuscito non viene mai scritto, anche se è la scrittura stessa a non riuscire:
il contenuto viene scritto accanto e poi rinominato. È sufficiente eseguire nuovamente il comando.

## Quale modello scegliere

Misurato su due documenti reali, tradotti nelle stesse quattordici lingue da
ciascun modello. **Il numero indica quante lingue, su quattordici, producono una
traduzione scritta in cui nulla differisce dalla fonte.**

| Modello                | Come accedervi                    | Articolo di monitoraggio denso | Questo README | Cosa differisce e in quante lingue                                                                                                                                    |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | abbonamento Google (Antigravity)  | ✅ 14/14                | ✅ 14/14     | nulla, in nessuno dei due documenti                                                                                                                                 |
| **Claude Sonnet 5.5** | chiave API Anthropic              | ✅ 14/14                | ✅ 14/14     | nulla, in nessuno dei due documenti                                                                                                                                 |
| **Gemini 3.7 Flash**  | chiave API Google                 | ✅ 14/14                | ⚠️ 13/14     | 1 lingua su 14: una parola in grassetto in più (ja)                                                                                                                 |
| **Gemini 3.7 Flash**  | abbonamento Google (Antigravity)  | ✅ 14/14                | ⚠️ 13/14     | 1 lingua su 14: una parola in grassetto in meno (ko)                                                                                                                |
| **GPT-5.6 Sol**       | abbonamento ChatGPT o chiave OpenAI | ✅ 14/14              | ⚠️ 12/14     | 2 lingue su 14: una parola in grassetto in meno (ar, ja)                                                                                                            |
| **GLM-5.2**           | chiave OpenRouter                 | ✅ 14/14                | ⚠️ 11/14     | 3 lingue su 14: una parola in grassetto in meno (hi, ja, ko)                                                                                                        |
| Claude Sonnet 5       | abbonamento Claude (Claude Code)  | ⚠️ 13/14                | ⚠️ 13/14     | 1 lingua su 14 nell'articolo: una parola in grassetto in più (zh); 1 in questo README: una riga della tabella attaccata alla precedente, nascosta nella visualizzazione (ar) |
| Claude Haiku 4.5      | abbonamento Claude (Claude Code)  | ⚠️ 11/14                | ✅ 14/14     | 3 lingue nell'articolo: un titolo di sezione passato al livello 1 (en, pl, ro); in questo README, nulla per il comparatore, ma i link interni sono duplicati in inglese |
| Claude Sonnet 5       | chiave API Anthropic              | ⚠️ 11/14                | ⚠️ 12/14     | 3 lingue nell'articolo: è comparso un blocco di codice (es, de, hi); 2 in questo README: un link senza markup (sv), una parola in grassetto (zh)                       |
| Claude Haiku 4.5      | chiave API Anthropic              | ⚠️ 7/14                 | ✅ 14/14     | 7 lingue nell'articolo: un titolo di sezione passato al livello 1 — in giapponese, rimasto in francese; nulla in questo README                                       |
| Claude Haiku 5.5      | chiave API Anthropic              | ⚠️ 11/14                | ❌ 12/14     | 3 lingue nell'articolo: un titolo di sezione ha cambiato livello o è stato duplicato (ja, ko, zh); in questo README, 2 lingue rifiutate, codici inline persi (ar, hi) |
| Qwen 3.7 Flash        | chiave OpenRouter                 | ❌ 8/14                 | ⚠️ 10/14     | 1 lingua rifiutata nell'articolo, altre 5 divergono; in questo README, una quarantina di parole inserite in `code` (ar)                                      |
| Grok 4.6              | abbonamento Grok                  | ❌ 8/14                 | non valutato | 5 lingue su 14 rifiutate per la mancata restituzione di codici inline e URL; l'olandese diverge completamente                                                       |
| GPT-OSS 20B           | modello locale (Ollama)           | ❌ 7/14                 | non rimisurato | 4 lingue su 14 rifiutate: il modello vi lasciava dei passaggi in francese, il controllo li ha bloccati                                                             |
| MiMo v2.5 (gratuito)  | OpenCode Zen, senza account       | ❌ 11/14                | non rimisurato | 1 lingua rifiutata; una sezione persa in polacco                                                                                                                  |
| Mistral Large         | chiave API Mistral                | ❌ 5/14                 | ❌ 1/14      | **scompare un'intera sezione**: 1 lingua nell'articolo (hi), 3 in questo README (ar, hi, ko) — e 3 lingue rifiutate nell'articolo                                  |
| DeepSeek V4 Flash     | chiave OpenRouter                 | ❌ 3/14                 | non rimisurato | 10 lingue su 14 rifiutate; 37 minuti per lingua                                                                                                                   |
| Claude Opus 5.5       | abbonamento Claude (Claude Code)  | ❌ 0/14                 | ✅ 14/14     | l'articolo è stato rifiutato in tutte le 14 lingue dai controlli di sicurezza di Opus, a causa di una breve notizia di biologia; nulla in questo README              |

|     | Significato del simbolo                                                                                                                                                                                |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | tutte e quattordici le lingue tradotte e nessuna differenza rispetto alla fonte                                                                                                                       |
| ⚠️  | tutte e quattordici le lingue tradotte; ciò che differisce è il **markup** — una parola in grassetto, un `code`, un link che perde le parentesi quadre. Non manca alcun testo, URL, blocco di codice o sezione |
| ❌  | almeno una lingua non ha potuto essere tradotta — il file viene rifiutato e non scritto — **oppure** manca del contenuto in un file scritto                                                            |

Cosa bisogna ricordare:

- **Una traduzione rifiutata non è una traduzione danneggiata.** Quando manca un token
  al ritorno, il file non viene scritto e la lingua viene conteggiata come
  rifiutata. È ciò che accade a Grok nell'articolo: quattro codici inline e
  tre URL persi già nel primo segmento, nei cinque sistemi di scrittura non latini.
- **Un modello può rifiutare un intero documento per una sola frase.** Opus 5.5
  traduce questo README senza alcuna differenza, ma nessun articolo di monitoraggio: i suoi
  controlli di sicurezza interrompono la risposta in corrispondenza di una breve notizia di biologia. Il file non viene
  scritto e aipmt ne indica il motivo.
- **Questa rete di sicurezza non copre i titoli, le tabelle, il front matter né il
  testo.** Un modello che elimina una sezione restituisce un file che lo strumento scrive
  senza protestare — è il caso di Mistral. Questi elementi non possono essere
  sostituiti da un token e i controlli attuali non li verificano;
  `scripts/compare_structure.py` rileva una sezione persa, ma a posteriori.
- **Grok non ha una valutazione per questo README**: la sua sessione CLI è scaduta dopo dodici
  lingue, undici delle quali senza differenze. Una campagna interrotta non viene valutata.
- **La densità del documento conta più della lingua.** Grok regge sui
  README ordinari e cede su un articolo ricco di link, anche in
  olandese.

Date e documenti: la colonna «Questo README» è stata misurata il 9 settembre 2026
su una revisione bloccata di questo file (785 righe, 285 codici inline, 89 righe
di tabella), modificata successivamente — a eccezione delle righe Antigravity e Claude Code,
misurate il 26 settembre sulla revisione pubblicata con la 1.14.0, più breve
(600 righe, 257 codici inline, 85 righe di tabella), e delle righe Claude
Sonnet 5.5, Haiku 5.5 e Haiku 4.5 tramite API, misurate il 18 ottobre sulla
stessa revisione. La colonna «Articolo di monitoraggio denso» proviene dalla campagna del
4 e 5 settembre su un articolo di 589 righe, a eccezione della riga Grok, rimisurata il
9 settembre su un'altra edizione dello stesso monitoraggio, delle righe Antigravity e
Claude Code, misurate il 26 settembre sullo stesso articolo, e di queste tre righe
Claude, il 18 ottobre. Le tabelle complete, le durate e il protocollo si trovano
in [Misurazioni dettagliate](#misurazioni-dettagliate).
## Tutte le opzioni

| Opzione                  | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Singolo file Markdown da tradurre (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Directory sorgente contenente i file Markdown (predefinita: `content/posts`)                                   |
| `--target_dir`           | Directory di output per i file tradotti (predefinita: `traductions_en`)                                    |
| `--source_lang`          | Lingua sorgente (predefinita: `fr`)                                                                                  |
| `--target_lang`          | Lingua di destinazione (predefinita: `en`)                                                                                   |
| `--model`                | Modello specifico da utilizzare                                                                                  |
| `--eco`                  | Utilizzare i modelli economici                                                                              |
| `--use_mistral`          | Utilizzare l'API Mistral AI                                                                                     |
| `--use_claude`           | Utilizzare l'API Claude                                                                                         |
| `--use_gemini`           | Utilizzare l'API Gemini                                                                                         |
| `--use_grok`             | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                                                           |
| `--use_codex`            | Utilizzare la CLI Codex sulla quota dell'abbonamento ChatGPT                                                    |
| `--use_grok_cli`         | Utilizzare la CLI Grok sulla quota dell'abbonamento Grok                                                        |
| `--use_antigravity`      | Utilizzare la CLI Antigravity (`agy`) sulla quota dell'abbonamento Google AI Pro o Ultra                       |
| `--use_claude_code`      | Utilizzare la CLI Claude Code (`claude -p`) sulla quota dell'abbonamento Claude Pro o Max                      |
| `--use_opencode`         | Utilizzare OpenCode (open source) con il provider configurato in OpenCode; richiede `--model provider/modèle` |
| `--use_openrouter`       | Utilizzare OpenRouter — richiede `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--force`                | Forzare la ritraduzione                                                                                       |
| `--keep_filename`        | Conservare il nome originale del file                                                                          |
| `--news`                 | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua                                      |
| `--add_translation_note` | Aggiungere una nota di traduzione                                                                                |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinita) o `both`                                                     |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) o `marker`                                            |
| `--include_model`        | Includere il nome del modello nel file di output                                                            |
| `--reasoning_effort`     | Sforzo di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

I nove flag `--use_*` si escludono a vicenda: combinarne due viene
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

| Provider    | Qualità (predefinita)                                | Economico (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                   | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (anche `terra` e `luna` tramite `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, sforzo `low`                                | uguale — `--eco` senza effetto |
| OpenCode    | `--model provider/modèle` obbligatorio                 | uguale — `--eco` senza effetto |
| OpenRouter  | `--model fournisseur/modèle` obbligatorio              | uguale — `--eco` senza effetto |

### Con l'abbonamento ChatGPT: `--use_codex`

Controlla la CLI ufficiale Codex: la traduzione viene detratta dalla quota
dell'abbonamento ChatGPT, senza chiave API né fatturazione in base all'utilizzo.

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
  se la convalida fallisce e viene riprovato. OpenAI indica, a titolo
  di stima, 250-2 000 messaggi/5 h per `gpt-5.6-luna` (`--eco`) e
  10-100 per `gpt-5.6-sol` con un piano Plus.
- Anche `--model gpt-5.6-terra` e `--model gpt-5.6-luna` passano tramite
  l'abbonamento. Un modello a cui l'account non ha diritto restituisce un errore 400 «model is
  not supported when using Codex with a ChatGPT account».
- Più lento di un'API, e il divario aumenta con il documento: su questo README,
  6 min 46 s per lingua come mediana con `gpt-5.6-sol`, contro 36 s per
  `gemini-3.7-flash`.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definito): l'abbonamento si autentica
  tramite un file di sessione personale, che non deve trovarsi su un runner
  condiviso.
- Variabili: `CODEX_BIN`, `CODEX_TIMEOUT` (secondi per segmento, valore predefinito 600).

### Con l'abbonamento Grok: `--use_grok_cli`

Stesso principio con la CLI ufficiale Grok Build, tramite l'abbonamento SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Confinamento più debole rispetto a Codex.** Il sandbox OS di Grok non si applica
  su molte postazioni Linux recenti (AppArmor, socket del runtime
  dei container) e un profilo che non può essere applicato si avvia senza confinamento
  e senza avvisare. Lo script non richiede quindi alcun profilo per impostazione predefinita, lo segnala e
  si basa sulle regole `--deny` della CLI, compreso il catch-all `*` — l'unico
  livello che rifiuta di avviarsi anziché rimuovere la protezione senza
  segnalarlo. `GROK_TRANSLATE_SANDBOX=read-only` richiede il sandbox OS e l'avvio
  fallisce se la macchina non è in grado di supportarlo.
- La quota è settimanale, condivisa con Chat, Imagine e Voice, e nessun
  comando consente di leggerla: un batch può intaccare l'utilizzo conversazionale
  senza alcuna segnalazione.
- Variabili: `GROK_BIN`, `GROK_HOME` (directory della CLI, valore predefinito `~/.grok`),
  `GROK_TIMEOUT` (valore predefinito 900), `GROK_TRANSLATE_SANDBOX`.

### Con l'abbonamento Google: `--use_antigravity`

Stesso principio con `agy`, la CLI ufficiale di Antigravity: per chi paga Google
AI Pro o Ultra, la traduzione viene detratta dalla quota dell'abbonamento anziché
essere fatturata per token. È l'unico modo per accedere a questa quota: Gemini CLI non
serve più questi account dal 18 giugno 2026
([annuncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e l'SDK di Antigravity accetta soltanto una chiave API o un progetto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Non rimane aperto alcun canale a pagamento.** agy riceve dal vostro
  ambiente soltanto un elenco chiuso di variabili — `PATH`, lingua e fuso orario,
  terminale, identità, proxy e certificati, bus di sessione — e nessuna chiave:
  diverse sue variabili fanno passare una chiamata a un altro canale senza mostrare nulla (risultato delle misurazioni:
  una invia il documento a un gateway di terze parti, un'altra a un progetto
  Google Cloud fatturato), mentre a ogni revisione risultava che un elenco di variabili negate ne dimenticava qualcuna.
  Prima di qualsiasi segmento, `agy -p /config`, che non consuma alcuna quota, deve mostrare
  i crediti IA a pagamento disattivati, senza chiave API né progetto Google Cloud — un'impostazione
  assente comporta il rifiuto —, altrimenti non viene tradotto nulla; il log di ogni
  chiamata deve poi attestare l'abbonamento (`authMethod=consumer`), altrimenti la
  risposta viene rifiutata.
- **Confinamento.** Ogni chiamata viene eseguita in una directory personale privata e
  usa e getta, con un agente di traduzione privo di strumenti: le vostre impostazioni, regole,
  plugin, server MCP e hook di agy non vi entrano, nulla viene aggiunto alla vostra
  cronologia e la connessione rimane nel portachiavi, che aipmt non legge mai.
  Se un agente non viene trovato, agy ripiega silenziosamente sul proprio agente di coding
  e sui relativi strumenti: un'intera riga del log deve confermare l'agente corretto — un
  documento che cita questo messaggio non la sostituisce —, altrimenti la chiamata viene rifiutata.
- **Piattaforme**: Linux, in una sessione dotata di portachiavi (bus di sessione
  D-Bus, Secret Service); macOS è accettato, ma non è stato sottoposto a misurazioni. Rifiutato
  su Windows, dove agy non legge le variabili che isolano ogni chiamata, e
  su Linux senza bus di sessione — sessione SSH, container, server: agy vi
  memorizza il proprio token in un file di `~/.gemini`, che l'isolamento nasconde. Il
  rifiuto avviene prima di qualsiasi avvio, indicandone la causa, invece di attendere
  per un minuto un codice di connessione.
- **Modelli**: quelli di `agy models`. I Gemini includono lo sforzo nel proprio nome
  (`gemini-3.8-flash-medium`…): un nome senza suffisso viene rifiutato prima della chiamata
  e `--reasoning_effort` non ha effetto. Per impostazione predefinita `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` con `--eco`; le campagne che li hanno determinati sono
  descritte in [Misurazioni dettagliate](#misurazioni-dettagliate). Claude e GPT-OSS
  hanno una propria quota, molto più piccola: circa l'1% della finestra di
  5 ore per chiamata misurata, contro lo 0,05% in Flash.
- **Quota**: per gruppo, una finestra di 5 ore e una settimanale, in
  proporzione al costo in token. Misurato sull'account dell'autore: circa
  16 punti della finestra di 5 ore per milione di caratteri sorgente con
  `gemini-3.8-flash-medium`, 14 con `gemini-3.7-flash-medium` e da 7 a 8 con
  uno sforzo basso — un README di 40 000 caratteri costa quindi poco più di
  mezzo punto. Il limite settimanale dipende invece dal livello. I nuovi tentativi seguono
  ciò che agy dichiara riprovabile; in caso contrario, una finestra esaurita non viene mai
  riprovata: provoca il fallimento di ogni file fino alla reimpostazione
  mostrata da `/usage`.
- **Più lento dell'API**: sull'articolo denso relativo alle misurazioni, 3 min 59 s per
  lingua come mediana con `gemini-3.8-flash-medium` e 3 min 14 s con
  `gemini-3.7-flash-medium`, contro 1 min 18 s per Gemini 3.7 Flash tramite API.
- **Interruzione**: Ctrl-C, o la chiusura del terminale, arrestano agy insieme al
  comando anziché lasciarlo terminare il proprio turno consumando la vostra quota; lo stesso vale per
  Codex, Grok CLI e OpenCode. Con `nohup`, la traduzione continua.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definito): la connessione risiede in un
  portachiavi personale. Su un runner, `--use_gemini` con `GOOGLE_API_KEY`.
- Variabili: `AGY_BIN` (altrimenti il `PATH`, quindi `~/.local/bin/agy`),
  `AGY_TIMEOUT` (secondi per segmento, avvio compreso, valore predefinito 900).

**Condizioni d'uso: è il vostro account a essere coinvolto.** Le
[condizioni di Antigravity](https://antigravity.google/terms) (sezione 6) e le sue
[FAQ](https://antigravity.google/docs/faq/) vietano di accedere al servizio
tramite software di terze parti utilizzando la connessione Antigravity — Claude Code,
OpenClaw e OpenCode vengono citati —, pena la sospensione dell'account. aipmt
non legge né riutilizza il token: avvia il binario ufficiale nella
[modalità headless](https://antigravity.google/docs/cli/headless/) che Google
documenta per gli script e la CI. Un membro di Google ha giudicato «standard»
avviare `agy -p` da uno script locale per il proprio lavoro
([forum ufficiale, 25 settembre 2026, risposta non vincolante](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nessun testo chiarisce il caso di uno strumento distribuito come questo.

**Solo documenti pubblici.** Secondo la sezione 5 delle medesime condizioni, le
interazioni — prompt, risposte, metadati — possono essere usate per migliorare i
prodotti e il machine learning di Google ed essere esaminate da persone,
anche con un abbonamento a pagamento. La disattivazione passa attraverso l'impostazione
`enableTelemetry`, il cui effetto non è documentato e che aipmt non imposta; le vostre impostazioni
di agy non vengono trasferite nel suo ambiente isolato. Non fatevi passare nulla di riservato.
### Sull'abbonamento Claude: `--use_claude_code`

Stesso principio con `claude`, la CLI ufficiale di Claude Code, in modalità `-p`: per
chi paga Claude Pro o Max, la traduzione viene scalata dalla quota
dell'abbonamento anziché essere fatturata per token. Da non confondere con
`--use_claude`, l'API di Anthropic, fatturata in base all'utilizzo.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Non rimane aperto alcun canale a pagamento e ogni chiamata lo dimostra.** Claude
  Code riceve dal vostro ambiente soltanto un elenco chiuso di variabili: nessuna
  chiave API, nessun token, nessun provider cloud, nessun indicatore della sessione Claude Code
  dalla quale verrebbe avviato aipmt. Prima del primo segmento, `claude auth status` deve
  mostrare la connessione tramite abbonamento, senza chiave Console, e `/usage`, che non consuma
  alcuna quota, deve confermarlo; ogni chiamata lo conferma a sua volta nel proprio
  evento di inizializzazione, altrimenti la risposta viene rifiutata.
- **Disattivate l'«extra usage»** (claude.ai, Impostazioni → Utilizzo) affinché
  il costo rimanga pari a zero: se attivato, subentra quando una finestra è esaurita e
  fattura senza mostrare alcun errore. aipmt interrompe la traduzione non appena il resoconto
  della quota di una chiamata lo segnala, ma quella chiamata è già stata conteggiata.
- **Quota condivisa con le vostre sessioni Claude Code.** Ogni chiamata riporta
  l'utilizzo delle finestre di 5 ore e della settimana; oltre l'80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), non viene avviato alcun segmento aggiuntivo, per non
  esaurire ciò che serve al vostro lavoro.
- **Confinamento.** Ogni chiamata viene eseguita senza strumenti, in una directory privata ed
  effimera, in modalità senza personalizzazione: né i vostri `CLAUDE.md`, né i vostri plugin,
  hook, server MCP o impostazioni vengono caricati, e nulla della
  sessione viene conservato. Gli allegati sono disattivati: un `@chemin` nel vostro documento
  rimane testo e non apre alcun file (verificato).
- **Modelli**: `sonnet` per impostazione predefinita, con effort `low`, e anche in `--eco`:
  `--eco` non cambia nulla in questo percorso. Misurato sugli stessi documenti, `haiku`
  è due volte più lento — ragiona senza che sia possibile impedirglielo — a fronte
  di un costo appena inferiore, mentre `opus` rifiuta contenuti di biologia (punto
  successivo). Entrambi rimangono accessibili tramite `--model`; questi alias seguono
  l'ultimo modello della rispettiva famiglia. `fable` e le varianti `[1m]` vengono rifiutati,
  perché utilizzano crediti a pagamento. `--reasoning_effort` regola l'effort,
  dal quale una traduzione non trae alcun vantaggio: il ragionamento misurato è nullo o quasi.
- **Opus rifiuta alcuni contenuti di biologia.** Le sue protezioni sono più
  rigorose di quelle di Sonnet e il messaggio di errore di Anthropic avverte che
  «a volte possono segnalare attività affini alla ricerca biologica». Verificato: una breve notizia di
  monitoraggio su 279 molecole generate ha fatto rifiutare l'articolo nelle quattordici
  lingue. Non viene scritto nulla: aipmt rifiuta la risposta interrotta, indica le
  protezioni e consiglia `--model sonnet`.
- Rifiutato in CI (se `CI` o `GITHUB_ACTIONS` è definito) e su Windows (non verificato).
- Variabili: `AIPMT_CLAUDE_BIN` (altrimenti `PATH`, poi `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (secondi per segmento, valore predefinito 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (valore predefinito 0.8), `CLAUDE_CONFIG_DIR` (l'account di
  Claude Code, mai ricavato da un `.env` di progetto); directory di lavoro in
  `XDG_CACHE_HOME/aipmt/claude-code` (valore predefinito `~/.cache`).

**Condizioni d'uso: è il vostro account a essere coinvolto.** La
[pagina legale di Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
non impedisce «a un utente finale di accedere al binario Claude Code non modificato
con il proprio abbonamento Claude»: è ciò che fa aipmt, che avvia il
binario ufficiale e non legge mai il token. Tuttavia Anthropic «non consente
agli sviluppatori di terze parti […] di instradare richieste tramite le credenziali dei piani Free, Pro o Max
per conto dei propri utenti», preferisce la chiave API per gli strumenti
di terze parti, «inclusi i progetti open source», e si riserva di addebitare il loro
utilizzo sui crediti a pagamento
([guida di Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nessun testo chiarisce il caso di uno strumento distribuito che avvia il binario.

**Dati**: sugli account Free, Pro e Max, l'addestramento dei modelli
si applica anche a Claude Code quando l'impostazione della privacy lo consente
([pagina sui dati](https://code.claude.com/docs/en/data-usage)). aipmt non conserva
alcuna trascrizione locale (`--no-session-persistence`). Non fatevi transitare
nulla di riservato.

### Verso il provider preferito: `--use_opencode`

[OpenCode](https://opencode.ai) è un agente di programmazione open source (MIT) che
instrada verso i provider configurati al suo interno: chiave API, abbonamento,
gateway OpenCode Zen (modelli gratuiti, senza account) o modello locale. Due
percorsi sono stati verificati integralmente qui, Zen e Ollama.

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

- una configurazione inline, prioritaria rispetto alla vostra, definisce un agente `aipmt`
  al quale sono vietati tutti gli strumenti (`permission: { "*": "deny" }`), condivisione della
  sessione disattivata, `--pure`, mai `--auto`;
- directory di lavoro effimera e vuota, con `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` impostati — senza di essi, OpenCode inserisce nel
  prompt l'`AGENTS.md` della directory corrente e `~/.claude/CLAUDE.md`. Il
  `~/.config/opencode/AGENTS.md` globale continua a essere inserito, poiché OpenCode non consente
  di escluderlo;
- contratto di output: codice di uscita 0, nessun evento `error`, nessuna chiamata
  a strumenti, ultimo passaggio in `stop`, testo non vuoto e agente `aipmt`
  effettivamente caricato — un `--agent` sconosciuto non provoca il fallimento di OpenCode, che
  ripiega silenziosamente sull'agente di programmazione;
- non viene trasmessa alcuna chiave di `aipmt`, tranne `OPENCODE_API_KEY`, la chiave
  di OpenCode stesso. I provider si configurano in OpenCode, non nel
  `.env` di `aipmt`.

Da sapere:

- I modelli gratuiti di Zen cambiano, hanno limiti non documentati e
  le loro conversazioni possono essere utilizzate per l'addestramento: adatti a documentazione
  pubblica, non a contenuti privati.
- Un modello locale deve offrire almeno 16 k token di contesto, poiché i segmenti
  arrivano fino a 16.000 caratteri. Ollama spesso ne configura 4.096: occorre passare
  attraverso un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` non ha effetto; `--reasoning_effort` viene trasmesso così com'è come
  `--variant` di OpenCode.
- OpenCode registra ogni sessione in `~/.local/share/opencode/`.
- Variabili: `OPENCODE_BIN` (altrimenti `PATH`, poi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secondi per segmento, valore predefinito 600). `OPENCODE_CONFIG`
  viene passato così com'è a OpenCode.

Esempio di modello locale tramite Ollama, in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` disattiva la riflessione che Ollama attiva per impostazione predefinita su questi
modelli e che un Modelfile non può disattivare. Misurato su una frase di
sei parole: 919 token di riflessione e 68 secondi senza l'opzione, 9 token con essa.

### Verso oltre 400 modelli: `--use_openrouter`

OpenRouter è un router fatturato in base all'utilizzo, su un credito unico, che dà accesso a
modelli ospitati da terze parti, inclusi i modelli cinesi aperti che nessun
altro provider espone qui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` è obbligatorio. Un preflight, eseguito prima di qualsiasi addebito, gestisce
due particolarità dell'instradamento:

- **Uno stesso modello è servito da decine di host con limiti
  diversi** — per `z-ai/glm-5.3-flash`, 23 host, uno dei quali limitato a
  2.048 token di output. Il preflight legge `/api/v1/models/{modèle}/endpoints`,
  esclude gli host con meno di 8.000 token di output o con stato degradato e
  fissa gli altri tramite `allow_fallbacks: false`.
- **Il ragionamento viene fatturato alla tariffa dell'output** — 107 token contro 2 per
  una risposta «OK» di `z-ai/glm-5.2`. È disattivato per impostazione predefinita; i modelli
  che lo impongono ricevono l'effort minimo che accettano, poiché l'impostazione predefinita del
  catalogo potrebbe saturare l'output prima della fine della traduzione.
  `--reasoning_effort` mantiene la priorità.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La finestra di contesto proviene dal catalogo. Un modello con meno di 16.400 token viene
  rifiutato prima di qualsiasi chiamata: 8.400 per il prompt e il segmento, almeno
  8.000 per l'output.
- Uno slug assente dal catalogo, un catalogo non raggiungibile o l'assenza
  di un host che rispetti il limite interrompono il comando.
- `finish_reason=length` con un output vuoto indica un budget consumato dal
  ragionamento, non un troncamento: il messaggio distingue i due casi.
- `--eco` non ha effetto.
- Variabili: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (valore predefinito `https://openrouter.ai/api/v1`, `https://`
  richiesto), `OPENROUTER_TIMEOUT` (valore predefinito 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (valore predefinito 30).

### Nota di traduzione

`--add_translation_note` aggiunge una nota, in `bottom` (impostazione predefinita), `top` (dopo il
front matter) o `both` (`--note_position`), nel formato `legacy` (paragrafo in
grassetto, impostazione predefinita) o `marker` (`--note_format`). Il formato `marker` è una
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
**Scritte** indica i file lasciati passare dalle protezioni; **Senza
discrepanze** quelli nei quali `scripts/compare_structure.py` non rileva nulla: stesso numero di
sezioni, sottotitoli, link, URL distinti, blocchi di codice,
codici inline, righe di tabella, blocchi di citazione e parole in grassetto.

«Senza discrepanze» significa «nulla di rilevato», non «identico»: il comparatore
conta gli elementi senza leggerne il contenuto. Non segnala né un titolo di
livello 4 eliminato, né il testo di un codice inline sostituito, né una bandiera
scambiata, né un link interno reso con una parentesi di troppo,
`[texte]((#ancre))`, che non porta più da nessuna parte, e non valuta la
lingua.

### Articolo di monitoraggio denso, modalità `--news`

Un'edizione del [monitoraggio IA di jls42.org](https://jls42.org/fr/news):
589 righe, 140 link, 21 sezioni, 3 citazioni inglesi protette. Campagna
del 4 e 5 settembre 2026.

| Modello                                          | Accesso              | Scritte | Senza discrepanze | Mediana/lingua |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | abbonamento Google  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abbonamento Google  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abbonamento ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | abbonamento Claude  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | abbonamento Claude  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | locale              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abbonamento Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | abbonamento Claude  | 0/14    | ❌ 0/14      | —              |

Grok è stato misurato nuovamente il 9 settembre su un'altra edizione dello stesso monitoraggio
(356 righe): 9 lingue scritte su 14, 8 senza discrepanze. È questo il dato
riportato nella tabella iniziale. Tre campagne interrotte non sono
riportate: `qwen3.5-27b` (9 lingue) e `kimi-k2.6` (4) per mancanza di credito,
`z-ai/glm-5.3-flash`, i cui due fallimenti erano dovuti a un'impostazione di ragionamento
che il provider sta correggendo. Le righe OpenRouter sono state misurate con le
impostazioni predefinite del router, prima di `--use_openrouter`; `z-ai/glm-5.2`,
misurato nuovamente con il provider fornito, restituisce lo stesso 14/14. I dati sono stati
ricalcolati il 10 settembre con il comparatore attuale: `qwen3.8-flash` e
`qwen3.7-flash` guadagnano ciascuno una lingua rispetto alla prima
pubblicazione, mentre gli altri rimangono invariati.

Le righe `--use_antigravity` sono state misurate il 26 settembre sullo stesso
articolo, con quattro traduzioni in parallelo: `gemini-3.7-flash-medium` al mattino,
`gemini-3.8-flash-medium` nel pomeriggio. In inglese, ciascuno ha rimosso autonomamente
le tre righe di traduzione francese sotto le citazioni, senza inventare alcuna
bandiera, e le citazioni inglesi sono rimaste intatte: la pulizia di fallback non ha
dovuto fare nulla. In `--eco` (`gemini-3.7-flash-low`), soltanto su quattro lingue
(en, ja, ar, hi): 4 scritte su 4, tutte senza discrepanze, mediana di 1 min 52 s.
Controprova nello stesso giorno su un'edizione più recente del monitoraggio,
quella del 25 settembre (438 righe, 2 citazioni inglesi), tradotta al di fuori del
blog da `gemini-3.7-flash-medium`: 14 scritte su 14, tutte senza discrepanze, da 87 a
128 s per lingua.

Le righe `--use_claude_code` sono state misurate il 26 settembre sullo stesso
articolo, con quattro traduzioni in parallelo e con effort `low`. Con `sonnet`, le
citazioni inglesi sono rimaste intatte in tutte e quattordici le lingue e, in inglese, il
modello ha rimosso autonomamente le righe di traduzione francese, senza inventare alcuna
bandiera. `opus` non ha scritto alcuna lingua: in ognuna, le sue protezioni hanno
interrotto la risposta all'ultimo segmento, a causa di una breve notizia su 279 molecole
generate per un sito di legame. Inviata da sola, questa breve notizia viene rifiutata
nella categoria «bio»; `sonnet` l'ha tradotta ovunque. `haiku` scrive
tutte e quattordici le lingue; in tre (en, pl, ro), un titolo di sezione passa dal
livello 2 al livello 1. Ragiona senza che sia possibile impedirglielo — il 61% dei
suoi token di output —, da cui un tempo più che doppio rispetto a `sonnet`.

Le righe `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` sono
state misurate il 18 ottobre tramite l'API di Anthropic, sullo stesso articolo, con quattro
traduzioni in parallelo per modello. Sonnet 5.5 rifiuta di disattivare la propria
riflessione: aipmt gli invia l'impostazione minima che accetta e le sue
risposte non ne contengono alcuna. Scrive tutte e quattordici le lingue senza discrepanze e senza
rielaborare alcun segmento; in inglese, ha rimosso autonomamente le righe della
traduzione francese, senza inventare alcuna bandiera, e le citazioni inglesi sono
rimaste intatte ovunque. Haiku 5.5 è misurato con la sua riflessione adattiva: con la riflessione
disattivata, lasciava interi paragrafi in francese, che la protezione rifiuta —
3 lingue scritte su 14. Entrambi gli Haiku inciampano sulla stessa breve notizia: Haiku 5.5
modifica il livello del suo titolo o lo duplica in giapponese, coreano e
cinese; Haiku 4.5 lo porta al livello 1 in sette lingue e lo lascia in
francese in giapponese. Haiku 4.5 costa 3,67 $ per entrambi i documenti nelle
quattordici lingue, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README di questo progetto, Markdown standard

Revisione congelata il 9 settembre 2026: 785 righe, 285 codici inline, 40
chiusure di blocchi, 89 righe di tabella. Quattro traduzioni in parallelo.

| Modello                                         | Scritte | Senza scostamenti | Mediana/lingua | Elementi diversi                                                          |
| ----------------------------------------------- | ------- | ----------------- | -------------- | ------------------------------------------------------------------------- |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14          | 1 min 43 s     | nulla                                                                      |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14          | 1 min 48 s     | nulla                                                                      |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14          | 4 min 02 s     | nulla per lo strumento di confronto; link interni duplicati (en)           |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14          | 1 min 18 s     | nulla                                                                      |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14          | 2 min 06 s     | nulla                                                                      |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14          | 36 s           | una parola in grassetto (ja)                                               |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14          | 1 min 22 s     | una parola in grassetto (ko)                                               |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14          | 2 min 20 s     | una riga di tabella attaccata alla precedente (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14          | 2 min 56 s     | un link (sv), una parola in grassetto (zh)                                 |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14          | 6 min 46 s     | una parola in grassetto (ar, ja)                                           |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14          | 2 min 34 s     | una parola in grassetto (hi, ja, ko)                                       |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14          | 2 min 17 s     | 40 codici inline aggiunti in arabo; grassetto (hi, ja, ko)                 |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14          | 1 min 14 s     | 2 lingue rifiutate (ar, hi): alcuni codici inline persi nella restituzione |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14           | 2 min 44 s     | una sezione persa (ar, hi, ko); blocchi di codice aggiunti (ja, ko, ro, zh) |

Due campagne interrotte non sono valutate: Grok, sessione CLI scaduta
dopo dodici lingue (undici senza scostamenti), e `qwen3.8-flash`, HTTP 429 del suo
provider dopo due. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
non sono stati misurati nuovamente su questa revisione; su quella del 4 e 5 settembre,
più breve di 277 righe, ciascuno scriveva 9 traduzioni su 14, di cui rispettivamente 7
e 1 senza scostamenti.

Le righe `--use_antigravity` e `--use_claude_code` non sono state misurate sulla
revisione congelata, ma il 26 settembre su quella pubblicata con la 1.14.0 — e
le righe `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` il 18
ottobre, sulla stessa: 600 righe, 257 codici inline, 30 chiusure di blocchi, 85
righe di tabella. Più
breve di 185 righe, non può essere confrontata elemento per elemento con le altre righe;
queste righe, invece, sono confrontabili tra loro. Per quanto riguarda i link interni, che lo
strumento di confronto non verifica, `gemini-3.8-flash-medium` li ha mantenuti intatti
in tutte e quattordici le lingue, `gemini-3.7-flash-medium` li ha interrotti in italiano;
`sonnet` e `opus` li hanno mantenuti intatti ovunque, `haiku` li ha duplicati in
inglese; `claude-sonnet-5-5` e `claude-haiku-4-5` li hanno mantenuti intatti
in tutte e quattordici le lingue, `claude-haiku-5-5` nelle dodici che ha scritto.

### Quattro README di progetti noti

FastAPI, Ollama, tldr-pages e Vue.js, presi così come sono da GitHub — documenti
più semplici dei due precedenti. La campagna era rivolta ai modelli
in difficoltà; Gemini funge da termine di confronto.

| Modello                    | Ambito                     | Scritte | Senza scostamenti |
| ------------------------- | -------------------------- | ------- | ----------------- |
| `gemini-3.7-flash`        | 4 progetti × 14 lingue     | 56/56   | ✅ **55/56**      |
| `opencode/mimo-v2.5-free` | 4 progetti × 14 lingue     | 55/56   | ❌ 47/56          |
| `grok-4.6` (abbonamento)   | 4 progetti × ar, hi, ja, zh | 16/16   | ❌ 14/16          |
| `ollama/gpt-oss-20b-32k`  | 4 progetti × ar, hi, ja, zh | 15/16   | ❌ 9/16           |

### Cosa non sono queste misurazioni

- **Non una classifica esaustiva**: solo OpenRouter propone più di quattrocento
  modelli, ne sono stati misurati una quindicina.
- **Durate indicative**: da tre a sei traduzioni in parallelo a seconda
  delle campagne, e la velocità di un provider varia durante la giornata.
- **Osservazioni datate**: i modelli cambiano pur mantenendo lo stesso nome e i vostri
  documenti non sono i nostri.

Per ripetere la misurazione sui vostri documenti, su una copia congelata del file:

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

Sono necessarie entrambe le righe: senza `pip install -e .`, `python -m aipmt`
risponde `No module named aipmt`.

Strumenti per la qualità, facoltativi ma consigliati:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Le 28 traduzioni del repository (README e CHANGELOG, quattordici lingue) si
rigenerano con `./regen_translations.sh --force` — Codex e `gpt-5.6-sol` con
l'abbonamento ChatGPT predefinito, quattro in parallelo. `REGEN_PROVIDER` e
`REGEN_MODEL` cambiano il percorso: `antigravity` resta su un abbonamento, quello
di Google, e passa senza deroga; un'API a pagamento (`openai`, `gemini`,
`grok`, `openrouter`) viene rifiutata senza `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` impone un limite a ogni job (600 s, 1 800 s su Codex e
Antigravity). I dettagli degli strumenti sono in `CLAUDE.md`.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** — blog personale pubblicato in 15 lingue. La sua
  [rassegna quotidiana sull'IA](https://jls42.org/fr/news) viene tradotta ogni giorno
  da questo strumento e funge da documento di riferimento per le misurazioni precedenti.

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avvertenza

Questo programma è distribuito **senza alcuna garanzia**, secondo i termini delle
sezioni 15 e 16 della GPL v3: fornito «così com'è», senza garanzia di commerciabilità
né di idoneità a uno scopo particolare, e il suo autore non può essere
ritenuto responsabile per eventuali danni derivanti dal suo utilizzo. Il testo della
licenza prevale su questo riepilogo.

- **Rileggete prima di pubblicare.** Le protezioni coprono i blocchi di codice, il
  codice inline, gli URL, le ancore e le citazioni della modalità `--news` — non i
  titoli, le tabelle, il front matter o il significato delle vostre frasi.
- **I vostri documenti vengono inviati al provider scelto**, secondo le sue condizioni
  d'uso e la sua politica sui dati. Alcuni modelli gratuiti possono
  riutilizzare le vostre interazioni per l'addestramento e le condizioni di Antigravity
  consentono a Google di riutilizzarle e di farle esaminare da esseri umani,
  anche con un abbonamento a pagamento; un modello locale è l'unica soluzione che impedisce
  a qualsiasi dato di uscire dalla vostra macchina.
- **Le chiamate API vi vengono addebitate.** Questo programma non impone un limite alla
  spesa: un documento lungo, un nuovo tentativo dopo un errore o un modello che ragiona
  molto costano di più.
- **Le misurazioni pubblicate sono osservazioni datate**, non garanzie.

I nomi dei prodotti e delle società citati appartengono ai rispettivi
proprietari. Questo progetto non è affiliato ad alcuno di essi.

**Articolo tradotto dal francese all’italiano con gpt-5.6-sol.**
