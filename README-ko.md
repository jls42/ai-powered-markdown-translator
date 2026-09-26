# AI 기반 Markdown 번역기

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복 라인 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 라인 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

코드 블록, 인라인 코드, URL, 앵커, 표, 프론트 매터(front matter) 등의
구조를 보존하면서 Markdown 파일을 한 언어에서 다른 언어로 번역합니다.
모델을 호출하는 10가지 방법(API 5종, 종량제 과금 없는 구독 3종, 라우터
2종)과 각 모델이 실제로 무엇을 보존하는지에 대한 공개된 측정 결과를
제공합니다.

## 주요 특징

- **10가지 프로바이더 경로**: OpenAI, Mistral, Claude, Gemini, Grok API;
  종량제 과금 없는 ChatGPT(Codex), Grok, Google(Antigravity) 구독;
  OpenCode(오픈 소스, 무료 또는 로컬) 및 OpenRouter(400개 이상의 모델)
  라우터.
- **토큰 누락으로 인한 오류 방지**: 호출 전에 코드 블록, 인라인 코드,
  URL, 앵커, 인용문을 토큰으로 대체하고 반환 시 검증합니다. 하나라도
  누락되면 파일이 작성되지 않습니다.
- **긴 문서 처리**: 모델의 컨텍스트 윈도우에 따른 자동 분할.
- **`--news` 모드**: 모니터링/뉴스 기사를 위해 영어 인용문을 보호하고
  언어별 플래그를 관리합니다.
