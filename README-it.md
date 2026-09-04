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

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** e **Grok (xAI)** — tramite API, sfruttando la quota di un abbonamento ChatGPT (Codex) o Grok senza fatturazione a consumo, oppure tramite **OpenCode**, l'agente open source, verso il provider scelto: modello locale (Ollama), gratuito, in abbonamento (GitHub Copilot…) o con chiave.

Questo script Python traduce file Markdown da una lingua di origine a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati front matter.

## Caratteristiche principali

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI in abbonamento, senza fatturazione a consumo — Codex (ChatGPT) e Grok — + OpenCode (open source, MIT) verso qualsiasi provider configurato in OpenCode, incluso un modello locale
- **Modelli 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modalità economica**: opzione `--eco` per utilizzare modelli più veloci e meno costosi
- **File singolo**: opzione `--file` per tradurre un solo file
- **Segmentazione intelligente**: gestione dei testi lunghi con limiti di token specifici per modello
- **Preservazione del codice**: i blocchi di codice E il codice inline (`` `...` ``) vengono preservati
- **Nome del file**: opzione `--keep_filename` per conservare il nome originale
- **Modalità News**: opzione `--news` per proteggere le citazioni in inglese e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: supporto del file `.env` per le chiavi API
- **Nota di traduzione**: aggiunta facoltativa di una nota alla fine del documento

## Installazione

### Per utilizzare lo strumento

```bash
pip install ai-powered-markdown-translator
```

Il comando `aipmt` è quindi disponibile ovunque. Se la directory degli script
di Python non è nel proprio `PATH`, `python -m aipmt` esegue esattamente la stessa
operazione. È richiesto Python 3.10 o più recente.

Per un'installazione isolata dal resto dei propri pacchetti:

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

`requirements.txt` è un **lock completamente vincolato**, che rispecchia esattamente
l'ambiente testato. I vincoli pubblicati in `pyproject.toml` sono
volutamente più ampi: non impongono nulla agli altri pacchetti.

### Strumenti per la qualità (facoltativi ma consigliati)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire il commit di codice formattato male, vulnerabile o contenente un segreto. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (CVE delle dipendenze), unittest. Consultare la sezione _Quality / pre-commit_ di `CLAUDE.md` per i dettagli.

## Configurazione

Le chiavi vengono cercate in **tre posizioni**, dalla priorità più alta a quella più bassa.
Ciascuna si limita a colmare ciò che la precedente ha lasciato vuoto.

|     | Dove                                          | Per cosa                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabili d'ambiente                          | CI, container, deroga occasionale     |
| 2   | `.env` della directory corrente (o di una directory superiore) | una chiave specifica per un progetto  |
| 3   | `~/.config/aipmt/.env`                        | **installato una volta, valido ovunque** |

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
(altrimenti viene ignorata, come prescrive la specifica) e `%APPDATA%`
su Windows.

La seconda opzione resta utile quando un repository dispone di una propria chiave: un `.env` nella sua radice
prevale sulla configurazione utente, senza modificarla. Inoltre, una
variabile già definita nell'ambiente prevale su entrambe:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Se non viene trovata alcuna chiave, il comando non mostra alcuno stack trace:
elenca le tre posizioni con il relativo percorso esatto.

