# Tłumacz Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena utrzymywalności"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie kodu"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Luki w zabezpieczeniach"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Zduplikowane linie (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linie kodu"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Odznaka Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumaczy pliki Markdown z jednego języka na inny, zachowując
strukturę: bloki kodu, kod w tekście, adresy URL, kotwice, tabele i front
matter. Dziesięć sposobów wywołania modelu — pięć API, trzy subskrypcje bez
rozliczania według zużycia, dwa routery — oraz opublikowany pomiar tego, co każdy
model rzeczywiście zachowuje.

## W skrócie

- **Dziesięć ścieżek dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex), Grok i Google (Antigravity) bez rozliczania według
  zużycia; routery OpenCode (open source, darmowy lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Żadnych błędów z powodu utraconego tokena**: bloki kodu, kod w tekście,
  adresy URL, kotwice i cytaty są zastępowane tokenami przed wywołaniem i
  weryfikowane po powrocie. Jeśli któregoś brakuje, plik nie zostaje zapisany.
- **Długie dokumenty**: segmentacja według okna kontekstowego modelu.
- **Tryb `--news`**: angielskie cytaty są chronione, a flagi zarządzane według
  języka, z myślą o artykułach przeglądowych.
- **Tryb `--eco`**: szybkie i tańsze modele.
- Opcjonalna **notatka o tłumaczeniu**, na górze, na dole lub w obu miejscach.

## Instalacja

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 lub nowszy. Aby zainstalować z repozytorium, zobacz
[Współtworzenie](#współpraca).

## Konfiguracja

Klucze są odczytywane z trzech miejsc, od najwyższego priorytetu do najniższego;
każde z nich uzupełnia tylko to, co poprzednie pozostawiło puste.

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
użytkownika podlega `XDG_CONFIG_HOME` (tylko ścieżka bezwzględna) oraz `%APPDATA%`
w systemie Windows. Bez klucza polecenie wyświetla wszystkie trzy lokalizacje.

**Plik `.env` w projekcie nie może ani przekierowywać wywołań, ani wybierać
wykonywanego programu.** Dostarcza klucze, nigdy cel ani plik binarny: wszelkie
zmienne w `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, serwery proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane wraz z ostrzeżeniem. Sklonowane repozytorium nie może
mieć możliwości przechwycenia Twojego klucza ani uruchomienia własnego programu przy
pierwszym tłumaczeniu. Plik ten jest również odczytywany bez interpolacji:
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

`document.md` przetłumaczony na język hiszpański daje `document-es.md` w `--target_dir`;
z `--include_model` — `document-es-gpt-5.6-terra.md`. Rozszerzeniem
zawsze staje się `.md` — `article.mdx` daje `article-en.md` — z wyjątkiem opcji
`--keep_filename`, która zachowuje oryginalną nazwę. Istniejące już tłumaczenie
jest pomijane, chyba że użyto `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli chociaż jeden plik
zakończył się niepowodzeniem (lista na standardowym wyjściu błędów), `2`, jeśli problem dotyczy konfiguracji.
Plik z błędem nigdy nie zostaje zapisany, nawet jeśli sam zapis się nie powiedzie:
zawartość jest zapisywana obok, a następnie zmieniana jest jej nazwa. Wystarczy uruchomić ponownie.

## Jaki model wybrać

Zmierzone na dwóch rzeczywistych dokumentach, przetłumaczonych na te same czternaście języków przez
każdy model. **Liczba oznacza liczbę języków, na czternaście, w których tłumaczenie
zostało zapisane i w których nic nie różni się od źródła.**

| Model                | Jak uzyskać dostęp                | Gęsty artykuł przeglądowy | Ten README   | Co się różni i w ilu językach                                                                                                         |
| -------------------- | --------------------------------- | ------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ✅ 14/14     | nic, w żadnym z dwóch dokumentów                                                                                                      |
| **Gemini 3.7 Flash** | klucz API Google                  | ✅ 14/14                  | ⚠️ 13/14     | 1 język na 14: o jedno pogrubione słowo więcej (ja)                                                                                   |
| **Gemini 3.7 Flash** | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ⚠️ 13/14     | 1 język na 14: o jedno pogrubione słowo mniej (ko)                                                                                    |
| **GPT-5.6 Sol**      | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14               | ⚠️ 12/14     | 2 języki na 14: o jedno pogrubione słowo mniej (ar, ja)                                                                               |
| **GLM-5.2**          | klucz OpenRouter                  | ✅ 14/14                  | ⚠️ 11/14     | 3 języki na 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                           |
| Claude Sonnet 5      | klucz API Anthropic               | ⚠️ 11/14                  | ⚠️ 12/14     | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym README: link bez znaczników (sv), pogrubione słowo (zh)              |
| Qwen 3.7 Flash       | klucz OpenRouter                  | ❌ 8/14                   | ⚠️ 10/14     | 1 język odrzucony w artykule, 5 innych odbiega od normy; w tym README około czterdziestu słów ujętych w `code` (ar)         |
| Grok 4.6             | subskrypcja Grok                  | ❌ 8/14                   | nieoceniany  | 5 języków odrzuconych na 14 z powodu braku zwróconych kodów w tekście i adresów URL; język niderlandzki odbiega we wszystkim         |
| GPT-OSS 20B          | model lokalny (Ollama)            | ❌ 7/14                   | nie mierzono ponownie | 4 języki odrzucone na 14: model pozostawił fragmenty po francusku, mechanizm ochronny je zatrzymał                                 |
| MiMo v2.5 (darmowy)  | OpenCode Zen, bez konta           | ❌ 11/14                  | nie mierzono ponownie | 1 język odrzucony; utracona sekcja w języku polskim                                                                                   |
| Mistral Large        | klucz API Mistral                 | ❌ 5/14                   | ❌ 1/14      | **cała sekcja znika**: 1 język w artykule (hi), 3 w tym README (ar, hi, ko) — oraz 3 języki odrzucone w artykule                      |
| DeepSeek V4 Flash    | klucz OpenRouter                  | ❌ 3/14                   | nie mierzono ponownie | 10 języków odrzuconych na 14; 37 minut na język                                                                                      |

|     | Co oznacza symbol                                                                                                                                                                                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | wszystkie czternaście języków przetłumaczone i nic nie różni się od źródła                                                                                                                           |
| ⚠️  | wszystkie czternaście języków przetłumaczone; różnice dotyczą **znaczników** — pogrubionego słowa, `code`, linku tracącego nawiasy kwadratowe. Nie brakuje żadnego tekstu, adresu URL, bloku kodu ani sekcji |
| ❌  | co najmniej jeden język nie mógł zostać przetłumaczony — plik został odrzucony i nie zapisany — **lub** w zapisanym pliku brakuje zawartości                                                          |

Wnioski:

- **Odrzucone tłumaczenie to nie uszkodzone tłumaczenie.** Gdy po powrocie brakuje
  tokena, plik nie zostaje zapisany, a język liczy się jako
  odrzucony. To właśnie przytrafiło się modelowi Grok w artykule: cztery fragmenty kodu w tekście i
  trzy adresy URL utracone już w pierwszym segmencie w pięciu pismach nielacińskich.
- **Ta siatka bezpieczeństwa nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik, który narzędzie zapisuje
  bez wahania — tak jest w przypadku Mistrala. Elementów tych nie da się
  zastąpić tokenem, a obecne mechanizmy ochronne ich nie kontrolują;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny w tym README**: jego sesja CLI wygasła po dwunastu
  językach, z czego jedenaście bez żadnych rozbieżności. Przerwany przebieg testów nie podlega ocenie.
- **Gęstość dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze
  zwykłymi plikami README, a gubi się przy artykule przeładowanym linkami, w tym w
  języku niderlandzkim.

Daty i dokumenty: kolumna „Ten README” została zmierzona 9 września 2026 r.
na zamrożonej wersji tego pliku (785 wierszy, 285 kodów w tekście, 89 wierszy
tabeli), od tego czasu zmodyfikowanej — z wyjątkiem dwóch wierszy Antigravity, zmierzonych
26 września na wersji opublikowanej z wydaniem 1.14.0, która była krótsza (600 wierszy,
257 kodów w tekście, 85 wierszy tabeli). Kolumna „Gęsty artykuł
przeglądowy” pochodzi z testów z 4 i 5 września na artykule liczącym 589 wierszy,
z wyjątkiem wiersza Grok, zmierzonego ponownie 9 września na innym wydaniu tego samego
przeglądu, oraz dwóch wierszy Antigravity, zmierzonych 26 września na tym samym
artykule.
Pełne tabele, czasy trwania i protokół znajdują się w sekcji
[Szczegółowe pomiary](#szczegółowe-pomiary).

## Wszystkie opcje

| Opcja                    | Opis                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Pojedynczy plik Markdown do przetłumaczenia (alternatywa dla `--source_dir`)                                  |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown (domyślnie: `content/posts`)                                       |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików (domyślnie: `traductions_en`)                                     |
| `--source_lang`           | Język źródłowy (domyślnie: `fr`)                                                                   |
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
| `--use_opencode`           | Użyj OpenCode (open source) z dostawcą skonfigurowanym w OpenCode; wymaga `--model provider/modèle`                      |
| `--use_openrouter`           | Użyj OpenRouter — wymaga `OPENROUTER_API_KEY` oraz `--model fournisseur/modèle`                                                   |
| `--force`           | Wymuś ponowne tłumaczenie                                                                                     |
| `--keep_filename`           | Zachowaj oryginalną nazwę pliku                                                                               |
| `--news`           | Tryb aktualności: chroni cytaty w języku angielskim, zarządza flagami według języka                           |
| `--add_translation_note`           | Dodaj notatkę o tłumaczeniu                                                                                   |
| `--note_position`           | Pozycja notatki: `top`, `bottom` (domyślnie) lub `both`                                |
| `--note_format`           | Format notatki: `legacy` (domyślnie, pogrubiony akapit) lub `marker`                              |
| `--include_model`          | Dołącz nazwę modelu w pliku wyjściowym                                                                        |
| `--reasoning_effort`          | Wysiłek rozumowania GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`  |

Dziewięć flag `--use_*` wzajemnie się wyklucza: połączenie dwóch z nich jest
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

| Provider    | Jakość (domyślnie)                                    | Ekonomiczny (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (także `terra` i `luna` przez `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` wymagany                 | to samo — `--eco` bez wpływu |
| OpenRouter  | `--model fournisseur/modèle` wymagany              | to samo — `--eco` bez wpływu |

### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest odliczane od limitu
subskrypcji ChatGPT, bez klucza API i bez rozliczania według użycia.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Plik binarny jest szukany w `CODEX_BIN`, następnie w `PATH`, a potem w pakiecie
  `openai-codex-cli-bin`. `~/.codex/auth.json` nigdy nie jest odczytywany.
- `OPENAI_API_KEY` i `CODEX_API_KEY` są usuwane ze środowiska
  podprocesu: obecny klucz nigdy nie powoduje przełączenia na API.
- Każdy segment kosztuje co najmniej jedną „wiadomość” z 5-godzinnego okna — dwie,
  jeśli jego walidacja się nie powiedzie i nastąpi ponowna próba. OpenAI szacunkowo
  podaje 250–2000 wiadomości/5 h dla `gpt-5.6-luna` (`--eco`) oraz
  10–100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-terra` i `--model gpt-5.6-luna` również działają w ramach
  subskrypcji. Model, do którego konto nie ma uprawnień, zwraca błąd 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Wolniejsze niż API, a różnica rośnie wraz z wielkością dokumentu: w przypadku tego README
  mediana wynosi 6 min 46 s na język przy `gpt-5.6-sol`, w porównaniu z 36 s dla
  `gemini-3.7-flash`.
- Odrzucane w środowisku CI (zdefiniowane `CI` lub `GITHUB_ACTIONS`): subskrypcja
  uwierzytelnia się za pomocą osobistego pliku sesji, który nie powinien znajdować się na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada z oficjalnym CLI Grok Build, w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Piaskownica systemu operacyjnego Grok nie ma
  zastosowania na wielu nowszych maszynach z systemem Linux (AppArmor, gniazda runtime'u
  kontenerów), a profil, którego nie da się zastosować, uruchamia się po cichu
  bez izolacji. Skrypt domyślnie nie żąda więc żadnego profilu, informuje o tym i
  polega na regułach `--deny` z CLI, w tym zbiorczej `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast po cichu wyłączać ochronę.
  `GROK_TRANSLATE_SANDBOX=read-only` wymaga piaskownicy systemu operacyjnego, a uruchomienie
  kończy się błędem, jeśli maszyna nie jest w stanie jej zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, i żadne
  polecenie nie pozwala go odczytać: partia zadań może uszczuplić limit konwersacyjny
  bez ostrzeżenia.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach subskrypcji Google: `--use_antigravity`

Ta sama zasada z `agy`, oficjalnym CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie jest odliczane od limitu subskrypcji zamiast
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
  terminal, tożsamość, proxy i certyfikaty, magistralę sesji — i żadnego klucza:
  kilka z jego zmiennych potrafi przełączyć wywołanie bez wyświetlania czegokolwiek (zmierzone:
  jedna wysyła dokument do zewnętrznej bramki, inna do płatnego projektu
  Google Cloud), a lista blokowanych pomijała coś przy każdym przeglądzie.
  Przed jakimkolwiek segmentem polecenie `agy -p /config`, które nie zużywa limitu, musi pokazać,
  że płatne kredyty AI są wyłączone, bez klucza API ani projektu Google Cloud — brak
  ustawienia oznacza odmowę —, w przeciwnym razie nic nie zostanie przetłumaczone; dziennik każdego
  wywołania musi następnie potwierdzić subskrypcję (`authMethod=consumer`), inaczej
  odpowiedź zostanie odrzucona.
- **Izolacja.** Każde wywołanie działa w prywatnym, tymczasowym katalogu domowym,
  z agentem tłumaczącym pozbawionym narzędzi: Twoje ustawienia, reguły,
  wtyczki, serwery MCP i hooki agy nie mają do niego dostępu, nic nie trafia do Twojej
  historii, a dane logowania pozostają w pęku kluczy, którego aipmt nigdy nie czyta.
  Nieodnaleziony agent powoduje cichy powrót agy do domyślnego agenta programowania
  i jego narzędzi: cała linia w dzienniku musi potwierdzić właściwego agenta — dokument
  cytujący ten komunikat jej nie zastępuje —, w przeciwnym razie następuje odmowa.
- **Platformy**: Linux w sesji posiadającej pęk kluczy (magistrala sesyjna
  D-Bus, Secret Service); macOS jest akceptowany, choć nie był na nim mierzony. Odrzucane
  w systemie Windows, gdzie agy nie odczytuje zmiennych izolujących poszczególne wywołania,
  oraz w systemie Linux bez magistrali sesyjnej — sesje SSH, kontenery, serwery: agy
  przechowuje tam swój token w pliku w `~/.gemini`, który izolacja ukrywa.
  Odmowa następuje przed jakimkolwiek uruchomieniem, wraz z podaniem przyczyny, zamiast minutowego
  oczekiwania na kod logowania.
- **Modele**: modele z `agy models`. Modele Gemini mają poziom wysiłku (effort) w swojej nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez sufiksu jest odrzucana przed wywołaniem,
  a `--reasoning_effort` nie przynosi efektu. Domyślnie `gemini-3.8-flash-medium`,
  a `gemini-3.7-flash-low` w trybie `--eco`; serie pomiarowe, które je ustaliły,
  opisano w sekcji [Szczegółowe pomiary](#szczegółowe-pomiary). Claude i GPT-OSS
  mają własny, znacznie mniejszy limit: około 1% 5-godzinnego okna na zmierzone wywołanie,
  w porównaniu do 0,05% w przypadku Flash.
- **Limit**: według grupy — okno 5-godzinne oraz tygodniowe, proporcjonalnie
  do kosztu w tokenach. Zmierzone na koncie autora: około
  16 punktów 5-godzinnego okna na milion znaków źródłowych w `gemini-3.8-flash-medium`,
  14 w `gemini-3.7-flash-medium` oraz 7 do 8 przy niskim wysiłku (effort) — README o objętości
  40 000 znaków kosztuje zatem nieco ponad pół punktu. Tygodniowy limit zależy
  od planu. Ponawianie prób przebiega według reguł zgłaszanych przez agy jako możliwe
  do ponowienia; w przeciwnym razie wyczerpane okno nigdy nie jest ponawiane:
  powoduje błąd każdego pliku aż do resetu wyświetlanego przez `/usage`.
- **Wolniejsze niż API**: w gęstym artykule z pomiarami mediana wyniosła 3 min 59 s na
  język w `gemini-3.8-flash-medium` oraz 3 min 14 s w
  `gemini-3.7-flash-medium`, w porównaniu do 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerywanie**: Ctrl-C lub zamknięcie terminala zatrzymują agy wraz z
  poleceniem, zamiast pozwalać mu dokończyć turę na Twoim limicie; to samo dotyczy
  Codex, Grok CLI i OpenCode. W przypadku `nohup` tłumaczenie jest kontynuowane.
- Odrzucane w CI (zdefiniowane `CI` lub `GITHUB_ACTIONS`): logowanie opiera się na
  osobistym pęku kluczy. Na runnerze należy użyć `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, a następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment, łącznie z uruchomieniem, domyślnie 900).

**Warunki korzystania: robisz to na odpowiedzialność własnego konta.**
[Warunki Antigravity](https://antigravity.google/terms) (sekcja 6) oraz
[FAQ](https://antigravity.google/docs/faq/) zabraniają uzyskiwania dostępu do usługi
za pośrednictwem oprogramowania firm trzecich przy użyciu sesji logowania Antigravity — Claude Code,
OpenClaw i OpenCode są tam wymienione — pod rygorem zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokena: uruchamia oficjalny plik binarny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
dokumentuje na potrzeby skryptów i CI. Przedstawiciel Google uznał za „standardowe”
uruchamianie `agy -p` z lokalnego skryptu na własne potrzeby
([oficjalne forum, 25 września 2026 r., odpowiedź niewiążąca](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden zapis nie rozstrzyga jednoznacznie kwestii narzędzi dystrybuowanych w ten sposób.

**Tylko dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków
interakcje — prompty, odpowiedzi, metadane — mogą być wykorzystywane do ulepszania
produktów i uczenia maszynowego Google oraz weryfikowane przez
ludzi, również w przypadku płatnej subskrypcji. Rezygnacja wymaga użycia ustawienia
`enableTelemetry`, o nieudokumentowanym działaniu, którego aipmt nie ustawia; Twoje ustawienia
agy nie są przenoszone do środowiska izolowanego. Nie przesyłaj tą drogą żadnych poufnych danych.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to otwartoźródłowy (MIT) agent do kodowania, który
kieruje zapytania do dostawców skonfigurowanych wewnątrz niego: klucz API, subskrypcja,
bramka OpenCode Zen (darmowe modele, bez konta) lub model lokalny. Dwie
ścieżki zostały tutaj zmierzone kompleksowo: Zen i Ollama.

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

`--model` jest wymagany: bez niego OpenCode powróciłby do bezpłatnego modelu,
którego zapytania mogą być wykorzystywane do trenowania, a wybór ten nie powinien być
podejmowany za Ciebie.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, mająca pierwszeństwo przed Twoją, definiuje agenta `aipmt`,
  dla którego wszystkie narzędzia są odrzucone (`permission: { "*": "deny" }`), udostępnianie
  sesji wyłączone, `--pure`, nigdy `--auto`;
- tymczasowy i pusty katalog roboczy, ustawione `OPENCODE_DISABLE_PROJECT_CONFIG` i
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstrzykuje do promptu
  `AGENTS.md` z bieżącego katalogu oraz `~/.claude/CLAUDE.md`.
  Globalny `~/.config/opencode/AGENTS.md` nadal jest wstrzykiwany, OpenCode nie pozwala
  go pominąć;
- warunki wyjścia (output contract): kod wyjścia 0, brak zdarzeń `error`, brak wywołań
  narzędzi, ostatni krok jako `stop`, niepusty tekst i agent `aipmt`
  rzeczywiście załadowany — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  cichy powrót do agenta programowania;
- żaden klucz z `aipmt` nie jest przekazywany, z wyjątkiem `OPENCODE_API_KEY`, czyli klucza
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  `.env` z `aipmt`.

Warto wiedzieć:

- Darmowe modele w Zen ulegają zmianom, mają nieudokumentowane limity, a
  przesyłane do nich treści mogą służyć do trenowania: nadają się do publicznej
  dokumentacji, nie do treści poufnych.
- Model lokalny musi oferować co najmniej 16k tokenów kontekstu, ponieważ segmenty
  mają do 16 000 znaków. Ollama często ustawia domyślnie 4096: należy użyć
  `Modelfile` z `PARAMETER num_ctx 32768`.
- `--eco` nie ma wpływu; `--reasoning_effort` jest przekazywany bez zmian jako
  `--variant` w OpenCode.
- OpenCode rejestruje każdą sesję w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, a następnie `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekundy na segment, domyślnie 600). `OPENCODE_CONFIG`
  jest przekazywany bez zmian do OpenCode.

Przykład lokalnego modelu przez Ollama, w `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` wyłącza rozumowanie (thinking), które Ollama domyślnie włącza w tych
modelach i którego Modelfile nie może wyłączyć. Zmierzone na zdaniu liczącym
sześć słów: 919 tokenów rozumowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Dostęp do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według rzeczywistego użycia w ramach jednorazowego doładowania, działający przed
modelami hostowanymi przez podmioty trzecie — w tym otwartymi modelami chińskimi, których żaden
inny dostawca tutaj nie udostępnia.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest wymagany. Test wstępny (preflight), wykonywany przed jakimkolwiek naliczeniem opłat, rozwiązuje
dwie specyficzne kwestie związane z routingiem:

- **Ten sam model jest obsługiwany przez dziesiątki dostawców hostingu o różnych limitach** —
  w przypadku `z-ai/glm-5.3-flash` to 23 dostawców, z czego jeden ma limit wyjściowy wynoszący zaledwie
  2048 tokenów. Test wstępny odczytuje `/api/v1/models/{modèle}/endpoints`,
  odrzuca dostawców z limitem poniżej 8000 tokenów wyjściowych lub ze statusem obniżonej jakości, a
  pozostałych przypina za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki wyjściowej** — 107 tokenów w porównaniu do 2 przy
  odpowiedzi „OK” z `z-ai/glm-5.2`. Jest ono domyślnie wyłączone; modele,
  które go wymagają, otrzymują najniższy akceptowany poziom wysiłku, ponieważ domyślna wartość
  z katalogu mogłaby wyczerpać limit wyjściowy przed ukończeniem tłumaczenia.
  `--reasoning_effort` nadal ma pierwszeństwo.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model poniżej 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8400 na prompt i segment oraz co najmniej
  8000 na wyjście.
- Brak sluga w katalogu, niedostępny katalog lub brak
  hosta spełniającego wymagania limitu powodują zatrzymanie polecenia.
- `finish_reason=length` z pustym wyjściem oznacza budżet skonsumowany przez
  rozumowanie, a nie obcięcie odpowiedzi: komunikat wyraźnie to rozróżnia.
- `--eco` nie przynosi efektu.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Notatka o tłumaczeniu

`--add_translation_note` dodaje notatkę, na `bottom` (domyślnie), na `top` (po
front matter) lub `both` (`--note_position`), w formacie `legacy` (akapit
wytłuszczony, domyślnie) lub `marker` (`--note_format`). Format `marker` to
niewidoczna definicja referencyjna Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje wytłuszczony cytat blokowy: czytelny na GitHubie, możliwy do wykorzystania podczas budowania przez
wtyczkę remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary to tłumaczenia rzeczywiście wykonane za pomocą `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** zlicza pliki, które przepuściły mechanizmy ochronne (guards); **Bez
różnic** te, w których `scripts/compare_structure.py` nie wykrywa niczego — taka sama liczba
sekcji, podtytułów, linków, unikalnych adresów URL, bloków kodu,
kodu w tekście, wierszy tabeli, bloków cytatów i pogrubionych słów.

„Bez różnic” oznacza „nic nie wykryto”, a nie „identyczne”: narzędzie porównujące
zlicza elementy bez czytania ich treści. Nie zgłasza usunięcia nagłówka
poziomu 4, zastąpienia tekstu w kodzie w tekście, zamiany flagi
ani linku wewnętrznego wygenerowanego ze zbędnym nawiasem,
`[texte]((#ancre))`, który już nigdzie nie prowadzi — i nie ocenia
języka.

### Gęsty artykuł z przeglądu wiadomości, tryb `--news`

Wydanie [przeglądu AI z jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty w języku angielskim. Pomiary
z 4 i 5 września 2026 r.

| Model                                           | Dostęp             | Zapisane | Bez rozbieżności | Mediana/język |
| ----------------------------------------------- | ------------------ | -------- | ---------------- | ------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14    | ✅ **14/14**     | 1 min 18 s    |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | subskrypcja Google | 14/14    | ✅ **14/14**     | 3 min 59 s    |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | subskrypcja Google | 14/14    | ✅ **14/14**     | 3 min 14 s    |
| `gpt-5.6-sol` (`--use_codex`)                   | subskrypcja ChatGPT | 14/14    | ✅ **14/14**     | 11 min 28 s   |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14    | ✅ **14/14**     | 5 min 37 s    |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14    | ✅ **14/14**     | 26 min 23 s   |
| `claude-sonnet-5`                               | API Anthropic      | 14/14    | ⚠️ 11/14         | 6 min 31 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14    | ❌ 11/14         | 9 min 27 s    |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14    | ❌ 8/14          | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`                        | lokalnie           | 10/14    | ❌ 7/14          | 12 min 39 s   |
| `mistral-large-latest`                          | API Mistral        | 11/14    | ❌ 5/14          | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14     | ❌ 3/14          | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)                   | subskrypcja Grok   | 1/14     | ❌ 1/14          | 23 min 11 s   |

Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): 9 zapisanych języków na 14, 8 bez rozbieżności. To właśnie ta liczba
widnieje w głównej tabeli. Trzy przerwane serie testów nie zostały uwzględnione:
`qwen3.5-27b` (9 języków) i `kimi-k2.6` (4) z braku środków,
`z-ai/glm-5.3-flash`, którego dwie nieudane próby wynikały z ustawienia wnioskowania,
poprawionego w międzyczasie przez dostawcę. Wiersze OpenRouter zmierzono przy
domyślnych ustawieniach routera, przed `--use_openrouter`; `z-ai/glm-5.2`,
ponownie zmierzony z domyślnym dostawcą, daje ten sam wynik 14/14. Liczby zostały
przeliczone 10 września za pomocą obecnego narzędzia porównującego: `qwen3.8-flash` i
`qwen3.7-flash` zyskują po jednym języku w stosunku do pierwszej
publikacji, pozostałe pozostały bez zmian.

Wiersze `--use_antigravity` zmierzono 26 września na tym samym
artykule, cztery tłumaczenia równolegle: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W języku angielskim każdy z nich samodzielnie
usunął trzy wiersze francuskiego tłumaczenia pod cytatami, nie generując żadnej
flagi, a angielskie cytaty pozostały nienaruszone: mechanizm czyszczenia awaryjnego
nie musiał nic robić. W `--eco` (`gemini-3.7-flash-low`), tylko dla czterech
języków (en, ja, ar, hi): 4 zapisane na 4, wszystkie bez rozbieżności, mediana
1 min 52 s. Próba kontrolna tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 cytaty angielskie), przetłumaczona poza
blogiem przez `gemini-3.7-flash-medium`: 14 zapisanych na 14, wszystkie bez rozbieżności, od 87 do
128 s na język.

### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026 r.: 785 wierszy, 285 kodów śródliniowych, 40
domknięć bloków, 89 wierszy tabeli. Cztery tłumaczenia równolegle.

| Model                                           | Zapisane | Bez rozbieżności | Mediana/język | Różnice                                                                  |
| ----------------------------------------------- | -------- | ---------------- | ------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14         | 1 min 43 s    | nic                                                                      |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14         | 36 s          | jedno pogrubione słowo (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14         | 1 min 22 s    | jedno pogrubione słowo (ko)                                              |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14         | 2 min 56 s    | jeden link (sv), jedno pogrubione słowo (zh)                             |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14         | 6 min 46 s    | jedno pogrubione słowo (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14         | 2 min 34 s    | jedno pogrubione słowo (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14         | 2 min 17 s    | 40 dodanych kodów śródliniowych w arabskim; pogrubienie (hi, ja, ko)     |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14          | 2 min 44 s    | utracona sekcja (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh)        |

Dwie przerwane serie nie zostały uwzględnione: Grok, wygaśnięcie sesji CLI
po dwunastu językach (jedenaście bez rozbieżności), oraz `qwen3.8-flash`, błąd HTTP 429
od dostawcy hostingu po dwóch. Modele `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie były ponownie mierzone na tej rewizji; na wersji z 4 i 5 września,
krótszej o 277 wierszy, każdy z nich zapisał po 9 tłumaczeń na 14, w tym odpowiednio 7
i 1 bez rozbieżności.

Wiersze `--use_antigravity` nie były mierzone na zamrożonej rewizji,
lecz 26 września na wersji opublikowanej z wydaniem 1.14.0: 600 wierszy, 257 kodów
śródliniowych, 30 domknięć bloków, 85 wierszy tabeli. Krótsza o 185
wierszy, nie pozwala na bezpośrednie porównanie z pozostałymi wierszami; natomiast oba
wiersze Antigravity można porównywać między sobą. W przypadku linków wewnętrznych,
których narzędzie porównujące nie weryfikuje, `gemini-3.8-flash-medium` zachował je
w nienaruszonym stanie we wszystkich czternastu językach, a `gemini-3.7-flash-medium` uszkodził je w języku
włoskim.

### Cztery pliki README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane wprost z GitHuba — dokumenty
prostsze niż dwa poprzednie. Seria ta była skierowana na modele
mające trudności; Gemini służy w niej jako punkt odniesienia.

| Model                         | Zakres                     | Zapisane | Bez rozbieżności |
| ----------------------------- | -------------------------- | -------- | ---------------- |
| `gemini-3.7-flash`             | 4 projekty × 14 języków    | 56/56    | ✅ **55/56**     |
| `opencode/mimo-v2.5-free`      | 4 projekty × 14 języków    | 55/56    | ❌ 47/56         |
| `grok-4.6` (subskrypcja) | 4 projekty × ar, hi, ja, zh | 16/16    | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`       | 4 projekty × ar, hi, ja, zh | 15/16    | ❌ 9/16          |

### Czym te pomiary nie są

- **To nie jest wyczerpujący ranking**: sam OpenRouter oferuje ponad czterysta
  modeli, zmierzono około piętnastu.
- **Czasy mają charakter orientacyjny**: od trzech do sześciu równoległych tłumaczeń
  w zależności od serii testów, a przepustowość dostawcy zmienia się w ciągu dnia.
- **Obserwacje osadzone w czasie**: modele zmieniają się pod tą samą nazwą, a Twoje
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

Oba wiersze są wymagane: bez `pip install -e .` narzędzie `python -m aipmt`
odpowiada `No module named aipmt`.

Narzędzia zapewniania jakości, opcjonalne, ale zalecane:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Wszystkie 28 tłumaczeń w repozytorium (README i CHANGELOG, czternaście języków)
regeneruje się za pomocą `./regen_translations.sh --force` — domyślnie Codex i `gpt-5.6-sol`
w ramach subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` i
`REGEN_MODEL` zmieniają ścieżkę: `antigravity` pozostaje przy subskrypcji, tym razem
Google, i przechodzi bez wyjątku; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1800 s dla Codex i
Antigravity). Szczegółowe informacje o narzędziach znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — prywatny blog publikowany w 15 językach. Jego
  [codzienny przegląd AI](https://jls42.org/fr/news) jest tłumaczony każdego dnia
  przez to narzędzie i służy jako dokument referencyjny dla powyższych pomiarów.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Zastrzeżenia prawne

Niniejszy program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, na warunkach
określonych w punktach 15 i 16 licencji GPL v3: dostarczany w stanie, w jakim się znajduje („tak jak jest”),
bez rękojmi przydatności handlowej ani przydatności do określonego celu, a jego autor nie może być
pociągnięty do odpowiedzialności za jakiekolwiek szkody wynikające z jego użytkowania. Pełny tekst
licencji ma pierwszeństwo przed niniejszym podsumowaniem.

- **Sprawdź przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod śródliniowy, adresy URL, kotwice oraz cytaty w trybie `--news` — nie
  obejmują nagłówków, tabel, sekcji front matter ani sensu Twoich zdań.
- **Twoje dokumenty są przesyłane do wybranego dostawcy**, zgodnie z jego warunkami
  korzystania z usług i polityką ochrony danych. Niektóre darmowe modele mogą
  wykorzystywać Twoje dane do trenowania, a warunki usługi Antigravity
  pozwalają firmie Google na ich ponowne wykorzystanie i weryfikację przez ludzi,
  w tym również w ramach płatnej subskrypcji; model lokalny jest jedynym rozwiązaniem, które
  gwarantuje, że żadne dane nie opuszczą Twojej maszyny.
- **Wywołania API są płatne.** Program ten nie nakłada limitu
  wydatków: długi dokument, ponowienie próby po błędzie lub model intensywnie
  korzystający z wnioskowania generują wyższe koszty.
- **Opublikowane pomiary to obserwacje osadzone w czasie**, a nie gwarancje.

Wymienione nazwy produktów i firm należą do ich odpowiednich
właścicieli. Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z fr na pl za pomocą gemini-3.8-flash-medium.**
