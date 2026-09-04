# Traducător de Markdown bazat pe AI

🌍 [Franceză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engleză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spaniolă](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chineză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Germană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japoneză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreeană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabă](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandeză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Poloneză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugheză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Suedeză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Calitatea codului</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Starea pragului de calitate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Evaluarea securității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Evaluarea fiabilității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Evaluarea mentenabilității"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Acoperire"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilități"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Erori"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Probleme de calitate a codului"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Linii duplicate (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Datorie tehnică"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linii de cod"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Insignă Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traducător de fișiere Markdown care utilizează **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** și **Grok (xAI)** — prin API, folosind cota unui abonament ChatGPT (Codex) sau Grok fără facturare în funcție de utilizare ori prin **OpenCode**, agentul open source, către furnizorul ales: model local (Ollama), gratuit, abonament (GitHub Copilot…) sau cheie.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă, păstrând formatarea, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Furnizori multipli**: 5 API-uri (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI-uri pe bază de abonament, fără facturare în funcție de utilizare — Codex (ChatGPT) și Grok — + OpenCode (open source, MIT) către orice furnizor configurat în OpenCode, inclusiv un model local
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Mod economic**: Opțiunea `--eco` pentru utilizarea unor modele mai rapide și mai ieftine
- **Fișier unic**: Opțiunea `--file` pentru traducerea unui singur fișier
- **Segmentare inteligentă**: Gestionarea textelor lungi cu limite de tokenuri pentru fiecare model
- **Păstrarea codului**: Blocurile de cod ȘI codul inline (`` `...` ``) sunt păstrate
- **Numele fișierului**: Opțiunea `--keep_filename` pentru păstrarea numelui original
- **Mod News**: Opțiunea `--news` pentru protejarea citatelor în engleză și gestionarea steagurilor în articolele de actualitate
- **Configurare .env**: Suport pentru fișierul `.env` destinat cheilor API
- **Notă de traducere**: Adăugarea opțională a unei note la sfârșitul documentului

## Instalare

### Pentru utilizarea instrumentului

```bash
pip install ai-powered-markdown-translator
```

Comanda `aipmt` este apoi disponibilă de oriunde. Dacă directorul scripturilor
Python nu se află în `PATH`, `python -m aipmt` face exact același
lucru. Este necesar Python 3.10 sau o versiune mai recentă.

Pentru o instalare izolată de restul pachetelor:

```bash
pipx install ai-powered-markdown-translator
```

### Pentru a contribui la proiect

Depozitul clonat rămâne necesar pentru dezvoltare: acolo se află testele,
cele 28 de traduceri și toate instrumentele de calitate.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` este un **fișier lock cu versiuni fixate integral**, reprezentând fidel
mediul testat. Limitele publicate în `pyproject.toml` sunt
intenționat mai largi: acestea nu impun nimic celorlalte pachete.

### Instrumente de calitate (opționale, dar recomandate)

Proiectul utilizează [`pre-commit`](https://pre-commit.com) pentru a împiedica efectuarea de commit-uri cu cod formatat incorect, vulnerabil sau care conține un secret. Instalare:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook-uri active: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexitate), detect-secrets (chei API), mypy (tipare progresivă), Opengrep (SAST), pip-audit (CVE ale dependențelor), unittest. Consultați secțiunea _Calitate / pre-commit_ din `CLAUDE.md` pentru detalii.

## Configurare

Cheile sunt căutate în **trei locuri**, în ordinea descrescătoare a priorității.
Fiecare completează doar ceea ce precedentul a lăsat necompletat.

|     | Unde                                            | Pentru ce                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabile de mediu                     | CI, containere, derogare punctuală |
| 2   | `.env` din directorul curent (sau dintr-un director părinte) | o cheie specifică unui proiect            |
| 3   | `~/.config/aipmt/.env`                        | **instalat o singură dată, valabil peste tot**   |

Cea mai simplă variantă după un `pip install` este a treia:

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

Acest fișier urmează `XDG_CONFIG_HOME` atunci când variabila indică o cale absolută
(în caz contrar, este ignorată, conform specificației) și `%APPDATA%`
în Windows.

A doua variantă rămâne utilă atunci când un depozit are propria cheie: un fișier `.env` la rădăcina sa
are atunci prioritate față de configurația utilizatorului, fără a o modifica. Iar o
variabilă deja definită în mediu are prioritate față de ambele:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Dacă nu este găsită nicio cheie, comanda nu afișează o urmă a apelului: aceasta
enumeră cele trei locații împreună cu calea lor exactă.

`GEMINI_API_KEY` este acceptată ca alternativă la `GOOGLE_API_KEY` (convenția AI
Studio). Variabile opționale: `XAI_BASE_URL` (endpoint xAI, implicit
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secunde per apel Anthropic, implicit
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consultați secțiunea Grok CLI) și `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consultați secțiunea OpenCode). Pentru
`regen_translations.sh`: `REGEN_PROVIDER` (implicit `codex`, pe bază de abonament),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (derogare obligatorie pentru un API
facturat) și `REGEN_JOB_TIMEOUT` (limită per job, implicit 600 s, 1.800 s în Codex).

