# Traduttore di Markdown AI-Powered

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

Traduce file Markdown da una lingua all'altra preservando la struttura:
blocchi di codice, codice inline, URL, ancore, tabelle e front matter.
Undici modalità di chiamata a un modello — cinque API, quattro abbonamenti
senza fatturazione a consumo, due router — e una misurazione pubblicata di
ciò che ciascun modello preserva realmente.

## In breve

- **Undici percorsi di provider**: API OpenAI, Mistral, Claude, Gemini e Grok;
  abbonamenti ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) senza fatturazione a consumo; router OpenCode (open source, gratuito o locale) e OpenRouter
  (più di 400 modelli).
- **Nessun errore dovuto a un token perso**: blocchi di codice, codice inline,
  URL, ancore e citazioni vengono sostituiti da token prima della chiamata e
  verificati al ritorno. Se ne manca uno, il file non viene scritto.
- **Documenti lunghi**: segmentazione in base alla finestra di contesto del modello.
- **Modalità `--news`**: citazioni in inglese protette e bandiere gestite per
  lingua, per gli articoli di rassegna.
- **Modalità `--eco`**: modelli veloci ed economici.
- **Nota di traduzione** opzionale, in alto, in basso o in entrambe le posizioni.

## Installazione

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 o successivo. Per l'installazione dal repository, vedere
[Contribuire](#contribuire).

## Configurazione

Le chiavi vengono lette in tre posizioni, dalla priorità più alta alla più bassa;
ciascuna colma solo ciò che la precedente lascia vuoto.

|     | Dove                                                  | Per cosa                               |
| --- | ----------------------------------------------------- | -------------------------------------- |
| 1   | Variabili d'ambiente                                  | CI, container, deroga temporanea       |
| 2   | `.env` della directory corrente (o genitrice)  | una chiave specifica per un progetto   |
| 3   | `~/.config/aipmt/.env`                                         | installato una volta, valido ovunque   |

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
sotto Windows. In assenza di chiavi, il comando elenca le tre posizioni.

**Il file `.env` di un progetto non può né reindirizzare le chiamate né scegliere il programma
eseguito.** Fornisce chiavi, mai una destinazione né un binario: qualsiasi
variabile in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, i proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), gli archivi di certificati (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` vi vengono ignorati, con un avviso. Un repository clonato non deve
poter sottrarre la tua chiave, né farti avviare il proprio programma alla
prima traduzione. Questo file viene letto anche senza interpolazione:
`NOM=${OPENAI_API_KEY}` non vi ricopia la chiave. Imposta queste variabili
nell'ambiente o in `~/.config/aipmt/.env`.

Variabili opzionali: `XAI_BASE_URL` (predefinito `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secondi per chiamata, predefinito 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predefinito 600), `GROK_BIN`, `GROK_HOME` (predefinito `~/.grok`), `GROK_TIMEOUT`
(predefinito 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (predefinito 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (predefinito 600), `OPENROUTER_BASE_URL`
(`https://` richiesto), `OPENROUTER_TIMEOUT` (predefinito 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (predefinito 30). Ciascuna è descritta dettagliatamente nella
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
con `--include_model`, `document-es-gpt-6.1-terra.md`. L'estensione diventa
sempre `.md` — `article.mdx` genera `article-en.md` — tranne con
`--keep_filename`, che mantiene il nome originale. Una traduzione già presente
viene saltata a meno di usare `--force`.

Codici di uscita: `0` se tutto è andato a buon fine o è stato saltato, `1` se rimane un file
non riuscito (elenco sullo standard error), `2` se la causa è la configurazione.
Un file non riuscito non viene mai scritto, anche se la scrittura stessa fallisce:
il contenuto viene scritto a parte e poi rinominato. È sufficiente riavviare.

## Quale modello scegliere

Misurato su due documenti reali, tradotti nelle stesse quattordici lingue da
ciascun modello. **Il numero indica le lingue, su quattordici, in cui la
traduzione viene scritta e nulla differisce dalla fonte.**

| Modello               | Come accedervi                    | Articolo di rassegna denso | Questo README | Cosa differisce, e su quante lingue                                                                                                                                |
| --------------------- | --------------------------------- | -------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | abbonamento Google (Antigravity)  | ✅ 14/14                   | ✅ 14/14      | nulla, su nessuno dei due documenti                                                                                                                                |
| **Claude Sonnet 5.5** | chiave API Anthropic              | ✅ 14/14                   | ✅ 14/14      | nulla, su nessuno dei due documenti                                                                                                                                |
| **Gemini 3.7 Flash**  | chiave API Google                 | ✅ 14/14                   | ⚠️ 13/14      | 1 lingua su 14: una parola in grassetto in più (ja)                                                                                                                |
| **Gemini 3.7 Flash**  | abbonamento Google (Antigravity)  | ✅ 14/14                   | ⚠️ 13/14      | 1 lingua su 14: una parola in grassetto in meno (ko)                                                                                                                |
| **GPT-5.6 Sol**       | abbonamento ChatGPT, o chiave OpenAI | ✅ 14/14                | ⚠️ 12/14      | 2 lingue su 14: una parola in grassetto in meno (ar, ja)                                                                                                           |
| **GLM-5.2**           | chiave OpenRouter                 | ✅ 14/14                   | ⚠️ 11/14      | 3 lingue su 14: una parola in grassetto in meno (hi, ja, ko)                                                                                                       |
| Claude Sonnet 5       | abbonamento Claude (Claude Code)  | ⚠️ 13/14                   | ⚠️ 13/14      | 1 lingua su 14 sull'articolo: una parola in grassetto in più (zh); 1 su questo README: una riga di tabella attaccata alla precedente, nascosta alla visualizzazione (ar) |
| Claude Haiku 4.5      | abbonamento Claude (Claude Code)  | ⚠️ 11/14                   | ✅ 14/14      | 3 lingue sull'articolo: un titolo di sezione passato al livello 1 (en, pl, ro); su questo README, nulla per lo strumento di confronto, ma i link interni duplicati in inglese |
| Claude Sonnet 5       | chiave API Anthropic              | ⚠️ 11/14                   | ⚠️ 12/14      | 3 lingue sull'articolo: un blocco di codice comparso (es, de, hi); 2 su questo README: un link senza formattazione (sv), una parola in grassetto (zh)            |
| Claude Haiku 4.5      | chiave API Anthropic              | ⚠️ 7/14                    | ✅ 14/14      | 7 lingue sull'articolo: un titolo di sezione passato al livello 1 — in giapponese, rimasto in francese; nulla su questo README                                    |
| Claude Haiku 5.5      | chiave API Anthropic              | ⚠️ 11/14                   | ❌ 12/14      | 3 lingue sull'articolo: un titolo di sezione cambiato di livello o duplicato (ja, ko, zh); su questo README, 2 lingue rifiutate, codici inline persi (ar, hi)     |
| Qwen 3.7 Flash        | chiave OpenRouter                 | ❌ 8/14                    | ⚠️ 10/14      | 1 lingua rifiutata sull'articolo, 5 altre deviano; su questo README, una quarantina di parole racchiuse in `code` (ar)                                    |
| Grok 4.6              | abbonamento Grok                  | ❌ 8/14                    | non valutato  | 5 lingue rifiutate su 14, per assenza di codici inline e URL restituiti; l'olandese diverge su tutto                                                               |
| GPT-OSS 20B           | modello locale (Ollama)            | ❌ 7/14                    | non rimisurato | 4 lingue rifiutate su 14: il modello vi lasciava passaggi in francese, le protezioni li hanno bloccati                                                            |
| MiMo v2.5 (gratuito)  | OpenCode Zen, senza account       | ❌ 11/14                   | non rimisurato | 1 lingua rifiutata; una sezione persa in polacco                                                                                                                   |
| Mistral Large         | chiave API Mistral                | ❌ 5/14                    | ❌ 1/14       | **un'intera sezione scompare**: 1 lingua sull'articolo (hi), 3 su questo README (ar, hi, ko) — e 3 lingue rifiutate sull'articolo                                  |
| DeepSeek V4 Flash     | chiave OpenRouter                 | ❌ 3/14                    | non rimisurato | 10 lingue rifiutate su 14; 37 minuti per lingua                                                                                                                    |
| Claude Opus 5.5       | abbonamento Claude (Claude Code)  | ❌ 0/14                    | ✅ 14/14      | l'articolo rifiutato in tutte le 14 lingue dai guardrail di Opus, a causa di una breve notizia di biologia; nulla su questo README                                 |

|     | Significato del simbolo                                                                                                                                                                               |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | tutte e quattordici le lingue tradotte, e nulla differisce dalla fonte                                                                                                                                |
| ⚠️  | tutte e quattordici le lingue tradotte; ciò che differisce riguarda la **formattazione** — una parola in grassetto, un `code`, un link che perde le parentesi quadre. Nessun testo, nessun URL, nessun blocco di codice, nessuna sezione mancante |
| ❌  | almeno una lingua non è stata potuta tradurre — il file viene rifiutato, non scritto — **oppure** mancano contenuti in un file scritto                                                                |

Cosa tenere a mente:

- **Una traduzione rifiutata non è una traduzione danneggiata.** Quando manca
  un token al ritorno, il file non viene scritto e la lingua viene conteggiata
  come rifiutata. È quanto accade a Grok sull'articolo: quattro codici inline e
  tre URL persi fin dal primo segmento, sulle cinque scritture non latine.
- **Un modello può rifiutare un intero documento per una sola frase.** Opus 5.5
  traduce questo README senza alcuna discrepanza, ma nessun articolo di rassegna:
  i suoi guardrail bloccano la risposta su una breve notizia di biologia. Il file non viene
  scritto e aipmt ne spiega il motivo.
- **Questa rete di sicurezza non copre titoli, tabelle, front matter né testo.**
  Un modello che elimina una sezione restituisce un file che lo strumento scrive
  senza esitazione — è il caso di Mistral. Questi elementi non sono
  sostituibili da un token e le verifiche attuali non li controllano;
  `scripts/compare_structure.py` rileva una sezione persa, ma solo a posteriori.
- **Grok non ha una valutazione su questo README**: la sua sessione CLI è scaduta
  dopo dodici lingue, di cui undici senza discrepanze. Una campagna di test interrotta non si valuta.
- **La densità del documento conta più della lingua.** Grok regge su README
  ordinari e cede su un articolo denso di link, anche in
  olandese.

Date e documenti: la colonna «Questo README» è stata misurata il 9 settembre 2026
su una revisione bloccata di questo file (785 righe, 285 codici inline, 89 righe
di tabella), poi modificata — tranne le righe Antigravity e Claude Code,
misurate il 26 settembre sulla revisione pubblicata con la 1.14.0, più breve
(600 righe, 257 codici inline, 85 righe di tabella), e le righe Claude
Sonnet 5.5, Haiku 5.5 e Haiku 4.5 tramite API, misurate il 18 ottobre sulla
medesima revisione. La colonna «Articolo di rassegna denso» proviene dalla sessione di test
del 4 e 5 settembre su un articolo di 589 righe, tranne la riga Grok, rimisurata il
9 settembre su un'altra edizione della stessa rassegna, le righe Antigravity e
Claude Code, misurate il 26 settembre sullo stesso articolo, e queste tre righe
Claude, il 18 ottobre. Le tabelle complete, le durate e il protocollo si trovano
in [Misurazioni dettagliate](#misurazioni-dettagliate).

## Tutte le opzioni

| Opzione                  | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | File Markdown singolo da tradurre (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Directory sorgente contenente i file Markdown (predefinito: `content/posts`)                                   |
| `--target_dir`           | Directory di output per i file tradotti (predefinito: `traductions_en`)                                    |
| `--source_lang`          | Lingua di partenza (predefinito: `fr`)                                                                                  |
| `--target_lang`          | Lingua di destinazione (predefinito: `en`)                                                                                   |
| `--model`                | Modello specifico da utilizzare                                                                                  |
| `--eco`                  | Usa i modelli economici                                                                              |
| `--use_mistral`          | Usa l'API Mistral AI                                                                                     |
| `--use_claude`           | Usa l'API Claude                                                                                         |
| `--use_gemini`           | Usa l'API Gemini                                                                                         |
| `--use_grok`             | Usa l'API xAI (Grok) — richiede `XAI_API_KEY`                                                           |
| `--use_codex`            | Usa la CLI Codex sulla quota dell'abbonamento ChatGPT                                                    |
| `--use_grok_cli`         | Usa la CLI Grok sulla quota dell'abbonamento Grok                                                        |
| `--use_antigravity`      | Usa la CLI Antigravity (`agy`) sulla quota dell'abbonamento Google AI Pro o Ultra                       |
| `--use_claude_code`      | Usa la CLI Claude Code (`claude -p`) sulla quota dell'abbonamento Claude Pro o Max                      |
| `--use_opencode`         | Usa OpenCode (open source) verso il provider configurato in OpenCode; richiede `--model provider/modèle` |
| `--use_openrouter`       | Usa OpenRouter — richiede `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--force`                | Forza la ritraduzione                                                                                       |
| `--keep_filename`        | Mantieni il nome file originale                                                                          |
| `--news`                 | Modalità notizie: protegge le citazioni in EN, gestisce le bandiere per lingua                                      |
| `--add_translation_note` | Aggiungi una nota di traduzione                                                                                |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinito), o `both`                                                     |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) o `marker`                                            |
| `--include_model`        | Includi il nome del modello nel file di output                                                            |
| `--reasoning_effort`     | Sforzo di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

I nove flag `--use_*` sono mutuamente esclusivi: combinarne due viene
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

| Provider    | Qualità (predefinito)                                                | Economico (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (anche `gpt-5.6-sol`, `terra` e `luna` tramite `--model`) | `gpt-6-luna`              |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | idem — `--eco` senza effetto |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, sforzo `low`                                               | idem — `--eco` senza effetto |
| OpenCode    | `--model provider/modèle` obbligatorio                                | idem — `--eco` senza effetto |
| OpenRouter  | `--model fournisseur/modèle` obbligatorio                             | idem — `--eco` senza effetto |

I valori predefiniti seguono l'ultima generazione di ciascun provider, misurata
prima di essere adottata: GPT-6 per OpenAI, Gemini 4 Hydrogen per Google,
Grok 4.7 per xAI a partire dalla versione 1.19.0. I modelli precedenti rimangono accettati
tramite `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), così come
Gemini 4 Argon e Carbon, la fascia alta di Google. aipmt regola autonomamente
lo sforzo di ragionamento di GPT e Grok, disattivato in `--eco`, e
`--reasoning_effort` lo forza; un Gemini riceve sempre il livello più
basso che accetta.
Un guasto temporaneo dell'API Gemini (503, 429, timeout) ritenta
la chiamata fino a tre volte, dopo 10, 20 e poi 40 secondi. Un tentativo
rimasto senza risposta viene abbandonato dopo 5 minuti, quindi ritentato allo
stesso modo: un server che non risponde fa fallire il segmento in una ventina di minuti
al massimo, invece di bloccarsi a tempo indeterminato.

### Con l'abbonamento ChatGPT: `--use_codex`

Controlla la CLI ufficiale di Codex: la traduzione viene scalata dalla quota
dell'abbonamento ChatGPT, senza chiave API né fatturazione a consumo.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Il binario viene cercato in `CODEX_BIN`, poi nel `PATH`, quindi nel pacchetto
  `openai-codex-cli-bin`. `~/.codex/auth.json` non viene mai letto.
- `OPENAI_API_KEY` e `CODEX_API_KEY` vengono rimosse dall'ambiente del
  sottoprocesso: una chiave presente non fa mai passare all'API.
- Ogni segmento costa almeno un "messaggio" della finestra di 5 ore — due
  se la sua convalida fallisce e viene ritentato. OpenAI dichiara, a titolo
  di stima, 250-2.000 messaggi/5 h per `gpt-5.6-luna`, la modalità economica fino alla
  1.18.0, e 10-100 per `gpt-5.6-sol` su un piano Plus.
- Anche `--model gpt-5.6-sol`, l'impostazione predefinita fino alla 1.16.3, `--model gpt-5.6-terra`
  e `--model gpt-5.6-luna` passano attraverso l'abbonamento.
- Un 429 dal server non fa perdere il file: Codex si riconnette da solo,
  aipmt attende la fine del turno e, se l'errore 429 persiste, il segmento
  riparte dopo 30 e poi 60 secondi. Un modello a cui l'account non ha diritto restituisce un 400 "model is
  not supported when using Codex with a ChatGPT account".
- Più lento di un'API, e il divario cresce con le dimensioni del documento: su questo README,
  6 min e 46 s per lingua come valore mediano con `gpt-5.6-sol`, contro 36 s per
  `gemini-3.7-flash`.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definita): l'abbonamento si autentica
  tramite un file di sessione personale, che non deve trovarsi su un runner
  condiviso.
- Variabili: `CODEX_BIN`, `CODEX_TIMEOUT` (secondi per segmento, predefinito 600).

### Con l'abbonamento Grok: `--use_grok_cli`

Stesso principio con la CLI ufficiale Grok Build, sull'abbonamento SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Isolamento più debole rispetto a Codex.** La sandbox del sistema operativo di Grok non funziona
  su molte macchine Linux recenti (AppArmor, socket di runtime
  dei container), e un profilo che non può essere applicato si avvia senza isolamento in
  modo silenzioso. Lo script non richiede quindi alcun profilo per impostazione predefinita, lo segnala e
  si affida alle regole `--deny` della CLI, tra cui il catch-all `*` — l'unico
  livello che rifiuta di avviarsi anziché rimuovere la protezione senza
  avvisare. `GROK_TRANSLATE_SANDBOX=read-only` richiede la sandbox del sistema operativo, e l'avvio
  fallisce se la macchina non può soddisfarla.
- La quota è settimanale, condivisa con Chat, Imagine e Voice, e nessun
  comando consente di consultarla: un batch può intaccare l'utilizzo conversazionale
  senza alcun preavviso.
- Variabili: `GROK_BIN`, `GROK_HOME` (directory della CLI, predefinito `~/.grok`),
  `GROK_TIMEOUT` (predefinito 900), `GROK_TRANSLATE_SANDBOX`.

### Con l'abbonamento Google: `--use_antigravity`

Stesso principio con `agy`, la CLI ufficiale di Antigravity: per chi paga Google
AI Pro o Ultra, la traduzione viene scalata dalla quota dell'abbonamento invece
di essere fatturata a token. È l'unica via d'accesso a questa quota: Gemini CLI non
serve più questi account dal 18 giugno 2026
([annuncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e l'SDK di Antigravity accetta solo una chiave API o un progetto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nessuna modalità a pagamento rimane aperta.** agy riceve dal vostro
  ambiente solo un elenco chiuso di variabili — `PATH`, lingua e fuso orario,
  terminale, identità, proxy e certificati, bus di sessione — e nessuna chiave:
  diverse delle sue variabili reindirizzano una chiamata senza mostrare nulla (misurato:
  una invia il documento a un gateway di terze parti, un'altra a un progetto
  Google Cloud fatturato), e un elenco di esclusione ne tralasciava qualcuna a ogni revisione.
  Prima di qualsiasi segmento, `agy -p /config`, che non consuma alcuna quota, deve mostrare
  i crediti AI a pagamento disattivati, senza chiave API né progetto Google Cloud — un'impostazione
  assente equivale a un rifiuto —, altrimenti nulla viene tradotto; il registro di ogni
  chiamata deve poi attestare l'abbonamento (`authMethod=consumer`), altrimenti la
  risposta viene rifiutata.
- **Isolamento.** Ogni chiamata viene eseguita in una home directory privata e
  usa e getta, con un agente di traduzione privo di strumenti: le vostre impostazioni, regole,
  plugin, server MCP e hook di agy non vi accedono, nulla viene aggiunto alla vostra
  cronologia e l'autenticazione rimane nel portachiavi, che aipmt non legge mai.
  Un agente non trovato fa ricadere agy, silenziosamente, sul suo agente di programmazione
  e sui suoi strumenti: un'intera riga del log deve confermare l'agente corretto — un
  documento che cita questo messaggio non la sostituisce —, altrimenti viene rifiutato.
- **Piattaforme**: Linux, all'interno di una sessione dotata di un portachiavi (bus di sessione
  D-Bus, Secret Service); macOS è supportato, ma non vi è stato misurato. Rifiutato
  su Windows, dove agy non legge le variabili che isolano ciascuna chiamata, e
  su Linux senza bus di sessione — sessione SSH, container, server: agy vi
  memorizza il token in un file in `~/.gemini`, che l'isolamento nasconde. Il
  rifiuto avviene prima di qualsiasi avvio, con la relativa motivazione, invece di attendere
  un minuto un codice di accesso.
- **Modelli**: quelli di `agy models`. I modelli Gemini includono lo sforzo nel nome
  (`gemini-3.8-flash-medium`…): un nome senza suffisso viene rifiutato prima della chiamata,
  e `--reasoning_effort` non ha effetto. Per impostazione predefinita `gemini-3.8-flash-medium`,
  e `gemini-3.8-flash-low` in `--eco`, da quando agy non serve più Gemini 3.7
  Flash; la campagna che ha stabilito il valore predefinito è
  descritta in [Misurazioni dettagliate](#misurazioni-dettagliate). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) condivide la quota di 3.8 Flash e ne consuma
  di più: 0,95 punti della finestra di 5 ore per questo README a sforzo
  medio, contro 0,32. Claude e GPT-OSS
  hanno una propria quota, molto più ridotta: circa l'1% della finestra di
  5 ore per chiamata misurata, contro lo 0,05% con Flash. Gemini 4 Argon ha una
  quota propria, settimanale: questo README ne consuma l'1,35%.
- **Quota**: per gruppo, una finestra di 5 ore e una settimanale, proporzionale
  al costo in token. Misurato sull'account dell'autore: circa
  16 punti della finestra di 5 ore per milione di caratteri sorgente in
  `gemini-3.8-flash-medium`, 14 in `gemini-3.7-flash-medium` e da 7 a 8 con
  sforzo basso — un README di 40.000 caratteri costa quindi poco più di mezzo
  punto. Il limite settimanale dipende invece dal livello di abbonamento. Il nuovo tentativo segue
  quanto dichiarato come ritentabile da agy; in caso contrario, una finestra esaurita non viene mai
  ritentata: causa il fallimento di ogni file fino al ripristino
  mostrato da `/usage`.
- **Più lento dell'API**: sull'articolo denso delle misurazioni, 3 min e 59 s per
  lingua come valore mediano in `gemini-3.8-flash-medium` e 3 min e 14 s in
  `gemini-3.7-flash-medium`, contro 1 min e 18 s per Gemini 3.7 Flash tramite API.
- **Interruzione**: Ctrl-C, o un terminale chiuso, arrestano agy insieme al
  comando invece di lasciargli completare il turno a carico della quota; lo stesso
  vale per Codex, Grok CLI e OpenCode. Sotto `nohup`, la traduzione continua.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definita): la sessione di accesso risiede in un
  portachiavi personale. Su un runner, usare `--use_gemini` con `GOOGLE_API_KEY`.
- Variabili: `AGY_BIN` (altrimenti `PATH`, poi `~/.local/bin/agy`),
  `AGY_TIMEOUT` (secondi per segmento, avvio compreso, predefinito 900).

**Condizioni d'uso: la responsabilità ricade sul vostro account.** Le
[condizioni di Antigravity](https://antigravity.google/terms) (sezione 6) e le relative
[FAQ](https://antigravity.google/docs/faq/) vietano l'accesso al servizio
tramite software di terze parti utilizzando l'autenticazione di Antigravity — Claude Code,
OpenClaw e OpenCode vi sono citati —, a pena di sospensione dell'account. aipmt
non legge né riutilizza il token: avvia il binario ufficiale nella
[modalità headless](https://antigravity.google/docs/cli/headless/) documentata da Google
per script e CI. Un membro di Google ha definito "standard"
l'esecuzione di `agy -p` da uno script locale per il proprio lavoro
([forum ufficiale, 25 settembre 2026, risposta non vincolante](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nessun testo definisce chiaramente il caso di uno strumento distribuito come questo.

**Solo documenti pubblici.** In base alla sezione 5 delle stesse condizioni, le
comunicazioni — prompt, risposte, metadati — possono essere utilizzate per migliorare i
prodotti e l'apprendimento automatico di Google ed essere esaminate da revisori
umani, abbonamenti a pagamento inclusi. L'opt-out avviene tramite l'impostazione
`enableTelemetry`, dal funzionamento non documentato, che aipmt non imposta; le vostre impostazioni
di agy non vengono ereditate nel suo isolamento. Non fatevi transitare nulla di confidenziale.

### Sull'abbonamento Claude: `--use_claude_code`

Stesso principio con `claude`, la CLI ufficiale di Claude Code, in modalità `-p`: per
chi paga Claude Pro o Max, la traduzione viene scalata dalla quota
dell'abbonamento invece di essere fatturata a token. Da non confondere con
`--use_claude`, l'API di Anthropic, fatturata a consumo.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nessun canale a pagamento rimane aperto, e ogni chiamata lo dimostra.** Claude
  Code riceve dal vostro ambiente solo un elenco chiuso di variabili — né
  chiave API, né token, né cloud provider, né marcatore della sessione Claude Code
  da cui verrebbe avviato aipmt. Prima del primo segmento, `claude auth status` deve
  mostrare la connessione dell'abbonamento, senza chiave Console, e `/usage`, che non consuma
  alcuna quota, deve attestarlo; ogni chiamata lo attesta a sua volta nel suo
  evento di inizializzazione, altrimenti la risposta viene rifiutata.
- **Disattivate l'«extra usage»** (claude.ai, Impostazioni → Utilizzo) per
  mantenere il costo a zero euro: se abilitato, subentra a una finestra esaurita e
  fattura senza mostrare alcun errore. aipmt interrompe la traduzione non appena il report
  della quota di una chiamata lo segnala, ma quella specifica chiamata è già conteggiata.
- **Quota condivisa con le vostre sessioni Claude Code.** Ogni chiamata riporta
  l'utilizzo delle finestre di 5 ore e settimanale; oltre l'80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), non viene avviato alcun segmento aggiuntivo, per non
  esaurire le risorse necessarie al vostro lavoro.
- **Isolamento.** Ogni chiamata viene eseguita senza strumenti, in una directory privata e
  monouso, in modalità priva di personalizzazioni: né i vostri `CLAUDE.md`, né i vostri plugin,
  hook, server MCP o impostazioni vengono caricati, e nulla viene conservato della
  sessione. Gli allegati vengono disattivati: un `@chemin` nel vostro documento
  rimane testo semplice e non apre alcun file (misurato).
- **Modelli**: `sonnet` per impostazione predefinita, con livello di effort `low`, e anche in `--eco`:
  `--eco` non cambia nulla su questo percorso. Misurati sugli stessi documenti, `haiku`
  è due volte più lento — ragiona senza che sia possibile impedirlo — a
  fronte di un costo appena inferiore, e `opus` rifiuta contenuti di biologia (punto
  successivo). Entrambi rimangono accessibili tramite `--model`; questi alias seguono
  l'ultimo modello della loro famiglia. `fable` e le varianti `[1m]` vengono rifiutati,
  poiché passano su crediti a pagamento. `--reasoning_effort` regola l'effort,
  da cui una traduzione non trae alcun vantaggio: il ragionamento misurato è nullo o quasi.
- **Opus rifiuta alcuni contenuti di biologia.** I suoi guardrail sono più
  severi di quelli di Sonnet, e il messaggio di errore di Anthropic avverte che
  «can sometimes flag biology-research-adjacent work». Misurato: una breve nota di
  monitoraggio su 279 molecole generate ha causato il rifiuto dell'articolo in tutte e quattordici
  le lingue. Non viene scritto nulla: aipmt rifiuta la risposta interrotta, segnala i
  guardrail e consiglia `--model sonnet`.
- Rifiutato in CI (`CI` o `GITHUB_ACTIONS` definito) e sotto Windows (non misurato).
- Variabili: `AIPMT_CLAUDE_BIN` (altrimenti il `PATH`, poi `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (secondi per segmento, predefinito 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (predefinito 0.8), `CLAUDE_CONFIG_DIR` (l'account di
  Claude Code, mai preso da un `.env` di progetto); directory di lavoro sotto
  `XDG_CACHE_HOME/aipmt/claude-code` (predefinito `~/.cache`).

**Condizioni d'uso: la responsabilità ricade sul vostro account.** La
[pagina legale di Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
non impedisce a «an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription»: è esattamente ciò che fa aipmt, che avvia il
binario ufficiale e non legge mai il token. Tuttavia Anthropic «does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users», preferisce la chiave API per gli strumenti
di terze parti, «including open-source projects», e si riserva il diritto di addebitare il loro
utilizzo sui crediti a pagamento
([guida di Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nessun testo dirime esplicitamente il caso di uno strumento distribuito che avvia il binario.

**Dati**: sugli account Free, Pro e Max, l'addestramento dei modelli
si applica anche a Claude Code quando l'impostazione sulla privacy lo consente
([pagina dati](https://code.claude.com/docs/en/data-usage)). aipmt non conserva
alcuna trascrizione locale (`--no-session-persistence`). Non fatevi transitare
nulla di riservato.

### Verso il provider a propria scelta: `--use_opencode`

[OpenCode](https://opencode.ai) è un agente di codice open source (MIT) che
instrada verso i provider configurati al suo interno: chiave API, abbonamento,
gateway OpenCode Zen (modelli gratuiti, senza account) o modello locale. Due
percorsi sono stati misurati end-to-end in questa sede: Zen e Ollama.

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
  i cui strumenti sono tutti disabilitati (`permission: { "*": "deny" }`), condivisione di
  sessione disattivata, `--pure`, mai `--auto`;
- directory di lavoro monouso e vuota, con `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` impostati — senza di essi, OpenCode inietta nel
  prompt il file `AGENTS.md` della directory corrente e `~/.claude/CLAUDE.md`. Il
  `~/.config/opencode/AGENTS.md` globale viene comunque iniettato, poiché OpenCode non consente
  di escluderlo;
- contratto di output: codice di uscita 0, nessun evento `error`, nessuna chiamata
  di strumenti, ultimo passaggio in `stop`, testo non vuoto, e l'agente `aipmt`
  effettivamente caricato — un `--agent` sconosciuto non causa il fallimento di OpenCode, ma
  ricade silenziosamente sull'agente di coding;
- nessuna chiave di `aipmt` viene trasmessa, tranne `OPENCODE_API_KEY`, la chiave
  di OpenCode stesso. I provider si configurano in OpenCode, non nel
  `.env` di `aipmt`.

Da sapere:

- I modelli gratuiti di Zen sono mutevoli, con limiti non documentati, e
  i loro scambi possono essere impiegati per l'addestramento: adatti per documentazione
  pubblica, non per contenuti riservati.
- Un modello locale deve offrire almeno 16k token di contesto, dato che i segmenti
  raggiungono fino a 16.000 caratteri. Ollama ne configura spesso 4.096: passare
  attraverso un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` non ha effetto; `--reasoning_effort` viene trasmesso così com'è come
  `--variant` di OpenCode.
- OpenCode registra ogni sessione in `~/.local/share/opencode/`.
- Variabili: `OPENCODE_BIN` (altrimenti il `PATH`, poi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secondi per segmento, predefinito 600). `OPENCODE_CONFIG`
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

`reasoningEffort: "none"` disattiva il reasoning che Ollama abilita per impostazione predefinita su questi
modelli, e che un Modelfile non può disattivare. Misurato su una frase di
sei parole: 919 token di ragionamento e 68 secondi senza l'opzione, 9 token con l'opzione.

### Verso oltre 400 modelli: `--use_openrouter`

OpenRouter è un router fatturato a consumo, su un unico credito, davanti a
modelli ospitati da terze parti — inclusi i modelli cinesi aperti che nessun
altro provider espone in questo contesto.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` è obbligatorio. Un preflight, eseguito prima di qualsiasi fatturazione, gestisce
due particolarità del routing:

- **Uno stesso modello è servito da decine di host con limiti
  differenti** — su `z-ai/glm-5.3-flash`, 23 host di cui uno limitato a
  2.048 token di output. Il preflight legge `/api/v1/models/{modèle}/endpoints`,
  esclude gli host al di sotto di 8.000 token di output o con stato degradato, e
  blocca gli altri con `allow_fallbacks: false`.
- **Il ragionamento viene fatturato alla tariffa di output** — 107 token contro 2 su
  una risposta «OK» di `z-ai/glm-5.2`. È disattivato per impostazione predefinita; i modelli
  che lo impongono ricevono il livello di effort più basso che accettano, poiché l'impostazione
  predefinita del catalogo potrebbe saturare l'output prima del termine della traduzione.
  `--reasoning_effort` mantiene la priorità.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La finestra di contesto proviene dal catalogo. Un modello con meno di 16.400 token viene
  rifiutato prima di qualsiasi chiamata: 8.400 per il prompt e il segmento, almeno 8.000
  di output.
- Uno slug assente dal catalogo, un catalogo non raggiungibile o l'assenza
  di un host che rispetti il limite interrompono il comando.
- `finish_reason=length` con un output vuoto corrisponde a un budget consumato dal
  ragionamento, non a un troncamento: il messaggio lo segnala chiaramente.
- `--eco` non ha effetto.
- Variabili: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (predefinito `https://openrouter.ai/api/v1`, `https://`
  richiesto), `OPENROUTER_TIMEOUT` (predefinito 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (predefinito 30).

### Nota di traduzione

`--add_translation_note` aggiunge una nota, in `bottom` (predefinito), `top` (dopo il
front matter) o `both` (`--note_position`), in formato `legacy` (paragrafo in
grassetto, predefinito) o `marker` (`--note_format`). Il formato `marker` è una
definizione di riferimento Markdown invisibile,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguita da una citazione in grassetto: leggibile su GitHub, utilizzabile in fase di build da un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Misurazioni dettagliate

Tutte le misurazioni sono traduzioni realmente eseguite con `aipmt`, verso
quattordici lingue: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scritte** conta i file che i controlli hanno lasciato passare; **Senza
discrepanze** quelli in cui `scripts/compare_structure.py` non rileva nulla — stesso numero di
sezioni, sottotitoli, link, URL distinti, blocchi di codice,
codici inline, righe di tabelle, citazioni e parole in grassetto.

«Senza discrepanze» significa «nulla di rilevato», non «identico»: lo strumento di confronto
conta gli elementi senza leggerne il contenuto. Non segnala un titolo di
livello 4 rimosso, né il testo di un codice inline sostituito, né una bandiera
scambiata, né un link interno reso con una parentesi di troppo,
`[texte]((#ancre))`, che non porta più a nulla — e non esprime un giudizio sulla
lingua.

### Articolo di rassegna denso, modalità `--news`

Un'edizione della [rassegna IA di jls42.org](https://jls42.org/fr/news):
589 righe, 140 link, 21 sezioni, 3 citazioni inglesi protette. Campagna
del 4 e 5 settembre 2026.

| Modello                                         | Accesso            | Scritte | Senza discrepanze | Mediana/lingua |
| ----------------------------------------------- | ------------------ | ------- | ----------------- | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14**      | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | abbonamento Google | 14/14   | ✅ **14/14**      | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abbonamento Google | 14/14   | ✅ **14/14**      | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14**      | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abbonamento ChatGPT| 14/14   | ✅ **14/14**      | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**      | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**      | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | abbonamento Claude | 14/14   | ⚠️ 13/14          | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14          | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | abbonamento Claude | 14/14   | ⚠️ 11/14          | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14          | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14           | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14          | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14           | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | locale             | 10/14   | ❌ 7/14           | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14           | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14           | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abbonamento Grok   | 1/14    | ❌ 1/14           | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | abbonamento Claude | 0/14    | ❌ 0/14           | —              |

Grok è stato rimisurato il 9 settembre su un'altra edizione della stessa rassegna
(356 righe): 9 lingue scritte su 14, 8 senza discrepanze. È questa la cifra che
compare nella tabella principale. Tre campagne interrotte non sono state
riportate: `qwen3.5-27b` (9 lingue) e `kimi-k2.6` (4) per esaurimento del credito,
`z-ai/glm-5.3-flash` i cui due fallimenti derivavano da un'impostazione di reasoning
che il provider ha corretto successivamente. Le righe OpenRouter sono state misurate con le
impostazioni predefinite del router, prima di `--use_openrouter`; `z-ai/glm-5.2`,
rimisurato con il provider integrato, restituisce lo stesso 14/14. Le cifre sono state
ricalcolate il 10 settembre con l'attuale strumento di confronto: `qwen3.8-flash` e
`qwen3.7-flash` guadagnano ciascuno una lingua rispetto alla prima
pubblicazione, gli altri rimangono invariati.

Le righe `--use_antigravity` sono state misurate il 26 settembre sullo stesso
articolo, quattro traduzioni in parallelo: `gemini-3.7-flash-medium` al mattino,
`gemini-3.8-flash-medium` nel pomeriggio. In inglese, ciascuno ha rimosso autonomamente
le tre righe di traduzione francese sotto le citazioni, senza inventare alcuna
bandiera, e le citazioni inglesi sono rimaste intatte: la pulizia di fallback non ha
dovuto fare nulla. In `--eco` (`gemini-3.7-flash-low`), su sole quattro lingue
(en, ja, ar, hi): 4 scritte su 4, tutte senza discrepanze, 1 min 52 s di
mediana. Controprova lo stesso giorno su un'edizione più recente della rassegna,
quella del 25 settembre (438 righe, 2 citazioni inglesi), tradotta al di fuori del
blog tramite `gemini-3.7-flash-medium`: 14 scritte su 14, tutte senza discrepanze, da 87 a
128 s per lingua.

Le righe `--use_claude_code` sono state misurate il 26 settembre sullo stesso
articolo, quattro traduzioni in parallelo, con effort `low`. Con `sonnet`, le
citazioni inglesi sono rimaste intatte nelle quattordici lingue e, in inglese, il
modello ha rimosso autonomamente le righe di traduzione francese, senza inventare alcuna
bandiera. `opus` non ha scritto alcuna lingua: in ciascuna di esse, i suoi guardrail hanno
bloccato la risposta all'ultimo segmento, a causa di una breve nota su 279 molecole
generate per un sito di legame. Inviata da sola, tale nota viene rifiutata sotto
la categoria «bio»; `sonnet` l'ha tradotta ovunque. `haiku` scrive
tutte le quattordici lingue; in tre di esse (en, pl, ro), un titolo di sezione passa dal
livello 2 al livello 1. Ragiona senza che sia possibile impedirlo — 61% dei
suoi token di output —, da cui più del doppio del tempo rispetto a `sonnet`.

Le righe `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` sono
state misurate il 18 ottobre tramite l'API di Anthropic, sullo stesso articolo, quattro
traduzioni in parallelo per modello. Sonnet 5.5 rifiuta la disattivazione del
suo reasoning: aipmt gli trasmette l'impostazione più bassa accettata, e le sue
risposte non ne recano alcuno. Scrive le quattordici lingue senza discrepanze e senza
dover ripetere alcun segmento; in inglese, ha rimosso autonomamente le righe di
traduzione francese, senza inventare alcuna bandiera, e le citazioni inglesi sono
rimaste intatte ovunque. Haiku 5.5 è stato misurato con il suo reasoning adattivo: a ragionamento
disattivato, lasciava interi paragrafi in francese, respinti dal controllo —
3 lingue scritte su 14. Entrambi gli Haiku inciampano sulla medesima nota: Haiku 5.5
modifica il livello del titolo o lo sdoppia in giapponese, coreano e
cinese, Haiku 4.5 lo porta al livello 1 in sette lingue, e lo lascia in
francese in giapponese. Haiku 4.5 costa 3,67 $ per i due documenti nelle
quattordici lingue, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.

### README di questo progetto, Markdown standard

Revisione congelata il 9 settembre 2026: 785 righe, 285 codici inline, 40
chiusure di blocchi, 89 righe di tabella. Quattro traduzioni in parallelo.

| Modello                                         | Scritte | Senza scostamento | Mediana/lingua | Cosa differisce                                                          |
| ----------------------------------------------- | ------- | ----------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14          | 1 min 43 s     | niente                                                                   |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14          | 1 min 48 s     | niente                                                                   |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14          | 4 min 02 s     | niente per il comparatore; collegamenti interni raddoppiati (en)         |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14          | 1 min 18 s     | niente                                                                   |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14          | 2 min 06 s     | niente                                                                   |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14          | 36 s           | una parola in grassetto (ja)                                             |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14          | 1 min 22 s     | una parola in grassetto (ko)                                             |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14          | 2 min 20 s     | una riga di tabella attaccata alla precedente (ar)                       |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14          | 2 min 56 s     | un link (sv), una parola in grassetto (zh)                               |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14          | 6 min 46 s     | una parola in grassetto (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14          | 2 min 34 s     | una parola in grassetto (hi, ja, ko)                                     |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14          | 2 min 17 s     | 40 codici inline aggiunti in arabo; grassetto (hi, ja, ko)                |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14          | 1 min 14 s     | 2 lingue rifiutate (ar, hi): codici inline persi al ritorno              |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14           | 2 min 44 s     | una sezione persa (ar, hi, ko); blocchi di codice aggiunti (ja, ko, ro, zh) |

Due campagne interrotte non sono valutate: Grok, sessione CLI scaduta
dopo dodici lingue (undici senza scostamento), e `qwen3.8-flash`, HTTP 429 dal
suo hosting provider dopo due. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
non sono stati rimisurati su questa revisione; su quella del 4 e 5 settembre,
più corta di 277 righe, scrivevano ciascuno 9 traduzioni su 14, di cui 7
e 1 senza scostamento.

Le righe `--use_antigravity` e `--use_claude_code` non sono state misurate sulla
revisione congelata, ma il 26 settembre su quella pubblicata con la 1.14.0 — e
le righe `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` il 18
ottobre, sulla stessa: 600 righe, 257 codici inline, 30 chiusure di blocchi, 85
righe di tabella. Più
corta di 185 righe, non si confronta termine a termine con le altre righe;
queste righe qui, invece, si confrontano tra loro. Sui collegamenti interni, che il
comparatore non controlla, `gemini-3.8-flash-medium` li ha mantenuti intatti nelle
quattordici lingue, `gemini-3.7-flash-medium` li ha rotti in italiano;
`sonnet` e `opus` li hanno mantenuti intatti ovunque, `haiku` li ha raddoppiati in
inglese; `claude-sonnet-5-5` e `claude-haiku-4-5` li hanno mantenuti intatti nelle
quattordici lingue, `claude-haiku-5-5` nelle dodici che ha scritto.

### Quattro README di progetti noti

FastAPI, Ollama, tldr-pages e Vue.js, presi tali e quali su GitHub — dei
documenti più facili dei due precedenti. La campagna mirava ai modelli
in difficoltà; Gemini funge qui da punto di confronto.

| Modello                   | Ambito                     | Scritte | Senza scostamento |
| ------------------------- | -------------------------- | ------- | ----------------- |
| `gemini-3.7-flash`        | 4 progetti × 14 lingue     | 56/56   | ✅ **55/56**      |
| `opencode/mimo-v2.5-free` | 4 progetti × 14 lingue     | 55/56   | ❌ 47/56          |
| `grok-4.6` (abbonamento)  | 4 progetti × ar, hi, ja, zh | 16/16   | ❌ 14/16          |
| `ollama/gpt-oss-20b-32k`  | 4 progetti × ar, hi, ja, zh | 15/16   | ❌ 9/16           |

### Cosa non sono queste misurazioni

- **Non una classifica esaustiva**: la sola OpenRouter propone più di quattrocento
  modelli, ne è stata misurata una quindicina.
- **Durate indicative**: da tre a sei traduzioni in parallelo a seconda
  delle campagne, e la velocità di trasferimento di un provider varia nel corso della giornata.
- **Osservazioni datate**: i modelli cambiano con lo stesso nome, e i vostri
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

Entrambe le righe sono necessarie: senza `pip install -e .`, `python -m aipmt`
risponde `No module named aipmt`.

Strumenti di qualità, opzionali ma consigliati:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Le 28 traduzioni del repository (README e CHANGELOG, quattordici lingue) si
rigenerano con `./regen_translations.sh --force` — Codex e `gpt-6.1-sol` sull'abbonamento
ChatGPT per impostazione predefinita, quattro in parallelo. `REGEN_PROVIDER` e
`REGEN_MODEL` cambiano il percorso: `antigravity` rimane su un abbonamento, quello
di Google, e passa senza deroga; un'API a pagamento (`openai`, `gemini`,
`grok`, `openrouter`) viene rifiutata senza `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` imposta un tetto massimo a ciascun job (600 s, 1 800 s su Codex e
Antigravity). Il dettaglio degli strumenti si trova in `CLAUDE.md`.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** — blog personale pubblicato in 15 lingue. La sua
  [rassegna quotidiana sull'IA](https://jls42.org/fr/news) viene tradotta ogni giorno
  da questo strumento e funge da documento di riferimento per le misurazioni di cui sopra.

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avvertenza

Questo programma è distribuito **senza alcuna garanzia**, secondo i termini delle
sezioni 15 e 16 della GPL v3: fornito "così com'è", senza garanzia di commerciabilità
o di idoneità per uno scopo particolare, e il suo autore non può essere
ritenuto responsabile per eventuali danni derivanti dal suo utilizzo. Il testo della
licenza prevale su questo riassunto.

- **Rileggete prima di pubblicare.** Le protezioni coprono i blocchi di codice, il
  codice inline, gli URL, le ancore e le citazioni della modalità `--news` — né i
  titoli, né le tabelle, né il front matter, né il senso delle vostre frasi.
- **I vostri documenti vengono inviati al provider scelto**, secondo i suoi termini
  di servizio e la sua informativa sui dati. Alcuni modelli gratuiti possono
  riutilizzare le vostre conversazioni per l'addestramento, e i termini di Antigravity
  consentono a Google di riutilizzarli e farli revisionare da persone umane,
  compreso l'abbonamento a pagamento; un modello locale è l'unico modo per non far
  uscire alcun dato dalla vostra macchina.
- **Le chiamate API vi vengono fatturate.** Questo programma non pone un limite alla
  spesa: un documento lungo, una ripresa dopo un errore o un modello che ragiona
  molto costano di più.
- **Le misurazioni pubblicate sono osservazioni datate**, non garanzie.

I nomi di prodotti e società citati appartengono ai rispettivi proprietari.
Questo progetto non è affiliato con nessuno di essi.

**Articolo tradotto dal fr all'it con gemini-3.8-flash-medium.**
