# Tłumacz Markdown oparty na AI

🌍 [Francuski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Angielski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Hiszpański](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chiński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Niemiecki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japoński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreański](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Włoski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Niderlandzki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugalski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumuński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Szwedzki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Problemy z jakością kodu"></a>
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

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** i **Grok (xAI)** — przez API, w ramach limitu subskrypcji ChatGPT (Codex) lub Grok bez rozliczeń za użycie albo za pośrednictwem **OpenCode**, agenta open source, z wybranym przez użytkownika providerem: modelem lokalnym (Ollama), bezpłatnym, subskrypcyjnym (GitHub Copilot…) lub korzystającym z klucza.

Ten skrypt Python tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Wielu providerów**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI w ramach subskrypcji, bez rozliczeń za użycie — Codex (ChatGPT) i Grok — oraz OpenCode (open source, MIT) z dowolnym providerem skonfigurowanym w OpenCode, w tym modelem lokalnym
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Tryb ekonomiczny**: Opcja `--eco` umożliwiająca użycie szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` umożliwiająca przetłumaczenie jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów właściwymi dla poszczególnych modeli
- **Zachowanie kodu**: Zachowywane są zarówno bloki kodu, JAK I kod inline (`` `...` ``)
- **Nazwa pliku**: Opcja `--keep_filename` umożliwiająca zachowanie oryginalnej nazwy
- **Tryb wiadomości**: Opcja `--news` chroniąca angielskie cytaty i obsługująca flagi w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` zawierającego klucze API
- **Nota o tłumaczeniu**: Opcjonalne dodanie noty na końcu dokumentu

## Instalacja

### Aby korzystać z narzędzia

```bash
pip install ai-powered-markdown-translator
```

Polecenie `aipmt` jest odtąd dostępne wszędzie. Jeśli katalog skryptów
Python nie znajduje się w zmiennej `PATH`, polecenie `python -m aipmt` działa dokładnie
tak samo. Wymagany jest Python 3.10 lub nowszy.

Aby przeprowadzić instalację odizolowaną od pozostałych pakietów:

```bash
pipx install ai-powered-markdown-translator
```

### Aby współtworzyć projekt

Sklonowane repozytorium pozostaje niezbędne do prac rozwojowych: znajdują się w nim testy,
28 tłumaczeń oraz wszystkie narzędzia kontroli jakości.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` jest **w pełni przypiętym plikiem lock**, dokładnie odzwierciedlającym
przetestowane środowisko. Zakresy opublikowane w `pyproject.toml` są
celowo szersze: nie narzucają żadnych wymagań pozostałym pakietom użytkownika.

### Narzędzia kontroli jakości (opcjonalne, ale zalecane)

Projekt używa [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego, podatnego na ataki kodu lub kodu zawierającego sekret. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (CVE zależności), unittest. Szczegółowe informacje znajdują się w sekcji _Quality / pre-commit_ pliku `CLAUDE.md`.

## Konfiguracja

Klucze są wyszukiwane w **trzech miejscach**, od najwyższego do najniższego priorytetu.
Każde z nich uzupełnia wyłącznie wartości, których nie dostarczyło poprzednie.

|     | Gdzie                                            | Do czego                                      |
| --- | ----------------------------------------------- | --------------------------------------------- |
| 1   | Zmienne środowiskowe                             | CI, kontenery, jednorazowe nadpisanie         |
| 2   | `.env` w bieżącym katalogu (lub katalogu nadrzędnym) | klucz właściwy dla danego projektu            |
| 3   | `~/.config/aipmt/.env`                                  | **instalowany raz, działa wszędzie**           |

Po wykonaniu `pip install` najprostszym rozwiązaniem jest trzecia opcja:

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

Ten plik korzysta ze ścieżki `XDG_CONFIG_HOME`, gdy zmienna wskazuje ścieżkę bezwzględną
(w przeciwnym razie jest ignorowana, zgodnie ze specyfikacją), oraz ze ścieżki `%APPDATA%`
w systemie Windows.

Druga opcja pozostaje przydatna, gdy repozytorium ma własny klucz: plik `.env` w jego katalogu głównym
ma wtedy pierwszeństwo przed konfiguracją użytkownika, nie zmieniając jej. Z kolei
zmienna już zdefiniowana w środowisku ma pierwszeństwo przed obiema opcjami:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Jeśli nie znaleziono żadnego klucza, polecenie nie wyświetla śladu wywołania:
wymienia trzy lokalizacje wraz z ich dokładnymi ścieżkami.

`GEMINI_API_KEY` jest akceptowane jako alternatywa dla `GOOGLE_API_KEY` (konwencja AI
Studio). Zmienne opcjonalne: `XAI_BASE_URL` (endpoint xAI, domyślnie
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (liczba sekund na wywołanie Anthropic, domyślnie
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (zobacz sekcję Grok CLI) oraz `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (zobacz sekcję OpenCode). Dla
`regen_translations.sh`: `REGEN_PROVIDER` (domyślnie `codex`, w ramach subskrypcji),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (obowiązkowe nadpisanie dla płatnego API)
oraz `REGEN_JOB_TIMEOUT` (limit na zadanie, domyślnie 600 s, 1 800 s w Codex).

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Tłumaczenie w ramach subskrypcji ChatGPT (`--use_codex`)

Ten provider nie używa żadnego klucza API: steruje oficjalnym CLI Codex w trybie
nieinteraktywnym, dzięki czemu tłumaczenie jest rozliczane w ramach limitu już opłaconej
subskrypcji ChatGPT (Plus, Pro, Business…). Jest to jedyna udokumentowana przez
OpenAI metoda takiego użycia — tokeny `~/.codex/auth.json` nie uwierzytelniają
wywołań API Platform, a ten skrypt nigdy ich nawet nie odczytuje.

**Wymagania wstępne:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Plik wykonywalny jest wyszukiwany w następującej kolejności: zmienna `CODEX_BIN`, zmienna `PATH`,
a następnie pakiet Python `openai-codex-cli-bin`. Ten ostatni celowo nie znajduje się
w `requirements.txt`: zajmuje około 250 MB, co obciążałoby wszystkich
użytkowników ze względu na opcjonalny provider.

**Warto wiedzieć:**

- **Nie jest używany żaden klucz API.** Zmienne `OPENAI_API_KEY` i `CODEX_API_KEY` są
  usuwane ze środowiska podprocesu, co gwarantuje, że klucz obecny
  w `.env` nigdy nie przełączy tłumaczenia na rozliczanie za użycie.
- **Jeden segment = jedna „lokalna wiadomość”** w pięciogodzinnym oknie planu.
  Używaj `--eco` (model `gpt-5.6-luna`, 250–2 000 wiadomości/5 h w planie Plus)
  zamiast modelu jakościowego (`gpt-5.6-sol`, 10–100 wiadomości/5 h).
- **Wolniej** niż bezpośrednie wywołanie API: pełny plik README zajmuje około 45 s,
  zamiast kilku sekund przy połączeniu bezpośrednim.
- **Niedozwolone w CI** (zdefiniowane `CI` lub `GITHUB_ACTIONS`): uwierzytelnianie
  za pomocą subskrypcji nie jest przeznaczone dla współdzielonego runnera, a OpenAI odradza taki
  workflow w publicznych repozytoriach. W tym przypadku należy użyć klucza API.
- Zmienne środowiskowe: `CODEX_BIN` (jawna ścieżka do pliku wykonywalnego) oraz
  `CODEX_TIMEOUT` (liczba sekund na segment, domyślnie `600`).

### Tłumaczenie w ramach subskrypcji Grok (`--use_grok_cli`)

Ta sama zasada co w przypadku `--use_codex`, z oficjalnym CLI **Grok Build**:
tłumaczenie jest rozliczane w ramach subskrypcji Grok (SuperGrok / X Premium+), zamiast
według liczby tokenów.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolacja — przeczytaj przed użyciem.** Ten provider jest z założenia **słabiej
zabezpieczony** niż `--use_codex` i jest to świadoma decyzja:

- Codex działa w `--sandbox read-only`, granicy narzuconej przez system.
- Sandbox Grok **nie może zostać zastosowany** na wielu nowszych komputerach z Linux:
  AppArmor blokuje nieuprzywilejowane przestrzenie nazw użytkownika od Ubuntu
  24.04, a lista odmowy dla socketów środowiska uruchomieniowego kontenerów zawodzi, jeśli
  `/run/podman` znajduje się w `0700`. Natomiast **wbudowany** profil, którego
  nie można zastosować, uruchamia proces **bez izolacji i bez ostrzeżenia**.
- Dlatego skrypt domyślnie nie wymaga żadnego profilu i **nigdy nie przechodzi
  po cichu do trybu awaryjnego**: wyświetla ostrzeżenie. Izolacja opiera się na
  regułach `--deny` CLI (w tym catch-all `*`), czyli jedynej zweryfikowanej
  warstwie działającej zgodnie z zasadą _fail-closed_ — nieznana reguła powoduje odmowę uruchomienia,
  zamiast wyłączenia ochrony bez powiadomienia.
- Aby **wymusić** sandbox systemu operacyjnego: `GROK_TRANSLATE_SANDBOX=read-only`.
  Uruchomienie zakończy się niepowodzeniem, jeśli komputer nie będzie w stanie go zastosować,
  co jest zamierzonym zachowaniem.

**Limit**: pula Grok jest **tygodniowa i współdzielona** z Chat, Imagine oraz
Voice, a żadne polecenie nie pozwala jej odczytać. Przetwarzanie wsadowe może więc
ograniczyć twoje użycie konwersacyjne bez żadnego ostrzeżenia — stąd
współbieżność ograniczona do 2 i ostrzeżenie w `regen_translations.sh`.

Pozostałe zmienne: `GROK_BIN` (ścieżka do pliku wykonywalnego), `GROK_TIMEOUT` (domyślnie 900 s).

Aby ponownie wygenerować 28 tłumaczeń:

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

### Tłumaczenie za pomocą OpenCode z wybranym providerem (`--use_opencode`)

[OpenCode](https://opencode.ai) to działający w terminalu agent do kodowania **open source (MIT)**.
Nie jest providerem modeli, lecz **routerem** do providerów
skonfigurowanych w samym OpenCode: klucza API, subskrypcji
(GitHub Copilot, ChatGPT, SuperGrok), bramy OpenCode Zen — udostępniającej
bezpłatne modele **bez konta** — albo modelu **lokalnego** (Ollama, LM Studio,
llama.cpp). Ten provider steruje `opencode run` w trybie nieinteraktywnym i ogranicza
wywołanie do pojedynczej wymiany, bez żadnych narzędzi.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` jest **obowiązkowe** i musi mieć format `provider/modèle`. OpenCode nie jest
providerem i żaden domyślny model nie zostanie wybrany za użytkownika: jego własnym rozwiązaniem
awaryjnym byłby bezpłatny model, którego konwersacje mogą być wykorzystywane do trenowania.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Izolacja — działania wykonywane przez skrypt przy każdym wywołaniu:**

- Konfiguracja inline (`OPENCODE_CONFIG_CONTENT`), mająca pierwszeństwo przed
  konfiguracją użytkownika, definiuje agenta `aipmt`, któremu **odmówiono dostępu do wszystkich narzędzi**
  (`permission: { "*": "deny" }`): model nie może odczytywać ani zapisywać plików czy
  uruchamiać poleceń — pomiary wykazały, że nawet tego nie próbuje. Udostępnianie sesji
  jest wyłączone, `--pure` wyklucza zewnętrzne pluginy, nigdy `--auto`.
- Wywołanie działa w **tymczasowym, pustym katalogu**, z przełącznikami
  `OPENCODE_DISABLE_PROJECT_CONFIG` i `OPENCODE_DISABLE_CLAUDE_CODE`: bez
  nich OpenCode wstrzykuje do każdego promptu plik `AGENTS.md` z bieżącego katalogu
  oraz plik `~/.claude/CLAUDE.md` użytkownika — pomiary wykazały, że instrukcja „kończ każdą odpowiedź
  słowem BANANA” umieszczona w `AGENTS.md` była stosowana podczas tłumaczenia.
  Globalne reguły `~/.config/opencode/AGENTS.md` nadal jednak obowiązują:
  OpenCode nie pozwala ich pominąć.
- Kontrakt wyjściowy wymaga jednocześnie: kodu powrotu 0, braku zdarzeń
  `error`, braku wywołań narzędzi, ostatniego kroku zakończonego jako `stop`, niepustego
  tekstu oraz faktycznego załadowania agenta — nieznany `--agent` nie powoduje
  błędu OpenCode, lecz **po cichu przełącza go** na agenta kodującego z aktywnymi
  narzędziami. `exit 0` również niczego tutaj nie dowodzi.
- **Żaden klucz aipmt nie jest przekazywany** do podprocesu (to samo filtrowanie
  co w przypadku Codex i Grok), z jednym wyraźnie wskazanym wyjątkiem: `OPENCODE_API_KEY`,
  czyli kluczem samego OpenCode (Zen, Go). Providerów konfiguruje się
  w OpenCode (`opencode auth login`, `opencode.json`), a nie w pliku `.env` narzędzia aipmt.

**Warto wiedzieć:**

- **Bezpłatne modele Zen są modelami „stealth” lub pochodzącymi od współtwórców**,
  zmieniają się, mają nieudokumentowane limity, a ich konwersacje mogą być wykorzystywane
  do trenowania: świetnie nadają się do publicznej dokumentacji, ale należy ich unikać w przypadku
  treści prywatnych. Pomiary: `opencode/mimo-v2.5-free` tłumaczy ten plik README w jednym
  przebiegu; `opencode/big-pickle` działa wolniej, a dwa jednoczesne żądania pozostały
  bez odpowiedzi.
- **Model lokalny musi obsługiwać co najmniej 16 k kontekstu** — segmenty mają
  do 16 000 znaków — podczas gdy Ollama często ustawia domyślnie 4 096.
  Z Ollama: plik `Modelfile` zawierający `PARAMETER num_ctx 32768`, a następnie
  `ollama create`. Jakość zależy od modelu: model 7B odwrócił kolejność listy i
  uszkodził zamknięcie bloku kodu w pliku testowym, podczas gdy model
  dostępny przez bramę zachował wszystko.
- `--eco` nie ma wpływu (używany jest model z `--model`);
  `--reasoning_effort` jest przekazywane bez zmian jako `--variant` OpenCode i należy
  je podawać tylko wtedy, gdy model je obsługuje.
- Sesje są rejestrowane przez OpenCode w jego bazie
  (`~/.local/share/opencode/`), tak jak każda sesja OpenCode.
- Zmienne środowiskowe: `OPENCODE_BIN` (jawna ścieżka do pliku wykonywalnego,
  w przeciwnym razie `PATH`, a następnie `~/.opencode/bin/opencode`) oraz `OPENCODE_TIMEOUT`
  (liczba sekund na segment, domyślnie `600`). `OPENCODE_CONFIG` jest respektowane,
  jeśli zostanie wyeksportowane.

**Przykład z pomiarami: model lokalny przez Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

Następnie provider w `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` nie jest drobnym szczegółem: Ollama domyślnie włącza rozumowanie
w Gemma 4 i Qwen 3.5, a Modelfile nie może go wyłączyć. Pomiar przez
OpenCode: bez tej opcji zdanie „Kot śpi na dywanie” zużywa 919 tokenów
rozumowania i zajmuje 68 s; z nią — 9 tokenów.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Wyniki dla rzeczywistego artykułu na blogu liczącego 589 wierszy (140 linków, 21 sekcji,
3 angielskie cytaty chronione przez tryb `--news`), to samo polecenie, trzy
modele:

| Model                                    | Czas         | Struktura                                                    | Odstępstwa                                                                                  |
| ---------------------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, bezpłatny)         | 4 min 26 s   | identyczna ze źródłem                                        | brak                                                                                        |
| `ollama/gemma4-12b-32k` (lokalny)                | 10 min 10 s  | linki, URL, tabele, tagi, pogrubienia i kod inline identyczne | jeden zmyślony wiersz cytatu (🇺🇸 + parafraza), jedno zduplikowane przypisanie autorstwa      |
| `ollama/qwen3.5-9b-32k` (lokalny)                | 8 min 18 s   | linki, URL, tabele i tagi identyczne                          | jeden zmyślony wiersz cytatu, kilka dodanych pogrubień i fragmentów kodu inline, jeden segment przetworzony ponownie |

Podczas tłumaczenia lokalnego: obciążenie GPU 98% i 170 W, zajęte 10 GB VRAM
(model i cache 32 k tokenów, bez przenoszenia czegokolwiek do RAM), 7,5 GB RAM dla
serwera Ollama. Model mający od 9 do 12 miliardów parametrów zachowuje
strukturę, ale pozwala sobie na jedną dowolną zmianę w każdym artykule, podczas gdy model dostępny przez bramę
nie wprowadził żadnej: przed publikacją należy wszystko sprawdzić lub używać go wyłącznie do wersji roboczych.

### Tryb ekonomiczny

Używa szybszych i tańszych modeli (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opcje

| Opcja                   | Opis                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                                                                            |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                                                             |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                                                               |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                                                                  |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                                                                   |
| `--model`                | Konkretny model do użycia                                                                                  |
| `--eco`                  | Użyj modeli ekonomicznych                                                                              |
| `--use_mistral`          | Użyj API Mistral AI                                                                                     |
| `--use_claude`           | Użyj API Claude                                                                                         |
| `--use_gemini`           | Użyj API Gemini                                                                                         |
| `--use_codex`            | Użyj CLI Codex w ramach limitu subskrypcji ChatGPT                                                    |
| `--use_grok`             | Użyj API xAI (Grok) — wymaga `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Użyj CLI Grok w ramach limitu subskrypcji Grok                                                        |
| `--use_opencode`         | Użyj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle` |
| `--force`                | Wymuś ponowne tłumaczenie                                                                                       |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                                                          |
| `--news`                 | Tryb aktualności: chroni cytaty w języku angielskim, obsługuje flagi według języka                                      |
| `--add_translation_note` | Dodaj notę o tłumaczeniu                                                                                |
| `--note_position`        | Położenie noty: `top`, `bottom` (domyślnie) lub `both`                                                     |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                                            |
| `--include_model`        | Uwzględnij nazwę modelu w pliku wyjściowym                                                            |
| `--reasoning_effort`     | Poziom wnioskowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **Siedem flag dostawców wzajemnie się wyklucza.** Wcześniej połączenie dwóch
> było po cichu akceptowane i wybierana była pierwsza sprawdzana opcja: tłumaczenie
> zlecone w ramach limitu subskrypcji (`--use_codex`, `--use_grok_cli`)
> mogło więc bez żadnego ostrzeżenia zostać rozliczone według użycia.
> `argparse` odrzuca teraz taką kombinację.

### Nota o tłumaczeniu: położenia i formaty

Za pomocą `--add_translation_note` translator może umieścić notę na górze, na dole albo w obu miejscach oraz sformatować ją jako zwykły tekst (zgodny wstecznie) lub jako format `marker` obsługiwany przez plugin Markdown.

**Położenie** (`--note_position`):

- `bottom` (domyślnie): nota na końcu pliku, jak dotychczas.
- `top`: nota wstawiona **po frontmatter YAML** (bezpieczne dla Astro Content Collections, gray-matter itp.).
- `both`: nota wstawiona na górze ORAZ na dole (jedno wywołanie LLM, treść używana ponownie w obu miejscach).

**Format** (`--note_format`):

- `legacy` (domyślnie): pogrubiony akapit `**...**` — zachowanie dokładnie takie samo jak w wersji v1.8, bajt po bajcie. Zgodny z Hugo, GitHub, GitLab i każdym rendererem Markdown.
- `marker`: niewidoczna definicja odwołania do linku Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), po której następuje pogrubiony blockquote. Czytelna natywnie w GitHub/GitLab i możliwa do wykorzystania podczas buildu przez plugin remark po stronie Astro w celu utworzenia stylizowanego banera (zob. blog jls42.org).

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

| Dostawca | Jakość (domyślnie)                      | Ekonomiczny (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | wymagany `--model provider/modèle` | tak samo — `--eco` bez efektu |

> **Zalecenie dotyczące tłumaczeń długich tekstów**: `--use_gemini` (domyślnie = `gemini-3.7-flash`) wiernie zachowuje strukturę Markdown w przypadku skryptów innych niż łaciński (PL, JA, ZH, AR, HI), również w trybie `--news`, w którym liczy się wierne zachowanie placeholderów. Pomiar na tym pliku README przetłumaczonym na język japoński: struktura identyczna jak w przypadku `gemini-3.1-pro-preview` (21 list, 18 bloków kodu, 13 linków HTML, 13 obrazów, wszystkie adresy URL zachowane) przy około 6-krotnie mniejszym opóźnieniu. OpenAI pozostaje domyślnym wyborem ze względu na zgodność wsteczną.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE wersja 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-5.6-sol.**