## Utilizare

### Traducerea unui singur fișier

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducerea unui director

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

### Traducerea folosind abonamentul ChatGPT (`--use_codex`)

Acest furnizor nu utilizează nicio cheie API: controlează CLI-ul oficial Codex în mod
neinteractiv, astfel încât traducerea este dedusă din cota abonamentului
ChatGPT (Plus, Pro, Business…) deja plătit. Aceasta este singura metodă documentată de
OpenAI pentru această utilizare — tokenurile din `~/.codex/auth.json` nu autentifică
apelurile către API Platform și, de altfel, nu sunt niciodată citite de acest script.

**Cerințe preliminare:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Fișierul binar este căutat în această ordine: variabila `CODEX_BIN`, `PATH`,
apoi pachetul Python `openai-codex-cli-bin`. Acesta din urmă nu este inclus în mod intenționat
în `requirements.txt`: ocupă aproximativ 250 Mo, ceea ce ar fi impus tuturor
utilizatorilor pentru un furnizor opțional.

**De reținut:**

- **Nu este utilizată nicio cheie API.** `OPENAI_API_KEY` și `CODEX_API_KEY` sunt
  eliminate din mediul subprocesului, ceea ce garantează că o cheie
  prezentă în `.env` nu va trece niciodată traducerea la facturarea în funcție de
  utilizare.
- **Un segment = un „mesaj local”** din fereastra de 5 ore a planului.
  Utilizați `--eco` (modelul `gpt-5.6-luna`, 250–2.000 de mesaje/5 h în Plus)
  în locul modelului de calitate (`gpt-5.6-sol`, 10–100 de mesaje/5 h).
- **Mai lent** decât un apel API: aproximativ 45 s pentru un README complet, față de
  câteva secunde în mod direct.
- **Refuzat în CI** (dacă `CI` sau `GITHUB_ACTIONS` este definită): autentificarea prin
  abonament nu este concepută pentru un runner partajat, iar OpenAI descurajează acest
  flux de lucru în depozitele publice. Utilizați o cheie API în această situație.
- Variabile de mediu: `CODEX_BIN` (calea explicită a fișierului binar) și
  `CODEX_TIMEOUT` (secunde per segment, implicit `600`).

### Traducerea folosind abonamentul Grok (`--use_grok_cli`)

Același principiu ca pentru `--use_codex`, cu CLI-ul oficial **Grok Build**:
traducerea este dedusă din abonamentul Grok (SuperGrok / X Premium+), în loc
să fie facturată per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolare — de citit înainte de utilizare.** Acest furnizor este, prin construcție, **mai
slab** decât `--use_codex`, iar acest lucru este asumat:

