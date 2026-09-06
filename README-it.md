# Traduttore Markdown basato sull'AI

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

Traduttore di file Markdown che utilizza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** e **Grok (xAI)** — tramite API, sfruttando la quota di un abbonamento ChatGPT (Codex) o Grok senza fatturazione a consumo, oppure tramite **OpenCode**, l'agente open source, con il provider scelto: modello locale (Ollama), gratuito, in abbonamento (GitHub Copilot…) o mediante chiave.

Questo script Python traduce file Markdown da una lingua di origine a una lingua di destinazione preservando la formattazione, i blocchi di codice e i metadati del front matter.

## Caratteristiche principali

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI in abbonamento, senza fatturazione a consumo — Codex (ChatGPT) e Grok — + OpenCode (open source, MIT) con qualsiasi provider configurato in OpenCode, incluso un modello locale
- **Modelli 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modalità economica**: opzione `--eco` per utilizzare modelli più veloci e meno costosi
- **File singolo**: opzione `--file` per tradurre un solo file
- **Segmentazione intelligente**: gestione dei testi lunghi con limiti di token specifici per modello
- **Preservazione del codice**: i blocchi di codice E il codice inline (`` `...` ``) vengono preservati
- **Nome del file**: opzione `--keep_filename` per mantenere il nome originale
- **Modalità News**: opzione `--news` per proteggere le citazioni in inglese e gestire le bandiere negli articoli di attualità
- **Configurazione .env**: supporto del file `.env` per le chiavi API
- **Nota di traduzione**: aggiunta facoltativa di una nota alla fine del documento

## Installazione

### Per utilizzare lo strumento

```bash
pip install ai-powered-markdown-translator
```

Il comando `aipmt` è quindi disponibile ovunque. Se la directory degli script
di Python non è inclusa nel tuo `PATH`, `python -m aipmt` esegue esattamente la stessa
operazione. È richiesto Python 3.10 o una versione successiva.

Per un'installazione isolata dal resto dei pacchetti:

```bash
pipx install ai-powered-markdown-translator
```

### Per contribuire al progetto

Il repository clonato resta necessario per lo sviluppo: è qui che si trovano i test,
le 28 traduzioni e tutti gli strumenti per la qualità.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` è un **lock completamente vincolato**, che rispecchia esattamente
l'ambiente testato. I limiti pubblicati in `pyproject.toml` sono
intenzionalmente più ampi: non impongono alcun vincolo agli altri pacchetti.

### Strumenti per la qualità (facoltativi ma consigliati)

Il progetto utilizza [`pre-commit`](https://pre-commit.com) per impedire il commit di codice mal formattato, vulnerabile o contenente un segreto. Installazione:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook attivi: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complessità), detect-secrets (chiavi API), mypy (tipizzazione progressiva), Opengrep (SAST), pip-audit (CVE delle dipendenze), unittest. Consulta la sezione _Quality / pre-commit_ di `CLAUDE.md` per i dettagli.

## Configurazione

Le chiavi vengono cercate in **tre posizioni**, dalla priorità più alta alla più bassa.
Ognuna si limita a completare ciò che la precedente ha lasciato vuoto.

|     | Dove                                          | Per cosa                                      |
| --- | --------------------------------------------- | --------------------------------------------- |
| 1   | Variabili d'ambiente                          | CI, container, eccezioni occasionali          |
| 2   | `.env` della directory corrente (o di una directory superiore) | una chiave specifica per un progetto           |
| 3   | `~/.config/aipmt/.env`                               | **installato una volta, valido ovunque**       |

La soluzione più semplice dopo un `pip install` è la terza:

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

Questo file segue `XDG_CONFIG_HOME` quando la variabile indica un percorso assoluto
(altrimenti viene ignorata, come prescritto dalla specifica) e `%APPDATA%`
su Windows.

La seconda opzione resta utile quando un repository dispone di una propria chiave: un `.env` nella sua directory radice
prevale quindi sulla configurazione dell'utente, senza modificarla. Una
variabile già definita nell'ambiente prevale su entrambe:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Se non viene trovata alcuna chiave, il comando non mostra uno stack trace:
elenca le tre posizioni con il relativo percorso esatto.

`GEMINI_API_KEY` è accettato come alternativa a `GOOGLE_API_KEY` (convenzione AI
Studio). Variabili facoltative: `XAI_BASE_URL` (endpoint xAI, valore predefinito
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondi per chiamata Anthropic, valore predefinito
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consulta la sezione Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consulta la sezione OpenCode) e `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (consulta la sezione
OpenRouter). Per
`regen_translations.sh`: `REGEN_PROVIDER` (valore predefinito `codex`, in abbonamento),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (eccezione obbligatoria per un'API
a pagamento) e `REGEN_JOB_TIMEOUT` (limite per job, valore predefinito 600 s, 1.800 s con Codex).

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Tradurre utilizzando il proprio abbonamento ChatGPT (`--use_codex`)

