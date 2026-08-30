# Tłumacz Markdown wspierany przez AI

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Stan bramki jakości"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena łatwości utrzymania"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Podatności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Problemy jakości kodu"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Zduplikowane wiersze (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Wiersze kodu"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Odznaka Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumacz plików Markdown korzystający z **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Python tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Wielu providerów**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini) oraz CLI Codex w ramach subskrypcji ChatGPT
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Tryb ekonomiczny**: Opcja `--eco` umożliwiająca korzystanie z szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` umożliwiająca przetłumaczenie jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów zależnymi od modelu
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: Opcja `--keep_filename` umożliwiająca zachowanie oryginalnej nazwy
- **Tryb wiadomości**: Opcja `--news` chroniąca angielskie cytaty i obsługująca flagi w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` dla kluczy API
- **Nota o tłumaczeniu**: Opcjonalne dodanie noty na końcu dokumentu

## Instalacja

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Narzędzia jakościowe (opcjonalne, ale zalecane)

Projekt korzysta z [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego, podatnego na ataki lub zawierającego dane poufne kodu. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (CVE zależności), unittest. Szczegółowe informacje znajdują się w sekcji _Quality / pre-commit_ pliku `CLAUDE.md`.

## Konfiguracja

Utwórz plik `.env` w katalogu głównym projektu lub zdefiniuj zmienne środowiskowe:

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

`GEMINI_API_KEY` jest akceptowane jako alternatywa dla `GOOGLE_API_KEY` (konwencja AI
Studio). Zmienne opcjonalne: `XAI_BASE_URL` (endpoint xAI, domyślnie
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (liczba sekund na wywołanie Anthropic, domyślnie
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`
oraz `GROK_TRANSLATE_SANDBOX` (zobacz sekcję Grok CLI). Po stronie
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` i
`REGEN_JOB_TIMEOUT` (limit na zadanie, domyślnie 600 s).

## Użycie

### Tłumaczenie pojedynczego pliku

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tłumaczenie katalogu

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

### Tłumaczenie w ramach subskrypcji ChatGPT (`--use_codex`)

Ten provider nie zużywa żadnego klucza API: steruje oficjalnym CLI Codex w trybie
nieinteraktywnym, więc tłumaczenie jest rozliczane w ramach limitu opłaconej już
subskrypcji ChatGPT (Plus, Pro, Business…). Jest to jedyna metoda udokumentowana
przez OpenAI dla takiego zastosowania — tokeny `~/.codex/auth.json` nie uwierzytelniają
wywołań API Platform i skrypt nigdy ich nie odczytuje.

**Wymagania wstępne:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Plik binarny jest wyszukiwany w następującej kolejności: zmienna `CODEX_BIN`, `PATH`,
a następnie pakiet Python `openai-codex-cli-bin`. Ten ostatni celowo nie znajduje się
w `requirements.txt`: zajmuje około 250 MB, co stanowiłoby obciążenie dla wszystkich
użytkowników z powodu opcjonalnego providera.

**Warto wiedzieć:**

- **Nie jest używany żaden klucz API.** `OPENAI_API_KEY` i `CODEX_API_KEY` są
  usuwane ze środowiska podprocesu, co gwarantuje, że klucz
  obecny w `.env` nigdy nie przełączy tłumaczenia na rozliczanie
  według użycia.
- **Jeden segment = jedna „wiadomość lokalna”** w 5-godzinnym oknie planu.
  Używaj `--eco` (model `gpt-5.6-luna`, 250–2 000 wiadomości/5 godz. w Plus)
  zamiast modelu jakościowego (`gpt-5.6-sol`, 10–100 wiadomości/5 godz.).
- **Wolniejsze** niż wywołanie API: pełny README zajmuje około 45 s zamiast
  kilku sekund przy wywołaniu bezpośrednim.
- **Niedozwolone w CI** (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): uwierzytelnianie
  za pomocą subskrypcji nie jest przeznaczone dla współdzielonego runnera, a OpenAI
  odradza ten workflow w repozytoriach publicznych. W tym przypadku użyj klucza API.
- Zmienne środowiskowe: `CODEX_BIN` (jawna ścieżka do pliku binarnego) oraz
  `CODEX_TIMEOUT` (liczba sekund na segment, domyślnie `600`).

### Tłumaczenie w ramach subskrypcji Grok (`--use_grok_cli`)

Zasada jest taka sama jak w przypadku `--use_codex`, z użyciem oficjalnego CLI **Grok Build**:
tłumaczenie jest rozliczane w ramach subskrypcji Grok (SuperGrok / X Premium+), zamiast
być naliczane za tokeny.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolacja — przeczytaj przed użyciem.** Ten provider jest konstrukcyjnie **słabszy**
niż `--use_codex` i jest to świadoma decyzja:

- Codex działa w `--sandbox read-only`, granicy narzuconej przez system.
- Sandbox Grok **nie może zostać zastosowany** na wielu współczesnych komputerach
  z systemem Linux: AppArmor blokuje nieuprzywilejowane user namespaces od Ubuntu
  24.04, a deny-lista gniazd środowiska uruchomieniowego kontenerów zawodzi, jeśli
  `/run/podman` znajduje się w `0700`. Tymczasem **wbudowany** profil, którego
  nie można zastosować, uruchamia się **bez izolacji i bez ostrzeżenia**.
- Dlatego skrypt domyślnie nie żąda żadnego profilu i **nigdy nie przechodzi
  bez ostrzeżenia** do trybu awaryjnego: wyświetla komunikat ostrzegawczy. Izolacja opiera się
  na regułach `--deny` CLI (w tym catch-all `*`), jedynej warstwie o zmierzonym
  zachowaniu _fail-closed_ — nieznana reguła powoduje odmowę uruchomienia zamiast
  usunięcia ochrony bez powiadomienia.
- Aby **wymusić** sandbox systemu operacyjnego: `GROK_TRANSLATE_SANDBOX=read-only`.
  Uruchomienie zakończy się niepowodzeniem, jeśli komputer nie będzie w stanie go zastosować,
  co jest zamierzonym zachowaniem.

**Limit**: pula Grok jest **tygodniowa i współdzielona** z Chat, Imagine oraz
Voice, a żadne polecenie nie pozwala sprawdzić jej stanu. Przetwarzanie wsadowe może więc
ograniczyć dostępne użycie konwersacyjne bez żadnego powiadomienia — stąd
współbieżność ograniczona do 2 oraz ostrzeżenie w `regen_translations.sh`.

Inne zmienne: `GROK_BIN` (ścieżka do pliku binarnego), `GROK_TIMEOUT` (domyślnie 900 s).

Aby ponownie wygenerować 28 tłumaczeń:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Tryb ekonomiczny

Korzysta z szybszych i tańszych modeli (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                    | Opis                                                                     |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                              |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                              |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                            |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                               |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                               |
| `--model`                | Konkretny model do użycia                                                |
| `--eco`                  | Użycie modeli ekonomicznych                                              |
| `--use_mistral`          | Użycie API Mistral AI                                                    |
| `--use_claude`           | Użycie API Claude                                                        |
| `--use_gemini`           | Użycie API Gemini                                                        |
| `--use_codex`            | Użycie CLI Codex w ramach limitu subskrypcji ChatGPT                     |
| `--use_grok`             | Użycie API xAI (Grok) — wymaga `XAI_API_KEY`                            |
| `--use_grok_cli`         | Użycie CLI Grok w ramach limitu subskrypcji Grok                         |
| `--force`                | Wymuszenie ponownego tłumaczenia                                         |
| `--keep_filename`        | Zachowanie oryginalnej nazwy pliku                                       |
| `--news`                 | Tryb wiadomości: chroni cytaty EN, obsługuje flagi według języka         |
| `--add_translation_note` | Dodanie noty o tłumaczeniu                                                |
| `--note_position`        | Pozycja noty: `top`, `bottom` (domyślnie) lub `both` |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker` |
| `--include_model`        | Umieszczenie nazwy modelu w pliku wyjściowym                             |
| `--reasoning_effort`     | Poziom rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **Sześć flag providerów wzajemnie się wyklucza.** Wcześniej podanie dwóch
> było akceptowane bez ostrzeżenia i wybierany był pierwszy sprawdzany provider:
> tłumaczenie zlecone w ramach limitu subskrypcji (`--use_codex`, `--use_grok_cli`)
> mogło więc zostać rozliczone według użycia bez żadnego ostrzeżenia.
> `argparse` odrzuca teraz takie połączenie.

### Nota o tłumaczeniu: pozycje i formaty

Dzięki `--add_translation_note` translator może umieścić notę na górze, na dole albo w obu miejscach oraz wyświetlić ją jako zwykły tekst (zgodny wstecznie) lub w formacie `marker`, który może być przetwarzany przez plugin Markdown.

**Pozycja** (`--note_position`):

- `bottom` (domyślnie): nota na końcu pliku, tak jak dotychczas.
- `top`: nota wstawiana **po frontmatter YAML** (zgodność z Astro Content Collections, gray-matter itp.).
- `both`: nota wstawiana na górze ORAZ na dole (jedno wywołanie LLM, treść używana ponownie w obu miejscach).

**Format** (`--note_format`):

- `legacy` (domyślnie): pogrubiony akapit `**...**` — zachowanie całkowicie identyczne z v1.8, byte-for-byte. Zgodne z Hugo, GitHub, GitLab i każdym rendererem Markdown.
- `marker`: niewidoczna definicja referencji linku Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), po której następuje pogrubiony blockquote. Czytelne natywnie w GitHub/GitLab i możliwe do wykorzystania podczas buildu przez plugin remark po stronie Astro w celu utworzenia stylizowanego banera (zob. blog jls42.org).

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

### Modele domyślne (2026)

| Provider | Jakość (domyślnie)      | Ekonomiczny (`--eco`) |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Zalecenie dotyczące tłumaczeń long-form**: `--use_gemini` (domyślnie = `gemini-3.7-flash`) wiernie zachowuje strukturę markdown w przypadku alfabetów innych niż łaciński (PL, JA, ZH, AR, HI), również w trybie `--news`, w którym istotna jest zgodność placeholderów. Pomiar na tym README przetłumaczonym na język japoński: struktura identyczna jak w `gemini-3.1-pro-preview` (21 list, 18 bloków kodu, 13 linków HTML, 13 obrazów, wszystkie adresy URL zachowane) przy około 6-krotnie mniejszym opóźnieniu. OpenAI pozostaje domyślnym wyborem ze względu na zgodność wsteczną.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](LICENSE).

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-5.6-sol.**
