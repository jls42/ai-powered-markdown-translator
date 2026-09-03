# Tłumacz Markdown oparty na AI

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Luki w zabezpieczeniach"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Zduplikowane linie (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Liczba linii kodu"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Odznaka Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** i **Grok (xAI)** — przez API albo w ramach limitu subskrypcji ChatGPT (Codex) lub Grok, bez rozliczania za użycie.

Ten skrypt Python tłumaczy pliki Markdown z języka źródłowego na docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Najważniejsze funkcje

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI w ramach subskrypcji, bez rozliczania za użycie — Codex (ChatGPT) i Grok
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Tryb ekonomiczny**: Opcja `--eco` umożliwiająca korzystanie z szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów zależnymi od modelu
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: Opcja `--keep_filename` pozwalająca zachować oryginalną nazwę
- **Tryb News**: Opcja `--news` chroniąca angielskie cytaty i obsługująca flagi w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` z kluczami API
- **Nota tłumaczeniowa**: Opcjonalne dodawanie noty na końcu dokumentu

## Instalacja

### Korzystanie z narzędzia

```bash
pip install ai-powered-markdown-translator
```

Polecenie `aipmt` jest wtedy dostępne wszędzie. Jeśli katalog skryptów
Pythona nie znajduje się w zmiennej `PATH`, `python -m aipmt` robi dokładnie
to samo. Python 3.10 lub nowszy.

Aby zainstalować narzędzie w izolacji od pozostałych pakietów:

```bash
pipx install ai-powered-markdown-translator
```

### Współtworzenie projektu

Sklonowane repozytorium jest nadal potrzebne do programowania: znajdują się w nim testy,
28 tłumaczeń i całe oprzyrządowanie jakościowe.

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

Projekt korzysta z [`pre-commit`](https://pre-commit.com), aby uniemożliwić commitowanie źle sformatowanego kodu, podatności lub sekretu. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (zależności CVE), unittest. Szczegóły opisano w sekcji _Quality / pre-commit_ pliku `CLAUDE.md`.

## Konfiguracja

Klucze są wyszukiwane w **trzech miejscach**, od najbardziej do najmniej priorytetowego.
Każde kolejne uzupełnia tylko to, czego poprzednie nie dostarczyło.

|     | Gdzie                                            | Do czego                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                     | CI, kontenery, jednorazowe nadpisanie |
| 2   | `.env` bieżącego katalogu (lub katalogu nadrzędnego) | klucz właściwy dla projektu            |
| 3   | `~/.config/aipmt/.env`                        | **zainstalowany raz, obowiązuje wszędzie**   |

Po wykonaniu `pip install` najprostsze jest trzecie miejsce:

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

Plik ten respektuje `XDG_CONFIG_HOME`, gdy zmienna wskazuje ścieżkę bezwzględną
(w przeciwnym razie jest ignorowana, zgodnie ze specyfikacją), oraz `%APPDATA%`
w systemie Windows.

Drugie miejsce pozostaje przydatne, gdy repozytorium ma własny klucz: `.env` w katalogu głównym
ma wtedy pierwszeństwo przed konfiguracją użytkownika, bez jej modyfikowania. Zmienna
już zdefiniowana w środowisku ma pierwszeństwo przed oboma:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Jeśli nie znaleziono żadnego klucza, polecenie nie wyświetla śladu wywołania: wylicza
trzy lokalizacje wraz z ich dokładnymi ścieżkami.

`GEMINI_API_KEY` jest akceptowane jako alternatywa dla `GOOGLE_API_KEY` (konwencja AI
Studio). Zmienne opcjonalne: `XAI_BASE_URL` (endpoint xAI, domyślnie
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekundy na wywołanie Anthropic, domyślnie
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
oraz `GROK_TRANSLATE_SANDBOX` (zob. sekcję Grok CLI). Po stronie
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
OpenAI metoda tego zastosowania — tokeny `~/.codex/auth.json` nie uwierzytelniają
wywołań API Platform i zresztą nigdy nie są odczytywane przez ten skrypt.

**Wymagania wstępne:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binarne pliki są wyszukiwane w następującej kolejności: zmienna `CODEX_BIN`, `PATH`,
a następnie pakiet Python `openai-codex-cli-bin`. Ten ostatni celowo nie znajduje się w
`requirements.txt`: zajmuje około 250 MB, co narzucałoby się wszystkim użytkownikom
dla opcjonalnego providera.

**Warto wiedzieć:**

- **Nie jest używany żaden klucz API.** `OPENAI_API_KEY` i `CODEX_API_KEY` są
  usuwane ze środowiska podprocesu, co gwarantuje, że klucz obecny w `.env`
  nigdy nie przełączy tłumaczenia na rozliczanie za użycie.
- **Jeden segment = jedna „wiadomość lokalna”** w pięciogodzinnym oknie planu.
  Należy używać `--eco` (model `gpt-5.6-luna`, 250–2 000 wiadomości/5 h w planie Plus)
  zamiast modelu jakościowego (`gpt-5.6-sol`, 10–100 wiadomości/5 h).
- **Wolniej** niż wywołanie API: należy liczyć około 45 s na kompletny README, w porównaniu
  z kilkoma sekundami przy bezpośrednim użyciu.
- **Odrzucane w CI** (zdefiniowano `CI` lub `GITHUB_ACTIONS`): uwierzytelnianie
  subskrypcją nie jest przeznaczone dla współdzielonego runnera, a OpenAI odradza ten
  workflow w publicznych repozytoriach. Na tej ścieżce należy użyć klucza API.
- Zmienne środowiskowe: `CODEX_BIN` (jawna ścieżka do pliku binarnego) oraz
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

- Codex działa w `--sandbox read-only`, czyli w granicy narzuconej przez system.
- Sandbox Grok **nie może być stosowany** na wielu nowszych systemach Linux:
  AppArmor blokuje nieuprzywilejowane user namespaces od Ubuntu 24.04, a lista odmów
  dla gniazd środowiska uruchomieniowego kontenerów zawodzi, jeśli
  `/run/podman` ma wartość `0700`. Tymczasem **wbudowany** profil, którego
  nie można zastosować, uruchamia się **po cichu bez izolacji**.
- Skrypt nie żąda więc domyślnie żadnego profilu i **nigdy nie przechodzi po cichu**
  do trybu awaryjnego: wyświetla ostrzeżenie. Izolacja opiera się na regułach
  `--deny` CLI (w tym catch-all `*`), jedynej mierzalnej warstwie
  _fail-closed_ — nieznana reguła powoduje odmowę uruchomienia zamiast cichego
  usunięcia ochrony.
- Aby **wymusić** sandbox systemu operacyjnego: `GROK_TRANSLATE_SANDBOX=read-only`. Uruchomienie
  zakończy się niepowodzeniem, jeśli maszyna nie może go respektować, co jest
  zamierzonym zachowaniem.

**Limit**: pula Grok jest **tygodniowa i współdzielona** z Chat, Imagine i Voice,
a żadna komenda nie pozwala jej odczytać. Przetwarzanie wsadowe może więc zmniejszyć
limit rozmów bez żadnego ostrzeżenia — stąd współbieżność ograniczona do 2 oraz
ostrzeżenie w `regen_translations.sh`.

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

Korzysta z szybszych i tańszych modeli (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                   | Opis                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                                       |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                        |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                          |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                             |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                              |
| `--model`                | Model do użycia                                             |
| `--eco`                  | Używanie modeli ekonomicznych                                         |
| `--use_mistral`          | Używanie API Mistral AI                                                |
| `--use_claude`           | Używanie API Claude                                                    |
| `--use_gemini`           | Używanie API Gemini                                                    |
| `--use_codex`            | Używanie CLI Codex w ramach limitu subskrypcji ChatGPT               |
| `--use_grok`             | Używanie API xAI (Grok) — wymaga `XAI_API_KEY`                      |
| `--use_grok_cli`         | Używanie CLI Grok w ramach limitu subskrypcji Grok                   |
| `--force`                | Wymuszenie ponownego tłumaczenia                                                  |
| `--keep_filename`        | Zachowanie oryginalnej nazwy pliku                                     |
| `--news`                 | Tryb aktualności: chroni cytaty EN i obsługuje flagi według języka |
| `--add_translation_note` | Dodanie noty tłumaczeniowej                                           |
| `--note_position`        | Położenie noty: `top`, `bottom` (domyślnie) lub `both`                |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker`       |
| `--include_model`        | Dołączenie nazwy modelu do pliku wyjściowego                       |
| `--reasoning_effort`     | Wysiłek rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