Questo provider non utilizza alcuna chiave API: controlla la CLI ufficiale di Codex in modalità
non interattiva, quindi la traduzione viene conteggiata nella quota dell'abbonamento
ChatGPT (Plus, Pro, Business…) già pagato. È l'unico metodo documentato da
OpenAI per questo utilizzo: i token di `~/.codex/auth.json` non autenticano
le chiamate all'API Platform e, inoltre, non vengono mai letti da questo script.

**Prerequisiti:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Il binario viene cercato nel seguente ordine: la variabile `CODEX_BIN`, il `PATH`,
quindi il pacchetto Python `openai-codex-cli-bin`. Quest'ultimo, intenzionalmente,
non è incluso in `requirements.txt`: occupa circa 250 MB, che verrebbero imposti a tutti gli
utenti per un provider facoltativo.

**Da sapere:**

- **Non viene utilizzata alcuna chiave API.** `OPENAI_API_KEY` e `CODEX_API_KEY` vengono
  rimosse dall'ambiente del sottoprocesso, garantendo che una chiave
  presente in `.env` non possa mai far passare la traduzione alla fatturazione
  a consumo.
- **Un segmento = un «messaggio locale»** della finestra di 5 ore del piano.
  Utilizza `--eco` (modello `gpt-5.6-luna`, 250-2.000 messaggi/5 h con Plus)
  invece del modello di qualità (`gpt-5.6-sol`, 10-100 messaggi/5 h).
- **Più lento** di una chiamata API: occorrono circa 45 s per un README completo, rispetto a
  pochi secondi con una chiamata diretta.
- **Non consentito in CI** (se `CI` o `GITHUB_ACTIONS` sono definiti): l'abbonamento
  si autentica mediante un file di sessione personale e trasferirlo su un runner
  condiviso equivale a depositarvi un'identità riutilizzabile da qualsiasi processo
  in esecuzione. Utilizza una chiave API in questo caso.
- Variabili d'ambiente: `CODEX_BIN` (percorso esplicito del binario) e
  `CODEX_TIMEOUT` (secondi per segmento, valore predefinito `600`).

### Tradurre utilizzando il proprio abbonamento Grok (`--use_grok_cli`)

Lo stesso principio di `--use_codex`, con la CLI ufficiale **Grok Build**: la
traduzione viene conteggiata nell'abbonamento Grok (SuperGrok / X Premium+) anziché
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
  24.04 e la deny-list dei socket del runtime dei container non riesce se
  `/run/podman` è in `0700`. Tuttavia, un profilo **integrato** che non può
  essere applicato viene avviato **senza confinamento e senza alcun avviso**.
- Lo script non richiede quindi alcun profilo per impostazione predefinita e **non ricorre mai
  silenziosamente a un'alternativa**: mostra un avviso. Il confinamento si basa sulle
  regole `--deny` della CLI (incluso il catch-all `*`), l'unico livello verificato
  come _fail-closed_: una regola sconosciuta impedisce l'avvio anziché
  rimuovere la protezione senza segnalarlo.
