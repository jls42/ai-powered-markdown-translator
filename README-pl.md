# Tłumacz Markdown oparty na AI

🌍 [Francuski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Angielski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Hiszpański](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chiński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Niemiecki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japoński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreański](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Włoski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Niderlandzki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugalski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumuński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Szwedzki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Stan Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena łatwości utrzymania"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Podatności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Nieprawidłowości w kodzie"></a>
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

Tłumacz plików Markdown korzystający z **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** i **Grok (xAI)** — przez API, w ramach limitu subskrypcji ChatGPT (Codex) lub Grok bez opłat za użycie albo za pośrednictwem **OpenCode**, agenta open source, z wybranym dostawcą: modelem lokalnym (Ollama), bezpłatnym, subskrypcyjnym (GitHub Copilot…) lub dostępnym za pomocą klucza.

Ten skrypt Python tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Najważniejsze funkcje

- **Wielu dostawców**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI działające w ramach subskrypcji, bez opłat za użycie — Codex (ChatGPT) i Grok — + OpenCode (open source, MIT) obsługujący dowolnego dostawcę skonfigurowanego w OpenCode, w tym model lokalny
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Tryb ekonomiczny**: Opcja `--eco` umożliwiająca korzystanie z szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` umożliwiająca przetłumaczenie pojedynczego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów zależnymi od modelu
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) pozostają niezmienione
- **Nazwa pliku**: Opcja `--keep_filename` umożliwiająca zachowanie oryginalnej nazwy
- **Tryb wiadomości**: Opcja `--news` chroniąca angielskie cytaty i obsługująca flagi w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` na klucze API
- **Notatka o tłumaczeniu**: Opcjonalne dodanie notatki na końcu dokumentu

## Instalacja

### Aby korzystać z narzędzia

```bash
pip install ai-powered-markdown-translator
```

Polecenie `aipmt` jest wówczas dostępne wszędzie. Jeśli katalog skryptów
Python nie znajduje się w Twojej zmiennej `PATH`, `python -m aipmt` robi dokładnie to
samo. Wymagany jest Python 3.10 lub nowszy.

Aby przeprowadzić instalację odizolowaną od pozostałych pakietów:

```bash
pipx install ai-powered-markdown-translator
```

### Aby współtworzyć projekt

Sklonowane repozytorium pozostaje niezbędne do pracy nad projektem: znajdują się w nim testy,
28 tłumaczeń oraz wszystkie narzędzia do kontroli jakości.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` jest **w pełni przypiętym plikiem lock**, dokładnie odzwierciedlającym
przetestowane środowisko. Zakresy opublikowane w `pyproject.toml` są
celowo szersze: nie narzucają żadnych ograniczeń pozostałym pakietom.

### Narzędzia do kontroli jakości (opcjonalne, ale zalecane)

Projekt korzysta z [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego lub podatnego kodu oraz kodu zawierającego dane poufne. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (CVE zależności), unittest. Szczegółowe informacje znajdziesz w `CLAUDE.md`, w sekcji _Jakość / pre-commit_.

## Konfiguracja

Klucze są wyszukiwane w **trzech miejscach**, od najwyższego do najniższego priorytetu.
Każde z nich uzupełnia jedynie wartości pozostawione puste przez poprzednie.

|     | Gdzie                                            | Zastosowanie                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                     | CI, kontenery, jednorazowe nadpisanie |
| 2   | `.env` w bieżącym katalogu (lub katalogu nadrzędnym) | klucz właściwy dla projektu            |
| 3   | `~/.config/aipmt/.env`                        | **instalowany raz, działa wszędzie**   |

Najprostszym rozwiązaniem po `pip install` jest trzecia opcja:

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

Ten plik uwzględnia `XDG_CONFIG_HOME`, gdy zmienna wskazuje ścieżkę bezwzględną
(w przeciwnym razie jest ignorowana, zgodnie ze specyfikacją), oraz `%APPDATA%`
w systemie Windows.

Druga opcja pozostaje przydatna, gdy repozytorium ma własny klucz: plik `.env` w jego katalogu głównym
ma wtedy pierwszeństwo przed konfiguracją użytkownika, nie zmieniając jej. Z kolei
zmienna już zdefiniowana w środowisku ma pierwszeństwo przed obiema opcjami:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Jeśli nie zostanie znaleziony żaden klucz, polecenie nie wyświetla śladu wywołania:
wymienia trzy lokalizacje wraz z ich dokładnymi ścieżkami.

`GEMINI_API_KEY` jest akceptowany jako alternatywa dla `GOOGLE_API_KEY` (konwencja AI
Studio). Zmienne opcjonalne: `XAI_BASE_URL` (endpoint xAI, domyślnie
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (liczba sekund na wywołanie Anthropic, domyślnie
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (zobacz sekcję Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (zobacz sekcję OpenCode) oraz `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (zobacz sekcję
OpenRouter). Po stronie
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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Tłumaczenie w ramach subskrypcji ChatGPT (`--use_codex`)

Ten dostawca nie używa żadnego klucza API: steruje oficjalnym CLI Codex w trybie
nieinteraktywnym, dlatego tłumaczenie jest rozliczane w ramach limitu już opłaconej
subskrypcji ChatGPT (Plus, Pro, Business…). Jest to jedyna metoda udokumentowana przez
OpenAI dla tego zastosowania — tokeny `~/.codex/auth.json` nie uwierzytelniają
wywołań API Platform i ten skrypt nigdy ich nie odczytuje.

**Wymagania wstępne:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Plik wykonywalny jest wyszukiwany w następującej kolejności: zmienna `CODEX_BIN`, wartość `PATH`,
a następnie pakiet Python `openai-codex-cli-bin`. Ten ostatni celowo nie znajduje się
w `requirements.txt`: zajmuje około 250 MB, co obciążałoby wszystkich
użytkowników ze względu na opcjonalnego dostawcę.

**Warto wiedzieć:**

- **Żaden klucz API nie jest używany.** `OPENAI_API_KEY` i `CODEX_API_KEY` są
  usuwane ze środowiska podprocesu, co gwarantuje, że klucz
  obecny w `.env` nigdy nie spowoduje przełączenia tłumaczenia na rozliczanie
  według użycia.
- **Jeden segment = jedna „wiadomość lokalna”** w 5-godzinnym oknie planu.
  Używaj `--eco` (model `gpt-5.6-luna`, 250–2 000 wiadomości/5 h w Plus)
  zamiast modelu jakościowego (`gpt-5.6-sol`, 10–100 wiadomości/5 h).
- **Wolniej** niż bezpośrednie wywołanie API: pełny README zajmuje około 45 s zamiast
  kilku sekund.
- **Niedostępne w CI** (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): subskrypcja
  uwierzytelnia się za pomocą osobistego pliku sesji, a przeniesienie go na współdzielony runner
  oznacza umieszczenie tam tożsamości wielokrotnego użytku, dostępnej dla wszystkiego, co jest
  na nim wykonywane. W takim przypadku użyj klucza API.
- Zmienne środowiskowe: `CODEX_BIN` (jawna ścieżka do pliku wykonywalnego) oraz
  `CODEX_TIMEOUT` (liczba sekund na segment, domyślnie `600`).

### Tłumaczenie w ramach subskrypcji Grok (`--use_grok_cli`)

Zasada jest taka sama jak w przypadku `--use_codex`, z wykorzystaniem oficjalnego CLI **Grok Build**:
tłumaczenie jest rozliczane w ramach subskrypcji Grok (SuperGrok / X Premium+), zamiast
według liczby tokenów.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolacja — przeczytaj przed użyciem.** Ten dostawca jest z założenia **słabiej
zabezpieczony** niż `--use_codex` i jest to świadoma decyzja:

- Codex działa w `--sandbox read-only`, czyli w granicach narzuconych przez system.
- Sandbox Grok **nie może być zastosowany** na wielu nowych komputerach z systemem Linux:
  AppArmor blokuje nieuprzywilejowane przestrzenie nazw użytkownika od Ubuntu
  24.04, a deny-lista socketów środowiska uruchomieniowego kontenerów zawodzi, jeśli
  `/run/podman` znajduje się w `0700`. Wbudowany profil, którego **nie da się**
  zastosować, uruchamia się natomiast **bez izolacji i bez ostrzeżenia**.
- Dlatego skrypt domyślnie nie żąda żadnego profilu i **nigdy nie przełącza się po cichu
  na słabszy tryb**: wyświetla ostrzeżenie. Izolacja opiera się na regułach
  `--deny` CLI (w tym catch-all `*`), jedynej sprawdzonej warstwie
  działającej zgodnie z zasadą _fail-closed_ — nieznana reguła powoduje odmowę uruchomienia,
  zamiast wyłączyć ochronę bez powiadomienia.
- Aby **wymusić** sandbox systemu operacyjnego: `GROK_TRANSLATE_SANDBOX=read-only`.
  Uruchomienie zakończy się niepowodzeniem, jeśli komputer nie będzie w stanie go zastosować,
  co jest zamierzonym zachowaniem.

**Limit**: pula Grok jest **tygodniowa i współdzielona** z Chat, Imagine oraz
Voice, a żadne polecenie nie pozwala jej sprawdzić. Przetwarzanie wsadowe może więc
uszczuplić limit przeznaczony na rozmowy bez żadnego powiadomienia — dlatego
współbieżność jest ograniczona do 2, a w `regen_translations.sh` wyświetlane jest ostrzeżenie.

Pozostałe zmienne: `GROK_BIN` (ścieżka do pliku wykonywalnego), `GROK_TIMEOUT` (domyślnie 900 s).

Aby ponownie wygenerować 28 tłumaczeń:

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
### Tłumaczenie za pomocą OpenCode, przez wybranego dostawcę (`--use_opencode`)

[OpenCode](https://opencode.ai) to **open source’owy (MIT)** agent programistyczny działający
w terminalu. Nie jest dostawcą modeli, lecz **routerem** kierującym żądania do
źródeł skonfigurowanych w samym OpenCode: klucza API, subskrypcji,
bramy OpenCode Zen — udostępniającej darmowe modele **bez konta** — lub
modelu **lokalnego**. Ten dostawca uruchamia `opencode run` w trybie nieinteraktywnym
i ogranicza wywołanie do jednej wymiany, bez żadnych narzędzi.

Dwie z tych ścieżek zostały tutaj zmierzone od początku do końca: **brama Zen**
oraz lokalna **Ollama**. Pozostałe zapowiadane przez OpenCode (GitHub Copilot,
LM Studio, llama.cpp) powinny działać z racji konstrukcji, ponieważ dostawca
komunikuje się wyłącznie z OpenCode — nie zostały jednak sprawdzone, a ten README
opisuje tylko to, co zweryfikowano.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` jest **wymagane** w formacie `provider/modèle`. OpenCode nie jest
dostawcą i żaden domyślny wybór nie jest dokonywany za Ciebie: jego własnym
rozwiązaniem awaryjnym byłby darmowy model, którego konwersacje mogą służyć
do trenowania.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Izolacja — co skrypt robi przy każdym wywołaniu:**

- Konfiguracja inline (`OPENCODE_CONFIG_CONTENT`), mająca pierwszeństwo przed
  Twoją konfiguracją, definiuje agenta `aipmt`, któremu **odmówiono dostępu do wszystkich narzędzi**
  (`permission: { "*": "deny" }`): model nie może czytać, zapisywać ani
  uruchamiać poleceń — pomiary wskazują, że nawet tego nie próbuje. Udostępnianie
  sesji jest wyłączone, `--pure` odrzuca zewnętrzne pluginy, nigdy `--auto`.
- Wywołanie działa w **jednorazowym, pustym katalogu**, z przełącznikami
  `OPENCODE_DISABLE_PROJECT_CONFIG` i `OPENCODE_DISABLE_CLAUDE_CODE`: bez
  nich OpenCode wstrzykuje do każdego promptu `AGENTS.md` bieżącego katalogu
  oraz Twój `~/.claude/CLAUDE.md` — w pomiarze instrukcja „kończ każdą odpowiedź
  słowem BANANA” umieszczona w `AGENTS.md` była stosowana do tłumaczenia.
  Globalne reguły `~/.config/opencode/AGENTS.md` nadal jednak obowiązują:
  OpenCode nie pozwala ich pominąć.
- Kontrakt wyjściowy wymaga jednocześnie: kodu wyjścia 0, braku zdarzeń
  `error`, braku wywołań narzędzi, ostatniego kroku zakończonego jako `stop`,
  niepustego tekstu oraz faktycznego załadowania agenta — nieznany `--agent`
  nie powoduje błędu OpenCode, lecz **po cichu przełącza się** on na agenta
  programistycznego z aktywnymi narzędziami. `exit 0` również niczego
  tutaj nie dowodzi.
- **Żaden klucz aipmt nie jest przekazywany** do podprocesu (takie samo filtrowanie
  jak w przypadku Codex i Grok), z jednym nazwanym wyjątkiem: `OPENCODE_API_KEY`,
  czyli kluczem samego OpenCode (Zen, Go). Dostawców konfiguruje się w
  OpenCode (`opencode auth login`, `opencode.json`), a nie w `.env` aipmt.

**Warto wiedzieć:**

- **Darmowe modele Zen są modelami „stealth” lub dostarczanymi przez społeczność**,
  zmiennymi, z nieudokumentowanymi limitami, a ich konwersacje mogą służyć
  do trenowania: świetnie nadają się do publicznej dokumentacji, lecz należy
  ich unikać w przypadku treści prywatnych. Zmierzono: `opencode/mimo-v2.5-free` tłumaczy ten
  README w jednym przebiegu; `opencode/big-pickle` jest wolniejszy, a dwa równoczesne
  żądania pozostały w nim bez odpowiedzi.
- **Model lokalny musi oferować co najmniej 16 tys. tokenów kontekstu** — segmenty
  mają do 16 000 znaków — podczas gdy Ollama często konfiguruje domyślnie 4 096.
  W przypadku Ollama: `Modelfile` z `PARAMETER num_ctx 32768`, a następnie
  `ollama create`. Jakość zależy od modelu: model 7B odwrócił listę i
  uszkodził zamknięcie bloku kodu w pliku testowym, podczas gdy model
  z bramy zachował wszystko.
- `--eco` nie ma wpływu (modelem jest ten z `--model`);
  `--reasoning_effort` jest przekazywane bez zmian jako `--variant` OpenCode i
  należy go używać tylko wtedy, gdy model je rozpoznaje.
- Sesje są rejestrowane przez OpenCode w jego bazie
  (`~/.local/share/opencode/`), tak jak każda sesja OpenCode.
- Zmienne środowiskowe: `OPENCODE_BIN` (jawna ścieżka do pliku wykonywalnego,
  w przeciwnym razie `PATH`, a następnie `~/.opencode/bin/opencode`) oraz `OPENCODE_TIMEOUT`
  (liczba sekund na segment, domyślnie `600`). `OPENCODE_CONFIG` jest
  uwzględniane, jeśli je wyeksportujesz.

**Zmierzony przykład: model lokalny przez Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Następnie dostawca w `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` nie jest drobnym szczegółem: Ollama domyślnie włącza
rozumowanie w tych modelach, a Modelfile nie może go wyłączyć. Pomiar
za pośrednictwem OpenCode: bez tej opcji „Kot śpi na dywanie” zużywa 919 tokenów
rozumowania i 68 s; z nią — 9 tokenów.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Wyniki dla rzeczywistego artykułu blogowego liczącego 589 wierszy (140 linków,
21 sekcji, 3 angielskie cytaty chronione przez tryb `--news`), to samo
polecenie, trzy modele:

| Model                                    | Czas         | Struktura                                                   | Odstępstwa                                                                                |
| ---------------------------------------- | ------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, darmowy) | 4 min 26 s   | identyczna ze źródłem                                       | brak                                                                                      |
| `ollama/gemma4-12b-32k` (lokalny)        | 10 min 10 s  | identyczne linki, URL-e, tabele, tagi, pogrubienia i kod inline | jeden zmyślony wiersz cytatu (🇺🇸 + parafraza), jedno zduplikowane przypisanie autorstwa |
| `ollama/qwen3.5-9b-32k` (lokalny)        | 8 min 18 s   | identyczne linki, URL-e, tabele i tagi                      | jeden zmyślony wiersz cytatu, kilka dodanych pogrubień i fragmentów kodu inline, jeden segment przetworzony ponownie |

Te dwa modele lokalne zostały od tego czasu **odrzucone**: jedna swobodna zmiana
na artykuł wystarcza, by zdyskwalifikować model z tłumaczenia publikowanych
treści. Pięć kolejnych odrzucono z tych samych powodów lub z powodu przekroczenia
limitu czasu (`gemma4:26b-a4b`, `qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`,
`hy-mt2:7b`). Zachowano tylko `gpt-oss:20b` — a nawet on pozostawia
fragmenty po francusku w rozbudowanym artykule; zob. tabelę zalecanych modeli.

Podczas tłumaczenia lokalnego: GPU obciążone w 98% i pobierające 170 W, zajęte
10 GB VRAM (model i cache 32 tys. tokenów, bez przenoszenia czegokolwiek do RAM),
7,5 GB RAM dla serwera Ollama. Model o 9–12 miliardach parametrów zachowuje
strukturę, ale pozwala sobie na jedną swobodną zmianę na artykuł, podczas gdy
model z bramy nie dokonał żadnej: przed publikacją należy tekst sprawdzić lub
używać go wyłącznie do wersji roboczych.

### Tłumaczenie przez OpenRouter (`--use_openrouter`)

OpenRouter to **router** obsługujący ponad 400 modeli hostowanych przez podmioty
trzecie, rozliczany według użycia ze wspólnego salda. Za pomocą jednego klucza
zapewnia dostęp do modeli, których nie udostępnia żaden z pozostałych dostawców,
w szczególności do otwartych modeli chińskich.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Na implementację wpłynęły dwie właściwości routingu, a obie można zmierzyć:

- **Ten sam model jest obsługiwany przez dziesiątki hostów o różnych
  limitach.** Dla `z-ai/glm-5.3-flash` dostępnych jest 23 hostów, w tym jeden z limitem
  2 048 tokenów wyjściowych: bez zabezpieczenia jedno długie tłumaczenie na 23
  było losowo obcinane przez routing, bez najmniejszego sygnału. Preflight
  odczytuje `/api/v1/models/{modèle}/endpoints`, odrzuca hostów z limitem
  wyjściowym poniżej 8 000 tokenów lub ze statusem degraded, a następnie przypina
  pozostałych za pomocą `allow_fallbacks: false` — bez tego router ponownie
  kieruje żądanie do odrzuconego hosta.
- **Rozumowanie jest rozliczane według stawki za tokeny wyjściowe.** To samo
  żądanie do `z-ai/glm-5.2`, odpowiedź „OK”: 107 tokenów completion przy
  domyślnych ustawieniach modelu, 2 po wyłączeniu rozumowania. Dlatego jest ono
  domyślnie wyłączone w modelach, które na to pozwalają. Modele, które je
  wymuszają — `reasoning.mandatory`, czyli 288 z 431 modeli w katalogu — otrzymują
  **najniższy deklarowany przez nie akceptowany poziom wysiłku**, a nie ustawienie
  domyślne: dla `z-ai/glm-5.3-flash` jest to `max`, co powodowało wykorzystanie
  wszystkich 32 768 tokenów wyjściowych przed końcem tłumaczenia. Zwiększenie
  limitu niczego by nie zmieniło, ponieważ wysiłek przydziela jego procent.
  `--reasoning_effort` zachowuje pierwszeństwo, a `none` w przypadku modelu
  wymuszającego rozumowanie jest zgłaszane zamiast obchodzone.

Preflight działa w trybie **fail-closed** i wyświetla dokonany wybór:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Brak sluga w katalogu, niedostępny katalog lub brak hosta spełniającego limit
zatrzymują polecenie przed naliczeniem jakichkolwiek opłat.

Pozostałe informacje:

- Okno kontekstu pochodzi z katalogu, a nie ze stałej: segmentacja rzeczywiście
  się do niego dostosowuje, również w przypadku modeli z 4 095 tokenami.
- `--eco` nie ma wpływu (modelem jest ten z `--model`).
- `finish_reason=length` z pustym wyjściem nie oznacza obcięcia, lecz budżet zużyty
  przez rozumowanie; komunikat to wyjaśnia, ponieważ oba przypadki wymagają
  przeciwnych działań.
- Zmienne środowiskowe: `OPENROUTER_API_KEY` (klucz, dostępny pod
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (domyślnie
  `https://openrouter.ai/api/v1`, wymagane `https://`), `OPENROUTER_TIMEOUT`
  (liczba sekund na wywołanie, domyślnie `900`) oraz `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie `30`).

### Tryb ekonomiczny

Używa szybszych i tańszych modeli (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                    | Opis                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                                                                   |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                                                                   |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                                                                 |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                                                   |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                                                   |
| `--model`                | Konkretny model do użycia                                                                                     |
| `--eco`                  | Użycie modeli ekonomicznych                                                                                   |
| `--use_mistral`          | Użycie API Mistral AI                                                                                         |
| `--use_claude`           | Użycie API Claude                                                                                             |
| `--use_gemini`           | Użycie API Gemini                                                                                             |
| `--use_codex`            | Użycie CLI Codex w ramach limitu subskrypcji ChatGPT                                                          |
| `--use_grok`             | Użycie API xAI (Grok) — wymaga `XAI_API_KEY`                                                                |
| `--use_openrouter`       | Użycie OpenRouter — wymaga `OPENROUTER_API_KEY` i `--model fournisseur/modèle`                                                  |
| `--use_grok_cli`         | Użycie CLI Grok w ramach limitu subskrypcji Grok                                                              |
| `--use_opencode`         | Użycie OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle`                    |
| `--force`                | Wymuszenie ponownego tłumaczenia                                                                              |
| `--keep_filename`        | Zachowanie oryginalnej nazwy pliku                                                                            |
| `--news`                 | Tryb wiadomości: chroni cytaty EN i obsługuje flagi według języka                                             |
| `--add_translation_note` | Dodanie noty o tłumaczeniu                                                                                     |
| `--note_position`        | Pozycja noty: `top`, `bottom` (domyślnie) lub `both`                                |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                               |
| `--include_model`        | Umieszczenie nazwy modelu w pliku wyjściowym                                                                  |
| `--reasoning_effort`     | Poziom wysiłku rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **Siedem flag dostawców wzajemnie się wyklucza.** Wcześniej połączenie dwóch
> było po cichu akceptowane i wybierano pierwszą sprawdzaną flagę: tłumaczenie
> zlecone w ramach limitu subskrypcji (`--use_codex`, `--use_grok_cli`) mogło
> więc bez ostrzeżenia zostać rozliczone według użycia.
> `argparse` odrzuca teraz taką kombinację.

### Nota o tłumaczeniu: pozycje i formaty

Dzięki `--add_translation_note` translator może umieścić notę na górze, na dole albo
w obu miejscach oraz renderować ją jako zwykły tekst (zgodny wstecznie) lub
w formacie `marker`, który może zostać przetworzony przez plugin Markdown.

**Pozycja** (`--note_position`):

- `bottom` (domyślnie): nota na końcu pliku, tak jak dotychczas.
- `top`: nota wstawiona **po frontmatter YAML** (bezpiecznie dla Astro Content Collections, gray-matter itd.).
- `both`: nota wstawiona na górze ORAZ na dole (jedno wywołanie LLM, treść używana ponownie w obu miejscach).

**Format** (`--note_format`):

- `legacy` (domyślnie): pogrubiony akapit `**...**` — zachowanie ściśle identyczne z v1.8, byte-for-byte. Zgodne z Hugo, GitHub, GitLab i każdym rendererem Markdown.
- `marker`: niewidoczna definicja link reference Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), po której następuje pogrubiony blockquote. Czytelne natywnie w GitHub/GitLab i możliwe do wykorzystania podczas buildu przez plugin remark po stronie Astro w celu wygenerowania stylizowanego banera (zob. blog jls42.org).

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

| Dostawca   | Jakość (domyślnie)                       | Ekonomiczny (`--eco`) |
| ---------- | ---------------------------------------- | ----------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`               |
| Claude     | `claude-sonnet-5`                          | `claude-haiku-4-5`               |
| Mistral    | `mistral-large-latest`                          | `mistral-small-latest`               |
| Gemini     | `gemini-3.7-flash`                          | `gemini-3.1-flash-lite`               |
| Codex      | `gpt-5.6-sol`                          | `gpt-5.6-luna`               |
| Grok API   | `grok-4.6`                          | `grok-4.3`               |
| Grok CLI   | `grok-4.6`                          | `grok-4.5`               |
| OpenCode   | wymagane `--model provider/modèle`                 | tak samo — `--eco` bez wpływu |
| OpenRouter | wymagane `--model fournisseur/modèle`                 | tak samo — `--eco` bez wpływu |
## Które modele dają radę

Model, który dobrze tłumaczy akapit, niekoniecznie zachowuje strukturę całego
dokumentu. Poniższe wyniki pochodzą z **rzeczywiście wykonanych
tłumaczeń**, przy użyciu polecenia opisanego powyżej, na trzech zestawach
dokumentów i dla czternastu języków docelowych: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Dwie kolumny, które nie oznaczają tego samego. **Zapisane** zlicza ukończone
tłumaczenia — zabezpieczenia skryptu przed niezauważonym niepowodzeniem
przepuszczają plik. **Bez rozbieżności** zlicza te, których struktura jest
identyczna ze źródłem: te same sekcje, linki, URL-e, bloki i kody w tekście,
tabele, cytaty oraz flagi.

### Obszerny artykuł na blogu, tryb `--news`

589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty w języku angielskim. Jest to
najbardziej wymagający z trzech dokumentów: tryb `--news` dodaje do struktury
Markdown dodatkowe ograniczenia dotyczące flag i cytatów.

| Model                             | Dostęp             | Zapisane | Bez rozbieżności | Mediana/język |
| --------------------------------- | ------------------ | -------- | ---------------- | ------------- |
| `gemini-3.7-flash`                | API Google         | 14/14    | **14/14**        | 1 min 18 s    |
| `gpt-5.6-sol` (`--use_codex`)     | subskrypcja ChatGPT | 14/14    | **14/14**        | 11 min 28 s   |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14    | **14/14**        | 5 min 37 s    |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14    | 13/14            | 26 min 23 s   |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14    | 12/14            | 15 min 49 s   |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9      | 7/9              | 20 min 33 s   |
| `claude-sonnet-5`                 | API Anthropic      | 14/14    | 11/14            | 6 min 31 s    |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14    | 11/14            | 9 min 27 s    |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14    | 7/14             | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`          | lokalnie           | 10/14    | 7/14             | 12 min 39 s   |
| `mistral-large-latest`            | API Mistral        | 11/14    | 5/14             | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14     | 3/14             | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)     | subskrypcja Grok    | 1/14     | 1/14             | 23 min 11 s   |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4      | 1/4              | 23 min 00 s   |

