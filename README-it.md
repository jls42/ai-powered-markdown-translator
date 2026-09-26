# Traduttore Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Qualità del codice</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduce file Markdown da una lingua all'altra preservando la
struttura: blocchi di codice, codice inline, URL, ancore, tabelle e front
matter. Dieci modi per chiamare un modello — cinque API, tre abbonamenti senza
fatturazione a consumo, due router — e una misurazione pubblicata di ciò che ciascun
modello preserva realmente.

## In breve

- **Dieci percorsi di provider**: API OpenAI, Mistral, Claude, Gemini e Grok;
  abbonamenti ChatGPT (Codex), Grok e Google (Antigravity) senza fatturazione a
  consumo; router OpenCode (open source, gratuito o locale) e OpenRouter
  (oltre 400 modelli).
- **Nessun errore dovuto a un token perso**: blocchi di codice, codice inline,
  URL, ancore e citazioni vengono sostituiti da token prima della chiamata e
  verificati al ritorno. Se ne manca anche solo uno, il file non viene scritto.
- **Documenti lunghi**: segmentazione in base alla finestra di contesto del modello.
- **Modalità `--news`**: citazioni in inglese protette e bandiere gestite per
  lingua, per gli articoli di rassegna stampa.
- **Modalità `--eco`**: modelli veloci ed economici.
- **Nota di traduzione** opzionale, in alto, in basso o in entrambe le posizioni.

