# Tłumacz Markdown oparty na AI

🌍 [Francuski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Angielski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Hiszpański](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chiński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Niemiecki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japoński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreański](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Włoski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Niderlandzki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugalski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumuński](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Szwedzki](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status bramki jakości"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena łatwości utrzymania"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie testami"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Podatności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Oznaki problemów w kodzie"></a>
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

Tłumaczy pliki Markdown z jednego języka na inny, zachowując
strukturę: bloki kodu, kod w linii, URL, kotwice, tabele i front
matter. Jedenaście sposobów wywołania modelu — pięć API, cztery abonamenty bez
opłat za użycie, dwa routery — oraz opublikowane wyniki pomiarów pokazujące, co każdy
model rzeczywiście zachowuje.

## W skrócie

- **Jedenaście ścieżek dostępu do dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  abonamenty ChatGPT (Codex), Grok, Google (Antigravity) i Claude (Claude
  Code) bez opłat za użycie; routery OpenCode (open source, bezpłatny lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Żadnych uszkodzeń przez zgubiony token**: bloki kodu, kod w linii,
  URL, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  sprawdzane po otrzymaniu odpowiedzi. Jeśli choć jednego brakuje, plik nie jest zapisywany.
- **Długie dokumenty**: podział na segmenty zgodnie z oknem kontekstowym modelu.
- **Tryb `--news`**: chronione angielskie cytaty i flagi obsługiwane dla
  poszczególnych języków, na potrzeby artykułów z przeglądem aktualności.
- **Tryb `--eco`**: szybkie i tańsze modele.
- Opcjonalna **informacja o tłumaczeniu**, na górze, na dole lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 lub nowszy. Instalację z repozytorium opisano w sekcji
[Współtworzenie](#współtworzenie).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego do najniższego priorytetu; każde
uzupełnia tylko to, czego nie znaleziono w poprzednim.

|     | Gdzie                                            | Do czego                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                     | CI, kontenery, jednorazowe nadpisanie ustawień |
| 2   | `.env` w bieżącym katalogu (lub w katalogu nadrzędnym) | klucz przypisany do konkretnego projektu            |
| 3   | `~/.config/aipmt/.env`                        | skonfigurowany raz, obowiązuje wszędzie       |

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

`GEMINI_API_KEY` jest akceptowany zamiast `GOOGLE_API_KEY`. Plik
użytkownika uwzględnia `XDG_CONFIG_HOME` (wyłącznie ścieżka bezwzględna) i `%APPDATA%`
w systemie Windows. Jeśli nie ma klucza, polecenie wyświetla wszystkie trzy lokalizacje.

**Plik `.env` projektu nie może przekierowywać wywołań ani wybierać uruchamianego
programu.** Dostarcza klucze, nigdy adres docelowy ani plik wykonywalny: wszystkie
zmienne z `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, serwery proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane, z ostrzeżeniem. Sklonowane repozytorium nie powinno
móc przechwycić Twojego klucza ani spowodować uruchomienia własnego programu przy
pierwszym tłumaczeniu. Ten plik jest również odczytywany bez interpolacji:
`NOM=${OPENAI_API_KEY}` nie kopiuje w nim klucza. Ustaw te zmienne w
środowisku lub w `~/.config/aipmt/.env`.

Zmienne opcjonalne: `XAI_BASE_URL` (domyślnie `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekundy na wywołanie, domyślnie 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(domyślnie 600), `GROK_BIN`, `GROK_HOME` (domyślnie `~/.grok`), `GROK_TIMEOUT`
(domyślnie 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (domyślnie 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (domyślnie 600), `OPENROUTER_BASE_URL`
(wymagany `https://`), `OPENROUTER_TIMEOUT` (domyślnie 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (domyślnie 30). Każda z nich jest szczegółowo opisana w
sekcji swojego dostawcy.

## Pierwsze kroki

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` przetłumaczony na hiszpański daje `document-es.md` w `--target_dir`;
z `--include_model` — `document-es-gpt-5.6-terra.md`. Rozszerzenie zawsze zmienia się na
`.md` — `article.mdx` daje `article-en.md` — z wyjątkiem
`--keep_filename`, który zachowuje pierwotną nazwę. Istniejące tłumaczenie
jest pomijane bez `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli pozostał plik,
którego przetwarzanie się nie powiodło (lista na standardowym wyjściu błędów), `2`, jeśli przyczyną jest konfiguracja.
Plik, którego przetwarzanie się nie powiodło, nigdy nie jest zapisywany, nawet jeśli zawiedzie sam zapis:
treść jest zapisywana obok, a następnie zmieniana jest nazwa pliku. Wystarczy uruchomić ponownie.

## Który model wybrać

Pomiary przeprowadzono na dwóch rzeczywistych dokumentach, przetłumaczonych przez każdy
model na te same czternaście języków. **Wynik oznacza liczbę języków spośród czternastu, dla których
tłumaczenie zostało zapisane i nic nie różni się od źródła.**

| Model                | Jak uzyskać dostęp                 | Obszerny artykuł z przeglądem aktualności | Ten README    | Co się różni i w ilu językach                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | abonament Google (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nic w żadnym z dwóch dokumentów                                                                                                                                 |
| **Claude Sonnet 5.5** | klucz API Anthropic                 | ✅ 14/14                | ✅ 14/14     | nic w żadnym z dwóch dokumentów                                                                                                                                 |
| **Gemini 3.7 Flash**  | klucz API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 język z 14: jedno dodatkowe pogrubione słowo (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | abonament Google (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 język z 14: o jedno pogrubione słowo mniej (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | abonament ChatGPT lub klucz OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 języki z 14: o jedno pogrubione słowo mniej (ar, ja)                                                                                                                |
| **GLM-5.2**           | klucz OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 języki z 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | abonament Claude (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 język z 14 w artykule: jedno dodatkowe pogrubione słowo (zh); 1 w tym README: wiersz tabeli doklejony do poprzedniego, niewidoczny po wyrenderowaniu (ar)            |
| Claude Haiku 4.5      | abonament Claude (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 języki w artykule: nagłówek sekcji zmieniony na poziom 1 (en, pl, ro); w tym README narzędzie porównujące nie wykryło różnic, ale linki wewnętrzne zostały zdublowane po angielsku |
| Claude Sonnet 5       | klucz API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym README: link bez znaczników (sv), pogrubione słowo (zh)                              |
| Claude Haiku 4.5      | klucz API Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 języków w artykule: nagłówek sekcji zmieniony na poziom 1 — w japońskim pozostał po francusku; żadnych różnic w tym README                                              |
| Claude Haiku 5.5      | klucz API Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 języki w artykule: poziom nagłówka sekcji zmieniony lub nagłówek zdublowany (ja, ko, zh); w tym README 2 języki odrzucone z powodu utraty kodu w linii (ar, hi)    |
| Qwen 3.7 Flash        | klucz OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 język odrzucony w artykule, 5 innych wykazuje różnice; w tym README około czterdziestu słów umieszczonych w `code` (ar)                                                    |
| Grok 4.6              | abonament Grok                   | ❌ 8/14                 | bez oceny     | 5 języków z 14 odrzuconych z powodu niezwróconego kodu w linii i URL; wersja niderlandzka wykazuje różnice we wszystkim                                                               |
| GPT-OSS 20B           | model lokalny (Ollama)             | ❌ 7/14                 | bez ponownego pomiaru | 4 języki z 14 odrzucone: model pozostawiał w nich fragmenty po francusku, zabezpieczenie je zatrzymało                                                                  |
| MiMo v2.5 (bezpłatny)   | OpenCode Zen, bez konta         | ❌ 11/14                | bez ponownego pomiaru | 1 język odrzucony; utracona sekcja w języku polskim                                                                                                                  |
| Mistral Large         | klucz API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **znika cała sekcja**: 1 język w artykule (hi), 3 w tym README (ar, hi, ko) — oraz 3 języki odrzucone w artykule                                |
| DeepSeek V4 Flash     | klucz OpenRouter                    | ❌ 3/14                 | bez ponownego pomiaru | 10 języków z 14 odrzuconych; 37 minut na język                                                                                                                 |
| Claude Opus 5.5       | abonament Claude (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | artykuł odrzucony we wszystkich 14 językach przez zabezpieczenia Opus z powodu krótkiej wiadomości z biologii; żadnych różnic w tym README                                               |

|     | Co oznacza symbol                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | przetłumaczono wszystkie czternaście języków i nic nie różni się od źródła                                                                                                                                       |
| ⚠️  | przetłumaczono wszystkie czternaście języków; różnice dotyczą **znaczników** — pogrubionego słowa, `code`, linku tracącego nawiasy kwadratowe. Nie brakuje żadnego tekstu, URL, bloku kodu ani sekcji |
| ❌  | co najmniej jednego języka nie udało się przetłumaczyć — plik został odrzucony i nie został zapisany — **lub** w zapisanym pliku brakuje treści                                                                      |

Co z tego wynika:

- **Odrzucone tłumaczenie nie jest uszkodzonym tłumaczeniem.** Gdy w odpowiedzi
  brakuje tokenu, plik nie jest zapisywany, a język jest uznawany za
  odrzucony. Tak dzieje się z Grok w artykule: cztery fragmenty kodu w linii i
  trzy URL utracone już w pierwszym segmencie, we wszystkich pięciu pismach innych niż łacińskie.
- **Model może odrzucić cały dokument z powodu jednego zdania.** Opus 5.5
  tłumaczy ten README bez żadnych różnic, ale nie tłumaczy żadnego artykułu z przeglądem aktualności:
  jego zabezpieczenia zatrzymują odpowiedź przy krótkiej wiadomości z biologii. Plik nie jest
  zapisywany, a aipmt podaje przyczynę.
- **Ta ochrona nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik, który narzędzie zapisuje
  bez zastrzeżeń — tak jest w przypadku Mistral. Tych elementów nie da się
  zastąpić tokenem, a obecne zabezpieczenia ich nie kontrolują;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego README**: jego sesja CLI wygasła po dwunastu
  językach, z których jedenaście nie wykazywało różnic. Przerwanej serii pomiarów nie przyznaje się oceny.
- **Gęstość treści dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze
  zwykłymi README, ale zawodzi przy artykule pełnym linków, również w
  języku niderlandzkim.

Daty i dokumenty: kolumnę „Ten README” zmierzono 9 września 2026
na ustalonej wersji tego pliku (785 wierszy, 285 fragmentów kodu w linii, 89 wierszy
tabel), od tego czasu zmodyfikowanej — z wyjątkiem wierszy Antigravity i Claude Code,
zmierzonych 26 września na krótszej wersji opublikowanej wraz z 1.14.0
(600 wierszy, 257 fragmentów kodu w linii, 85 wierszy tabel), oraz wierszy Claude
Sonnet 5.5, Haiku 5.5 i Haiku 4.5 przez API, zmierzonych 18 października na
tej samej wersji. Kolumna „Obszerny artykuł z przeglądem aktualności” pochodzi z serii pomiarów
z 4 i 5 września na artykule liczącym 589 wierszy, z wyjątkiem wiersza Grok, ponownie zmierzonego
9 września na innym wydaniu tego samego przeglądu, wierszy Antigravity i
Claude Code, zmierzonych 26 września na tym samym artykule, oraz tych trzech wierszy
Claude, zmierzonych 18 października. Pełne tabele, czasy i procedura znajdują się
w sekcji [Szczegółowe pomiary](#szczegółowe-pomiary).
## Wszystkie opcje

| Opcja                   | Opis                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia (alternatywa dla `--source_dir`)                                             |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown (domyślnie: `content/posts`)                                   |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików (domyślnie: `traductions_en`)                                    |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                                                                  |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                                                                   |
| `--model`                | Konkretny model do użycia                                                                                  |
| `--eco`                  | Używaj modeli ekonomicznych                                                                              |
| `--use_mistral`          | Używaj API Mistral AI                                                                                     |
| `--use_claude`           | Używaj API Claude                                                                                         |
| `--use_gemini`           | Używaj API Gemini                                                                                         |
| `--use_grok`             | Używaj API xAI (Grok) — wymaga `XAI_API_KEY`                                                           |
| `--use_codex`            | Używaj CLI Codex w ramach limitu abonamentu ChatGPT                                                    |
| `--use_grok_cli`         | Używaj CLI Grok w ramach limitu abonamentu Grok                                                        |
| `--use_antigravity`      | Używaj CLI Antigravity (`agy`) w ramach limitu abonamentu Google AI Pro lub Ultra                       |
| `--use_claude_code`      | Używaj CLI Claude Code (`claude -p`) w ramach limitu abonamentu Claude Pro lub Max                      |
| `--use_opencode`         | Używaj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle` |
| `--use_openrouter`       | Używaj OpenRouter — wymaga `OPENROUTER_API_KEY` i `--model fournisseur/modèle`                          |
| `--force`                | Wymuś ponowne tłumaczenie                                                                                       |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                                                          |
| `--news`                 | Tryb wiadomości: chroni cytaty EN, obsługuje flagi według języka                                      |
| `--add_translation_note` | Dodaj notę o tłumaczeniu                                                                                |
| `--note_position`        | Położenie noty: `top`, `bottom` (domyślnie) lub `both`                                                     |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                                            |
| `--include_model`        | Uwzględnij nazwę modelu w pliku wyjściowym                                                            |
| `--reasoning_effort`     | Poziom rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Dziewięć flag `--use_*` wzajemnie się wyklucza: połączenie dwóch jest
odrzucane.

## Dostawcy

### Przez API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` przełącza na wariant ekonomiczny każdego dostawcy.

| Dostawca    | Jakość (domyślnie)                                                     | Ekonomiczny (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.8-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (także `gpt-5.6-sol`, `terra` i `luna` przez `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | tak samo — `--eco` bez wpływu |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, poziom rozumowania `low`                                               | tak samo — `--eco` bez wpływu |
| OpenCode    | `--model provider/modèle` wymagany                                | tak samo — `--eco` bez wpływu |
| OpenRouter  | `--model fournisseur/modèle` wymagany                             | tak samo — `--eco` bez wpływu |

Gemini 3.7 Flash, domyślny do wersji 1.17.1, jest wycofywany: Google udostępnia
w jego miejsce Gemini 3.8 Flash, a `--model gemini-3.7-flash` pozostaje akceptowany.
Przejściowa awaria API Gemini (503, 429, przekroczenie limitu czasu) powoduje ponowienie
wywołania do trzech razy, po 10, 20, a następnie 40 sekundach. Próba,
która pozostała bez odpowiedzi, jest przerywana po 5 minutach, a następnie ponawiana
w ten sam sposób: milczący serwer powoduje niepowodzenie segmentu po najwyżej około
dwudziestu minutach, zamiast blokować go bez końca.

### W ramach abonamentu ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie zużywa limit
abonamentu ChatGPT, bez klucza API ani opłat za użycie.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Plik wykonywalny jest wyszukiwany w `CODEX_BIN`, następnie w `PATH`, a potem w pakiecie
  `openai-codex-cli-bin`. `~/.codex/auth.json` nigdy nie jest odczytywany.
- `OPENAI_API_KEY` i `CODEX_API_KEY` są usuwane ze środowiska
  podprocesu: obecność klucza nigdy nie powoduje przełączenia na API.
- Każdy segment kosztuje co najmniej jedną „wiadomość” w oknie 5 godzin — dwie,
  jeśli jego walidacja się nie powiedzie i zostanie ponowiony. OpenAI podaje szacunkowo
  250-2 000 wiadomości/5 h dla `gpt-5.6-luna` (`--eco`) oraz
  10-100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-sol`, domyślny do wersji 1.16.3, `--model gpt-5.6-terra`
  i `--model gpt-5.6-luna` również korzystają z abonamentu.
- Błąd 429 z serwera nie powoduje utraty pliku: Codex łączy się ponownie samodzielnie,
  aipmt czeka na koniec tury, a jeśli ostatecznie pozostaje błąd 429, segment
  jest ponawiany po 30, a następnie 60 sekundach. Model, do którego konto nie ma dostępu, zwraca błąd 400 „model nie jest
  obsługiwany podczas korzystania z Codex z kontem ChatGPT”.
- Wolniejsze niż API, a różnica rośnie wraz z dokumentem: dla tego README
  mediana wynosi 6 min 46 s na język przy `gpt-5.6-sol`, wobec 36 s dla
  `gemini-3.7-flash`.
- Odrzucane w CI (ustawione `CI` lub `GITHUB_ACTIONS`): uwierzytelnianie abonamentu
  odbywa się przez osobisty plik sesji, dla którego nie ma miejsca na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach abonamentu Grok: `--use_grok_cli`

Ta sama zasada z oficjalnym CLI Grok Build, w ramach abonamentu SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Sandbox systemu operacyjnego Grok nie działa
  na wielu nowszych stanowiskach z Linuksem (AppArmor, gniazda środowiska uruchomieniowego
  kontenerów), a profil, którego nie można zastosować, uruchamia się bez izolacji
  i bez ostrzeżenia. Skrypt domyślnie nie żąda więc żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` CLI, w tym regule catch-all `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast usuwać ochronę bez
  powiadomienia. `GROK_TRANSLATE_SANDBOX=read-only` wymaga sandboxa systemu operacyjnego, a uruchomienie
  kończy się niepowodzeniem, jeśli maszyna nie może go zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, a żadne
  polecenie nie pozwala go odczytać: seria tłumaczeń może zużyć limit przeznaczony na rozmowy
  bez żadnego sygnału.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach abonamentu Google: `--use_antigravity`

Ta sama zasada z `agy`, oficjalnym CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie zużywa limit abonamentu zamiast
być rozliczane za token. To jedyna droga do tego limitu: Gemini CLI nie
obsługuje już tych kont od 18 czerwca 2026
([ogłoszenie](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
a SDK Antigravity akceptuje wyłącznie klucz API lub projekt Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Żadna płatna ścieżka nie pozostaje otwarta.** agy otrzymuje z Twojego
  środowiska wyłącznie zamkniętą listę zmiennych — `PATH`, język i strefę czasową,
  terminal, tożsamość, proxy i certyfikaty, magistralę sesji — i żadnego klucza:
  kilka jego zmiennych przełącza wywołanie bez żadnego komunikatu (zaobserwowano:
  jedna wysyła dokument do bramy strony trzeciej, inna do płatnego projektu
  Google Cloud), a przy każdym przeglądzie lista blokowanych zmiennych okazywała się niepełna.
  Przed każdym segmentem `agy -p /config`, które nie zużywa limitu, musi wykazać
  wyłączone płatne kredyty AI oraz brak klucza API i projektu Google Cloud —
  brak ustawienia oznacza odmowę — w przeciwnym razie nic nie jest tłumaczone; dziennik każdego
  wywołania musi następnie potwierdzić korzystanie z abonamentu (`authMethod=consumer`), inaczej
  odpowiedź jest odrzucana.
- **Izolacja.** Każde wywołanie działa w prywatnym, jednorazowym katalogu domowym,
  z agentem tłumaczącym bez narzędzi: Twoje ustawienia, reguły,
  pluginy, serwery MCP i hooki agy nie są tam przenoszone, nic nie trafia do Twojej
  historii, a dane logowania pozostają w pęku kluczy, którego aipmt nigdy nie odczytuje.
  Gdy agent nie zostanie znaleziony, agy po cichu wraca do swojego agenta programistycznego
  i jego narzędzi: pełny wiersz dziennika musi potwierdzić właściwego agenta —
  dokument cytujący ten komunikat go nie zastępuje — w przeciwnym razie następuje odmowa.
- **Platformy**: Linux, w sesji z pękiem kluczy (magistrala sesji
  D-Bus, Secret Service); macOS jest akceptowany, choć nie przeprowadzono na nim pomiarów. Odrzucane
  w Windows, gdzie agy nie odczytuje zmiennych izolujących każde wywołanie, oraz
  w Linuksie bez magistrali sesji — sesja SSH, kontener, serwer: agy
  zapisuje tam swój token w pliku w `~/.gemini`, który izolacja ukrywa.
  Odmowa następuje przed uruchomieniem, z podaniem przyczyny, zamiast po minucie
  oczekiwania na kod logowania.
- **Modele**: te z `agy models`. Modele Gemini mają poziom rozumowania w nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez przyrostka jest odrzucana przed wywołaniem,
  a `--reasoning_effort` nie ma wpływu. Domyślnie `gemini-3.8-flash-medium`,
  a `gemini-3.7-flash-low` w trybie `--eco`; kampanie pomiarowe, na podstawie których je wybrano,
  opisano w [Szczegółowych pomiarach](#szczegółowe-pomiary). Claude i GPT-OSS
  mają własny, znacznie mniejszy limit: około 1 % okna
  5 godzin na zmierzone wywołanie, wobec 0,05 % w przypadku Flash.
- **Limit**: dla każdej grupy okno 5 godzin i okno tygodniowe,
  proporcjonalnie do kosztu w tokenach. Pomiary na koncie autora: około
  16 punktów okna 5 godzin na milion znaków źródłowych przy
  `gemini-3.8-flash-medium`, 14 przy `gemini-3.7-flash-medium` i 7 do 8 przy
  niskim poziomie rozumowania — README o długości 40 000 znaków kosztuje więc nieco ponad
  pół punktu. Limit tygodniowy zależy natomiast od poziomu abonamentu. Ponowienie odbywa się
  zgodnie z tym, co agy uznaje za możliwe do ponowienia; w przeciwnym razie wyczerpane okno nigdy
  nie powoduje ponowienia: każdy plik kończy się niepowodzeniem aż do resetu
  wskazanego przez `/usage`.
- **Wolniejsze niż API**: dla obszernego artykułu z pomiarów mediana wynosi 3 min 59 s na
  język przy `gemini-3.8-flash-medium` i 3 min 14 s przy
  `gemini-3.7-flash-medium`, wobec 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerwanie**: Ctrl-C lub zamknięcie terminala zatrzymują agy wraz z
  poleceniem, zamiast pozwalać mu dokończyć turę kosztem Twojego limitu; to samo dotyczy
  Codex, Grok CLI i OpenCode. Pod `nohup` tłumaczenie jest kontynuowane.
- Odrzucane w CI (ustawione `CI` lub `GITHUB_ACTIONS`): dane logowania znajdują się w
  osobistym pęku kluczy. Na runnerze użyj `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment, łącznie z uruchomieniem, domyślnie 900).

**Warunki korzystania: to Twoje konto jest na szali.**
[Warunki Antigravity](https://antigravity.google/terms) (sekcja 6) i jego
[FAQ](https://antigravity.google/docs/faq/) zabraniają dostępu do usługi
przez oprogramowanie stron trzecich przy użyciu logowania Antigravity — wymieniono tam Claude Code,
OpenClaw i OpenCode — pod groźbą zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokena: uruchamia oficjalny plik wykonywalny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
dokumentuje jako przeznaczony do skryptów i CI. Pracownik Google uznał za „standardowe”
uruchamianie `agy -p` z lokalnego skryptu na potrzeby własnej pracy
([oficjalne forum, 25 września 2026, odpowiedź niewiążąca](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden zapis nie rozstrzyga przypadku rozpowszechnianego narzędzia takiego jak to.

**Wyłącznie dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków
wymiana danych — prompty, odpowiedzi, metadane — może służyć do ulepszania
produktów i uczenia maszynowego Google oraz być przeglądana przez
ludzi, również w przypadku płatnego abonamentu. Rezygnacja odbywa się przez ustawienie
`enableTelemetry`, którego działanie nie jest udokumentowane i którego aipmt nie ustawia; Twoje ustawienia
agy nie są przenoszone do jego odizolowanego środowiska. Nie przesyłaj tą drogą żadnych poufnych informacji.
### W ramach abonamentu Claude: `--use_claude_code`

Ta sama zasada dotyczy `claude`, oficjalnego CLI Claude Code, w trybie `-p`: dla
osób opłacających Claude Pro lub Max tłumaczenie jest odliczane od limitu
abonamentu, zamiast być rozliczane za tokeny. Nie należy tego mylić z
`--use_claude`, API Anthropic, rozliczanym według zużycia.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Żadna płatna ścieżka nie pozostaje otwarta, a każde wywołanie to potwierdza.** Claude
  Code otrzymuje z Twojego środowiska wyłącznie zamkniętą listę zmiennych — bez
  klucza API, tokenu, dostawcy chmurowego ani znacznika sesji Claude Code,
  z której uruchomiono by aipmt. Przed pierwszym segmentem `claude auth status` musi
  pokazać połączenie w ramach abonamentu, bez klucza Console, a `/usage`, które nie zużywa
  żadnego limitu, musi to potwierdzić; każde wywołanie potwierdza to następnie w swoim
  zdarzeniu inicjalizacji, w przeciwnym razie odpowiedź jest odrzucana.
- **Wyłącz „extra usage”** (claude.ai, Ustawienia → Zużycie), aby
  koszt pozostał na poziomie zero euro: po włączeniu funkcja przejmuje obsługę po wyczerpaniu limitu okna i
  nalicza opłaty bez wyświetlania błędu. aipmt zatrzymuje tłumaczenie, gdy raport
  limitu danego wywołania to zasygnalizuje, ale to wywołanie zostało już naliczone.
- **Limit współdzielony z Twoimi sesjami Claude Code.** Każde wywołanie raportuje
  wykorzystanie okien 5-godzinnych i tygodniowych; powyżej 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) żaden kolejny segment nie jest uruchamiany, aby
  nie wyczerpać zasobów potrzebnych do pracy.
- **Izolacja.** Każde wywołanie działa bez narzędzi, w prywatnym,
  tymczasowym katalogu, w trybie bez personalizacji: ani Twoje `CLAUDE.md`, ani pluginy,
  hooki, serwery MCP czy ustawienia nie są ładowane, a z sesji nic nie jest
  zachowywane. Załączniki są wyłączone: `@chemin` w Twoim dokumencie
  pozostaje tekstem i nie otwiera żadnego pliku (sprawdzone pomiarowo).
- **Modele**: domyślnie `sonnet`, z poziomem wysiłku `low`, także w `--eco`:
  `--eco` niczego na tej ścieżce nie zmienia. W pomiarach na tych samych dokumentach `haiku`
  jest dwukrotnie wolniejszy — prowadzi rozumowanie, którego nie można wyłączyć — przy
  zaledwie nieco niższym koszcie, a `opus` odmawia przetwarzania treści biologicznych (następny
  punkt). Oba pozostają dostępne przez `--model`; te aliasy wskazują
  najnowszy model ze swojej rodziny. `fable` i warianty `[1m]` są odrzucane,
  ponieważ korzystają z płatnych kredytów. `--reasoning_effort` ustawia poziom wysiłku,
  z którego tłumaczenie nie czerpie korzyści: zmierzone rozumowanie jest zerowe lub niemal zerowe.
- **Opus odmawia przetwarzania niektórych treści biologicznych.** Jego zabezpieczenia są
  bardziej rygorystyczne niż w Sonnet, a komunikat błędu Anthropic ostrzega, że
  „mogą czasem oznaczać prace związane z badaniami biologicznymi”. Wynik pomiaru: krótka
  wiadomość przeglądowa o 279 wygenerowanych cząsteczkach spowodowała odrzucenie artykułu we wszystkich czternastu
  językach. Nic nie jest zapisywane: aipmt odrzuca uciętą odpowiedź, wskazuje
  zabezpieczenia i zaleca `--model sonnet`.
- Niedostępne w CI (gdy ustawiono `CI` lub `GITHUB_ACTIONS`) oraz w Windows (bez pomiarów).
- Zmienne: `AIPMT_CLAUDE_BIN` (w przeciwnym razie `PATH`, następnie `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekundy na segment, domyślnie 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (domyślnie 0.8), `CLAUDE_CONFIG_DIR` (konto
  Claude Code, nigdy niepobierane z projektowego `.env`); katalogi robocze w
  `XDG_CACHE_HOME/aipmt/claude-code` (domyślnie `~/.cache`).

**Warunki użytkowania: odpowiedzialność ponosisz na swoim koncie.**
[Strona prawna Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nie zabrania „użytkownikowi końcowemu logowania się do niezmodyfikowanego pliku binarnego Claude Code
przy użyciu własnego abonamentu Claude”: tak właśnie działa aipmt, uruchamiając
oficjalny plik binarny i nigdy nie odczytując tokenu. Jednak Anthropic „nie zezwala
zewnętrznym deweloperom […] na kierowanie żądań przy użyciu danych uwierzytelniających planów Free, Pro lub Max
w imieniu ich użytkowników”, preferuje klucz API w narzędziach
zewnętrznych, „w tym w projektach open source”, i zastrzega sobie prawo do odliczania ich
zużycia z płatnych kredytów
([pomoc Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Żaden zapis nie rozstrzyga przypadku rozpowszechnianego narzędzia, które uruchamia plik binarny.

**Dane**: na kontach Free, Pro i Max trenowanie modeli
obejmuje również Claude Code, gdy pozwala na to ustawienie prywatności
([strona dotycząca danych](https://code.claude.com/docs/en/data-usage)). aipmt nie zachowuje
żadnego lokalnego zapisu rozmowy (`--no-session-persistence`). Nie przesyłaj tą drogą
żadnych poufnych treści.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to agent programistyczny open source (MIT), który
kieruje żądania do skonfigurowanych w nim dostawców: klucz API, abonament,
brama OpenCode Zen (darmowe modele, bez konta) lub model lokalny. Dwie
ścieżki zmierzono tutaj od początku do końca: Zen i Ollama.

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

`--model` jest obowiązkowe: bez niego OpenCode użyłby awaryjnie darmowego modelu,
którego rozmowy mogą służyć do trenowania, a ten wybór nie jest dokonywany
za Ciebie.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, mająca pierwszeństwo przed Twoją, definiuje agenta `aipmt`,
  któremu zabroniono korzystania ze wszystkich narzędzi (`permission: { "*": "deny" }`), z wyłączonym udostępnianiem
  sesji, `--pure`, nigdy `--auto`;
- pusty, tymczasowy katalog roboczy, ustawione `OPENCODE_DISABLE_PROJECT_CONFIG` i
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstawia do
  promptu `AGENTS.md` z bieżącego katalogu oraz `~/.claude/CLAUDE.md`. Globalny
  `~/.config/opencode/AGENTS.md` nadal jest wstawiany, OpenCode nie pozwala
  go wykluczyć;
- kontrakt wyjścia: kod zakończenia 0, brak zdarzeń `error`, brak wywołań
  narzędzi, ostatni krok w `stop`, niepusty tekst oraz faktycznie załadowany agent `aipmt`
  — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  cichy powrót do agenta programistycznego;
- żaden klucz z `aipmt` nie jest przekazywany, poza `OPENCODE_API_KEY`, kluczem
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  `.env` narzędzia `aipmt`.

Warto wiedzieć:

- Darmowe modele Zen zmieniają się, mają nieudokumentowane limity, a
  ich rozmowy mogą służyć do trenowania: nadają się do dokumentacji
  publicznej, nie do treści prywatnych.
- Model lokalny musi oferować co najmniej 16 k tokenów kontekstu, ponieważ segmenty
  mają do 16 000 znaków. Ollama często ustawia 4 096: należy użyć
  `Modelfile` z `PARAMETER num_ctx 32768`.
- `--eco` nie ma wpływu; `--reasoning_effort` jest przekazywane bez zmian jako
  `--variant` OpenCode.
- OpenCode zapisuje każdą sesję w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, następnie `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekundy na segment, domyślnie 600). `OPENCODE_CONFIG`
  jest przekazywane bez zmian do OpenCode.

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

`reasoningEffort: "none"` wyłącza rozumowanie, które Ollama domyślnie aktywuje w tych
modelach i którego Modelfile nie może wyłączyć. Pomiar dla zdania złożonego z
sześciu słów: 919 tokenów rozumowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według zużycia, z jednym saldem kredytów, zapewniający dostęp do
modeli hostowanych przez podmioty zewnętrzne — w tym otwartych modeli chińskich, których żaden
inny provider tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest obowiązkowe. Preflight, wykonywany przed naliczeniem jakichkolwiek opłat, uwzględnia
dwie specyficzne cechy routingu:

- **Ten sam model jest obsługiwany przez dziesiątki dostawców hostingu o różnych
  limitach** — dla `z-ai/glm-5.3-flash` jest ich 23, w tym jeden z limitem
  2 048 tokenów wyjścia. Preflight odczytuje `/api/v1/models/{modèle}/endpoints`,
  odrzuca dostawców z limitem poniżej 8 000 tokenów wyjścia lub z pogorszonym stanem usługi i
  przypina pozostałych za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki za wyjście** — 107 tokenów zamiast 2 przy
  odpowiedzi „OK” modelu `z-ai/glm-5.2`. Domyślnie jest wyłączone; modele,
  które go wymagają, otrzymują najniższy akceptowany poziom wysiłku, ponieważ ustawienie domyślne
  z katalogu może wyczerpać limit wyjścia przed końcem tłumaczenia.
  `--reasoning_effort` zachowuje pierwszeństwo.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model z limitem poniżej 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8 400 na prompt i segment, co najmniej 8 000 na wyjście.
- Slug nieobecny w katalogu, niedostępny katalog lub brak
  dostawcy hostingu spełniającego wymagany limit zatrzymują polecenie.
- `finish_reason=length` z pustym wyjściem oznacza budżet zużyty na
  rozumowanie, a nie ucięcie: komunikat rozróżnia te przypadki.
- `--eco` nie ma wpływu.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Adnotacja o tłumaczeniu

`--add_translation_note` dodaje adnotację w `bottom` (domyślnie), `top` (po
front matter) lub `both` (`--note_position`), w formacie `legacy` (pogrubiony
akapit, domyślnie) lub `marker` (`--note_format`). Format `marker` to
niewidoczna definicja odwołania Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje pogrubiony cytat: czytelny na GitHub, możliwy do wykorzystania podczas buildu przez
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary dotyczą tłumaczeń faktycznie wykonanych za pomocą `aipmt`, na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** zlicza pliki przepuszczone przez mechanizmy kontrolne; **Bez
rozbieżności** te, w których `scripts/compare_structure.py` niczego nie wykrywa — ta sama liczba
sekcji, podtytułów, linków, unikatowych URL, bloków kodu,
fragmentów kodu inline, wierszy tabel, bloków cytatów i pogrubionych słów.

„Bez rozbieżności” oznacza „niczego nie wykryto”, a nie „identyczne”: narzędzie porównujące
zlicza elementy bez czytania ich zawartości. Nie sygnalizuje ani usuniętego nagłówka
poziomu 4, ani zastąpienia tekstu kodu inline, ani zamienionej
flagi, ani linku wewnętrznego z dodatkowym nawiasem,
`[texte]((#ancre))`, który już donikąd nie prowadzi — i nie ocenia
języka.

### Obszerny artykuł przeglądowy, tryb `--news`

Wydanie [przeglądu AI z jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty angielskie. Seria testów
z 4 i 5 września 2026.

| Model                                          | Dostęp              | Zapisane | Bez rozbieżności   | Mediana/język |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | abonament Google  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abonament Google  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abonament ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | abonament Claude  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | abonament Claude  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokalnie              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abonament Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | abonament Claude  | 0/14    | ❌ 0/14      | —              |

Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): zapisano 9 języków z 14, 8 bez rozbieżności. To ten wynik
widnieje w tabeli na początku. Nie uwzględniono trzech przerwanych
serii testów: `qwen3.5-27b` (9 języków) i `kimi-k2.6` (4) z powodu braku kredytów,
`z-ai/glm-5.3-flash`, którego dwa niepowodzenia wynikały z ustawienia rozumowania
od tego czasu korygowanego przez provider. Wiersze OpenRouter zmierzono przy
domyślnych ustawieniach routera, przed `--use_openrouter`; `z-ai/glm-5.2`,
zmierzony ponownie z dostarczonym providerem, daje ten sam wynik 14/14. Wyniki
przeliczono 10 września aktualnym narzędziem porównującym: `qwen3.8-flash` i
`qwen3.7-flash` zyskują po jednym języku względem pierwszej
publikacji, pozostałe pozostają bez zmian.

Wiersze `--use_antigravity` zmierzono 26 września na tym samym
artykule, przy czterech tłumaczeniach równolegle: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W języku angielskim każdy sam usunął
trzy wiersze francuskiego tłumaczenia pod cytatami, bez wymyślania
flagi, a cytaty angielskie pozostały nienaruszone: awaryjne czyszczenie nie miało
nic do zrobienia. W `--eco` (`gemini-3.7-flash-low`), tylko dla czterech języków
(en, ja, ar, hi): zapisano 4 z 4, wszystkie bez rozbieżności, mediana 1 min 52 s.
Test kontrolny tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 cytaty angielskie), przetłumaczonym poza
blogiem przez `gemini-3.7-flash-medium`: zapisano 14 z 14, wszystkie bez rozbieżności, od 87 do
128 s na język.

Wiersze `--use_claude_code` zmierzono 26 września na tym samym
artykule, przy czterech tłumaczeniach równolegle, z poziomem wysiłku `low`. Przy `sonnet`
cytaty angielskie pozostały nienaruszone we wszystkich czternastu językach, a po angielsku
model sam usunął wiersze francuskiego tłumaczenia, bez wymyślania
flagi. `opus` nie zapisał żadnego języka: w każdym jego zabezpieczenia
zatrzymały odpowiedź na ostatnim segmencie z powodu krótkiej wiadomości o 279 cząsteczkach
wygenerowanych dla miejsca wiązania. Wysłana osobno wiadomość jest odrzucana
w kategorii „bio”; `sonnet` przetłumaczył ją we wszystkich językach. `haiku` zapisuje
czternaście języków; w trzech (en, pl, ro) nagłówek sekcji przechodzi z
poziomu 2 na poziom 1. Prowadzi rozumowanie, którego nie można wyłączyć — 61 % jego
tokenów wyjścia — stąd ponad dwukrotnie dłuższy czas niż dla `sonnet`.

Wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5`
zmierzono 18 października przez API Anthropic, na tym samym artykule, przy czterech
tłumaczeniach równolegle na model. Sonnet 5.5 nie pozwala wyłączyć
rozumowania: aipmt wysyła mu najniższe akceptowane ustawienie, a jego
odpowiedzi nie zawierają śladów rozumowania. Zapisuje czternaście języków bez rozbieżności i bez
ponawiania segmentów; po angielsku sam usunął wiersze
francuskiego tłumaczenia, bez wymyślania flagi, a cytaty angielskie pozostały
wszędzie nienaruszone. Haiku 5.5 jest mierzony z adaptacyjnym rozumowaniem: przy wyłączonym
rozumowaniu pozostawiał całe akapity po francusku, co mechanizm kontrolny odrzuca —
zapisano 3 języki z 14. Oba modele Haiku potykają się o tę samą krótką wiadomość: Haiku 5.5
zmienia poziom jej nagłówka lub powiela go po japońsku, koreańsku i
chińsku, Haiku 4.5 zmienia go na poziom 1 w siedmiu językach, a w wersji
japońskiej pozostawia go po francusku. Haiku 4.5 kosztuje 3,67 $ za oba dokumenty we
wszystkich czternastu językach, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026: 785 wierszy, 285 fragmentów kodu inline, 40
znaczników zamykających bloki, 89 wierszy tabel. Cztery tłumaczenia równolegle.

| Model                                          | Zapisane | Bez odchyleń | Mediana/język | Co się różni                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nic                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nic                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nic według narzędzia porównującego; zduplikowane linki wewnętrzne (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nic                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nic                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | jedno pogrubione słowo (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | jedno pogrubione słowo (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | jeden wiersz tabeli sklejony z poprzednim (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | jeden link (sv), jedno pogrubione słowo (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | jedno pogrubione słowo (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | jedno pogrubione słowo (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 dodanych fragmentów kodu inline w arabskim; pogrubienie (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 odrzucone języki (ar, hi): utrata fragmentów kodu inline w odpowiedzi        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | utrata jednej sekcji (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh) |

Dwie przerwane serie pomiarów nie zostały ocenione: Grok, którego sesja CLI wygasła
po dwunastu językach (jedenaście bez odchyleń), oraz `qwen3.8-flash`, którego dostawca
zwrócił HTTP 429 po dwóch. `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie zostały ponownie zmierzone na tej wersji; na wersji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisywał 9 tłumaczeń z 14, w tym odpowiednio 7
i 1 bez odchyleń.

Wiersze `--use_antigravity` i `--use_claude_code` nie zostały zmierzone na
zamrożonej wersji, lecz 26 września na wersji opublikowanej wraz z 1.14.0 — a
wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5` 18
października, na tej samej: 600 wierszy, 257 fragmentów kodu inline, 30 znaczników zamykających bloki, 85
wierszy tabel. Jako
wersja krótsza o 185 wierszy nie pozwala na bezpośrednie porównanie z pozostałymi wierszami;
te wiersze można natomiast porównywać ze sobą. Jeśli chodzi o linki wewnętrzne, których
narzędzie porównujące nie sprawdza, `gemini-3.8-flash-medium` zachował je bez zmian we
wszystkich czternastu językach, `gemini-3.7-flash-medium` uszkodził je we włoskim;
`sonnet` i `opus` zachowały je bez zmian wszędzie, `haiku` zduplikował je w
angielskim; `claude-sonnet-5-5` i `claude-haiku-4-5` zachowały je bez zmian we
wszystkich czternastu językach, `claude-haiku-5-5` w dwunastu, w których zapisał tłumaczenia.

### Cztery pliki README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane bez zmian z GitHub — dokumenty
łatwiejsze niż dwa poprzednie. Seria pomiarów obejmowała modele
mające trudności; Gemini służy tu jako punkt odniesienia.

| Model                    | Zakres                  | Zapisane | Bez odchyleń   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projekty × 14 języków     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków     | 55/56   | ❌ 47/56     |
| `grok-4.6` (subskrypcja)   | 4 projekty × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Czym te pomiary nie są

- **Nie są wyczerpującym rankingiem**: sam OpenRouter oferuje ponad czterysta
  modeli, a zmierzono około piętnastu.
- **Czasy są orientacyjne**: od trzech do sześciu tłumaczeń równolegle zależnie od
  serii pomiarów, a przepustowość dostawcy zmienia się w ciągu dnia.
- **To obserwacje z określonego dnia**: modele zmieniają się pod tą samą nazwą, a wasze
  dokumenty różnią się od naszych.

Aby powtórzyć pomiar na własnych dokumentach, na zamrożonej kopii pliku:

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

Oba wiersze są konieczne: bez `pip install -e .` polecenie `python -m aipmt`
zwraca `No module named aipmt`.

Narzędzia kontroli jakości, opcjonalne, ale zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń w repozytorium (README i CHANGELOG, czternaście języków)
regeneruje się za pomocą `./regen_translations.sh --force` — domyślnie Codex i `gpt-6.1-sol` w ramach
subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` i
`REGEN_MODEL` zmieniają sposób działania: `antigravity` nadal korzysta z subskrypcji,
tym razem Google, i działa bez specjalnego zezwolenia; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1 800 s dla Codex i
Antigravity). Szczegóły dotyczące narzędzi znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — osobisty blog publikowany w 15 językach. Jego
  [codzienny przegląd wiadomości o AI](https://jls42.org/fr/news) jest tłumaczony każdego dnia
  za pomocą tego narzędzia i służy jako dokument referencyjny w powyższych pomiarach.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE, wersja 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Ostrzeżenie

Ten program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, zgodnie z postanowieniami
sekcji 15 i 16 GPL v3: dostarczany „w stanie, w jakim jest”, bez gwarancji wartości
handlowej ani przydatności do określonego celu, a jego autor nie ponosi
odpowiedzialności za szkody wynikające z jego używania. Tekst
licencji ma pierwszeństwo przed tym podsumowaniem.

- **Sprawdź tekst przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod inline, adresy URL, kotwice i cytaty w trybie `--news` — nie obejmują
  nagłówków, tabel, front matter ani sensu zdań.
- **Wasze dokumenty trafiają do wybranego dostawcy**, zgodnie z jego warunkami
  użytkowania i polityką dotyczącą danych. Niektóre bezpłatne modele mogą
  wykorzystywać wasze rozmowy do trenowania, a warunki Antigravity
  pozwalają Google wykorzystywać je ponownie i przekazywać do przeglądu ludziom,
  również w przypadku płatnej subskrypcji; model lokalny to jedyne rozwiązanie, przy którym
  żadne dane nie opuszczają waszego komputera.
- **Wywołania API są płatne.** Ten program nie ogranicza
  wydatków: długi dokument, ponowienie po błędzie lub model, który dużo rozumuje,
  kosztują więcej.
- **Opublikowane pomiary są obserwacjami z określonego dnia**, a nie gwarancjami.

Wymienione nazwy produktów i firm należą do ich odpowiednich właścicieli.
Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z fr na pl za pomocą gpt-6.1-sol.**