- Codex rulează în `--sandbox read-only`, o limită impusă de sistem.
- Sandbox-ul Grok **nu poate fi aplicat** pe multe sisteme Linux
  recente: AppArmor blochează user namespaces neprivilegiate începând cu Ubuntu
  24.04, iar lista de interdicții pentru socket-urile runtime-ului containerului eșuează dacă
  `/run/podman` se află în `0700`. Or, un profil **integrat** care nu poate fi
  aplicat pornește **fără izolare, în tăcere**.
- Prin urmare, scriptul nu solicită implicit niciun profil și **nu recurge niciodată
  în tăcere la o variantă de rezervă**: afișează un avertisment. Izolarea se bazează pe
  regulile `--deny` ale CLI-ului (inclusiv regula generală `*`), singurul strat măsurat
  _fail-closed_ — o regulă necunoscută determină refuzul pornirii, în loc să
  elimine protecția fără avertisment.
- Pentru a **impune** sandbox-ul sistemului de operare: `GROK_TRANSLATE_SANDBOX=read-only`.
  Pornirea va eșua dacă sistemul nu îl poate respecta, acesta fiind
  comportamentul dorit.

**Cotă**: fondul Grok este **săptămânal și partajat** cu Chat, Imagine și
Voice, iar nicio comandă nu permite consultarea acestuia. Prin urmare, o procesare în lot poate
consuma din utilizarea conversațională fără nicio notificare — de aici
limitarea concurenței la 2 și avertismentul din `regen_translations.sh`.

Alte variabile: `GROK_BIN` (calea fișierului binar), `GROK_TIMEOUT` (implicit 900 s).

Pentru regenerarea celor 28 de traduceri:

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

### Traducerea cu OpenCode, către furnizorul ales (`--use_opencode`)

