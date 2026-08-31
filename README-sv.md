# AI-driven Markdownöversättare

🌍 [Franska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engelska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spanska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Kinesiska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Tyska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japanska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreanska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabiska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italienska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederländska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugisiska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumänska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status för kvalitetsgrind"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Säkerhetsklassificering"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Tillförlitlighetsklassificering"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Underhållbarhetsklassificering"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Täckning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Sårbarheter"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Buggar"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Kodlukt"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicerade rader (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Teknisk skuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Kodrader"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-märke"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Översättare för Markdown-filer med **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Multi-Provider**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini) samt Codex CLI med ChatGPT-prenumeration
- **Modeller 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Ekonomiskt läge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativet `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokenbegränsningar per modell
- **Kodbevarande**: Kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativet `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativet `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsanteckning**: Valfritt tillägg av en anteckning i slutet av dokumentet

## Installation

### Använda verktyget

```bash
pip install ai-powered-markdown-translator
```

Kommandot `aipmt` är då tillgängligt överallt. Om katalogen med
Python-skript inte finns i din `PATH`, gör `python -m aipmt` exakt samma
sak. Python 3.10 eller senare.

För en isolerad installation, separerad från dina övriga paket:

```bash
pipx install ai-powered-markdown-translator
```

### Bidra till projektet

Det klonade arkivet behövs fortfarande för utveckling: det är där testerna,
de 28 översättningarna och alla kvalitetsverktyg finns.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` är en **helt låst lock-fil**, en exakt avbild av den testade
miljön. Gränserna som publiceras i `pyproject.toml` är avsiktligt bredare:
de ställer inga krav på dina andra paket.

### Kvalitetsverktyg (valfritt men rekommenderat)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra att fel formaterad eller sårbar kod, eller kod som innehåller en hemlighet, committas. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (successiv typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet _Quality / pre-commit_ i `CLAUDE.md` för mer information.

## Konfiguration

Skapa en fil `.env` **i katalogen från vilken du kör
kommandot** (den söks där och därefter i överordnade kataloger), eller
definiera miljövariablerna:

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

`GEMINI_API_KEY` accepteras som alternativ till `GOOGLE_API_KEY` (AI
Studio-konvention). Valfria variabler: `XAI_BASE_URL` (xAI-slutpunkt,
standardvärde `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekunder per Anthropic-anrop,
standardvärde 900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` /
`GROK_HOME` / `GROK_TIMEOUT`, samt `GROK_TRANSLATE_SANDBOX` (se avsnittet Grok CLI).
För `regen_translations.sh` gäller: `REGEN_PROVIDER`, `REGEN_MODEL` och
`REGEN_JOB_TIMEOUT` (tak per jobb, standardvärde 600 s).

## Användning

### Översätta en enskild fil

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätta en katalog

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

### Översätta med sin ChatGPT-prenumeration (`--use_codex`)

Denna provider använder ingen API-nyckel: den styr den officiella Codex CLI:n i
icke-interaktivt läge, så översättningen räknas av den redan betalda
ChatGPT-prenumerationens kvot (Plus, Pro, Business …). Detta är den enda
dokumenterade vägen från OpenAI för denna användning — tokens från
`~/.codex/auth.json` autentiserar inte anrop till Platform API och läses dessutom
aldrig av detta skript.

**Förutsättningar:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binären söks i denna ordning: variabeln `CODEX_BIN`, `PATH`,
därefter Python-paketet `openai-codex-cli-bin`. Det sistnämnda ingår avsiktligt
inte i `requirements.txt`: det är cirka 250 MB stort, vilket skulle tvingas på
alla användare för en valfri provider.

**Bra att veta:**

- **Ingen API-nyckel används.** `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort
  från underprocessens miljö, vilket garanterar att en nyckel i `.env`
  aldrig får översättningen att övergå till användningsbaserad debitering.
- **Ett segment = ett ”lokalt meddelande”** i planens femtimmarsfönster.
  Använd `--eco` (modell `gpt-5.6-luna`, 250–2 000 meddelanden/5 h på
  Plus) i stället för kvalitetsmodellen (`gpt-5.6-sol`, 10–100 meddelanden/5 h).
- **Långsammare** än ett API-anrop: räkna med cirka 45 s för en komplett
  README, jämfört med några sekunder direkt.
- **Nekas i CI** (`CI` eller `GITHUB_ACTIONS` definierad):
  prenumerationsautentisering är inte avsedd för en delad runner, och OpenAI
  avråder från detta arbetsflöde i offentliga arkiv. Använd en API-nyckel
  för denna väg.
- Miljövariabler: `CODEX_BIN` (explicit sökväg till binären) och
  `CODEX_TIMEOUT` (sekunder per segment, standardvärde `600`).

### Översätta med sin Grok-prenumeration (`--use_grok_cli`)

Samma princip som för `--use_codex`, med den officiella CLI:n **Grok Build**:
översättningen räknas av Grok-prenumerationens kvot (SuperGrok / X Premium+)
i stället för att debiteras per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Begränsning — läs före användning.** Denna provider är strukturellt
**svagare** än `--use_codex`, och det är avsiktligt:

- Codex körs i `--sandbox read-only`, en gräns som systemet kräver.
- Groks sandbox **kan inte tillämpas** på många nyare Linux-system:
  AppArmor blockerar oprivilegierade user namespaces sedan Ubuntu 24.04, och
  deny-listan för containrars runtime-sockets misslyckas om `/run/podman` är
  `0700`. En **inbyggd** profil som inte kan tillämpas startar
  dessutom **okonfinerad, i tysthet**.
- Skriptet begär därför ingen profil som standard och faller **aldrig tillbaka i
  tysthet**: det visar en varning. Begränsningen bygger på CLI:ns
  `--deny`-regler (inklusive catch-all-regeln `*`), det enda
  uppmätta lagret med _fail-closed_ — en okänd regel gör att starten nekas
  i stället för att skyddet tas bort utan att det meddelas.
- För att **kräva** OS-sandboxen: `GROK_TRANSLATE_SANDBOX=read-only`. Starten misslyckas om
  maskinen inte kan uppfylla kravet, vilket är det avsedda beteendet.

**Kvot**: Grok-poolen är **veckovis och delad** med Chat, Imagine och Voice,
och inget kommando kan läsa den. En batchkörning kan därför förbruka din
konversationskvot utan att något meddelar det — därav en begränsning till
2 samtidiga körningar och en varning i `regen_translations.sh`.

Övriga variabler: `GROK_BIN` (sökväg till binären), `GROK_TIMEOUT`
(standardvärde 900 s).

För att återskapa de 28 översättningarna:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Ekonomiskt läge

Använder snabbare och billigare modeller (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ                | Beskrivning                                                              |
| ------------------------- | ------------------------------------------------------------------------ |
| `--file`            | Enskild Markdown-fil att översätta                                       |
| `--source_dir`            | Källkatalog som innehåller Markdown-filerna                              |
| `--target_dir`            | Utmatningskatalog för de översatta filerna                               |
| `--source_lang`            | Källspråk (standard: `fr`)                                    |
| `--target_lang`            | Målspråk (standard: `en`)                                     |
| `--model`            | Specifik modell att använda                                              |
| `--eco`            | Använd ekonomiska modeller                                                |
| `--use_mistral`            | Använd Mistral AI API                                                     |
| `--use_claude`            | Använd Claude API                                                         |
| `--use_gemini`            | Använd Gemini API                                                         |
| `--use_codex`            | Använd Codex CLI på ChatGPT-prenumerationens kvot                        |
| `--use_grok`            | Använd xAI API (Grok) — kräver `XAI_API_KEY`                            |
| `--use_grok_cli`            | Använd Grok CLI på Grok-prenumerationens kvot                             |
| `--force`            | Tvinga fram en ny översättning                                            |
| `--keep_filename`            | Behåll det ursprungliga filnamnet                                        |
| `--news`            | Nyhetsläge: skyddar EN-citat och hanterar flaggor per språk              |
| `--add_translation_note`            | Lägg till en översättningsanteckning                                      |
| `--note_position`            | Anteckningens placering: `top`, `bottom` (standard), eller `both` |
| `--note_format`            | Anteckningens format: `legacy` (standard, fet paragraf) eller `marker` |
| `--include_model`            | Inkludera modellnamnet i utdatafilen                                     |
| `--reasoning_effort`            | GPT-5.x-resonemangsansträngning: `none`/`low`/`medium`/`high`/`xhigh` |

> **De sex provider-flaggorna är ömsesidigt uteslutande.** Att kombinera två
> accepterades tidigare i tysthet och löstes till den första som testades:
> en översättning som begärdes på prenumerationskvot (`--use_codex`,
> `--use_grok_cli`) kunde därmed gå över till användningsbaserad debitering utan
> någon varning. `argparse` avvisar nu kombinationen.

### Översättningsanteckning: placeringar och format

Med `--add_translation_note` kan translator placera anteckningen längst upp, längst ned
eller på båda platserna, och återge den antingen i enkelt textformat
(bakåtkompatibelt) eller i formatet `marker` som kan användas av ett
Markdown-plugin.

**Placering** (`--note_position`):

- `bottom` (standard): anteckning i slutet av filen, som historiskt.
- `top`: anteckning infogas **efter YAML-frontmatter** (säkerhet för Astro Content Collections, gray-matter osv.).
- `both`: anteckning infogas både längst upp OCH längst ned (ett enda LLM-anrop, innehållet återanvänds för båda placeringarna).

**Format** (`--note_format`):

- `legacy` (standard): fet paragraf `**...**` — exakt samma beteende som i v1.8, byte för byte. Kompatibelt med Hugo, GitHub, GitLab och alla Markdown-renderare.
- `marker`: osynlig Markdown-definition av länkreferens (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), följd av ett fetstilt blockquote. Läsbar direkt på GitHub/GitLab och kan användas vid bygget av ett remark-plugin i Astro för att skapa en stiliserad banner (se bloggen jls42.org).

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

### Standardmodeller (2026)

| Provider | Kvalitet (standard) | Ekonomisk (`--eco`) |
| -------- | ------------------- | --------------------------- |
| OpenAI   | `gpt-5.6-terra`     | `gpt-5.6-luna`              |
| Claude   | `claude-sonnet-5`     | `claude-haiku-4-5`              |
| Mistral  | `mistral-large-latest`     | `mistral-small-latest`              |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite`              |
| Codex    | `gpt-5.6-sol`     | `gpt-5.6-luna`              |
| Grok API | `grok-4.6`     | `grok-4.3`              |
| Grok CLI | `grok-4.6`     | `grok-4.5`              |

> **Rekommendation för långformstexter**: `--use_gemini` (standard =
> `gemini-3.7-flash`) bevarar Markdown-strukturen troget för skript på icke-latinska
> språk (PL, JA, ZH, AR, HI), även i `--news`-läge där
> platshållarnas trohet är viktig. Mätt på denna README översatt till japanska:
> identisk struktur med `gemini-3.1-pro-preview` (21 listor, 18 kodblock, 13 HTML-länkar,
> 13 bilder, alla URL:er bevarade) med cirka 6 gånger lägre latens. OpenAI
> förblir standard för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX  
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel översatt från fr till sv med gpt-5.6-luna.**