- Per **richiedere** il sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`.
  L'avvio non riuscirà se il sistema non è in grado di rispettarlo, che è il
  comportamento desiderato.

**Quota**: il pool di Grok è **settimanale e condiviso** con Chat, Imagine e
Voice e nessun comando permette di visualizzarlo. Un'elaborazione batch può quindi
ridurre l'utilizzo disponibile per le conversazioni senza alcuna segnalazione: per questo
la concorrenza è limitata a 2 e viene mostrato un avviso in `regen_translations.sh`.

Altre variabili: `GROK_BIN` (percorso del binario), `GROK_TIMEOUT` (valore predefinito 900 s).

Per rigenerare le 28 traduzioni:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### Tradurre con OpenCode, verso il provider scelto (`--use_opencode`)

[OpenCode](https://opencode.ai) è un agente di coding **open source (MIT)** per il
terminale. Non è un provider di modelli, ma un **router** verso quelli
configurati in OpenCode stesso: una chiave API, un abbonamento,
il gateway OpenCode Zen — che offre modelli gratuiti **senza account** — oppure
un modello **locale**. Questo provider esegue `opencode run` in modalità non interattiva e
limita la chiamata a un unico scambio, senza alcuno strumento.

Due di queste modalità sono state misurate end-to-end qui: il **gateway Zen** e
**Ollama** in locale. Le altre annunciate da OpenCode (GitHub Copilot, LM Studio,
llama.cpp) dovrebbero funzionare per costruzione, poiché il provider comunica
solo con OpenCode — ma non sono state testate e questo README riporta soltanto
ciò che è stato verificato.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` è **obbligatorio**, nel formato `provider/modèle`. OpenCode non è
un provider e non viene selezionato alcun valore predefinito al posto vostro: il suo fallback
sarebbe un modello gratuito le cui conversazioni potrebbero essere usate per l'addestramento.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamento — cosa fa lo script a ogni chiamata:**

- Una configurazione inline (`OPENCODE_CONFIG_CONTENT`), prioritaria rispetto alla
  vostra, definisce un agente `aipmt` in cui **tutti gli strumenti sono negati**
  (`permission: { "*": "deny" }`): il modello non può leggere, scrivere né
  eseguire comandi — dalle misurazioni, non prova nemmeno a farlo. La condivisione della sessione
  è disattivata, `--pure` esclude i plugin esterni, mai `--auto`.
- La chiamata viene eseguita in una **directory temporanea e vuota**, con le opzioni
  `OPENCODE_DISABLE_PROJECT_CONFIG` e `OPENCODE_DISABLE_CLAUDE_CODE`: senza
  di esse, OpenCode inserisce in ogni prompt l'`AGENTS.md` della directory corrente
  e il vostro `~/.claude/CLAUDE.md` — dalle misurazioni, un'istruzione «terminare ogni risposta
  con BANANA» inserita in un `AGENTS.md` veniva applicata alla traduzione. Le
  regole globali di `~/.config/opencode/AGENTS.md` rimangono invece
  applicate: OpenCode non permette di escluderle.
- Il contratto di output richiede contemporaneamente: codice di uscita 0, nessun evento
  `error`, nessuna chiamata a strumenti, un ultimo passaggio completato con `stop`, testo non
  vuoto e l'agente effettivamente caricato — un `--agent` sconosciuto non provoca
  il fallimento di OpenCode, che **torna silenziosamente** all'agente di coding, con gli strumenti
  attivi. Neppure un `exit 0` dimostra nulla in questo caso.
- **Nessuna chiave di aipmt viene trasmessa** al sottoprocesso (lo stesso filtraggio
  usato con Codex e Grok), con una sola eccezione nominativa: `OPENCODE_API_KEY`,
  la chiave di OpenCode stesso (Zen, Go). I provider si configurano in
  OpenCode (`opencode auth login`, `opencode.json`), non nel `.env` di aipmt.

**Da sapere:**

- **I modelli gratuiti di Zen sono modelli «stealth» o forniti da contributori**,
  variabili, con limiti non documentati, e le loro conversazioni possono essere usate per
  l'addestramento: perfetti per la documentazione pubblica, da evitare per i
  contenuti privati. Dalle misurazioni: `opencode/mimo-v2.5-free` traduce questo README in
  un solo passaggio; `opencode/big-pickle` è più lento e due richieste simultanee sono
  rimaste senza risposta.
- **Un modello locale deve offrire almeno 16 k di contesto** — i segmenti raggiungono
  i 16.000 caratteri — mentre Ollama ne configura spesso 4.096 per
  impostazione predefinita. Con Ollama: un `Modelfile` con `PARAMETER num_ctx 32768`, quindi
  `ollama create`. La qualità dipende dal modello: un 7B ha invertito una lista e
  danneggiato la chiusura di un blocco di codice in un file di prova, mentre un modello del
  gateway ha preservato tutto.
- `--eco` non ha effetto (il modello è quello di `--model`);
  `--reasoning_effort` viene trasmesso senza modifiche come `--variant` di OpenCode, da
  richiedere solo se il modello lo supporta.
- Le sessioni vengono registrate da OpenCode nel suo database
  (`~/.local/share/opencode/`), come qualsiasi sessione OpenCode.
