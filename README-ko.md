# AI 기반 Markdown 번역기

🌍 [프랑스어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [영어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [스페인어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [중국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [독일어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [일본어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [아랍어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [힌디어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [이탈리아어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [네덜란드어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [폴란드어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [포르투갈어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [루마니아어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [스웨덴어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 코드 품질</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="품질 게이트 상태"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="보안 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="신뢰성 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="유지보수성 등급"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="커버리지"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="취약점"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="버그"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 스멜"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복된 줄 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 줄 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

코드 블록, 인라인 코드, URL, 앵커, 표, front matter 등의 구조를
보존하면서 Markdown 파일을 한 언어에서 다른 언어로 번역합니다.
모델을 호출하는 아홉 가지 방법으로 다섯 개의 API, 사용량별 과금이
없는 두 개의 구독, 두 개의 라우터를 제공하며, 각 모델이 실제로
무엇을 보존하는지 측정한 결과도 공개합니다.

## 요약

- **아홉 가지 provider 경로**: OpenAI, Mistral, Claude, Gemini, Grok API,
  사용량별 과금이 없는 ChatGPT(Codex) 및 Grok 구독, OpenCode(오픈 소스,
  무료 또는 로컬) 및 OpenRouter(400개 이상의 모델) 라우터.
- **토큰 하나를 잃어 잘못된 결과를 만들지 않음**: 코드 블록, 인라인
  코드, URL, 앵커, 인용문을 호출 전에 토큰으로 대체하고 반환 시
  검증합니다. 하나라도 누락되면 파일을 쓰지 않습니다.
- **긴 문서**: 모델의 컨텍스트 창에 맞게 분할합니다.
- **`--news` 모드**: 모니터링 기사에 맞게 영어 인용문을 보호하고
  언어별 국기를 처리합니다.
- **`--eco` 모드**: 더 빠르고 저렴한 모델을 사용합니다.
- 선택 사항인 **번역 참고문**을 위쪽, 아래쪽 또는 양쪽에 추가합니다.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 이상이 필요합니다. 저장소에서 설치하려면
[기여하기](#기여하기)를 참조하세요.

## 구성

키는 우선순위가 높은 순서대로 세 위치에서 읽으며, 각 위치는 앞선
위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일시적인 재정의 |
| 2   | 현재 디렉터리 또는 상위 디렉터리의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | 한 번 설치하면 어디서나 적용       |

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

`GOOGLE_API_KEY` 대신 `GEMINI_API_KEY`도 사용할 수 있습니다. 사용자 파일은
`XDG_CONFIG_HOME`(절대 경로만 허용)을 따르며 Windows에서는 `%APPDATA%`도
따릅니다. 키가 없으면 명령이 세 위치를 나열합니다.

**프로젝트의 `.env`는 호출을 다른 곳으로 리디렉션할 수 없습니다.**
이 파일은 키만 제공하며 목적지는 절대 지정하지 않습니다. `_BASE_URL`,
`_API_BASE` 또는 `_ENDPOINT` 형식의 모든 변수, 프록시
(`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), 인증서 저장소
(`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), 그리고
`XDG_CONFIG_HOME` / `APPDATA`는 경고와 함께 무시됩니다. 복제한 저장소가
사용자의 키를 가로챌 수 없어야 하기 때문입니다. 또한 이 파일은 보간
없이 읽히므로 `NOM=${OPENAI_API_KEY}`가 키를 복사하지 않습니다. 이러한 변수는
환경이나 `~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT`(호출당 초, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(기본값 600), `GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`),
`GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(기본값 600), `OPENROUTER_BASE_URL`(`https://` 필수), `OPENROUTER_TIMEOUT`
(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각 변수는 해당 provider
섹션에서 자세히 설명합니다.

## 시작하기

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`를 스페인어로 번역하면 `--target_dir`에 `document-es.md`가
생성되고, `--include_model`를 사용하면 `document-es-gpt-5.6-terra.md`가 생성됩니다. 확장자는
항상 `.md`가 되므로 `article.mdx`는 `article-en.md`가 됩니다.
단, `--keep_filename`을 사용하면 원래 이름을 유지합니다. 이미 번역이
존재하면 `--force` 없이는 건너뜁니다.

종료 코드: 모든 작업이 완료되었거나 건너뛰어졌으면 `0`,
실패한 파일이 남아 있으면 `1`(표준 오류에 목록 출력),
구성에 문제가 있으면 `2`입니다. 실패한 파일은 쓰기 자체가
실패한 경우에도 절대 기록되지 않습니다. 내용을 옆에 별도로 쓴 다음
이름을 바꾸기 때문입니다. 다시 실행하기만 하면 됩니다.

## 어떤 모델을 선택할 것인가

실제 문서 두 개를 각 모델로 동일한 열네 개 언어로 번역해 측정했습니다.
**수치는 열네 개 언어 중 번역 파일이 작성되고 원본과 다른 부분이
전혀 없는 언어의 수입니다.**

| 모델               | 이용 방법                 | 밀도 높은 모니터링 기사 | 이 README    | 차이가 있는 부분과 해당 언어 수                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API 키                    | ✅ 14/14                | ⚠️ 13/14     | 14개 언어 중 1개: 굵게 표시된 단어 하나 추가(ja)                                                                                         |
| **GPT-5.6 Sol**      | ChatGPT 구독 또는 OpenAI 키 | ✅ 14/14                | ⚠️ 12/14     | 14개 언어 중 2개: 굵게 표시된 단어 하나 누락(ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter 키                    | ✅ 14/14                | ⚠️ 11/14     | 14개 언어 중 3개: 굵게 표시된 단어 하나 누락(hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic API 키                 | ⚠️ 11/14                | ⚠️ 12/14     | 기사에서 3개 언어: 코드 블록 하나가 추가됨(es, de, hi), 이 README에서 2개 언어: 마크업이 없는 링크 하나(sv), 굵게 표시된 단어 하나(zh) |
| Qwen 3.7 Flash       | OpenRouter 키                    | ❌ 8/14                 | ⚠️ 10/14     | 기사에서 1개 언어가 거부되고 다른 5개가 달라짐. 이 README에서는 약 40개 단어가 `code`로 표시됨(ar)                       |
| Grok 4.6             | Grok 구독                   | ❌ 8/14                 | 평가되지 않음     | 반환된 인라인 코드와 URL이 누락되어 14개 중 5개 언어가 거부됨. 네덜란드어는 전체적으로 다름                                  |
| GPT-OSS 20B          | 로컬 모델(Ollama)             | ❌ 7/14                 | 재측정되지 않음 | 14개 중 4개 언어가 거부됨. 모델이 프랑스어 구절을 남겨 두어 보호 장치가 중단함                                     |
| MiMo v2.5(무료)  | 계정 없는 OpenCode Zen         | ❌ 11/14                | 재측정되지 않음 | 1개 언어가 거부되고 폴란드어에서 섹션 하나가 누락됨                                                                                     |
| Mistral Large        | Mistral API 키                   | ❌ 5/14                 | ❌ 1/14      | **섹션 전체가 사라짐**: 기사에서 1개 언어(hi), 이 README에서 3개 언어(ar, hi, ko). 기사에서는 3개 언어도 거부됨   |
| DeepSeek V4 Flash    | OpenRouter 키                    | ❌ 3/14                 | 재측정되지 않음 | 14개 중 10개 언어가 거부됨. 언어당 37분 소요                                                                                    |

|     | 기호의 의미                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 열네 개 언어가 모두 번역되었고 원본과 다른 부분이 전혀 없음                                                                                                                                       |
| ⚠️  | 열네 개 언어가 모두 번역됨. 차이가 있는 부분은 굵게 표시된 단어, `code`, 대괄호가 사라진 링크 같은 **마크업**뿐임. 텍스트, URL, 코드 블록, 섹션은 하나도 누락되지 않음 |
| ❌  | 하나 이상의 언어를 번역하지 못해 파일이 거부되고 작성되지 **않았거나**, 작성된 파일에서 콘텐츠가 누락됨                                                                      |

여기서 기억해야 할 점은 다음과 같습니다.

- **거부된 번역은 손상된 번역이 아닙니다.** 반환 시 토큰이 누락되면 파일을
  쓰지 않고 해당 언어를 거부된 것으로 계산합니다. Grok이 기사에서 보이는
  현상이 바로 이것입니다. 라틴 문자를 사용하지 않는 다섯 언어에서 첫 번째
  세그먼트부터 인라인 코드 네 개와 URL 세 개가 누락되었습니다.
- **이 안전망은 제목, 표, front matter 또는 텍스트를 보호하지 않습니다.**
  모델이 섹션을 삭제해도 도구는 아무 문제 없이 파일을 씁니다. Mistral이
  바로 이러한 경우입니다. 이런 요소는 토큰으로 대체할 수 없고 현재
  보호 장치도 이를 검사하지 않습니다. `scripts/compare_structure.py`는 누락된 섹션을
  감지하지만 사후에만 가능합니다.
- **Grok은 이 README에 대한 평가가 없습니다.** CLI 세션이 열두 개
  언어를 처리한 뒤 만료되었으며 그중 열한 개에는 차이가 없었습니다.
  중단된 측정에는 점수를 매기지 않습니다.
- **언어보다 문서의 밀도가 더 중요합니다.** Grok은 일반적인 README는
  처리하지만 링크가 많은 기사에서는 문제가 발생하며 네덜란드어도
  예외가 아닙니다.

날짜와 문서: ‘이 README’ 열은 2026년 9월 9일에 이 파일의 고정된
리비전(785줄, 인라인 코드 285개, 표 89줄)을 대상으로 측정했으며 이후
파일이 수정되었습니다. ‘밀도 높은 모니터링 기사’ 열은 589줄 분량의
기사를 대상으로 9월 4일과 5일에 수행한 측정 결과입니다. 단, Grok 행은
동일한 모니터링 기사의 다른 판본으로 9월 9일에 다시 측정했습니다.
전체 표, 소요 시간 및 프로토콜은
[상세 측정 결과](#상세-측정-결과)에 있습니다.

## 모든 옵션

| 옵션                   | 설명                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일(`--source_dir`의 대안)                                             |
| `--source_dir`           | Markdown 파일이 들어 있는 소스 디렉터리(기본값: `content/posts`)                                   |
| `--target_dir`           | 번역된 파일의 출력 디렉터리(기본값: `traductions_en`)                                    |
| `--source_lang`          | 원본 언어(기본값: `fr`)                                                                                  |
| `--target_lang`          | 대상 언어(기본값: `en`)                                                                                   |
| `--model`                | 사용할 특정 모델                                                                                  |
| `--eco`                  | 경제형 모델 사용                                                                              |
| `--use_mistral`          | Mistral AI API 사용                                                                                     |
| `--use_claude`           | Claude API 사용                                                                                         |
| `--use_gemini`           | Gemini API 사용                                                                                         |
| `--use_grok`             | xAI API(Grok) 사용 — `XAI_API_KEY` 필요                                                           |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용                                                    |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                                                        |
| `--use_opencode`         | OpenCode에서 구성한 provider로 OpenCode(오픈 소스) 사용. `--model provider/modèle` 필요 |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                          |
| `--force`                | 강제로 다시 번역                                                                                       |
| `--keep_filename`        | 원래 파일 이름 유지                                                                          |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 국기를 처리                                      |
| `--add_translation_note` | 번역 참고문 추가                                                                                |
| `--note_position`        | 참고문 위치: `top`, `bottom`(기본값) 또는 `both`                                                     |
| `--note_format`          | 참고문 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 노력 수준: `none`/`low`/`medium`/`high`/`xhigh`                                         |

여덟 개의 `--use_*` 플래그는 상호 배타적이므로 두 개를 함께 사용하면
거부됩니다.

## Provider

### API 사용: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`을 사용하면 각 provider의 경제형 등급으로 전환됩니다.

| Provider   | 고품질(기본값)                                      | 경제형(`--eco`)      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`(`--model`을 통해 `terra` 및 `luna`도 지원) | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` 필수                 | 동일 — `--eco`은 효과 없음 |
| OpenRouter | `--model fournisseur/modèle` 필수              | 동일 — `--eco`은 효과 없음 |
### ChatGPT 구독 사용: `--use_codex`

공식 Codex CLI를 구동합니다. 번역 사용량은 API 키나 사용량 기반 요금 청구 없이 ChatGPT 구독 할당량에서 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 바이너리는 `CODEX_BIN`, 그다음 `PATH`, 그다음 `openai-codex-cli-bin` package 순서로 검색됩니다. `~/.codex/auth.json`은 절대 읽지 않습니다.
- `OPENAI_API_KEY`과 `CODEX_API_KEY`은 하위 프로세스 환경에서 제거됩니다. 키가 존재해도 API로 전환되지 않습니다.
- 각 세그먼트에는 5시간 한도에서 최소 한 개의 « 메시지 »가 소모되며, 검증에 실패해 재시도하면 두 개가 소모됩니다. OpenAI가 제시하는 추정치는 Plus 플랜에서 `gpt-5.6-luna` (`--eco`)의 경우 250-2 000개 메시지/5 h, `gpt-5.6-sol`의 경우 10-100개입니다.
- `--model gpt-5.6-terra`과 `--model gpt-5.6-luna`도 구독을 통해 처리됩니다. 계정에 사용 권한이 없는 모델은 400 « model is not supported when using Codex with a ChatGPT account »를 반환합니다.
- API보다 느리며 문서가 길어질수록 격차가 커집니다. 이 README에서는 `gpt-5.6-sol`이 언어당 중앙값 6 min 46 s인 반면, `gemini-3.7-flash`는 36 s입니다.
- CI에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS`이 설정된 경우). 구독은 개인 세션 파일로 인증되므로 공유 runner에 두어서는 안 됩니다.
- 변수: `CODEX_BIN`, `CODEX_TIMEOUT`(세그먼트당 초, 기본값 600).

### Grok 구독 사용: `--use_grok_cli`

SuperGrok 또는 X Premium+ 구독에서 공식 Grok Build CLI를 사용하는 동일한 방식입니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex보다 약한 격리.** Grok의 OS sandbox는 최근의 많은 Linux 환경에서 적용되지 않으며(AppArmor, 컨테이너 runtime socket), 적용할 수 없는 프로필은 아무런 알림 없이 격리되지 않은 상태로 시작됩니다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않고 이를 알리며, 시작을 거부하는 catch-all `*`을 포함한 CLI의 `--deny` 규칙에 의존합니다. 이는 보호 기능을 알리지 않고 제거하는 대신 시작을 거부하는 유일한 계층입니다. `GROK_TRANSLATE_SANDBOX=read-only`은 OS sandbox를 요구하며, 시스템이 이를 준수할 수 없으면 시작에 실패합니다.
- 할당량은 주 단위이며 Chat, Imagine, Voice와 공유되고 이를 조회할 수 있는 명령도 없습니다. 따라서 일괄 작업이 아무런 신호 없이 대화용 사용량을 소모할 수 있습니다.
- 변수: `GROK_BIN`, `GROK_HOME`(CLI 디렉터리, 기본값 `~/.grok`), `GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`.

### 원하는 공급자 사용: `--use_opencode`

[OpenCode](https://opencode.ai)는 내부에 구성된 공급자로 요청을 전달하는 open source(MIT) 코딩 agent입니다. API 키, 구독, OpenCode Zen gateway(계정 없이 사용하는 무료 모델) 또는 로컬 모델을 사용할 수 있습니다. 여기에서는 Zen과 Ollama 두 경로를 처음부터 끝까지 측정했습니다.

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

`--model`은 필수입니다. 이것이 없으면 OpenCode가 대화 내용을 학습에 사용할 수 있는 무료 모델로 되돌아갈 수 있으므로, 이 선택을 대신 결정하지 않습니다.

각 호출의 격리 방식:

- 사용자 구성보다 우선하는 inline 구성이 모든 도구를 거부하는(`permission: { "*": "deny" }`) `aipmt` agent를 정의하고, 세션 공유를 비활성화하며, `--pure`만 사용하고 `--auto`은 절대 사용하지 않습니다.
- 비어 있는 일회용 작업 디렉터리에 `OPENCODE_DISABLE_PROJECT_CONFIG`와 `OPENCODE_DISABLE_CLAUDE_CODE`을 설정합니다. 이렇게 하지 않으면 OpenCode가 현재 디렉터리의 `AGENTS.md`과 `~/.claude/CLAUDE.md`을 prompt에 삽입합니다. 전역 `~/.config/opencode/AGENTS.md`은 계속 삽입되며 OpenCode에서는 이를 제외할 수 없습니다.
- 출력 계약은 반환 코드 0, `error` 이벤트 없음, 도구 호출 없음, 마지막 단계가 `stop`일 것, 비어 있지 않은 텍스트, 그리고 `aipmt` agent가 실제로 로드되었을 것을 요구합니다. 알 수 없는 `--agent` 때문에 OpenCode가 실패하지는 않으며 아무런 알림 없이 코딩 agent로 되돌아갑니다.
- `OPENCODE_API_KEY`인 OpenCode 자체 키를 제외한 어떤 `aipmt` 키도 전달하지 않습니다. 공급자는 `aipmt`의 `.env`이 아니라 OpenCode에서 구성합니다.

알아둘 사항:

- Zen의 무료 모델은 수시로 변경되고 한도가 문서화되어 있지 않으며 대화 내용이 학습에 사용될 수 있습니다. 공개 문서에는 사용할 수 있지만 비공개 콘텐츠에는 적합하지 않습니다.
- 세그먼트가 최대 16 000자이므로 로컬 모델은 최소 16 k token의 context를 제공해야 합니다. Ollama는 이를 흔히 4 096으로 설정하므로 `PARAMETER num_ctx 32768`이 포함된 `Modelfile`을 사용해야 합니다.
- `--eco`은 효과가 없으며, `--reasoning_effort`은 OpenCode의 `--variant`으로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 변수: `OPENCODE_BIN`(없으면 `PATH`, 그다음 `~/.opencode/bin/opencode`), `OPENCODE_TIMEOUT`(세그먼트당 초, 기본값 600). `OPENCODE_CONFIG`은 OpenCode에 그대로 전달됩니다.

`~/.config/opencode/opencode.json`에서 Ollama를 통해 로컬 모델을 사용하는 예:

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

`reasoningEffort: "none"`은 Ollama가 이러한 모델에서 기본적으로 활성화하며 Modelfile로는 비활성화할 수 없는 추론을 끕니다. 여섯 단어로 된 문장에서 측정한 결과, 옵션이 없으면 추론에 919 token과 68초가 소요되었지만 옵션을 사용하면 9 token이 소요되었습니다.

### 400개 이상의 모델 사용: `--use_openrouter`

OpenRouter는 단일 크레딧을 기반으로 사용량에 따라 요금이 청구되는 router로, 제3자가 호스팅하는 모델에 연결합니다. 여기에는 이곳의 다른 어떤 provider도 제공하지 않는 중국산 open model도 포함됩니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`은 필수입니다. 요금이 청구되기 전에 실행되는 preflight가 routing의 두 가지 특성을 처리합니다.

- **동일한 모델이 서로 다른 상한을 가진 수십 개의 호스팅 업체에서 제공됩니다.** `z-ai/glm-5.3-flash`의 경우 호스팅 업체가 23곳이며, 그중 한 곳은 출력이 2 048 token으로 제한됩니다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽고 출력 한도가 8 000 token 미만이거나 상태가 저하된 호스팅 업체를 제외한 뒤, 나머지를 `allow_fallbacks: false`로 고정합니다.
- **추론은 출력 요율로 청구됩니다.** `z-ai/glm-5.2`의 « OK » 응답에서는 추론 token이 107개, 출력 token이 2개였습니다. 추론은 기본적으로 꺼집니다. 추론을 강제하는 모델에는 해당 모델이 허용하는 가장 낮은 effort가 지정됩니다. catalog 기본값을 사용하면 번역이 끝나기 전에 출력 한도를 모두 소모할 수 있습니다. `--reasoning_effort`이 계속 우선합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- context window는 catalog에서 가져옵니다. 16 400 token 미만인 모델은 호출 전에 거부됩니다. prompt와 세그먼트에 8 400 token, 출력에 최소 8 000 token이 필요합니다.
- catalog에 없는 slug, 접근할 수 없는 catalog 또는 상한을 충족하는 호스팅 업체의 부재는 명령을 중단시킵니다.
- 출력이 비어 있는 `finish_reason=length`은 잘림이 아니라 추론에 소모된 예산이며, 메시지에서 이를 구분합니다.
- `--eco`은 효과가 없습니다.
- 변수: `OPENROUTER_API_KEY`(<https://openrouter.ai/keys>), `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30).

### 번역 안내문

`--add_translation_note`은 `bottom`(기본값), `top`(front matter 다음) 또는 `both`(`--note_position`) 위치에 `legacy` 형식(굵은 문단, 기본값)이나 `marker` 형식(`--note_format`)으로 안내문을 추가합니다. `marker` 형식은 보이지 않는 Markdown 참조 정의인 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` 뒤에 굵은 인용문을 붙인 형태입니다. GitHub에서 읽을 수 있고 build 시 remark plugin으로 처리할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정 결과

모든 측정은 `aipmt`을 사용해 en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi의 14개 언어로 실제 번역을 실행한 결과입니다. **작성됨**은 보호 검사를 통과한 파일 수이고, **차이 없음**은 `scripts/compare_structure.py`에서 차이가 발견되지 않은 파일 수입니다. 즉, section, 소제목, link, 고유 URL, code block, inline code, 표의 행, 인용 block 및 굵은 단어의 수가 동일한 경우입니다.

« 차이 없음 »은 « 발견된 차이가 없음 »을 뜻하며 « 동일함 »을 뜻하지는 않습니다. 비교기는 요소의 내용을 읽지 않고 개수만 셉니다. 삭제된 4단계 제목, 바뀐 inline code 텍스트 또는 서로 뒤바뀐 flag는 감지하지 못하며 언어도 판정하지 않습니다.

### 밀도 높은 동향 기사, `--news` 모드

[jls42.org의 AI 동향](https://jls42.org/fr/news) 한 호를 사용했습니다. 589줄, link 140개, section 21개, 보호된 영어 인용문 3개로 구성되며 2026년 9월 4일과 5일에 측정했습니다.

| 모델                            | 접근 방식              | 작성됨 | 차이 없음   | 언어당 중앙값 |
| --------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT 구독 | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                 | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | 로컬              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`            | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | Grok 구독    | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok는 9월 9일 동일한 동향의 다른 호(356줄)에서 다시 측정했으며, 14개 언어 중 9개가 작성되고 8개는 차이가 없었습니다. 상단 표에는 이 수치가 기재되어 있습니다. 중단된 세 차례의 측정은 포함하지 않았습니다. `qwen3.5-27b`은 9개 언어, `kimi-k2.6`은 4개 언어에서 크레딧이 소진되었고, `z-ai/glm-5.3-flash`의 두 차례 실패는 provider가 이후 수정한 추론 설정 때문이었습니다. OpenRouter 행은 `--use_openrouter` 이전에 router의 기본 설정으로 측정했습니다. 제공되는 provider를 사용해 다시 측정한 `z-ai/glm-5.2`도 동일하게 14/14를 기록했습니다. 수치는 현재 비교기를 사용해 9월 10일에 다시 계산했습니다. `qwen3.8-flash`과 `qwen3.7-flash`은 최초 공개 결과보다 각각 한 개 언어가 늘었고 나머지는 변하지 않았습니다.

### 이 프로젝트의 README, 표준 Markdown

2026년 9월 9일에 고정한 개정판입니다. 785줄, inline code 285개, block fence 40개, 표 행 89개이며 번역 네 개를 병렬로 실행했습니다.

| 모델                        | 작성됨 | 차이 없음 | 언어당 중앙값 | 차이점                                                           |
| ----------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14   | 36 s           | 굵은 단어 하나(ja)                                                      |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14   | 2 min 56 s     | link 하나(sv), 굵은 단어 하나(zh)                                        |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 굵은 단어 하나(ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 굵은 단어 하나(hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 아랍어에 inline code 40개 추가, 굵은 글씨(hi, ja, ko)                   |
| `mistral-large-latest`        | 14/14   | ❌ 1/14    | 2 min 44 s     | section 하나 누락(ar, hi, ko), code block 추가(ja, ko, ro, zh) |

중단된 두 차례의 측정은 포함하지 않았습니다. Grok는 12개 언어를 처리한 뒤 CLI 세션이 만료되었고 그중 11개는 차이가 없었으며, `qwen3.8-flash`은 두 개를 처리한 뒤 호스팅 업체가 HTTP 429를 반환했습니다. `opencode/mimo-v2.5-free`과 `ollama/gpt-oss-20b-32k`은 이 개정판에서 다시 측정하지 않았습니다. 277줄 더 짧았던 9월 4일과 5일 개정판에서는 각각 14개 중 9개의 번역을 작성했으며, 차이가 없는 번역은 각각 7개와 1개였습니다.

### 잘 알려진 네 프로젝트의 README

GitHub에 있는 FastAPI, Ollama, tldr-pages, Vue.js를 그대로 사용했습니다. 앞선 두 문서보다 쉬운 문서들입니다. 이 측정은 어려움을 겪은 모델을 대상으로 했으며, Gemini는 비교 기준으로 사용했습니다.

| 모델                    | 범위                  | 작성됨 | 차이 없음   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 프로젝트 4개 × 언어 14개     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 프로젝트 4개 × 언어 14개     | 55/56   | ❌ 47/56     |
| `grok-4.6` (구독)   | 프로젝트 4개 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 프로젝트 4개 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 이 측정 결과가 의미하지 않는 것

- **포괄적인 순위가 아닙니다.** OpenRouter만 해도 400개가 넘는 모델을 제공하지만 측정한 모델은 약 15개입니다.
- **소요 시간은 참고치입니다.** 측정에 따라 번역 세 개에서 여섯 개를 병렬로 실행했으며, 공급자의 처리량은 하루 중에도 달라집니다.
- **특정 시점의 관찰 결과입니다.** 같은 이름의 모델도 변경되며, 사용자의 문서는 이 측정에 사용한 문서와 다릅니다.

사용자 문서로 다시 측정하려면 고정된 파일 복사본에서 다음을 실행하십시오.

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## 기여하기

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

두 줄 모두 필요합니다. `pip install -e .`이 없으면 `python -m aipmt`이 `No module named aipmt`으로 응답합니다.

선택 사항이지만 권장하는 품질 관리 도구:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 번역 28개(README와 CHANGELOG, 14개 언어)는 `./regen_translations.sh --force`으로 다시 생성할 수 있습니다. 기본적으로 ChatGPT 구독의 Codex와 `gpt-5.6-sol`을 사용하며 네 개를 병렬로 실행합니다. `REGEN_PROVIDER`과 `REGEN_MODEL`은 경로를 변경합니다. 유료 API(`openai`, `gemini`, `grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다. `REGEN_JOB_TIMEOUT`은 각 job의 시간을 제한합니다(Codex에서는 600 s, 1 800 s). 도구에 대한 자세한 내용은 `CLAUDE.md`에 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 게시되는 개인 blog입니다. 이 사이트의 [일일 AI 동향](https://jls42.org/fr/news)은 매일 이 도구로 번역되며 위 측정의 참조 문서로 사용됩니다.

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하십시오.

## 경고

이 프로그램은 GPL v3의 section 15와 16에 따라 **어떠한 보증도 없이** 배포됩니다. 상품성이나 특정 용도 적합성에 대한 보증 없이 « 있는 그대로 » 제공되며, 작성자는 이 프로그램의 사용으로 발생한 손해에 책임을 지지 않습니다. 이 요약보다 라이선스 원문이 우선합니다.

- **게시하기 전에 검토하십시오.** 보호 기능은 `--news` 모드의 code block, inline code, URL, anchor 및 인용문을 보호하지만 제목, 표, front matter 또는 문장의 의미는 보호하지 않습니다.
- **문서는 선택한 공급자에게 전송되며**, 해당 공급자의 이용 약관과 데이터 정책이 적용됩니다. 일부 무료 모델은 대화 내용을 학습에 재사용할 수 있습니다. 로컬 모델만이 사용자 시스템 밖으로 데이터를 전혀 내보내지 않는 유일한 방법입니다.
- **API 호출에는 요금이 청구됩니다.** 이 프로그램은 지출 상한을 설정하지 않습니다. 긴 문서, 실패 후 재시도 또는 추론을 많이 하는 모델은 비용이 더 많이 듭니다.
- **공개된 측정 결과는 특정 시점의 관찰 결과이며**, 보증이 아닙니다.

언급된 제품명과 회사명은 각 소유자의 자산입니다. 이 프로젝트는 그 어느 곳과도 제휴하지 않습니다.

**gpt-5.6-sol을 사용하여 프랑스어에서 한국어로 번역된 기사.**
