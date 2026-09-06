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

Traducător de fișiere Markdown care utilizează **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** și **Grok (xAI)** — prin API, din cota unui abonament ChatGPT (Codex) sau Grok, fără facturare în funcție de utilizare, ori prin **OpenCode**, agentul open source, către furnizorul ales: model local (Ollama), gratuit, abonament (GitHub Copilot…) sau cheie.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă, păstrând formatarea, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Furnizori multipli**: 5 API-uri (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI-uri pe bază de abonament, fără facturare în funcție de utilizare — Codex (ChatGPT) și Grok — + OpenCode (open source, MIT) către orice furnizor configurat în OpenCode, inclusiv un model local
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Mod economic**: Opțiunea `--eco` pentru utilizarea unor modele mai rapide și mai puțin costisitoare
- **Fișier unic**: Opțiunea `--file` pentru traducerea unui singur fișier
- **Segmentare inteligentă**: Gestionarea textelor lungi cu limite de tokenuri pentru fiecare model
- **Păstrarea codului**: Blocurile de cod ȘI codul inline (`` `...` ``) sunt păstrate
- **Numele fișierului**: Opțiunea `--keep_filename` pentru păstrarea numelui original
- **Mod News**: Opțiunea `--news` pentru protejarea citatelor în limba engleză și gestionarea steagurilor în articolele de știri
- **Configurare .env**: Compatibilitate cu fișierul `.env` pentru cheile API
- **Notă de traducere**: Adăugarea opțională a unei note la sfârșitul documentului

## Instalare

### Pentru utilizarea instrumentului

```bash
pip install ai-powered-markdown-translator
```

Comanda `aipmt` este apoi disponibilă de oriunde. Dacă directorul de scripturi
Python nu se află în `PATH`, `python -m aipmt` face exact același
lucru. Este necesar Python 3.10 sau o versiune mai recentă.

Pentru o instalare izolată de restul pachetelor:

```bash
pipx install ai-powered-markdown-translator
```

### Pentru a contribui la proiect

Depozitul clonat rămâne necesar pentru dezvoltare: acolo se află testele,
cele 28 de traduceri și toate instrumentele de asigurare a calității.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` este un **lock fixat complet**, care reflectă exact
mediul testat. Limitele publicate în `pyproject.toml` sunt
intenționat mai largi: acestea nu impun nimic celorlalte pachete.

### Instrumente de calitate (opționale, dar recomandate)

Proiectul utilizează [`pre-commit`](https://pre-commit.com) pentru a împiedica trimiterea de cod formatat incorect, vulnerabil sau care conține un secret. Instalare:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook-uri active: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexitate), detect-secrets (chei API), mypy (tipizare progresivă), Opengrep (SAST), pip-audit (CVE-uri ale dependențelor), unittest. Consultați secțiunea _Quality / pre-commit_ din `CLAUDE.md` pentru detalii.

## Configurare

Cheile sunt căutate în **trei locuri**, de la prioritatea cea mai mare la cea mai mică.
Fiecare completează doar ceea ce precedentul lasă necompletat.

|     | Unde                                          | Pentru ce                                 |
| --- | --------------------------------------------- | ----------------------------------------- |
| 1   | Variabile de mediu                            | CI, containere, suprascriere punctuală    |
| 2   | `.env` din directorul curent (sau dintr-un director părinte) | o cheie specifică unui proiect            |
| 3   | `~/.config/aipmt/.env`                        | **instalat o singură dată, valabil peste tot** |

Cea mai simplă opțiune după un `pip install` este a treia:

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

Acest fișier urmează `XDG_CONFIG_HOME` atunci când variabila indică o cale absolută
(în caz contrar, aceasta este ignorată, conform specificației), și `%APPDATA%`
în Windows.

A doua opțiune rămâne utilă atunci când un depozit are propria cheie: un `.env` la rădăcina sa
are atunci prioritate față de configurația utilizatorului, fără să o modifice. Iar o
variabilă deja definită în mediu are prioritate față de ambele:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Dacă nu este găsită nicio cheie, comanda nu afișează un traceback: aceasta
enumeră cele trei locații împreună cu calea lor exactă.

`GEMINI_API_KEY` este acceptată ca alternativă la `GOOGLE_API_KEY` (convenția AI
Studio). Variabile opționale: `XAI_BASE_URL` (endpoint xAI, implicit
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secunde per apel Anthropic, implicit
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consultați secțiunea Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consultați secțiunea OpenCode) și `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (consultați secțiunea
OpenRouter). Pentru
`regen_translations.sh`: `REGEN_PROVIDER` (implicit `codex`, pe bază de abonament),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (suprascriere obligatorie pentru un API
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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Traducerea folosind abonamentul ChatGPT (`--use_codex`)

Acest furnizor nu utilizează nicio cheie API: controlează CLI-ul oficial Codex în mod
neinteractiv, astfel încât traducerea este dedusă din cota abonamentului
ChatGPT deja plătit (Plus, Pro, Business…). Aceasta este singura modalitate documentată de
OpenAI pentru această utilizare — tokenurile din `~/.codex/auth.json` nu autentifică
apelurile către API Platform și, de altfel, nu sunt citite niciodată de acest script.

**Cerințe preliminare:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Executabilul este căutat în această ordine: variabila `CODEX_BIN`, `PATH`,
apoi pachetul Python `openai-codex-cli-bin`. Acesta din urmă nu este inclus în mod intenționat
în `requirements.txt`: ocupă aproximativ 250 MB, ceea ce ar fi impus tuturor
utilizatorilor pentru un furnizor opțional.

**De știut:**

- **Nu este utilizată nicio cheie API.** `OPENAI_API_KEY` și `CODEX_API_KEY` sunt
  eliminate din mediul subprocesului, ceea ce garantează că o cheie
  prezentă în `.env` nu va face niciodată ca traducerea să treacă la facturarea în funcție de
  utilizare.
- **Un segment = un „mesaj local”** din fereastra de 5 ore a planului.
  Utilizați `--eco` (modelul `gpt-5.6-luna`, 250-2.000 de mesaje/5 h în Plus)
  în locul modelului de calitate (`gpt-5.6-sol`, 10-100 de mesaje/5 h).
- **Mai lent** decât un apel API: aproximativ 45 s pentru un README complet, față de
  câteva secunde prin apel direct.
- **Refuzat în CI** (dacă `CI` sau `GITHUB_ACTIONS` este definită): abonamentul
  se autentifică printr-un fișier personal de sesiune, iar transferarea acestuia pe un runner
  partajat înseamnă depunerea acolo a unei identități reutilizabile de orice proces care
  rulează pe acesta. Utilizați o cheie API în acest caz.
- Variabile de mediu: `CODEX_BIN` (calea explicită a executabilului) și
  `CODEX_TIMEOUT` (secunde per segment, implicit `600`).

### Traducerea folosind abonamentul Grok (`--use_grok_cli`)

Același principiu ca pentru `--use_codex`, cu CLI-ul oficial **Grok Build**: traducerea
este dedusă din abonamentul Grok (SuperGrok / X Premium+), în loc să fie
facturată per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolare — de citit înainte de utilizare.** Acest furnizor este structural **mai
slab** decât `--use_codex`, iar acest lucru este asumat:

- Codex rulează în `--sandbox read-only`, o limită impusă de sistem.
- Sandbox-ul Grok **nu poate fi aplicat** pe multe sisteme Linux
  recente: AppArmor blochează user namespaces fără privilegii începând cu Ubuntu
  24.04, iar deny-list-ul socketurilor runtime-ului pentru containere eșuează dacă
  `/run/podman` se află în `0700`. Totuși, un profil **integrat** care nu poate fi
  aplicat pornește **fără izolare, în tăcere**.
- Prin urmare, scriptul nu solicită implicit niciun profil și **nu recurge niciodată
  în tăcere la o variantă alternativă**: afișează un avertisment. Izolarea se bazează pe
  regulile `--deny` ale CLI-ului (inclusiv regula generală `*`), singurul strat măsurat
  _fail-closed_ — o regulă necunoscută determină refuzarea pornirii, în loc să
  elimine protecția fără avertisment.
- Pentru a **impune** sandbox-ul sistemului de operare: `GROK_TRANSLATE_SANDBOX=read-only`.
  Pornirea va eșua dacă sistemul nu îl poate aplica, acesta fiind
  comportamentul dorit.

**Cotă**: fondul Grok este **săptămânal și partajat** cu Chat, Imagine și
Voice și nicio comandă nu permite consultarea lui. Prin urmare, o procesare în lot poate
reduce utilizarea disponibilă pentru conversații fără nicio notificare — de aici
concurența limitată la 2 și avertismentul din `regen_translations.sh`.

Alte variabile: `GROK_BIN` (calea executabilului), `GROK_TIMEOUT` (implicit 900 s).

Pentru regenerarea celor 28 de traduceri:

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
### Traducerea cu OpenCode, către furnizorul ales (`--use_opencode`)

[OpenCode](https://opencode.ai) este un agent de cod **open source (MIT)** în
terminal. Nu este un furnizor de modele, ci un **router** către cele
configurate chiar în OpenCode: o cheie API, un abonament,
gateway-ul OpenCode Zen — care oferă modele gratuite **fără cont** — sau
un model **local**. Acest provider controlează `opencode run` în mod neinteractiv și
limitează apelul la un singur schimb, fără niciun instrument.

Două dintre aceste variante au fost măsurate aici de la un capăt la altul: **gateway-ul Zen** și
**Ollama** local. Celelalte anunțate de OpenCode (GitHub Copilot, LM Studio,
llama.cpp) ar trebui să funcționeze prin construcție, deoarece provider-ul comunică
doar cu OpenCode — dar nu au fost testate, iar acest README menționează doar ceea
ce a fost verificat.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` este **obligatoriu**, în formatul `provider/modèle`. OpenCode nu este
un furnizor și nu este aleasă nicio valoare implicită în locul dvs.: propria sa
variantă de rezervă ar fi un model gratuit ale cărui schimburi pot fi folosite pentru antrenare.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Izolare — ce face scriptul la fiecare apel:**

- O configurație inline (`OPENCODE_CONFIG_CONTENT`), care are prioritate față de
  configurația dvs., definește un agent `aipmt` pentru care **toate instrumentele sunt refuzate**
  (`permission: { "*": "deny" }`): modelul nu poate nici să citească, nici să scrie, nici să
  lanseze comenzi — conform măsurătorilor, nici măcar nu încearcă. Partajarea sesiunii
  este dezactivată, `--pure` exclude pluginurile externe, niciodată `--auto`.
- Apelul rulează într-un **director temporar și gol**, cu opțiunile
  `OPENCODE_DISABLE_PROJECT_CONFIG` și `OPENCODE_DISABLE_CLAUDE_CODE`: fără
  acestea, OpenCode injectează în fiecare prompt `AGENTS.md` din directorul curent
  și propriul `~/.claude/CLAUDE.md` — conform măsurătorilor, o instrucțiune „încheie fiecare răspuns
  cu BANANA” introdusă într-un `AGENTS.md` era aplicată traducerii. În schimb,
  regulile globale din `~/.config/opencode/AGENTS.md` rămân
  aplicate: OpenCode nu permite excluderea lor.
- Contractul de ieșire impune simultan: cod de retur 0, niciun eveniment
  `error`, niciun apel de instrument, un ultim pas încheiat cu `stop`, un text
  nevid și agentul încărcat efectiv — un `--agent` necunoscut nu provoacă
  eșecul OpenCode, ci revine **în tăcere** la agentul de codare, cu instrumentele
  active. Nici un `exit 0` nu dovedește nimic aici.
- **Nicio cheie aipmt nu este transmisă** subprocesului (aceeași filtrare
  ca pentru Codex și Grok), cu o singură excepție nominală: `OPENCODE_API_KEY`,
  cheia OpenCode însuși (Zen, Go). Furnizorii se configurează în
  OpenCode (`opencode auth login`, `opencode.json`), nu în `.env` al aipmt.

**De știut:**

- **Modelele gratuite Zen sunt modele „stealth” sau furnizate de contribuitori**,
  variabile, cu limite nedocumentate, iar schimburile lor pot fi folosite pentru
  antrenare: perfecte pentru documentație publică, de evitat pentru
  conținut privat. Conform măsurătorilor: `opencode/mimo-v2.5-free` traduce acest README
  dintr-o singură trecere; `opencode/big-pickle` este mai lent, iar două cereri simultane
  au rămas fără răspuns.
- **Un model local trebuie să ofere cel puțin 16 k de context** — segmentele au
  până la 16.000 de caractere — în timp ce Ollama configurează adesea implicit
  4.096. Cu Ollama: un `Modelfile` cu `PARAMETER num_ctx 32768`, apoi
  `ollama create`. Calitatea depinde de model: un 7B a inversat o listă și
  a deteriorat delimitatorul unui bloc de cod într-un fișier de test, în timp ce un model din
  gateway a păstrat totul.
- `--eco` nu are efect (modelul este cel din `--model`);
  `--reasoning_effort` este transmis ca atare drept `--variant` al OpenCode și trebuie
  solicitat doar dacă modelul îl cunoaște.
- Sesiunile sunt înregistrate de OpenCode în baza sa de date
  (`~/.local/share/opencode/`), ca orice sesiune OpenCode.
- Variabile de mediu: `OPENCODE_BIN` (calea explicită către binar,
  altfel `PATH`, apoi `~/.opencode/bin/opencode`) și `OPENCODE_TIMEOUT`
  (secunde per segment, implicit `600`). `OPENCODE_CONFIG` este respectat dacă îl
  exportați.

**Exemplu măsurat: un model local prin Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
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

`reasoningEffort: "none"` nu este un detaliu: Ollama activează implicit raționamentul
pentru aceste modele, iar un Modelfile nu îl poate dezactiva. Măsurat prin
OpenCode: fără opțiune, „Pisica doarme pe covor” consumă 919 tokens
de raționament și 68 s; cu aceasta, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Rezultate pentru un articol de blog real de 589 de rânduri (140 de linkuri, 21 de secțiuni,
3 citate în engleză protejate prin modul `--news`), aceeași comandă, trei
modele:

| Model                                    | Durată       | Structură                                                  | Abateri                                                                                   |
| ---------------------------------------- | ------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuit) | 4 min 26 s   | identică sursei                                            | niciuna                                                                                   |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s  | linkuri, URL-uri, tabele, taguri, text aldin și cod inline identice | un rând de citat inventat (🇺🇸 + parafrază), o atribuire duplicată                         |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s   | linkuri, URL-uri, tabele și taguri identice                | un rând de citat inventat, câteva texte aldine și coduri inline adăugate, un segment retradus |

Aceste două modele locale au fost între timp **eliminate**: o singură abatere per articol
este suficientă pentru a descalifica un model destinat traducerilor publicate. Alte cinci au fost
eliminate din aceleași motive sau din cauza depășirii limitei de timp (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Doar
`gpt-oss:20b` a fost păstrat — și chiar acesta lasă pasaje în franceză într-un
articol dens; consultați tabelul modelelor recomandate.

În timpul traducerii locale: GPU la 98% și 170 W, 10 GB de VRAM utilizați
(modelul și cache-ul de 32 k tokens, fără nimic transferat în RAM), 7,5 GB RAM pentru
serverul Ollama. Un model cu 9 până la 12 miliarde de parametri respectă
structura, dar își permite o abatere per articol, în timp ce modelul din gateway
nu și-a permis niciuna: trebuie recitit înainte de publicare sau rezervat ciornelor.

### Traducerea prin OpenRouter (`--use_openrouter`)

OpenRouter este un **router** pentru peste 400 de modele găzduite de terți,
facturat în funcție de utilizare dintr-un credit unic. Oferă acces printr-o singură cheie la modele
pe care niciunul dintre ceilalți providers nu le expune, în special la modelele chinezești deschise.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Două particularități ale rutării au dictat implementarea și ambele pot fi
măsurate:

- **Același model este furnizat de zeci de servicii de găzduire cu limite
  diferite.** Pentru `z-ai/glm-5.3-flash`, 23 de servicii de găzduire, dintre care unul limitat la
  2.048 de tokens de ieșire: fără măsuri de precauție, una din 23 de traduceri lungi era
  trunchiată, aleatoriu în funcție de rutare și fără niciun semnal. Un preflight citește
  `/api/v1/models/{modèle}/endpoints`, exclude serviciile de găzduire cu mai puțin de 8.000 de tokens
  de ieșire sau cu stare degradată, apoi le fixează pe celelalte cu
  `allow_fallbacks: false` — în lipsa căruia routerul alege din nou un serviciu de găzduire
  exclus.
- **Raționamentul este facturat la tariful de ieșire.** Aceeași cerere pentru
  `z-ai/glm-5.2`, răspuns „OK”: 107 tokens de completare cu setarea implicită a modelului,
  2 cu raționamentul dezactivat. Prin urmare, acesta este dezactivat implicit pentru modelele
  care permit acest lucru. Cele care îl impun — `reasoning.mandatory`, 288 dintre cele 431 de
  modele din catalog — primesc **cel mai redus efort pe care declară că îl
  acceptă**, nu setarea lor implicită: pentru `z-ai/glm-5.3-flash` acesta este
  `max` și satura cei 32.768 de tokens de ieșire înainte de terminarea
  traducerii. Mărirea limitei nu ar fi schimbat nimic, deoarece efortul îi alocă un
  procent. `--reasoning_effort` rămâne prioritar, iar `none` pentru un model
  care impune raționamentul este semnalat, nu eludat.

Preflight-ul este **fail-closed** și afișează ceea ce a selectat:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Un slug absent din catalog, un catalog inaccesibil sau lipsa unui serviciu de găzduire
care respectă limita opresc comanda înainte de orice facturare.

Alte aspecte:

- Fereastra de context provine din catalog, nu dintr-o constantă: segmentarea
  se adaptează efectiv la aceasta, inclusiv pentru modelele cu 4.095 de tokens.
- `--eco` nu are efect (modelul este cel din `--model`).
- `finish_reason=length` cu o ieșire goală nu reprezintă o trunchiere, ci un
  buget consumat de raționament; mesajul precizează acest lucru, deoarece cele două
  cazuri necesită acțiuni opuse.
- Variabile de mediu: `OPENROUTER_API_KEY` (cheie, la
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (implicit
  `https://openrouter.ai/api/v1`, `https://` obligatoriu), `OPENROUTER_TIMEOUT`
  (secunde per apel, implicit `900`) și `OPENROUTER_PREFLIGHT_TIMEOUT`
  (implicit `30`).

### Modul economic

Folosește modele mai rapide și mai ieftine (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opțiuni

| Opțiune                  | Descriere                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Un singur fișier Markdown de tradus                                                                           |
| `--source_dir`           | Directorul sursă care conține fișierele Markdown                                                              |
| `--target_dir`           | Directorul de ieșire pentru fișierele traduse                                                                 |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                                                        |
| `--target_lang`          | Limba țintă (implicit: `en`)                                                                        |
| `--model`                | Modelul specific de utilizat                                                                                  |
| `--eco`                  | Folosește modelele economice                                                                                  |
| `--use_mistral`          | Folosește API-ul Mistral AI                                                                                   |
| `--use_claude`           | Folosește API-ul Claude                                                                                       |
| `--use_gemini`           | Folosește API-ul Gemini                                                                                       |
| `--use_codex`            | Folosește CLI-ul Codex din cota abonamentului ChatGPT                                                         |
| `--use_grok`             | Folosește API-ul xAI (Grok) — necesită `XAI_API_KEY`                                                        |
| `--use_openrouter`       | Folosește OpenRouter — necesită `OPENROUTER_API_KEY` și `--model fournisseur/modèle`                                                |
| `--use_grok_cli`         | Folosește CLI-ul Grok din cota abonamentului Grok                                                             |
| `--use_opencode`         | Folosește OpenCode (open source) către furnizorul configurat în OpenCode; necesită `--model provider/modèle` |
| `--force`                | Forțează retraducerea                                                                                         |
| `--keep_filename`        | Păstrează numele original al fișierului                                                                       |
| `--news`                 | Modul știri: protejează citatele în EN, gestionează steagurile în funcție de limbă                            |
| `--add_translation_note` | Adaugă o notă de traducere                                                                                     |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                                 |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf aldin) sau `marker`                                 |
| `--include_model`        | Include numele modelului în fișierul de ieșire                                                                |
| `--reasoning_effort`     | Efortul de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **Cele șapte flags de provider se exclud reciproc.** Combinarea a două dintre ele
> era acceptată anterior în tăcere și o selecta pe prima verificată: o
> traducere solicitată din cota abonamentului (`--use_codex`, `--use_grok_cli`)
> putea astfel ajunge să fie facturată în funcție de utilizare, fără niciun avertisment.
> `argparse` refuză acum combinația.

### Nota de traducere: poziții și formate

Cu `--add_translation_note`, translator-ul poate plasa nota sus, jos sau în ambele locuri și o poate reda fie în format text simplu (compatibil retroactiv), fie în format `marker` utilizabil de un plugin Markdown.

**Poziție** (`--note_position`):

- `bottom` (implicit): nota la sfârșitul fișierului, ca în trecut.
- `top`: nota inserată **după frontmatter-ul YAML** (compatibilitate cu Astro Content Collections, gray-matter etc.).
- `both`: nota inserată sus ȘI jos (un singur apel LLM, conținut reutilizat pentru ambele poziționări).

**Format** (`--note_format`):

- `legacy` (implicit): paragraf aldin `**...**` — comportament strict identic cu v1.8, byte-for-byte. Compatibil cu Hugo, GitHub, GitLab și orice renderer Markdown.
- `marker`: definiție Markdown invizibilă a unei referințe de link (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), urmată de un blockquote aldin. Poate fi citită nativ pe GitHub/GitLab și utilizată la build de un plugin remark în Astro pentru a produce un banner stilizat (consultați blogul jls42.org).

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

| Provider   | Calitate (implicit)                      | Economic (`--eco`) |
| ---------- | ---------------------------------------- | -------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                          | `claude-haiku-4-5`            |
| Mistral    | `mistral-large-latest`                          | `mistral-small-latest`            |
| Gemini     | `gemini-3.7-flash`                          | `gemini-3.1-flash-lite`            |
| Codex      | `gpt-5.6-sol`                          | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                          | `grok-4.3`            |
| Grok CLI   | `grok-4.6`                          | `grok-4.5`            |
| OpenCode   | `--model provider/modèle` obligatoriu              | la fel — `--eco` fără efect |
| OpenRouter | `--model fournisseur/modèle` obligatoriu              | la fel — `--eco` fără efect |
## Ce modele se ridică la înălțimea așteptărilor

Un model care traduce bine un paragraf nu păstrează neapărat structura
unui document întreg. Aceste măsurători provin din **traduceri executate
efectiv**, cu comanda pe care ați vedea-o mai sus, pe trei seturi de
documente și paisprezece limbi-țintă: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Două coloane, iar ele nu indică același lucru. **Scrise** numără
traducerile finalizate — mecanismele de protecție împotriva eșecurilor silențioase ale scriptului
permit trecerea fișierului. **Fără abateri** le numără pe cele a căror structură este
identică sursei: aceleași secțiuni, aceleași linkuri, aceleași URL-uri, aceleași blocuri și
coduri inline, aceleași tabele, aceleași citate, aceleași marcaje.

### Articol de blog dens, modul `--news`

589 de linii, 140 de linkuri, 21 de secțiuni, 3 citate în engleză protejate. Este
cel mai solicitant document dintre cele trei: modul `--news` adaugă constrângeri privind
marcajele și citatele peste structura Markdown.

| Model                             | Acces              | Scrise  | Fără abateri | Mediană/limbă |
| --------------------------------- | ------------------ | ------- | ------------ | ------------- |
| `gemini-3.7-flash`                | API Google         | 14/14   | **14/14**    | 1 min 18 s    |
| `gpt-5.6-sol` (`--use_codex`)     | abonament ChatGPT  | 14/14   | **14/14**    | 11 min 28 s   |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | **14/14**    | 5 min 37 s    |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | 13/14        | 26 min 23 s   |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14   | 12/14        | 15 min 49 s   |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9     | 7/9          | 20 min 33 s   |
| `claude-sonnet-5`                 | API Anthropic      | 14/14   | 11/14        | 6 min 31 s    |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | 11/14        | 9 min 27 s    |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | 7/14         | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`          | local              | 10/14   | 7/14         | 12 min 39 s   |
| `mistral-large-latest`            | API Mistral        | 11/14   | 5/14         | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | 3/14         | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)     | abonament Grok     | 1/14    | 1/14         | 23 min 11 s   |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4     | 1/4          | 23 min 00 s   |

Două loturi au fost **întrerupte din lipsă de credit**, iar numitorul lor indică acest lucru:
`qwen3.5-27b` s-a oprit la nouă limbi, iar `kimi-k2.6` la patru — acesta din urmă
după depășirea limitei de timp de patruzeci de minute și două refuzuri, la aproape
0,33 $ per limbă.

O precizare metodologică privind rândurile OpenRouter: acestea au fost măsurate cu
setările **implicite ale routerului**, înainte ca `--use_openrouter` să existe.
`z-ai/glm-5.2` a fost măsurat din nou între timp cu providerul inclus, cu raționamentul dezactivat,
și oferă exact același rezultat de 14/14. `z-ai/glm-5.3-flash` a eșuat de două ori din
cauza epuizării bugetului de ieșire la setările implicite ale routerului; providerul solicită acum
acestor modele cel mai redus nivel de efort pe care îl acceptă, iar verificarea de control pe
limbile problematice reușește.

### README-ul acestui proiect, Markdown standard

508 linii, 219 coduri inline, 40 de delimitatoare de blocuri, 45 de linii de tabel. Nu există
modul `--news` aici: dificultatea provine din densitatea codului.

| Model                         | Scrise  | Fără abateri | Mediană/limbă |
| ----------------------------- | ------- | ------------ | ------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14        | 1 min 22 s    |
| `gemini-3.7-flash`            | 14/14   | 13/14        | 21 s          |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14        | 2 min 04 s    |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14         | 3 min 25 s    |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14         | 3 min 38 s    |

### Patru README-uri ale unor proiecte cunoscute

FastAPI, Ollama, tldr-pages și Vue.js, preluate ca atare de pe GitHub. Aceste documente
sunt **mai ușoare** decât cele două precedente, iar tabelul arată acest lucru.

| Model                     | Domeniu                    | Scrise  | Fără abateri |
| ------------------------- | -------------------------- | ------- | ------------ |
| `opencode/mimo-v2.5-free` | 4 proiecte × 14 limbi      | 55/56   | 47/56        |
| `grok-4.6` (abonament)    | 4 proiecte × ar, hi, ja, zh | 16/16   | 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 proiecte × ar, hi, ja, zh | 15/16   | 9/16         |

### Ce concluzii tragem

- **Trei modele nu au pierdut niciodată informații** în cele două documente
  dense: `gemini-3.7-flash`, `gpt-5.6-sol` prin abonamentul ChatGPT și
  `z-ai/glm-5.2` prin OpenRouter. Singurele lor abateri în modul standard sunt câte o
  pereche de `**` care nu a fost reprodusă în una sau două limbi, niciodată un URL, un bloc
  de cod sau un citat.
- **Factorul determinant este densitatea documentului, nu modul `--news`.**
  Grok prin abonament eșuează de 13 ori din 14 pentru articolul de blog și reușește 14
  README-uri publice din 16: cauza eșecului său este pierderea firului într-un segment lung,
  confirmată printr-o verificare de control — pasajul izolat este tradus corect.
- **Scrierile non-latine nu reprezintă diferența așteptată.** `gpt-oss` lasă
  pasaje în franceză în traducerile în arabă, japoneză, poloneză **și română**; Mistral
  și MiMo pierd coduri inline doar în scrierile non-latine.
- **Dezactivarea raționamentului nu afectează deloc calitatea.** `z-ai/glm-5.2` produce
  paisprezece limbi fără nicio abatere în ambele condiții — raționament activ
  în mod implicit în router, apoi dezactivat prin `--use_openrouter` — cu de optsprezece ori
  mai puțini tokeni de ieșire facturați. Aceasta este măsurătoarea care justifică setarea
  implicită a providerului.
- **Un model lent nu este un model sigur.** `deepseek-v4-flash-0731` are nevoie de 37 de
  minute per limbă pentru 4 traduceri din 14, `qwen3.8-flash` de 26 de minute pentru
  un rezultat aproape perfect, iar Gemini de 1 minut și 18 secunde pentru un rezultat fără greșeală.

### Ce nu reprezintă acest tabel

- **Nu este un clasament exhaustiv.** Numai OpenRouter oferă peste
  patru sute de modele; aproximativ cincisprezece au fost măsurate aici. Absența unui
  model nu spune nimic despre calitatea sa, ci doar că nu a fost încercat.
- **Aceste măsurători au o dată**: 4 și 5 septembrie 2026. Modelele se schimbă
  sub același nume, furnizorii ajustează cuantificările și limitele, iar
  modele noi apar în fiecare săptămână.
- **Duratele nu stabilesc niciun clasament.** Paralelismul a variat între 3 și 6 traduceri
  simultane, în funcție de campanie, iar debitul unui furnizor variază de-a lungul
  zilei. Ele oferă un ordin de mărime, nu o comparație.
- **Un rezultat depinde de document la fel de mult ca de model.** Același model
  reușește paisprezece limbi pentru un articol și nouă pentru acest README. Fișierele dumneavoastră nu
  sunt ale noastre.
- **Abordarea corectă rămâne să măsurați în propriul mediu**: traduceți unul dintre
  documentele dumneavoastră în limbile-țintă, apoi comparați structura — numărul de
  secțiuni, linkuri, URL-uri distincte, blocuri de cod, coduri inline și
  linii de tabel. Exact acest lucru îl face protocolul de mai sus și încape
  într-o buclă pe `aipmt`.

## Proiecte care utilizează acest script

- **[jls42.org](https://jls42.org)** - Blog personal multilingv (15 limbi)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articol tradus din fr în ro cu gpt-5.6-sol.**
