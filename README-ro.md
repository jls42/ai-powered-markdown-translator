# Traductor Markdown bazat pe AI

🌍 [Franceză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engleză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spaniolă](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chineză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Germană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japoneză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreeană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabă](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandeză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Poloneză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugheză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Suedeză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Calitatea codului</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Starea Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Evaluarea securității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Evaluarea fiabilității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Evaluarea mentenabilității"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Acoperire"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilități"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Erori"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Linii duplicate (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Datorie tehnică"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linii de cod"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Insigna Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traductor de fișiere Markdown care utilizează **OpenAI**, **Mistral AI**, **Claude (Anthropic)** și **Google Gemini**.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă, păstrând formatarea, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Multi-Provider**: compatibil cu 4 API-uri (OpenAI, Mistral, Claude, Gemini) + CLI-ul Codex inclus în abonamentul ChatGPT
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Mod economic**: opțiunea `--eco` pentru utilizarea unor modele mai rapide și mai puțin costisitoare
- **Fișier unic**: opțiunea `--file` pentru traducerea unui singur fișier
- **Segmentare inteligentă**: gestionarea textelor lungi cu limite de tokeni per model
- **Păstrarea codului**: blocurile de cod ȘI codul inline (`` `...` ``) sunt păstrate
- **Nume de fișier**: opțiunea `--keep_filename` pentru păstrarea numelui original
- **Mod News**: opțiunea `--news` pentru protejarea citatelor în engleză și gestionarea steagurilor în articolele de știri
- **Configurare .env**: compatibilitate cu fișierul `.env` pentru cheile API
- **Notă de traducere**: adăugarea opțională a unei note la sfârșitul documentului

## Instalare

### Pentru utilizarea instrumentului

```bash
pip install ai-powered-markdown-translator
```

Comanda `aipmt` este acum disponibilă oriunde. Dacă directorul scripturilor
Python nu se află în `PATH`, `python -m aipmt` face exact același
lucru. Python 3.10 sau o versiune mai recentă.

Pentru o instalare izolată de restul pachetelor:

```bash
pipx install ai-powered-markdown-translator
```

### Pentru a contribui la proiect

Depozitul clonat rămâne necesar pentru dezvoltare: aici se află testele,
cele 28 de traduceri și toate instrumentele de verificare a calității.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` este un **lock fixat complet**, o reflectare exactă a
mediului testat. Limitele publicate în `pyproject.toml` sunt
intenționat mai largi: nu impun nimic celorlalte pachete.

### Instrumente de verificare a calității (opționale, dar recomandate)

Proiectul utilizează [`pre-commit`](https://pre-commit.com) pentru a împiedica trimiterea unui cod neformatat, vulnerabil sau care conține un secret. Instalare:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook-uri active: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexitate), detect-secrets (chei API), mypy (tipizare progresivă), Opengrep (SAST), pip-audit (dependențe CVE), unittest. Consultă secțiunea _Quality / pre-commit_ din `CLAUDE.md` pentru detalii.

## Configurare

Cheile sunt căutate în **trei locuri**, de la cel mai prioritar la cel mai puțin prioritar.
Fiecare completează doar ceea ce precedentul lasă necompletat.

|     | Unde                                            | Pentru ce                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabile de mediu                     | CI, containere, excepții punctuale |
| 2   | `.env` din directorul curent (sau dintr-un director părinte) | o cheie proprie proiectului            |
| 3   | `~/.config/aipmt/.env`                        | **instalat o singură dată, valabil peste tot**   |

Cel mai simplu după un `pip install` este al treilea:

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
(altfel este ignorată, conform specificației) și `%APPDATA%`
în Windows.

Al doilea rămâne util atunci când un depozit are propria cheie: un `.env` din rădăcina sa
are prioritate față de configurația utilizatorului, fără a o modifica. Iar o variabilă deja
definită în mediu are prioritate față de ambele:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Dacă nu este găsită nicio cheie, comanda nu afișează o urmă de apel: enumeră
cele trei locații împreună cu calea lor exactă.

`GEMINI_API_KEY` este acceptat ca alternativă la `GOOGLE_API_KEY` (convenția AI
Studio). Variabile opționale: `XAI_BASE_URL` (endpoint xAI, implicit
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secunde per apel Anthropic, implicit
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
și `GROK_TRANSLATE_SANDBOX` (consultă secțiunea Grok CLI). Pentru
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` și
`REGEN_JOB_TIMEOUT` (limită per job, implicit 600 s).

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
```

### Traducerea folosind abonamentul ChatGPT (`--use_codex`)

Acest provider nu consumă nicio cheie API: controlează CLI-ul Codex oficial în modul
non-interactiv, astfel încât traducerea este dedusă din cota abonamentului
ChatGPT (Plus, Pro, Business…) deja plătit. Aceasta este singura cale documentată de
OpenAI pentru această utilizare — tokenii din `~/.codex/auth.json` nu autentifică
apelurile către API-ul Platform și, de altfel, nu sunt citiți niciodată de acest script.

**Cerințe preliminare:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binarul este căutat în această ordine: variabila `CODEX_BIN`, `PATH`,
apoi pachetul Python `openai-codex-cli-bin`. Acesta din urmă nu este inclus intenționat în
`requirements.txt`: are aproximativ 250 MB, ceea ce ar fi impus tuturor
utilizatorilor pentru un provider opțional.

**De reținut:**

- **Nu este utilizată nicio cheie API.** `OPENAI_API_KEY` și `CODEX_API_KEY` sunt
  eliminate din mediul subprocesului, ceea ce garantează că o cheie prezentă în
  `.env` nu va comuta niciodată traducerea la facturarea
  în funcție de utilizare.
- **Un segment = un „mesaj local”** din fereastra de 5 ore a planului.
  Utilizează `--eco` (modelul `gpt-5.6-luna`, 250–2.000 de mesaje/5 h pentru Plus)
  mai degrabă decât modelul de calitate (`gpt-5.6-sol`, 10–100 de mesaje/5 h).
- **Mai lent** decât un apel API: estimează aproximativ 45 s pentru un README complet, față de
  câteva secunde în mod direct.
- **Refuzat în CI** (`CI` sau `GITHUB_ACTIONS` definit): autentificarea prin
  abonament nu este destinată unui runner partajat, iar OpenAI descurajează acest flux de lucru
  pe depozite publice. Utilizează o cheie API pentru această cale.
- Variabile de mediu: `CODEX_BIN` (cale explicită către binar) și
  `CODEX_TIMEOUT` (secunde per segment, implicit `600`).

### Traducerea folosind abonamentul Grok (`--use_grok_cli`)

Același principiu ca pentru `--use_codex`, cu CLI-ul oficial **Grok Build**:
traducerea este dedusă din abonamentul Grok (SuperGrok / X Premium+) în loc
să fie facturată per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolare — citește înainte de utilizare.** Acest provider este structural **mai
slab** decât `--use_codex`, iar acest lucru este asumat:

- Codex rulează în `--sandbox read-only`, o limită impusă de sistem.
- Sandbox-ul Grok **nu se poate aplica** pe multe sisteme Linux recente:
  AppArmor blochează user namespaces neprivilegiate începând cu Ubuntu 24.04,
  iar lista de respingere a socket-urilor runtime-ului de containere eșuează dacă
  `/run/podman` este `0700`. Or, un profil **integrat** care nu se poate
  aplica pornește **neizolat, în tăcere**.
- Prin urmare, scriptul nu solicită niciun profil implicit și **nu revine niciodată
  în tăcere**: afișează un avertisment. Izolarea se bazează pe regulile `--deny`
  ale CLI-ului (inclusiv regula catch-all `*`), singurul strat măsurat
  _fail-closed_ — o regulă necunoscută determină refuzul pornirii, în loc să elimine
  protecția fără a anunța.
- Pentru a **impune** sandbox-ul sistemului de operare: `GROK_TRANSLATE_SANDBOX=read-only`. Pornirea
  va eșua dacă mașina nu îl poate respecta, acesta fiind comportamentul dorit.

**Cotă**: fondul Grok este **săptămânal și partajat** cu Chat, Imagine și
Voice, iar nicio comandă nu permite citirea lui. Prin urmare, o procesare în lot
îți poate consuma utilizarea conversațională fără ca acest lucru să fie semnalat —
de aici concurența limitată la 2 și avertismentul din `regen_translations.sh`.

Alte variabile: `GROK_BIN` (calea binarului), `GROK_TIMEOUT` (implicit 900 s).

Pentru regenerarea celor 28 de traduceri:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Mod economic

Utilizează modele mai rapide și mai puțin costisitoare (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opțiuni

| Opțiune                   | Descriere                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Fișier Markdown unic de tradus                                       |
| `--source_dir`           | Director sursă care conține fișierele Markdown                        |
| `--target_dir`           | Director de ieșire pentru fișierele traduse                          |
| `--source_lang`          | Limbă sursă (implicit: `fr`)                                             |
| `--target_lang`          | Limbă țintă (implicit: `en`)                                              |
| `--model`                | Model specific de utilizat                                             |
| `--eco`                  | Utilizează modelele economice                                         |
| `--use_mistral`          | Utilizează API-ul Mistral AI                                                |
| `--use_claude`           | Utilizează API-ul Claude                                                    |
| `--use_gemini`           | Utilizează API-ul Gemini                                                    |
| `--use_codex`            | Utilizează CLI-ul Codex pe cota abonamentului ChatGPT               |
| `--use_grok`             | Utilizează API-ul xAI (Grok) — necesită `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utilizează CLI-ul Grok pe cota abonamentului Grok                   |
| `--force`                | Forțează retraducerea                                                  |
| `--keep_filename`        | Păstrează numele original al fișierului                                     |
| `--news`                 | Mod știri: protejează citatele EN și gestionează steagurile în funcție de limbă |
| `--add_translation_note` | Adaugă o notă de traducere                                           |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf aldin) sau `marker`       |
| `--include_model`        | Include numele modelului în fișierul de ieșire                       |
| `--reasoning_effort`     | Efortul de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

> **Cele șase flag-uri ale providerilor se exclud reciproc.** Anterior, combinarea a două
> era acceptată în tăcere și era aleasă prima verificată: o traducere solicitată pe cota
> abonamentului (`--use_codex`, `--use_grok_cli`) putea ajunge astfel să fie facturată
> în funcție de utilizare, fără niciun avertisment.
> `argparse` refuză acum combinația.

### Notă de traducere: poziții și formate

Cu `--add_translation_note`, translatorul poate plasa nota sus, jos sau în ambele locuri și o poate reda fie în format text simplu (compatibil retroactiv), fie în format `marker` consumabil de un plugin Markdown.

**Poziție** (`--note_position`):

- `bottom` (implicit): notă la sfârșitul fișierului, ca în trecut.
- `top`: notă inserată **după frontmatter-ul YAML** (pentru securitatea Astro Content Collections, gray-matter etc.).
- `both`: notă inserată SUS și JOS (un singur apel LLM, conținut reutilizat pentru ambele poziționări).

**Format** (`--note_format`):

- `legacy` (implicit): paragraf aldin `**...**` — comportament strict identic cu v1.8, byte-for-byte. Compatibil cu Hugo, GitHub, GitLab și orice renderer Markdown.
- `marker`: definiție Markdown invizibilă pentru referința unui link (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), urmată de un blockquote aldin. Lizibilă nativ pe GitHub/GitLab și utilizabilă la build de un plugin remark în Astro pentru a produce o bară stilizată (vezi blogul jls42.org).

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

| Provider | Calitate (implicit)       | Economic (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recomandare pentru traduceri long-form**: `--use_gemini` (implicit = `gemini-3.7-flash`) păstrează fidel structura Markdown pentru scripturile non-latine (PL, JA, ZH, AR, HI), inclusiv în modul `--news`, unde fidelitatea placeholderelor contează. Măsurat pe acest README tradus în japoneză: structură identică cu `gemini-3.1-pro-preview` (21 de liste, 18 blocuri de cod, 13 linkuri HTML, 13 imagini, toate URL-urile păstrate), cu o latență de aproximativ 6 ori mai mică. OpenAI rămâne implicit pentru compatibilitatea retroactivă.

## Proiecte care utilizează acest script

- **[jls42.org](https://jls42.org)** - Blog personal multilingv (15 limbi)

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Version 3. Vezi [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Articol tradus din fr în ro cu gpt-5.6-luna.**
