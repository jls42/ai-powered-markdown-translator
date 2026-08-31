# Tłumacz Markdown wspierany przez AI

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena łatwości utrzymania"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Podatności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Zapachy kodu"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Zduplikowane wiersze (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Liczba wierszy kodu"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Odznaka Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Python tłumaczy pliki Markdown z języka źródłowego na docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Najważniejsze funkcje

- **Multi-Provider**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini) + CLI Codex w ramach subskrypcji ChatGPT
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Tryb ekonomiczny**: Opcja `--eco` do używania szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów zależnymi od modelu
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: Opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Tryb News**: Opcja `--news` do ochrony angielskich cytatów i obsługi flag w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` dla kluczy API
- **Nota tłumaczeniowa**: Opcjonalne dodanie noty na końcu dokumentu

## Instalacja

### Korzystanie z narzędzia

```bash
pip install ai-powered-markdown-translator
```

Polecenie `aipmt` jest wtedy dostępne globalnie. Jeśli katalog skryptów
Pythona nie znajduje się w zmiennej `PATH`, polecenie `python -m aipmt` robi dokładnie
to samo. Python 3.10 lub nowszy.

Aby zainstalować narzędzie w izolacji od pozostałych pakietów:

```bash
pipx install ai-powered-markdown-translator
```

### Współtworzenie projektu

Sklonowane repozytorium jest nadal potrzebne do pracy nad projektem: znajdują się
w nim testy, 28 tłumaczeń i całe oprzyrządowanie jakościowe.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` to **w pełni przypięty lock**, będący dokładnym odzwierciedleniem
testowanego środowiska. Ograniczenia opublikowane w `pyproject.toml` są
celowo szersze: nie narzucają niczego pozostałym pakietom.

### Narzędzia jakościowe (opcjonalne, ale zalecane)