[OpenCode](https://opencode.ai) este un agent de programare **open source (MIT)** pentru
terminal. Nu este un furnizor de modele, ci un **router** către cele
configurate chiar în OpenCode: o cheie API, un abonament
(GitHub Copilot, ChatGPT, SuperGrok), gateway-ul OpenCode Zen — care oferă
modele gratuite **fără cont** — sau un model **local** (Ollama, LM Studio,
llama.cpp). Acest furnizor controlează `opencode run` în mod neinteractiv și limitează
apelul la un singur schimb, fără niciun instrument.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` este **obligatoriu**, în formatul `provider/modèle`. OpenCode nu este
un furnizor și nicio valoare implicită nu este aleasă în locul dumneavoastră: mecanismul său propriu de rezervă
ar fi un model gratuit ale cărui conversații pot fi folosite pentru antrenare.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Izolare — ce face scriptul la fiecare apel:**

- O configurație inline (`OPENCODE_CONFIG_CONTENT`), cu prioritate față de
  configurația dumneavoastră, definește un agent `aipmt` pentru care **toate instrumentele sunt refuzate**
  (`permission: { "*": "deny" }`): modelul nu poate nici să citească, nici să scrie, nici să
  execute comenzi — conform măsurătorilor, nici măcar nu încearcă. Partajarea sesiunii
  este dezactivată, `--pure` elimină pluginurile externe, niciodată `--auto`.
- Apelul rulează într-un **director temporar și gol**, cu opțiunile
  `OPENCODE_DISABLE_PROJECT_CONFIG` și `OPENCODE_DISABLE_CLAUDE_CODE`: fără
  acestea, OpenCode injectează în fiecare prompt fișierul `AGENTS.md` din directorul curent
  și fișierul dumneavoastră `~/.claude/CLAUDE.md` — conform măsurătorilor, o instrucțiune „încheie fiecare răspuns
  cu BANANA” plasată într-un `AGENTS.md` era aplicată traducerii. În schimb, regulile
  globale din `~/.config/opencode/AGENTS.md` rămân
  aplicate: OpenCode nu permite excluderea lor.
- Contractul de ieșire impune simultan: cod de retur 0, niciun eveniment
  `error`, niciun apel de instrument, un ultim pas încheiat cu `stop`, un text care nu este
  gol și agentul încărcat efectiv — un `--agent` necunoscut nu determină
  eșuarea OpenCode, ci acesta **revine în tăcere** la agentul de programare, cu instrumentele
  active. Nici un `exit 0` nu dovedește nimic în acest caz.
- **Nicio cheie aipmt nu este transmisă** subprocesului (aceeași filtrare
  ca în cazul Codex și Grok), cu o singură excepție nominală: `OPENCODE_API_KEY`,
  cheia OpenCode însuși (Zen, Go). Furnizorii se configurează în
  OpenCode (`opencode auth login`, `opencode.json`), nu în fișierul `.env` al aipmt.

**De reținut:**

- **Modelele gratuite Zen sunt modele „stealth” sau furnizate de contributori**,
  schimbătoare, cu limite nedocumentate, iar conversațiile lor pot fi utilizate pentru
  antrenare: perfecte pentru documentație publică, dar de evitat pentru
  conținut privat. Conform măsurătorilor: `opencode/mimo-v2.5-free` traduce acest README dintr-o
  singură trecere; `opencode/big-pickle` este mai lent, iar două solicitări simultane au
  rămas fără răspuns.
- **Un model local trebuie să ofere cel puțin 16 k de context** — segmentele au
  până la 16.000 de caractere — în timp ce Ollama configurează adesea implicit 4.096.
  Cu Ollama: un `Modelfile` cu `PARAMETER num_ctx 32768`, apoi
  `ollama create`. Calitatea depinde de model: un model 7B a inversat o listă și
  a deteriorat delimitatorul unui bloc de cod într-un fișier de test, în timp ce un model al
  gateway-ului a păstrat totul.
- `--eco` nu are efect (modelul este cel din `--model`);
  `--reasoning_effort` este transmis ca atare drept `--variant` al OpenCode și trebuie
  solicitat numai dacă modelul îl recunoaște.
- Sesiunile sunt înregistrate de OpenCode în baza sa de date
  (`~/.local/share/opencode/`), ca orice sesiune OpenCode.
- Variabile de mediu: `OPENCODE_BIN` (calea explicită a fișierului binar,
  în caz contrar `PATH`, apoi `~/.opencode/bin/opencode`) și `OPENCODE_TIMEOUT`
  (secunde per segment, implicit `600`). `OPENCODE_CONFIG` este respectată dacă o
  exportați.

**Exemplu măsurat: un model local prin Ollama** (RTX 3060 12 Go, 62 Go RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

Apoi furnizorul în `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` nu este un detaliu: Ollama activează implicit raționamentul pentru
Gemma 4 și Qwen 3.5, iar un Modelfile nu îl poate dezactiva. Conform măsurătorilor prin
OpenCode: fără opțiune, „Pisica doarme pe covor” consumă 919 tokenuri
de raționament și 68 s; cu opțiunea, 9 tokenuri.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Rezultate pentru un articol de blog real de 589 de linii (140 de linkuri, 21 de secțiuni,
3 citate în engleză protejate prin modul `--news`), aceeași comandă, trei
modele:

| Model                                   | Durată       | Structură                                                  | Abateri                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuit) | 4 min 26 s  | identică sursei                                      | niciuna                                                                                     |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s | linkuri, URL-uri, tabele, taguri, text îngroșat și cod inline identice | un rând de citat inventat (🇺🇸 + parafrazare), o atribuire duplicată               |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s  | linkuri, URL-uri, tabele și taguri identice                    | un rând de citat inventat, câteva fragmente de text îngroșat și coduri inline adăugate, un segment procesat din nou |

În timpul traducerii locale: GPU la 98% și 170 W, 10 Go de VRAM ocupați
(modelul și cache-ul de 32 k tokenuri, nimic transferat în RAM), 7,5 Go RAM pentru
serverul Ollama. Un model cu 9–12 miliarde de parametri respectă
structura, dar își permite câte o abatere per articol, în timp ce modelul gateway-ului
nu și-a permis niciuna: trebuie recitit înainte de publicare sau rezervat pentru schițe.

### Mod economic

Utilizează modele mai rapide și mai ieftine (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opțiuni

| Opțiune                   | Descriere                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Fișier Markdown unic de tradus                                                                            |
| `--source_dir`           | Director sursă care conține fișierele Markdown                                                             |
| `--target_dir`           | Director de ieșire pentru fișierele traduse                                                               |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                                                                  |
| `--target_lang`          | Limba țintă (implicit: `en`)                                                                                   |
| `--model`                | Model specific de utilizat                                                                                  |
| `--eco`                  | Utilizează modelele economice                                                                              |
| `--use_mistral`          | Utilizează API-ul Mistral AI                                                                                     |
| `--use_claude`           | Utilizează API-ul Claude                                                                                         |
| `--use_gemini`           | Utilizează API-ul Gemini                                                                                         |
| `--use_codex`            | Utilizează CLI-ul Codex din cota abonamentului ChatGPT                                                    |
| `--use_grok`             | Utilizează API-ul xAI (Grok) — necesită `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Utilizează CLI-ul Grok din cota abonamentului Grok                                                        |
| `--use_opencode`         | Utilizează OpenCode (open source) cu furnizorul configurat în OpenCode; necesită `--model provider/modèle` |
| `--force`                | Forțează retraducerea                                                                                       |
| `--keep_filename`        | Păstrează numele original al fișierului                                                                          |
| `--news`                 | Modul știri: protejează citatele în EN, gestionează steagurile în funcție de limbă                                      |
| `--add_translation_note` | Adaugă o notă de traducere                                                                                |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                                                     |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf aldin) sau `marker`                                            |
| `--include_model`        | Include numele modelului în fișierul de ieșire                                                            |
| `--reasoning_effort`     | Nivelul efortului de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **Cele șapte flag-uri de provider se exclud reciproc.** Combinarea a două
> era anterior acceptată în tăcere și se rezolva la primul verificat: o
> traducere solicitată din cota abonamentului (`--use_codex`, `--use_grok_cli`)
> putea astfel ajunge să fie facturată în funcție de utilizare fără niciun avertisment.
> `argparse` refuză acum combinația.

