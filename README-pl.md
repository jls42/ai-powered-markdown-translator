# Traducteur de Markdown AI-Powered

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

Tłumaczy pliki Markdown z jednego języka na inny, zachowując strukturę:
bloki kodu, kod w tekście, adresy URL, kotwice, tabele i front matter.
Jedenaście sposobów wywołania modelu — pięć API, cztery subskrypcje bez
rozliczania według zużycia, dwa routery — oraz opublikowany pomiar tego,
co każdy model rzeczywiście zachowuje.

## W skrócie

- **Jedenaście ścieżek dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex), Grok, Google (Antigravity) i Claude (Claude
  Code) bez opłat za zużycie; routery OpenCode (open source, bezpłatny lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Nic nie zostanie uszkodzone przez utracony token**: bloki kodu, kod w tekście,
  adresy URL, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  weryfikowane po powrocie. Jeśli któregoś brakuje, plik nie zostaje zapisany.
- **Długie dokumenty**: segmentacja według okna kontekstowego modelu.
- **Tryb `--news`**: chronione angielskie cytaty i flagi zarządzane według
  języka, z myślą o artykułach z przeglądem informacji.
- **Tryb `--eco`**: szybkie i tańsze modele.
- Opcjonalna **notatka o tłumaczeniu**, na górze, na dole lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 lub nowszy. Aby zainstalować z repozytorium, zobacz
[Współtworzenie](#współtworzenie).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego do najniższego priorytetu;
każde kolejne uzupełnia tylko to, co poprzednie pozostawiło puste.

|     | Gdzie                                         | Do czego                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Zmienne środowiskowe                          | CI, kontenery, jednorazowe nadpisanie |
| 2   | `.env` bieżącego katalogu (lub nadrzędnego) | klucz specyficzny dla projektu        |
| 3   | `~/.config/aipmt/.env`                                 | zainstalowany raz, działa wszędzie    |

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
w systemie Windows. W przypadku braku klucza polecenie wyświetla listę wszystkich trzech lokalizacji.

**Plik `.env` projektu nie może ani przekierowywać wywołań, ani wybierać uruchamianego
programu.** Dostarcza on klucze, nigdy adres docelowy ani plik wykonywalny: wszelkie
zmienne w `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, serwery proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane z ostrzeżeniem. Sklonowane repozytorium nie powinno
mieć możliwości przechwycenia Twojego klucza ani zmuszenia Cię do uruchomienia własnego programu
przy pierwszym tłumaczeniu. Plik ten jest również odczytywany bez interpolacji:
`NOM=${OPENAI_API_KEY}` nie kopiuje w nim klucza. Umieść te zmienne w
środowisku lub w `~/.config/aipmt/.env`.

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

`document.md` przetłumaczony na hiszpański daje `document-es.md` w `--target_dir`;
z `--include_model`, `document-es-gpt-5.6-terra.md`. Rozszerzenie zawsze zmienia
się na `.md` — `article.mdx` daje `article-en.md` — z wyjątkiem użycia
`--keep_filename`, które zachowuje oryginalną nazwę. Istniejące tłumaczenie
jest pomijane, chyba że podano `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli choć jeden plik
zakończył się niepowodzeniem (lista na standardowym wyjściu błędów), `2`, jeśli przyczyną jest konfiguracja.
Plik zakończony niepowodzeniem nigdy nie jest zapisywany, nawet jeśli sam zapis się nie powiedzie:
zawartość jest zapisywana obok, a następnie zmieniana jest jej nazwa. Wystarczy uruchomić ponownie.

## Jaki model wybrać

Zmierzone na dwóch rzeczywistych dokumentach, przetłumaczonych na te same czternaście języków przez
każdy model. **Liczba oznacza liczbę języków (na czternaście), w których
tłumaczenie zostało zapisane i w których nic nie różni się od źródła.**

| Model                | Jak uzyskać dostęp                | Gęsty artykuł przeglądowy | Ten plik README | Co się różni i w ilu językach                                                                                                                                      |
| -------------------- | --------------------------------- | ------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ✅ 14/14        | nic, w żadnym z dwóch dokumentów                                                                                                                                   |
| **Gemini 3.7 Flash** | klucz API Google                  | ✅ 14/14                  | ⚠️ 13/14        | 1 język na 14: o jedno pogrubione słowo więcej (ja)                                                                                                                |
| **Gemini 3.7 Flash** | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ⚠️ 13/14        | 1 język na 14: o jedno pogrubione słowo mniej (ko)                                                                                                                 |
| **GPT-5.6 Sol**      | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14               | ⚠️ 12/14        | 2 języki na 14: o jedno pogrubione słowo mniej (ar, ja)                                                                                                            |
| **GLM-5.2**          | klucz OpenRouter                  | ✅ 14/14                  | ⚠️ 11/14        | 3 języki na 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                                                        |
| Claude Sonnet 5      | subskrypcja Claude (Claude Code)  | ⚠️ 13/14                  | ⚠️ 13/14        | 1 język na 14 w artykule: o jedno pogrubione słowo więcej (zh); 1 w tym pliku README: wiersz tabeli połączony z poprzednim, ukryty podczas renderowania (ar)      |
| Claude Haiku 4.5     | subskrypcja Claude (Claude Code)  | ⚠️ 11/14                  | ✅ 14/14        | 3 języki w artykule: nagłówek sekcji zmieniony na poziom 1 (en, pl, ro); w tym pliku README: brak różnic dla porównywarki, ale linki wewnętrzne powielone po angielsku |
| Claude Sonnet 5      | klucz API Anthropic               | ⚠️ 11/14                  | ⚠️ 12/14        | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym pliku README: link pozbawiony formatowania (sv), pogrubione słowo (zh)                           |
| Qwen 3.7 Flash       | klucz OpenRouter                  | ❌ 8/14                   | ⚠️ 10/14        | 1 język odrzucony w artykule, 5 innych odbiega od normy; w tym pliku README: około czterdziestu słów umieszczonych w `code` (ar)                          |
| Grok 4.6             | subskrypcja Grok                  | ❌ 8/14                   | nieoceniany     | 5 języków odrzuconych na 14 z powodu brakujących kodów w tekście i adresów URL; niderlandzki odbiega we wszystkim                                                 |
| GPT-OSS 20B          | model lokalny (Ollama)            | ❌ 7/14                   | nie mierzono ponownie | 4 języki odrzucone na 14: model pozostawił fragmenty po francusku, strażnik je zatrzymał                                                                     |
| MiMo v2.5 (darmowy)  | OpenCode Zen, bez konta           | ❌ 11/14                  | nie mierzono ponownie | 1 język odrzucony; utracona sekcja w języku polskim                                                                                                                |
| Mistral Large        | klucz API Mistral                 | ❌ 5/14                   | ❌ 1/14         | **cała sekcja znika**: 1 język w artykule (hi), 3 w tym pliku README (ar, hi, ko) — oraz 3 języki odrzucone w artykule                                             |
| DeepSeek V4 Flash    | klucz OpenRouter                  | ❌ 3/14                   | nie mierzono ponownie | 10 języków odrzuconych na 14; 37 minut na język                                                                                                                   |
| Claude Opus 5.5      | subskrypcja Claude (Claude Code)  | ❌ 0/14                   | ✅ 14/14        | artykuł odrzucony we wszystkich 14 językach przez zabezpieczenia Opusa z powodu krótkiej wzmianki o biologii; brak różnic w tym pliku README                        |

|     | Co oznacza symbol                                                                                                                                                                                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | wszystkie czternaście języków przetłumaczonych i nic nie różni się od źródła                                                                                                                          |
| ⚠️  | wszystkie czternaście języków przetłumaczonych; to, co się różni, to **formatowanie** — pogrubione słowo, `code`, link, który traci nawiasy kwadratowe. Nie brakuje żadnego tekstu, adresu URL, bloku kodu ani sekcji |
| ❌  | co najmniej jednego języka nie udało się przetłumaczyć — plik został odrzucony, niezapisany — **lub** w zapisanym pliku brakuje treści                                                               |

Najważniejsze wnioski:

- **Odrzucone tłumaczenie to nie uszkodzone tłumaczenie.** Kiedy po powrocie
  brakuje tokenu, plik nie jest zapisywany, a język liczy się jako
  odrzucony. To właśnie przydarzyło się Grokowi w artykule: cztery fragmenty kodu w tekście i
  trzy adresy URL utracone już w pierwszym segmencie, we wszystkich pięciu alfabetach nielacińskich.
- **Model może odrzucić cały dokument z powodu jednego zdania.** Opus 5.5
  tłumaczy ten plik README bez żadnych odchyleń, ale ani jednego artykułu przeglądowego: jego
  filtry bezpieczeństwa blokują odpowiedź przy krótkiej wzmiance o biologii. Plik nie zostaje
  zapisany, a aipmt wyjaśnia dlaczego.
- **Ta siatka bezpieczeństwa nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik, który narzędzie zapisuje
  bez wahania — tak jest w przypadku Mistrala. Elementów tych nie da się
  zastąpić tokenem, a obecne zabezpieczenia ich nie kontrolują;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego pliku README**: jego sesja CLI wygasła po dwunastu
  językach, z czego jedenaście było bezbłędnych. Przerwany proces nie podlega ocenie.
- **Gęstość dokumentu ma większe znaczenie niż język.** Grok radzi sobie na
  zwykłych plikach README, a gubi się przy artykule gęstym od linków, w tym w
  języku niderlandzkim.

Daty i dokumenty: kolumna „Ten plik README” została zmierzona 9 września 2026 r.
na zamrożonej wersji tego pliku (785 wierszy, 285 kodów w tekście, 89 wierszy
tabeli), modyfikowanej od tego czasu — z wyjątkiem wierszy Antigravity i Claude Code,
zmierzonych 26 września na krótszej wersji opublikowanej z wydaniem 1.14.0
(600 wierszy, 257 kodów w tekście, 85 wierszy tabeli). Kolumna „Gęsty artykuł
przeglądowy” pochodzi z testów przeprowadzonych 4 i 5 września na artykule o długości 589
wierszy, z wyjątkiem wiersza Grok, zmierzonego ponownie 9 września na innym wydaniu tego
samego przeglądu, oraz wierszy Antigravity i Claude Code, zmierzonych 26 września
na tym samym artykule. Pełne tabele, czasy trwania i protokół znajdują się w sekcji
[Szczegółowe pomiary](#szczegółowe-pomiary).

## Wszystkie opcje

| Opcja                    | Opis                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Pojedynczy plik Markdown do przetłumaczenia (alternatywa dla `--source_dir`)                                 |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown (domyślnie: `content/posts`)                                       |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików (domyślnie: `traductions_en`)                                     |
| `--source_lang`           | Język źródłowy (domyślnie: `fr`)                                                                    |
| `--target_lang`           | Język docelowy (domyślnie: `en`)                                                                    |
| `--model`           | Konkretny model do użycia                                                                                     |
| `--eco`           | Użyj modeli ekonomicznych                                                                                     |
| `--use_mistral`           | Użyj API Mistral AI                                                                                           |
| `--use_claude`           | Użyj API Claude                                                                                               |
| `--use_gemini`           | Użyj API Gemini                                                                                               |
| `--use_grok`           | Użyj API xAI (Grok) — wymaga `XAI_API_KEY`                                                                   |
| `--use_codex`           | Użyj CLI Codex w ramach limitu subskrypcji ChatGPT                                                            |
| `--use_grok_cli`           | Użyj CLI Grok w ramach limitu subskrypcji Grok                                                                |
| `--use_antigravity`           | Użyj CLI Antigravity (`agy`) w ramach limitu subskrypcji Google AI Pro lub Ultra                     |
| `--use_claude_code`           | Użyj CLI Claude Code (`claude -p`) w ramach limitu subskrypcji Claude Pro lub Max                          |
| `--use_opencode`           | Użyj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle`                      |
| `--use_openrouter`           | Użyj OpenRouter — wymaga `OPENROUTER_API_KEY` i `--model fournisseur/modèle`                                                      |
| `--force`           | Wymuś ponowne tłumaczenie                                                                                     |
| `--keep_filename`           | Zachowaj oryginalną nazwę pliku                                                                               |
| `--news`           | Tryb wiadomości: chroni cytaty EN, obsługuje flagi według języka                                              |
| `--add_translation_note`           | Dodaj notatkę o tłumaczeniu                                                                                   |
| `--note_position`           | Pozycja notatki: `top`, `bottom` (domyślnie) lub `both`                                |
| `--note_format`           | Format notatki: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                            |
| `--include_model`          | Dołącz nazwę modelu do pliku wyjściowego                                                                      |
| `--reasoning_effort`          | Nakład pracy na wnioskowanie GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

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

`--eco` przełącza na poziom ekonomiczny każdego dostawcy.

| Dostawca    | Jakość (domyślnie)                                    | Ekonomiczny (`--eco`)     |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                   |
| Codex       | `gpt-5.6-sol` (także `terra` i `luna` przez `--model`) | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| Claude Code | `sonnet`, nakład pracy `low`         | to samo — `--eco` bez wpływu |
| OpenCode    | wymagane `--model provider/modèle`                              | to samo — `--eco` bez wpływu |
| OpenRouter  | wymagane `--model fournisseur/modèle`                              | to samo — `--eco` bez wpływu |

### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest odliczane z limitu
subskrypcji ChatGPT, bez klucza API i opłat za użycie.

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
  250–2000 wiadomości/5 godz. dla `gpt-5.6-luna` (`--eco`) oraz
  10–100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-terra` i `--model gpt-5.6-luna` również przechodzą przez
  subskrypcję. Model, do którego konto nie ma uprawnień, zwraca błąd 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Wolniejsze niż API, a różnica rośnie wraz z rozmiarem dokumentu: w przypadku tego README
  mediana wynosi 6 min 46 s na język przy użyciu `gpt-5.6-sol`, w porównaniu z 36 s dla
  `gemini-3.7-flash`.
- Odrzucane w środowisku CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): subskrypcja uwierzytelnia się
  za pomocą osobistego pliku sesji, który nie powinien znajdować się na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada dotyczy oficjalnego CLI Grok Build w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w przypadku Codexa.** Piaskownica systemu operacyjnego Grok nie działa
  na wielu nowszych maszynach z systemem Linux (AppArmor, gniazda środowiska uruchomieniowego
  kontenerów), a profil, którego nie można zastosować, uruchamia się po cichu bez izolacji.
  Dlatego skrypt domyślnie nie żąda żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` interfejsu CLI, w tym uniwersalnej regule `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast po cichu wyłączać ochronę.
  `GROK_TRANSLATE_SANDBOX=read-only` wymaga piaskownicy systemu operacyjnego, a uruchomienie
  kończy się niepowodzeniem, jeśli maszyna nie może jej obsłużyć.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, i żadne
  polecenie nie pozwala go sprawdzić: przetwarzanie wsadowe może bez ostrzeżenia
  uszczuplić limit na rozmowy.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach subskrypcji Google: `--use_antigravity`

Ta sama zasada dotyczy `agy`, oficjalnego CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie jest odliczane z limitu subskrypcji zamiast
naliczania opłat za tokeny. To jedyna droga do tego limitu: Gemini CLI nie
obsługuje już tych kont od 18 czerwca 2026 r.
([ogłoszenie](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
a SDK Antigravity akceptuje tylko klucz API lub projekt Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Żadna płatna ścieżka nie pozostaje otwarta.** agy otrzymuje ze środowiska
  użytkownika jedynie zamkniętą listę zmiennych — `PATH`, język i strefę czasową,
  terminal, tożsamość, serwery proxy i certyfikaty, magistralę sesji — oraz żadnych kluczy:
  kilka jego zmiennych potrafi po cichu przekierować wywołanie (potwierdzone pomiarami:
  jedna wysyła dokument do bramki podmiotu trzeciego, inna do płatnego projektu
  Google Cloud), a czarna lista pomijała kolejne przy każdym przeglądzie.
  Przed każdym segmentem polecenie `agy -p /config`, które nie zużywa limitu, musi wykazać
  wyłączone płatne kredyty AI, brak klucza API i brak projektu Google Cloud — brakujące
  ustawienie oznacza odmowę —, w przeciwnym razie nic nie zostanie przetłumaczone; log każdego
  wywołania musi następnie poświadczyć subskrypcję (`authMethod=consumer`), inaczej
  odpowiedź zostanie odrzucona.
- **Izolacja.** Każde wywołanie działa w prywatnym, tymczasowym katalogu domowym
  z agentem tłumaczącym pozbawionym narzędzi: Twoje ustawienia, reguły,
  wtyczki, serwery MCP i hooki agy nie mają tam dostępu, nic nie jest dodawane do Twojej
  historii, a dane logowania pozostają w pęku kluczy, którego aipmt nigdy nie czyta.
  Brak agenta powoduje, że agy po cichu powraca do swojego agenta kodowania
  i jego narzędzi: cały wiersz logu musi potwierdzać właściwego agenta — cytowanie
  tego komunikatu w dokumencie go nie zastępuje —, w przeciwnym razie następuje odmowa.
- **Platformy**: Linux w sesji posiadającej pęk kluczy (magistrala sesji
  D-Bus, Secret Service); macOS jest akceptowany, choć nie był testowany pomiarami. Odrzucane
  w systemie Windows, gdzie agy nie odczytuje zmiennych izolujących każde wywołanie, oraz
  w systemie Linux bez magistrali sesji — sesja SSH, kontener, serwer: agy przechowuje
  w nich swój token w pliku w `~/.gemini`, który izolacja ukrywa.
  Odmowa następuje przed jakimkolwiek uruchomieniem, wraz z podaniem przyczyny, zamiast
  minutowego oczekiwania na kod logowania.
- **Modele**: te z `agy models`. Modele Gemini mają nakład pracy zawarty w nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez sufiksu jest odrzucana przed wywołaniem,
  a `--reasoning_effort` nie przynosi żadnego efektu. Domyślnie `gemini-3.8-flash-medium`,
  a `gemini-3.7-flash-low` w `--eco`; serie testowe, które je ustaliły,
  opisano w sekcji [Szczegółowe pomiary](#szczegółowe-pomiary). Claude i GPT-OSS
  mają własny, znacznie mniejszy limit: około 1% 5-godzinnego okna
  na zmierzone wywołanie, w porównaniu z 0,05% dla Flash.
- **Limit**: według grup, okno 5-godzinne oraz tygodniowe,
  proporcjonalnie do kosztu w tokenach. Zmierzone na koncie autora: około
  16 punktów z 5-godzinnego okna na milion znaków źródłowych w
  `gemini-3.8-flash-medium`, 14 w `gemini-3.7-flash-medium` oraz od 7 do 8 przy
  niskim nakładzie pracy — README o długości 40 000 znaków kosztuje więc nieco ponad
  pół punktu. Tygodniowy limit zależy natomiast od poziomu subskrypcji. Ponawianie prób
  odbywa się zgodnie z tym, co agy oznacza jako możliwe do ponowienia; w przeciwnym razie
  wyczerpane okno nigdy nie jest ponawiane: powoduje błąd każdego pliku aż do resetu,
  który wyświetla `/usage`.
- **Wolniejsze niż API**: w przypadku gęstego artykułu z pomiarami mediana wynosi 3 min 59 s na
  język w `gemini-3.8-flash-medium` i 3 min 14 s w
  `gemini-3.7-flash-medium`, w porównaniu z 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerwanie**: Ctrl-C lub zamknięcie terminala zatrzymuje agy wraz z
  poleceniem, zamiast pozwalać mu dokończyć działanie na Twoim limicie; to samo
  dotyczy Codexa, Grok CLI i OpenCode. Pod kontrolą `nohup` tłumaczenie jest kontynuowane.
- Odrzucane w środowisku CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): sesja logowania znajduje się
  w osobistym pęku kluczy. Na runnerze należy użyć `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, a następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment, łącznie z uruchomieniem, domyślnie 900).

**Warunki korzystania: ponosisz odpowiedzialność własnym kontem.** [Warunki
korzystania z usługi Antigravity](https://antigravity.google/terms) (sekcja 6) oraz jej
[FAQ](https://antigravity.google/docs/faq/) zabraniają uzyskiwania dostępu do usługi
za pośrednictwem oprogramowania innych firm przy użyciu danych logowania Antigravity — Claude Code,
OpenClaw i OpenCode są tam wymienione — pod rygorem zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokena: uruchamia oficjalny plik binarny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
dokumentuje dla skryptów i środowisk CI. Przedstawiciel Google uznał uruchamianie `agy -p`
z poziomu lokalnego skryptu do własnej pracy za „standardowe”
([oficjalne forum, 25 września 2026 r., odpowiedź niewiążąca](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden dokument nie rozstrzyga jednoznacznie przypadku narzędzia dystrybuowanego takiego jak to.

**Tylko dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków,
interakcje — prompty, odpowiedzi, metadane — mogą być wykorzystywane do ulepszania
produktów oraz uczenia maszynowego Google i mogą być weryfikowane przez
ludzi, dotyczy to również płatnej subskrypcji. Rezygnacja wymaga ustawienia
`enableTelemetry`, o nieudokumentowanym działaniu, którego aipmt nie konfiguruje; Twoje ustawienia
agy nie są przenoszone do środowiska izolowanego. Nie przesyłaj tą drogą niczego poufnego.

### W ramach subskrypcji Claude: `--use_claude_code`

Ta sama zasada dotyczy `claude`, oficjalnego CLI Claude Code, w trybie `-p`: dla
osób opłacających Claude Pro lub Max tłumaczenie jest odliczane z limitu
subskrypcji zamiast rozliczania za tokeny. Nie należy mylić z
`--use_claude`, API firmy Anthropic, rozliczanym według użycia.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Żadna płatna ścieżka nie pozostaje otwarta, a każde wywołanie to potwierdza.** Claude
  Code otrzymuje z Twojego środowiska wyłącznie zamkniętą listę zmiennych — ani
  klucza API, ani tokena, ani dostawcy chmury, ani znacznika sesji Claude Code,
  z której aipmt zostałby uruchomiony. Przed pierwszym segmentem `claude auth status` musi
  wykazać połączenie subskrypcyjne bez klucza Console, a `/usage`, które nie zużywa
  żadnego limitu, musi to poświadczyć; każde wywołanie poświadcza to ze swojej strony
  w zdarzeniu inicjalizacji, w przeciwnym razie odpowiedź zostaje odrzucona.
- **Wyłącz „extra usage”** (claude.ai, Ustawienia → Użycie), aby
  zachować zerowy koszt: gdy ta opcja jest aktywna, przejmuje działanie po wyczerpaniu okna i
  nalicza opłaty bez wyświetlania błędu. aipmt zatrzymuje tłumaczenie, gdy tylko odczyt
  limitu wywołania to zasygnalizuje, ale to konkretne wywołanie jest już policzone.
- **Limit współdzielony z Twoimi sesjami Claude Code.** Każde wywołanie raportuje
  wykorzystanie okien 5-godzinnych oraz tygodniowych; powyżej 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) żaden kolejny segment nie jest uruchamiany, aby
  nie wyczerpać puli potrzebnej do Twojej pracy.
- **Izolacja.** Każde wywołanie działa bez narzędzi, w prywatnym,
  tymczasowym katalogu, w trybie bez personalizacji: ani Twoje `CLAUDE.md`, ani wtyczki,
  hooki, serwery MCP czy ustawienia nie są ładowane, a z sesji nic nie jest
  zachowywane. Załączniki są wyłączone: `@chemin` w Twoim dokumencie
  pozostaje tekstem i nie otwiera żadnego pliku (zmierzone).
- **Modele**: domyślnie `sonnet`, z nakładem `low`, oraz w `--eco` również:
  `--eco` niczego nie zmienia na tej ścieżce. Zmierzone na tych samych dokumentach: `haiku`
  jest dwa razy wolniejszy — rozumuje bez możliwości wyłączenia tego — przy
  niewiele niższym koszcie, a `opus` odrzuca treści biologiczne (kolejny
  punkt). Oba pozostają dostępne przez `--model`; te aliasy podążają za
  najnowszym modelem ze swojej rodziny. `fable` oraz warianty `[1m]` są odrzucane,
  ponieważ korzystają z płatnych środków. `--reasoning_effort` reguluje nakład pracy,
  z którego tłumaczenie nic nie zyskuje: zmierzone rozumowanie jest zerowe lub niemal zerowe.
- **Opus odrzuca niektóre treści biologiczne.** Jego zabezpieczenia są bardziej
  rygorystyczne niż w przypadku Sonnet, a komunikat o błędzie firmy Anthropic ostrzega, że
  „can sometimes flag biology-research-adjacent work”. Zmierzone: krótka notka
  prasowa o 279 wygenerowanych cząsteczkach spowodowała odrzucenie artykułu we wszystkich czternastu
  językach. Nic nie zostaje zapisane: aipmt odrzuca uciętą odpowiedź, wskazuje
  zabezpieczenia i sugeruje `--model sonnet`.
- Odrzucane w środowisku CI (zdefiniowane `CI` lub `GITHUB_ACTIONS`) oraz pod systemem Windows (niezmierzone).
- Zmienne: `AIPMT_CLAUDE_BIN` (w przeciwnym razie `PATH`, a następnie `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekundy na segment, domyślnie 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (domyślnie 0.8), `CLAUDE_CONFIG_DIR` (konto
  Claude Code, nigdy niepobierane z projektowego `.env`); katalogi robocze w
  `XDG_CACHE_HOME/aipmt/claude-code` (domyślnie `~/.cache`).

**Warunki korzystania: to Twoje konto ponosi odpowiedzialność.** [Strona
prawna Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nie zabrania „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription”: tak właśnie działa aipmt, który uruchamia
oficjalny plik binarny i nigdy nie odczytuje tokena. Jednak Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users”, preferuje klucz API dla narzędzi
zewnętrznych, „including open-source projects”, i zastrzega sobie prawo do rozliczania ich
użycia z płatnych środków
([pomoc Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Żaden zapis nie rozstrzyga jednoznacznie przypadku dystrybuowanego narzędzia uruchamiającego plik binarny.

**Dane**: na kontach Free, Pro i Max trenowanie modeli
obejmuje również Claude Code, jeśli zezwalają na to ustawienia prywatności
([strona dotycząca danych](https://code.claude.com/docs/en/data-usage)). aipmt nie przechowuje
żadnej lokalnej transkrypcji (`--no-session-persistence`). Nie przesyłaj
tą drogą żadnych poufnych informacji.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to otwartoźródłowy agent programistyczny (MIT), który
kieruje zapytania do skonfigurowanych w nim dostawców: klucza API, subskrypcji,
bramki OpenCode Zen (darmowe modele, bez konta) lub modelu lokalnego. Dwie
ścieżki zostały tutaj w pełni zmierzone: Zen i Ollama.

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

`--model` jest wymagany: bez niego OpenCode wybrałby domyślnie darmowy model,
którego konwersacje mogą być wykorzystywane do trenowania, a taki wybór nie powinien być dokonywany
za Ciebie.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, nadrzędna wobec Twojej, definiuje agenta `aipmt`,
  dla którego wszystkie narzędzia są odrzucone (`permission: { "*": "deny" }`), udostępnianie
  sesji wyłączone, `--pure`, nigdy `--auto`;
- tymczasowy i pusty katalog roboczy, z utworzonymi `OPENCODE_DISABLE_PROJECT_CONFIG` oraz
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstrzykuje do
  promptu zawartość `AGENTS.md` z bieżącego katalogu oraz `~/.claude/CLAUDE.md`.
  Globalny `~/.config/opencode/AGENTS.md` pozostaje wstrzyknięty, OpenCode nie pozwala
  go pominąć;
- warunki wyjścia: kod wyjścia 0, brak zdarzenia `error`, brak wywołania
  narzędzi, ostatni krok w `stop`, niepusty tekst oraz rzeczywiście
  załadowany agent `aipmt` — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  dyskretnie powraca do domyślnego agenta programistycznego;
- żaden klucz `aipmt` nie jest przekazywany, z wyjątkiem `OPENCODE_API_KEY`, klucza
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  pliku `.env` narzędzia `aipmt`.

Warto wiedzieć:

- Darmowe modele w Zen są zmienne, mają nieudokumentowane limity, a
  generowane zapytania mogą służyć do trenowania: nadają się do publicznej
  dokumentacji, nie do prywatnych treści.
- Model lokalny musi oferować co najmniej 16k tokenów kontekstu, ponieważ segmenty
  mają do 16 000 znaków. Ollama często ustawia domyślnie 4 096: należy użyć
  pliku `Modelfile` z parametrem `PARAMETER num_ctx 32768`.
- `--eco` nie przynosi żadnego efektu; `--reasoning_effort` jest przekazywany bez zmian jako
  `--variant` w OpenCode.
- OpenCode rejestruje każdą sesję w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, a następnie `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekundy na segment, domyślnie 600). `OPENCODE_CONFIG`
  jest przekazywane bez zmian do OpenCode.

Przykład lokalnego modelu przez Ollama w pliku `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` wyłącza rozumowanie, które Ollama domyślnie aktywuje na tych
modelach i którego nie da się wyłączyć w pliku Modelfile. Zmierzone na zdaniu liczącym
sześć słów: 919 tokenów rozumowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według zużycia, w oparciu o jedno wspólne doładowanie, dający dostęp do
modeli hostowanych przez podmioty trzecie — w tym otwartych modeli chińskich, których żaden
inny provider tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest wymagany. Preflight, wykonywany przed jakimkolwiek naliczeniem opłat, obsługuje
dwie specyficzne cechy routingu:

- **Ten sam model jest obsługiwany przez dziesiątki hostów o różnych limitach** —
  w przypadku `z-ai/glm-5.3-flash` to 23 hostów, w tym jeden z limitem zaledwie
  2 048 tokenów wyjściowych. Preflight odczytuje `/api/v1/models/{modèle}/endpoints`,
  odrzuca hosty z limitem poniżej 8 000 tokenów wyjściowych lub o obniżonym statusie, a
  pozostałe przypina za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki wyjściowej** — 107 tokenów w porównaniu do 2 przy
  odpowiedzi „OK” z `z-ai/glm-5.2`. Domyślnie jest wyłączone; modele,
  które go wymagają, otrzymują najniższy możliwy nakład pracy, jaki akceptują, ponieważ domyślna wartość
  w katalogu mogłaby nasycić wyjście przed zakończeniem tłumaczenia.
  `--reasoning_effort` ma nadal priorytet.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model z oknem poniżej 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8 400 na prompt i segment, minimum 8 000
  na wyjściu.
- Brak sluga w katalogu, brak dostępu do katalogu lub brak
  hosta spełniającego limit przerywa wykonanie polecenia.
- `finish_reason=length` z pustym wyjściem oznacza budżet skonsumowany przez
  rozumowanie, a nie obcięcie: komunikat wyraźnie to rozróżnia.
- `--eco` nie przynosi żadnego efektu.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagany `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Notatka o tłumaczeniu

`--add_translation_note` dodaje notatkę w formacie `bottom` (domyślnie), `top` (po
front matterze) lub `both` (`--note_position`), w formacie `legacy` (akapit
wytłuszczony, domyślnie) lub `marker` (`--note_format`). Format `marker` to
niewidoczna definicja referencji Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje wytłuszczony cytat: czytelna na GitHubie, możliwa do przetworzenia podczas budowania przez
wtyczkę remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary to rzeczywiste tłumaczenia wykonane za pomocą `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** zlicza pliki, które przeszły przez mechanizmy ochronne; **Bez
rozbieżności** te, w których `scripts/compare_structure.py` niczego nie wykrywa — identyczna liczba
sekcji, podtytułów, linków, unikalnych adresów URL, bloków kodu,
kodu inline, wierszy tabeli, bloków cytatów i pogrubionych słów.

„Bez rozbieżności” oznacza „nic nie wykryto”, a nie „identyczny”: moduł porównujący
zlicza elementy bez analizy ich treści. Nie sygnalizuje usuniętego nagłówka
poziomu 4, zastąpionego tekstu w kodzie inline, zamienionej flagi
ani linku wewnętrznego z dodanym zbędnym nawiasem,
`[texte]((#ancre))`, który przestaje dokądkolwiek prowadzić — nie ocenia też
samego języka.

### Gęsty artykuł przeglądowy, tryb `--news`

Wydanie z [przeglądu AI na jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty w języku angielskim. Pomiary
z 4 i 5 września 2026 r.

| Model                                          | Dostęp             | Zapisane | Bez rozbieżności | Mediana/język |
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
(356 wierszy): 9 zapisanych języków na 14, 8 bez rozbieżności. To właśnie ta wartość
widnieje w głównej tabeli. Trzy przerwane serie pomiarowe nie zostały
uwzględnione: `qwen3.5-27b` (9 języków) oraz `kimi-k2.6` (4) z powodu braku środków,
oraz `z-ai/glm-5.3-flash`, w którym dwie porażki wynikały z ustawienia rozumowania,
które dostawca od tego czasu poprawił. Wiersze OpenRouter były mierzone przy
domyślnych ustawieniach routera, przed `--use_openrouter`; model `z-ai/glm-5.2`,
zmierzony ponownie z dostarczonym dostawcą, osiąga ten sam wynik 14/14. Wartości zostały
przeliczone 10 września przy użyciu bieżącego modułu porównującego: `qwen3.8-flash` oraz
`qwen3.7-flash` zyskują po jednym języku w stosunku do pierwszej
publikacji, pozostałe pozostały bez zmian.

Wiersze `--use_antigravity` zostały zmierzone 26 września na tym samym
artykule, w czterech równoległych tłumaczeniach: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W języku angielskim każdy model sam usunął
trzy linijki francuskiego tłumaczenia pod cytatami, nie wymyślając żadnej
flagi, a angielskie cytaty pozostały nienaruszone: mechanizm czyszczenia rezerwowego nie
musiał nic robić. W `--eco` (`gemini-3.7-flash-low`), na zaledwie czterech językach
(en, ja, ar, hi): 4 zapisane na 4, wszystkie bez rozbieżności, mediana 1 min 52 s.
Sprawdzian krzyżowy tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 angielskie cytaty), przetłumaczonym poza
blogiem przez `gemini-3.7-flash-medium`: 14 zapisanych na 14, wszystkie bez rozbieżności, od 87 do
128 s na język.

Wiersze `--use_claude_code` zostały zmierzone 26 września na tym samym
artykule, w czterech równoległych tłumaczeniach, przy nakładzie pracy `low`. Z `sonnet`
angielskie cytaty pozostały nienaruszone we wszystkich czternastu językach, a w języku angielskim
model sam usunął linijki francuskiego tłumaczenia, nie wymyślając żadnej
flagi. `opus` nie zapisał żadnego języka: w każdym z nich zabezpieczenia
zatrzymały odpowiedź na ostatnim segmencie z powodu krótkiej notki o 279 cząsteczkach
wygenerowanych dla miejsca wiązania. Wysłana osobno, notka ta zostaje odrzucona ze
względu na kategorię „bio”; model `sonnet` przetłumaczył ją wszędzie. `haiku` zapisuje
wszystkie czternaście języków; w trzech (en, pl, ro) tytuł sekcji przeszedł z
poziomu 2 na poziom 1. Model rozumuje bez możliwości wyłączenia tego — 61%
jego tokenów wyjściowych —, co przekłada się na ponad dwukrotnie dłuższy czas w porównaniu z `sonnet`.

### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026 r.: 785 wierszy, 285 fragmentów kodu w tekście, 40
domknięć bloków, 89 wierszy tabeli. Cztery tłumaczenia równolegle.

| Model                                           | Zapisane | Bez rozbieżności | Mediana/język | Co się różni                                                             |
| ----------------------------------------------- | -------- | ---------------- | ------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14         | 1 min 43 s    | nic                                                                      |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14         | 1 min 48 s    | nic                                                                      |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14         | 4 min 02 s    | nic dla narzędzia porównującego; zduplikowane linki wewnętrzne (en)      |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14         | 36 s          | jedno słowo pogrubione (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14         | 1 min 22 s    | jedno słowo pogrubione (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14         | 2 min 20 s    | jeden wiersz tabeli połączony z poprzednim (ar)                          |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14         | 2 min 56 s    | jeden link (sv), jedno słowo pogrubione (zh)                             |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14         | 6 min 46 s    | jedno słowo pogrubione (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14         | 2 min 34 s    | jedno słowo pogrubione (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14         | 2 min 17 s    | 40 fragmentów kodu w tekście dodanych w arabskim; pogrubienie (hi, ja, ko) |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14          | 2 min 44 s    | utracona sekcja (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh)        |

Dwie przerwane serie nie zostały uwzględnione: Grok, wygaśnięcie sesji CLI
po dwunastu językach (jedenaście bez rozbieżności), oraz `qwen3.8-flash`, HTTP 429 od
dostawcy hostingu po dwóch. `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie były ponownie mierzone na tej wersji; w wersji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisał 9 z 14 tłumaczeń, w tym odpowiednio 7
i 1 bez rozbieżności.

Wiersze `--use_antigravity` i `--use_claude_code` nie były mierzone na
wersji zamrożonej, lecz 26 września na wersji opublikowanej wraz z 1.14.0: 600
wierszy, 257 fragmentów kodu w tekście, 30 domknięć bloków, 85 wierszy tabeli. Jako że
jest krótsza o 185 wierszy, nie można jej bezpośrednio porównywać z pozostałymi wierszami;
te konkretne wiersze można jednak porównywać między sobą. W przypadku linków wewnętrznych,
których narzędzie porównujące nie weryfikuje, `gemini-3.8-flash-medium` zachował je w stanie
nienaruszonym we wszystkich czternastu językach, `gemini-3.7-flash-medium` uszkodził je we włoskim;
`sonnet` i `opus` zachowały je nienaruszone wszędzie, a `haiku` zduplikował je w
angielskim.

### Cztery pliki README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane wprost z GitHuba — dokumenty
prostsze niż dwa poprzednie. Seria ta skupiała się na modelach mających
trudności; Gemini służy w niej jako punkt odniesienia.

| Model                     | Zakres                     | Zapisane | Bez rozbieżności |
| ------------------------- | -------------------------- | -------- | ---------------- |
| `gemini-3.7-flash`        | 4 projekty × 14 języków    | 56/56    | ✅ **55/56**     |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków    | 55/56    | ❌ 47/56         |
| `grok-4.6` (subskrypcja) | 4 projekty × ar, hi, ja, zh | 16/16    | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16    | ❌ 9/16          |

### Czym te pomiary nie są

- **To nie jest wyczerpujący ranking**: sam OpenRouter oferuje ponad czterysta
  modeli, z czego przetestowano około piętnastu.
- **Czas trwania ma charakter orientacyjny**: od trzech do sześciu tłumaczeń równolegle w
  zależności od serii, a przepustowość dostawcy zmienia się w ciągu dnia.
- **Obserwacje są przypisane do konkretnego momentu**: modele zmieniają się pod tą samą nazwą,
  a Twoje dokumenty różnią się od naszych.

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

Oba wiersze są niezbędne: bez `pip install -e .` polecenie `python -m aipmt`
zwraca `No module named aipmt`.

Narzędzia jakościowe, opcjonalne, ale zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń w repozytorium (README i CHANGELOG, czternaście języków) można
wygenerować ponownie za pomocą `./regen_translations.sh --force` — domyślnie Codex i `gpt-5.6-sol` w ramach
subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` oraz
`REGEN_MODEL` zmieniają ścieżkę: `antigravity` pozostaje w ramach subskrypcji, tym razem
Google, i przechodzi bez odstępstw; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) zostanie odrzucone bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ustala limit czasu dla każdego zadania (600 s, 1800 s dla Codex i
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

Niniejszy program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, na warunkach
określonych w sekcjach 15 i 16 licencji GPL v3: dostarczany „w stanie, w jakim się znajduje” (as is), bez gwarancji
przydatności handlowej ani przydatności do określonego celu, a jego autor nie może
zostać pociągnięty do odpowiedzialności za jakiekolwiek szkody wynikające z jego użytkowania. Tekst
licencji ma pierwszeństwo przed niniejszym podsumowaniem.

- **Przejrzyj tekst przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod w tekście, adresy URL, kotwice oraz cytaty w trybie `--news` — nie obejmują
  nagłówków, tabel, front matter ani sensu Twoich zdań.
- **Twoje dokumenty trafiają do wybranego dostawcy**, na warunkach
  jego regulaminu świadczenia usług i polityki przetwarzania danych. Niektóre darmowe modele mogą
  wykorzystywać Twoje zapytania do trenowania, a warunki Antigravity
  pozwalają firmie Google na ich ponowne użycie oraz weryfikację przez ludzi,
  w tym w ramach płatnej subskrypcji; model lokalny jest jedynym rozwiązaniem, które nie powoduje
  przesłania jakichkolwiek danych poza Twoją maszynę.
- **Zapytania API są płatne.** Ten program nie nakłada limitu na
  wydatki: długi dokument, ponowienie próby po błędzie lub model intensywnie
  rozumujący generują wyższe koszty.
- **Opublikowane pomiary są obserwacjami przypisanymi do konkretnego momentu**, a nie gwarancjami.

Wymienione nazwy produktów i firm należą do ich odpowiednich właścicieli.
Niniejszy projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z fr na pl za pomocą gemini-3.8-flash-medium.**
