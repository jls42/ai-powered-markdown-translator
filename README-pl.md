# Translator Markdown oparty na AI

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Problemy jakości kodu"></a>
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
matter. Jedenaście sposobów wywoływania modelu — pięć API, cztery subskrypcje bez
opłat za użycie oraz dwa routery — wraz z opublikowanym pomiarem tego, co każdy
model rzeczywiście zachowuje.

## W skrócie

- **Jedenaście ścieżek dostawców**: API OpenAI, Mistral, Claude, Gemini i Grok;
  subskrypcje ChatGPT (Codex), Grok, Google (Antigravity) i Claude (Claude
  Code) bez opłat za użycie; routery OpenCode (open source, bezpłatny lub lokalny) i OpenRouter
  (ponad 400 modeli).
- **Żadnych fałszywych wyników wskutek utraty tokenu**: bloki kodu, kod w tekście,
  URL-e, kotwice i cytaty są zastępowane tokenami przed wywołaniem modelu i
  sprawdzane po otrzymaniu odpowiedzi. Jeśli któregoś brakuje, plik nie jest zapisywany.
- **Długie dokumenty**: segmentacja zgodnie z oknem kontekstowym modelu.
- **Tryb `--news`**: chronione angielskie cytaty i flagi obsługiwane według
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

Klucze są odczytywane z trzech miejsc, od najwyższego do najniższego priorytetu;
każde z nich uzupełnia wyłącznie wartości pozostawione puste przez poprzednie.

|     | Gdzie                                            | Zastosowanie                                  |
| --- | ----------------------------------------------- | --------------------------------------------- |
| 1   | Zmienne środowiskowe                            | CI, kontenery, jednorazowe nadpisanie         |
| 2   | `.env` w bieżącym katalogu (lub nadrzędnym) | klucz właściwy dla danego projektu            |
| 3   | `~/.config/aipmt/.env`                                  | instalowany raz, obowiązuje wszędzie          |

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
użytkownika korzysta z `XDG_CONFIG_HOME` (wyłącznie ścieżka bezwzględna) oraz `%APPDATA%`
w systemie Windows. W razie braku klucza polecenie wyświetla wszystkie trzy lokalizacje.

