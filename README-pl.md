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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
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
strukturę: bloki kodu, kod w tekście, URL, kotwice, tabele i front
matter. Jedenaście sposobów wywołania modelu — pięć API, cztery subskrypcje bez
opłat za użycie, dwa routery — oraz opublikowane pomiary tego, co każdy
model rzeczywiście zachowuje.

## W skrócie

- **Jedenaście sposobów dostępu do dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex), Grok, Google (Antigravity) i Claude (Claude
  Code) bez opłat za użycie; routery OpenCode (open source, bezpłatny lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Żadnych uszkodzeń przez utracony token**: bloki kodu, kod w tekście,
  URL, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  sprawdzane po otrzymaniu odpowiedzi. Jeśli któregoś brakuje, plik nie jest zapisywany.
- **Długie dokumenty**: podział na segmenty zgodnie z oknem kontekstowym modelu.
- **Tryb `--news`**: chronione cytaty angielskie i flagi obsługiwane
  zależnie od języka, do artykułów z przeglądem nowości.
- **Tryb `--eco`**: szybkie i tańsze modele.
- Opcjonalna **adnotacja o tłumaczeniu**, na górze, na dole lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 lub nowszy. Instalacja z repozytorium: zobacz
[Współtworzenie](#współtworzenie).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego do najniższego priorytetu; każde
uzupełnia tylko to, czego nie dostarczyło poprzednie.

|     | Gdzie                                         | Do czego                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                           | CI, kontenery, jednorazowe nadpisanie  |
| 2   | `.env` w bieżącym katalogu (lub katalogu nadrzędnym) | klucz przypisany do projektu          |
| 3   | `~/.config/aipmt/.env`                        | jednorazowa konfiguracja, działa wszędzie |

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

`GEMINI_API_KEY` jest akceptowany zamiast `GOOGLE_API_KEY`. Lokalizacja pliku
użytkownika zależy od `XDG_CONFIG_HOME` (tylko ścieżka bezwzględna) i `%APPDATA%`
w systemie Windows. Bez klucza polecenie wyświetla wszystkie trzy lokalizacje.

**Plik `.env` projektu nie może przekierowywać wywołań ani wybierać uruchamianego
programu.** Dostarcza klucze, nigdy adresu docelowego ani pliku wykonywalnego: wszystkie
zmienne typu `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane, z ostrzeżeniem. Sklonowane repozytorium nie powinno
móc przechwycić Twojego klucza ani nakłonić Cię do uruchomienia własnego programu przy
pierwszym tłumaczeniu. Ten plik jest również odczytywany bez interpolacji:
`NOM=${OPENAI_API_KEY}` nie kopiuje w nim klucza. Ustaw te zmienne
w środowisku lub w `~/.config/aipmt/.env`.

Zmienne opcjonalne: `XAI_BASE_URL` (domyślnie `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekundy na wywołanie, domyślnie 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(domyślnie 600), `GROK_BIN`, `GROK_HOME` (domyślnie `~/.grok`), `GROK_TIMEOUT`
(domyślnie 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (domyślnie 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (domyślnie 600), `OPENROUTER_BASE_URL`
(wymagane `https://`), `OPENROUTER_TIMEOUT` (domyślnie 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (domyślnie 30). Każda jest szczegółowo opisana
w sekcji swojego dostawcy.

## Pierwsze kroki

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` po przetłumaczeniu na hiszpański daje `document-es.md` w `--target_dir`;
z `--include_model` — `document-es-gpt-5.6-terra.md`. Rozszerzenie zawsze zmienia się na
`.md` — `article.mdx` daje `article-en.md` — z wyjątkiem użycia
`--keep_filename`, które zachowuje oryginalną nazwę. Istniejące tłumaczenie
jest pomijane bez `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli pozostał plik,
którego przetwarzanie się nie powiodło (lista na standardowym wyjściu błędów), `2`, jeśli problem dotyczy konfiguracji.
Plik, którego przetwarzanie się nie powiodło, nigdy nie jest zapisywany, nawet jeśli błąd wystąpi podczas samego zapisu:
zawartość jest zapisywana obok, a następnie plik otrzymuje docelową nazwę. Wystarczy uruchomić ponownie.

## Który model wybrać

Pomiary przeprowadzono na dwóch rzeczywistych dokumentach, tłumaczonych przez
każdy model na te same czternaście języków. **Liczba oznacza liczbę języków spośród czternastu, dla których
tłumaczenie zostało zapisane i nic nie różni się od źródła.**

| Model                 | Jak uzyskać dostęp                | Obszerny artykuł z przeglądem nowości | Ten README   | Co się różni i w ilu językach                                                                                                                                       |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | subskrypcja Google (Antigravity)  | ✅ 14/14                | ✅ 14/14     | nic, w żadnym z dwóch dokumentów                                                                                                                                   |
| **Claude Sonnet 5.5** | klucz API Anthropic               | ✅ 14/14                | ✅ 14/14     | nic, w żadnym z dwóch dokumentów                                                                                                                                   |
| **Gemini 3.7 Flash**  | klucz API Google                  | ✅ 14/14                | ⚠️ 13/14     | 1 język na 14: jedno dodatkowe pogrubione słowo (ja)                                                                                                                |
| **Gemini 3.7 Flash**  | subskrypcja Google (Antigravity)  | ✅ 14/14                | ⚠️ 13/14     | 1 język na 14: o jedno pogrubione słowo mniej (ko)                                                                                                                  |
| **GPT-5.6 Sol**       | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14             | ⚠️ 12/14     | 2 języki na 14: o jedno pogrubione słowo mniej (ar, ja)                                                                                                             |
| **GLM-5.2**           | klucz OpenRouter                  | ✅ 14/14                | ⚠️ 11/14     | 3 języki na 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                                                         |
| Claude Sonnet 5       | subskrypcja Claude (Claude Code)  | ⚠️ 13/14                | ⚠️ 13/14     | 1 język na 14 w artykule: jedno dodatkowe pogrubione słowo (zh); 1 w tym README: wiersz tabeli doklejony do poprzedniego, niewidoczny po wyświetleniu (ar)          |
| Claude Haiku 4.5      | subskrypcja Claude (Claude Code)  | ⚠️ 11/14                | ✅ 14/14     | 3 języki w artykule: nagłówek sekcji zmieniony na poziom 1 (en, pl, ro); w tym README porównywarka nie wykryła różnic, ale linki wewnętrzne zostały zdublowane po angielsku |
| Claude Sonnet 5       | klucz API Anthropic               | ⚠️ 11/14                | ⚠️ 12/14     | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym README: link bez znaczników (sv), pogrubione słowo (zh)                                            |
| Claude Haiku 4.5      | klucz API Anthropic               | ⚠️ 7/14                 | ✅ 14/14     | 7 języków w artykule: nagłówek sekcji zmieniony na poziom 1 — po japońsku pozostał po francusku; żadnych różnic w tym README                                         |
| Claude Haiku 5.5      | klucz API Anthropic               | ⚠️ 11/14                | ❌ 12/14     | 3 języki w artykule: zmieniony poziom lub zdublowany nagłówek sekcji (ja, ko, zh); w tym README odrzucono 2 języki z powodu utraconego kodu w tekście (ar, hi)        |
| Qwen 3.7 Flash        | klucz OpenRouter                  | ❌ 8/14                 | ⚠️ 10/14     | 1 język odrzucony w artykule, 5 innych z różnicami; w tym README około czterdziestu słów zapisanych jako `code` (ar)                                         |
| Grok 4.6              | subskrypcja Grok                  | ❌ 8/14                 | nie oceniono | 5 języków na 14 odrzuconych z powodu brakującego kodu w tekście i URL w odpowiedzi; niderlandzki różni się pod każdym względem                                        |
| GPT-OSS 20B           | model lokalny (Ollama)            | ❌ 7/14                 | nie zmierzono ponownie | 4 języki na 14 odrzucone: model pozostawiał w nich fragmenty po francusku, mechanizm ochronny je zatrzymał                                                  |
| MiMo v2.5 (bezpłatny) | OpenCode Zen, bez konta           | ❌ 11/14                | nie zmierzono ponownie | 1 język odrzucony; utracona sekcja po polsku                                                                                                               |
| Mistral Large         | klucz API Mistral                 | ❌ 5/14                 | ❌ 1/14      | **znika cała sekcja**: 1 język w artykule (hi), 3 w tym README (ar, hi, ko) — oraz 3 języki odrzucone w artykule                                                     |
| DeepSeek V4 Flash     | klucz OpenRouter                  | ❌ 3/14                 | nie zmierzono ponownie | 10 języków na 14 odrzuconych; 37 minut na język                                                                                                           |
| Claude Opus 5.5       | subskrypcja Claude (Claude Code)  | ❌ 0/14                 | ✅ 14/14     | artykuł odrzucony we wszystkich 14 językach przez zabezpieczenia Opus z powodu krótkiej wiadomości z biologii; żadnych różnic w tym README                            |

|     | Co oznacza symbol                                                                                                                                                                                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | przetłumaczono wszystkie czternaście języków i nic nie różni się od źródła                                                                                                                              |
| ⚠️  | przetłumaczono wszystkie czternaście języków; różnice dotyczą **znaczników** — pogrubionego słowa, `code`, linku, który utracił nawiasy. Nie brakuje tekstu, URL, bloków kodu ani sekcji           |
| ❌  | co najmniej jednego języka nie udało się przetłumaczyć — plik został odrzucony, nie zapisany — **lub** w zapisanym pliku brakuje treści                                                                  |

Co z tego wynika:

- **Odrzucone tłumaczenie nie jest uszkodzonym tłumaczeniem.** Gdy w odpowiedzi
  brakuje tokenu, plik nie jest zapisywany, a język jest uznawany za
  odrzucony. Tak dzieje się z Grok w przypadku artykułu: cztery fragmenty kodu w tekście i
  trzy URL utracone już w pierwszym segmencie, we wszystkich pięciu systemach pisma innych niż łaciński.
- **Model może odmówić przetłumaczenia całego dokumentu z powodu jednego zdania.** Opus 5.5
  tłumaczy ten README bez żadnych różnic, ale nie tłumaczy żadnego artykułu z przeglądem nowości:
  jego zabezpieczenia zatrzymują odpowiedź na krótkiej wiadomości z biologii. Plik nie jest
  zapisywany, a aipmt wyjaśnia dlaczego.
- **Ta ochrona nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik zapisywany przez narzędzie
  bez zastrzeżeń — tak jest w przypadku Mistral. Tych elementów nie można
  zastąpić tokenem, a obecne mechanizmy ochronne ich nie sprawdzają;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego README**: jego sesja CLI wygasła po dwunastu
  językach, z których jedenaście nie miało różnic. Przerwana seria pomiarów nie podlega ocenie.
- **Gęstość treści dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze
  zwykłymi plikami README, a zawodzi przy artykule pełnym linków, także w
  języku niderlandzkim.

Daty i dokumenty: kolumnę „Ten README” zmierzono 9 września 2026
na zamrożonej rewizji tego pliku (785 wierszy, 285 fragmentów kodu w tekście, 89 wierszy
tabel), od tego czasu zmodyfikowanej — z wyjątkiem wierszy Antigravity i Claude Code,
zmierzonych 26 września na krótszej rewizji opublikowanej z wersją 1.14.0
(600 wierszy, 257 fragmentów kodu w tekście, 85 wierszy tabel), oraz wierszy Claude
Sonnet 5.5, Haiku 5.5 i Haiku 4.5 przez API, zmierzonych 18 października na
tej samej rewizji. Kolumna „Obszerny artykuł z przeglądem nowości” pochodzi z serii pomiarów
z 4 i 5 września na artykule liczącym 589 wierszy, z wyjątkiem wiersza Grok, zmierzonego ponownie
9 września na innym wydaniu tego samego przeglądu, wierszy Antigravity i
Claude Code, zmierzonych 26 września na tym samym artykule, oraz tych trzech wierszy
Claude, zmierzonych 18 października. Pełne tabele, czasy i procedura znajdują się
w [Szczegółowych pomiarach](#szczegółowe-pomiary).
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
| `--use_antigravity`      | Użyj CLI Antigravity (`agy`) w ramach limitu subskrypcji Google AI Pro lub Ultra                       |
| `--use_claude_code`      | Użyj CLI Claude Code (`claude -p`) w ramach limitu subskrypcji Claude Pro lub Max                      |
| `--use_opencode`         | Użyj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle` |
| `--use_openrouter`       | Użyj OpenRouter — wymaga `OPENROUTER_API_KEY` i `--model fournisseur/modèle`                          |
| `--force`                | Wymuś ponowne tłumaczenie                                                                                       |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                                                          |
| `--news`                 | Tryb wiadomości: chroni cytaty w języku angielskim, obsługuje flagi według języka                                      |
| `--add_translation_note` | Dodaj adnotację o tłumaczeniu                                                                                |
| `--note_position`        | Pozycja adnotacji: `top`, `bottom` (domyślnie) lub `both`                                                     |
| `--note_format`          | Format adnotacji: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                                            |
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

| Dostawca    | Jakość (domyślnie)                                                     | Wariant ekonomiczny (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (także `gpt-5.6-sol`, `terra` i `luna` przez `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | jak obok — `--eco` bez efektu |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, poziom rozumowania `low`                                               | jak obok — `--eco` bez efektu |
| OpenCode    | `--model provider/modèle` wymagane                                | jak obok — `--eco` bez efektu |
| OpenRouter  | `--model fournisseur/modèle` wymagane                             | jak obok — `--eco` bez efektu |

### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest odliczane od limitu
subskrypcji ChatGPT, bez klucza API i opłat za użycie.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Plik wykonywalny jest wyszukiwany w `CODEX_BIN`, następnie w `PATH`, a potem w pakiecie
  `openai-codex-cli-bin`. `~/.codex/auth.json` nigdy nie jest odczytywany.
- `OPENAI_API_KEY` i `CODEX_API_KEY` są usuwane ze środowiska
  podprocesu: obecność klucza nigdy nie powoduje przełączenia na API.
- Każdy segment zużywa co najmniej jedną „wiadomość” z 5-godzinnego okna — dwie,
  jeśli walidacja się nie powiedzie i nastąpi ponowna próba. OpenAI podaje
  szacunkowo 250-2 000 wiadomości/5 h dla `gpt-5.6-luna` (`--eco`) oraz
  10-100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-sol`, model domyślny do wersji 1.16.3, `--model gpt-5.6-terra`
  i `--model gpt-5.6-luna` również korzystają z subskrypcji.
- Odpowiedź 429 z serwera nie powoduje utraty pliku: Codex sam nawiązuje połączenie ponownie,
  aipmt czeka na zakończenie tury, a jeśli ostatecznie pozostanie błąd 429, segment
  jest ponawiany po 30, a następnie 60 sekundach. Model, do którego konto nie ma uprawnień, zwraca błąd 400 „model nie jest
  obsługiwany podczas korzystania z Codex za pomocą konta ChatGPT”.
- Wolniejsze niż API, a różnica rośnie wraz z dokumentem: dla tego README
  mediana wynosi 6 min 46 s na język przy `gpt-5.6-sol`, wobec 36 s dla
  `gemini-3.7-flash`.
- Niedozwolone w CI (gdy ustawiono `CI` lub `GITHUB_ACTIONS`): uwierzytelnianie subskrypcji
  odbywa się za pomocą osobistego pliku sesji, którego nie powinno być na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada z oficjalnym CLI Grok Build, w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Sandbox systemu operacyjnego w Grok nie działa
  na wielu nowszych stanowiskach z Linuksem (AppArmor, gniazda środowiska uruchomieniowego
  kontenerów), a profil, którego nie można zastosować, uruchamia się po cichu bez izolacji.
  Skrypt domyślnie nie żąda więc żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` CLI, w tym regule ogólnej `*` — jedynej
  warstwie, która odmawia uruchomienia zamiast usuwać ochronę bez
  powiadomienia. `GROK_TRANSLATE_SANDBOX=read-only` wymaga sandboxa systemu operacyjnego, a uruchomienie
  kończy się niepowodzeniem, jeśli komputer nie może go zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, a żadne
  polecenie nie pozwala go odczytać: przetwarzanie partii może bez ostrzeżenia uszczuplić limit
  przeznaczony na rozmowy.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach subskrypcji Google: `--use_antigravity`

Ta sama zasada z `agy`, oficjalnym CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie jest odliczane od limitu subskrypcji zamiast
rozliczania za tokeny. To jedyna droga do tego limitu: Gemini CLI nie
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
  środowiska tylko zamkniętą listę zmiennych — `PATH`, język i strefę czasową,
  terminal, tożsamość, proxy i certyfikaty, magistralę sesji — i żadnego klucza:
  kilka jego zmiennych po cichu przekierowuje wywołanie (potwierdzone pomiarami:
  jedna wysyła dokument do bramy podmiotu trzeciego, inna do płatnego
  projektu Google Cloud), a przy każdym przeglądzie na liście blokowanych zmiennych brakowało kolejnych pozycji.
  Przed każdym segmentem `agy -p /config`, które nie zużywa limitu, musi pokazać,
  że płatne kredyty AI są wyłączone, bez klucza API i projektu Google Cloud — brak
  ustawienia oznacza odmowę — w przeciwnym razie nic nie zostanie przetłumaczone; następnie dziennik każdego
  wywołania musi potwierdzać korzystanie z subskrypcji (`authMethod=consumer`), inaczej
  odpowiedź jest odrzucana.
- **Izolacja.** Każde wywołanie działa w prywatnym, jednorazowym katalogu domowym,
  z agentem tłumaczącym bez narzędzi: Twoje ustawienia, reguły,
  pluginy, serwery MCP i hooki agy nie są do niego przenoszone, nic nie jest dodawane do Twojej
  historii, a dane logowania pozostają w pęku kluczy, którego aipmt nigdy nie odczytuje.
  Nieodnalezienie agenta powoduje, że agy po cichu wraca do swojego agenta programistycznego
  i jego narzędzi: pełny wiersz dziennika musi potwierdzać właściwego agenta —
  dokument cytujący ten komunikat nie może go zastąpić — w przeciwnym razie następuje odmowa.
- **Platformy**: Linux, w sesji z pękiem kluczy (magistrala sesji
  D-Bus, Secret Service); macOS jest akceptowany, ale nie przeprowadzono na nim pomiarów. Niedozwolone
  w Windows, gdzie agy nie odczytuje zmiennych izolujących każde wywołanie, oraz
  w Linuksie bez magistrali sesji — sesja SSH, kontener, serwer: agy
  zapisuje tam token w pliku w `~/.gemini`, który jest ukrywany przez izolację.
  Odmowa następuje przed uruchomieniem, z podaniem przyczyny, zamiast minuty
  oczekiwania na kod logowania.
- **Modele**: dostępne w `agy models`. Modele Gemini mają poziom rozumowania w nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez sufiksu jest odrzucana przed wywołaniem,
  a `--reasoning_effort` nie ma efektu. Domyślnie `gemini-3.8-flash-medium`,
  a w trybie `--eco` — `gemini-3.7-flash-low`; serie pomiarów, na podstawie których je wybrano,
  opisano w [Szczegółowych pomiarach](#szczegółowe-pomiary). Claude i GPT-OSS
  mają własny, znacznie mniejszy limit: według pomiarów około 1% limitu
  5-godzinnego okna na wywołanie, wobec 0,05% w Flash.
- **Limit**: na grupę, okno 5-godzinne i tygodniowe, zużywane
  proporcjonalnie do kosztu w tokenach. Pomiary na koncie autora: około
  16 punktów limitu 5-godzinnego okna na milion znaków źródłowych przy
  `gemini-3.8-flash-medium`, 14 przy `gemini-3.7-flash-medium` i 7 do 8 przy
  niskim poziomie rozumowania — README o długości 40 000 znaków zużywa więc nieco ponad
  pół punktu. Limit tygodniowy zależy natomiast od wariantu subskrypcji. Ponowienie następuje
  zgodnie z tym, co agy uznaje za możliwe do ponowienia; w przeciwnym razie po wyczerpaniu limitu okna
  nigdy nie następuje ponowna próba: każdy plik kończy się niepowodzeniem aż do resetu,
  którego termin pokazuje `/usage`.
- **Wolniejsze niż API**: dla obszernego, treściwego artykułu użytego do pomiarów mediana wynosi 3 min 59 s na
  język przy `gemini-3.8-flash-medium` i 3 min 14 s przy
  `gemini-3.7-flash-medium`, wobec 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerwanie**: Ctrl-C lub zamknięcie terminala zatrzymuje agy wraz z
  poleceniem, zamiast pozwolić mu dokończyć turę kosztem Twojego limitu; to samo dotyczy
  Codex, Grok CLI i OpenCode. W `nohup` tłumaczenie jest kontynuowane.
- Niedozwolone w CI (gdy ustawiono `CI` lub `GITHUB_ACTIONS`): dane logowania są przechowywane w
  osobistym pęku kluczy. Na runnerze użyj `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, a następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment, wraz z uruchomieniem, domyślnie 900).

**Warunki korzystania: to Twoje konto ponosi konsekwencje.**
[Warunki Antigravity](https://antigravity.google/terms) (sekcja 6) i
[FAQ](https://antigravity.google/docs/faq/) zabraniają dostępu do usługi
za pośrednictwem oprogramowania innych firm przy użyciu logowania Antigravity — wymieniono tam Claude Code,
OpenClaw i OpenCode — pod groźbą zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokenu: uruchamia oficjalny plik wykonywalny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
dokumentuje dla skryptów i CI. Przedstawiciel Google uznał uruchamianie
`agy -p` z lokalnego skryptu do własnej pracy za „standardowe”
([oficjalne forum, 25 września 2026, odpowiedź niewiążąca umownie](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden dokument nie rozstrzyga przypadku narzędzia dystrybuowanego tak jak to.

**Tylko dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków
wymiana danych — prompty, odpowiedzi, metadane — może służyć ulepszaniu
produktów i uczeniu maszynowemu Google oraz być przeglądana przez
ludzi, również w przypadku płatnej subskrypcji. Rezygnacja odbywa się za pomocą ustawienia
`enableTelemetry`, którego działanie nie jest udokumentowane i którego aipmt nie ustawia; Twoje ustawienia
agy nie są przenoszone do jego odizolowanego środowiska. Nie przesyłaj tą drogą żadnych poufnych danych.
### W ramach subskrypcji Claude: `--use_claude_code`

Ta sama zasada dotyczy `claude`, oficjalnego CLI Claude Code, w trybie `-p`: dla
osób opłacających Claude Pro lub Max tłumaczenie jest odliczane od limitu
subskrypcji zamiast być rozliczane za token. Nie należy tego mylić z
`--use_claude`, API Anthropic rozliczanym według zużycia.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Żadna płatna ścieżka nie pozostaje otwarta, a każde wywołanie to potwierdza.** Claude
  Code otrzymuje ze środowiska wyłącznie zamkniętą listę zmiennych — bez
  klucza API, tokenu, dostawcy chmurowego ani znacznika sesji Claude Code,
  z której uruchomiono by aipmt. Przed pierwszym segmentem `claude auth status` musi
  pokazać połączenie przez subskrypcję, bez klucza Console, a `/usage`, które nie zużywa
  żadnego limitu, musi to potwierdzić; każde wywołanie potwierdza to z kolei w swoim
  zdarzeniu inicjalizacji, w przeciwnym razie odpowiedź zostaje odrzucona.
- **Wyłącz „extra usage”** (claude.ai, Ustawienia → Użycie), aby
  koszt pozostał zerowy: po włączeniu funkcja przejmuje obsługę po wyczerpaniu limitu okna i
  nalicza opłaty bez wyświetlania błędu. aipmt zatrzymuje tłumaczenie, gdy raport
  limitu któregoś wywołania to zasygnalizuje, ale to wywołanie zostało już rozliczone.
- **Limit współdzielony z sesjami Claude Code.** Każde wywołanie raportuje
  wykorzystanie limitów w oknie 5-godzinnym i tygodniowym; powyżej 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) nie jest uruchamiany żaden kolejny segment, aby nie
  wyczerpać zasobów potrzebnych do pracy.
- **Izolacja.** Każde wywołanie działa bez narzędzi, w prywatnym,
  tymczasowym katalogu, w trybie bez personalizacji: nie są ładowane ani Twoje `CLAUDE.md`, ani pluginy,
  hooks, serwery MCP czy ustawienia, a z sesji nic nie jest zachowywane.
  Załączniki są wyłączone: `@chemin` w dokumencie
  pozostaje tekstem i nie otwiera żadnego pliku (potwierdzone pomiarem).
- **Modele**: domyślnie `sonnet`, z poziomem wysiłku `low`, również w `--eco`:
  `--eco` niczego nie zmienia w tej ścieżce. W pomiarach na tych samych dokumentach `haiku`
  jest dwa razy wolniejszy — rozumuje i nie da się tego wyłączyć — przy
  zaledwie nieco niższym koszcie, a `opus` odmawia przetwarzania treści biologicznych (następny
  punkt). Oba pozostają dostępne przez `--model`; te aliasy wskazują
  najnowszy model ze swojej rodziny. `fable` i warianty `[1m]` są odrzucane,
  ponieważ korzystają z płatnych kredytów. `--reasoning_effort` ustawia poziom wysiłku,
  z którego tłumaczenie nie czerpie korzyści: zmierzone rozumowanie jest zerowe lub niemal zerowe.
- **Opus odmawia przetwarzania niektórych treści biologicznych.** Jego zabezpieczenia są
  bardziej rygorystyczne niż w Sonnet, a komunikat błędu Anthropic ostrzega, że
  „mogą czasami oznaczać prace związane z badaniami biologicznymi”. Potwierdzone pomiarem: krótka wiadomość z
  przeglądu o 279 wygenerowanych cząsteczkach spowodowała odrzucenie artykułu we wszystkich czternastu
  językach. Nic nie zostaje zapisane: aipmt odrzuca urwaną odpowiedź, wskazuje
  zabezpieczenia i zaleca `--model sonnet`.
- Odrzucane w CI (ustawione `CI` lub `GITHUB_ACTIONS`) i w Windows (bez pomiarów).
- Zmienne: `AIPMT_CLAUDE_BIN` (w przeciwnym razie `PATH`, potem `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekundy na segment, domyślnie 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (domyślnie 0.8), `CLAUDE_CONFIG_DIR` (konto
  Claude Code, nigdy niepobierane z projektowego `.env`); katalogi robocze w
  `XDG_CACHE_HOME/aipmt/claude-code` (domyślnie `~/.cache`).

**Warunki użytkowania: odpowiedzialność wiąże się z Twoim kontem.**
[Strona prawna Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nie zabrania „użytkownikowi końcowemu logowania się do niezmodyfikowanego pliku binarnego Claude Code
przy użyciu własnej subskrypcji Claude”: właśnie to robi aipmt, uruchamiając
oficjalny plik binarny i nigdy nie odczytując tokenu. Anthropic jednak „nie zezwala
zewnętrznym deweloperom […] na kierowanie żądań z użyciem danych uwierzytelniających planów Free, Pro lub Max
w imieniu swoich użytkowników”, preferuje klucz API dla narzędzi
zewnętrznych, „w tym projektów open source”, i zastrzega sobie możliwość odliczania ich
zużycia od płatnych kredytów
([pomoc Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Żaden zapis nie rozstrzyga przypadku rozpowszechnianego narzędzia, które uruchamia plik binarny.

**Dane**: na kontach Free, Pro i Max trenowanie modeli
obejmuje również Claude Code, gdy pozwala na to ustawienie prywatności
([strona dotycząca danych](https://code.claude.com/docs/en/data-usage)). aipmt nie zachowuje
żadnego lokalnego zapisu rozmowy (`--no-session-persistence`). Nie przesyłaj tą drogą
żadnych poufnych danych.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to agent programistyczny open source (MIT), który
kieruje żądania do skonfigurowanych w nim dostawców: przez klucz API, subskrypcję,
bramę OpenCode Zen (darmowe modele, bez konta) lub model lokalny. Dwie
ścieżki zostały tu zmierzone od początku do końca: Zen i Ollama.

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

`--model` jest wymagane: bez niego OpenCode użyłby awaryjnie darmowego modelu,
w którym wymiana wiadomości może służyć do trenowania, a ten wybór nie jest dokonywany
za Ciebie.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, mająca pierwszeństwo przed Twoją, definiuje agenta `aipmt`,
  któremu zabroniono używania wszystkich narzędzi (`permission: { "*": "deny" }`), z wyłączonym udostępnianiem
  sesji, `--pure`, nigdy `--auto`;
- pusty, tymczasowy katalog roboczy, ustawione `OPENCODE_DISABLE_PROJECT_CONFIG` i
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstawia do
  promptu `AGENTS.md` z bieżącego katalogu oraz `~/.claude/CLAUDE.md`. Globalny
  `~/.config/opencode/AGENTS.md` nadal jest wstawiany, OpenCode nie pozwala
  go pominąć;
- kontrakt wyjścia: kod zakończenia 0, brak zdarzeń `error`, brak wywołań
  narzędzi, ostatni krok w `stop`, niepusty tekst i faktycznie załadowany agent `aipmt`
  — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  cichy powrót do agenta programistycznego;
- żaden klucz z `aipmt` nie jest przekazywany poza `OPENCODE_API_KEY`, kluczem
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  `.env` narzędzia `aipmt`.

Warto wiedzieć:

- Darmowe modele Zen zmieniają się, mają nieudokumentowane limity, a
  wymiana wiadomości z nimi może służyć do trenowania: nadają się do dokumentacji
  publicznej, nie do prywatnych treści.
- Model lokalny musi oferować co najmniej 16 k tokenów kontekstu, ponieważ segmenty
  mają do 16 000 znaków. Ollama często ustawia 4 096: należy użyć
  `Modelfile` z `PARAMETER num_ctx 32768`.
- `--eco` nie ma wpływu; `--reasoning_effort` jest przekazywane bez zmian jako
  `--variant` w OpenCode.
- OpenCode zapisuje dziennik każdej sesji w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, potem `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` wyłącza rozumowanie, które Ollama domyślnie włącza w tych
modelach i którego nie da się wyłączyć przez Modelfile. Pomiar na zdaniu
złożonym z sześciu słów: 919 tokenów rozumowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według zużycia, korzystający z jednego salda kredytów i zapewniający dostęp do
modeli hostowanych przez podmioty trzecie — w tym otwartych modeli chińskich, których żaden
inny dostawca tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest wymagane. Kontrola wstępna, wykonywana przed naliczeniem jakichkolwiek opłat, uwzględnia
dwie szczególne cechy routingu:

- **Ten sam model jest obsługiwany przez dziesiątki dostawców hostingu o różnych
  limitach** — w przypadku `z-ai/glm-5.3-flash` jest ich 23, w tym jeden z limitem
  2 048 tokenów wyjściowych. Kontrola wstępna odczytuje `/api/v1/models/{modèle}/endpoints`,
  wyklucza dostawców hostingu z limitem poniżej 8 000 tokenów wyjściowych lub o obniżonej sprawności i
  przypina pozostałych przez `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki za wyjście** — 107 tokenów wobec 2 przy
  odpowiedzi „OK” modelu `z-ai/glm-5.2`. Jest domyślnie wyłączone; modele,
  które go wymagają, otrzymują najniższy akceptowany poziom wysiłku, ponieważ domyślne ustawienie
  z katalogu może wyczerpać limit wyjścia przed ukończeniem tłumaczenia.
  `--reasoning_effort` zachowuje pierwszeństwo.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model z limitem poniżej 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8 400 na prompt i segment, co najmniej 8 000
  na wyjście.
- Slug nieobecny w katalogu, niedostępny katalog lub brak
  dostawcy hostingu spełniającego wymagany limit zatrzymują polecenie.
- `finish_reason=length` z pustym wyjściem oznacza budżet zużyty na
  rozumowanie, a nie ucięcie odpowiedzi: komunikat rozróżnia te przypadki.
- `--eco` nie ma wpływu.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane
  `https://`), `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Adnotacja o tłumaczeniu

`--add_translation_note` dodaje adnotację w `bottom` (domyślnie), `top` (po
front matter) lub `both` (`--note_position`), w formacie `legacy` (akapit
pogrubiony, domyślnie) lub `marker` (`--note_format`). Format `marker` to
niewidoczna definicja odwołania Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje pogrubiony cytat: czytelny na GitHub i możliwy do wykorzystania podczas buildu przez
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary dotyczą tłumaczeń faktycznie wykonanych przy użyciu `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** oznacza liczbę plików przepuszczonych przez mechanizmy kontrolne; **Bez
różnic** — te, w których `scripts/compare_structure.py` niczego nie wykrywa: taka sama liczba
sekcji, podtytułów, linków, odrębnych URL, bloków kodu,
fragmentów kodu inline, wierszy tabel, bloków cytatów i pogrubionych słów.

„Bez różnic” oznacza „niczego nie wykryto”, a nie „identyczne”: porównywarka
zlicza elementy, nie odczytując ich treści. Nie zgłasza ani usuniętego nagłówka
poziomu 4, ani zastąpienia tekstu kodu inline, ani zamienionej
flagi, ani linku wewnętrznego z dodatkowym nawiasem,
`[texte]((#ancre))`, który już donikąd nie prowadzi — i nie ocenia
języka.

### Obszerny artykuł przeglądowy, tryb `--news`

Jedno z wydań [przeglądu AI na jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty angielskie. Seria pomiarów
z 4 i 5 września 2026.

| Model                                          | Dostęp              | Zapisane | Bez różnic   | Mediana/język |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | subskrypcja Google  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | subskrypcja Google  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | subskrypcja ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | subskrypcja Claude  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | subskrypcja Claude  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokalnie              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | subskrypcja Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | subskrypcja Claude  | 0/14    | ❌ 0/14      | —              |

Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): zapisano 9 języków z 14, 8 bez różnic. To właśnie ten wynik
widnieje w tabeli na początku. Nie uwzględniono trzech przerwanych serii:
`qwen3.5-27b` (9 języków) i `kimi-k2.6` (4) z powodu braku kredytów,
`z-ai/glm-5.3-flash`, którego dwa niepowodzenia wynikały z ustawienia rozumowania,
korygowanego obecnie przez dostawcę. Wiersze OpenRouter zmierzono przy
domyślnych ustawieniach routera, przed `--use_openrouter`; `z-ai/glm-5.2`,
ponownie zmierzony z dostarczonym modułem dostawcy, daje ten sam wynik 14/14. Wyniki
przeliczono 10 września aktualną porównywarką: `qwen3.8-flash` i
`qwen3.7-flash` zyskują po jednym języku względem pierwszej
publikacji, pozostałe pozostają bez zmian.

Wiersze `--use_antigravity` zmierzono 26 września na tym samym
artykule, z czterema tłumaczeniami równolegle: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W języku angielskim każdy sam usunął
trzy wiersze francuskiego tłumaczenia pod cytatami, nie wymyślając
flagi, a cytaty angielskie pozostały nienaruszone: awaryjny mechanizm czyszczenia nie
miał nic do zrobienia. W `--eco` (`gemini-3.7-flash-low`), tylko dla czterech języków
(en, ja, ar, hi): zapisano 4 z 4, wszystkie bez różnic, mediana
1 min 52 s. Próba kontrolna tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 cytaty angielskie), przetłumaczonym poza
blogiem przez `gemini-3.7-flash-medium`: zapisano 14 z 14, wszystkie bez różnic, od 87 do
128 s na język.

Wiersze `--use_claude_code` zmierzono 26 września na tym samym
artykule, z czterema tłumaczeniami równolegle, przy poziomie wysiłku `low`. Z `sonnet`
cytaty angielskie pozostały nienaruszone we wszystkich czternastu językach, a w języku angielskim
model sam usunął wiersze francuskiego tłumaczenia, nie wymyślając
flagi. `opus` nie zapisał żadnego języka: w każdym jego zabezpieczenia
zatrzymały odpowiedź przy ostatnim segmencie z powodu krótkiej wiadomości o 279 cząsteczkach
wygenerowanych dla miejsca wiązania. Wysłana osobno wiadomość jest odrzucana
w kategorii „bio”; `sonnet` przetłumaczył ją we wszystkich językach. `haiku` zapisuje
wszystkie czternaście języków; w trzech (en, pl, ro) nagłówek sekcji zmienia
poziom z 2 na 1. Model rozumuje i nie da się tego wyłączyć — przeznacza na to 61 %
tokenów wyjściowych — stąd czas ponad dwukrotnie dłuższy niż w przypadku `sonnet`.

Wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5`
zmierzono 18 października przez API Anthropic, na tym samym artykule, z czterema
tłumaczeniami równolegle na model. Sonnet 5.5 odmawia wyłączenia
rozumowania: aipmt wysyła mu najniższe akceptowane ustawienie, a jego
odpowiedzi nie zawierają żadnego rozumowania. Zapisuje wszystkie czternaście języków bez różnic i bez
ponawiania żadnego segmentu; w języku angielskim sam usunął wiersze
francuskiego tłumaczenia, nie wymyślając flagi, a cytaty angielskie pozostały
wszędzie nienaruszone. Haiku 5.5 zmierzono z adaptacyjnym rozumowaniem: przy wyłączonym
rozumowaniu pozostawiał całe akapity po francusku, co mechanizm kontrolny odrzuca —
zapisano 3 języki z 14. Oba modele Haiku potykają się na tej samej krótkiej wiadomości: Haiku 5.5
zmienia poziom jej nagłówka lub go powiela w języku japońskim, koreańskim i
chińskim, Haiku 4.5 zmienia go na poziom 1 w siedmiu językach, a w tłumaczeniu
japońskim pozostawia go po francusku. Haiku 4.5 kosztuje 3,67 $ za oba dokumenty we
wszystkich czternastu językach, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026: 785 wierszy, 285 fragmentów kodu w tekście, 40
znaczników zamykających bloki, 89 wierszy tabel. Cztery tłumaczenia równolegle.

| Model                                          | Zapisane | Bez różnic | Mediana/język | Co się różni                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nic                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nic                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nic według narzędzia porównującego; podwojone linki wewnętrzne (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nic                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nic                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | jedno słowo pogrubione (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | jedno słowo pogrubione (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | jeden wiersz tabeli doklejony do poprzedniego (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | jeden link (sv), jedno słowo pogrubione (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | jedno słowo pogrubione (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | jedno słowo pogrubione (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 dodanych fragmentów kodu w tekście w języku arabskim; pogrubienie (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 języki odrzucone (ar, hi): utracone fragmenty kodu w tekście w zwróconym wyniku        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | utracona sekcja (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh) |

Dwie przerwane serie pomiarów nie zostały ocenione: Grok, którego sesja CLI wygasła
po dwunastu językach (jedenaście bez różnic), oraz `qwen3.8-flash`, z błędem HTTP 429 od
dostawcy hostingu po dwóch. `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie zostały ponownie zmierzone na tej wersji; na wersji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisywał 9 tłumaczeń z 14, z czego odpowiednio 7
i 1 bez różnic.

Wiersze `--use_antigravity` i `--use_claude_code` nie były mierzone na
zamrożonej wersji, lecz 26 września na wersji opublikowanej wraz z 1.14.0 — a
wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5` 18
października, na tej samej: 600 wierszy, 257 fragmentów kodu w tekście, 30 znaczników zamykających bloki, 85
wierszy tabel. Jest ona
krótsza o 185 wierszy, więc nie można jej bezpośrednio porównywać z pozostałymi wierszami;
te wiersze można jednak porównywać między sobą. Jeśli chodzi o linki wewnętrzne, których
narzędzie porównujące nie sprawdza, `gemini-3.8-flash-medium` zachował je bez zmian we
wszystkich czternastu językach, `gemini-3.7-flash-medium` zepsuł je w języku włoskim;
`sonnet` i `opus` zachowały je wszędzie bez zmian, `haiku` podwoił je w
języku angielskim; `claude-sonnet-5-5` i `claude-haiku-4-5` zachowały je bez zmian we
wszystkich czternastu językach, `claude-haiku-5-5` w dwunastu, dla których zapisał tłumaczenia.

### Cztery README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane bez zmian z GitHub — dokumenty
łatwiejsze niż dwa poprzednie. Seria pomiarów obejmowała modele,
które miały trudności; Gemini służy tu jako punkt odniesienia.

| Model                    | Zakres                  | Zapisane | Bez różnic   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projekty × 14 języków     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków     | 55/56   | ❌ 47/56     |
| `grok-4.6` (abonament)   | 4 projekty × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Czym te pomiary nie są

- **Nie są wyczerpującym rankingiem**: sam OpenRouter oferuje ponad czterysta
  modeli, a zmierzono około piętnastu.
- **Czasy są orientacyjne**: od trzech do sześciu tłumaczeń równolegle zależnie od
  serii pomiarów, a przepustowość dostawcy zmienia się w ciągu dnia.
- **To obserwacje z określonego momentu**: modele zmieniają się pod tą samą nazwą, a Wasze
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

Oba wiersze są niezbędne: bez `pip install -e .`, `python -m aipmt`
odpowiada `No module named aipmt`.

Narzędzia kontroli jakości, opcjonalne, ale zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń w repozytorium (README i CHANGELOG, czternaście języków)
można wygenerować ponownie za pomocą `./regen_translations.sh --force` — domyślnie Codex i `gpt-6.1-sol` w ramach
abonamentu ChatGPT, po cztery równolegle. `REGEN_PROVIDER` i
`REGEN_MODEL` zmieniają sposób działania: `antigravity` nadal korzysta z abonamentu,
tym razem Google, i działa bez specjalnego zezwolenia; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1 800 s dla Codex i
Antigravity). Szczegóły narzędzi znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — blog osobisty publikowany w 15 językach. Jego
  [codzienny przegląd wiadomości o AI](https://jls42.org/fr/news) jest codziennie tłumaczony
  przez to narzędzie i służy jako dokument referencyjny dla powyższych pomiarów.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Wersja 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Ostrzeżenie

Ten program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, zgodnie z
postanowieniami sekcji 15 i 16 GPL v3: dostarczany „w stanie, w jakim jest”, bez gwarancji przydatności
handlowej ani przydatności do określonego celu, a jego autor nie może
ponosić odpowiedzialności za szkody wynikające z jego użytkowania. Tekst
licencji ma pierwszeństwo przed tym podsumowaniem.

- **Przeczytaj ponownie przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod w tekście, adresy URL, kotwice i cytaty w trybie `--news` — nie obejmują
  nagłówków, tabel, front matter ani sensu zdań.
- **Twoje dokumenty trafiają do wybranego dostawcy**, zgodnie z jego warunkami
  korzystania i polityką dotyczącą danych. Niektóre bezpłatne modele mogą
  wykorzystywać Twoje rozmowy do trenowania, a warunki Antigravity
  pozwalają Google na ich ponowne wykorzystanie i przekazywanie do wglądu ludziom,
  również w przypadku płatnego abonamentu; model lokalny jest jedyną opcją, przy której
  żadne dane nie opuszczają Twojego komputera.
- **Opłaty za wywołania API ponosisz Ty.** Ten program nie ogranicza
  wydatków: długi dokument, ponowienie po niepowodzeniu lub model, który intensywnie rozumuje,
  kosztują więcej.
- **Opublikowane pomiary są obserwacjami z określonego momentu**, a nie gwarancjami.

Wymienione nazwy produktów i firm należą do ich
odpowiednich właścicieli. Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z francuskiego na polski za pomocą gpt-6.1-sol.**
