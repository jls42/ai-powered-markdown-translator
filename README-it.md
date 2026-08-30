# Traduttore di Markdown AI-Powered

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

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

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Questo script Python traduce file Markdown da una lingua di origine a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche principali

- **Multi-Provider**: supporto di 4 API (OpenAI, Mistral, Claude, Gemini) + CLI Codex con abbonamento ChatGPT
- **Modelli 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modalità economica**: opzione `--eco` per utilizzare modelli più veloci e meno costosi
- **File singolo**: opzione `--file` per tradurre un solo file
- **Segmentazione intelligente**: gestione di testi lunghi con limiti di token per modello
- **Preservazione del codice**: vengono preservati sia i blocchi di codice SIA il codice inline (`` `...` ``)
- **Nome del file**: opzione `--keep_filename` per mantenere il nome originale
- **Modalità News**: opzione `--news` per proteggere le citazioni inglesi e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: supporto del file `.env` per le chiavi API
- **Nota di traduzione**: aggiunta facoltativa di una nota alla fine del documento

## Installazione

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Strumenti per la qualità (facoltativi ma consigliati)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire il commit di codice formattato male, vulnerabile o contenente un segreto. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (CVE delle dipendenze), unittest. Per i dettagli, vedere la sezione _Quality / pre-commit_ di `CLAUDE.md`.

## Configurazione