`GEMINI_API_KEY` è accettato come alternativa a `GOOGLE_API_KEY` (convenzione AI
Studio). Variabili facoltative: `XAI_BASE_URL` (endpoint xAI, valore predefinito
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondi per chiamata Anthropic, valore predefinito
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consultare la sezione Grok CLI) e `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consultare la sezione OpenCode). Per
`regen_translations.sh`: `REGEN_PROVIDER` (valore predefinito `codex`, in abbonamento),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (deroga obbligatoria per un'API
a pagamento) e `REGEN_JOB_TIMEOUT` (limite per job, valore predefinito 600 s, 1.800 s su Codex).

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

### Tradurre con il proprio abbonamento ChatGPT (`--use_codex`)

Questo provider non utilizza alcuna chiave API: controlla la CLI Codex ufficiale in modalità
non interattiva, quindi la traduzione viene conteggiata nella quota dell'abbonamento
ChatGPT (Plus, Pro, Business…) già pagato. È l'unica modalità documentata da
OpenAI per questo utilizzo: i token di `~/.codex/auth.json` non autenticano
le chiamate alla Platform API e, del resto, non vengono mai letti da questo script.

**Prerequisiti:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Il binario viene cercato in quest'ordine: la variabile `CODEX_BIN`, il `PATH`,
quindi il pacchetto Python `openai-codex-cli-bin`. Quest'ultimo non è intenzionalmente
in `requirements.txt`: pesa circa 250 MB, che verrebbero imposti a tutti gli
utenti per un provider facoltativo.

**Da sapere:**

- **Non viene utilizzata alcuna chiave API.** `OPENAI_API_KEY` e `CODEX_API_KEY` vengono
  rimosse dall'ambiente del sottoprocesso, garantendo che una chiave
  presente in `.env` non faccia mai passare la traduzione alla fatturazione
  a consumo.
- **Un segmento = un «messaggio locale»** della finestra di 5 ore del piano.
  Utilizzare `--eco` (modello `gpt-5.6-luna`, 250-2.000 messaggi/5 h su Plus)
  anziché il modello di qualità (`gpt-5.6-sol`, 10-100 messaggi/5 h).
- **Più lento** di una chiamata API: occorrono circa 45 s per un README completo, contro
  pochi secondi con una chiamata diretta.
- **Rifiutato in CI** (se `CI` o `GITHUB_ACTIONS` è definito): l'autenticazione tramite
  abbonamento non è pensata per un runner condiviso e OpenAI sconsiglia questo
  workflow nei repository pubblici. Utilizzare una chiave API in questo caso.
- Variabili d'ambiente: `CODEX_BIN` (percorso esplicito del binario) e
  `CODEX_TIMEOUT` (secondi per segmento, valore predefinito `600`).

### Tradurre con il proprio abbonamento Grok (`--use_grok_cli`)

Stesso principio di `--use_codex`, con la CLI ufficiale **Grok Build**: la
traduzione viene conteggiata nell'abbonamento Grok (SuperGrok / X Premium+) invece
di essere fatturata per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — da leggere prima dell'uso.** Questo provider è strutturalmente **più
debole** di `--use_codex`, ed è una scelta consapevole:

- Codex viene eseguito in `--sandbox read-only`, un confine imposto dal sistema.
- Il sandbox di Grok **non può essere applicato** su molte workstation Linux
  recenti: AppArmor blocca gli user namespace non privilegiati da Ubuntu
  24.04 e la deny-list dei socket del runtime dei container non funziona se
  `/run/podman` si trova in `0700`. Tuttavia, un profilo **integrato** che non può
  essere applicato si avvia **senza confinamento e senza avvisare**.
- Lo script non richiede quindi alcun profilo per impostazione predefinita e **non ricorre mai
  silenziosamente a un'alternativa**: mostra un avviso. Il confinamento si basa sulle
  regole `--deny` della CLI (inclusa la catch-all `*`), l'unico livello misurato
  _fail-closed_: una regola sconosciuta impedisce l'avvio, invece di
  rimuovere la protezione senza segnalarlo.
- Per **richiedere** il sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`.
  L'avvio non riuscirà se la macchina non può rispettarlo, che è il
  comportamento desiderato.

**Quota**: il pool Grok è **settimanale e condiviso** con Chat, Imagine e
Voice e nessun comando consente di consultarlo. Un'elaborazione in batch può quindi
ridurre il tuo utilizzo conversazionale senza alcuna segnalazione: da qui una
concorrenza limitata a 2 e un avviso in `regen_translations.sh`.

Altre variabili: `GROK_BIN` (percorso del binario), `GROK_TIMEOUT` (valore predefinito 900 s).

Per rigenerare le 28 traduzioni:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Tradurre con OpenCode, verso il provider scelto (`--use_opencode`)