Dwie partie zostały **przerwane z powodu wyczerpania środków**, co odzwierciedla
ich mianownik: `qwen3.5-27b` zatrzymał się na dziewięciu językach, a `kimi-k2.6` na czterech —
ten ostatni po przekroczeniu limitu czasu wynoszącego czterdzieści minut i dwóch odmowach, przy koszcie
blisko 0,33 $ za język.

Jedno zastrzeżenie metodologiczne dotyczące wierszy OpenRouter: pomiary wykonano przy
**domyślnych ustawieniach routera**, zanim powstał `--use_openrouter`.
Od tego czasu `z-ai/glm-5.2` został ponownie zmierzony z dostarczonym providerem i wyłączonym
rozumowaniem, uzyskując dokładnie ten sam wynik 14/14. `z-ai/glm-5.3-flash` dwukrotnie zawiódł z powodu
wyczerpania budżetu wyjściowego przy domyślnych ustawieniach routera; provider żąda teraz od
tych modeli najniższego obsługiwanego poziomu wysiłku, a próba kontrolna dla
problematycznych języków kończy się powodzeniem.

### README tego projektu, standardowy Markdown

508 wierszy, 219 kodów w tekście, 40 znaczników zamykających bloki, 45 wierszy tabel. Nie ma
tu trybu `--news`: trudność wynika z dużego zagęszczenia kodu.