Crea un file `.env` nella directory radice del progetto oppure definisci le variabili d'ambiente:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` è accettata come alternativa a `GOOGLE_API_KEY` (convenzione AI
Studio). Variabili facoltative: `XAI_BASE_URL` (endpoint xAI, valore predefinito
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondi per chiamata Anthropic, valore predefinito
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
e `GROK_TRANSLATE_SANDBOX` (vedere la sezione Grok CLI).

## Utilizzo

### Tradurre un singolo file

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tradurre una directory

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Tradurre con il proprio abbonamento ChatGPT (`--use_codex`)

Questo provider non utilizza alcuna chiave API: controlla la CLI Codex ufficiale in modalità
non interattiva, quindi la traduzione viene detratta dalla quota dell'abbonamento
ChatGPT (Plus, Pro, Business…) già pagato. È l'unico metodo documentato da
OpenAI per questo utilizzo: i token di `~/.codex/auth.json` non autenticano
le chiamate all'API Platform e, del resto, non vengono mai letti da questo script.

**Prerequisiti:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Il binario viene cercato in quest'ordine: la variabile `CODEX_BIN`, il `PATH`,
quindi il package Python `openai-codex-cli-bin`. Quest'ultimo non è intenzionalmente
in `requirements.txt`: pesa circa 250 MB, un onere che altrimenti verrebbe imposto a tutti gli
utenti per un provider facoltativo.

**Da sapere:**

- **Non viene utilizzata alcuna chiave API.** `OPENAI_API_KEY` e `CODEX_API_KEY` vengono
  rimosse dall'ambiente del sottoprocesso, garantendo che una chiave
  presente in `.env` non faccia mai passare la traduzione alla fatturazione a
  consumo.
- **Un segmento = un «messaggio locale»** della finestra di 5 ore del piano.
  Usa `--eco` (modello `gpt-5.6-luna`, 250-2.000 messaggi/5 h con Plus)
  anziché il modello di qualità (`gpt-5.6-sol`, 10-100 messaggi/5 h).
- **Più lento** di una chiamata API: occorrono circa 45 s per un README completo, rispetto a
  pochi secondi con una chiamata diretta.
- **Rifiutato in CI** (se `CI` o `GITHUB_ACTIONS` sono definiti): l'autenticazione tramite
  abbonamento non è progettata per un runner condiviso e OpenAI sconsiglia questo
  workflow nei repository pubblici. Usa una chiave API in questo caso.
- Variabili d'ambiente: `CODEX_BIN` (percorso esplicito del binario) e
  `CODEX_TIMEOUT` (secondi per segmento, valore predefinito `600`).

### Tradurre con il proprio abbonamento Grok (`--use_grok_cli`)

Stesso principio di `--use_codex`, con la CLI ufficiale **Grok Build**: la
traduzione viene detratta dall'abbonamento Grok (SuperGrok / X Premium+) anziché
essere fatturata per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — da leggere prima dell'uso.** Questo provider è strutturalmente **più
debole** di `--use_codex`, e ciò è intenzionale:

- Codex viene eseguito in `--sandbox read-only`, un confine imposto dal sistema.
- Il sandbox di Grok **non può essere applicato** su molti sistemi Linux
  recenti: AppArmor blocca gli user namespace senza privilegi a partire da Ubuntu
  24.04 e la deny-list dei socket di runtime dei container non funziona se
  `/run/podman` si trova in `0700`. Tuttavia, un profilo **integrato** che non può
  essere applicato viene avviato **senza confinamento e senza alcun avviso**.
- Pertanto, per impostazione predefinita lo script non richiede alcun profilo e **non effettua mai
  silenziosamente un fallback**: mostra un avviso. Il confinamento si basa sulle
  regole `--deny` della CLI (incluso il catch-all `*`), l'unico livello verificato
  come _fail-closed_: una regola sconosciuta impedisce l'avvio anziché
  rimuovere la protezione senza segnalarlo.
- Per **esigere** il sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`.
  L'avvio non riuscirà se il sistema non è in grado di applicarlo, che è il
  comportamento desiderato.

**Quota**: il pool Grok è **settimanale e condiviso** con Chat, Imagine e
Voice, e non esiste alcun comando per consultarlo. Un'elaborazione batch può quindi
ridurre la tua disponibilità per le conversazioni senza che venga segnalato nulla: da qui una
concorrenza limitata a 2 e un avviso in `regen_translations.sh`.

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

Utilizza modelli più veloci e meno costosi (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Opzione                  | Descrizione                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| `--file`                 | Singolo file Markdown da tradurre                                          |
| `--source_dir`           | Directory di origine contenente i file Markdown                            |
| `--target_dir`           | Directory di output per i file tradotti                                    |
| `--source_lang`          | Lingua di origine (valore predefinito: `fr`)                              |
| `--target_lang`          | Lingua di destinazione (valore predefinito: `en`)                         |
| `--model`                | Modello specifico da utilizzare                                            |
| `--eco`                  | Utilizzare i modelli economici                                             |
| `--use_mistral`          | Utilizzare l'API Mistral AI                                                |
| `--use_claude`           | Utilizzare l'API Claude                                                    |
| `--use_gemini`           | Utilizzare l'API Gemini                                                    |
| `--use_codex`            | Utilizzare la CLI Codex con la quota dell'abbonamento ChatGPT              |
| `--use_grok`             | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                       |
| `--use_grok_cli`         | Utilizzare la CLI Grok con la quota dell'abbonamento Grok                  |
| `--force`                | Forzare la ritraduzione                                                    |
| `--keep_filename`        | Mantenere il nome del file originale                                       |
| `--news`                 | Modalità notizie: protegge le citazioni EN e gestisce le bandiere per lingua |
| `--add_translation_note` | Aggiungere una nota di traduzione                                          |
| `--note_position`        | Posizione della nota: `top`, `bottom` (valore predefinito) o `both` |
| `--note_format`          | Formato della nota: `legacy` (valore predefinito, paragrafo in grassetto) o `marker` |
| `--include_model`        | Includere il nome del modello nel file di output                           |
| `--reasoning_effort`     | Livello di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

### Nota di traduzione: posizioni e formati

Con `--add_translation_note`, il translator può posizionare la nota in alto, in basso o in entrambe le posizioni e renderla in formato testo semplice (retrocompatibile) oppure in formato `marker` utilizzabile da un plugin Markdown.

**Posizione** (`--note_position`):

- `bottom` (valore predefinito): nota alla fine del file, come in precedenza.
- `top`: nota inserita **dopo il frontmatter YAML** (compatibilità con Astro Content Collections, gray-matter, ecc.).
- `both`: nota inserita sia in alto SIA in basso (una sola chiamata LLM, contenuto riutilizzato in entrambe le posizioni).

**Formato** (`--note_format`):

- `legacy` (valore predefinito): paragrafo in grassetto `**...**` — comportamento rigorosamente identico alla v1.8, byte-for-byte. Compatibile con Hugo, GitHub, GitLab e qualsiasi renderer Markdown.
- `marker`: link reference definition Markdown invisibile (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguita da un blockquote in grassetto. Leggibile nativamente su GitHub/GitLab e utilizzabile durante la build da un plugin remark lato Astro per produrre un banner stilizzato (cfr. blog jls42.org).

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

| Provider | Qualità (valore predefinito) | Economico (`--eco`) |
| -------- | ---------------------------- | -------------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Raccomandazione per traduzioni long-form**: `--use_gemini` (valore predefinito = `gemini-3.7-flash`) preserva fedelmente la struttura markdown negli script non latini (PL, JA, ZH, AR, HI), anche in modalità `--news`, dove la fedeltà dei placeholder è importante. Misurato su questo README tradotto in giapponese: struttura identica a `gemini-3.1-pro-preview` (21 liste, 18 blocchi di codice, 13 link HTML, 13 immagini, tutti gli URL preservati) con una latenza circa 6 volte inferiore. OpenAI rimane il valore predefinito per la retrocompatibilità.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](LICENSE).

**Articolo tradotto dal francese all'italiano con gpt-5.6-sol.**