### Notă de traducere: poziții și formate

Cu `--add_translation_note`, translator-ul poate plasa nota sus, jos sau în ambele locuri și o poate reda fie în format text simplu (retrocompatibil), fie în format `marker`, utilizabil de un plugin Markdown.

**Poziție** (`--note_position`):

- `bottom` (implicit): nota la sfârșitul fișierului, ca și până acum.
- `top`: nota inserată **după frontmatter-ul YAML** (compatibilitate sigură cu Astro Content Collections, gray-matter etc.).
- `both`: nota inserată sus ȘI jos (un singur apel LLM, conținut reutilizat pentru ambele amplasări).

**Format** (`--note_format`):

- `legacy` (implicit): paragraf aldin `**...**` — comportament strict identic cu v1.8, byte-for-byte. Compatibil cu Hugo, GitHub, GitLab și orice renderer Markdown.
- `marker`: definiție invizibilă a unei referințe de link Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), urmată de un blockquote aldin. Lizibilă nativ pe GitHub/GitLab și utilizabilă la build de un plugin remark în Astro pentru a produce un banner stilizat (consultați blogul jls42.org).

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

### Modele implicite (2026)

| Provider | Calitate (implicit)                      | Economic (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obligatoriu | la fel — `--eco` fără efect |

> **Recomandare pentru traduceri long-form**: `--use_gemini` (implicit = `gemini-3.7-flash`) păstrează fidel structura Markdown pentru scrierile non-latine (PL, JA, ZH, AR, HI), inclusiv în modul `--news`, unde fidelitatea placeholder-elor contează. Măsurat pe acest README tradus în japoneză: structură identică cu `gemini-3.1-pro-preview` (21 de liste, 18 blocuri de cod, 13 linkuri HTML, 13 imagini, toate URL-urile păstrate), cu o latență de aproximativ 6 ori mai mică. OpenAI rămâne opțiunea implicită pentru retrocompatibilitate.

## Proiecte care utilizează acest script

- **[jls42.org](https://jls42.org)** - Blog personal multilingv (15 limbi)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articol tradus din fr în ro cu gpt-5.6-sol.**