| Model                         | Zapisane | Bez rozbieżności | Mediana/język |
| ----------------------------- | -------- | ---------------- | ------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14    | 11/14            | 1 min 22 s    |
| `gemini-3.7-flash`            | 14/14    | 13/14            | 21 s          |
| `gpt-5.6-sol` (`--use_codex`) | 14/14    | 12/14            | 2 min 04 s    |
| `opencode/mimo-v2.5-free`     | 9/14     | 7/14             | 3 min 25 s    |
| `ollama/gpt-oss-20b-32k`      | 9/14     | 1/14             | 3 min 38 s    |

### Cztery README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane bez zmian z GitHub. Dokumenty te
są **łatwiejsze** niż dwa poprzednie, co widać w tabeli.

| Model                     | Zakres                     | Zapisane | Bez rozbieżności |
| ------------------------- | -------------------------- | -------- | ---------------- |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków     | 55/56    | 47/56            |
| `grok-4.6` (subskrypcja)   | 4 projekty × ar, hi, ja, zh | 16/16    | 14/16            |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16    | 9/16             |

### Wnioski

- **Trzy modele nigdy nie utraciły informacji** w dwóch obszernych
  dokumentach: `gemini-3.7-flash`, `gpt-5.6-sol` przez subskrypcję ChatGPT oraz
  `z-ai/glm-5.2` przez OpenRouter. Ich jedyne rozbieżności w trybie standardowym to
  para nieprzeniesionych `**` w jednym lub dwóch językach, nigdy zaś URL, blok
  kodu ani cytat.