**Plik `.env` projektu nie może ani przekierowywać wywołań, ani wybierać
uruchamianego programu.** Udostępnia klucze, nigdy miejsce docelowe ani plik wykonywalny:
wszystkie zmienne w `_BASE_URL`, `_API_BASE`, `_ENDPOINT` lub `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxy (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), magazyny certyfikatów (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) oraz `XDG_CONFIG_HOME` /
`APPDATA` są w nim ignorowane, czemu towarzyszy ostrzeżenie. Sklonowane repozytorium nie może
przechwycić klucza ani spowodować uruchomienia własnego programu podczas
pierwszego tłumaczenia. Plik ten jest również odczytywany bez interpolacji:
`NOM=${OPENAI_API_KEY}` nie kopiuje do niego klucza. Ustaw te zmienne w
środowisku lub w `~/.config/aipmt/.env`.

Zmienne opcjonalne: `XAI_BASE_URL` (domyślnie `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekundy na wywołanie, domyślnie 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(domyślnie 600), `GROK_BIN`, `GROK_HOME` (domyślnie `~/.grok`), `GROK_TIMEOUT`
(domyślnie 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (domyślnie 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (domyślnie 600), `OPENROUTER_BASE_URL`
(wymagany `https://`), `OPENROUTER_TIMEOUT` (domyślnie 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (domyślnie 30). Każdą z nich szczegółowo opisano w
sekcji odpowiedniego dostawcy.

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
`--keep_filename`, które zachowuje oryginalną nazwę. Istniejące już tłumaczenie
jest pomijane bez `--force`.

Kody wyjścia: `0`, jeśli wszystko się powiodło lub zostało pominięte, `1`, jeśli pozostał plik,
którego przetwarzanie się nie powiodło (lista na standardowym wyjściu błędów), `2`, jeśli przyczyną jest konfiguracja.
Plik, którego przetwarzanie się nie powiodło, nigdy nie zostaje zapisany, nawet jeśli zawiedzie sam zapis:
treść jest zapisywana obok, a następnie zmieniana jest nazwa pliku. Wystarczy uruchomić polecenie ponownie.

## Który model wybrać

Pomiary przeprowadzono na dwóch rzeczywistych dokumentach tłumaczonych przez
każdy model na tych samych czternaście języków. **Liczba oznacza, w ilu spośród
czternastu języków tłumaczenie zostało zapisane i nic nie różniło się od źródła.**

| Model                 | Sposób dostępu                    | Gęsty artykuł przeglądowy | Ten plik README | Co się różni i w ilu językach                                                                                                                                      |
| --------------------- | --------------------------------- | ------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ✅ 14/14        | nic w żadnym z dwóch dokumentów                                                                                                                                    |
| **Claude Sonnet 5.5** | klucz API Anthropic               | ✅ 14/14                  | ✅ 14/14        | nic w żadnym z dwóch dokumentów                                                                                                                                    |
| **Gemini 3.7 Flash**  | klucz API Google                  | ✅ 14/14                  | ⚠️ 13/14        | 1 język z 14: jedno dodatkowe pogrubione słowo (ja)                                                                                                                |
| **Gemini 3.7 Flash**  | subskrypcja Google (Antigravity)  | ✅ 14/14                  | ⚠️ 13/14        | 1 język z 14: o jedno pogrubione słowo mniej (ko)                                                                                                                  |
| **GPT-5.6 Sol**       | subskrypcja ChatGPT lub klucz OpenAI | ✅ 14/14               | ⚠️ 12/14        | 2 języki z 14: o jedno pogrubione słowo mniej (ar, ja)                                                                                                             |
| **GLM-5.2**           | klucz OpenRouter                  | ✅ 14/14                  | ⚠️ 11/14        | 3 języki z 14: o jedno pogrubione słowo mniej (hi, ja, ko)                                                                                                         |
| Claude Sonnet 5       | subskrypcja Claude (Claude Code)  | ⚠️ 13/14                  | ⚠️ 13/14        | 1 język z 14 w artykule: jedno dodatkowe pogrubione słowo (zh); 1 w tym README: wiersz tabeli sklejony z poprzednim i niewidoczny podczas wyświetlania (ar)         |
| Claude Haiku 4.5      | subskrypcja Claude (Claude Code)  | ⚠️ 11/14                  | ✅ 14/14        | 3 języki w artykule: nagłówek sekcji zmieniony na poziom 1 (en, pl, ro); w tym README nic według narzędzia porównującego, ale linki wewnętrzne po angielsku zdublowane |
| Claude Sonnet 5       | klucz API Anthropic               | ⚠️ 11/14                  | ⚠️ 12/14        | 3 języki w artykule: pojawił się blok kodu (es, de, hi); 2 w tym README: link bez znaczników (sv), pogrubione słowo (zh)                                           |
| Claude Haiku 4.5      | klucz API Anthropic               | ⚠️ 7/14                   | ✅ 14/14        | 7 języków w artykule: nagłówek sekcji zmieniony na poziom 1 — w wersji japońskiej pozostał po francusku; nic w tym README                                          |
| Claude Haiku 5.5      | klucz API Anthropic               | ⚠️ 11/14                  | ❌ 12/14        | 3 języki w artykule: zmieniono poziom nagłówka sekcji lub go zdublowano (ja, ko, zh); w tym README odrzucono 2 języki z powodu utraty kodu w tekście (ar, hi)       |
| Qwen 3.7 Flash        | klucz OpenRouter                  | ❌ 8/14                   | ⚠️ 10/14        | 1 język odrzucony w artykule, 5 innych wykazuje różnice; w tym README około czterdziestu słów umieszczono w `code` (ar)                                    |
| Grok 4.6              | subskrypcja Grok                  | ❌ 8/14                   | bez oceny       | 5 języków z 14 odrzucono z powodu niezwrócenia kodu w tekście i URL-i; wersja niderlandzka różni się w całości                                                     |
| GPT-OSS 20B           | model lokalny (Ollama)            | ❌ 7/14                   | bez ponownego pomiaru | 4 języki z 14 odrzucono: model pozostawiał w nich fragmenty po francusku, więc mechanizm ochronny je zatrzymał                                               |
| MiMo v2.5 (bezpłatny) | OpenCode Zen, bez konta           | ❌ 11/14                  | bez ponownego pomiaru | 1 język odrzucony; w polskiej wersji utracono sekcję                                                                                                        |
| Mistral Large         | klucz API Mistral                 | ❌ 5/14                   | ❌ 1/14         | **znika cała sekcja**: w 1 języku artykułu (hi), w 3 językach tego README (ar, hi, ko) — ponadto w artykule odrzucono 3 języki                                    |
| DeepSeek V4 Flash     | klucz OpenRouter                  | ❌ 3/14                   | bez ponownego pomiaru | 10 języków z 14 odrzucono; 37 minut na język                                                                                                                |
| Claude Opus 5.5       | subskrypcja Claude (Claude Code)  | ❌ 0/14                   | ✅ 14/14        | artykuł odrzucony we wszystkich 14 językach przez mechanizmy ochronne Opus z powodu krótkiej wiadomości biologicznej; nic w tym README                            |

|     | Znaczenie symbolu                                                                                                                                                                                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | przetłumaczono wszystkie czternaście języków i nic nie różni się od źródła                                                                                                                              |
| ⚠️  | przetłumaczono wszystkie czternaście języków; różnice dotyczą **znaczników** — pogrubionego słowa, `code`, linku tracącego nawiasy kwadratowe. Nie brakuje żadnego tekstu, URL-a, bloku kodu ani sekcji |
| ❌  | co najmniej jednego języka nie udało się przetłumaczyć — plik został odrzucony i niezapisany — **lub** w zapisanym pliku brakuje treści                                                                  |

Najważniejsze wnioski:

- **Odrzucone tłumaczenie nie jest uszkodzonym tłumaczeniem.** Jeśli po otrzymaniu
  odpowiedzi brakuje tokenu, plik nie zostaje zapisany, a język jest liczony jako
  odrzucony. Tak dzieje się w przypadku Grok w artykule: cztery fragmenty kodu w tekście i
  trzy URL-e zostają utracone już w pierwszym segmencie w pięciu systemach pisma niełacińskiego.
- **Model może odrzucić cały dokument z powodu jednego zdania.** Opus 5.5
  tłumaczy ten plik README bez żadnych różnic, ale nie tłumaczy żadnego artykułu przeglądowego: jego
  mechanizmy ochronne zatrzymują odpowiedź na krótkiej wiadomości biologicznej. Plik nie zostaje
  zapisany, a aipmt podaje przyczynę.
- **Ta siatka bezpieczeństwa nie obejmuje nagłówków, tabel, front matter ani
  tekstu.** Model, który usuwa sekcję, zwraca plik zapisywany przez narzędzie
  bez sprzeciwu — tak dzieje się w przypadku Mistral. Tych elementów nie można
  zastąpić tokenem, a obecne mechanizmy ochronne ich nie sprawdzają;
  `scripts/compare_structure.py` wykrywa utraconą sekcję, ale dopiero po fakcie.
- **Grok nie ma oceny dla tego README**: jego sesja CLI wygasła po dwunastu
  językach, z których jedenaście nie wykazywało różnic. Przerwanej kampanii nie ocenia się.
- **Gęstość dokumentu ma większe znaczenie niż język.** Grok radzi sobie ze
  zwykłymi plikami README, ale zawodzi w artykule pełnym linków, także w języku
  niderlandzkim.

Daty i dokumenty: kolumnę „Ten plik README” zmierzono 9 września 2026 r.
na ustalonej rewizji tego pliku (785 wierszy, 285 fragmentów kodu w tekście, 89 wierszy
tabel), od tamtej pory zmodyfikowanej — z wyjątkiem wierszy Antigravity i Claude Code,
zmierzonych 26 września na rewizji opublikowanej z wersją 1.14.0, która jest krótsza
(600 wierszy, 257 fragmentów kodu w tekście, 85 wierszy tabel), oraz wierszy Claude
Sonnet 5.5, Haiku 5.5 i Haiku 4.5 przez API, zmierzonych 18 października na
tej samej rewizji. Kolumna „Gęsty artykuł przeglądowy” pochodzi z kampanii z
4 i 5 września przeprowadzonej na artykule liczącym 589 wierszy, z wyjątkiem wiersza Grok, zmierzonego ponownie
9 września na innym wydaniu tego samego przeglądu, wierszy Antigravity i
Claude Code, zmierzonych 26 września na tym samym artykule, oraz tych trzech wierszy
Claude, zmierzonych 18 października. Pełne tabele, czasy trwania i protokół znajdują się
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
| `--add_translation_note` | Dodaj notę dotyczącą tłumaczenia                                                                                |
| `--note_position`        | Pozycja noty: `top`, `bottom` (domyślnie) lub `both`                                                     |
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

`--eco` przełącza na ekonomiczny poziom każdego dostawcy.

| Dostawca    | Jakość (domyślnie)                                      | Ekonomiczny (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                   | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (także `terra` i `luna` przez `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, poziom `low`                                | bez zmian — `--eco` bez efektu |
| OpenCode    | `--model provider/modèle` wymagane                 | bez zmian — `--eco` bez efektu |
| OpenRouter  | `--model fournisseur/modèle` wymagane              | bez zmian — `--eco` bez efektu |

### W ramach subskrypcji ChatGPT: `--use_codex`

Steruje oficjalnym CLI Codex: tłumaczenie jest odliczane od limitu
subskrypcji ChatGPT, bez klucza API ani rozliczeń za użycie.

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
  jeśli jego walidacja zakończy się niepowodzeniem i zostanie ponowiona. OpenAI podaje szacunkowo
  250–2 000 wiadomości/5 godz. dla `gpt-5.6-luna` (`--eco`) oraz
  10–100 dla `gpt-5.6-sol` w planie Plus.
- `--model gpt-5.6-terra` i `--model gpt-5.6-luna` również korzystają z
  subskrypcji. Model, do którego konto nie ma dostępu, zwraca błąd 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Wolniejsze niż API, a różnica rośnie wraz z długością dokumentu: dla tego README
  mediana wynosi 6 min 46 s na język z `gpt-5.6-sol`, wobec 36 s dla
  `gemini-3.7-flash`.
- Odrzucane w CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): subskrypcja uwierzytelnia się
  przy użyciu osobistego pliku sesji, który nie powinien znajdować się na współdzielonym
  runnerze.
- Zmienne: `CODEX_BIN`, `CODEX_TIMEOUT` (sekundy na segment, domyślnie 600).

### W ramach subskrypcji Grok: `--use_grok_cli`

Ta sama zasada obowiązuje w przypadku oficjalnego CLI Grok Build, w ramach subskrypcji SuperGrok lub
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Słabsza izolacja niż w Codex.** Sandbox systemu operacyjnego Grok nie działa
  na wielu nowszych stanowiskach z Linuxem (AppArmor, sockety środowiska uruchomieniowego
  kontenerów), a profil, którego nie można zastosować, uruchamia się po cichu bez
  izolacji. Dlatego skrypt domyślnie nie wymaga żadnego profilu, informuje o tym i
  opiera się na regułach `--deny` CLI, w tym regule catch-all `*` — jedynej
  warstwie, która odmawia uruchomienia, zamiast bez ostrzeżenia usuwać ochronę.
  `GROK_TRANSLATE_SANDBOX=read-only` wymaga sandboxa systemu operacyjnego, a uruchomienie
  kończy się niepowodzeniem, jeśli maszyna nie może go zapewnić.
- Limit jest tygodniowy, współdzielony z Chat, Imagine i Voice, a żadna
  komenda nie pozwala go odczytać: zadanie wsadowe może zużyć część limitu przeznaczonego na rozmowy
  bez żadnego ostrzeżenia.
- Zmienne: `GROK_BIN`, `GROK_HOME` (katalog CLI, domyślnie `~/.grok`),
  `GROK_TIMEOUT` (domyślnie 900), `GROK_TRANSLATE_SANDBOX`.

### W ramach subskrypcji Google: `--use_antigravity`

Ta sama zasada obowiązuje w przypadku `agy`, oficjalnego CLI Antigravity: dla osób opłacających Google
AI Pro lub Ultra tłumaczenie jest odliczane od limitu subskrypcji zamiast
rozliczania za tokeny. To jedyny sposób korzystania z tego limitu: Gemini CLI
nie obsługuje już tych kont od 18 czerwca 2026 r.
([ogłoszenie](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
a SDK Antigravity akceptuje wyłącznie klucz API lub projekt Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Żadna płatna droga nie pozostaje otwarta.** agy otrzymuje z Twojego
  środowiska wyłącznie zamkniętą listę zmiennych — `PATH`, język i strefę czasową,
  terminal, tożsamość, proxy i certyfikaty, magistralę sesji — oraz żadnych kluczy:
  kilka jego zmiennych przełącza wywołanie bez wyświetlania jakiejkolwiek informacji (zmierzono:
  jedna wysyła dokument do bramy podmiotu trzeciego, inna do płatnego projektu
  Google Cloud), a lista odmów za każdym przeglądem pomijała kolejne przypadki.
  Przed każdym segmentem `agy -p /config`, które nie zużywa żadnego limitu, musi wskazać,
  że płatne kredyty AI są wyłączone, bez klucza API ani projektu Google Cloud —
  brak ustawienia oznacza odmowę — w przeciwnym razie nic nie zostanie przetłumaczone;
  dziennik każdego wywołania musi następnie potwierdzić użycie subskrypcji
  (`authMethod=consumer`), inaczej odpowiedź zostanie odrzucona.
- **Izolacja.** Każde wywołanie działa w prywatnym, jednorazowym katalogu domowym,
  z agentem tłumaczącym bez narzędzi: Twoje ustawienia, reguły,
  pluginy, serwery MCP i hooki agy nie trafiają do niego, nic nie jest dodawane do Twojej
  historii, a dane logowania pozostają w pęku kluczy, którego aipmt nigdy nie odczytuje.
  Jeśli agent nie zostanie znaleziony, agy po cichu przełącza się na swojego agenta kodującego
  i jego narzędzia: cały wiersz dziennika musi potwierdzać właściwego agenta — dokument,
  który cytuje ten komunikat, nie może go zastąpić — w przeciwnym razie następuje odmowa.
- **Platformy**: Linux w sesji z pękiem kluczy (magistrala sesji
  D-Bus, Secret Service); macOS jest obsługiwany, choć nie został na nim przetestowany.
  Odrzucane w systemie Windows, gdzie agy nie odczytuje zmiennych izolujących każde wywołanie,
  oraz w Linuxie bez magistrali sesji — sesja SSH, kontener, serwer: agy
  zapisuje tam swój token w pliku w `~/.gemini`, który zostaje ukryty przez izolację.
  Odmowa następuje przed uruchomieniem czegokolwiek i podaje przyczynę, zamiast powodować minutę
  oczekiwania na kod logowania.
- **Modele**: modele z `agy models`. Modele Gemini zawierają poziom rozumowania w nazwie
  (`gemini-3.8-flash-medium`…): nazwa bez sufiksu jest odrzucana przed wywołaniem,
  a `--reasoning_effort` nie ma efektu. Domyślnie używany jest `gemini-3.8-flash-medium`,
  a w `--eco` — `gemini-3.7-flash-low`; kampanie, w których je ustalono, opisano
  w sekcji [Szczegółowe pomiary](#szczegółowe-pomiary). Claude i GPT-OSS
  mają własny, znacznie mniejszy limit: około 1% 5-godzinnego okna
  na zmierzone wywołanie, wobec 0,05% w przypadku Flash.
- **Limit**: dla każdej grupy obowiązuje okno 5-godzinne oraz tygodniowe,
  proporcjonalnie do kosztu w tokenach. Pomiar na koncie autora: około
  16 punktów 5-godzinnego okna na milion znaków źródłowych dla
  `gemini-3.8-flash-medium`, 14 dla `gemini-3.7-flash-medium` oraz od 7 do 8 przy
  niskim poziomie — README zawierający 40 000 znaków kosztuje więc nieco ponad
  pół punktu. Limit tygodniowy zależy natomiast od poziomu subskrypcji. Ponowienie następuje
  zgodnie z tym, co agy określa jako możliwe do ponowienia; jeśli brak takiej informacji,
  wyczerpane okno nigdy nie jest ponawiane: powoduje niepowodzenie każdego pliku aż do
  resetu wskazywanego przez `/usage`.
- **Wolniejsze niż API**: dla obszernego artykułu z pomiarami mediana wynosi 3 min 59 s na
  język z `gemini-3.8-flash-medium` i 3 min 14 s z
  `gemini-3.7-flash-medium`, wobec 1 min 18 s dla Gemini 3.7 Flash przez API.
- **Przerwanie**: Ctrl-C lub zamknięcie terminala zatrzymują agy wraz z
  komendą, zamiast pozwalać mu dokończyć działanie kosztem Twojego limitu; tak samo jest w
  przypadku Codex, Grok CLI i OpenCode. W `nohup` tłumaczenie jest kontynuowane.
- Odrzucane w CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`): dane logowania znajdują się w
  osobistym pęku kluczy. Na runnerze użyj `--use_gemini` z `GOOGLE_API_KEY`.
- Zmienne: `AGY_BIN` (w przeciwnym razie `PATH`, a następnie `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekundy na segment, łącznie z uruchomieniem, domyślnie 900).

**Warunki korzystania: odpowiedzialność spoczywa na właścicielu konta.**
[Warunki Antigravity](https://antigravity.google/terms) (sekcja 6) oraz jego
[FAQ](https://antigravity.google/docs/faq/) zabraniają uzyskiwania dostępu do usługi
za pomocą oprogramowania podmiotu trzeciego przy użyciu danych logowania Antigravity — wymieniono tam
Claude Code, OpenClaw i OpenCode — pod groźbą zawieszenia konta. aipmt
nie odczytuje ani nie wykorzystuje ponownie tokenu: uruchamia oficjalny plik wykonywalny w
[trybie headless](https://antigravity.google/docs/cli/headless/), który Google
dokumentuje na potrzeby skryptów i CI. Pracownik Google uznał uruchamianie
`agy -p` z lokalnego skryptu na potrzeby własnej pracy za „standardową” praktykę
([oficjalne forum, 25 września 2026 r., odpowiedź niewiążąca](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
żaden dokument nie rozstrzyga przypadku dystrybuowanego narzędzia takiego jak to.

**Tylko dokumenty publiczne.** Zgodnie z sekcją 5 tych samych warunków
interakcje — prompty, odpowiedzi, metadane — mogą służyć do ulepszania
produktów Google i uczenia maszynowego oraz być przeglądane przez
ludzi, także w ramach płatnej subskrypcji. Rezygnacja odbywa się za pomocą ustawienia
`enableTelemetry`, którego działanie nie jest udokumentowane i którego aipmt nie ustawia; Twoje ustawienia
agy nie są przenoszone do jego odizolowanego środowiska. Nie przesyłaj w ten sposób żadnych poufnych danych.
### W ramach subskrypcji Claude: `--use_claude_code`

Ta sama zasada obowiązuje w przypadku `claude`, oficjalnego CLI Claude Code, w trybie `-p`: dla osób
opłacających Claude Pro lub Max tłumaczenie jest odliczane od limitu
subskrypcji, zamiast być rozliczane za token. Nie należy tego mylić z
`--use_claude`, API Anthropic rozliczanym według użycia.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Żadna płatna ścieżka nie pozostaje otwarta, a każde wywołanie tego dowodzi.** Claude
  Code otrzymuje ze środowiska wyłącznie zamkniętą listę zmiennych — bez
  klucza API, tokenu, dostawcy chmurowego ani znacznika sesji Claude Code,
  z której uruchomiono by aipmt. Przed pierwszym segmentem `claude auth status` musi
  pokazać połączenie w ramach subskrypcji, bez klucza Console, a `/usage`, które nie zużywa
  żadnego limitu, musi to potwierdzić; każde wywołanie potwierdza to również w swoim
  zdarzeniu inicjalizacyjnym, w przeciwnym razie odpowiedź zostaje odrzucona.
- **Wyłącz „dodatkowe użycie”** (claude.ai, Ustawienia → Użycie), aby
  koszt rzeczywiście pozostał zerowy: gdy ta opcja jest włączona, przejmuje obsługę po wyczerpaniu okna i
  nalicza opłaty bez wyświetlania błędu. aipmt zatrzymuje tłumaczenie, gdy tylko raport
  limitu wywołania to zasygnalizuje, ale samo to wywołanie jest już rozliczone.
- **Limit współdzielony z sesjami Claude Code.** Każde wywołanie raportuje
  wykorzystanie okien 5-godzinnych i tygodniowych; po przekroczeniu 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) nie jest uruchamiany żaden kolejny segment, aby
  nie wyczerpać zasobów potrzebnych do pracy.
- **Izolacja.** Każde wywołanie działa bez narzędzi, w prywatnym,
  jednorazowym katalogu, w trybie bez personalizacji: nie są ładowane ani `CLAUDE.md`, ani pluginy,
  hooki, serwery MCP czy ustawienia, a z sesji nic nie jest zachowywane.
  Załączniki są odcięte: `@chemin` w dokumencie
  pozostaje tekstem i nie otwiera żadnego pliku (zmierzone).
- **Modele**: domyślnie `sonnet`, z poziomem wysiłku `low`, także w `--eco`:
  `--eco` niczego na tej ścieżce nie zmienia. W pomiarach na tych samych dokumentach `haiku`
  jest dwukrotnie wolniejszy — rozumuje, choć nie można mu tego uniemożliwić — przy
  zaledwie nieco niższym koszcie, a `opus` odrzuca treści biologiczne (patrz
  następny punkt). Oba są nadal dostępne przez `--model`; te aliasy wskazują
  najnowszy model z danej rodziny. `fable` i warianty `[1m]` są odrzucane,
  ponieważ wykorzystują płatne środki. `--reasoning_effort` ustawia poziom wysiłku,
  z którego tłumaczenie nie czerpie żadnych korzyści: zmierzony zakres rozumowania jest zerowy lub niemal zerowy.
- **Opus odrzuca niektóre treści biologiczne.** Jego zabezpieczenia są
  bardziej rygorystyczne niż w Sonnet, a komunikat błędu Anthropic ostrzega, że mogą one
  „czasami oznaczać jako podejrzane prace zbliżone do badań biologicznych”. Pomiar: krótka wiadomość
  przeglądowa o 279 wygenerowanych cząsteczkach spowodowała odrzucenie artykułu we wszystkich czternastu
  językach. Nic nie jest zapisywane: aipmt odrzuca uciętą odpowiedź, wskazuje
  zabezpieczenia i zaleca `--model sonnet`.
- Odrzucane w CI (gdy zdefiniowano `CI` lub `GITHUB_ACTIONS`) oraz w systemie Windows (niezmierzone).
- Zmienne: `AIPMT_CLAUDE_BIN` (w przeciwnym razie `PATH`, a następnie `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekundy na segment, domyślnie 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (domyślnie 0.8), `CLAUDE_CONFIG_DIR` (konto
  Claude Code, nigdy niepobierane z projektowego `.env`); katalogi robocze w
  `XDG_CACHE_HOME/aipmt/claude-code` (domyślnie `~/.cache`).

**Warunki użytkowania: odpowiedzialność ponosi Twoje konto.** 
[strona prawna Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nie zabrania „użytkownikowi końcowemu logowania się do niezmodyfikowanego pliku binarnego Claude Code
za pomocą własnej subskrypcji Claude”: właśnie to robi aipmt, który uruchamia
oficjalny plik binarny i nigdy nie odczytuje tokenu. Anthropic jednak „nie zezwala
zewnętrznym deweloperom […] na przekazywanie żądań przy użyciu danych uwierzytelniających planu Free, Pro lub Max
w imieniu ich użytkowników”, preferuje klucz API dla narzędzi
zewnętrznych, „w tym projektów open source”, i zastrzega sobie możliwość odliczania ich
użycia od płatnych środków
([pomoc Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Żaden zapis nie rozstrzyga przypadku dystrybuowanego narzędzia, które uruchamia plik binarny.

**Dane**: na kontach Free, Pro i Max trenowanie modeli
obejmuje również Claude Code, gdy zezwala na to ustawienie prywatności
([strona o danych](https://code.claude.com/docs/en/data-usage)). aipmt nie przechowuje
żadnej lokalnej transkrypcji (`--no-session-persistence`). Nie przesyłaj przez nie
żadnych poufnych informacji.

### Do wybranego dostawcy: `--use_opencode`

[OpenCode](https://opencode.ai) to agent programistyczny open source (MIT), który
kieruje żądania do skonfigurowanych w nim dostawców: przez klucz API, subskrypcję,
bramę OpenCode Zen (bezpłatne modele bez konta) lub model lokalny. Dwie
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

`--model` jest obowiązkowe: bez niego OpenCode przełączyłby się na bezpłatny model,
którego konwersacje mogą służyć do trenowania, a ten wybór nie jest dokonywany
za Ciebie.

Izolacja przy każdym wywołaniu:

- konfiguracja inline, nadrzędna wobec Twojej, definiuje agenta `aipmt`,
  któremu odmówiono dostępu do wszystkich narzędzi (`permission: { "*": "deny" }`), z wyłączonym
  udostępnianiem sesji, `--pure`, nigdy `--auto`;
- jednorazowy, pusty katalog roboczy z ustawionymi `OPENCODE_DISABLE_PROJECT_CONFIG` i
  `OPENCODE_DISABLE_CLAUDE_CODE` — bez nich OpenCode wstrzykuje do
  promptu `AGENTS.md` bieżącego katalogu oraz `~/.claude/CLAUDE.md`. Globalny
  `~/.config/opencode/AGENTS.md` nadal jest wstrzykiwany, ponieważ OpenCode nie pozwala
  go wyłączyć;
- kontrakt wyjściowy: kod zakończenia 0, brak zdarzenia `error`, brak wywołania
  narzędzia, ostatni krok w `stop`, niepusty tekst i faktycznie załadowany agent `aipmt`
  — nieznany `--agent` nie powoduje błędu OpenCode, lecz
  po cichu przełącza go na agenta programistycznego;
- nie jest przekazywany żaden klucz `aipmt` poza `OPENCODE_API_KEY`, kluczem
  samego OpenCode. Dostawców konfiguruje się w OpenCode, a nie w
  `.env` narzędzia `aipmt`.

Warto wiedzieć:

- Bezpłatne modele Zen zmieniają się, mają nieudokumentowane limity, a
  ich konwersacje mogą służyć do trenowania: nadają się do publicznej dokumentacji,
  lecz nie do prywatnych treści.
- Model lokalny musi oferować co najmniej 16 tys. tokenów kontekstu, ponieważ segmenty
  mogą mieć do 16 000 znaków. Ollama często ustawia 4096: należy użyć
  `Modelfile` z `PARAMETER num_ctx 32768`.
- `--eco` nie działa; `--reasoning_effort` jest przekazywane bez zmian jako
  `--variant` OpenCode.
- OpenCode zapisuje dziennik każdej sesji w `~/.local/share/opencode/`.
- Zmienne: `OPENCODE_BIN` (w przeciwnym razie `PATH`, a następnie `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekundy na segment, domyślnie 600). `OPENCODE_CONFIG`
  jest przekazywane bez zmian do OpenCode.

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

`reasoningEffort: "none"` wyłącza rozumowanie, które Ollama domyślnie aktywuje w tych
modelach i którego nie można wyłączyć za pomocą Modelfile. Pomiar na zdaniu złożonym z
sześciu słów: 919 tokenów rozumowania i 68 sekund bez tej opcji, 9 tokenów z nią.

### Do ponad 400 modeli: `--use_openrouter`

OpenRouter to router rozliczany według użycia, korzystający z jednego salda środków i pośredniczący w dostępie do
modeli hostowanych przez podmioty zewnętrzne — w tym otwartych modeli chińskich, których nie
udostępnia tutaj żaden inny dostawca.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` jest obowiązkowe. Preflight, wykonywany przed naliczeniem jakiejkolwiek opłaty, obsługuje
dwie szczególne cechy routingu:

- **Ten sam model jest obsługiwany przez dziesiątki hosterów o różnych
  limitach** — w przypadku `z-ai/glm-5.3-flash` jest to 23 hosterów, w tym jeden z limitem
  2048 tokenów wyjściowych. Preflight odczytuje `/api/v1/models/{modèle}/endpoints`,
  wyklucza hosterów oferujących mniej niż 8000 tokenów wyjściowych lub mających
  obniżony status i przypina pozostałych za pomocą `allow_fallbacks: false`.
- **Rozumowanie jest rozliczane według stawki za dane wyjściowe** — 107 tokenów wobec 2 przy
  odpowiedzi „OK” z `z-ai/glm-5.2`. Domyślnie jest wyłączone; modele,
  które go wymagają, otrzymują najniższy akceptowany poziom wysiłku, ponieważ ustawienie domyślne
  katalogu może wyczerpać limit wyjściowy przed zakończeniem tłumaczenia.
  `--reasoning_effort` zachowuje pierwszeństwo.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Okno kontekstu pochodzi z katalogu. Model oferujący mniej niż 16 400 tokenów jest
  odrzucany przed jakimkolwiek wywołaniem: 8400 na prompt i segment oraz co najmniej
  8000 na dane wyjściowe.
- Brak sluga w katalogu, niedostępność katalogu lub brak
  hostera spełniającego limit powodują zatrzymanie polecenia.
- `finish_reason=length` z pustym wyjściem oznacza budżet zużyty przez
  rozumowanie, a nie ucięcie: komunikat rozróżnia te przypadki.
- `--eco` nie działa.
- Zmienne: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (domyślnie `https://openrouter.ai/api/v1`, wymagane `https://`),
  `OPENROUTER_TIMEOUT` (domyślnie 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (domyślnie 30).

### Nota o tłumaczeniu

`--add_translation_note` dodaje notę w `bottom` (domyślnie), `top` (po
front matter) lub `both` (`--note_position`), w formacie `legacy` (pogrubiony
akapit, domyślnie) albo `marker` (`--note_format`). Format `marker` to
niewidoczna definicja odwołania Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
po której następuje pogrubiony cytat: czytelny na GitHubie i możliwy do wykorzystania podczas buildu przez
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Szczegółowe pomiary

Wszystkie pomiary pochodzą z tłumaczeń rzeczywiście wykonanych przy użyciu `aipmt` na
czternaście języków: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Zapisane** oznacza pliki przepuszczone przez zabezpieczenia; **Bez
rozbieżności** — te, w których `scripts/compare_structure.py` niczego nie wykrywa: tę samą liczbę
sekcji, nagłówków, linków, odrębnych URL-i, bloków kodu,
fragmentów kodu inline, wierszy tabeli, bloków cytatu i pogrubionych słów.

„Bez rozbieżności” oznacza „niczego nie wykryto”, a nie „identyczne”: porównywarka
zlicza elementy, nie odczytując ich treści. Nie wykrywa ani usuniętego nagłówka
poziomu 4, ani zastąpionego tekstu kodu inline, ani zamienionej
flagi, ani wewnętrznego linku wyrenderowanego z jednym nawiasem za dużo,
`[texte]((#ancre))`, który już donikąd nie prowadzi — nie ocenia też
języka.

### Gęsty artykuł przeglądowy, tryb `--news`

Jedno wydanie [przeglądu AI na jls42.org](https://jls42.org/fr/news):
589 wierszy, 140 linków, 21 sekcji, 3 chronione cytaty angielskie. Kampania
z 4 i 5 września 2026 r.

| Model                                           | Dostęp             | Zapisane | Bez rozbieżności | Mediana/język |
| ----------------------------------------------- | ------------------ | -------- | ---------------- | ------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14    | ✅ **14/14**      | 1 min 18 s    |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | subskrypcja Google | 14/14    | ✅ **14/14**      | 3 min 59 s    |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | subskrypcja Google | 14/14    | ✅ **14/14**      | 3 min 14 s    |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14    | ✅ **14/14**      | 3 min 37 s    |
| `gpt-5.6-sol` (`--use_codex`)                   | subskrypcja ChatGPT | 14/14    | ✅ **14/14**      | 11 min 28 s   |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14    | ✅ **14/14**      | 5 min 37 s    |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14    | ✅ **14/14**      | 26 min 23 s   |
| `sonnet` (`--use_claude_code`)                  | subskrypcja Claude | 14/14    | ⚠️ 13/14          | 6 min 49 s    |
| `claude-sonnet-5`                               | API Anthropic      | 14/14    | ⚠️ 11/14          | 6 min 31 s    |
| `haiku` (`--use_claude_code`)                   | subskrypcja Claude | 14/14    | ⚠️ 11/14          | 15 min 54 s   |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14    | ⚠️ 11/14          | 2 min 54 s    |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14    | ⚠️ 7/14           | 6 min 00 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14    | ❌ 11/14          | 9 min 27 s    |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14    | ❌ 8/14           | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`                        | lokalny            | 10/14    | ❌ 7/14           | 12 min 39 s   |
| `mistral-large-latest`                          | API Mistral        | 11/14    | ❌ 5/14           | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14     | ❌ 3/14           | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)                   | subskrypcja Grok   | 1/14     | ❌ 1/14           | 23 min 11 s   |
| `opus` (`--use_claude_code`)                    | subskrypcja Claude | 0/14     | ❌ 0/14           | —             |

Grok został ponownie zmierzony 9 września na innym wydaniu tego samego przeglądu
(356 wierszy): zapisano 9 z 14 języków, z czego 8 bez rozbieżności. To ta liczba
widnieje w tabeli podsumowującej. Nie uwzględniono trzech przerwanych kampanii:
`qwen3.5-27b` (9 języków) i `kimi-k2.6` (4) z powodu braku środków oraz
`z-ai/glm-5.3-flash`, którego dwie awarie wynikały z ustawienia rozumowania
korygowanego od tego czasu przez dostawcę. Wiersze OpenRouter zmierzono przy
domyślnych ustawieniach routera, przed `--use_openrouter`; `z-ai/glm-5.2`,
zmierzony ponownie z dostarczonym providerem, daje ten sam wynik 14/14. Wyniki
przeliczono 10 września za pomocą obecnej porównywarki: `qwen3.8-flash` i
`qwen3.7-flash` zyskują po jednym języku względem pierwszej
publikacji, pozostałe pozostają bez zmian.

Wiersze `--use_antigravity` zmierzono 26 września na tym samym
artykule, z czterema tłumaczeniami równolegle: `gemini-3.7-flash-medium` rano,
`gemini-3.8-flash-medium` po południu. W wersji angielskiej każdy z nich samodzielnie usunął
trzy wiersze francuskiego tłumaczenia pod cytatami, nie wymyślając
flagi, a cytaty angielskie pozostały nienaruszone: awaryjne czyszczenie nie miało
nic do zrobienia. W `--eco` (`gemini-3.7-flash-low`), tylko dla czterech języków
(en, ja, ar, hi): zapisano 4 z 4, wszystkie bez rozbieżności, mediana 1 min 52 s.
Próba kontrolna tego samego dnia na nowszym wydaniu przeglądu,
z 25 września (438 wierszy, 2 cytaty angielskie), przetłumaczonym poza
blogiem przez `gemini-3.7-flash-medium`: zapisano 14 z 14, wszystkie bez rozbieżności, od 87 do
128 s na język.

Wiersze `--use_claude_code` zmierzono 26 września na tym samym
artykule, z czterema tłumaczeniami równolegle i poziomem wysiłku `low`. W przypadku `sonnet`
cytaty angielskie pozostają nienaruszone we wszystkich czternastu językach, a w wersji angielskiej
model samodzielnie usunął wiersze francuskiego tłumaczenia, nie wymyślając
flagi. `opus` nie zapisał żadnego języka: w każdym z nich jego zabezpieczenia
zatrzymały odpowiedź na ostatnim segmencie z powodu krótkiej wiadomości o 279
cząsteczkach wygenerowanych dla miejsca wiązania. Wysłana osobno wiadomość ta jest odrzucana
w kategorii „bio”; `sonnet` przetłumaczył ją wszędzie. `haiku` zapisuje
wszystkie czternaście języków; w trzech z nich (en, pl, ro) nagłówek sekcji zmienia się z
poziomu 2 na poziom 1. Model rozumuje, choć nie można mu tego uniemożliwić — odpowiada to 61%
jego tokenów wyjściowych — stąd ponad dwukrotnie dłuższy czas niż w przypadku `sonnet`.

Wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5`
zmierzono 18 października przez API Anthropic na tym samym artykule, z czterema
równoległymi tłumaczeniami na model. Sonnet 5.5 nie pozwala wyłączyć
rozumowania: aipmt wysyła mu najniższe akceptowane ustawienie, a jego
odpowiedzi nie zawierają żadnych śladów rozumowania. Zapisuje wszystkie czternaście języków bez rozbieżności i bez
ponownego przetwarzania segmentów; w wersji angielskiej samodzielnie usunął wiersze
francuskiego tłumaczenia, nie wymyślając flagi, a cytaty angielskie pozostały
wszędzie nienaruszone. Haiku 5.5 zmierzono z adaptacyjnym rozumowaniem: przy
wyłączonym rozumowaniu pozostawiał całe akapity po francusku, co zabezpieczenie odrzucało —
zapisano 3 z 14 języków. Oba modele Haiku potykają się na tej samej krótkiej wiadomości: Haiku 5.5
zmienia poziom jej nagłówka albo go duplikuje w języku japońskim, koreańskim i
chińskim, Haiku 4.5 zmienia go na poziom 1 w siedmiu językach, a w wersji
japońskiej pozostawia go po francusku. Haiku 4.5 kosztuje 3,67 USD za oba dokumenty we
wszystkich czternastu językach, Haiku 5.5 — 0,57 USD, a Sonnet 5.5 — 9,21 USD.
### README tego projektu, standardowy Markdown

Wersja zamrożona 9 września 2026 r.: 785 wierszy, 285 fragmentów kodu w tekście, 40
zamknięć bloków, 89 wierszy tabel. Cztery tłumaczenia równolegle.

| Model                                           | Wygenerowane | Bez różnic | Mediana/język | Różnice                                                                  |
| ----------------------------------------------- | ------------ | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14        | ✅ 14/14   | 1 min 43 s     | brak                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14        | ✅ 14/14   | 1 min 48 s     | brak                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14        | ✅ 14/14   | 4 min 02 s     | brak według narzędzia porównującego; zduplikowane linki wewnętrzne (en)  |
| `claude-sonnet-5-5`                             | 14/14        | ✅ 14/14   | 1 min 18 s     | brak                                                                     |
| `claude-haiku-4-5`                              | 14/14        | ✅ 14/14   | 2 min 06 s     | brak                                                                     |
| `gemini-3.7-flash`                              | 14/14        | ⚠️ 13/14   | 36 s           | jedno słowo zapisane pogrubieniem (ja)                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14        | ⚠️ 13/14   | 1 min 22 s     | jedno słowo zapisane pogrubieniem (ko)                                   |
| `sonnet` (`--use_claude_code`)                  | 14/14        | ⚠️ 13/14   | 2 min 20 s     | jeden wiersz tabeli sklejony z poprzednim (ar)                           |
| `claude-sonnet-5`                               | 14/14        | ⚠️ 12/14   | 2 min 56 s     | jeden link (sv), jedno słowo zapisane pogrubieniem (zh)                  |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14        | ⚠️ 12/14   | 6 min 46 s     | jedno słowo zapisane pogrubieniem (ar, ja)                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14        | ⚠️ 11/14   | 2 min 34 s     | jedno słowo zapisane pogrubieniem (hi, ja, ko)                           |
| `qwen/qwen3.7-flash`                            | 14/14        | ⚠️ 10/14   | 2 min 17 s     | dodano 40 fragmentów kodu w tekście po arabsku; pogrubienie (hi, ja, ko) |
| `claude-haiku-5-5`                              | 12/14        | ❌ 12/14   | 1 min 14 s     | odmowa dla 2 języków (ar, hi): utrata fragmentów kodu w odpowiedzi       |
| `mistral-large-latest`                          | 14/14        | ❌ 1/14    | 2 min 44 s     | utrata sekcji (ar, hi, ko); dodane bloki kodu (ja, ko, ro, zh)           |

Nie oceniono dwóch przerwanych kampanii: Grok, którego sesja CLI wygasła
po dwunastu językach (jedenaście bez różnic), oraz `qwen3.8-flash`, którego
dostawca zwrócił HTTP 429 po dwóch. `opencode/mimo-v2.5-free` i `ollama/gpt-oss-20b-32k`
nie zostały ponownie zmierzone na tej wersji; w krótszej o 277 wierszy wersji
z 4 i 5 września każdy z nich wygenerował 9 z 14 tłumaczeń, z czego odpowiednio
7 i 1 bez różnic.

Wierszy `--use_antigravity` i `--use_claude_code` nie zmierzono na
zamrożonej wersji, lecz 26 września na wersji opublikowanej wraz z wydaniem 1.14.0 —
natomiast wiersze `claude-sonnet-5-5`, `claude-haiku-5-5` i `claude-haiku-4-5` zmierzono 18
października na tej samej wersji: 600 wierszy, 257 fragmentów kodu w tekście, 30 zamknięć bloków, 85
wierszy tabel. Ponieważ jest ona
krótsza o 185 wierszy, nie można jej porównywać element po elemencie z pozostałymi wierszami;
te wiersze można jednak porównywać między sobą. Jeśli chodzi o linki wewnętrzne, których
narzędzie porównujące nie sprawdza, `gemini-3.8-flash-medium` zachował je bez zmian
we wszystkich czternastu językach, a `gemini-3.7-flash-medium` uszkodził je po włosku;
`sonnet` i `opus` zachowały je bez zmian we wszystkich językach, a `haiku` zduplikował je
po angielsku; `claude-sonnet-5-5` i `claude-haiku-4-5` zachowały je bez zmian we
wszystkich czternastu językach, a `claude-haiku-5-5` w dwunastu, dla których wygenerował tłumaczenia.

### Cztery pliki README znanych projektów

FastAPI, Ollama, tldr-pages i Vue.js, pobrane bez zmian z GitHub — dokumenty
łatwiejsze niż dwa poprzednie. Kampania skupiała się na modelach
mających trudności; Gemini służy w niej jako punkt odniesienia.

| Model                     | Zakres                     | Wygenerowane | Bez różnic   |
| ------------------------- | -------------------------- | ------------ | ------------ |
| `gemini-3.7-flash`        | 4 projekty × 14 języków     | 56/56        | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projekty × 14 języków     | 55/56        | ❌ 47/56     |
| `grok-4.6` (subskrypcja)   | 4 projekty × ar, hi, ja, zh | 16/16        | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projekty × ar, hi, ja, zh | 15/16        | ❌ 9/16      |

### Czym nie są te pomiary

- **Nie są wyczerpującym rankingiem**: sam OpenRouter oferuje ponad czterysta
  modeli, a zmierzono około piętnastu.
- **Czasy są orientacyjne**: zależnie od kampanii wykonywano od trzech do sześciu
  tłumaczeń równolegle, a przepustowość dostawcy zmienia się w ciągu dnia.
- **Są to obserwacje z określonego momentu**: modele zmieniają się pod tą samą nazwą, a Wasze
  dokumenty różnią się od naszych.

Aby powtórzyć pomiar na swoich dokumentach, korzystając z zamrożonej kopii pliku:

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

Opcjonalne, lecz zalecane narzędzia kontroli jakości:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

28 tłumaczeń repozytorium (README i CHANGELOG, czternaście języków) można
wygenerować ponownie za pomocą `./regen_translations.sh --force` — Codex i `gpt-5.6-sol` w ramach
domyślnej subskrypcji ChatGPT, cztery równolegle. `REGEN_PROVIDER` i
`REGEN_MODEL` zmieniają ścieżkę: `antigravity` pozostaje w ramach subskrypcji, tym razem
Google, i działa bez dodatkowego zezwolenia; płatne API (`openai`, `gemini`,
`grok`, `openrouter`) jest odrzucane bez `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` ogranicza czas każdego zadania (600 s, 1 800 s w przypadku Codex i
Antigravity). Szczegóły dotyczące narzędzi znajdują się w `CLAUDE.md`.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** — osobisty blog publikowany w 15 językach. Jego
  [codzienny przegląd wiadomości o AI](https://jls42.org/fr/news) jest codziennie tłumaczony
  za pomocą tego narzędzia i służy jako dokument referencyjny dla powyższych pomiarów.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Ostrzeżenie

Ten program jest rozpowszechniany **bez jakiejkolwiek gwarancji**, zgodnie z
sekcjami 15 i 16 GPL v3: jest dostarczany „w stanie, w jakim się znajduje”, bez gwarancji wartości
handlowej ani przydatności do określonego celu, a jego autor nie może zostać
pociągnięty do odpowiedzialności za szkody wynikające z jego używania. Tekst
licencji ma pierwszeństwo przed niniejszym podsumowaniem.

- **Przeczytajcie ponownie przed publikacją.** Zabezpieczenia obejmują bloki kodu,
  kod w tekście, adresy URL, kotwice i cytaty trybu `--news` — nie obejmują
  nagłówków, tabel, front matter ani znaczenia zdań.
- **Wasze dokumenty są przesyłane do wybranego dostawcy** i podlegają jego warunkom
  użytkowania oraz polityce dotyczącej danych. Niektóre bezpłatne modele mogą
  ponownie wykorzystywać Wasze konwersacje do trenowania, a warunki Antigravity
  pozwalają Google wykorzystywać je ponownie i przekazywać do weryfikacji przez ludzi,
  również w ramach płatnej subskrypcji; model lokalny jest jedynym rozwiązaniem,
  dzięki któremu żadne dane nie opuszczają Waszego komputera.
- **Opłaty za wywołania API ponosicie Wy.** Ten program nie ogranicza
  wydatków: długi dokument, wznowienie po błędzie lub model wykonujący dużo rozumowania
  kosztują więcej.
- **Opublikowane pomiary są obserwacjami z określonego momentu**, a nie gwarancjami.

Nazwy wymienionych produktów i firm należą do ich odpowiednich właścicieli.
Ten projekt nie jest powiązany z żadnym z nich.

**Artykuł przetłumaczony z fr na pl za pomocą gpt-5.6-sol.**