- Variabili d'ambiente: `OPENCODE_BIN` (percorso esplicito del binario,
  altrimenti il `PATH` e poi `~/.opencode/bin/opencode`) e `OPENCODE_TIMEOUT`
  (secondi per segmento, valore predefinito `600`). `OPENCODE_CONFIG` viene rispettato se
  esportato.

**Esempio misurato: un modello locale tramite Ollama** (RTX 3060 12 GB, 62 GB di RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
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

`reasoningEffort: "none"` non è un dettaglio: Ollama abilita il ragionamento per
impostazione predefinita su questi modelli e un Modelfile non può disattivarlo. Misurato
tramite OpenCode: senza l'opzione, «Il gatto dorme sul tappeto» costa 919 token
di ragionamento e 68 s; con l'opzione, 9 token.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Risultati su un vero articolo di blog di 589 righe (140 link, 21 sezioni,
3 citazioni inglesi protette dalla modalità `--news`), stesso comando, tre
modelli:

| Modello                                  | Durata      | Struttura                                                  | Differenze                                                                                |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuito) | 4 min 26 s  | identica alla fonte                                        | nessuna                                                                                   |
| `ollama/gemma4-12b-32k` (locale)         | 10 min 10 s | link, URL, tabelle, tag, grassetti e codice inline identici | una riga di citazione inventata (🇺🇸 + parafrasi), un'attribuzione duplicata               |
| `ollama/qwen3.5-9b-32k` (locale)         | 8 min 18 s  | link, URL, tabelle e tag identici                          | una riga di citazione inventata, alcuni grassetti e codici inline aggiunti, un segmento rielaborato |