- **Czynnikiem rozstrzygającym jest zagęszczenie dokumentu, a nie tryb `--news`.**
  Grok w subskrypcji zawodzi 13 razy na 14 w przypadku artykułu na blogu, a poprawnie tłumaczy 14
  publicznych README na 16: przyczyną niepowodzenia jest utrata spójności na długim segmencie,
  potwierdzona próbą kontrolną — wyizolowany fragment jest tłumaczony poprawnie.
- **Pisma niełacińskie nie stanowią spodziewanej granicy podziału.** `gpt-oss` pozostawia
  fragmenty po francusku w tłumaczeniach na arabski, japoński, polski **i rumuński**; Mistral
  i MiMo tracą kody w tekście wyłącznie w przypadku pism niełacińskich.
- **Wyłączenie rozumowania nie pogarsza jakości.** `z-ai/glm-5.2` obsługuje
  czternaście języków bez żadnej rozbieżności w obu warunkach — z rozumowaniem domyślnie
  włączonym przez router, a następnie wyłączonym przez `--use_openrouter` — przy osiemnastokrotnie
  mniejszej liczbie rozliczanych tokenów wyjściowych. To właśnie ten pomiar uzasadnia domyślne
  ustawienie providera.
- **Powolny model nie jest bezpiecznym modelem.** `deepseek-v4-flash-0731` potrzebuje 37
  minut na język, uzyskując 4 tłumaczenia na 14, `qwen3.8-flash` 26 minut na
  niemal doskonały wynik, a Gemini 1 minuty i 18 sekund na bezbłędny rezultat.

