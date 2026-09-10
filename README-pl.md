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

Tłumaczy pliki Markdown z jednego języka na inny, zachowując ich
strukturę: bloki kodu, kod w tekście, URL-e, kotwice, tabele i front
matter. Dziewięć sposobów wywołania modelu — pięć API, dwie subskrypcje bez
opłat za użycie i dwa routery — oraz opublikowany pomiar tego, co każdy
model rzeczywiście zachowuje.

## W skrócie

- **Dziewięć ścieżek providerów**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex) i Grok bez opłat za użycie; routery
  OpenCode (open source, bezpłatny lub lokalny) i OpenRouter (ponad 400 modeli).
- **Brak nieprawidłowego wyniku z powodu utraconego tokenu**: bloki kodu, kod w tekście,
  URL-e, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  sprawdzane po otrzymaniu odpowiedzi. Jeśli któregoś brakuje, plik nie jest zapisywany.
- **Długie dokumenty**: segmentacja zgodnie z oknem kontekstowym modelu.
- **Tryb `--news`**: chronione cytaty angielskie i flagi obsługiwane zależnie od
  języka na potrzeby artykułów przeglądowych.
- **Tryb `--eco`**: szybsze i tańsze modele.
- Opcjonalna **nota o tłumaczeniu** u góry, u dołu lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 lub nowszy. Instrukcje instalacji z repozytorium znajdują się w sekcji
[Współtworzenie](#współtworzenie).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego do najniższego priorytetu; każde z nich
uzupełnia tylko to, czego nie dostarczyło poprzednie.

|     | Gdzie                                            | Zastosowanie                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                     | CI, kontenery, jednorazowe nadpisanie |
| 2   | `.env` w bieżącym katalogu (lub katalogu nadrzędnym) | klucz właściwy dla projektu            |
| 3   | `~/.config/aipmt/.env`                        | instalowany raz, działa wszędzie       |

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

`GEMINI_API_KEY` jest akceptowane zamiast `GOOGLE_API_KEY`. Plik
użytkownika jest zgodny z `XDG_CONFIG_HOME` (wyłącznie ścieżka bezwzględna) oraz `%APPDATA%`
w systemie Windows. Bez klucza polecenie wyświetla wszystkie trzy lokalizacje.

**Plik `.env` projektu nie może przekierowywać wywołań.** Dostarcza klucze,
nigdy adres docelowy: wszystkie zmienne z `_BASE_URL`, `_API_BASE` lub
`_ENDPOINT`, proxy (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), magazyny
certyfikatów (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` / `APPDATA` są w nim ignorowane wraz z
ostrzeżeniem. Sklonowane repozytorium nie powinno móc przechwycić Twojego klucza. Ten
plik jest również odczytywany bez interpolacji: `NOM=${OPENAI_API_KEY}` nie kopiuje
do niego klucza. Ustaw te zmienne w środowisku lub w
`~/.config/aipmt/.env`.

Zmienne opcjonalne: `XAI_BASE_URL` (domyślnie `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekundy na wywołanie, domyślnie 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(domyślnie 600), `GROK_BIN`, `GROK_HOME` (domyślnie `~/.grok`), `GROK_TIMEOUT`
(domyślnie 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(domyślnie 600), `OPENROUTER_BASE_URL` (wymagane `https://`), `OPENROUTER_TIMEOUT`
(domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (domyślnie 30). Każda z nich została szczegółowo opisana
w sekcji odpowiedniego providera.

## Pierwsze kroki

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` tłumaczy na język hiszpański, tworząc `document-es.md` w `--target_dir`;
z `--include_model` powstaje `document-es-gpt-5.6-terra.md`. Rozszerzeniem jest
zawsze `.md` — `article.mdx` daje `article-en.md` — z wyjątkiem użycia
`--keep_filename`, które zachowuje pierwotną nazwę. Istniejące już tłumaczenie
jest pomijane bez `--force`.

Kody wyjścia: `0`, jeśli wszystkie operacje zakończyły się powodzeniem lub zostały pominięte, `1`, jeśli pozostał plik,
którego przetwarzanie się nie powiodło (lista na standardowym wyjściu błędów), `2`, jeśli przyczyną jest konfiguracja.
Plik, którego przetwarzanie się nie powiodło, nigdy nie jest zapisywany, nawet jeśli nie powiedzie się sam zapis:
treść jest zapisywana obok, a następnie plik otrzymuje właściwą nazwę. Wystarczy uruchomić polecenie ponownie.

## Który model wybrać

Pomiar przeprowadzono na dwóch rzeczywistych dokumentach tłumaczonych przez
każdy model na tych samych czternaście języków. **Liczba oznacza liczbę języków spośród czternastu, dla których
tłumaczenie zostało zapisane i w których nic nie różni się od źródła.**

| Model               | Sposób dostępu                 | Gęsty artykuł przeglądowy | Ten README    | Co się różni i w ilu językach                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | klucz API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 język na 14: jedno dodatkowe słowo zapisane pogrubieniem (ja)                                                                                         |
| **GPT-5.6 Sol**      | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 języki na 14: jedno słowo mniej zapisane pogrubieniem (ar, ja)                                                                                   |
| **GLM-5.2**          | klucz OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 języki na 14: jedno słowo mniej zapisane pogrubieniem (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | klucz API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym README: link bez znaczników (sv), słowo zapisane pogrubieniem (zh) |
| Qwen 3.7 Flash       | klucz OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 język odrzucony w artykule, 5 innych wykazuje różnice; w tym README około czterdziestu słów umieszczono w `code` (ar)                       |
| Grok 4.6             | subskrypcja Grok                   | ❌ 8/14                 | bez oceny     | 5 języków odrzuconych na 14 z powodu niezwrócenia kodu w tekście i URL-i; wersja niderlandzka różni się w całości                                  |
| GPT-OSS 20B          | model lokalny (Ollama)             | ❌ 7/14                 | nie zmierzono ponownie | 4 języki odrzucone na 14: model pozostawiał w nich fragmenty po francusku, a mechanizmy kontrolne je zatrzymały                                     |
| MiMo v2.5 (bezpłatny)  | OpenCode Zen, bez konta         | ❌ 11/14                | nie zmierzono ponownie | 1 język odrzucony; utracona sekcja w języku polskim                                                                                     |
| Mistral Large        | klucz API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **znika cała sekcja**: 1 język w artykule (hi), 3 w tym README (ar, hi, ko) — ponadto 3 języki odrzucono w artykule   |
| DeepSeek V4 Flash    | klucz OpenRouter                    | ❌ 3/14                 | nie zmierzono ponownie | 10 języków odrzuconych na 14; 37 minut na język                                                                                    |

|     | Znaczenie symbolu                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | przetłumaczono wszystkie czternaście języków i nic nie różni się od źródła                                                                                                                                       |
| ⚠️  | przetłumaczono wszystkie czternaście języków; różnice dotyczą **znaczników** — słowa zapisanego pogrubieniem, elementu `code`, linku, który utracił nawiasy kwadratowe. Nie brakuje żadnego tekstu, URL-a, bloku kodu ani sekcji |
| ❌  | co najmniej jednego języka nie udało się przetłumaczyć — plik został odrzucony i niezapisany — **lub** w zapisanym pliku brakuje treści                                                                      |

Najważniejsze wnioski:

- **Odrzucone tłumaczenie nie jest uszkodzonym tłumaczeniem.** Gdy po otrzymaniu odpowiedzi brakuje tokenu,
  plik nie jest zapisywany, a język uznaje się za
  odrzucony. Tak dzieje się w przypadku Grok w artykule: cztery fragmenty kodu w tekście i
  trzy URL-e zostają utracone już w pierwszym segmencie dla pięciu pism niełacińskich.
- **Ten mechanizm zabezpieczający nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik zapisywany przez narzędzie
  bez protestu — tak jest w przypadku Mistral. Tych elementów nie można
  zastąpić tokenem, a obecne mechanizmy kontrolne ich nie sprawdzają;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego README**: jego sesja CLI wygasła po dwunastu
  językach, z których jedenaście nie wykazało różnic. Przerwana kampania nie otrzymuje oceny.
- **Gęstość dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze zwykłymi
  plikami README, ale zawodzi przy artykule wypełnionym linkami, także w języku
  niderlandzkim.

Daty i dokumenty: kolumnę „Ten README” zmierzono 9 września 2026 roku
na zamrożonej rewizji tego pliku (785 wierszy, 285 fragmentów kodu w tekście, 89 wierszy
tabel), która została później zmodyfikowana. Kolumna „Gęsty artykuł przeglądowy” pochodzi z
kampanii z 4 i 5 września przeprowadzonej na artykule liczącym 589 wierszy, z wyjątkiem wiersza
Grok, zmierzonego ponownie 9 września na innym wydaniu tego samego przeglądu. Pełne
tabele, czasy trwania i protokół znajdują się w sekcji
[Szczegółowe pomiary](#szczegółowe-pomiary).

## Wszystkie opcje

| Opcja                   | Opis                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia (alternatywa dla `--source_dir`)                                             |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown (domyślnie: `content/posts`)                                   |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików (domyślnie: `traductions_en`)                                    |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                                                                  |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                                                                   |
| `--model`                | Konkretny model do użycia                                                                                  |
| `--eco`                  | Użyj modeli ekonomicznych                                                                              |
| `--use_mistral`          | Użyj API Mistral AI                                                                                     |
| `--use_claude`           | Użyj API Claude                                                                                         |
| `--use_gemini`           | Użyj API Gemini                                                                                         |
| `--use_grok`             | Użyj API xAI (Grok) — wymaga `XAI_API_KEY`                                                           |
| `--use_codex`            | Użyj CLI Codex w ramach limitu subskrypcji ChatGPT                                                    |
| `--use_grok_cli`         | Użyj CLI Grok w ramach limitu subskrypcji Grok                                                        |
| `--use_opencode`         | Użyj OpenCode (open source) z providerem skonfigurowanym w OpenCode; wymaga `--model provider/modèle` |
| `--use_openrouter`       | Użyj OpenRouter — wymaga `OPENROUTER_API_KEY` i `--model fournisseur/modèle`                          |
| `--force`                | Wymuś ponowne tłumaczenie                                                                                       |
| `--keep_filename`        | Zachowaj pierwotną nazwę pliku                                                                          |
| `--news`                 | Tryb aktualności: chroni cytaty EN, obsługuje flagi zależnie od języka                                      |
| `--add_translation_note` | Dodaj notę o tłumaczeniu                                                                                |
| `--note_position`        | Położenie noty: `top`, `bottom` (domyślnie) lub `both`                                                     |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                                            |
| `--include_model`        | Umieść nazwę modelu w pliku wyjściowym                                                            |
| `--reasoning_effort`     | Poziom rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Osiem flag `--use_*` wzajemnie się wyklucza: połączenie dwóch zostanie
odrzucone.

## Providerzy

### Przez API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` przełącza na ekonomiczny poziom każdego providera.

| Provider   | Jakość (domyślnie)                                      | Ekonomiczny (`--eco`)      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol` (także `terra` i `luna` przez `--model`) | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` wymagane                 | tak samo — `--eco` bez efektu |
| OpenRouter | `--model fournisseur/modèle` wymagane              | tak samo — `--eco` bez efektu |
### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest odliczane od limitu
subskrypcji ChatGPT, bez klucza API ani rozliczania według użycia.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Plik wykonywalny jest wyszukiwany w `CODEX_BIN`, następnie w `PATH`, a potem w pakiecie
  `openai-codex-cli-bin`. `~/.codex/auth.json` nigdy nie jest odczytywany.
- `OPENAI_API_KEY` i `CODEX_API_KEY` są usuwane ze środowiska
  podprocesu: obecność klucza nigdy nie powoduje przełączenia na API.
- Każdy segment kosztuje co najmniej jedną „wiadomość” z 5-godzinnego okna — dwie,
  jeśli jego walidacja się nie powiedzie i zostanie ponowiona. Według szacunków
  OpenAI jest to 250–2 000 wiadomości/5 godz. dla `gpt-5.6-luna` (`--eco`) oraz
  10–100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-terra` i `--model gpt-5.6-luna` również korzystają z
  subskrypcji. Model, do którego konto nie ma dostępu, zwraca błąd 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Działa wolniej niż API, a różnica rośnie wraz z rozmiarem dokumentu: dla tego README
  mediana wynosi 6 min 46 s na język z `gpt-5.6-sol`, w porównaniu z 36 s dla
  `gemini-3.7-flash`.
- Niedozwolone w CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): subskrypcja uwierzytelnia się
  za pomocą osobistego pliku sesji, który nie powinien znajdować się na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada obowiązuje z oficjalnym CLI Grok Build, w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Sandbox systemu operacyjnego Grok nie działa
  na wielu nowszych stanowiskach z systemem Linux (AppArmor, sockety runtime
  kontenera), a profil, którego nie można zastosować, uruchamia się po cichu bez
  izolacji. Dlatego skrypt domyślnie nie żąda żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` CLI, w tym regule ogólnej `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast bez ostrzeżenia usuwać
  ochronę. `GROK_TRANSLATE_SANDBOX=read-only` wymaga sandboxa systemu operacyjnego, a uruchomienie
  kończy się niepowodzeniem, jeśli maszyna nie może go zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, a żadna
  komenda nie pozwala go odczytać: zadanie wsadowe może uszczuplić limit na rozmowy
  bez żadnego ostrzeżenia.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to agent programistyczny open source (MIT), który
kieruje żądania do skonfigurowanych w nim dostawców: klucza API, subskrypcji,
bramy OpenCode Zen (darmowe modele, bez konta) lub modelu lokalnego. Dwie
ścieżki zostały tutaj zmierzone od początku do końca: Zen i Ollama.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` jest obowiązkowe: bez niego OpenCode przełączyłby się na darmowy model,
którego konwersacje mogą służyć do trenowania, a ten wybór nie jest podejmowany
za użytkownika.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, mająca pierwszeństwo przed konfiguracją użytkownika, definiuje agenta `aipmt`,
  któremu odmówiono dostępu do wszystkich narzędzi (`permission: { "*": "deny" }`), z wyłączonym
  udostępnianiem sesji, `--pure`, nigdy `--auto`;
- jednorazowy, pusty katalog roboczy oraz ustawione `OPENCODE_DISABLE_PROJECT_CONFIG` i
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstrzykuje do
  promptu `AGENTS.md` bieżącego katalogu oraz `~/.claude/CLAUDE.md`. Globalny
  `~/.config/opencode/AGENTS.md` nadal jest wstrzykiwany, ponieważ OpenCode nie pozwala
  go wyłączyć;
- kontrakt wyjścia: kod zakończenia 0, brak zdarzenia `error`, brak wywołań
  narzędzi, ostatni krok w `stop`, niepusty tekst i faktycznie załadowany agent `aipmt`
  — nieznany `--agent` nie powoduje błędu OpenCode, lecz po cichu
  przełącza go na agenta programistycznego;
- żaden klucz `aipmt` nie jest przekazywany poza `OPENCODE_API_KEY`, kluczem
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  `.env` programu `aipmt`.

Warto wiedzieć:

- Darmowe modele Zen zmieniają się, mają nieudokumentowane limity, a ich
  konwersacje mogą służyć do trenowania: nadają się do publicznej dokumentacji,
  lecz nie do treści prywatnych.
- Model lokalny musi oferować co najmniej 16 tys. tokenów kontekstu, ponieważ segmenty
  mogą mieć do 16 000 znaków. Ollama często konfiguruje 4 096: należy użyć
  `Modelfile` z `PARAMETER num_ctx 32768`.
- `--eco` nie ma wpływu; `--reasoning_effort` jest przekazywane bez zmian jako
  `--variant` OpenCode.
- OpenCode zapisuje dziennik każdej sesji w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, a następnie `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekundy na segment, domyślnie 600). `OPENCODE_CONFIG`
  jest przekazywane do OpenCode bez zmian.

Przykład modelu lokalnego przez Ollama, w `~/.config/opencode/opencode.json`:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

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

`reasoningEffort: "none"` wyłącza rozumowanie, które Ollama domyślnie aktywuje dla tych
modeli i którego nie można wyłączyć za pomocą Modelfile. Pomiar dla zdania
złożonego z sześciu słów: 919 tokenów rozumowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Dostęp do ponad 400 modeli: `--use_openrouter`

OpenRouter to rozliczany według użycia router, opłacany z jednorazowego kredytu, pośredniczący
w dostępie do modeli hostowanych przez podmioty zewnętrzne — w tym otwartych modeli chińskich, których żaden
inny dostawca tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest obowiązkowe. Preflight, wykonywany przed naliczeniem jakiejkolwiek opłaty, obsługuje
dwie szczególne cechy routingu:

- **Ten sam model jest obsługiwany przez dziesiątki dostawców hostingu o różnych
  limitach** — w przypadku `z-ai/glm-5.3-flash` jest to 23 dostawców, w tym jeden z limitem
  2 048 tokenów wyjściowych. Preflight odczytuje `/api/v1/models/{modèle}/endpoints`,
  odrzuca dostawców oferujących mniej niż 8 000 tokenów wyjściowych lub mających obniżony status i
  przypina pozostałych za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki za dane wyjściowe** — 107 tokenów wobec 2 dla
  odpowiedzi „OK” modelu `z-ai/glm-5.2`. Domyślnie jest wyłączone; modele,
  które go wymagają, otrzymują najniższy akceptowany poziom wysiłku, ponieważ domyślna wartość
  katalogu mogłaby wyczerpać limit wyjściowy przed końcem tłumaczenia.
  `--reasoning_effort` zachowuje pierwszeństwo.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model oferujący mniej niż 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8 400 na prompt i segment oraz co najmniej
  8 000 na dane wyjściowe.
- Brak sluga w katalogu, niedostępny katalog lub brak
  dostawcy hostingu spełniającego limit powodują zatrzymanie komendy.
- `finish_reason=length` z pustymi danymi wyjściowymi oznacza budżet zużyty przez
  rozumowanie, a nie obcięcie: komunikat rozróżnia te przypadki.
- `--eco` nie ma wpływu.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Informacja o tłumaczeniu

`--add_translation_note` dodaje informację w `bottom` (domyślnie), `top` (po
front matter) lub `both` (`--note_position`), w formacie `legacy` (pogrubiony
akapit, domyślnie) albo `marker` (`--note_format`). Format `marker` jest
niewidoczną definicją odwołania Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje pogrubiony cytat: czytelny na GitHubie i możliwy do wykorzystania podczas buildu przez
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary pochodzą z tłumaczeń rzeczywiście wykonanych za pomocą `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** oznacza pliki przepuszczone przez zabezpieczenia; **Bez
różnic** oznacza te, w których `scripts/compare_structure.py` niczego nie wykrywa — tę samą liczbę
sekcji, podtytułów, linków, różnych URL-i, bloków kodu,
fragmentów kodu inline, wierszy tabel, bloków cytatów i pogrubionych słów.

„Bez różnic” oznacza „niczego nie wykryto”, a nie „identyczne”: narzędzie porównujące
zlicza elementy bez odczytywania ich zawartości. Nie wykrywa ani usuniętego nagłówka
poziomu 4, ani zastąpienia tekstu kodu inline, ani zamiany
flagi i nie ocenia języka.

### Obszerny artykuł przeglądowy, tryb `--news`

Jedno wydanie [przeglądu AI serwisu jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty angielskie. Kampania
z 4 i 5 września 2026 r.

| Model                             | Dostęp             | Zapisane | Bez różnic   | Mediana/język |
| --------------------------------- | ------------------ | -------- | ------------ | ------------- |
| `gemini-3.7-flash`                | API Google         | 14/14    | ✅ **14/14** | 1 min 18 s    |
| `gpt-5.6-sol` (`--use_codex`)     | subskrypcja ChatGPT | 14/14    | ✅ **14/14** | 11 min 28 s   |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14    | ✅ **14/14** | 5 min 37 s    |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14    | ✅ **14/14** | 26 min 23 s   |
| `claude-sonnet-5`                 | API Anthropic      | 14/14    | ⚠️ 11/14     | 6 min 31 s    |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14    | ❌ 11/14     | 9 min 27 s    |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14    | ❌ 8/14      | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`          | lokalnie           | 10/14    | ❌ 7/14      | 12 min 39 s   |
| `mistral-large-latest`            | API Mistral        | 11/14    | ❌ 5/14      | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14     | ❌ 3/14      | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)     | subskrypcja Grok    | 1/14     | ❌ 1/14      | 23 min 11 s   |

Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): zapisano 9 z 14 języków, w tym 8 bez różnic. To właśnie ta wartość
widnieje w tabeli głównej. Nie uwzględniono trzech przerwanych kampanii:
`qwen3.5-27b` (9 języków) i `kimi-k2.6` (4) z powodu braku środków oraz
`z-ai/glm-5.3-flash`, którego dwa niepowodzenia wynikały z ustawienia rozumowania
naprawianego od tego czasu przez dostawcę. Wiersze OpenRouter zmierzono przy
domyślnych ustawieniach routera, przed `--use_openrouter`; ponownie zmierzony
`z-ai/glm-5.2` z dostarczonym dostawcą uzyskuje ten sam wynik 14/14. Wyniki zostały
ponownie obliczone 10 września przy użyciu obecnego narzędzia porównującego: `qwen3.8-flash` i
`qwen3.7-flash` zyskują po jednym języku względem pierwszej
publikacji, pozostałe wyniki pozostają bez zmian.

### README tego projektu, standardowy Markdown

Rewizja utrwalona 9 września 2026 r.: 785 wierszy, 285 fragmentów kodu inline, 40
ogrodzeń bloków, 89 wierszy tabel. Cztery równoległe tłumaczenia.

| Model                         | Zapisane | Bez różnic | Mediana/język | Różnice                                                                  |
| ----------------------------- | -------- | ---------- | ------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14    | ⚠️ 13/14   | 36 s          | jedno pogrubione słowo (ja)                                              |
| `claude-sonnet-5`             | 14/14    | ⚠️ 12/14   | 2 min 56 s    | jeden link (sv), jedno pogrubione słowo (zh)                              |
| `gpt-5.6-sol` (`--use_codex`) | 14/14    | ⚠️ 12/14   | 6 min 46 s    | jedno pogrubione słowo (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14    | ⚠️ 11/14   | 2 min 34 s    | jedno pogrubione słowo (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`          | 14/14    | ⚠️ 10/14   | 2 min 17 s    | 40 fragmentów kodu inline dodanych po arabsku; pogrubienie (hi, ja, ko)  |
| `mistral-large-latest`        | 14/14    | ❌ 1/14    | 2 min 44 s    | utracona sekcja (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh)         |

Nie uwzględniono dwóch przerwanych kampanii: Grok — sesja CLI wygasła
po dwunastu językach (jedenaście bez różnic), oraz `qwen3.8-flash` — błąd HTTP 429 od jego
dostawcy hostingu po dwóch. `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie zostały ponownie zmierzone na tej rewizji; na rewizji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisał 9 z 14 tłumaczeń, w tym odpowiednio 7
i 1 bez różnic.

### Cztery README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane w niezmienionej postaci z GitHuba — dokumenty
łatwiejsze niż dwa poprzednie. Kampania skupiała się na modelach
mających trudności; Gemini służy w niej jako punkt odniesienia.

| Model                     | Zakres                     | Zapisane | Bez różnic   |
| ------------------------- | -------------------------- | -------- | ------------ |
| `gemini-3.7-flash`        | 4 projekty × 14 języków    | 56/56    | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków    | 55/56    | ❌ 47/56     |
| `grok-4.6` (subskrypcja)   | 4 projekty × ar, hi, ja, zh | 16/16    | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16    | ❌ 9/16      |

### Czym te pomiary nie są

- **Nie jest to wyczerpujący ranking**: sam OpenRouter oferuje ponad czterysta
  modeli, a zmierzono około piętnastu.
- **Czasy są orientacyjne**: zależnie od kampanii wykonywano od trzech do sześciu tłumaczeń równolegle,
  a przepustowość dostawcy zmienia się w ciągu dnia.
- **Są to obserwacje z określonego czasu**: modele zmieniają się pod tą samą nazwą, a dokumenty
  użytkownika nie są naszymi dokumentami.

Aby powtórzyć pomiar na swoich dokumentach, korzystając z utrwalonej kopii pliku:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Współtworzenie

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Oba wiersze są konieczne: bez `pip install -e .` program `python -m aipmt`
odpowiada `No module named aipmt`.

Narzędzia do kontroli jakości, opcjonalne, ale zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń repozytorium (README i CHANGELOG, czternaście języków) można
wygenerować ponownie za pomocą `./regen_translations.sh --force` — domyślnie Codex i `gpt-5.6-sol` w ramach
subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` i
`REGEN_MODEL` zmieniają ścieżkę; rozliczane API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1 800 s w Codex). Szczegóły
dotyczące narzędzi znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — osobisty blog publikowany w 15 językach. Jego
  [codzienny przegląd AI](https://jls42.org/fr/news) jest każdego dnia tłumaczony
  za pomocą tego narzędzia i służy jako dokument referencyjny dla powyższych pomiarów.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Zastrzeżenie

Ten program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, zgodnie z postanowieniami
sekcji 15 i 16 GPL v3: jest dostarczany „w stanie, w jakim jest”, bez gwarancji jakości
handlowej ani przydatności do określonego celu, a jego autor nie ponosi
odpowiedzialności za szkody wynikające z jego użytkowania. Tekst
licencji ma pierwszeństwo przed tym podsumowaniem.

- **Przeczytaj ponownie przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod inline, URL-e, kotwice i cytaty w trybie `--news` — lecz nie
  nagłówki, tabele, front matter ani znaczenie zdań.
- **Dokumenty są wysyłane do wybranego dostawcy** zgodnie z jego warunkami
  użytkowania i polityką dotyczącą danych. Niektóre darmowe modele mogą
  ponownie wykorzystywać konwersacje do trenowania; model lokalny jest jedynym
  rozwiązaniem, które nie wysyła żadnych danych poza maszynę użytkownika.
- **Wywołania API są płatne.** Ten program nie ogranicza
  wydatków: długi dokument, wznowienie po błędzie lub model intensywnie wykorzystujący rozumowanie
  kosztują więcej.
- **Opublikowane pomiary są obserwacjami z określonego czasu**, a nie gwarancjami.

Nazwy wymienionych produktów i firm należą do ich odpowiednich właścicieli.
Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-5.6-sol.**
