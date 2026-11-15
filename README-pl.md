# Tłumacz Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumaczy pliki Markdown z jednego języka na inny z zachowaniem
struktury: bloków kodu, kodu w tekście, adresów URL, kotwic, tabel i front
matter. Jedenaście sposobów wywołania modelu — pięć API, cztery subskrypcje bez
rozliczania za użycie, dwa routery — oraz opublikowane pomiary tego, co każdy
model rzeczywiście zachowuje.

## W skrócie

- **Jedenaście ścieżek dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex), Grok, Google (Antigravity) i Claude (Claude
  Code) bez rozliczania za użycie; routery OpenCode (open source, bezpłatny lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Zero błędów spowodowanych utraconym tokenem**: bloki kodu, kod w tekście,
  adresy URL, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  weryfikowane po powrocie. Jeśli któregoś brakuje, plik nie zostaje zapisany.
- **Długie dokumenty**: podział na segmenty dostosowany do okna kontekstowego modelu.
- **Tryb `--news`**: chronione angielskie cytaty i flagi zarządzane według
  języka, z myślą o artykułach prasówkowych.
- **Tryb `--eco`**: szybkie i tańsze modele.
- **Opcjonalna notka o tłumaczeniu**, na górze, na dole lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 lub nowszy. Aby zainstalować z repozytorium, zobacz
[Współtworzenie](#współtworzenie).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego do najniższego priorytetu;
każde kolejne uzupełnia tylko to, co poprzednie pozostawiło puste.

|     | Gdzie                                         | Do czego                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                          | CI, kontenery, jednorazowe nadpisanie |
| 2   | `.env` bieżącego katalogu (lub nadrzędnego) | klucz specyficzny dla projektu        |
| 3   | `~/.config/aipmt/.env`                        | instalacja jednorazowa, działa wszędzie |

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
użytkownika jest zgodny z `XDG_CONFIG_HOME` (tylko ścieżka bezwzględna) oraz `%APPDATA%`
w systemie Windows. W przypadku braku klucza polecenie wymienia wszystkie trzy lokalizacje.

**Plik `.env` projektu nie może przekierowywać wywołań ani wybierać wykonywanego
programu.** Dostarcza klucze, nigdy punkt docelowy ani plik binarny: każda
zmienna zaczynająca się od `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, serwery proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane z ostrzeżeniem. Sklonowane repozytorium nie może
mieć możliwości przejęcia Twojego klucza ani uruchomienia własnego programu przy
pierwszym tłumaczeniu. Plik ten jest również odczytywany bez interpolacji:
`NOM=${OPENAI_API_KEY}` nie kopiuje w nim klucza. Zmienne te należy zdefiniować
w środowisku lub w pliku `~/.config/aipmt/.env`.

Zmienne opcjonalne: `XAI_BASE_URL` (domyślnie `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekundy na wywołanie, domyślnie 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(domyślnie 600), `GROK_BIN`, `GROK_HOME` (domyślnie `~/.grok`), `GROK_TIMEOUT`
(domyślnie 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (domyślnie 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (domyślnie 600), `OPENROUTER_BASE_URL`
(wymagane `https://`), `OPENROUTER_TIMEOUT` (domyślnie 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (domyślnie 30). Każda z nich została szczegółowo opisana w
sekcji poświęconej danemu dostawcy.

## Pierwsze kroki

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

Plik `document.md` przetłumaczony na język hiszpański daje `document-es.md` w katalogu `--target_dir`;
z flagą `--include_model`, `document-es-gpt-6.1-terra.md`. Rozszerzenie zawsze
zmienia się na `.md` — `article.mdx` daje `article-en.md` — z wyjątkiem
użycia `--keep_filename`, co pozwala zachować pierwotną nazwę. Istniejące już tłumaczenie
jest pomijane bez flagi `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli chociaż jeden plik
zakończył się niepowodzeniem (lista na standardowym wyjściu błędów), `2`, jeśli przyczyną jest konfiguracja.
Plik zakończony błędem nigdy nie zostaje zapisany, nawet jeśli sam zapis się nie powiedzie:
zawartość jest zapisywana obok, a następnie zmieniana jest jej nazwa. Wystarczy uruchomić ponownie.

## Jaki model wybrać

Zmierzone na dwóch rzeczywistych dokumentach, przetłumaczonych na te same czternaście języków przez
każdy model. **Liczba oznacza liczbę języków (na czternaście), w których
tłumaczenie zostało zapisane i niczym nie różni się od źródła.**

| Model                 | Jak uzyskać dostęp                | Gęsty artykuł prasówkowy | Ten README   | Co się różni i w ilu językach                                                                                                                                      |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | subskrypcja Google (Antigravity)  | ✅ 14/14                | ✅ 14/14     | nic, w żadnym z dwóch dokumentów                                                                                                                                   |
| **Claude Sonnet 5.5** | klucz API Anthropic               | ✅ 14/14                | ✅ 14/14     | nic, w żadnym z dwóch dokumentów                                                                                                                                   |
| **Gemini 3.7 Flash**  | klucz API Google                  | ✅ 14/14                | ⚠️ 13/14     | 1 język na 14: o jedno pogrubione słowo więcej (ja)                                                                                                                |
| **Gemini 3.7 Flash**  | subskrypcja Google (Antigravity)  | ✅ 14/14                | ⚠️ 13/14     | 1 język na 14: o jedno pogrubione słowo mniej (ko)                                                                                                                 |
| **GPT-5.6 Sol**       | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14             | ⚠️ 12/14     | 2 języki na 14: o jedno pogrubione słowo mniej (ar, ja)                                                                                                            |
| **GLM-5.2**           | klucz OpenRouter                  | ✅ 14/14                | ⚠️ 11/14     | 3 języki na 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                                                       |
| Claude Sonnet 5       | subskrypcja Claude (Claude Code)  | ⚠️ 13/14                | ⚠️ 13/14     | 1 język na 14 w artykule: o jedno pogrubione słowo więcej (zh); 1 w tym README: wiersz tabeli doklejony do poprzedniego, niewidoczny przy renderowaniu (ar)        |
| Claude Haiku 4.5      | subskrypcja Claude (Claude Code)  | ⚠️ 11/14                | ✅ 14/14     | 3 języki w artykule: nagłówek sekcji podniesiony do poziomu 1 (en, pl, ro); w tym README brak różnic w porównaniu, ale linki wewnętrzne zdublowane po angielsku |
| Claude Sonnet 5       | klucz API Anthropic               | ⚠️ 11/14                | ⚠️ 12/14     | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym README: link bez formatowania (sv), pogrubione słowo (zh)                                        |
| Claude Haiku 4.5      | klucz API Anthropic               | ⚠️ 7/14                 | ✅ 14/14     | 7 języków w artykule: nagłówek sekcji podniesiony do poziomu 1 — w japońskim pozostał po francusku; nic w tym README                                              |
| Claude Haiku 5.5      | klucz API Anthropic               | ⚠️ 11/14                | ❌ 12/14     | 3 języki w artykule: zmieniony poziom nagłówka sekcji lub jego zdublowanie (ja, ko, zh); w tym README 2 języki odrzucone, utracony kod w tekście (ar, hi)        |
| Qwen 3.7 Flash        | klucz OpenRouter                  | ❌ 8/14                 | ⚠️ 10/14     | 1 język odrzucony w artykule, 5 innych odbiega; w tym README około czterdziestu słów sformatowanych jako `code` (ar)                                      |
| Grok 4.6              | subskrypcja Grok                  | ❌ 8/14                 | nieoceniany  | 5 języków odrzuconych na 14 z powodu braku zwróconego kodu w tekście i adresów URL; niderlandzki odbiega w całości                                               |
| GPT-OSS 20B           | model lokalny (Ollama)            | ❌ 7/14                 | nie mierzono ponownie | 4 języki odrzucone na 14: model pozostawił fragmenty po francusku, mechanizm zabezpieczający je zatrzymał                                                |
| MiMo v2.5 (bezpłatny) | OpenCode Zen, bez konta           | ❌ 11/14                | nie mierzono ponownie | 1 język odrzucony; utracona sekcja w języku polskim                                                                                                                |
| Mistral Large         | klucz API Mistral                 | ❌ 5/14                 | ❌ 1/14      | **znika cała sekcja**: 1 język w artykule (hi), 3 w tym README (ar, hi, ko) — oraz 3 języki odrzucone w artykule                                                |
| DeepSeek V4 Flash     | klucz OpenRouter                  | ❌ 3/14                 | nie mierzono ponownie | 10 języków odrzuconych na 14; 37 minut na język                                                                                                                   |
| Claude Opus 5.5       | subskrypcja Claude (Claude Code)  | ❌ 0/14                 | ✅ 14/14     | artykuł odrzucony we wszystkich 14 językach przez filtry bezpieczeństwa Opusa z powodu notki biologicznej; nic w tym README                                        |

|     | Co oznacza symbol                                                                                                                                                                                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | przetłumaczono wszystkie czternaście języków i niczym nie różnią się od źródła                                                                                                                       |
| ⚠️  | przetłumaczono wszystkie czternaście języków; to, co się różni, to **formatowanie** — pogrubione słowo, `code`, link tracący nawiasy. Żaden tekst, adres URL, blok kodu ani sekcja nie zniknęły |
| ❌  | co najmniej jednego języka nie udało się przetłumaczyć — plik został odrzucony, niezapisany — **lub** w zapisanym pliku brakuje treści                                                               |

Najważniejsze wnioski:

- **Odrzucone tłumaczenie to nie to samo co zepsute tłumaczenie.** Gdy po powrocie
  brakuje tokena, plik nie zostaje zapisany, a dany język liczy się jako
  odrzucony. To właśnie przydarzyło się modelowi Grok w artykule: cztery fragmenty kodu w tekście
  i trzy adresy URL utracone już w pierwszym segmencie w pięciu pismach nielacińskich.
- **Model może odrzucić cały dokument przez jedno zdanie.** Opus 5.5
  tłumaczy ten README bezbłędnie, ale żaden artykuł prasówkowy nie przechodzi: jego
  filtry bezpieczeństwa przerywają odpowiedź przy notce biologicznej. Plik nie zostaje
  zapisany, a aipmt informuje o przyczynie.
- **Ta ochrona nie obejmuje nagłówków, tabel, front matter ani zwykłego
  tekstu.** Model, który usunie sekcję, zwraca plik, który narzędzie zapisuje
  bez mrugnięcia okiem — tak dzieje się w przypadku Mistrala. Elementów tych nie da się
  zastąpić tokenem, a obecne zabezpieczenia ich nie weryfikują;
  narzędzie `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego README**: jego sesja CLI wygasła po dwunastu
  językach, z czego jedenaście bez odchyleń. Przerwanych testów się nie ocenia.
- **Gęstość dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze
  zwykłymi plikami README, a gubi się przy artykule gęstym od linków, również
  w języku niderlandzkim.

Daty i dokumenty: kolumna „Ten README” została zmierzona 9 września 2026 r.
na zamrożonej wersji tego pliku (785 linii, 285 fragmentów kodu w tekście, 89 wierszy
tabeli), od tego czasu modyfikowanej — z wyjątkiem wierszy Antigravity i Claude Code,
zmierzonych 26 września na wersji opublikowanej z wydaniem 1.14.0, która jest krótsza
(600 linii, 257 fragmentów kodu w tekście, 85 wierszy tabeli), oraz wierszy Claude
Sonnet 5.5, Haiku 5.5 i Haiku 4.5 przez API, zmierzonych 18 października na tej
samej wersji. Kolumna „Gęsty artykuł prasówkowy” pochodzi z testów z
4 i 5 września na artykule liczącym 589 linii, z wyjątkiem wiersza Grok, zmierzonego ponownie
9 września na innym wydaniu tego samego przeglądu, wierszy Antigravity i
Claude Code, zmierzonych 26 września na tym samym artykule, oraz tych trzech wierszy
Claude z 18 października. Pełne tabele, czasy trwania i protokół znajdują się
w sekcji [Szczegółowe pomiary](#szczegółowe-pomiary).

## Wszystkie opcje

| Opcja                    | Opis                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia (alternatywa dla `--source_dir`)                                  |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown (domyślnie: `content/posts`)                                       |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików (domyślnie: `traductions_en`)                                     |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                                                    |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                                                   |
| `--model`                | Konkretny model do użycia                                                                                     |
| `--eco`                  | Używaj modeli ekonomicznych                                                                                   |
| `--use_mistral`          | Użyj API Mistral AI                                                                                           |
| `--use_claude`           | Użyj API Claude                                                                                               |
| `--use_gemini`           | Użyj API Gemini                                                                                               |
| `--use_grok`             | Użyj API xAI (Grok) — wymaga `XAI_API_KEY`                                                                   |
| `--use_codex`            | Użyj CLI Codex w ramach limitu subskrypcji ChatGPT                                                            |
| `--use_grok_cli`         | Użyj CLI Grok w ramach limitu subskrypcji Grok                                                                |
| `--use_antigravity`      | Użyj CLI Antigravity (`agy`) w ramach limitu subskrypcji Google AI Pro lub Ultra                     |
| `--use_claude_code`      | Użyj CLI Claude Code (`claude -p`) w ramach limitu subskrypcji Claude Pro lub Max                          |
| `--use_opencode`         | Użyj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle`                      |
| `--use_openrouter`       | Użyj OpenRouter — wymaga `OPENROUTER_API_KEY` oraz `--model fournisseur/modèle`                                                   |
| `--force`                | Wymuś ponowne tłumaczenie                                                                                     |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                                                                |
| `--news`                 | Tryb aktualności: chroni cytaty w EN, obsługuje flagi według języka                                           |
| `--add_translation_note` | Dodaj notatkę o tłumaczeniu                                                                                   |
| `--note_position`        | Pozycja notatki: `top`, `bottom` (domyślnie) lub `both`                                |
| `--note_format`          | Format notatki: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                            |
| `--include_model`        | Dołącz nazwę modelu w pliku wyjściowym                                                                        |
| `--reasoning_effort`     | Poziom wnioskowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

Dziewięć flag `--use_*` wyklucza się wzajemnie: połączenie dwóch z nich jest
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

`--eco` przełącza na poziom ekonomiczny każdego dostawcy.

| Dostawca    | Jakość (domyślnie)                                                   | Ekonomiczny (`--eco`)        |
| ----------- | -------------------------------------------------------------------- | ------------------------------------ |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`                      |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`                |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`            |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`           |
| Codex       | `gpt-6.1-sol` (również `gpt-5.6-sol`, `terra` i `luna` przez `--model`) | `gpt-6-luna`                      |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                        |
| Grok CLI    | `grok-4.7`                                                           | to samo — `--eco` bez wpływu |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`            |
| Claude Code | `sonnet`, wysiłek `low`                                               | to samo — `--eco` bez wpływu |
| OpenCode    | `--model provider/modèle` wymagane                                | to samo — `--eco` bez wpływu |
| OpenRouter  | `--model fournisseur/modèle` wymagane                             | to samo — `--eco` bez wpływu |

Wartości domyślne podążają za najnowszą generacją każdego dostawcy, zmierzoną
przed wdrożeniem: GPT-6 w OpenAI, Gemini 4 Hydrogen w Google,
Grok 4.7 w xAI od wersji 1.19.0. Poprzednie modele są nadal akceptowane
przez `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), podobnie jak
Gemini 4 Argon i Carbon, najwyższa półka od Google. aipmt sam dostosowuje
wysiłek wnioskowania dla modeli GPT i Grok, wyłączony w `--eco`, a
`--reasoning_effort` go wymusza; Gemini zawsze otrzymuje najniższy
poziom, jaki akceptuje.
Chwilowa awaria API Gemini (503, 429, przekroczenie limitu czasu) powoduje ponowienie
wywołania do trzech razy, po 10, 20, a następnie 40 sekundach. Próba,
która pozostała bez odpowiedzi, jest przerywana po 5 minutach, a następnie wznawiana
w ten sam sposób: milczący serwer powoduje niepowodzenie segmentu po maksymalnie
około dwudziestu minutach, zamiast blokować działanie w nieskończoność.

### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest odliczane z limitu
subskrypcji ChatGPT, bez klucza API i opłat za zużycie.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Plik binarny jest wyszukiwany w `CODEX_BIN`, następnie w `PATH`, a potem w pakiecie
  `openai-codex-cli-bin`. `~/.codex/auth.json` nigdy nie jest odczytywany.
- `OPENAI_API_KEY` i `CODEX_API_KEY` są usuwane ze środowiska
  podprocesu: obecny klucz nigdy nie powoduje przełączenia na API.
- Każdy segment kosztuje co najmniej jedną „wiadomość” z 5-godzinnego okna — dwie,
  jeśli jego walidacja się nie powiedzie i nastąpi ponowna próba. OpenAI podaje szacunkowo
  250–2000 wiadomości/5 godz. dla `gpt-5.6-luna`, wersji ekonomicznej do
  1.18.0, oraz 10–100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-sol`, domyślny do wersji 1.16.3, `--model gpt-5.6-terra`
  oraz `--model gpt-5.6-luna` również działają w ramach subskrypcji.
- Błąd 429 z serwera nie powoduje utraty pliku: Codex łączy się ponownie sam,
  aipmt czeka na zakończenie rundy, a jeśli 429 utrzyma się do końca, segment
  jest wznawiany po 30, a następnie po 60 sekundach. Model, do którego konto nie ma uprawnień,
  zwraca błąd 400 „model is not supported when using Codex with a ChatGPT account”.
- Działa wolniej niż API, a różnica rośnie wraz z wielkością dokumentu: w przypadku tego README
  mediana wynosi 6 min 46 s na język przy użyciu `gpt-5.6-sol`, w porównaniu do 36 s dla
  `gemini-3.7-flash`.
- Odrzucane w środowisku CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): subskrypcja
  uwierzytelnia się za pomocą osobistego pliku sesji, który nie powinien
  znajdować się na współdzielonym runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada z oficjalnym CLI Grok Build, w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Piaskownica systemu operacyjnego Grok nie działa
  na wielu współczesnych stanowiskach Linux (AppArmor, gniazda środowiska uruchomieniowego
  kontenerów), a profil, którego nie da się zastosować, uruchamia się bez izolacji
  w milczeniu. Skrypt domyślnie nie żąda więc żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` CLI, w tym regule ogólnej `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast po cichu usuwać ochronę.
  `GROK_TRANSLATE_SANDBOX=read-only` wymaga piaskownicy OS, a uruchomienie
  kończy się niepowodzeniem, jeśli maszyna nie może jej zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, i żadne
  polecenie nie pozwala go odczytać: zadanie wsadowe może bez ostrzeżenia
  uszczuplić pulę na korzystanie z czatu.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach subskrypcji Google: `--use_antigravity`

Ta sama zasada z `agy`, oficjalnym CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie jest odliczane z limitu subskrypcji zamiast
rozliczania za tokeny. To jedyna droga do tego limitu: Gemini CLI nie
obsługuje już tych kont od 18 czerwca 2026 r.
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
  terminal, tożsamość, serwery proxy i certyfikaty, magistralę sesji — i żadnego klucza:
  kilka z jego zmiennych potrafi przekierować wywołanie bez wyświetlania czegokolwiek (zmierzone:
  jedna wysyła dokument do bramy zewnętrznej, inna do płatnego projektu
  Google Cloud), a lista blokowanych zmiennych okazywała się niekompletna przy każdej weryfikacji.
  Przed każdym segmentem polecenie `agy -p /config`, które nie zużywa limitu, musi wykazać
  wyłączone płatne kredyty AI, brak klucza API oraz brak projektu Google Cloud — brak
  ustawienia jest traktowany jako odmowa —, w przeciwnym razie nic nie zostanie przetłumaczone;
  dziennik każdego wywołania musi następnie potwierdzić subskrypcję (`authMethod=consumer`),
  inaczej odpowiedź zostanie odrzucona.
- **Izolacja.** Każde wywołanie działa w prywatnym, jednorazowym
  katalogu domowym, z agentem tłumaczącym pozbawionym narzędzi: Twoje ustawienia, reguły,
  wtyczki, serwery MCP i hooki agy nie mają do niego dostępu, nic nie jest dodawane do Twojej
  historii, a sesja pozostaje w pęku kluczy, którego aipmt nigdy nie odczytuje.
  Brak agenta sprawia, że agy po cichu powraca do swojego agenta programistycznego
  i jego narzędzi: cała linia w dzienniku musi potwierdzić właściwego agenta — cytowanie
  tego komunikatu przez dokument jej nie zastępuje —, w przeciwnym razie następuje odmowa.
- **Platformy**: Linux w sesji posiadającej pęk kluczy (magistrala sesyjna
  D-Bus, Secret Service); macOS jest akceptowany, choć nie był tam mierzony. Odrzucane
  w systemie Windows, gdzie agy nie odczytuje zmiennych izolujących poszczególne wywołania,
  oraz w systemie Linux bez magistrali sesyjnej — sesje SSH, kontenery, serwery: agy
  przechowuje tam swój token w pliku w `~/.gemini`, który jest ukrywany przez izolację.
  Odmowa następuje przed jakimkolwiek uruchomieniem wraz z podaniem przyczyny, zamiast
  minutowego oczekiwania na kod logowania.
- **Modele**: dostępne w `agy models`. Modele Gemini mają poziom wysiłku w nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez sufiksu jest odrzucana przed wywołaniem,
  a flaga `--reasoning_effort` nie przynosi efektu. Domyślnie `gemini-3.8-flash-medium`,
  a `gemini-3.8-flash-low` w trybie `--eco`, odkąd agy nie obsługuje już Gemini 3.7
  Flash; seria testów, która ustaliła wartość domyślną, jest
  opisana w sekcji [Szczegółowe pomiary](#szczegółowe-pomiary). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) współdzieli limit z 3.8 Flash i zużywa go
  więcej: 0,95 punktu z 5-godzinnego okna dla tego README przy średnim
  wysiłku, w porównaniu do 0,32. Claude oraz GPT-OSS
  mają własny, znacznie mniejszy limit: około 1% 5-godzinnego okna
  na zmierzone wywołanie, w porównaniu do 0,05% w przypadku Flash. Gemini 4 Argon posiada
  własny limit tygodniowy: ten plik README zużywa 1,35% z niego.
- **Limit**: według grup — okno 5-godzinne oraz okno tygodniowe, proporcjonalnie
  do kosztu w tokenach. Zmierzone na koncie autora: około
  16 punktów z 5-godzinnego okna na milion znaków źródłowych w
  `gemini-3.8-flash-medium`, 14 w `gemini-3.7-flash-medium` oraz 7 do 8 przy
  niskim wysiłku — README o długości 40 000 znaków kosztuje więc nieco ponad
  pół punktu. Limit tygodniowy zależy z kolei od poziomu subskrypcji. Ponawianie zależy od
  tego, co agy uzna za możliwe do powtórzenia; w przeciwnym razie wyczerpane okno nigdy nie jest
  ponawiane: powoduje błąd każdego pliku aż do zresetowania,
  które wyświetla `/usage`.
- **Wolniejsze niż API**: w przypadku gęstego artykułu z pomiarami mediana wynosi 3 min 59 s na
  język w trybie `gemini-3.8-flash-medium` oraz 3 min 14 s w
  `gemini-3.7-flash-medium`, w porównaniu do 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerwanie**: Ctrl-C lub zamknięcie terminala zatrzymuje agy wraz z
  poleceniem, zamiast pozwalać mu dokończyć rundę na Twoim limicie; to samo
  dotyczy Codex, Grok CLI i OpenCode. Pod `nohup` tłumaczenie jest kontynuowane.
- Odrzucane w środowisku CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): sesja znajduje się
  w osobistym pęku kluczy. Na runnerze należy użyć `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment wraz z uruchomieniem, domyślnie 900).

**Warunki korzystania: korzystasz z własnego konta na własną odpowiedzialność.**
[Warunki korzystania z Antigravity](https://antigravity.google/terms) (sekcja 6) oraz powiązana
[FAQ](https://antigravity.google/docs/faq/) zabraniają uzyskiwania dostępu do usługi
za pośrednictwem oprogramowania firm trzecich przy użyciu sesji logowania Antigravity — wymieniono
tam m.in. Claude Code, OpenClaw i OpenCode — pod rygorem zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokenu: uruchamia oficjalny plik binarny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
opisuje w dokumentacji dla skryptów i środowisk CI. Przedstawiciel Google uznał uruchamianie
`agy -p` z poziomu lokalnego skryptu na własne potrzeby za „standardowe”
([oficjalne forum, 25 września 2026 r., odpowiedź niewiążąca prawnie](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden zapis nie rozstrzyga jednoznacznie kwestii narzędzi udostępnianych publicznie, takich jak to.

**Wyłącznie dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków,
wymieniane dane — prompty, odpowiedzi, metadane — mogą być wykorzystywane do ulepszania
produktów i uczenia maszynowego Google oraz mogą być weryfikowane przez
ludzi, również w przypadku płatnej subskrypcji. Rezygnacja jest możliwa za pomocą ustawienia
`enableTelemetry`, którego działanie nie jest udokumentowane i którego aipmt nie ustawia; Twoje
ustawienia agy nie są przenoszone do izolowanego środowiska. Nie przetwarzaj tą drogą żadnych poufnych danych.

### W ramach subskrypcji Claude: `--use_claude_code`

Ta sama zasada dotyczy `claude`, oficjalnego CLI Claude Code, w trybie `-p`: dla
osób opłacających Claude Pro lub Max tłumaczenie jest odliczane z limitu
subskrypcji zamiast rozliczania za tokeny. Nie należy mylić z
`--use_claude`, API Anthropic, rozliczanym według użycia.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Żadna płatna ścieżka nie pozostaje otwarta, a każde wywołanie to udowadnia.** Claude
  Code otrzymuje z Twojego środowiska wyłącznie zamkniętą listę zmiennych — ani
  klucza API, ani tokena, ani dostawcy chmurowego, ani znacznika sesji Claude Code,
  z której aipmt zostałby uruchomiony. Przed pierwszym segmentem `claude auth status` musi
  pokazać połączenie subskrypcyjne bez klucza Console, a `/usage`, które nie zużywa
  żadnego limitu, musi to poświadczyć; każde wywołanie poświadcza to z kolei w swoim
  zdarzeniu inicjalizacji, w przeciwnym razie odpowiedź jest odrzucana.
- **Wyłącz „extra usage”** (claude.ai, Ustawienia → Użycie), aby
  utrzymać koszt zero euro: gdy opcja jest włączona, przejmuje zadania po wyczerpaniu okna i
  nalicza opłaty bez wyświetlania błędu. aipmt przerywa tłumaczenie, gdy tylko odczyt
  limitu z wywołania to zasygnalizuje, ale to konkretne wywołanie jest już naliczone.
- **Limit współdzielony z sesjami Claude Code.** Każde wywołanie raportuje
  wykorzystanie okien 5-godzinnych oraz tygodniowych; powyżej 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) żaden kolejny segment nie jest uruchamiany, aby
  nie wyczerpać zasobów potrzebnych do Twojej pracy.
- **Izolacja.** Każde wywołanie działa bez narzędzi, w prywatnym,
  jednorazowym katalogu, w trybie bez personalizacji: ani Twoje `CLAUDE.md`, ani wtyczki,
  hooki, serwery MCP czy ustawienia nie są ładowane, a z sesji nic nie
  jest zachowywane. Załączniki są odcięte: odwołanie `@chemin` w Twoim dokumencie
  pozostaje tekstem i nie otwiera żadnego pliku (zmierzone).
- **Modele**: domyślnie `sonnet`, przy nakładzie pracy (effort) `low`, a także w `--eco`:
  `--eco` niczego nie zmienia na tej ścieżce. Zmierzone na tych samych dokumentach: `haiku`
  jest dwa razy wolniejszy — rozumuje bez możliwości powstrzymania go — przy
  niewiele niższym koszcie, a `opus` odrzuca treści biologiczne (kolejny
  punkt). Oba pozostają dostępne przez `--model`; aliasy te podążają za
  najnowszym modelem ze swojej rodziny. `fable` oraz warianty `[1m]` są odrzucane,
  ponieważ przechodzą na płatne kredyty. `--reasoning_effort` reguluje nakład pracy (effort),
  z którego tłumaczenie nic nie zyskuje: zmierzone rozumowanie jest zerowe lub niemal zerowe.
- **Opus odrzuca niektóre treści biologiczne.** Jego zabezpieczenia są
  bardziej rygorystyczne niż w przypadku Sonnet, a komunikat o błędzie od Anthropic ostrzega, że
  „can sometimes flag biology-research-adjacent work”. Zmierzone: krótka notka
  prasowa o 279 wygenerowanych cząsteczkach spowodowała odrzucenie artykułu we wszystkich czternastu
  językach. Nic nie zostaje zapisane: aipmt odrzuca uciętą odpowiedź, wskazuje
  zabezpieczenia i zaleca `--model sonnet`.
- Odrzucane w CI (zdefiniowane `CI` lub `GITHUB_ACTIONS`) oraz pod Windows (niezmierzone).
- Zmienne: `AIPMT_CLAUDE_BIN` (w przeciwnym razie `PATH`, następnie `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekundy na segment, domyślnie 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (domyślnie 0.8), `CLAUDE_CONFIG_DIR` (konto
  Claude Code, nigdy niepobierane z pliku `.env` projektu); katalogi robocze w
  `XDG_CACHE_HOME/aipmt/claude-code` (domyślnie `~/.cache`).

**Warunki użytkowania: to Twoje konto ponosi odpowiedzialność.**
[Strona prawna Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nie zabrania „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription”: właśnie to robi aipmt, uruchamiając
oficjalny plik binarny i nigdy nie czytając tokena. Jednak Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users”, preferuje klucz API dla narzędzi
trzecich, „including open-source projects”, i zastrzega sobie prawo do rozliczania ich
użycia z płatnych kredytów
([pomoc Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Żaden tekst nie rozstrzyga jednoznacznie przypadku dystrybuowanego narzędzia uruchamiającego plik binarny.

**Dane**: na kontach Free, Pro i Max trenowanie modeli
obejmuje również Claude Code, jeśli zezwalają na to ustawienia prywatności
([strona dotycząca danych](https://code.claude.com/docs/en/data-usage)). aipmt nie przechowuje
żadnej lokalnej transkrypcji (`--no-session-persistence`). Nie przesyłaj
tą drogą żadnych poufnych informacji.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to otwartoźródłowy agent kodujący (MIT), który
kieruje zapytania do skonfigurowanych w nim dostawców: klucz API, subskrypcja,
bramka OpenCode Zen (darmowe modele, bez konta) lub model lokalny. Dwie
ścieżki zostały tutaj zmierzone kompleksowo (end-to-end): Zen oraz Ollama.

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

`--model` jest obowiązkowy: bez niego OpenCode przełączyłby się na darmowy model,
którego konwersacje mogą być wykorzystywane do trenowania, a taki wybór nie powinien zapadać
bez Twojej wiedzy.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, nadrzędna wobec Twojej, definiuje agenta `aipmt`,
  którego wszystkie narzędzia są odrzucone (`permission: { "*": "deny" }`), udostępnianie
  sesji wyłączone, `--pure`, nigdy `--auto`;
- jednorazowy i pusty katalog roboczy, umieszczone `OPENCODE_DISABLE_PROJECT_CONFIG` oraz
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstrzykuje do
  promptu plik `AGENTS.md` bieżącego katalogu oraz `~/.claude/CLAUDE.md`. Globalny
  `~/.config/opencode/AGENTS.md` nadal jest wstrzykiwany, OpenCode nie pozwala
  go pominąć;
- kontrakt wyjściowy: kod wyjścia 0, brak zdarzenia `error`, brak wywołań
  narzędzi, ostatni krok jako `stop`, niepusty tekst i rzeczywiście załadowany
  agent `aipmt` — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  dyskretnie przełącza się na agenta kodującego;
- żaden klucz z pliku `aipmt` nie jest przekazywany, z wyjątkiem `OPENCODE_API_KEY`, czyli klucza
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  pliku `.env` narzędzia `aipmt`.

Warto wiedzieć:

- Darmowe modele Zen ulegają zmianom, mają nieudokumentowane limity, a
  ich konwersacje mogą służyć do trenowania: nadają się do publicznej
  dokumentacji, nie do treści prywatnych.
- Model lokalny musi zapewniać co najmniej 16 tys. tokenów kontekstu, ponieważ segmenty
  mają do 16 000 znaków. Ollama często konfiguruje 4096: należy użyć
  pliku `Modelfile` z parametrem `PARAMETER num_ctx 32768`.
- `--eco` nie przynosi żadnego efektu; parametr `--reasoning_effort` jest przekazywany w niezmienionej postaci jako
  `--variant` programu OpenCode.
- OpenCode rejestruje każdą sesję w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, następnie `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekundy na segment, domyślnie 600). Zmienna `OPENCODE_CONFIG`
  przechodzi bez zmian do OpenCode.

Przykład modelu lokalnego przez Ollama w pliku `~/.config/opencode/opencode.json`:

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

Flaga `reasoningEffort: "none"` wyłącza proces myślenia (thinking), który Ollama domyślnie aktywuje na tych
modelach, a którego nie da się wyłączyć w pliku Modelfile. Zmierzone na zdaniu liczącym
sześć słów: 919 tokenów myślenia i 68 sekund bez tej opcji, 9 tokenów z nią.

### Do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według użycia, w ramach jednorazowego doładowania, stojący przed
modelami hostowanymi przez podmioty trzecie — w tym otwartymi modelami chińskimi, których żaden
inny dostawca tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

Zmienna `--model` jest wymagana. Weryfikacja wstępna (preflight), wykonywana przed jakimkolwiek naliczeniem opłat, reguluje
dwie specyficzne cechy routingu:

- **Ten sam model jest obsługiwany przez dziesiątki hostów o różnych limitach**
  — w przypadku `z-ai/glm-5.3-flash` to 23 hostów, z czego jeden ograniczony do
  2048 tokenów wyjściowych. Weryfikacja wstępna odczytuje `/api/v1/models/{modèle}/endpoints`,
  odrzuca hosty oferujące poniżej 8000 tokenów wyjściowych lub o obniżonym statusie (degraded), a
  pozostałe przypina za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki wyjściowej** — 107 tokenów w porównaniu do 2 przy
  odpowiedzi „OK” z modelu `z-ai/glm-5.2`. Jest ono domyślnie wyłączone; modele,
  które je wymuszają, otrzymują najniższy akceptowany przez siebie nakład pracy (effort), ponieważ domyślna wartość
  katalogowa mogłaby nasycić wyjście przed zakończeniem tłumaczenia.
  `--reasoning_effort` zachowuje priorytet.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model poniżej 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8400 na prompt i segment, minimum 8000
  na wyjściu.
- Brakujący identyfikator (slug) w katalogu, niedostępny katalog lub brak
  hosta spełniającego limit przerywają polecenie.
- Błąd `finish_reason=length` z pustym wyjściem oznacza budżet skonsumowany przez
  rozumowanie, a nie obcięcie tekstu: komunikat to rozróżnia.
- Zmienna `--eco` nie ma wpływu na działanie.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Notatka o tłumaczeniu

Flaga `--add_translation_note` dodaje notatkę w pozycji `bottom` (domyślnie), `top` (za
front matterem) lub `both` (`--note_position`), w formacie `legacy` (akapit
wytłuszczony, domyślnie) lub `marker` (`--note_format`). Format `marker` to
niewidoczna definicja referencyjna Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje wytłuszczony cytat blokowy: czytelny na GitHubie, możliwy do przetworzenia podczas budowania przez
wtyczkę remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary to tłumaczenia rzeczywiście zrealizowane za pomocą `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
Kolumna **Zapisane** zlicza pliki, które przeszły przez mechanizmy ochronne; **Bez rozbieżności**
to pliki, w których `scripts/compare_structure.py` nie wykazuje żadnych różnic — taka sama liczba
sekcji, podtytułów, linków, unikalnych adresów URL, bloków kodu,
kodu śródliniowego, wierszy tabeli, cytatów blokowych i wytłuszczonych słów.

„Bez rozbieżności” oznacza „nic nie wykryto”, a nie „identyczne”: narzędzie porównujące
zlicza elementy bez analizowania ich treści. Nie zasygnalizuje usuniętego nagłówka
poziomu 4, zastąpionego tekstu w kodzie śródliniowym, zamienionej flagi
ani linku wewnętrznego wygenerowanego ze zbędnym nawiasem,
`[texte]((#ancre))`, który przestaje dokądkolwiek prowadzić — nie ocenia też
jakości językowej.

### Gęsty artykuł przeglądowy, tryb `--news`

Jedno z wydań [przeglądu AI z jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty w języku angielskim. Kampania
z 4 i 5 września 2026 r.

| Model                                          | Dostęp              | Zapisane | Bez rozbieżności | Mediana/język  |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | subskrypcja Google  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | subskrypcja Google  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | subskrypcja ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | subskrypcja Claude  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | subskrypcja Claude  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokalnie           | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | subskrypcja Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | subskrypcja Claude  | 0/14    | ❌ 0/14      | —              |

Model Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): zapisano 9 języków z 14, 8 bez rozbieżności. To właśnie ta wartość
widnieje w tabeli głównej. Trzy przerwane kampanie nie zostały
uwzględnione: `qwen3.5-27b` (9 języków) oraz `kimi-k2.6` (4) z powodu braku środków,
oraz `z-ai/glm-5.3-flash`, którego dwa niepowodzenia wynikały z konfiguracji rozumowania,
którą dostawca od tamtej pory koryguje. Wiersze OpenRouter zmierzono przy
domyślnych ustawieniach routera, przed wprowadzeniem `--use_openrouter`; model `z-ai/glm-5.2`,
zmierzony ponownie z dostarczonym dostawcą, osiąga ten sam wynik 14/14. Wartości zostały
przeliczone 10 września za pomocą obecnego narzędzia porównującego: `qwen3.8-flash` oraz
`qwen3.7-flash` zyskały po jednym języku w stosunku do pierwszej
publikacji, pozostałe nie uległy zmianie.

Wiersze `--use_antigravity` zmierzono 26 września na tym samym
artykule, wykonując cztery tłumaczenia równolegle: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W języku angielskim każdy z nich samodzielnie usunął
trzy linie francuskiego tłumaczenia pod cytatami, nie dodając żadnej flagi,
a angielskie cytaty pozostały nienaruszone: mechanizm czyszczenia awaryjnego nie
musiał podejmować żadnych działań. W trybie `--eco` (`gemini-3.7-flash-low`), tylko dla czterech języków
(en, ja, ar, hi): 4 zapisane z 4, wszystkie bez rozbieżności, mediana czasu 1 min 52 s.
Próba kontrolna tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 cytaty po angielsku), przetłumaczonym poza
blogiem przez `gemini-3.7-flash-medium`: 14 zapisanych z 14, wszystkie bez rozbieżności, od 87 do
128 s na język.

Wiersze `--use_claude_code` zmierzono 26 września na tym samym
artykule, wykonując cztery tłumaczenia równolegle, przy nakładzie pracy (effort) `low`. W przypadku `sonnet`
angielskie cytaty pozostały nienaruszone we wszystkich czternastu językach, a w języku angielskim
model samodzielnie usunął linie francuskiego tłumaczenia, nie dodając żadnej
flagi. Model `opus` nie zapisał żadnego języka: w każdym z nich filtry bezpieczeństwa
zatrzymały odpowiedź na ostatnim segmencie z powodu wzmianki o 279 cząsteczkach
wygenerowanych dla miejsca wiązania. Wysłana osobno, notatka ta zostaje odrzucona
w ramach kategorii „bio”; model `sonnet` przetłumaczył ją wszędzie. `haiku` zapisuje
wszystkie czternaście języków; w trzech (en, pl, ro) tytuł sekcji zmienia
poziom z 2 na 1. Rozumuje bez możliwości powstrzymania go — 61%
jego tokenów wyjściowych —, co przekłada się na ponad dwukrotnie dłuższy czas niż w przypadku `sonnet`.

Wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` oraz `claude-haiku-4-5` zostały
zmierzone 18 października przez API Anthropic, na tym samym artykule, po cztery
równoległe tłumaczenia na model. Sonnet 5.5 nie pozwala na wyłączenie
rozumowania: aipmt przekazuje mu najniższą akceptowaną przez niego wartość, a jego
odpowiedzi nie zawierają żadnego rozumowania. Zapisuje czternaście języków bez rozbieżności i bez
ponawiania segmentu; w języku angielskim sam usunął linie
francuskiego tłumaczenia, bez wymyślania flagi, a angielskie cytaty są
nienaruszone wszędzie. Haiku 5.5 jest mierzony z adaptacyjnym rozumowaniem: przy wyłączonym
rozumowaniu pozostawiał całe akapity po francusku, co filtr odrzuca —
zapisano zaledwie 3 języki z 14. Oba modele Haiku potykają się na tej samej notatce: Haiku 5.5
zmienia poziom jej tytułu lub go dubluje w języku japońskim, koreańskim i
chińskim, z kolei Haiku 4.5 podnosi go do poziomu 1 w siedmiu językach, a w japońskim pozostawia
po francusku. Haiku 4.5 kosztuje 3,67 $ za oba dokumenty we
wszystkich czternastu językach, Haiku 5.5 — 0,57 $, a Sonnet 5.5 — 9,21 $.

### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026 r.: 785 wierszy, 285 fragmentów kodu w tekście, 40
zamknięć bloków, 89 wierszy tabeli. Cztery tłumaczenia równolegle.

| Model                                           | Zapisane | Bez różnic | Mediana/język  | Co się różni                                                             |
| ----------------------------------------------- | -------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14   | 1 min 43 s     | nic                                                                      |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14   | 1 min 48 s     | nic                                                                      |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14   | 4 min 02 s     | nic dla narzędzia porównującego; zduplikowane linki wewnętrzne (en)      |
| `claude-sonnet-5-5`                             | 14/14    | ✅ 14/14   | 1 min 18 s     | nic                                                                      |
| `claude-haiku-4-5`                              | 14/14    | ✅ 14/14   | 2 min 06 s     | nic                                                                      |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14   | 36 s           | jedno słowo pogrubione (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14   | 1 min 22 s     | jedno słowo pogrubione (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14   | 2 min 20 s     | wiersz tabeli połączony z poprzednim (ar)                                 |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14   | 2 min 56 s     | jeden link (sv), jedno słowo pogrubione (zh)                             |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14   | 6 min 46 s     | jedno słowo pogrubione (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14   | 2 min 34 s     | jedno słowo pogrubione (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14   | 2 min 17 s     | 40 fragmentów kodu w tekście dodanych w arabskim; pogrubienie (hi, ja, ko)|
| `claude-haiku-5-5`                              | 12/14    | ❌ 12/14   | 1 min 14 s     | 2 języki odrzucone (ar, hi): utracone kody w tekście w odpowiedzi        |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14    | 2 min 44 s     | utracona sekcja (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh)        |

Dwie przerwane serie nie zostały uwzględnione: Grok, sesja CLI wygasła
po dwunastu językach (jedenaście bez różnic), oraz `qwen3.8-flash`, błąd HTTP 429 od jego
dostawcy po dwóch. Modele `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie były ponownie mierzone na tej wersji; w wersji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisał po 9 z 14 tłumaczeń, w tym odpowiednio 7
i 1 bez różnic.

Pozycje `--use_antigravity` i `--use_claude_code` nie były mierzone na
wersji zamrożonej, lecz 26 września na wersji opublikowanej wraz z 1.14.0 — a
pozycje `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5` 18
października na tej samej: 600 wierszy, 257 fragmentów kodu w tekście, 30 zamknięć bloków, 85
wierszy tabeli. Będąc
krótszą o 185 wierszy, nie pozwala na bezpośrednie porównanie z pozostałymi pozycjami;
te konkretne pozycje można jednak porównywać między sobą. W przypadku linków wewnętrznych, których
narzędzie porównujące nie weryfikuje, `gemini-3.8-flash-medium` zachował je nienaruszone we
wszystkich czternastu językach, `gemini-3.7-flash-medium` uszkodził je we włoskim;
`sonnet` i `opus` zachowały je nienaruszone wszędzie, `haiku` zduplikował je w
angielskim; `claude-sonnet-5-5` i `claude-haiku-4-5` zachowały je nienaruszone w
czternastu językach, a `claude-haiku-5-5` w dwunastu, które zapisał.

### Cztery pliki README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane wprost z GitHuba — dokumenty
prostsze niż dwa poprzednie. Seria testów była skierowana do modeli
mających trudności; Gemini służy tu jako punkt odniesienia.

| Model                     | Zakres                     | Zapisane | Bez różnic   |
| ------------------------- | -------------------------- | -------- | ------------ |
| `gemini-3.7-flash`        | 4 projekty × 14 języków    | 56/56    | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków    | 55/56    | ❌ 47/56     |
| `grok-4.6` (subskrypcja)   | 4 projekty × ar, hi, ja, zh| 16/16    | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh| 15/16    | ❌ 9/16      |

### Czym te pomiary nie są

- **To nie jest wyczerpujący ranking**: sam OpenRouter oferuje ponad czterysta
  modeli, zmierzono około piętnastu.
- **To orientacyjne czasy trwania**: od trzech do sześciu tłumaczeń równolegle w
  zależności od serii, a przepustowość dostawcy zmienia się w ciągu dnia.
- **To obserwacje osadzone w czasie**: modele zmieniają się pod tą samą nazwą, a Twoje
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

Oba wiersze są wymagane: bez `pip install -e .`, `python -m aipmt`
odpowiada `No module named aipmt`.

Narzędzia jakościowe, opcjonalne, lecz zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń w repozytorium (README i CHANGELOG, czternaście języków)
generuje się ponownie za pomocą `./regen_translations.sh --force` — Codex i `gpt-6.1-sol` w ramach
domyślnej subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` i
`REGEN_MODEL` zmieniają ścieżkę: `antigravity` pozostaje na subskrypcji, tym razem
Google, i przechodzi bez odstępstw; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1800 s w przypadku Codex i
Antigravity). Szczegółowe informacje o narzędziach znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — osobisty blog publikowany w 15 językach. Jego
  [codzienny przegląd AI](https://jls42.org/fr/news) jest tłumaczony każdego dnia
  przez to narzędzie i służy jako dokument referencyjny dla powyższych pomiarów.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Wersja 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Zastrzeżenie

Ten program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, na warunkach
określonych w sekcjach 15 i 16 licencji GPL v3: dostarczany w stanie „takim, w jakim jest” (as is), bez dorozumianej gwarancji przydatności
handlowej ani przydatności do określonego celu, a jego autor nie ponosi
odpowiedzialności za szkody wynikające z jego użytkowania. Pełny tekst
licencji ma pierwszeństwo przed niniejszym podsumowaniem.

- **Przeczytaj przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod w tekście, adresy URL, kotwice oraz cytaty w trybie `--news` — nie obejmują
  nagłówków, tabel, sekcji front matter ani sensu Twoich zdań.
- **Twoje dokumenty trafiają do wybranego dostawcy**, zgodnie z jego regulaminem
  i polityką prywatności danych. Niektóre bezpłatne modele mogą
  wykorzystywać Twoje rozmowy do trenowania, a warunki usługi Antigravity
  pozwalają Google na ich ponowne wykorzystanie oraz przekazywanie do weryfikacji przez ludzi,
  w tym w ramach płatnej subskrypcji; model lokalny to jedyny sposób, aby
  żadne dane nie opuściły Twojego komputera.
- **Wywołania API są płatne.** Ten program nie nakłada limitu
  wydatków: długi dokument, wznowienie po błędzie lub model, który intensywnie
  rozumuje, generują wyższe koszty.
- **Opublikowane pomiary to obserwacje osadzone w czasie**, a nie gwarancje.

Wymienione nazwy produktów i firm należą do ich odpowiednich
właścicieli. Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z fr na pl za pomocą gemini-3.8-flash-medium.**