- **`--eco` 모드**: 빠르고 경제적인 모델 사용.
- 상단, 하단 또는 양쪽 모두에 선택적인 **번역 알림** 추가 가능.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 이상. 저장소에서 직접 설치하는 방법은
[기여하기](#기여하기)를 참조하세요.

## 설정

키는 우선순위가 높은 순서대로 다음 세 위치에서 읽어오며, 각 위치는 이전
위치에서 비어 있는 항목만 채웁니다.

|     | 위치                                          | 용도                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                                     | CI, 컨테이너, 일회성 재정의           |
| 2   | 현재(또는 상위) 디렉터리의 `.env`     | 프로젝트별 전용 키                    |
| 3   | `~/.config/aipmt/.env`                                 | 한 번 설치하면 어디서나 적용          |

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
`XDG_CONFIG_HOME`(절대 경로만 지원)을 따르며 Windows에서는 `%APPDATA%`을
따릅니다. 키가 설정되어 있지 않으면 명령어가 세 위치를 나열합니다.

**프로젝트의 `.env` 파일은 호출을 리디렉션하거나 실행할 프로그램을 선택할 수 없습니다.**
키만 제공할 뿐 대상(destination)이나 바이너리는 제공하지 않습니다. `_BASE_URL`,
`_API_BASE`, `_ENDPOINT`, `_BIN`(`CODEX_BIN`, `GROK_BIN`,
`OPENCODE_BIN`, `AGY_BIN`)로 끝나는 모든 변수, `GROK_HOME`,
프록시(`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), 인증서 저장소(`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), `XDG_CONFIG_HOME` / `APPDATA`은
경고와 함께 무시됩니다. 복제(clone)된 저장소가 사용자의 키를 가로채거나
첫 번역 시 자체 프로그램을 실행하도록 유도해서는 안 되기 때문입니다. 이
파일은 변수 보간(interpolation) 없이 읽히므로 `NOM=${OPENAI_API_KEY}`가 키를 복사하지
않습니다. 이러한 변수들은 환경 변수나 `~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(호출당
초 단위, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`(기본값 600),
`GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`), `GROK_TIMEOUT`(기본값
900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT`(기본값 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT`(기본값 600), `OPENROUTER_BASE_URL`(`https://`
필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각 변수는
해당 프로바이더 섹션에 자세히 설명되어 있습니다.

## 시작하기

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`를 스페인어로 번역하면 `--target_dir` 안에 `document-es.md`가
생성되며, `--include_model`를 사용하면 `document-es-gpt-5.6-terra.md`가 됩니다. 확장자는 항상
`.md`로 변경됩니다(예: `article.mdx`는 `article-en.md`가 됨).
단, 원래 파일명을 유지하는 `--keep_filename`를 사용할 때는 예외입니다. 이미 번역본이
존재하는 경우 `--force` 옵션이 없으면 건너뜁니다.

종료 코드: 모두 성공하거나 건너뛴 경우 `0`, 실패한 파일이 남아 있는
경우 `1`(표준 에러로 목록 출력), 설정에 문제가 있는 경우 `2`입니다.
실패한 파일은 결코 디스크에 기록되지 않으며, 파일 쓰기 자체가 실패하더라도 안전합니다.
내용은 임시 파일로 작성된 후 이름이 변경되기 때문입니다. 다시 실행하기만 하면 됩니다.

## 어떤 모델을 선택해야 할까

실제 문서 2개를 각 모델을 통해 동일한 14개 언어로 번역하여 측정한 결과입니다.
**숫자는 14개 언어 중 번역이 작성되었고 원본과 어떠한 형식 차이도 발생하지 않은 언어의 수입니다.**

| 모델                 | 접근 방법                         | 조밀한 모니터링 기사   | 이 README    | 차이점 및 해당 언어 수                                                                                                               |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google 구독 (Antigravity)         | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 차이 없음                                                                                                                |
| **Gemini 3.7 Flash** | Google API 키                     | ✅ 14/14                | ⚠️ 13/14     | 14개 중 1개 언어: 굵은 글씨 단어 1개 추가 (ja)                                                                                        |
| **Gemini 3.7 Flash** | Google 구독 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14개 중 1개 언어: 굵은 글씨 단어 1개 누락 (ko)                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT 구독 또는 OpenAI 키       | ✅ 14/14                | ⚠️ 12/14     | 14개 중 2개 언어: 굵은 글씨 단어 1개 누락 (ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter 키                     | ✅ 14/14                | ⚠️ 11/14     | 14개 중 3개 언어: 굵은 글씨 단어 1개 누락 (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic API 키                  | ⚠️ 11/14                | ⚠️ 12/14     | 기사에서 3개 언어: 코드 블록 추가됨 (es, de, hi); 이 README에서 2개 언어: 마크업 없는 링크 (sv), 굵은 글씨 단어 (zh)                  |
| Qwen 3.7 Flash       | OpenRouter 키                     | ❌ 8/14                 | ⚠️ 10/14     | 기사에서 1개 언어 거부됨, 다른 5개 언어에서 차이 발생; 이 README에서 약 40개 단어가 `code` 처리됨 (ar)                        |
| Grok 4.6             | Grok 구독                         | ❌ 8/14                 | 측정되지 않음| 14개 중 5개 언어 거부됨(인라인 코드 및 URL 누락으로 반환됨); 네덜란드어는 전체적으로 차이 발생                                       |
| GPT-OSS 20B          | 로컬 모델 (Ollama)                | ❌ 7/14                 | 재측정되지 않음| 14개 중 4개 언어 거부됨: 모델이 프랑스어 구절을 남겨 가드가 이를 차단함                                                              |
| MiMo v2.5 (무료)     | OpenCode Zen, 계정 불필요         | ❌ 11/14                | 재측정되지 않음| 1개 언어 거부됨; 폴란드어에서 한 섹션 유실                                                                                            |
| Mistral Large        | Mistral API 키                    | ❌ 5/14                 | ❌ 1/14      | **섹션 전체가 사라짐**: 기사에서 1개 언어 (hi), 이 README에서 3개 언어 (ar, hi, ko) — 및 기사에서 3개 언어 거부됨                    |
| DeepSeek V4 Flash    | OpenRouter 키                     | ❌ 3/14                 | 재측정되지 않음| 14개 중 10개 언어 거부됨; 언어당 37분 소요                                                                                             |

|     | 기호의 의미                                                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14개 언어가 모두 번역되었으며 원본과 어떠한 차이도 없음                                                                                                                                               |
| ⚠️  | 14개 언어가 모두 번역됨; 차이나는 부분은 **마크업**(굵은 글씨 단어, `code`, 대괄호가 빠진 링크 등)에 불과함. 텍스트, URL, 코드 블록, 섹션은 전혀 누락되지 않음                              |
| ❌  | 최소 1개 언어가 번역되지 못함(파일이 거부되어 작성되지 않음) **또는** 작성된 파일에서 내용이 누락됨                                                                                                  |

기억해야 할 점:

- **거부된 번역이 훼손된 번역을 의미하는 것은 아닙니다.** 반환 시 토큰이 누락되면
  파일이 작성되지 않고 해당 언어는 거부된 것으로 처리됩니다. 기사 번역 시
  Grok에서 발생한 문제가 바로 이것입니다. 5개의 비라틴 문자 언어에서 첫 번째
  세그먼트부터 인라인 코드 4개와 URL 3개가 유실되었습니다.
- **이 안전망은 제목, 표, 프론트 매터, 본문 텍스트에는 적용되지 않습니다.** 모델이
  특정 섹션을 삭제하더라도 도구는 경고 없이 파일을 작성합니다(Mistral의 경우가
  이에 해당합니다). 이러한 요소들은 토큰으로 대체될 수 없으며 현재 가드가 이를
  검사하지 않습니다. `scripts/compare_structure.py`가 유실된 섹션을 감지하기는 하지만 사후
  검사일 뿐입니다.
- **이 README에서 Grok의 점수가 없는 이유**: 12개 언어(그중 11개는 차이 없음) 번역 후
  CLI 세션이 만료되었습니다. 중단된 테스트는 평가되지 않습니다.
- **언어보다 문서의 밀도가 더 중요합니다.** Grok은 일반적인 README 파일은 잘
  처리하지만 링크가 많은 기사에서는 네덜란드어를 포함해 성능이 저하됩니다.

날짜 및 문서: "이 README" 열은 2026년 9월 9일 당시 고정된 리비전(785줄, 인라인
코드 285개, 표 89줄, 이후 수정됨)을 기준으로 측정되었습니다(단, Antigravity 2개
항목은 9월 26일 1.14.0과 함께 출시된 더 짧은 리비전인 600줄, 인라인 코드 257개, 표
85줄을 기준으로 측정). "조밀한 모니터링 기사" 열은 9월 4~5일 진행된 589줄 기사
테스트를 바탕으로 합니다(단, Grok 항목은 동일 모니터링의 다른 판본으로 9월 9일
재측정, Antigravity 2개 항목은 9월 26일 동일 기사로 측정).
전체 표, 소요 시간 및 테스트 프로토콜은
[상세 측정 결과](#상세-측정-결과)에서 확인할 수 있습니다.

## 모든 옵션

| 옵션                     | 설명                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 번역할 단일 Markdown 파일 (`--source_dir`의 대안)                                                             |
| `--source_dir`           | Markdown 파일이 포함된 소스 디렉터리 (기본값: `content/posts`)                                                 |
| `--target_dir`           | 번역된 파일의 출력 디렉터리 (기본값: `traductions_en`)                                                          |
| `--source_lang`           | 원본 언어 (기본값: `fr`)                                                                            |
| `--target_lang`           | 대상 언어 (기본값: `en`)                                                                            |
| `--model`           | 사용할 특정 모델                                                                                              |
| `--eco`           | 경제적인 모델 사용                                                                                            |
| `--use_mistral`           | Mistral AI API 사용                                                                                           |
| `--use_claude`           | Claude API 사용                                                                                               |
| `--use_gemini`           | Gemini API 사용                                                                                               |
| `--use_grok`           | xAI (Grok) API 사용 — `XAI_API_KEY` 필요                                                                     |
| `--use_codex`           | ChatGPT 구독 할당량을 사용하여 Codex CLI 사용                                                                 |
| `--use_grok_cli`           | Grok 구독 할당량을 사용하여 Grok CLI 사용                                                                     |
| `--use_antigravity`           | Google AI Pro 또는 Ultra 구독 할당량을 사용하여 Antigravity CLI (`agy`) 사용                         |
| `--use_opencode`           | OpenCode에 구성된 프로바이더로 OpenCode(오픈 소스) 사용; `--model provider/modèle` 필요                                  |
| `--use_openrouter`           | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                                                       |
| `--force`           | 강제 재번역                                                                                                   |
| `--keep_filename`           | 원본 파일명 유지                                                                                              |
| `--news`           | 뉴스 모드: 영어 인용문 보호, 언어별 플래그 관리                                                              |
| `--add_translation_note`           | 번역 알림 추가                                                                                                |
| `--note_position`           | 알림 위치: `top`, `bottom`(기본값), 또는 `both`                                       |
| `--note_format`           | 알림 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`                                             |
| `--include_model`          | 출력 파일에 모델 이름 포함                                                                                    |
| `--reasoning_effort`          | GPT-5.x 추론 강도: `none`/`low`/`medium`/`high`/`xhigh`            |

9개의 `--use_*` 플래그는 상호 배타적입니다. 둘 이상을 함께 지정할 수
없습니다.

## 프로바이더

### API 사용: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 옵션은 각 제공자의 절약형 티어로 전환합니다.

| Provider    | 품질 (기본값)                                         | 절약형 (`--eco`)  |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (`--model` 사용 시 `terra` 및 `luna` 가능) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` 필수                 | 동일 — `--eco` 효과 없음 |
| OpenRouter  | `--model fournisseur/modèle` 필수              | 동일 — `--eco` 효과 없음 |

### ChatGPT 구독 사용: `--use_codex`

공식 Codex CLI를 제어합니다. 번역은 API 키나 종량제 결제 없이 ChatGPT 구독 쿼터에서 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 바이너리는 `CODEX_BIN`, `PATH`, 그리고 `openai-codex-cli-bin` 패키지 순서로 검색됩니다. `~/.codex/auth.json`는 절대 읽지 않습니다.
- 하위 프로세스의 환경에서 `OPENAI_API_KEY` 및 `CODEX_API_KEY`가 제거됩니다. 키가 존재하더라도 API로 전환되지 않습니다.
- 각 세그먼트는 5시간 기간의 "메시지"를 최소 1개 소모하며, 유효성 검사에 실패하여 재시도할 경우 2개를 소모합니다. OpenAI의 예상치에 따르면 Plus 플랜 기준 `gpt-5.6-luna`(`--eco`)는 5시간당 250~2,000개, `gpt-5.6-sol`는 10~100개의 메시지가 제공됩니다.
- `--model gpt-5.6-terra` 및 `--model gpt-5.6-luna` 또한 구독을 통해 전달됩니다. 계정에 권한이 없는 모델인 경우 400 "model is not supported when using Codex with a ChatGPT account" 오류를 반환합니다.
- API보다 느리며, 문서가 길어질수록 격차가 벌어집니다. 이 README 기준 중앙값으로 `gpt-5.6-sol`는 언어당 6분 46초가 걸린 반면, `gemini-3.7-flash`는 36초가 걸렸습니다.
- CI 환경에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS` 정의됨). 구독 인증은 공유 러너에 두어서는 안 되는 개인 세션 파일을 통해 이루어집니다.
- 변수: `CODEX_BIN`, `CODEX_TIMEOUT`(세그먼트당 초, 기본값 600).

### Grok 구독 사용: `--use_grok_cli`

SuperGrok 또는 X Premium+ 구독 환경에서 공식 Grok Build CLI를 사용하는 동일한 원리입니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex보다 약한 격리.** Grok의 OS 샌드박스는 최신 Linux 환경(AppArmor, 컨테이너 런타임 소켓) 다수에서 적용되지 않으며, 적용할 수 없는 프로필은 별다른 경고 없이 비격리 상태로 시작됩니다. 따라서 이 스크립트는 기본적으로 프로필을 요청하지 않고 이를 고지하며, 말없이 보호를 해제하기보다는 시작을 거부하는 유일한 계층인 CLI의 `--deny` 규칙(포괄 규칙 `*` 포함)에 의존합니다. `GROK_TRANSLATE_SANDBOX=read-only`는 OS 샌드박스를 요구하며, 머신이 이를 충족하지 못하면 시작이 실패합니다.
- 쿼터는 주 단위이며 Chat, Imagine, Voice와 공유되고, 이를 조회할 수 있는 명령어가 없습니다. 따라서 배치 작업이 알림 없이 대화형 사용량을 잠식할 수 있습니다.
- 변수: `GROK_BIN`, `GROK_HOME`(CLI 디렉터리, 기본값 `~/.grok`), `GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`.

### Google 구독 사용: `--use_antigravity`

Antigravity의 공식 CLI인 `agy`를 사용하는 동일한 원리입니다. Google AI Pro 또는 Ultra 결제 사용자의 경우, 번역 요금이 토큰 단위로 청구되지 않고 구독 쿼터에서 차감됩니다. 이 쿼터를 활용할 수 있는 유일한 경로입니다. Gemini CLI는 2026년 6월 18일부로 해당 계정 지원을 중단했으며([공지](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)), Antigravity SDK는 API 키 또는 Google Cloud 프로젝트만 허용합니다.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **유료 경로가 열려 있지 않습니다.** agy는 사용자 환경으로부터 엄격하게 제한된 변수 목록(`PATH`, 언어 및 표준시, 터미널, ID, 프록시 및 인증서, 세션 버스)만 전달받으며 어떠한 키도 받지 않습니다. agy의 일부 환경 변수는 화면에 아무것도 표시하지 않은 채 호출을 전환해 버립니다(테스트 결과: 하나는 문서를 타사 게이트웨이로 전송하고, 다른 하나는 과금되는 Google Cloud 프로젝트로 전송함). 차단 목록 방식은 검토할 때마다 누락이 발생했습니다. 모든 세그먼트 시작 전, 쿼터를 소모하지 않는 `agy -p /config`를 통해 유료 AI 크레딧이 비활성화되어 있고 API 키나 Google Cloud 프로젝트가 없는지 확인해야 하며(설정이 누락되면 거부 처리됨), 그렇지 않으면 아무것도 번역되지 않습니다. 이후 각 호출의 로그가 구독 사용(`authMethod=consumer`)을 증명해야 하며, 그렇지 않으면 응답이 거부됩니다.
- **격리.** 각 호출은 도구가 없는 번역 에이전트와 함께 일회용 비공개 홈 디렉터리에서 실행됩니다. 사용자의 agy 설정, 규칙, 플러그인, MCP 서버, 훅은 유입되지 않으며, 기록에 아무것도 추가되지 않고, 로그인은 키체인에 유지되며 aipmt는 이를 절대 읽지 않습니다. 에이전트를 찾을 수 없으면 agy는 경고 없이 코딩 에이전트와 도구로 되돌아갑니다. 따라서 로그 전체 행에서 올바른 에이전트인지 확인해야 하며(해당 메시지를 인용한 문서는 인정되지 않음), 그렇지 않으면 거부됩니다.
- **지원 플랫폼**: 키체인이 있는 세션(D-Bus 세션 버스, Secret Service)의 Linux. macOS는 허용되나 측정되지는 않았습니다. Windows에서는 agy가 각 호출을 격리하는 변수를 읽지 못하므로 거부되며, D-Bus 세션 버스가 없는 Linux(SSH 세션, 컨테이너, 서버)에서도 거부됩니다. 이러한 환경에서 agy는 토큰을 격리 기능에 의해 가려지는 `~/.gemini` 파일에 저장하기 때문입니다. 로그인 코드를 1분간 기다리는 대신, 실행 전 즉시 사유와 함께 거부됩니다.
- **모델**: `agy models`에서 제공하는 모델. Gemini 모델은 이름에 추론 강도(effort)가 포함되어 있습니다(`gemini-3.8-flash-medium` 등). 접미사가 없는 이름은 호출 전에 거부되며, `--reasoning_effort`는 효과가 없습니다. 기본값은 `gemini-3.8-flash-medium`이며, `--eco`에서는 `gemini-3.7-flash-low`입니다. 이를 결정한 테스트 캠페인은 [상세 측정 결과](#상세-측정-결과)에 기술되어 있습니다. Claude와 GPT-OSS는 훨씬 적은 별도의 쿼터를 가집니다. 측정된 호출당 5시간 기간의 약 1%를 소모하며, Flash는 0.05%를 소모합니다.
- **쿼터**: 그룹별로 5시간 윈도우와 주간 윈도우가 제공되며, 토큰 비용에 비례하여 차감됩니다. 작성자의 계정에서 측정한 결과: `gemini-3.8-flash-medium`에서는 원본 100만 자당 5시간 윈도우의 약 16포인트, `gemini-3.7-flash-medium`에서는 14포인트, 낮은 추론 강도에서는 7~8포인트가 소모되었습니다. 따라서 40,000자의 README는 0.5포인트를 조금 넘게 소모합니다. 주간 한도는 티어에 따라 다릅니다. 재시도는 agy가 재시도 가능하다고 보고한 내용을 따릅니다. 그렇지 않은 경우 소진된 윈도우는 절대 재시도되지 않으며, `/usage`에 표시되는 초기화 시점까지 각 파일 처리가 실패합니다.
- **API보다 느림**: 벤치마크의 밀도 높은 기사 기준, 중앙값으로 `gemini-3.8-flash-medium`는 언어당 3분 59초, `gemini-3.7-flash-medium`는 3분 14초가 걸린 반면, API를 통한 Gemini 3.7 Flash는 1분 18초가 걸렸습니다.
- **작업 중단**: Ctrl-C를 누르거나 터미널을 닫으면 쿼터를 계속 소모하도록 두지 않고 명령어와 함께 agy가 즉시 중지됩니다. 이는 Codex, Grok CLI, OpenCode도 동일합니다. `nohup` 환경에서는 번역이 계속 진행됩니다.
- CI 환경에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS` 정의됨). 로그인은 개인 키체인에 저장됩니다. 러너에서는 `GOOGLE_API_KEY`와 함께 `--use_gemini`를 사용하십시오.
- 변수: `AGY_BIN`(지정되지 않은 경우 `PATH`, 이후 `~/.local/bin/agy` 탐색), `AGY_TIMEOUT`(시작 시간을 포함한 세그먼트당 초, 기본값 900).

**이용 약관: 귀하의 계정으로 책임이 귀속됩니다.** [Antigravity 이용 약관](https://antigravity.google/terms)(섹션 6)과 [FAQ](https://antigravity.google/docs/faq/)에서는 타사 소프트웨어(Claude Code, OpenClaw, OpenCode 명시)에서 Antigravity 로그인을 사용하여 서비스에 접근하는 것을 금지하고 있으며, 위반 시 계정이 정지될 수 있습니다. aipmt는 토큰을 읽거나 재사용하지 않으며, Google이 스크립트 및 CI용으로 문서화한 [헤드리스 모드](https://antigravity.google/docs/cli/headless/)로 공식 바이너리를 실행합니다. Google 관계자는 로컬 스크립트에서 개인 작업을 위해 `agy -p`를 실행하는 것이 "표준적(standard)"이라고 밝힌 바 있으나([공식 포럼, 2026년 9월 25일, 비계약적 답변](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)), 이와 같은 배포용 도구의 사례에 대해 명확히 결론을 내린 공식 규정은 없습니다.

**공개 문서 전용.** 동일한 이용 약관의 섹션 5에 따르면, 유료 구독을 포함하여 대화 내용(프롬프트, 응답, 메타데이터)이 Google 제품 및 머신러닝 개선에 사용될 수 있으며 사람에 의해 검토될 수 있습니다. 수집 거부는 효과가 문서화되지 않은 `enableTelemetry` 설정을 통해 이루어지며 aipmt는 이를 설정하지 않습니다. 사용자의 agy 설정은 격리 환경으로 인계되지 않습니다. 기밀성이 있는 내용은 절대 처리하지 마십시오.

### 원하는 제공자 선택: `--use_opencode`

[OpenCode](https://opencode.ai)는 내부에서 구성된 제공자(API 키, 구독, OpenCode Zen 게이트웨이(계정 불필요, 무료 모델), 또는 로컬 모델)로 라우팅하는 오픈 소스(MIT) 코드 에이전트입니다. 여기서는 Zen과 Ollama 두 가지 경로를 종단 간으로 측정했습니다.

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

`--model`는 필수입니다. 이 옵션이 없으면 OpenCode는 대화 내용이 학습에 사용될 수 있는 무료 모델로 되돌아가며, 이러한 선택을 사용자 대신 임의로 내리지 않습니다.

각 호출 시 격리 방식:

- 사용자 설정보다 우선하는 인라인 구성이 정의되어 모든 도구가 거부된(`permission: { "*": "deny" }`) `aipmt` 에이전트를 설정하고, 세션 공유 비활성화, `--pure`, `--auto`는 절대 사용하지 않음;
- 비어 있는 일회용 작업 디렉터리를 사용하며, `OPENCODE_DISABLE_PROJECT_CONFIG` 및 `OPENCODE_DISABLE_CLAUDE_CODE`가 설정됨 — 이것이 없으면 OpenCode는 프롬프트에 현재 디렉터리의 `AGENTS.md`와 `~/.claude/CLAUDE.md`를 삽입함. 전역 `~/.config/opencode/AGENTS.md`는 계속 삽입되며, OpenCode에서는 이를 배제할 수 없음;
- 출력 조건: 반환 코드 0, `error` 이벤트 없음, 도구 호출 없음, 마지막 단계 `stop`, 비어 있지 않은 텍스트, 그리고 `aipmt` 에이전트가 실제로 로드되어야 함 — 알려지지 않은 `--agent`는 OpenCode 실행을 실패시키지 않고 말없이 코딩 에이전트로 되돌아감;
- OpenCode 자체의 키인 `OPENCODE_API_KEY`를 제외하고는 어떠한 `aipmt` 키도 전달되지 않음. 제공자는 `aipmt`의 `.env`가 아니라 OpenCode 내에서 구성해야 함.

참고 사항:

- Zen의 무료 모델은 수시로 변경되고 제한 사항이 문서화되어 있지 않으며, 대화 내용이 학습에 사용될 수 있습니다. 비공개 콘텐츠가 아닌 공개 문서용으로만 사용하십시오.
- 로컬 모델은 최소 16k 토큰의 컨텍스트를 제공해야 합니다. 세그먼트 크기가 최대 16,000자에 달하기 때문입니다. Ollama는 종종 4,096으로 구성하므로, `PARAMETER num_ctx 32768`를 포함한 `Modelfile`를 통해 설정하십시오.
- `--eco`는 효과가 없습니다. `--reasoning_effort`는 OpenCode의 `--variant`로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 변수: `OPENCODE_BIN`(지정되지 않은 경우 `PATH`, 이후 `~/.opencode/bin/opencode` 탐색), `OPENCODE_TIMEOUT`(세그먼트당 초, 기본값 600). `OPENCODE_CONFIG`는 OpenCode로 그대로 전달됩니다.

`~/.config/opencode/opencode.json`에서 Ollama를 통한 로컬 모델 예시:

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

`reasoningEffort: "none"`는 Ollama가 이러한 모델에서 기본적으로 활성화하며 Modelfile로 비활성화할 수 없는 생각(thinking) 과정을 끕니다. 6개 단어로 된 문장에서 측정한 결과: 옵션이 없을 때는 919개의 생각 토큰과 68초가 소요되었으나, 옵션을 사용했을 때는 9개 토큰만 소요되었습니다.

### 400개 이상의 모델 지원: `--use_openrouter`

OpenRouter는 타사에서 호스팅하는 모델(여기서 다른 어떤 제공자도 제공하지 않는 개방형 중국어 모델 포함) 앞단에서 단일 크레딧으로 종량제 과금되는 라우터입니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`는 필수입니다. 요금이 청구되기 전에 실행되는 사전 점검(preflight)을 통해 라우팅의 두 가지 특이 사항을 처리합니다.

- **동일한 모델이 서로 다른 한도를 가진 수십 개의 호스트에 의해 제공됨** — `z-ai/glm-5.3-flash`의 경우 23개 호스트가 있으며, 그중 하나는 최대 출력 토큰이 2,048개로 제한되어 있습니다. 사전 점검은 `/api/v1/models/{modèle}/endpoints`를 읽어 출력 토큰이 8,000개 미만이거나 상태가 저하된 호스트를 제외하고, `allow_fallbacks: false`로 나머지 호스트를 고정합니다.
- **추론(reasoning) 비용은 출력 요율로 청구됨** — `z-ai/glm-5.2`의 "OK" 응답에서 2토큰 대신 107토큰이 청구됩니다. 추론은 기본적으로 꺼져 있습니다. 이를 강제하는 모델은 허용하는 가장 낮은 강도로 설정되며, 카탈로그의 기본값은 번역이 완료되기 전에 출력을 소진시킬 수 있습니다. `--reasoning_effort`가 항상 우선합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 컨텍스트 윈도우는 카탈로그 정보를 따릅니다. 16,400토큰 미만의 모델은 호출 전 즉시 거부됩니다. 프롬프트 및 세그먼트용 8,400토큰, 최소 출력 토큰 8,000개가 필요하기 때문입니다.
- 카탈로그에 없는 슬러그이거나, 카탈로그에 연결할 수 없거나, 한도를 만족하는 호스트가 없는 경우 명령어가 중지됩니다.
- 빈 출력과 함께 `finish_reason=length`가 발생하는 것은 잘림(truncation)이 아니라 추론에 의해 예산이 소진된 경우이며, 메시지에서 이를 구분하여 안내합니다.
- `--eco`는 효과가 없습니다.
- 변수: `OPENROUTER_API_KEY`(<https://openrouter.ai/keys>), `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30).

### 번역 노트

`--add_translation_note`는 `bottom`(기본값), `top`(프론트매터 뒤) 또는 `both`(`--note_position`) 위치에, `legacy`(굵은 글씨 단락, 기본값) 또는 `marker`(`--note_format`) 형식으로 메모를 추가합니다. `marker` 형식은 보이지 않는 Markdown 참조 정의인 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` 뒤에 굵은 글씨의 인용구가 이어지는 형태입니다. GitHub에서 읽을 수 있으며, 빌드 시 remark 플러그인으로 활용할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정 결과

모든 측정 결과는 `aipmt`를 사용하여 14개 언어(en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi)로 실제로 실행된 번역을 바탕으로 합니다. **기록됨**은 가드가 통과시킨 파일 수를 나타내며, **불일치 없음**은 `scripts/compare_structure.py`가 아무것도 감지하지 못한 파일 수(섹션, 소제목, 링크, 고유 URL, 코드 블록, 인라인 코드, 표 행, 인용 블록, 굵은 글씨 단어 수가 동일함)를 나타냅니다.

"불일치 없음"은 내용을 읽지 않고 요소의 개수만 세는 비교 도구이므로 "내용이 동일함"이 아니라 "감지된 차이가 없음"을 의미합니다. 레벨 4 제목이 삭제되었거나, 인라인 코드 텍스트가 대체되었거나, 플래그가 바뀌었거나, 내부 링크에 괄호가 하나 더 들어가서(`[texte]((#ancre))`) 더 이상 연결되지 않는 경우 등은 보고되지 않으며, 언어의 품질을 평가하지도 않습니다.

### 밀도 높은 모니터링 기사, `--news` 모드

[jls42.org AI 모니터링](https://jls42.org/fr/news) 기사 중 하나:
589행, 링크 140개, 21개 섹션, 보호된 영어 인용문 3개. 2026년 9월 4일 및 5일
측정 기준.

| 모델                                            | 접근 방식          | 작성 완료 | 편차 없음    | 중앙값/언어    |
| ----------------------------------------------- | ------------------ | --------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14     | ✅ **14/14** | 1분 18초       |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 구독        | 14/14     | ✅ **14/14** | 3분 59초       |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 구독        | 14/14     | ✅ **14/14** | 3분 14초       |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 구독       | 14/14     | ✅ **14/14** | 11분 28초      |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14     | ✅ **14/14** | 5분 37초       |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14     | ✅ **14/14** | 26분 23초      |
| `claude-sonnet-5`                               | Anthropic API      | 14/14     | ⚠️ 11/14     | 6분 31초       |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14     | ❌ 11/14     | 9분 27초       |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14     | ❌ 8/14      | 10분 09초      |
| `ollama/gpt-oss-20b-32k`                        | 로컬               | 10/14     | ❌ 7/14      | 12분 39초      |
| `mistral-large-latest`                          | Mistral API        | 11/14     | ❌ 5/14      | 5분 32초       |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14      | ❌ 3/14      | 37분 27초      |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 구독          | 1/14      | ❌ 1/14      | 23분 11초      |

Grok은 9월 9일에 동일한 모니터링의 다른 회차(356행)를 대상으로
다시 측정되었습니다. 14개 언어 중 9개 작성 완료, 편차 없음은 8개였습니다. 상단
표에 나와 있는 수치가 바로 이것입니다. 중단된 세 차례의 측정은 기록되지
않았습니다: 크레딧 부족으로 중단된 `qwen3.5-27b`(9개 언어) 및 `kimi-k2.6`(4개),
그리고 제공업체가 이후 수정한 추론 설정 문제로 인해 두 건의 실패가 발생했던
`z-ai/glm-5.3-flash`입니다. OpenRouter 항목은 `--use_openrouter` 적용 전 라우터의 기본
설정으로 측정되었습니다. 제공된 공급자로 재측정한 `z-ai/glm-5.2`는 동일하게 14/14를
기록했습니다. 수치는 9월 10일에 최신 비교 도구로 다시 계산되었습니다. 최초 공개 대비
`qwen3.8-flash`와 `qwen3.7-flash`가 각각 1개 언어를 더 성공시켰으며, 나머지는
동일합니다.

`--use_antigravity` 항목은 9월 26일에 동일한 기사를 대상으로 4개 번역을
병렬 진행하여 측정되었습니다: 오전에 `gemini-3.7-flash-medium`, 오후에
`gemini-3.8-flash-medium`. 영어 번역 시, 인위적인 플래그를 추가하지 않고
인용문 아래의 세 줄짜리 프랑스어 번역을 각 모델이 자체적으로 제거했으며
영어 인용문은 원형을 유지했습니다. 따라서 대체 정리 작업이 전혀 필요하지
않았습니다. `--eco`(`gemini-3.7-flash-low`)의 경우 4개 언어(en, ja, ar, hi)만을
대상으로 진행되었습니다: 4개 중 4개 작성 완료, 모두 편차 없음, 중앙값 1분 52초.
같은 날 더 최근의 모니터링 회차인 9월 25일 자 기사(438행, 영어 인용문 2개)를
블로그 외부에서 `gemini-3.7-flash-medium`로 번역하여 교차 검증을 진행했습니다:
14개 중 14개 작성 완료, 모두 편차 없음, 언어당 87초에서 128초 소요.

### 본 프로젝트의 README, 표준 Markdown

2026년 9월 9일 고정 리비전: 785행, 인라인 코드 285개, 블록
닫기 마크 40개, 표 행 89개. 4개 번역 병렬 진행.

| 모델                                            | 작성 완료 | 편차 없음 | 중앙값/언어 | 차이점                                                                   |
| ----------------------------------------------- | --------- | --------- | ----------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14     | ✅ 14/14  | 1분 43초    | 없음                                                                     |
| `gemini-3.7-flash`                              | 14/14     | ⚠️ 13/14  | 36초        | 굵은 글씨 단어 하나 (ja)                                                 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14     | ⚠️ 13/14  | 1분 22초    | 굵은 글씨 단어 하나 (ko)                                                 |
| `claude-sonnet-5`                               | 14/14     | ⚠️ 12/14  | 2분 56초    | 링크 하나 (sv), 굵은 글씨 단어 하나 (zh)                                 |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14     | ⚠️ 12/14  | 6분 46초    | 굵은 글씨 단어 하나 (ar, ja)                                             |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14     | ⚠️ 11/14  | 2분 34초    | 굵은 글씨 단어 하나 (hi, ja, ko)                                         |
| `qwen/qwen3.7-flash`                            | 14/14     | ⚠️ 10/14  | 2분 17초    | 아랍어에서 인라인 코드 40개 추가됨, 굵은 글씨 (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14     | ❌ 1/14   | 2분 44초    | 섹션 하나 누락 (ar, hi, ko), 코드 블록 추가됨 (ja, ko, ro, zh)           |

중단된 두 차례의 측정은 기록되지 않았습니다: 12개 언어 진행 후 CLI 세션이
만료된 Grok(편차 없음 11개), 그리고 2개 진행 후 호스팅 업체로부터 HTTP 429
응답을 받은 `qwen3.8-flash`입니다. `opencode/mimo-v2.5-free`와 `ollama/gpt-oss-20b-32k`는
이 리비전에서 재측정되지 않았습니다. 277행 더 짧았던 9월 4일 및 5일 리비전에서는
두 모델 모두 14개 중 9개의 번역을 작성했으며, 편차 없는 번역은 각각 7개와
1개였습니다.

`--use_antigravity` 항목은 고정 리비전에서는 측정되지 않았으나,
1.14.0과 함께 배포된 리비전을 대상으로 9월 26일에 측정되었습니다: 600행,
인라인 코드 257개, 블록 닫기 마크 30개, 표 행 85개. 185행 더
짧기 때문에 다른 항목들과 1:1로 직접 비교할 수는 없지만, 두
Antigravity 항목끼리는 상호 비교가 가능합니다. 비교 도구가 검사하지
않는 내부 링크의 경우, `gemini-3.8-flash-medium`는 14개 언어 모두에서 온전히
유지한 반면, `gemini-3.7-flash-medium`는 이탈리아어에서 링크가 깨졌습니다.

### 널리 알려진 4개 프로젝트의 README

GitHub에서 그대로 가져온 FastAPI, Ollama, tldr-pages, Vue.js — 앞선
두 문서보다 난이도가 낮은 문서들입니다. 이 측정은 어려움을 겪는 모델들을
대상으로 진행되었으며, Gemini가 비교 기준으로 사용됩니다.

| 모델                      | 범위                       | 작성 완료 | 편차 없음    |
| ------------------------- | -------------------------- | --------- | ------------ |
| `gemini-3.7-flash`        | 4개 프로젝트 × 14개 언어   | 56/56     | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4개 프로젝트 × 14개 언어   | 55/56     | ❌ 47/56     |
| `grok-4.6` (구독)    | 4개 프로젝트 × ar, hi, ja, zh | 16/16     | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4개 프로젝트 × ar, hi, ja, zh | 15/16     | ❌ 9/16      |

### 이 측정 결과에 해당하지 않는 것

- **완전한 순위표가 아닙니다**: OpenRouter에만 400개가 넘는 모델이 존재하며,
  측정된 것은 15개 안팎에 불과합니다.
- **측정 시간은 참고용입니다**: 측정에 따라 3~6개의 번역을 병렬로 진행했으며,
  공급자의 처리량은 하루 중 시간대에 따라 달라집니다.
- **특정 시점의 관측 결과입니다**: 동일한 이름 아래에서도 모델은 변경되며,
  여러분의 문서는 본 테스트 문서와 다릅니다.

파일의 고정 복사본을 바탕으로 여러분의 문서에서 직접 측정을 재현하려면:

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

두 줄 모두 필수입니다: `pip install -e .`가 없으면 `python -m aipmt`가
`No module named aipmt`를 반환합니다.

품질 관리 도구(선택 사항이지만 권장됨):

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 28개 번역(README 및 CHANGELOG, 14개 언어)은 `./regen_translations.sh --force`를
통해 재생성할 수 있습니다 — 기본적으로 ChatGPT 구독을 사용하는 Codex 및
`gpt-5.6-sol`로 4개씩 병렬 실행됩니다. `REGEN_PROVIDER`와 `REGEN_MODEL`는
경로를 변경합니다: `antigravity`는 구독 방식(Google 구독)을 유지하므로
예외 설정 없이 실행 가능하며, 종량제 API(`openai`, `gemini`,
`grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다.
`REGEN_JOB_TIMEOUT`는 각 작업의 최대 시간을 제한합니다(600초, Codex 및 Antigravity는 1,800초).
도구에 대한 자세한 내용은 `CLAUDE.md`에 설명되어 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 발행되는 개인 블로그입니다.
  블로그의 [일일 AI 모니터링](https://jls42.org/fr/news)은 매일 이 도구로 번역되며,
  위 측정의 기준 문서 역할을 합니다.

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하십시오.

## 고지 사항

본 프로그램은 GPL v3 제15조 및 제16조의 조건에 따라 **어떠한 보증도 없이** 배포됩니다:
상품성이나 특정 목적에의 적합성에 대한 보증 없이 "있는 그대로(AS IS)" 제공되며,
작성자는 본 프로그램의 사용으로 인해 발생하는 손해에 대해 책임을 지지 않습니다.
이 요약보다 라이선스 원문이 우선합니다.

- **발행하기 전에 검토하십시오.** 보호 기능은 코드 블록, 인라인 코드, URL,
  앵커 및 `--news` 모드의 인용문에 적용되며, 제목, 표, 프론트 매터,
  문장의 의미는 보호 대상이 아닙니다.
- **문서는 선택한 공급자로 전송되며**, 해당 공급자의 이용 약관 및 데이터 정책이
  적용됩니다. 일부 무료 모델은 대화 내용을 학습에 재사용할 수 있으며, Antigravity의
  이용 약관에 따르면 유료 구독을 포함하여 Google이 데이터를 재사용하고 인간이 검토하도록
  할 수 있습니다. 로컬 모델만이 머신 외부로 데이터를 전혀 내보내지 않는 유일한 방법입니다.
- **API 호출 시 비용이 청구됩니다.** 본 프로그램은 지출 한도를 제한하지 않습니다:
  문서가 길거나, 실패 후 재시도하거나, 추론을 많이 수행하는 모델일수록 비용이 더 많이 발생합니다.
- **공개된 측정 결과는 특정 시점의 관측치일 뿐이며**, 어떠한 보증도 제공하지 않습니다.

언급된 제품 및 회사 이름은 해당 소유자의 상표입니다. 본 프로젝트는 이들 중 어느 곳과도 제휴되어 있지 않습니다.

**gemini-3.8-flash-medium으로 프랑스어에서 한국어로 번역된 기사.**