Questi due modelli locali sono stati successivamente **scartati**: una sola libertà per articolo
è sufficiente a squalificare un modello per le traduzioni pubblicate. Altri cinque sono stati
scartati per gli stessi motivi o per timeout (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Solo
`gpt-oss:20b` è stato mantenuto — e persino questo lascia alcuni passaggi in francese in
un articolo denso; vedere la tabella dei modelli consigliati.

Durante la traduzione locale: GPU al 98% e 170 W, 10 GB di VRAM utilizzati
(modello e cache da 32 k token, nulla scaricato nella RAM), 7,5 GB di RAM per il
server Ollama. Un modello da 9 a 12 miliardi di parametri rispetta la
struttura, ma si concede una libertà per articolo, mentre il modello del gateway
non se n'è concessa nessuna: da rileggere prima della pubblicazione oppure da riservare alle bozze.

### Tradurre tramite OpenRouter (`--use_openrouter`)

OpenRouter è un **router** davanti a più di 400 modelli ospitati da terze parti,
fatturati in base all'uso su un unico credito. Con una sola chiave permette di accedere a modelli
che nessun altro provider offre, in particolare ai modelli open cinesi.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Due particolarità del routing hanno determinato l'implementazione, ed entrambe sono
misurabili:

- **Lo stesso modello viene offerto da decine di host con limiti
  differenti.** Su `z-ai/glm-5.3-flash`, 23 host, uno dei quali limitato a
  2.048 token di output: senza precauzioni, una traduzione lunga su 23 veniva
  troncata, casualmente in base al routing e senza il minimo segnale. Un preflight legge
  `/api/v1/models/{modèle}/endpoints`, esclude gli host con meno di 8.000 token
  di output o con stato degradato, quindi vincola gli altri con
  `allow_fallbacks: false` — altrimenti il router torna a un host
  escluso.
- **Il ragionamento viene fatturato alla tariffa dell'output.** Stessa richiesta su
  `z-ai/glm-5.2`, risposta «OK»: 107 token di completamento con l'impostazione predefinita del modello,
  2 con il ragionamento disattivato. Viene quindi disattivato per impostazione predefinita sui modelli
  che lo consentono. Quelli che lo impongono — `reasoning.mandatory`, 288 dei 431
  modelli del catalogo — ricevono il **livello di effort più basso che dichiarano
  di accettare**, non la loro impostazione predefinita: quello di `z-ai/glm-5.3-flash` è
  `max` e saturava i 32.768 token di output prima della fine della
  traduzione. Aumentare il budget non avrebbe cambiato nulla, poiché l'effort ne assegna una
  percentuale. `--reasoning_effort` rimane prioritario e `none` su un modello
  che impone il ragionamento viene segnalato anziché aggirato.

Il preflight è **fail-closed** e mostra ciò che ha selezionato:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Uno slug assente dal catalogo, un catalogo irraggiungibile o l'assenza di host
che rispettino il limite interrompono il comando prima di qualsiasi addebito.

Altri punti:

- La finestra di contesto proviene dal catalogo, non da una costante: la
  segmentazione si adatta realmente, anche per i modelli da 4.095 token.
- `--eco` non ha effetto (il modello è quello di `--model`).
- `finish_reason=length` con un output vuoto non indica un troncamento, ma un
  budget consumato dal ragionamento; il messaggio lo specifica, perché i due
  casi richiedono interventi opposti.
- Variabili d'ambiente: `OPENROUTER_API_KEY` (chiave, su
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (valore predefinito
  `https://openrouter.ai/api/v1`, `https://` obbligatorio), `OPENROUTER_TIMEOUT`
  (secondi per chiamata, valore predefinito `900`) e `OPENROUTER_PREFLIGHT_TIMEOUT`
  (valore predefinito `30`).

### Modalità economica

Utilizza modelli più veloci e meno costosi (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opzioni

| Opzione                   | Descrizione                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Singolo file Markdown da tradurre                                                                             |
| `--source_dir`           | Directory sorgente contenente i file Markdown                                                                 |
| `--target_dir`           | Directory di output per i file tradotti                                                                       |
| `--source_lang`          | Lingua sorgente (valore predefinito: `fr`)                                                         |
| `--target_lang`          | Lingua di destinazione (valore predefinito: `en`)                                                  |
| `--model`                | Modello specifico da utilizzare                                                                               |
| `--eco`                  | Utilizzare i modelli economici                                                                                |
| `--use_mistral`          | Utilizzare l'API Mistral AI                                                                                   |
| `--use_claude`           | Utilizzare l'API Claude                                                                                       |
| `--use_gemini`           | Utilizzare l'API Gemini                                                                                       |
| `--use_codex`            | Utilizzare la CLI Codex sulla quota dell'abbonamento ChatGPT                                                  |
| `--use_grok`             | Utilizzare l'API xAI (Grok) — richiede `XAI_API_KEY`                                                        |
| `--use_openrouter`       | Utilizzare OpenRouter — richiede `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                                               |
| `--use_grok_cli`         | Utilizzare la CLI Grok sulla quota dell'abbonamento Grok                                                      |
| `--use_opencode`         | Utilizzare OpenCode (open source) verso il provider configurato in OpenCode; richiede `--model provider/modèle` |
| `--force`                | Forzare la ritraduzione                                                                                       |
| `--keep_filename`        | Conservare il nome file originale                                                                             |
| `--news`                 | Modalità notizie: protegge le citazioni EN, gestisce le bandiere per lingua                                   |
| `--add_translation_note` | Aggiungere una nota di traduzione                                                                              |
| `--note_position`        | Posizione della nota: `top`, `bottom` (valore predefinito) oppure `both`            |
| `--note_format`          | Formato della nota: `legacy` (valore predefinito, paragrafo in grassetto) oppure `marker`       |
| `--include_model`        | Includere il nome del modello nel file di output                                                              |
| `--reasoning_effort`     | Effort di ragionamento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **I sette flag dei provider si escludono a vicenda.** In precedenza, combinarne due
> veniva accettato silenziosamente e la scelta ricadeva sul primo verificato: una
> traduzione richiesta sulla quota dell'abbonamento (`--use_codex`, `--use_grok_cli`)
> poteva quindi essere fatturata in base all'uso senza alcun avvertimento.
> `argparse` ora rifiuta la combinazione.

### Nota di traduzione: posizioni e formati

Con `--add_translation_note`, il translator può collocare la nota in alto, in basso o in entrambe le posizioni e renderla in formato testo semplice (retrocompatibile) oppure in formato `marker` utilizzabile da un plugin Markdown.

**Posizione** (`--note_position`):

- `bottom` (valore predefinito): nota alla fine del file, come in precedenza.
- `top`: nota inserita **dopo il frontmatter YAML** (compatibilità con Astro Content Collections, gray-matter, ecc.).
- `both`: nota inserita sia in alto SIA in basso (una sola chiamata LLM, contenuto riutilizzato per entrambe le posizioni).

**Formato** (`--note_format`):

- `legacy` (valore predefinito): paragrafo in grassetto `**...**` — comportamento rigorosamente identico alla v1.8, byte per byte. Compatibile con Hugo, GitHub, GitLab e qualsiasi renderer Markdown.
- `marker`: definizione di riferimento Markdown invisibile (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguita da un blockquote in grassetto. Leggibile nativamente su GitHub/GitLab e utilizzabile durante la build da un plugin remark lato Astro per generare un banner stilizzato (vedere il blog jls42.org).

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

| Provider   | Qualità (valore predefinito)             | Economico (`--eco`) |
| ---------- | ---------------------------------------- | --------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`             |
| Claude     | `claude-sonnet-5`                          | `claude-haiku-4-5`             |
| Mistral    | `mistral-large-latest`                          | `mistral-small-latest`             |
| Gemini     | `gemini-3.7-flash`                          | `gemini-3.1-flash-lite`             |
| Codex      | `gpt-5.6-sol`                          | `gpt-5.6-luna`             |
| Grok API   | `grok-4.6`                          | `grok-4.3`             |
| Grok CLI   | `grok-4.6`                          | `grok-4.5`             |
| OpenCode   | `--model provider/modèle` obbligatorio             | uguale — `--eco` non ha effetto |
| OpenRouter | `--model fournisseur/modèle` obbligatorio             | uguale — `--eco` non ha effetto |
## Quali modelli sono all'altezza

Un modello che traduce bene un paragrafo non preserva necessariamente la struttura
di un intero documento. Queste misurazioni provengono da **traduzioni realmente
eseguite**, con il comando mostrato più sopra, su tre raccolte di
documenti e quattordici lingue di destinazione: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Due colonne, e non indicano la stessa cosa. **Scritte** conta le
traduzioni che vanno a buon fine: i controlli contro gli errori silenziosi dello script
lasciano passare il file. **Senza discrepanze** conta quelle la cui struttura è
identica alla fonte: stesse sezioni, stessi link, stessi URL, stessi blocchi e
codici inline, stesse tabelle, stesse citazioni, stessi flag.

### Articolo di blog denso, modalità `--news`

589 righe, 140 link, 21 sezioni, 3 citazioni inglesi protette. È il
documento più impegnativo dei tre: la modalità `--news` aggiunge vincoli relativi a
flag e citazioni oltre alla struttura Markdown.

| Modello                            | Accesso              | Scritte | Senza discrepanze | Mediana/lingua |
| --------------------------------- | ------------------ | ------- | ---------- | -------------- |
| `gemini-3.7-flash`                | API Google         | 14/14   | **14/14**  | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | abbonamento ChatGPT | 14/14   | **14/14**  | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | **14/14**  | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | 13/14      | 26 min 23 s    |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14   | 12/14      | 15 min 49 s    |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9     | 7/9        | 20 min 33 s    |
| `claude-sonnet-5`                 | API Anthropic      | 14/14   | 11/14      | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | 11/14      | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | 7/14       | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | locale              | 10/14   | 7/14       | 12 min 39 s    |
| `mistral-large-latest`            | API Mistral        | 11/14   | 5/14       | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | 3/14       | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | abbonamento Grok    | 1/14    | 1/14       | 23 min 11 s    |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4     | 1/4        | 23 min 00 s    |

Due lotti sono stati **interrotti per esaurimento del credito**, come indicano i rispettivi denominatori:
`qwen3.5-27b` si è fermato a nove lingue, `kimi-k2.6` a quattro — quest'ultimo
dopo un timeout di quaranta minuti e due rifiuti, a quasi
0,33 $ per lingua.

Una precisazione metodologica sulle righe OpenRouter: sono state misurate con
le impostazioni **predefinite del router**, prima che `--use_openrouter` esistesse.
`z-ai/glm-5.2` è stato nuovamente misurato in seguito con il provider incluso, reasoning disattivato,
e restituisce esattamente lo stesso 14/14. `z-ai/glm-5.3-flash` ha fallito due volte per
esaurimento del budget di output con le impostazioni predefinite del router; ora il provider richiede a
questi modelli il livello di effort più basso che accettano, e la controprova sulle
lingue problematiche va a buon fine.

### README di questo progetto, Markdown standard

508 righe, 219 codici inline, 40 delimitatori di blocchi, 45 righe di tabella. Nessuna
modalità `--news` qui: la difficoltà deriva dalla densità del codice.

| Modello                        | Scritte | Senza discrepanze | Mediana/lingua |
| ----------------------------- | ------- | ---------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14      | 1 min 22 s     |
| `gemini-3.7-flash`            | 14/14   | 13/14      | 21 s           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14      | 2 min 04 s     |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14       | 3 min 25 s     |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14       | 3 min 38 s     |

### Quattro README di progetti noti

FastAPI, Ollama, tldr-pages e Vue.js, presi così come sono da GitHub. Questi documenti
sono **più facili** dei due precedenti, e la tabella lo mostra.

| Modello                    | Ambito                  | Scritte | Senza discrepanze |
| ------------------------- | -------------------------- | ------- | ---------- |
| `opencode/mimo-v2.5-free` | 4 progetti × 14 lingue     | 55/56   | 47/56      |
| `grok-4.6` (abbonamento)   | 4 progetti × ar, hi, ja, zh | 16/16   | 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 progetti × ar, hi, ja, zh | 15/16   | 9/16       |

### Cosa ne ricaviamo

- **Tre modelli non hanno mai perso informazioni** nei due documenti
  densi: `gemini-3.7-flash`, `gpt-5.6-sol` tramite l'abbonamento ChatGPT e
  `z-ai/glm-5.2` tramite OpenRouter. Le loro uniche discrepanze in modalità standard sono una
  coppia di `**` non riportata in una o due lingue, mai un URL, un blocco
  di codice o una citazione.
- **Il fattore discriminante è la densità del documento, non la modalità `--news`.**
  Grok tramite abbonamento fallisce 13 volte su 14 sull'articolo di blog e completa correttamente 14
  README pubblici su 16: la causa dell'errore è una perdita di coerenza su un segmento lungo,
  verificata mediante controprova — il passaggio isolato viene tradotto correttamente.
- **Le scritture non latine non costituiscono la discriminante attesa.** `gpt-oss` lascia
  passaggi in francese in arabo, giapponese, polacco **e rumeno**; Mistral
  e MiMo perdono codici inline soltanto nelle scritture non latine.
- **Disattivare il reasoning non riduce affatto la qualità.** `z-ai/glm-5.2` completa
  quattordici lingue senza una sola discrepanza in entrambe le condizioni — reasoning attivo
  per impostazione predefinita del router, poi disattivato da `--use_openrouter` — con un numero di
  token di output fatturati diciotto volte inferiore. È la misurazione che giustifica l'impostazione
  predefinita del provider.
- **Un modello lento non è un modello affidabile.** `deepseek-v4-flash-0731` impiega 37
  minuti per lingua per 4 traduzioni su 14, `qwen3.8-flash` 26 minuti per
  un risultato quasi perfetto e Gemini 1 minuto e 18 secondi per un risultato impeccabile.

### Cosa non è questa tabella

- **Non è una classifica esaustiva.** OpenRouter da solo propone più
  di quattrocento modelli; qui ne sono stati misurati circa quindici. L'assenza di un
  modello non dice nulla sulla sua qualità, ma soltanto che non è stato provato.
- **Queste misurazioni hanno una data**: 4 e 5 settembre 2026. I modelli cambiano
  mantenendo lo stesso nome, i provider modificano quantizzazioni e limiti, e
  ogni settimana vengono pubblicati nuovi modelli.
- **Le durate non costituiscono una classifica.** Il parallelismo variava da 3 a 6 traduzioni
  simultanee a seconda delle campagne, e il throughput di un provider cambia nel corso della
  giornata. Forniscono un ordine di grandezza, non un confronto.
- **Un risultato dipende dal documento quanto dal modello.** Lo stesso modello
  completa correttamente quattordici lingue su un articolo e nove su questo README. I vostri file non
  sono i nostri.
- **L'approccio corretto resta misurare nel proprio ambiente**: traducete uno dei vostri
  documenti nelle lingue di destinazione, quindi confrontate la struttura — numero di
  sezioni, link, URL distinti, blocchi di codice, codici inline e
  righe di tabella. È esattamente ciò che fa il protocollo precedente, e
  richiede un solo ciclo su `aipmt`.

## Progetti che utilizzano questo script

- **[jls42.org](https://jls42.org)** - Blog personale multilingue (15 lingue)

## Autore

Julien LE SAUX
Email: contact@jls42.org

## Licenza

GNU GENERAL PUBLIC LICENSE Version 3. Consultare [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articolo tradotto dal fr all'it con gpt-5.6-sol.**