### Czego ta tabela nie przedstawia

- **Nie jest to wyczerpujący ranking.** Sam OpenRouter oferuje ponad
  czterysta modeli; tutaj zmierzono około piętnastu. Brak
  modelu nie mówi nic o jego jakości, a jedynie oznacza, że nie został przetestowany.
- **Pomiary mają określoną datę**: 4 i 5 września 2026 r. Modele zmieniają się
  pod tą samą nazwą, dostawcy dostosowują kwantyzację i limity, a nowe
  modele pojawiają się co tydzień.
- **Czasy nie tworzą żadnego rankingu.** Równolegle wykonywano od 3 do 6 tłumaczeń
  zależnie od serii testów, a przepustowość dostawcy zmienia się w ciągu
  dnia. Wskazują jedynie rząd wielkości, a nie pozwalają na porównanie.
- **Wynik zależy zarówno od dokumentu, jak i od modelu.** Ten sam model
  obsługuje czternaście języków w artykule i dziewięć w tym README. Wasze pliki nie
  są naszymi.
- **Najlepszym podejściem pozostaje wykonanie pomiarów u siebie**: przetłumaczcie jeden ze swoich
  dokumentów na języki docelowe, a następnie porównajcie strukturę — liczbę
  sekcji, linków, unikatowych URL-i, bloków kodu, kodów w tekście oraz
  wierszy tabel. Dokładnie to robi powyższy protokół, który
  mieści się w jednej pętli wykorzystującej `aipmt`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-5.6-sol.**