> **Sześć flag providerów wyklucza się wzajemnie.** Wcześniej połączenie dwóch było
> po cichu akceptowane i rozstrzygane na rzecz pierwszej testowanej opcji: tłumaczenie
> żądane w ramach limitu subskrypcji (`--use_codex`, `--use_grok_cli`) mogło więc
> zostać rozliczone za użycie bez żadnego ostrzeżenia.
> `argparse` od teraz odrzuca takie połączenie.

### Nota tłumaczeniowa: położenia i formaty

Za pomocą `--add_translation_note` translator może umieścić notę na początku, na końcu lub
w obu miejscach, a także wygenerować ją jako zwykły tekst (dla zgodności wstecznej)
albo w formacie `marker`, obsługiwanym przez plugin Markdown.

**Położenie** (`--note_position`):

- `bottom` (domyślnie): nota na końcu pliku, tak jak dotychczas.
- `top`: nota wstawiona **po frontmatter YAML** (bezpieczeństwo Astro Content Collections, gray-matter itd.).
- `both`: nota wstawiona NA GÓRZE I NA DOLE (jedno wywołanie LLM, treść ponownie użyta w obu miejscach).

**Format** (`--note_format`):

- `legacy` (domyślnie): pogrubiony akapit `**...**` — zachowanie identyczne z v1.8, byte-for-byte. Zgodne z Hugo, GitHub, GitLab i każdym rendererem Markdown.
- `marker`: niewidoczna definicja referencji linku Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), po której następuje pogrubiony blockquote. Natywnie czytelne w GitHub/GitLab i możliwe do wykorzystania podczas builda przez plugin remark po stronie Astro w celu wygenerowania stylizowanego banera (zob. blog jls42.org).

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

| Provider | Jakość (domyślnie)       | Ekonomiczny (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Zalecenie dotyczące tłumaczeń długich form**: `--use_gemini` (domyślnie = `gemini-3.7-flash`) wiernie zachowuje strukturę markdown w skryptach używających alfabetów niełacińskich (PL, JA, ZH, AR, HI), także w trybie `--news`, w którym kluczowe jest zachowanie placeholderów. Zmierzono to na tym README przetłumaczonym na japoński: struktura identyczna jak w `gemini-3.1-pro-preview` (21 list, 18 bloków kodu, 13 linków HTML, 13 obrazów, wszystkie URL-e zachowane) przy około 6 razy mniejszym opóźnieniu. OpenAI pozostaje domyślne ze względu na zgodność wsteczną.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zob. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-5.6-luna.**
