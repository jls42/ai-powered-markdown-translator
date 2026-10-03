# Tłumacz Markdown AI-Powered

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Powielone linie (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linie kodu"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Odznaka Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumaczy pliki Markdown z jednego języka na inny, zachowując strukturę:
bloki kodu, kod w tekście, adresy URL, kotwice, tabele i front matter.
Jedenaście sposobów wywołania modelu — pięć API, cztery subskrypcje bez
rozliczania według zużycia, dwa routery — oraz opublikowany pomiar tego, co
każdy model rzeczywiście zachowuje.

## W skrócie

- **Jedenaście ścieżek dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex), Grok, Google (Antigravity) i Claude (Claude
  Code) bez rozliczania według zużycia; routery OpenCode (open source, darmowy lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Żadnych błędów z powodu utraconego tokena**: bloki kodu, kod w tekście,
  adresy URL, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  weryfikowane po powrocie. Jeśli któregoś brakuje, plik nie zostaje zapisany.
- **Długie dokumenty**: segmentacja według okna kontekstowego modelu.
- **Tryb `--news`**: chronione angielskie cytaty i flagi zarządzane według
  języka, dla artykułów przeglądowych.
- **Tryb `--eco`**: szybkie i tańsze modele.
- Opcjonalna **nota o tłumaczeniu**, na górze, na dole lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 lub nowszy. Aby zainstalować z repozytorium, zobacz
[Współtworzenie](#współpraca).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego priorytetu do najniższego;
każde kolejne uzupełnia tylko to, co poprzednie pozostawiło puste.

|     | Gdzie                                                | Do czego                              |
| --- | ---------------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                                 | CI, kontenery, jednorazowe nadpisanie |
| 2   | `.env` w bieżącym katalogu (lub nadrzędnym)   | klucz specyficzny dla projektu        |
| 3   | `~/.config/aipmt/.env`                                        | zainstalowany raz, działa wszędzie    |

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
użytkownika jest zgodny z `XDG_CONFIG_HOME` (tylko ścieżka bezwzględna) oraz `%APPDATA%`
w systemie Windows. Bez klucza polecenie wymienia wszystkie trzy lokalizacje.

**Plik `.env` projektu nie może ani przekierowywać wywołań, ani wybierać uruchamianego
programu.** Dostarcza klucze, nigdy cel ani plik binarny: każda
zmienna w `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane z ostrzeżeniem. Sklonowane repozytorium nie powinno
mieć możliwości przejęcia Twojego klucza ani zmuszenia Cię do uruchomienia własnego programu
przy pierwszym tłumaczeniu. Plik ten jest również odczytywany bez interpolacji:
`NOM=${OPENAI_API_KEY}` nie kopiuje w nim klucza. Umieść te zmienne w
środowisku lub w `~/.config/aipmt/.env`.

Opcjonalne zmienne: `XAI_BASE_URL` (domyślnie `https://api.x.ai/v1`),
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

`document.md` przetłumaczony na język hiszpański daje `document-es.md` w `--target_dir`;
z `--include_model`, `document-es-gpt-5.6-terra.md`. Rozszerzenie zawsze
staje się `.md` — `article.mdx` daje `article-en.md` — z wyjątkiem
`--keep_filename`, który zachowuje pierwotną nazwę. Istniejące już tłumaczenie
jest pomijane bez flagi `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli pozostał plik
z błędem (lista na standardowym wyjściu błędów), `2`, jeśli problem dotyczy konfiguracji.
Plik z błędem nigdy nie jest zapisywany, nawet jeśli sam zapis się nie powiedzie:
zawartość jest zapisywana obok, a następnie zmieniana jest jej nazwa. Wystarczy uruchomić ponownie.

## Jaki model wybrać

Zmierzone na dwóch rzeczywistych dokumentach, przetłumaczonych na te same
czternaście języków przez każdy model. **Liczba oznacza liczbę języków (na
czternaście), w których tłumaczenie zostało zapisane i w których nic nie różni się od źródła.**

| Model                | Jak uzyskać dostęp                | Gęsty artykuł przeglądowy | To README   | Co się różni i w ilu językach                                                                                                                                      |
| -------------------- | --------------------------------- | ------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ✅ 14/14    | nic, w żadnym z dwóch dokumentów                                                                                                                                   |
| **Gemini 3.7 Flash** | klucz API Google                  | ✅ 14/14                  | ⚠️ 13/14    | 1 język na 14: o jedno pogrubione słowo więcej (ja)                                                                                                                |
| **Gemini 3.7 Flash** | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ⚠️ 13/14    | 1 język na 14: o jedno pogrubione słowo mniej (ko)                                                                                                                 |
| **GPT-5.6 Sol**      | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14               | ⚠️ 12/14    | 2 języki na 14: o jedno pogrubione słowo mniej (ar, ja)                                                                                                            |
| **GLM-5.2**          | klucz OpenRouter                  | ✅ 14/14                  | ⚠️ 11/14    | 3 języki na 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                                                        |
| Claude Sonnet 5      | subskrypcja Claude (Claude Code)  | ⚠️ 13/14                  | ⚠️ 13/14    | 1 język na 14 w artykule: o jedno pogrubione słowo więcej (zh); 1 w tym README: wiersz tabeli połączony z poprzednim, ukryty podczas wyświetlania (ar)            |
| Claude Haiku 4.5     | subskrypcja Claude (Claude Code)  | ⚠️ 11/14                  | ✅ 14/14    | 3 języki w artykule: nagłówek sekcji zmieniony na poziom 1 (en, pl, ro); w tym README nic dla narzędzia porównującego, ale linki wewnętrzne powielone po angielsku |
| Claude Sonnet 5      | klucz API Anthropic               | ⚠️ 11/14                  | ⚠️ 12/14    | 3 języki w artykule: dodany blok kodu (es, de, hi); 2 w tym README: link bez znaczników formatowania (sv), pogrubione słowo (zh)                                   |
| Qwen 3.7 Flash       | klucz OpenRouter                  | ❌ 8/14                   | ⚠️ 10/14    | 1 język odrzucony w artykule, 5 innych odbiega od normy; w tym README około czterdziestu słów umieszczonych w `code` (ar)                                  |
| Grok 4.6             | subskrypcja Grok                  | ❌ 8/14                   | nieoceniony | 5 języków na 14 odrzuconych z powodu braku zwróconego kodu w tekście i adresów URL; holenderski różni się we wszystkim                                             |
| GPT-OSS 20B          | model lokalny (Ollama)            | ❌ 7/14                   | nieponowiony| 4 języki na 14 odrzucone: model pozostawił w nich fragmenty po francusku, strażnik je zatrzymał                                                                     |
| MiMo v2.5 (darmowy)  | OpenCode Zen, bez konta           | ❌ 11/14                  | nieponowiony| 1 język odrzucony; utracona sekcja w języku polskim                                                                                                                |
| Mistral Large        | klucz API Mistral                 | ❌ 5/14                   | ❌ 1/14     | **cała sekcja znika**: 1 język w artykule (hi), 3 w tym README (ar, hi, ko) — oraz 3 języki odrzucone w artykule                                                   |
| DeepSeek V4 Flash    | klucz OpenRouter                  | ❌ 3/14                   | nieponowiony| 10 języków na 14 odrzuconych; 37 minut na język                                                                                                                    |
| Claude Opus 5.5      | subskrypcja Claude (Claude Code)  | ❌ 0/14                   | ✅ 14/14    | artykuł odrzucony we wszystkich 14 językach przez mechanizmy zabezpieczające Opusa z powodu wzmianki o biologii; nic w tym README                                 |

|     | Co oznacza symbol                                                                                                                                                                                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | wszystkie czternaście języków przetłumaczonych i nic nie różni się od źródła                                                                                                                          |
| ⚠️  | wszystkie czternaście języków przetłumaczonych; to, co się różni, to **formatowanie** — pogrubione słowo, `code`, link tracący nawiasy kwadratowe. Nie brakuje żadnego tekstu, adresu URL, bloku kodu ani sekcji |
| ❌  | co najmniej jeden język nie mógł zostać przetłumaczony — plik został odrzucony, niezapisany — **lub** w zapisanym pliku brakuje zawartości                                                            |

Najważniejsze wnioski:

- **Odrzucone tłumaczenie to nie to samo co uszkodzone tłumaczenie.** Kiedy po powrocie
  brakuje tokena, plik nie jest zapisywany, a język liczy się jako
  odrzucony. To właśnie przydarzyło się Grokowi w artykule: cztery fragmenty kodu w tekście i
  trzy adresy URL utracone już w pierwszym segmencie w pięciu pismach nielacińskich.
- **Model może odrzucić cały dokument z powodu jednego zdania.** Opus 5.5
  tłumaczy to README bez żadnych odchyleń, ale ani jednego artykułu przeglądowego: jego
  mechanizmy zabezpieczające zatrzymują odpowiedź na krótkiej notatce biologicznej. Plik nie zostaje
  zapisany, a aipmt wyjaśnia dlaczego.
- **Ta siatka ochronna nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik, który narzędzie zapisuje
  bez problemu — tak jest w przypadku Mistrala. Elementy te nie mogą zostać
  zastąpione tokenem, a obecne zabezpieczenia ich nie kontrolują;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego README**: jego sesja CLI wygasła po dwunastu
  językach, z czego jedenaście było bez odchyleń. Przerwany przebieg testów nie podlega ocenie.
- **Gęstość dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze
  zwykłymi plikami README i gubi się przy artykule przeładowanym linkami, w tym w
  języku niderlandzkim.

Daty i dokumenty: kolumna „To README” została zmierzona 9 września 2026 r.
na zamrożonej rewizji tego pliku (785 wierszy, 285 fragmentów kodu w tekście, 89 wierszy
tabeli), modyfikowanej od tego czasu — z wyjątkiem wierszy Antigravity i Claude Code,
zmierzonych 26 września na rewizji opublikowanej z wersją 1.14.0, krótszej
(600 wierszy, 257 fragmentów kodu w tekście, 85 wierszy tabeli). Kolumna „Gęsty artykuł
przeglądowy” pochodzi z testów z 4 i 5 września na artykule liczącym 589
wierszy, z wyjątkiem wiersza Grok, zmierzonego ponownie 9 września na innym wydaniu tego
samego przeglądu, oraz wierszy Antigravity i Claude Code, zmierzonych 26 września
na tym samym artykule. Pełne tabele, czasy trwania i protokół znajdują się w
[Szczegółowych pomiarach](#szczegółowe-pomiary).

## Wszystkie opcje

| Opcja                    | Opis                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia (alternatywa dla `--source_dir`)                                 |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown (domyślnie: `content/posts`)                                       |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików (domyślnie: `traductions_en`)                                    |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                                                    |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                                                   |
| `--model`                | Konkretny model do użycia                                                                                     |
| `--eco`                  | Użyj modeli ekonomicznych                                                                                     |
| `--use_mistral`          | Użyj API Mistral AI                                                                                           |
| `--use_claude`           | Użyj API Claude                                                                                               |
| `--use_gemini`           | Użyj API Gemini                                                                                               |
| `--use_grok`             | Użyj API xAI (Grok) — wymaga `XAI_API_KEY`                                                                   |
| `--use_codex`            | Użyj CLI Codex w ramach limitu subskrypcji ChatGPT                                                            |
| `--use_grok_cli`         | Użyj CLI Grok w ramach limitu subskrypcji Grok                                                                |
| `--use_antigravity`      | Użyj CLI Antigravity (`agy`) w ramach limitu subskrypcji Google AI Pro lub Ultra                     |
| `--use_claude_code`      | Użyj CLI Claude Code (`claude -p`) w ramach limitu subskrypcji Claude Pro lub Max                          |
| `--use_opencode`         | Użyj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle`                      |
| `--use_openrouter`       | Użyj OpenRouter — wymaga `OPENROUTER_API_KEY` i `--model fournisseur/modèle`                                                      |
| `--force`                | Wymuś ponowne tłumaczenie                                                                                     |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                                                                |
| `--news`                 | Tryb aktualności: chroni cytaty w EN, obsługuje flagi według języka                                           |
| `--add_translation_note` | Dodaj notatkę o tłumaczeniu                                                                                   |
| `--note_position`        | Pozycja notatki: `top`, `bottom` (domyślnie) lub `both`                                |
| `--note_format`          | Format notatki: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                           |
| `--include_model`        | Dołącz nazwę modelu w pliku wyjściowym                                                                        |
| `--reasoning_effort`     | Poziom rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`  |

Dziewięć flag `--use_*` wzajemnie się wyklucza: połączenie dwóch z nich zostanie
odrzucone.

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

| Dostawca    | Jakość (domyślnie)                                    | Ekonomiczny (`--eco`)     |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`                  |
| Codex       | `gpt-5.6-sol` (również `terra` i `luna` przez `--model`) | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                   |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`                   |
| Claude Code | `sonnet`, effort `low`                                | to samo — `--eco` bez wpływu |
| OpenCode    | `--model provider/modèle` wymagany                    | to samo — `--eco` bez wpływu |
| OpenRouter  | `--model fournisseur/modèle` wymagany                 | to samo — `--eco` bez wpływu |

### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest rozliczane z limitu
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
- Każdy segment kosztuje co najmniej jedną „wiadomość” z 5-godzinnego okna — dwie,
  jeśli jego walidacja się nie powiedzie i nastąpi ponowna próba. OpenAI szacunkowo podaje
  250–2000 wiadomości/5 godz. dla `gpt-5.6-luna` (`--eco`) oraz
  10–100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-terra` i `--model gpt-5.6-luna` również przechodzą przez
  subskrypcję. Model, do którego konto nie ma uprawnień, zwraca błąd 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Wolniejsze niż API, a różnica rośnie wraz z rozmiarem dokumentu: dla tego README
  mediana wynosi 6 min 46 s na język przy użyciu `gpt-5.6-sol`, w porównaniu z 36 s dla
  `gemini-3.7-flash`.
- Odrzucane w środowisku CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): subskrypcja uwierzytelnia się
  za pomocą osobistego pliku sesji, który nie powinien znajdować się na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada w przypadku oficjalnego CLI Grok Build, w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Piaskownica systemowa (sandbox OS) Groka nie działa
  na wielu współczesnych maszynach z systemem Linux (AppArmor, gniazda runtime
  kontenerów), a profil, którego nie można zastosować, uruchamia się po cichu bez
  izolacji. Skrypt nie wymaga więc domyślnie żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` narzędzia CLI, w tym regule typu catch-all `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast po cichu usuwać ochronę.
  `GROK_TRANSLATE_SANDBOX=read-only` wymaga piaskownicy systemowej, a uruchomienie
  kończy się niepowodzeniem, jeśli maszyna nie może jej zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, i żadne
  polecenie nie pozwala go odczytać: partia zadań może wyczerpać limit na konwersacje
  bez żadnego ostrzeżenia.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach subskrypcji Google: `--use_antigravity`

Ta sama zasada w przypadku `agy`, oficjalnego CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie jest rozliczane z limitu subskrypcji zamiast
naliczania opłat za tokeny. To jedyna droga do tego limitu: Gemini CLI nie
obsługuje już tych kont od 18 czerwca 2026 roku
([ogłoszenie](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
a SDK Antigravity akceptuje wyłącznie klucz API lub projekt Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Żadna płatna ścieżka nie pozostaje otwarta.** agy otrzymuje z Twojego
  środowiska jedynie zamkniętą listę zmiennych — `PATH`, język i strefę czasową,
  terminal, tożsamość, proxy i certyfikaty, magistralę sesji — i żadnych kluczy:
  kilka z jego zmiennych potrafi przełączyć wywołanie bez wyświetlania czegokolwiek (zmierzone:
  jedna wysyła dokument do zewnętrznej bramy, inna do płatnego projektu
  Google Cloud), a w liście blokowanych zmiennych przy każdym przeglądzie czegoś brakowało.
  Przed jakimkolwiek segmentem polecenie `agy -p /config`, które nie zużywa limitu, musi wykazać,
  że płatne kredyty AI są wyłączone, bez klucza API ani projektu Google Cloud — brakujące
  ustawienie oznacza odmowę —, w przeciwnym razie nic nie zostanie przetłumaczone; log każdego
  wywołania musi następnie potwierdzać subskrypcję (`authMethod=consumer`), w przeciwnym razie
  odpowiedź zostanie odrzucona.
- **Izolacja.** Każde wywołanie działa w prywatnym i tymczasowym katalogu
  domowym z agentem tłumaczącym pozbawionym narzędzi: Twoje ustawienia, reguły,
  wtyczki, serwery MCP i hooki agy nie mają do niego dostępu, nic nie jest dodawane do Twojej
  historii, a dane logowania pozostają w pęku kluczy, którego aipmt nigdy nie czyta.
  W przypadku nieznalezienia agenta agy po cichu wraca do swojego agenta programistycznego
  i jego narzędzi: pełna linia w logu musi potwierdzić prawidłowego agenta — dokument
  cytujący ten komunikat jej nie zastępuje —, w przeciwnym razie następuje odmowa.
- **Platformy**: Linux, w sesji posiadającej pęk kluczy (magistrala sesji
  D-Bus, Secret Service); macOS jest akceptowany, choć nie był tam mierzony. Odrzucane
  w systemie Windows, gdzie agy nie czyta zmiennych izolujących każde wywołanie, oraz
  w systemie Linux bez magistrali sesyjnej — sesja SSH, kontener, serwer: agy przechowuje
  tam swój token w pliku w katalogu `~/.gemini`, co izolacja maskuje. Odmowa
  następuje przed jakimkolwiek uruchomieniem, wraz z podaniem przyczyny, zamiast minutowego
  oczekiwania na kod logowania.
- **Modele**: modele z `agy models`. Modele Gemini mają poziom rozumowania w nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez sufiksu jest odrzucana przed wywołaniem,
  a `--reasoning_effort` nie ma wpływu. Domyślnie `gemini-3.8-flash-medium`,
  a `gemini-3.7-flash-low` w `--eco`; serie testowe, w których je ustalono,
  opisano w sekcji [Mesures détaillées](#szczegółowe-pomiary). Claude i GPT-OSS
  mają własny, znacznie mniejszy limit: około 1% 5-godzinnego okna na
  zmierzone wywołanie, w porównaniu z 0,05% w przypadku Flash.
- **Limit**: według grupy, jedno 5-godzinne okno i jedno tygodniowe, proporcjonalnie
  do kosztu w tokenach. Zmierzone na koncie autora: około
  16 punktów z 5-godzinnego okna na milion znaków źródłowych w
  `gemini-3.8-flash-medium`, 14 w `gemini-3.7-flash-medium` i 7 do 8 przy
  niskim poziomie rozumowania — README o objętości 40 000 znaków kosztuje więc nieco ponad
  pół punktu. Tygodniowy limit zależy natomiast od planu. Ponawianie prób odbywa się zgodnie
  z tym, co agy zgłasza jako możliwe do ponowienia; w przeciwnym razie wyczerpane okno nigdy nie
  jest ponawiane: powoduje błąd każdego pliku aż do zresetowania,
  które wyświetla `/usage`.
- **Wolniejsze niż API**: w przypadku gęstego artykułu z pomiarami mediana wynosi 3 min 59 s na
  język w `gemini-3.8-flash-medium` i 3 min 14 s w
  `gemini-3.7-flash-medium`, w porównaniu z 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerwanie**: Ctrl-C lub zamknięcie terminala zatrzymuje agy wraz z
  poleceniem, zamiast pozwalać mu dokończyć działanie na Twoim limicie; to samo
  dotyczy Codex, Grok CLI i OpenCode. W przypadku `nohup` tłumaczenie jest kontynuowane.
- Odrzucane w środowisku CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): sesja logowania znajduje się
  w osobistym pęku kluczy. Na runnerze należy użyć `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment, łącznie z uruchomieniem, domyślnie 900).

**Warunki korzystania: ponosisz odpowiedzialność za swoje konto.**
[Warunki korzystania z Antigravity](https://antigravity.google/terms) (sekcja 6) oraz
[FAQ](https://antigravity.google/docs/faq/) zabraniają dostępu do usługi
za pomocą oprogramowania innych firm z użyciem logowania Antigravity — wymieniono tam
Claude Code, OpenClaw i OpenCode — pod rygorem zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokena: uruchamia oficjalny plik binarny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
dokumentuje dla skryptów i CI. Przedstawiciel Google uznał za „standardowe”
uruchamianie `agy -p` z lokalnego skryptu na własne potrzeby
([oficjalne forum, 25 września 2026 r., odpowiedź niewiążąca](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden oficjalny dokument nie rozstrzyga jednoznacznie kwestii narzędzia dystrybuowanego w taki sposób jak to.

**Tylko dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków cała
wymiana danych — prompty, odpowiedzi, metadane — może służyć do ulepszania
produktów oraz uczenia maszynowego Google i może być przeglądana przez
ludzi, również w przypadku płatnej subskrypcji. Rezygnacja wymaga ustawienia
`enableTelemetry` o nieudokumentowanym działaniu, którego aipmt nie konfiguruje; Twoje ustawienia
agy nie przenoszą się do jego izolowanego środowiska. Nie przesyłaj tą drogą żadnych poufnych informacji.

### W ramach subskrypcji Claude: `--use_claude_code`

Ta sama zasada dotyczy `claude`, oficjalnego CLI Claude Code, w trybie `-p`: dla
osób opłacających Claude Pro lub Max tłumaczenie jest odliczane z limitu
subskrypcji, zamiast być rozliczane za tokeny. Nie należy mylić z
`--use_claude`, API Anthropic, rozliczanym według użycia.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Żadna płatna ścieżka nie pozostaje otwarta, a każde wywołanie to potwierdza.** Claude
  Code otrzymuje z Twojego środowiska wyłącznie zamkniętą listę zmiennych — ani
  klucza API, ani tokena, ani dostawcy chmurowego, ani znacznika sesji Claude Code,
  z której aipmt zostałby uruchomiony. Przed pierwszym segmentem `claude auth status` musi
  wykazać połączenie w ramach subskrypcji, bez klucza Console, a `/usage`, które nie zużywa
  żadnego limitu, musi to poświadczyć; każde wywołanie poświadcza to z kolei w swoim
  zdarzeniu inicjalizacyjnym, w przeciwnym razie odpowiedź jest odrzucana.
- **Wyłącz „extra usage”** (claude.ai, Ustawienia → Użycie), aby
  utrzymać koszt zero euro: gdy jest włączone, przejmuje obsługę po wyczerpaniu okna i
  nalicza opłaty bez wyświetlania błędu. aipmt przerywa tłumaczenie, gdy tylko odczyt
  limitu wywołania to zasygnalizuje, ale to konkretne wywołanie jest już naliczone.
- **Limit współdzielony z sesjami Claude Code.** Każde wywołanie raportuje
  wykorzystanie okien 5-godzinnych i tygodniowych; powyżej 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) żaden kolejny segment nie jest uruchamiany, aby
  nie wyczerpać zasobów potrzebnych do Twojej pracy.
- **Izolacja.** Każde wywołanie działa bez narzędzi, w prywatnym,
  tymczasowym katalogu, w trybie bez personalizacji: ani Twoje `CLAUDE.md`, ani Twoje wtyczki,
  hooki, serwery MCP czy ustawienia nie są ładowane, a z sesji nic nie jest
  zachowywane. Załączniki są wyłączone: `@chemin` w Twoim dokumencie
  pozostaje tekstem i nie otwiera żadnego pliku (zmierzone).
- **Modele**: domyślnie `sonnet`, z nakładem `low`, oraz w `--eco` również:
  `--eco` nic nie zmienia na tej ścieżce. Zmierzone na tych samych dokumentach: `haiku`
  jest dwukrotnie wolniejszy — rozumuje bez możliwości wyłączenia tego — przy
  koszcie zaledwie nieznacznie niższym, a `opus` odrzuca treści biologiczne (kolejny
  punkt). Oba pozostają dostępne przez `--model`; te aliasy podążają za
  najnowszym modelem ze swojej rodziny. `fable` i warianty `[1m]` są odrzucane,
  ponieważ przechodzą na płatne środki. `--reasoning_effort` reguluje nakład,
  z którego tłumaczenie nic nie zyskuje: zmierzone rozumowanie jest zerowe lub niemal zerowe.
- **Opus odrzuca niektóre treści biologiczne.** Jego zabezpieczenia są
  bardziej rygorystyczne niż w przypadku Sonnet, a komunikat o błędzie Anthropic ostrzega, że
  „can sometimes flag biology-research-adjacent work”. Zmierzone: krótka notatka
  prasowa o 279 wygenerowanych cząsteczkach spowodowała odrzucenie artykułu we wszystkich czternastu
  językach. Nic nie zostaje zapisane: aipmt odrzuca uciętą odpowiedź, wskazuje
  zabezpieczenia i zaleca `--model sonnet`.
- Odrzucane w środowisku CI (`CI` lub `GITHUB_ACTIONS` zdefiniowane) oraz pod Windows (niezmierzone).
- Zmienne: `AIPMT_CLAUDE_BIN` (w przeciwnym razie `PATH`, następnie `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekundy na segment, domyślnie 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (domyślnie 0.8), `CLAUDE_CONFIG_DIR` (konto
  Claude Code, nigdy nie pobierane z `.env` projektu); katalogi robocze w
  `XDG_CACHE_HOME/aipmt/claude-code` (domyślnie `~/.cache`).

**Warunki korzystania: to Twoje konto ponosi odpowiedzialność.** Strona
[prawna Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nie zabrania „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription”: to właśnie robi aipmt, który uruchamia
oficjalny plik binarny i nigdy nie odczytuje tokena. Jednak Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users”, preferuje klucz API dla narzędzi
zewnętrznych, „including open-source projects”, i zastrzega sobie prawo do rozliczania ich
użycia z płatnych środków
([pomoc Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Żaden zapis jednoznacznie nie rozstrzyga przypadku dystrybuowanego narzędzia uruchamiającego plik binarny.

**Dane**: na kontach Free, Pro i Max trenowanie modeli
dotyczy również Claude Code, gdy pozwala na to ustawienie prywatności
([strona o danych](https://code.claude.com/docs/en/data-usage)). aipmt nie przechowuje
żadnej lokalnej transkrypcji (`--no-session-persistence`). Nie przesyłaj tam
niczego poufnego.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to otwartoźródłowy (MIT) agent kodujący, który
kieruje zapytania do skonfigurowanych w nim dostawców: klucza API, subskrypcji,
bramki OpenCode Zen (darmowe modele, bez konta) lub modelu lokalnego. Zmierzono
tutaj kompleksowo dwie ścieżki: Zen oraz Ollama.

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

`--model` jest obowiązkowy: bez niego OpenCode powróciłby do darmowego modelu,
którego wymiana danych może służyć do trenowania, a ten wybór nie powinien zapadać
za Ciebie.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, mająca pierwszeństwo przed Twoją, definiuje agenta `aipmt`,
  którego wszystkie narzędzia są odrzucane (`permission: { "*": "deny" }`), udostępnianie
  sesji wyłączone, `--pure`, nigdy `--auto`;
- tymczasowy i pusty katalog roboczy, z utworzonymi `OPENCODE_DISABLE_PROJECT_CONFIG` oraz
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstrzykuje do
  promptu `AGENTS.md` bieżącego katalogu oraz `~/.claude/CLAUDE.md`.
  Globalny `~/.config/opencode/AGENTS.md` nadal jest wstrzykiwany, OpenCode nie pozwala
  go pominąć;
- kontrakt wyjściowy: kod wyjścia 0, brak zdarzenia `error`, brak wywołania
  narzędzia, ostatni krok jako `stop`, niepusty tekst i rzeczywiście
  załadowany agent `aipmt` — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  dyskretnie cofa się do agenta kodującego;
- żaden klucz z `aipmt` nie jest przekazywany, z wyjątkiem `OPENCODE_API_KEY`, klucza
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  `.env` narzędzia `aipmt`.

Warto wiedzieć:

- Darmowe modele Zen podlegają zmianom, mają nieudokumentowane limity, a
  przesyłane do nich dane mogą służyć do trenowania: nadają się do publicznej
  dokumentacji, nie do prywatnych treści.
- Model lokalny musi oferować co najmniej 16k tokenów kontekstu, ponieważ segmenty
  mają do 16 000 znaków. Ollama często konfiguruje 4096: należy użyć
  `Modelfile` z `PARAMETER num_ctx 32768`.
- `--eco` nie przynosi efektu; `--reasoning_effort` jest przekazywany bez zmian jako
  `--variant` w OpenCode.
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

`reasoningEffort: "none"` wyłącza wnioskowanie, które Ollama domyślnie aktywuje na tych
modelach i którego Modelfile nie może wyłączyć. Zmierzone na zdaniu złożonym
z sześciu słów: 919 tokenów wnioskowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według użycia, z pojedynczego salda, zapewniający
dostęp do modeli hostowanych przez podmioty trzecie — w tym otwartych modeli chińskich,
których żaden inny dostawca tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest obowiązkowy. Test wstępny (preflight), wykonywany przed jakimkolwiek naliczeniem opłat, obsługuje
dwie specyfiki routingu:

- **Ten sam model jest obsługiwany przez dziesiątki hostów o różnych limitach** —
  w przypadku `z-ai/glm-5.3-flash` to 23 hostów, w tym jeden ograniczony do
  2048 tokenów wyjściowych. Preflight odczytuje `/api/v1/models/{modèle}/endpoints`,
  odrzuca hostów oferujących poniżej 8000 tokenów wyjściowych lub ze statusem obniżonej jakości, a
  pozostałych przypina za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki wyjściowej** — 107 tokenów w porównaniu do 2 przy
  odpowiedzi „OK” z `z-ai/glm-5.2`. Domyślnie jest wyłączone; modele,
  które go wymagają, otrzymują najniższy akceptowany przez nie nakład, ponieważ domyślna wartość
  z katalogu mogłaby nasycić wyjście przed zakończeniem tłumaczenia.
  `--reasoning_effort` zachowuje pierwszeństwo.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model z oknem poniżej 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8400 na prompt i segment, minimum 8000
  na wyjściu.
- Slug nieobecny w katalogu, niedostępny katalog lub brak
  hosta spełniającego wymóg limitu zatrzymują polecenie.
- `finish_reason=length` z pustym wyjściem oznacza budżet skonsumowany przez
  rozumowanie, a nie ucięcie: komunikat wyraźnie to rozróżnia.
- `--eco` nie przynosi efektu.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Notatka o tłumaczeniu

`--add_translation_note` dodaje notatkę, w `bottom` (domyślnie), `top` (po
front matterze) lub `both` (`--note_position`), w formacie `legacy` (akapit
pogrubiony, domyślnie) lub `marker` (`--note_format`). Format `marker` to
niewidoczna definicja referencyjna Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje pogrubiony cytat: czytelny na GitHubie, możliwy do przetworzenia w procesie budowania przez
wtyczkę remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary to rzeczywiste tłumaczenia wykonane za pomocą `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** zlicza pliki, które przepuściły mechanizmy ochronne; **Bez
rozbieżności** te, w których `scripts/compare_structure.py` niczego nie wykrywa — identyczna liczba
sekcji, podtytułów, linków, unikalnych adresów URL, bloków kodu,
kodu inline, wierszy tabeli, bloków cytatów i pogrubionych słów.

„Bez rozbieżności” oznacza „nic nie wykryto”, a nie „identyczny”: komparator
zlicza elementy bez analizowania ich treści. Nie sygnalizuje usuniętego nagłówka
poziomu 4, zastąpionego tekstu w kodzie inline, zamienionej flagi
ani linku wewnętrznego wygenerowanego ze zbędnym nawiasem,
`[texte]((#ancre))`, który już nigdzie nie prowadzi — nie ocenia też
poprawności językowej.

### Gęsty artykuł przeglądowy, tryb `--news`

Wydanie [przeglądu AI z jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione angielskie cytaty. Testy z
4 i 5 września 2026 r.

| Model                                           | Dostęp             | Zapisane | Bez rozbieżności | Mediana/język |
| ----------------------------------------------- | ------------------ | -------- | ---------------- | ------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14    | ✅ **14/14**     | 1 min 18 s    |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | subskrypcja Google | 14/14    | ✅ **14/14**     | 3 min 59 s    |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | subskrypcja Google | 14/14    | ✅ **14/14**     | 3 min 14 s    |
| `gpt-5.6-sol` (`--use_codex`)                   | subskrypcja ChatGPT| 14/14    | ✅ **14/14**     | 11 min 28 s   |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14    | ✅ **14/14**     | 5 min 37 s    |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14    | ✅ **14/14**     | 26 min 23 s   |
| `sonnet` (`--use_claude_code`)                  | subskrypcja Claude | 14/14    | ⚠️ 13/14         | 6 min 49 s    |
| `claude-sonnet-5`                               | API Anthropic      | 14/14    | ⚠️ 11/14         | 6 min 31 s    |
| `haiku` (`--use_claude_code`)                   | subskrypcja Claude | 14/14    | ⚠️ 11/14         | 15 min 54 s   |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14    | ❌ 11/14         | 9 min 27 s    |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14    | ❌ 8/14          | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`                        | lokalnie           | 10/14    | ❌ 7/14          | 12 min 39 s   |
| `mistral-large-latest`                          | API Mistral        | 11/14    | ❌ 5/14          | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14     | ❌ 3/14          | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)                   | subskrypcja Grok   | 1/14     | ❌ 1/14          | 23 min 11 s   |
| `opus` (`--use_claude_code`)                    | subskrypcja Claude | 0/14     | ❌ 0/14          | —             |

Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): 9 języków zapisanych z 14, 8 bez rozbieżności. To ta liczba
widnieje w głównej tabeli. Trzy przerwane testy nie zostały
uwzględnione: `qwen3.5-27b` (9 języków) i `kimi-k2.6` (4) z braku środków,
`z-ai/glm-5.3-flash`, w którym dwa niepowodzenia wynikały z konfiguracji rozumowania,
którą dostawca od tego czasu koryguje. Wiersze OpenRouter zostały zmierzone przy
domyślnych ustawieniach routera, przed `--use_openrouter`; `z-ai/glm-5.2`,
ponownie zmierzony z dostarczonym providerem, zwraca ten sam wynik 14/14. Liczby zostały
przeliczone 10 września przy użyciu obecnego komparatora: `qwen3.8-flash` oraz
`qwen3.7-flash` zyskują po jednym języku w stosunku do pierwszej
publikacji, pozostałe pozostają bez zmian.

Wiersze `--use_antigravity` zostały zmierzone 26 września na tym samym
artykule, przy czterech równoległych tłumaczeniach: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W języku angielskim każdy z nich sam usunął
trzy wiersze francuskiego tłumaczenia pod cytatami, nie wymyślając
flagi, a angielskie cytaty pozostały nienaruszone: zapasowe czyszczenie nie miało
nic do roboty. W `--eco` (`gemini-3.7-flash-low`), tylko na czterech językach
(en, ja, ar, hi): 4 zapisane z 4, wszystkie bez rozbieżności, mediana 1 min 52 s.
Weryfikacja krzyżowa tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 angielskie cytaty), przetłumaczonym poza
blogiem przez `gemini-3.7-flash-medium`: 14 zapisanych z 14, wszystkie bez rozbieżności, od 87 do
128 s na język.

Wiersze `--use_claude_code` zostały zmierzone 26 września na tym samym
artykule, cztery równoległe tłumaczenia, przy nakładzie `low`. W przypadku `sonnet`
angielskie cytaty pozostały nienaruszone we wszystkich czternastu językach, a w języku angielskim
model sam usunął wiersze francuskiego tłumaczenia, nie dodając żadnej
flagi. `opus` nie zapisał żadnego języka: w każdym jego zabezpieczenia
zatrzymały odpowiedź na ostatnim segmencie z powodu notatki o 279 cząsteczkach
wygenerowanych dla miejsca wiązania. Wysłana osobno, notatka ta jest odrzucana
w ramach kategorii „bio”; `sonnet` przetłumaczył ją wszędzie. `haiku` zapisuje
wszystkie czternaście języków; w trzech (en, pl, ro) tytuł sekcji przechodzi z
poziomu 2 na poziom 1. Rozumuje bez możliwości wyłączenia tego — 61%
jego tokenów wyjściowych — stąd ponad dwukrotnie dłuższy czas niż w przypadku `sonnet`.

### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026 r.: 785 wierszy, 285 fragmentów kodu w tekście, 40
domknięć bloków, 89 wierszy tabeli. Cztery tłumaczenia równolegle.

| Model                                           | Zapisane | Bez rozbieżności | Mediana/język | Co się różni                                                             |
| ----------------------------------------------- | -------- | ---------------- | ------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14         | 1 min 43 s    | nic                                                                      |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14         | 1 min 48 s    | nic                                                                      |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14         | 4 min 02 s    | nic według komparatora; podwojone linki wewnętrzne (en)                  |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14         | 36 s          | jedno pogrubione słowo (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14         | 1 min 22 s    | jedno pogrubione słowo (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14         | 2 min 20 s    | wiersz tabeli połączony z poprzednim (ar)                                |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14         | 2 min 56 s    | jeden link (sv), jedno pogrubione słowo (zh)                             |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14         | 6 min 46 s    | jedno pogrubione słowo (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14         | 2 min 34 s    | jedno pogrubione słowo (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14         | 2 min 17 s    | 40 fragmentów kodu w tekście dodanych w arabskim; pogrubienia (hi, ja, ko) |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14          | 2 min 44 s    | utracona sekcja (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh)        |

Dwie przerwane serie nie zostały uwzględnione: Grok, sesja CLI wygasła
po dwunastu językach (jedenaście bez rozbieżności), oraz `qwen3.8-flash`, HTTP 429 od dostawcy
po dwóch. `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie były ponownie mierzone na tej rewizji; w wersji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisał po 9 tłumaczeń na 14, w tym odpowiednio 7
i 1 bez rozbieżności.

Wiersze `--use_antigravity` i `--use_claude_code` nie były mierzone na
zamrożonej rewizji, lecz 26 września na wersji opublikowanej z 1.14.0: 600
wierszy, 257 fragmentów kodu w tekście, 30 domknięć bloków, 85 wierszy tabeli. Krótsza
o 185 wierszy, nie porównuje się bezpośrednio z pozostałymi wierszami;
te konkretne wiersze można jednak porównywać między sobą. W przypadku linków wewnętrznych, których
komparator nie weryfikuje, `gemini-3.8-flash-medium` zachował je nienaruszone we
wszystkich czternastu językach, `gemini-3.7-flash-medium` uszkodził je w języku włoskim;
`sonnet` i `opus` zachowały je nienaruszone wszędzie, a `haiku` podwoił je w
angielskim.

### Cztery pliki README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane wprost z GitHuba — dokumenty
łatwiejsze niż dwa poprzednie. Seria ta skupiała się na modelach
mających trudności; Gemini służy tu jako punkt odniesienia.

| Model                    | Zakres                     | Zapisane | Bez rozbieżności |
| ------------------------ | -------------------------- | -------- | ---------------- |
| `gemini-3.7-flash`        | 4 projekty × 14 języków    | 56/56    | ✅ **55/56**     |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków    | 55/56    | ❌ 47/56         |
| `grok-4.6` (subskrypcja)   | 4 projekty × ar, hi, ja, zh | 16/16    | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16    | ❌ 9/16          |

### Czym te pomiary nie są

- **To nie jest wyczerpujący ranking**: sam OpenRouter oferuje ponad czterysta
  modeli, z czego zmierzono około piętnastu.
- **Czasy są orientacyjne**: od trzech do sześciu równoległych tłumaczeń w zależności
  od serii testów, a przepustowość dostawcy zmienia się w ciągu dnia.
- **Są to obserwacje powiązane z konkretną datą**: modele zmieniają się pod tą samą nazwą, a Państwa
  dokumenty różnią się od naszych.

Aby powtórzyć pomiar na własnych dokumentach, na zamrożonej kopii pliku:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Współpraca

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Oba wiersze są konieczne: bez `pip install -e .`, `python -m aipmt`
odpowiada `No module named aipmt`.

Narzędzia jakościowe, opcjonalne, lecz zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń w repozytorium (README i CHANGELOG, czternaście języków)
regeneruje się za pomocą `./regen_translations.sh --force` — domyślnie Codex i `gpt-5.6-sol` w ramach
subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` oraz
`REGEN_MODEL` zmieniają ścieżkę: `antigravity` pozostaje w ramach subskrypcji, tym razem
Google, i działa bez wyjątku; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1800 s w przypadku Codex i
Antigravity). Szczegółowe informacje o narzędziach znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — osobisty blog publikowany w 15 językach. Jego
  [codzienny przegląd AI](https://jls42.org/fr/news) jest tłumaczony każdego dnia
  za pomocą tego narzędzia i służy jako dokument referencyjny dla powyższych pomiarów.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Zastrzeżenie prawne

Ten program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, zgodnie z warunkami
sekcji 15 i 16 licencji GPL v3: dostarczany jest w stanie „takim, w jakim jest” (as is), bez gwarancji przydatności
handlowej lub przydatności do określonego celu, a jego autor nie ponosi
odpowiedzialności za jakiekolwiek szkody wynikające z jego użytkowania. Pełny tekst
licencji ma pierwszeństwo przed niniejszym podsumowaniem.

- **Przejrzyj tekst przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  fragmenty kodu w tekście, adresy URL, kotwice oraz cytaty w trybie `--news` — nie dotyczą
  nagłówków, tabel, sekcji front matter ani sensu Twoich zdań.
- **Twoje dokumenty są przesyłane do wybranego dostawcy**, zgodnie z jego warunkami
  korzystania z usług i polityką prywatności. Niektóre darmowe modele mogą
  wykorzystywać Twoje konwersacje do trenowania, a warunki Antigravity
  zezwalają firmie Google na ich ponowne wykorzystanie oraz przekazywanie do weryfikacji przez ludzi,
  również w przypadku płatnej subskrypcji; model lokalny to jedyny sposób, który gwarantuje,
  że żadne dane nie opuszczą Twojej maszyny.
- **Wywołania API są płatne.** Ten program nie nakłada limitu
  wydatków: długi dokument, ponawianie prób po błędzie lub model wymagający intensywnego
  wnioskowania wiążą się z wyższymi kosztami.
- **Opublikowane pomiary to obserwacje powiązane z konkretną datą**, a nie gwarancje.

Wymienione nazwy produktów i firm należą do ich odpowiednich właścicieli.
Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z fr na pl za pomocą gemini-3.8-flash-medium.**