## Installazione

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 o versione successiva. Per l'installazione dal repository, vedere
[Contribuire](#contribuire).

## Configurazione

Le chiavi vengono lette in tre posizioni, dalla priorità più alta alla più bassa; ciascuna
colma solo ciò che la precedente lascia vuoto.

|     | Dove                                          | Per cosa                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabili d'ambiente                          | CI, container, deroga puntuale        |
| 2   | `.env` della directory corrente (o di una cartella superiore) | una chiave specifica per un progetto  |
| 3   | `~/.config/aipmt/.env`                        | installato una volta, vale ovunque    |

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

**Il file `.env` di un progetto non può né reindirizzare le chiamate né scegliere il programma
eseguito.** Fornisce chiavi, mai una destinazione né un binario: qualsiasi
variabile che inizi con `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, i proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), i certificati store (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` vengono ignorati, con un avviso. Un repository clonato non deve
poter sottrarre la tua chiave, né farti eseguire il proprio programma alla
prima traduzione. Questo file viene letto anche senza interpolazione:
`NOM=${OPENAI_API_KEY}` non vi ricopia la chiave. Inserisci queste variabili
nell'ambiente o in `~/.config/aipmt/.env`.

Variabili opzionali: `XAI_BASE_URL` (predefinito `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secondi per chiamata, predefinito 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predefinito 600), `GROK_BIN`, `GROK_HOME` (predefinito `~/.grok`), `GROK_TIMEOUT`
(predefinito 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (predefinito 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (predefinito 600), `OPENROUTER_BASE_URL`
(`https://` richiesto), `OPENROUTER_TIMEOUT` (predefinito 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (predefinito 30). Ciascuna è dettagliata nella
sezione del rispettivo provider.

## Primi passi

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` tradotto in spagnolo genera `document-es.md` in `--target_dir`;
con `--include_model`, `document-es-gpt-5.6-terra.md`. L'estensione diventa
sempre `.md` — `article.mdx` produce `article-en.md` — tranne con
`--keep_filename`, che mantiene il nome originale. Una traduzione già presente
viene saltata se non si specifica `--force`.

Codici di uscita: `0` se tutto è andato a buon fine o è stato saltato, `1` se rimane un file
con errori (elencati sullo standard error), `2` se il problema riguarda la configurazione.
Un file non riuscito non viene mai scritto, anche nel caso in cui la scrittura stessa fallisca:
il contenuto viene scritto temporaneamente a parte e poi rinominato. È sufficiente rieseguire il comando.

## Quale modello scegliere

Misurato su due documenti reali, tradotti nelle stesse quattordici lingue da
ciascun modello. **La cifra indica il numero di lingue, su quattordici, in cui la
traduzione viene scritta e non differisce in nulla rispetto alla fonte.**

| Modello              | Come accedere                     | Articolo di rassegna denso | Questo README| Cosa differisce e su quante lingue                                                                                                   |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | abbonamento Google (Antigravity)  | ✅ 14/14                | ✅ 14/14     | nulla, su nessuno dei due documenti                                                                                                  |
| **Gemini 3.7 Flash** | chiave API Google                 | ✅ 14/14                | ⚠️ 13/14     | 1 lingua su 14: una parola in più in grassetto (ja)                                                                                  |
| **Gemini 3.7 Flash** | abbonamento Google (Antigravity)  | ✅ 14/14                | ⚠️ 13/14     | 1 lingua su 14: una parola in meno in grassetto (ko)                                                                                 |
| **GPT-5.6 Sol**      | abbonamento ChatGPT o chiave OpenAI| ✅ 14/14                | ⚠️ 12/14     | 2 lingue su 14: una parola in meno in grassetto (ar, ja)                                                                             |
| **GLM-5.2**          | chiave OpenRouter                 | ✅ 14/14                | ⚠️ 11/14     | 3 lingue su 14: una parola in meno in grassetto (hi, ja, ko)                                                                         |
| Claude Sonnet 5      | chiave API Anthropic              | ⚠️ 11/14                | ⚠️ 12/14     | 3 lingue sull'articolo: un blocco di codice in più apparso (es, de, hi); 2 su questo README: un link senza formattazione (sv), una parola in grassetto (zh) |
| Qwen 3.7 Flash       | chiave OpenRouter                 | ❌ 8/14                 | ⚠️ 10/14     | 1 lingua rifiutata sull'articolo, altre 5 divergono; su questo README, una quarantina di parole inserite in `code` (ar)  |
| Grok 4.6             | abbonamento Grok                  | ❌ 8/14                 | non valutato | 5 lingue rifiutate su 14, a causa di codici inline e URL non restituiti; l'olandese diverge completamente                             |
| GPT-OSS 20B          | modello locale (Ollama)           | ❌ 7/14                 | non rimisurato| 4 lingue rifiutate su 14: il modello lasciava passaggi in francese, il controllo di guardia li ha bloccati                          |
| MiMo v2.5 (gratuito) | OpenCode Zen, senza account       | ❌ 11/14                | non rimisurato| 1 lingua rifiutata; una sezione persa in polacco                                                                                     |
| Mistral Large        | chiave API Mistral                | ❌ 5/14                 | ❌ 1/14      | **un'intera sezione scompare**: 1 lingua sull'articolo (hi), 3 su questo README (ar, hi, ko) — e 3 lingue rifiutate sull'articolo   |
| DeepSeek V4 Flash    | chiave OpenRouter                 | ❌ 3/14                 | non rimisurato| 10 lingue rifiutate su 14; 37 minuti per lingua                                                                                     |

|     | Cosa indica il simbolo                                                                                                                                                                                |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | tutte le quattordici lingue tradotte, e nulla differisce dalla fonte                                                                                                                                  |
| ⚠️  | tutte le quattordici lingue tradotte; ciò che differisce riguarda la **formattazione** — una parola in grassetto, un `code`, un link che perde le parentesi quadre. Nessun testo, nessun URL, nessun blocco di codice, nessuna sezione mancante |
| ❌  | almeno una lingua non è stata tradotta — il file è rifiutato, non scritto — **oppure** mancano dei contenuti in un file scritto                                                                      |

Punti chiave:

- **Una traduzione rifiutata non è una traduzione danneggiata.** Quando manca un token
  al ritorno, il file non viene scritto e la lingua viene conteggiata come
  rifiutata. È quanto accade a Grok sull'articolo: quattro codici inline e
  tre URL persi fin dal primo segmento, sulle cinque scritture non latine.
- **Questa rete di protezione non copre titoli, tabelle, front matter né
  testo.** Un modello che rimuove una sezione restituisce un file che lo strumento scrive
  senza problemi — è il caso di Mistral. Questi elementi non sono
  sostituibili con un token e gli attuali controlli non li verificano;
  `scripts/compare_structure.py` rileva una sezione persa, ma solo a posteriori.
- **Grok non ha una valutazione su questo README**: la sua sessione CLI è scaduta dopo dodici
  lingue, di cui undici senza discrepanze. Una campagna interrotta non viene valutata.
- **La densità del documento conta più della lingua.** Grok regge su
  README ordinari ma fallisce su un articolo denso di link, persino in
  olandese.

Date e documenti: la colonna "Questo README" è stata misurata il 9 settembre 2026
su una revisione bloccata di questo file (785 righe, 285 codici inline, 89 righe
di tabella), ritoccata da allora — tranne le due righe relative ad Antigravity, misurate il
26 settembre sulla revisione pubblicata con la 1.14.0, più breve (600 righe,
257 codici inline, 85 righe di tabella). La colonna "Articolo di rassegna
denso" proviene dalla campagna del 4 e 5 settembre su un articolo di 589 righe,
ad eccezione della riga di Grok, rimisurata il 9 settembre su un'altra edizione della stessa
rassegna, e delle due righe di Antigravity, misurate il 26 settembre sullo stesso
articolo.
Le tabelle complete, le durate e il protocollo si trovano in
[Misurazioni dettagliate](#misure-dettagliate).

## Tutte le opzioni

| Opzione                  | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Singolo file Markdown da tradurre (alternativa a `--source_dir`)                                              |
| `--source_dir`           | Directory di origine contenente i file Markdown (predefinito: `content/posts`)                                 |
| `--target_dir`           | Directory di output per i file tradotti (predefinito: `traductions_en`)                                         |
| `--source_lang`          | Lingua di origine (predefinito: `fr`)                                                               |
| `--target_lang`          | Lingua di destinazione (predefinito: `en`)                                                          |
| `--model`                | Modello specifico da utilizzare                                                                               |
| `--eco`                  | Usa i modelli economici                                                                                       |
| `--use_mistral`          | Usa l'API Mistral AI                                                                                          |
| `--use_claude`           | Usa l'API Claude                                                                                              |
| `--use_gemini`           | Usa l'API Gemini                                                                                              |
| `--use_grok`             | Usa l'API xAI (Grok) — richiede `XAI_API_KEY`                                                                |
| `--use_codex`            | Usa la CLI Codex sulla quota dell'abbonamento ChatGPT                                                         |
| `--use_grok_cli`         | Usa la CLI Grok sulla quota dell'abbonamento Grok                                                             |
| `--use_antigravity`      | Usa la CLI Antigravity (`agy`) sulla quota dell'abbonamento Google AI Pro o Ultra                    |
| `--use_opencode`         | Usa OpenCode (open source) verso il provider configurato in OpenCode; richiede `--model provider/modèle`                 |
| `--use_openrouter`       | Usa OpenRouter — richiede `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                                                     |
| `--force`                | Forza la ritraduzione                                                                                         |
| `--keep_filename`        | Mantieni il nome del file originale                                                                           |
| `--news`                 | Modalità notizie: protegge le citazioni in EN, gestisce le bandiere per lingua                                |
| `--add_translation_note` | Aggiungi una nota di traduzione                                                                               |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinito) o `both`                           |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) o `marker`                     |
| `--include_model`        | Includi il nome del modello nel file di output                                                                |
| `--reasoning_effort`     | Livello di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`  |

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

| Provider    | Qualità (predefinito)                                 | Economico (`--eco`)       |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (anche `terra` e `luna` tramite `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` obbligatorio                | idem — `--eco` senza effetto |
| OpenRouter  | `--model fournisseur/modèle` obbligatorio             | idem — `--eco` senza effetto |

### Con l'abbonamento ChatGPT: `--use_codex`

Controlla la CLI Codex ufficiale: la traduzione viene scalata dalla quota
dell'abbonamento ChatGPT, senza chiave API né fatturazione a consumo.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Il file binario viene cercato in `CODEX_BIN`, poi nel `PATH`, poi nel pacchetto
  `openai-codex-cli-bin`. `~/.codex/auth.json` non viene mai letto.
- `OPENAI_API_KEY` e `CODEX_API_KEY` vengono rimosse dall'ambiente del
  sottoprocesso: una chiave presente non fa mai passare all'API.
- Ogni segmento costa almeno un "messaggio" della finestra di 5 ore — due
  se la sua convalida fallisce e viene ritentato. OpenAI dichiara, a titolo
  di stima, 250-2.000 messaggi/5 ore per `gpt-5.6-luna` (`--eco`) e
  10-100 per `gpt-5.6-sol` su un piano Plus.
- Anche `--model gpt-5.6-terra` e `--model gpt-5.6-luna` passano tramite
  l'abbonamento. Un modello a cui l'account non ha diritto restituisce un 400 « model is
  not supported when using Codex with a ChatGPT account ».
- Più lento di un'API, e il divario cresce con le dimensioni del documento: su questo README,
  6 min e 46 s per lingua come valore mediano con `gpt-5.6-sol`, contro 36 s per
  `gemini-3.7-flash`.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definito): l'abbonamento si autentica
  tramite un file di sessione personale, che non ha motivo di trovarsi su un runner
  condiviso.
- Variabili: `CODEX_BIN`, `CODEX_TIMEOUT` (secondi per segmento, predefinito 600).

### Con l'abbonamento Grok: `--use_grok_cli`

Stesso principio con la CLI ufficiale Grok Build, con l'abbonamento SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Isolamento più debole rispetto a Codex.** La sandbox OS di Grok non si applica
  su molte postazioni Linux recenti (AppArmor, socket di runtime
  dei container), e un profilo che non può essere applicato si avvia senza isolamento in
  modo silenzioso. Lo script non richiede quindi alcun profilo per impostazione predefinita, lo segnala, e
  si basa sulle regole `--deny` della CLI, tra cui il catch-all `*` — l'unico
  livello che rifiuta di avviarsi anziché rimuovere la protezione senza
  avvertire. `GROK_TRANSLATE_SANDBOX=read-only` richiede la sandbox OS, e l'avvio
  fallisce se la macchina non può soddisfarla.
- La quota è settimanale, condivisa con Chat, Imagine e Voice, e nessun
  comando consente di leggerla: un batch può intaccare l'utilizzo conversazionale
  senza alcuna segnalazione.
- Variabili: `GROK_BIN`, `GROK_HOME` (directory della CLI, predefinito `~/.grok`),
  `GROK_TIMEOUT` (predefinito 900), `GROK_TRANSLATE_SANDBOX`.

### Con l'abbonamento Google: `--use_antigravity`

Stesso principio con `agy`, la CLI ufficiale di Antigravity: per chi paga Google
AI Pro o Ultra, la traduzione viene scalata dalla quota dell'abbonamento invece
di essere fatturata a token. È l'unica via per accedere a questa quota: Gemini CLI non
supporta più questi account dal 18 giugno 2026
([annuncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e l'SDK di Antigravity accetta solo una chiave API o un progetto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nessuna via a pagamento rimane aperta.** agy riceve dal vostro
  ambiente solo un elenco chiuso di variabili — `PATH`, lingua e fuso orario,
  terminale, identità, proxy e certificati, bus di sessione — e nessuna chiave:
  diverse delle sue variabili reindirizzano una chiamata senza mostrare nulla (misurato:
  una invia il documento a un gateway di terze parti, un'altra a un progetto
  Google Cloud fatturato), e una lista di esclusione ne tralasciava a ogni revisione.
  Prima di qualsiasi segmento, `agy -p /config`, che non consuma alcuna quota, deve mostrare
  i crediti IA a pagamento disattivati, senza chiave API né progetto Google Cloud — un'impostazione
  assente equivale a un rifiuto —, altrimenti non viene tradotto nulla; il registro di ogni
  chiamata deve poi attestare l'abbonamento (`authMethod=consumer`), altrimenti la
  risposta viene rifiutata.
- **Isolamento.** Ogni chiamata viene eseguita in una home directory privata e
  usa e getta, con un agente di traduzione senza strumenti: le vostre impostazioni, regole,
  plugin, server MCP e hook di agy non vi hanno accesso, nulla viene aggiunto alla vostra
  cronologia e la connessione rimane nel portachiavi, che aipmt non legge mai.
  Un agente non trovato fa ricadere agy, silenziosamente, sul suo agente di programmazione
  e sui relativi strumenti: un'intera riga del registro deve confermare l'agente corretto — un
  documento che cita questo messaggio non la sostituisce —, altrimenti l'operazione viene rifiutata.
- **Piattaforme**: Linux, in una sessione provvista di portachiavi (bus di sessione
  D-Bus, Secret Service); macOS è supportato, sebbene non sia stato testato. Rifiutato
  su Windows, dove agy non legge le variabili che isolano ciascuna chiamata, e
  su Linux senza bus di sessione — sessione SSH, container, server: agy vi
  memorizza il proprio token in un file di `~/.gemini`, che l'isolamento nasconde. Il
  rifiuto avviene prima di qualsiasi avvio, con la relativa motivazione, invece di attendere
  un minuto per un codice di accesso.
- **Modelli**: quelli di `agy models`. I Gemini indicano il livello di effort nel loro nome
  (`gemini-3.8-flash-medium`…): un nome senza suffisso viene rifiutato prima della chiamata,
  e `--reasoning_effort` è privo di effetto. Come impostazione predefinita `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` in `--eco`; le campagne che li hanno stabiliti sono
  descritte in [Misure dettagliate](#misure-dettagliate). Claude e GPT-OSS
  hanno una propria quota, molto più ridotta: circa l'1% della finestra di
  5 ore per chiamata misurata, contro lo 0,05% in Flash.
- **Quota**: per gruppo, una finestra di 5 ore e una settimanale, proporzionale
  al costo in token. Misurato sull'account dell'autore: circa
  16 punti della finestra di 5 ore per milione di caratteri sorgente in
  `gemini-3.8-flash-medium`, 14 in `gemini-3.7-flash-medium` e da 7 a 8 con
  effort basso — un README di 40.000 caratteri costa quindi poco più di mezzo
  punto. Il limite settimanale, invece, dipende dal livello. Il nuovo tentativo segue
  quanto agy dichiara riprovabile; in caso contrario, una finestra esaurita non viene mai
  ritentata: causa il fallimento di ciascun file fino al ripristino
  mostrato da `/usage`.
- **Più lento dell'API**: sull'articolo denso delle misurazioni, 3 min e 59 s per
  lingua come valore mediano in `gemini-3.8-flash-medium` e 3 min e 14 s in
  `gemini-3.7-flash-medium`, contro 1 min e 18 s per Gemini 3.7 Flash tramite API.
- **Interruzione**: Ctrl-C, o un terminale chiuso, arrestano agy insieme al
  comando invece di lasciargli completare il turno a carico della quota; lo stesso vale
  per Codex, Grok CLI e OpenCode. Con `nohup`, la traduzione continua.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definito): la connessione risiede in un
  portachiavi personale. Su un runner, `--use_gemini` con `GOOGLE_API_KEY`.
- Variabili: `AGY_BIN` (altrimenti il `PATH`, poi `~/.local/bin/agy`),
  `AGY_TIMEOUT` (secondi per segmento, avvio compreso, predefinito 900).

**Termini di servizio: la responsabilità ricade sul vostro account.** I
[termini di Antigravity](https://antigravity.google/terms) (sezione 6) e le relative
[FAQ](https://antigravity.google/docs/faq/) vietano l'accesso al servizio
tramite software di terze parti utilizzando il login di Antigravity — Claude Code,
OpenClaw e OpenCode sono espressamente citati —, a pena di sospensione dell'account. aipmt
non legge né riutilizza il token: avvia il file binario ufficiale nella
[modalità headless](https://antigravity.google/docs/cli/headless/) che Google
documenta per script e CI. Un membro di Google ha definito "standard"
l'avvio di `agy -p` da uno script locale per il proprio lavoro
([forum ufficiale, 25 settembre 2026, risposta non vincolante](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nessun testo affronta nello specifico il caso di uno strumento distribuito come questo.

**Solo documenti pubblici.** Ai sensi della sezione 5 degli stessi termini, le
interazioni — prompt, risposte, metadati — possono essere utilizzate per migliorare i
prodotti e il machine learning di Google ed essere esaminate da revisori
umani, anche per gli abbonamenti a pagamento. L'opt-out avviene tramite l'impostazione
`enableTelemetry`, dal funzionamento non documentato, che aipmt non imposta; le vostre configurazioni
di agy non vengono ereditate nel suo ambiente isolato. Non elaborate alcun contenuto riservato tramite questo canale.

### Verso il provider di propria scelta: `--use_opencode`

[OpenCode](https://opencode.ai) è un agente di codice open source (MIT) che
instrada verso i provider configurati al suo interno: chiave API, abbonamento,
gateway OpenCode Zen (modelli gratuiti, senza account) o modello locale. In
questa sede sono stati testati end-to-end due percorsi: Zen e Ollama.

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

`--model` è obbligatorio: senza di esso, OpenCode ricadrebbe su un modello gratuito
i cui scambi possono essere utilizzati per l'addestramento, e questa scelta non viene effettuata al
vostro posto.

Isolamento a ogni chiamata:

- una configurazione inline, prioritaria rispetto alla vostra, definisce un agente `aipmt`
  a cui vengono negati tutti gli strumenti (`permission: { "*": "deny" }`), condivisione della
  sessione disattivata, `--pure`, mai `--auto`;
- directory di lavoro usa e getta e vuota, `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` impostati — senza di essi, OpenCode inietta nel
  prompt l'`AGENTS.md` della directory corrente e `~/.claude/CLAUDE.md`. Il
  `~/.config/opencode/AGENTS.md` globale rimane comunque iniettato, poiché OpenCode non consente
  di escluderlo;
- contratto di output: codice di ritorno 0, nessun evento `error`, nessuna chiamata
  a strumenti, ultimo passaggio in `stop`, testo non vuoto e l'agente `aipmt`
  effettivamente caricato — un `--agent` sconosciuto non fa fallire OpenCode, che
  ricade silenziosamente sull'agente di programmazione;
- non viene trasmessa alcuna chiave di `aipmt`, tranne `OPENCODE_API_KEY`, la chiave
  di OpenCode stesso. I provider si configurano in OpenCode, non nel
  `.env` di `aipmt`.

Da sapere:

- I modelli gratuiti di Zen sono mutevoli, presentano limiti non documentati e
  i relativi scambi possono essere utilizzati per l'addestramento: adatti per documentazione
  pubblica, non per contenuti riservati.
- Un modello locale deve offrire almeno 16k token di contesto, dato che i segmenti
  raggiungono fino a 16.000 caratteri. Ollama ne configura spesso 4.096: passare
  attraverso un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` è privo di effetto; `--reasoning_effort` viene trasmesso così com'è come
  `--variant` di OpenCode.