[OpenCode](https://opencode.ai) è un agente di programmazione **open source (MIT)** da
terminale. Non è un provider di modelli, ma un **router** verso quelli
configurati direttamente in OpenCode: una chiave API, un abbonamento
(GitHub Copilot, ChatGPT, SuperGrok), il gateway OpenCode Zen — che offre
modelli gratuiti **senza account** — oppure un modello **locale** (Ollama, LM Studio,
llama.cpp). Questo provider controlla `opencode run` in modalità non interattiva e limita
la chiamata a un unico scambio, senza alcuno strumento.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` è **obbligatorio**, nel formato `provider/modèle`. OpenCode non è un
provider e non viene selezionato alcun valore predefinito al posto dell'utente: il suo fallback
sarebbe un modello gratuito le cui interazioni possono essere utilizzate per l'addestramento.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamento — ciò che lo script esegue a ogni chiamata:**

- Una configurazione inline (`OPENCODE_CONFIG_CONTENT`), prioritaria rispetto alla
  propria, definisce un agente `aipmt` per il quale **tutti gli strumenti sono negati**
  (`permission: { "*": "deny" }`): il modello non può leggere, scrivere né
  eseguire comandi; dalle misurazioni, non tenta nemmeno di farlo. La condivisione della sessione
  è disattivata, `--pure` esclude i plugin esterni, mai `--auto`.
- La chiamata viene eseguita in una **directory temporanea e vuota**, con le opzioni
  `OPENCODE_DISABLE_PROJECT_CONFIG` e `OPENCODE_DISABLE_CLAUDE_CODE`: senza
  di esse, OpenCode inserisce in ogni prompt l'`AGENTS.md` della directory corrente
  e il proprio `~/.claude/CLAUDE.md` — nelle misurazioni, un'istruzione «termina ogni risposta
  con BANANA» inserita in un `AGENTS.md` veniva applicata alla traduzione. Le
  regole globali di `~/.config/opencode/AGENTS.md` continuano invece
  a essere applicate: OpenCode non consente di escluderle.
- Il contratto di output richiede contemporaneamente: codice di uscita 0, nessun evento
  `error`, nessuna chiamata a strumenti, un ultimo passaggio completato in `stop`, testo non
  vuoto e agente effettivamente caricato — un `--agent` sconosciuto non provoca
  il fallimento di OpenCode, che **ricorre silenziosamente** all'agente di programmazione, con gli strumenti
  attivi. Anche un `exit 0` non dimostra nulla in questo caso.
- **Nessuna chiave di aipmt viene trasmessa** al sottoprocesso (lo stesso filtraggio
  utilizzato con Codex e Grok), con un'unica eccezione nominativa: `OPENCODE_API_KEY`,
  la chiave dello stesso OpenCode (Zen, Go). I provider vengono configurati in
  OpenCode (`opencode auth login`, `opencode.json`), non nel `.env` di aipmt.

**Da sapere:**

- **I modelli gratuiti di Zen sono modelli «stealth» o forniti da contributori**,
  variabili, con limiti non documentati, e le loro interazioni possono essere utilizzate per
  l'addestramento: perfetti per la documentazione pubblica, da evitare per
  contenuti privati. Dalle misurazioni: `opencode/mimo-v2.5-free` traduce questo README in una
  sola passata; `opencode/big-pickle` è più lento e due richieste simultanee sono
  rimaste senza risposta.
- **Un modello locale deve offrire almeno 16 k di contesto** — i segmenti arrivano
  fino a 16.000 caratteri — mentre Ollama spesso ne configura 4.096 per
  impostazione predefinita. Con Ollama: un `Modelfile` con `PARAMETER num_ctx 32768`, quindi
  `ollama create`. La qualità dipende dal modello: un 7B ha invertito un elenco e
  danneggiato la chiusura di un blocco di codice in un file di prova, mentre un modello
  del gateway ha preservato tutto.
- `--eco` non ha effetto (il modello è quello di `--model`);
  `--reasoning_effort` viene trasmesso invariato come `--variant` di OpenCode, da
  richiedere soltanto se il modello lo supporta.
- Le sessioni vengono registrate da OpenCode nel suo database
  (`~/.local/share/opencode/`), come qualsiasi sessione OpenCode.
- Variabili d'ambiente: `OPENCODE_BIN` (percorso esplicito del binario,
  altrimenti il `PATH` e poi `~/.opencode/bin/opencode`) e `OPENCODE_TIMEOUT`
  (secondi per segmento, valore predefinito `600`). `OPENCODE_CONFIG` viene rispettato se
  esportato.

**Esempio misurato: un modello locale tramite Ollama** (RTX 3060 12 GB, 62 GB di RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

Quindi il provider in `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` non è un dettaglio: Ollama abilita la riflessione per
impostazione predefinita su Gemma 4 e Qwen 3.5, e un Modelfile non può disattivarla. Dalle misurazioni
tramite OpenCode: senza l'opzione, «Il gatto dorme sul tappeto» costa 919 token
di ragionamento e 68 s; con l'opzione, 9 token.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Risultati su un vero articolo di blog di 589 righe (140 link, 21 sezioni,
3 citazioni inglesi protette dalla modalità `--news`), stesso comando, tre
modelli:

| Modello                                  | Durata       | Struttura                                                  | Differenze                                                                                 |
| ---------------------------------------- | ------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `opencode/mimo-v2.5-free` (Zen, gratuito) | 4 min 26 s  | identica alla fonte                                        | nessuna                                                                                    |
| `ollama/gemma4-12b-32k` (locale)        | 10 min 10 s | link, URL, tabelle, tag, grassetto e codice inline identici | una riga di citazione inventata (🇺🇸 + parafrasi), un'attribuzione duplicata                |
| `ollama/qwen3.5-9b-32k` (locale)        | 8 min 18 s  | link, URL, tabelle e tag identici                          | una riga di citazione inventata, alcuni grassetti e codici inline aggiunti, un segmento rielaborato |

Durante la traduzione locale: GPU al 98% e 170 W, 10 GB di VRAM occupati
(modello e cache da 32 k token, nulla scaricato nella RAM), 7,5 GB di RAM per il
server Ollama. Un modello da 9 a 12 miliardi di parametri rispetta la
struttura, ma si concede una libertà per articolo, mentre il modello del gateway
non se ne è concessa alcuna: da rileggere prima della pubblicazione oppure da riservare alle bozze.

### Modalità economica

Utilizza modelli più veloci e meno costosi (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opzioni

| Opzione                   | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Singolo file Markdown da tradurre                                                                            |
| `--source_dir`           | Directory sorgente contenente i file Markdown                                                             |
| `--target_dir`           | Directory di output per i file tradotti                                                               |
| `--source_lang`          | Lingua sorgente (predefinita: `fr`)                                                                                  |
| `--target_lang`          | Lingua di destinazione (predefinita: `en`)                                                                                   |
| `--model`                | Modello specifico da utilizzare                                                                                  |
| `--eco`                  | Utilizzare i modelli economici                                                                              |
| `--use_mistral`          | Utilizzare l'API Mistral AI                                                                                     |
| `--use_claude`           | Utilizzare l'API Claude                                                                                         |
| `--use_gemini`           | Utilizzare l'API Gemini                                                                                         |
| `--use_codex`            | Utilizzare il CLI Codex con la quota dell'abbonamento ChatGPT                                                    |
| `--use_grok`             | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Utilizzare il CLI Grok con la quota dell'abbonamento Grok                                                        |
| `--use_opencode`         | Utilizzare OpenCode (open source) con il provider configurato in OpenCode; richiede `--model provider/modèle` |
| `--force`                | Forzare la ritraduzione                                                                                       |
| `--keep_filename`        | Conservare il nome del file originale                                                                          |
| `--news`                 | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua                                      |
| `--add_translation_note` | Aggiungere una nota di traduzione                                                                                |
| `--note_position`        | Posizione della nota: `top`, `bottom` (predefinita) o `both`                                                     |
| `--note_format`          | Formato della nota: `legacy` (predefinito, paragrafo in grassetto) o `marker`                                            |
| `--include_model`        | Includere il nome del modello nel file di output                                                            |
| `--reasoning_effort`     | Livello di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **I sette flag dei provider si escludono a vicenda.** In precedenza, combinarne due
> veniva accettato silenziosamente e si risolveva nel primo verificato: una
> traduzione richiesta con la quota dell'abbonamento (`--use_codex`, `--use_grok_cli`)
> poteva così essere fatturata in base all'utilizzo senza alcun avviso.
> `argparse` ora rifiuta la combinazione.

### Nota di traduzione: posizioni e formati

Con `--add_translation_note`, il translator può posizionare la nota in alto, in basso o in entrambi i punti e renderla sia in formato testo semplice (retrocompatibile) sia in formato `marker` utilizzabile da un plugin Markdown.

**Posizione** (`--note_position`):

- `bottom` (predefinita): nota alla fine del file, come in passato.
- `top`: nota inserita **dopo il frontmatter YAML** (compatibilità con Astro Content Collections, gray-matter, ecc.).
- `both`: nota inserita sia in alto SIA in basso (una sola chiamata LLM, contenuto riutilizzato per entrambe le posizioni).

**Formato** (`--note_format`):

- `legacy` (predefinito): paragrafo in grassetto `**...**` — comportamento rigorosamente identico alla v1.8, byte per byte. Compatibile con Hugo, GitHub, GitLab e qualsiasi renderer Markdown.
- `marker`: definizione di riferimento Markdown invisibile (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguita da una citazione in grassetto. Leggibile nativamente su GitHub/GitLab e utilizzabile durante la build da un plugin remark lato Astro per produrre un banner stilizzato (vedi blog jls42.org).

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
| OpenCode | `--model provider/modèle` obbligatorio | invariato — `--eco` senza effetto |

> **Raccomandazione per traduzioni long-form**: `--use_gemini` (predefinito = `gemini-3.7-flash`) preserva fedelmente la struttura Markdown per le scritture non latine (PL, JA, ZH, AR, HI), anche in modalità `--news`, dove la fedeltà dei placeholder è importante. Misurato su questo README tradotto in giapponese: struttura identica a `gemini-3.1-pro-preview` (21 elenchi, 18 blocchi di codice, 13 link HTML, 13 immagini, tutti gli URL preservati) con una latenza circa 6 volte inferiore. OpenAI resta l'impostazione predefinita per la retrocompatibilità.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Vedere [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articolo tradotto dal francese all'italiano con gpt-5.6-sol.**