Projekt wykorzystuje [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego kodu, podatności lub sekretu. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (zależności CVE), unittest. Szczegóły znajdują się w sekcji _Quality / pre-commit_ pliku `CLAUDE.md`.

## Konfiguracja

Utwórz plik `.env` **w katalogu, z którego uruchamiasz
polecenie** (jest wyszukiwany tam, a następnie w katalogach nadrzędnych) albo
zdefiniuj zmienne środowiskowe:

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
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekundy na wywołanie Anthropic, domyślnie
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
oraz `GROK_TRANSLATE_SANDBOX` (zobacz sekcję Grok CLI). Po stronie
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` i
`REGEN_JOB_TIMEOUT` (limit na zadanie, domyślnie 600 s).

## Użycie

### Tłumaczenie pojedynczego pliku

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tłumaczenie katalogu

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

### Tłumaczenie w ramach subskrypcji ChatGPT (`--use_codex`)

Ten provider nie zużywa żadnego klucza API: steruje oficjalnym CLI Codex w trybie
nieinteraktywnym, więc tłumaczenie jest odejmowane od już opłaconego limitu
subskrypcji ChatGPT (Plus, Pro, Business…). Jest to jedyna udokumentowana przez
OpenAI droga do tego zastosowania — tokeny z `~/.codex/auth.json` nie uwierzytelniają
wywołań API Platform i zresztą nigdy nie są odczytywane przez ten skrypt.

**Wymagania wstępne:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Plik binarny jest wyszukiwany w następującej kolejności: zmienna `CODEX_BIN`, `PATH`,
a następnie pakiet Python `openai-codex-cli-bin`. Ten ostatni celowo nie znajduje się w
`requirements.txt`: zajmuje około 250 MB, co byłoby narzucone wszystkim
użytkownikom w przypadku opcjonalnego providera.

**Warto wiedzieć:**

- **Nie jest używany żaden klucz API.** `OPENAI_API_KEY` i `CODEX_API_KEY` są
  usuwane ze środowiska podprocesu, co gwarantuje, że klucz obecny w `.env`
  nigdy nie przełączy tłumaczenia na rozliczanie za użycie.
- **Jeden segment = jedna „lokalna wiadomość”** w pięciogodzinnym oknie planu.
  Używaj `--eco` (model `gpt-5.6-luna`, 250–2 000 wiadomości/5 h w Plus)
  zamiast modelu jakościowego (`gpt-5.6-sol`, 10–100 wiadomości/5 h).
- **Wolniejsze** niż wywołanie API: pełny README zajmuje około 45 s, w porównaniu
  z kilkoma sekundami przy bezpośrednim użyciu API.
- **Odrzucane w CI** (`CI` lub `GITHUB_ACTIONS` jest zdefiniowane): uwierzytelnianie
  przez subskrypcję nie jest przeznaczone dla współdzielonego runnera, a OpenAI odradza
  ten workflow w publicznych repozytoriach. Na tej ścieżce użyj klucza API.
- Zmienne środowiskowe: `CODEX_BIN` (jawna ścieżka do pliku binarnego) i
  `CODEX_TIMEOUT` (sekundy na segment, domyślnie `600`).

### Tłumaczenie w ramach subskrypcji Grok (`--use_grok_cli`)

Ta sama zasada co w przypadku `--use_codex`, z oficjalnym CLI **Grok Build**:
tłumaczenie jest odejmowane od subskrypcji Grok (SuperGrok / X Premium+), zamiast
być rozliczane za token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolacja — przeczytaj przed użyciem.** Ten provider jest strukturalnie **słabszy**
niż `--use_codex` i jest to zamierzone:

- Codex działa w `--sandbox read-only`, czyli granicy narzuconej przez system.
- Sandbox Grok **nie może działać** na wielu nowszych systemach Linux: AppArmor
  blokuje nieuprzywilejowane user namespaces od Ubuntu 24.04, a lista blokad gniazd
  środowiska uruchomieniowego kontenerów zawodzi, jeśli `/run/podman` jest w
  `0700`. Tymczasem **zintegrowany** profil, którego nie można zastosować,
  uruchamia się **bez izolacji i po cichu**.
- Skrypt nie żąda więc domyślnie żadnego profilu i **nigdy nie przełącza się
  po cichu**: wyświetla ostrzeżenie. Izolacja opiera się na regułach `--deny`
  CLI (w tym na regule catch-all `*`), jedynej mierzonej warstwie
  _fail-closed_ — nieznana reguła powoduje odmowę uruchomienia zamiast usunięcia
  ochrony bez informowania użytkownika.
- Aby **wymusić** sandbox systemu operacyjnego: `GROK_TRANSLATE_SANDBOX=read-only`. Uruchomienie
  nie powiedzie się, jeśli maszyna nie może go zagwarantować, i jest to zamierzone
  zachowanie.

**Limit**: pula Grok jest **tygodniowa i współdzielona** z Chat, Imagine i
Voice, a żadna komenda nie pozwala jej odczytać. Przetwarzanie wsadowe może więc
zmniejszyć twój limit rozmów, nie sygnalizując tego w żaden sposób — stąd
ograniczenie współbieżności do 2 i ostrzeżenie w `regen_translations.sh`.

Pozostałe zmienne: `GROK_BIN` (ścieżka do pliku binarnego), `GROK_TIMEOUT` (domyślnie 900 s).

Aby ponownie wygenerować 28 tłumaczeń:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Tryb ekonomiczny

Używa szybszych i tańszych modeli (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                   | Opis                                                                    |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                            |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                             |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                           |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                              |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                               |
| `--model`                | Model, którego należy użyć                                              |
| `--eco`                  | Używanie modeli ekonomicznych                                           |
| `--use_mistral`          | Używanie API Mistral AI                                                 |
| `--use_claude`                  | Używanie API Claude                                                     |
| `--use_gemini`          | Używanie API Gemini                                                     |
| `--use_codex`            | Używanie CLI Codex w ramach limitu subskrypcji ChatGPT                 |
| `--use_grok`             | Używanie API xAI (Grok) — wymaga `XAI_API_KEY`                         |
| `--use_grok_cli`         | Używanie CLI Grok w ramach limitu subskrypcji Grok                       |
| `--force`                | Wymuszenie ponownego tłumaczenia                                        |
| `--keep_filename`        | Zachowanie oryginalnej nazwy pliku                                      |
| `--news`                 | Tryb wiadomości: chroni cytaty EN, obsługuje flagi według języka         |
| `--add_translation_note` | Dodanie noty tłumaczeniowej                                           |
| `--note_position`        | Pozycja noty: `top`, `bottom` (domyślnie) lub `both` |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker` |
| `--include_model`        | Uwzględnienie nazwy modelu w pliku wyjściowym                           |
| `--reasoning_effort`     | Wysiłek rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **Sześć flag providerów wzajemnie się wyklucza.** Wcześniej połączenie dwóch
> flag było po cichu akceptowane i wybierany był pierwszy sprawdzany provider:
> tłumaczenie zażądane w ramach limitu subskrypcji (`--use_codex`, `--use_grok_cli`)
> mogło więc zostać rozliczone za użycie bez żadnego ostrzeżenia.
> `argparse` od tej pory odrzuca takie połączenie.

### Nota tłumaczeniowa: pozycje i formaty

Za pomocą `--add_translation_note` translator może umieścić notę na początku, na końcu
lub w obu miejscach, a także wygenerować ją jako zwykły tekst (wstecznie
kompatybilny) albo jako format `marker` obsługiwany przez plugin Markdown.

**Pozycja** (`--note_position`):

- `bottom` (domyślnie): nota na końcu pliku, tak jak wcześniej.
- `top`: nota wstawiona **po frontmatter YAML** (bezpieczeństwo Astro Content Collections, gray-matter itd.).
- `both`: nota wstawiona NA GÓRZE i NA DOLE (jedno wywołanie LLM, treść ponownie użyta w obu miejscach).

**Format** (`--note_format`):

- `legacy` (domyślnie): pogrubiony akapit `**...**` — zachowanie identyczne z v1.8, bajt w bajt. Kompatybilne z Hugo, GitHub, GitLab i każdym rendererem Markdown.
- `marker`: niewidoczna definicja referencji linku Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), po której następuje pogrubiony blockquote. Natywnie czytelne w GitHub/GitLab i możliwe do wykorzystania podczas budowania przez plugin remark po stronie Astro w celu utworzenia stylizowanego banera (zob. blog jls42.org).

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

### Modele domyślne (2026)

| Provider | Jakość (domyślna) | Ekonomiczny (`--eco`) |
| -------- | ----------------- | ----------------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Zalecenie dotyczące długich tłumaczeń**: `--use_gemini` (domyślnie = `gemini-3.7-flash`) wiernie zachowuje strukturę Markdown w skryptach używających alfabetów innych niż łaciński (PL, JA, ZH, AR, HI), także w trybie `--news`, w którym kluczowe jest zachowanie placeholderów. Zmierzono na tym README przetłumaczonym na japoński: struktura identyczna jak w `gemini-3.1-pro-preview` (21 list, 18 bloków kodu, 13 linków HTML, 13 obrazów, wszystkie adresy URL zachowane), przy około 6 razy mniejszym opóźnieniu. OpenAI pozostaje domyślnym wyborem ze względu na kompatybilność wsteczną.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-5.6-luna.**