- OpenCode registra ogni sessione in `~/.local/share/opencode/`.
- Variabili: `OPENCODE_BIN` (altrimenti il `PATH`, poi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secondi per segmento, predefinito 600). `OPENCODE_CONFIG`
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

`reasoningEffort: "none"` disattiva il ragionamento che Ollama attiva per impostazione predefinita su questi
modelli, e che un Modelfile non può disattivare. Misurato su una frase di
sei parole: 919 token di ragionamento e 68 secondi senza l'opzione, 9 token con essa.

### Verso più di 400 modelli: `--use_openrouter`

OpenRouter è un router fatturato a consumo, su un unico credito, posto davanti a
modelli ospitati da terze parti — inclusi i modelli aperti cinesi che nessun
altro provider espone qui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` è obbligatorio. Un preflight, eseguito prima di qualsiasi fatturazione, gestisce
due particolarità del routing:

- **Uno stesso modello è fornito da decine di provider di hosting con massimali
  diversi** — su `z-ai/glm-5.3-flash`, 23 host di cui uno limitato a
  2.048 token di output. Il preflight legge `/api/v1/models/{modèle}/endpoints`,
  esclude gli host al di sotto di 8.000 token di output o con stato degradato, e
  fissa gli altri con `allow_fallbacks: false`.
- **Il ragionamento viene fatturato alla tariffa di output** — 107 token contro 2 per
  una risposta "OK" di `z-ai/glm-5.2`. È disattivato per impostazione predefinita; i modelli
  che lo richiedono obbligatoriamente ricevono il livello di effort più basso accettato, poiché l'impostazione predefinita del
  catalogo potrebbe saturare l'output prima del completamento della traduzione.
  `--reasoning_effort` rimane prioritario.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La finestra di contesto proviene dal catalogo. Un modello al di sotto di 16.400 token viene
  rifiutato prima di qualsiasi chiamata: 8.400 per il prompt e il segmento, almeno 8.000 di output.
- Uno slug assente dal catalogo, un catalogo non raggiungibile o l'assenza
  di un host in grado di garantire il massimale interrompono il comando.
- `finish_reason=length` con un output vuoto indica un budget esaurito dal
  ragionamento, non un troncamento: il messaggio lo distingue chiaramente.
- `--eco` è privo di effetto.
- Variabili: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (predefinito `https://openrouter.ai/api/v1`, `https://`
  richiesto), `OPENROUTER_TIMEOUT` (predefinito 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (predefinito 30).

### Nota di traduzione

`--add_translation_note` aggiunge una nota, in `bottom` (predefinito), `top` (dopo il
front matter) o `both` (`--note_position`), nel formato `legacy` (paragrafo in
grassetto, predefinito) o `marker` (`--note_format`). Il formato `marker` è una
definizione di riferimento Markdown invisibile,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguita da una citazione in grassetto: leggibile su GitHub, utilizzabile in fase di build da un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Misure dettagliate

Tutte le misurazioni sono traduzioni effettivamente eseguite con `aipmt`, verso
quattordici lingue: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scritte** conta i file lasciati passare dai controlli di sicurezza; **Senza
discrepanze** quelli in cui `scripts/compare_structure.py` non rileva nulla — stesso numero di
sezioni, sottotitoli, link, URL distinti, blocchi di codice,
codice inline, righe di tabella, blocchi di citazione e parole in grassetto.

"Senza discrepanze" significa "nessun elemento rilevato", non "identico": il comparatore
conta gli elementi senza leggerne il contenuto. Non segnala né un titolo di
livello 4 rimosso, né il testo di un codice inline sostituito, né un flag
scambiato, né un link interno restituito con una parentesi di troppo,
`[texte]((#ancre))`, che non porta più da nessuna parte — e non valuta la
qualità della lingua.

### Articolo di rassegna denso, modalità `--news`

Un'edizione della [rassegna IA di jls42.org](https://jls42.org/fr/news):
589 righe, 140 link, 21 sezioni, 3 citazioni in inglese protette. Campagna
del 4 e 5 settembre 2026.

| Modello                                         | Accesso            | Scritte | Senza scostamenti | Mediana/lingua |
| ----------------------------------------------- | ------------------ | ------- | ----------------- | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14**      | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | abbonamento Google | 14/14   | ✅ **14/14**      | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abbonamento Google | 14/14   | ✅ **14/14**      | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abbonamento ChatGPT| 14/14   | ✅ **14/14**      | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**      | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**      | 26 min 23 s    |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14          | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14          | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14           | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | locale             | 10/14   | ❌ 7/14           | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14           | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14           | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abbonamento Grok   | 1/14    | ❌ 1/14           | 23 min 11 s    |

Grok è stato rimisurato il 9 settembre su un'altra edizione della stessa rassegna
(356 righe): 9 lingue scritte su 14, 8 senza scostamenti. È questa cifra che
compare nella tabella riassuntiva. Tre campagne interrotte non sono
riportate: `qwen3.5-27b` (9 lingue) e `kimi-k2.6` (4) per mancanza di credito,
`z-ai/glm-5.3-flash` i cui due fallimenti derivavano da un'impostazione di ragionamento
che il provider sta correggendo da allora. Le righe OpenRouter sono state misurate con
le impostazioni predefinite del router, prima di `--use_openrouter`; `z-ai/glm-5.2`,
rimisurato con il provider integrato, restituisce lo stesso 14/14. Le cifre sono state
ricalcolate il 10 settembre con il comparatore attuale: `qwen3.8-flash` e
`qwen3.7-flash` guadagnano ciascuno una lingua rispetto alla prima
pubblicazione, gli altri rimangono invariati.

Le righe `--use_antigravity` sono state misurate il 26 settembre sullo stesso
articolo, quattro traduzioni in parallelo: `gemini-3.7-flash-medium` al mattino,
`gemini-3.8-flash-medium` nel pomeriggio. In inglese, ciascuno ha rimosso autonomamente
le tre righe di traduzione francese sotto le citazioni, senza inventare
flag, e le citazioni in inglese sono intatte: la pulizia di fallback non ha
dovuto fare nulla. In `--eco` (`gemini-3.7-flash-low`), su quattro sole lingue
(en, ja, ar, hi): 4 scritte su 4, tutte senza scostamenti, mediana di 1 min 52 s.
Controprova lo stesso giorno su un'edizione più recente della rassegna,
quella del 25 settembre (438 righe, 2 citazioni in inglese), tradotta all'esterno del
blog da `gemini-3.7-flash-medium`: 14 scritte su 14, tutte senza scostamenti, da 87 a
128 s per lingua.

### README di questo progetto, Markdown standard

Revisione congelata il 9 settembre 2026: 785 righe, 285 codici inline, 40
chiusure di blocchi, 89 righe di tabella. Quattro traduzioni in parallelo.

| Modello                                         | Scritte | Senza scostamenti | Mediana/lingua | Cosa differisce                                                          |
| ----------------------------------------------- | ------- | ----------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14          | 1 min 43 s     | niente                                                                   |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14          | 36 s           | una parola in grassetto (ja)                                             |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14          | 1 min 22 s     | una parola in grassetto (ko)                                             |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14          | 2 min 56 s     | un link (sv), una parola in grassetto (zh)                               |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14          | 6 min 46 s     | una parola in grassetto (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14          | 2 min 34 s     | una parola in grassetto (hi, ja, ko)                                     |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14          | 2 min 17 s     | 40 codici inline aggiunti in arabo; grassetto (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14           | 2 min 44 s     | una sezione persa (ar, hi, ko); blocchi di codice aggiunti (ja, ko, ro, zh) |

Due campagne interrotte non sono riportate: Grok, sessione CLI scaduta
dopo dodici lingue (undici senza scostamenti), e `qwen3.8-flash`, HTTP 429 dal suo
provider di hosting dopo due. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
non sono stati rimisurati su questa revisione; su quella del 4 e 5 settembre,
più corta di 277 righe, scrivevano ciascuno 9 traduzioni su 14, di cui 7
e 1 senza scostamenti.

Le righe `--use_antigravity` non sono state misurate sulla revisione congelata,
ma il 26 settembre su quella pubblicata con la versione 1.14.0: 600 righe, 257 codici
inline, 30 chiusure di blocchi, 85 righe di tabella. Più corta di 185
righe, non si confronta termine a termine con le altre righe; le due
righe Antigravity, invece, si confrontano tra loro. Sui link interni,
che il comparatore non controlla, `gemini-3.8-flash-medium` li ha mantenuti
intatti in tutte le quattordici lingue, mentre `gemini-3.7-flash-medium` li ha rotti in
italiano.

### Quattro README di progetti noti

FastAPI, Ollama, tldr-pages e Vue.js, presi così come sono da GitHub — dei
documenti più semplici rispetto ai due precedenti. La campagna mirava ai modelli
in difficoltà; Gemini funge qui da punto di confronto.

| Modello                   | Ambito                     | Scritte | Senza scostamenti |
| ------------------------- | -------------------------- | ------- | ----------------- |
| `gemini-3.7-flash`        | 4 progetti × 14 lingue     | 56/56   | ✅ **55/56**      |
| `opencode/mimo-v2.5-free` | 4 progetti × 14 lingue     | 55/56   | ❌ 47/56          |
| `grok-4.6` (abbonamento)  | 4 progetti × ar, hi, ja, zh| 16/16   | ❌ 14/16          |
| `ollama/gpt-oss-20b-32k`  | 4 progetti × ar, hi, ja, zh| 15/16   | ❌ 9/16           |

### Cosa non sono queste misurazioni

- **Non sono una classifica esaustiva**: solo OpenRouter offre più di quattrocento
  modelli, ne sono stati misurati una quindicina.
- **Sono durate indicative**: da tre a sei traduzioni in parallelo a seconda
  delle campagne, e la velocità di trasmissione di un provider varia nel corso della giornata.
- **Sono osservazioni datate**: i modelli cambiano sotto lo stesso nome, e i vostri
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

Le due righe sono necessarie: senza `pip install -e .`, `python -m aipmt`
risponde `No module named aipmt`.

Strumenti di qualità, opzionali ma consigliati:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Le 28 traduzioni del repository (README e CHANGELOG, quattordici lingue) si
rigenerano con `./regen_translations.sh --force` — Codex e `gpt-5.6-sol` con
l'abbonamento ChatGPT per impostazione predefinita, quattro in parallelo. `REGEN_PROVIDER` e
`REGEN_MODEL` cambiano il percorso: `antigravity` rimane su un abbonamento, quello
di Google, e passa senza deroghe; un'API a pagamento (`openai`, `gemini`,
`grok`, `openrouter`) viene rifiutata senza `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` fissa un limite massimo per ciascun job (600 s, 1.800 s su Codex e
Antigravity). I dettagli degli strumenti sono in `CLAUDE.md`.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** — blog personale pubblicato in 15 lingue. La sua
  [rassegna IA quotidiana](https://jls42.org/fr/news) viene tradotta ogni giorno
  da questo strumento, e funge da documento di riferimento per le misurazioni di cui sopra.

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avvertenza

Questo programma è distribuito **senza alcuna garanzia**, nei termini delle
sezioni 15 e 16 della GPL v3: fornito «così com'è», senza garanzia di commerciabilità
né di adeguatezza a uno scopo particolare, e il suo autore non può essere
ritenuto responsabile per danni derivanti dal suo utilizzo. Il testo della
licenza prevale su questo riepilogo.

- **Rileggere prima di pubblicare.** Le protezioni coprono i blocchi di codice, il
  codice inline, gli URL, gli ancoraggi e le citazioni della modalità `--news` — non i
  titoli, né le tabelle, né il front matter, né il senso delle vostre frasi.
- **I vostri documenti vengono inviati al provider scelto**, secondo le sue condizioni
  d'uso e la sua informativa sul trattamento dei dati. Alcuni modelli gratuiti possono
  riutilizzare le vostre interazioni per l'addestramento, e le condizioni di Antigravity
  consentono a Google di riutilizzarle e di farle rileggere da esseri umani,
  compreso l'abbonamento a pagamento; un modello locale è l'unica via per non far
  uscire alcun dato dalla vostra macchina.
- **Le chiamate alle API sono a vostro carico.** Questo programma non impone un limite alla
  spesa: un documento lungo, una ripresa dopo un errore o un modello che ragiona
  molto comportano costi maggiori.
- **Le misurazioni pubblicate sono osservazioni datate**, non garanzie.

I nomi di prodotti e aziende citati appartengono ai rispettivi titolari.
Questo progetto non è affiliato a nessuno di essi.

**Articolo tradotto dal fr all'it con gemini-3.8-flash-medium.**
