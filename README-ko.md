# AI 기반 Markdown 번역기

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 코드 품질</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="품질 게이트 상태"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="보안 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="신뢰성 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="유지 관리 가능성 등급"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="커버리지"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="취약점"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="버그"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 악취"></a>
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

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기입니다.

이 Python 스크립트는 소스 언어에서 대상 언어로 Markdown 파일을 번역하면서 서식, 코드 블록 및 front matter 메타데이터를 보존합니다.

## 주요 기능

- **멀티 Provider**: 4개의 API(OpenAI, Mistral, Claude, Gemini)와 ChatGPT 구독의 Codex CLI 지원
- **2026년 모델**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 파일 하나만 번역하기 위한 `--file` 옵션
- **지능형 세분화**: 모델별 토큰 제한을 고려한 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드(`` `...` ``)를 모두 보존
- **파일 이름**: 원래 이름을 유지하기 위한 `--keep_filename` 옵션
- **뉴스 모드**: 영어 인용문을 보호하고 뉴스 기사에서 국기를 처리하는 `--news` 옵션
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 참고 사항**: 문서 끝에 선택적으로 참고 사항 추가

## 설치

### 도구 사용

```bash
pip install ai-powered-markdown-translator
```

이제 `aipmt` 명령을 어디서나 사용할 수 있습니다. Python 스크립트 디렉터리가
`PATH`에 없으면 `python -m aipmt`가 정확히 같은 작업을 수행합니다. Python 3.10
이상 필요합니다.

다른 패키지와 격리하여 설치하려면 다음을 사용합니다.

```bash
pipx install ai-powered-markdown-translator
```

### 프로젝트에 기여

개발하려면 복제한 저장소가 여전히 필요합니다. 테스트, 28개의 번역 및 모든 품질 도구가
이곳에 있습니다.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`는 **완전히 고정된 lock 파일**로, 테스트된 환경을 정확히 반영합니다.
`pyproject.toml`에 공개된 범위는 의도적으로 더 넓으며, 다른 패키지에는 아무런 제약을
가하지 않습니다.

### 품질 도구(선택 사항이지만 권장)

이 프로젝트는 [`pre-commit`](https://pre-commit.com)을 사용하여 형식이 잘못되었거나 취약하거나
비밀 정보가 포함된 코드가 커밋되는 것을 방지합니다. 설치 방법:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성화된 훅: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard(복잡도),
detect-secrets(API 키), mypy(점진적 타이핑), Opengrep(SAST), pip-audit(CVE deps), unittest.
자세한 내용은 `CLAUDE.md`의 _Quality / pre-commit_ 섹션을 참조하세요.

## 구성

**명령을 실행하는 디렉터리 안에** `.env` 파일을 만드세요
(해당 위치에서 먼저 찾은 다음 상위 디렉터리에서 찾습니다). 또는 다음 환경 변수를
정의하세요.

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY`는 `GOOGLE_API_KEY`의 대안으로 사용할 수 있습니다(AI Studio 규칙).
선택적 변수: `XAI_BASE_URL`(xAI 엔드포인트, 기본값
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(Anthropic 호출당 초, 기본값
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
그리고 `GROK_TRANSLATE_SANDBOX`(Grok CLI 섹션 참조). `regen_translations.sh` 측면에서는
`REGEN_PROVIDER`, `REGEN_MODEL` 및 `REGEN_JOB_TIMEOUT`(작업당 제한, 기본값 600초)을
사용합니다.

## 사용법

### 단일 파일 번역

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 디렉터리 번역

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### ChatGPT 구독으로 번역(`--use_codex`)

이 Provider는 API 키를 사용하지 않습니다. 공식 Codex CLI를 비대화형 모드로 제어하므로,
번역 비용은 이미 결제된 ChatGPT 구독(Plus, Pro, Business 등)의 할당량에서 차감됩니다.
이는 OpenAI가 이 용도에 대해 문서화한 유일한 방법입니다. `~/.codex/auth.json`의 토큰은
Platform API 호출을 인증하지 않으며, 이 스크립트에서도 읽지 않습니다.

**사전 요구 사항:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

바이너리는 다음 순서로 검색됩니다: `CODEX_BIN` 변수, `PATH`, 그다음
Python 패키지 `openai-codex-cli-bin`. 후자는 `requirements.txt`에 의도적으로 포함되지 않습니다.
약 250MB에 달하므로 선택적 Provider를 위해 모든 사용자에게 설치를 강제하게 되기
때문입니다.

**알아 둘 점:**

- **API 키는 사용되지 않습니다.** `OPENAI_API_KEY` 및 `CODEX_API_KEY`는 하위 프로세스의
  환경에서 제거되므로, `.env`에 키가 있어도 번역이 사용량 기반 과금으로
  전환되지 않습니다.
- **세그먼트 하나 = 요금제의 5시간 창에서 하나의 ‘로컬 메시지’**입니다.
  품질 모델(`gpt-5.6-sol`, Plus에서 5시간당 10~100개 메시지) 대신
  `--eco`(모델 `gpt-5.6-luna`, Plus에서 5시간당 250~2,000개 메시지)을
  사용하세요.
- API 호출보다 **느립니다**. 직접 호출 시 몇 초면 되는 완전한 README 하나에 약 45초가
  걸립니다.
- **CI에서는 거부됩니다**(`CI` 또는 `GITHUB_ACTIONS`가 정의된 경우).
  구독 인증은 공유 러너를 대상으로 설계되지 않았으며, OpenAI도 공개 저장소에서 이
  워크플로를 사용하지 않을 것을 권장합니다. 이 경로에서는 API 키를 사용하세요.
- 환경 변수: `CODEX_BIN`(바이너리의 명시적 경로) 및 `CODEX_TIMEOUT`(세그먼트당
  초, 기본값 `600`).

### Grok 구독으로 번역(`--use_grok_cli`)

공식 **Grok Build** CLI를 사용하는 `--use_codex`와 동일한 원리입니다. 번역 비용은
토큰 단위로 청구되지 않고 Grok 구독(SuperGrok / X Premium+)의 할당량에서 차감됩니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**격리 — 사용 전에 읽으세요.** 이 Provider는 구조적으로 `--use_codex`보다
**보안 수준이 낮으며**, 이는 의도된 사항입니다.

- Codex는 시스템이 강제하는 경계인 `--sandbox read-only`에서 실행됩니다.
- Grok 샌드박스는 최근의 많은 Linux 시스템에서 적용되지 않을 수 있습니다.
  Ubuntu 24.04부터 AppArmor가 권한 없는 사용자 네임스페이스를 차단하며,
  `/run/podman`가 `0700`일 때 컨테이너 런타임 소켓 거부 목록도 실패합니다.
  그런데 적용할 수 없는 **통합** 프로필은 조용히 **격리되지 않은 상태로** 시작됩니다.
- 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않으며, 조용히 대체하지도 않습니다.
  경고를 표시합니다. 격리는 CLI의 `--deny` 규칙(`*` catch-all
  포함)에 의존합니다. 이는 측정된 유일한 _fail-closed_ 계층으로, 알 수 없는 규칙이
  보호 기능을 알리지 않고 제거하는 대신 시작을 거부하게 합니다.
- OS 샌드박스를 **강제**하려면 `GROK_TRANSLATE_SANDBOX=read-only`를 사용하세요. 시스템이 이를
  준수할 수 없으면 시작이 실패하며, 이것이 의도된 동작입니다.

**할당량**: Grok 풀은 Chat, Imagine, Voice와 **주 단위로 공유**되며, 이를 조회할 수 있는
명령은 없습니다. 따라서 일괄 처리가 아무런 표시 없이 대화 사용량을 소모할 수 있습니다.
이 때문에 동시 실행 수를 2로 제한하고 `regen_translations.sh`에 경고를 표시합니다.

기타 변수: `GROK_BIN`(바이너리 경로), `GROK_TIMEOUT`(기본값 900초).

28개 번역을 재생성하려면 다음을 실행합니다.

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### 경제 모드

더 빠르고 저렴한 모델(gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite)을 사용합니다.

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션 | 설명 |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file` | 번역할 단일 Markdown 파일 |
| `--source_dir` | Markdown 파일이 포함된 소스 디렉터리 |
| `--target_dir` | 번역된 파일의 출력 디렉터리 |
| `--source_lang` | 소스 언어(기본값: `fr`) |
| `--target_lang` | 대상 언어(기본값: `en`) |
| `--model` | 사용할 특정 모델 |
| `--eco` | 경제 모델 사용 |
| `--use_mistral` | Mistral AI API 사용 |
| `--use_claude` | Claude API 사용 |
| `--use_gemini` | Gemini API 사용 |
| `--use_codex` | ChatGPT 구독 할당량으로 Codex CLI 사용 |
| `--use_grok` | xAI API(Grok) 사용 — `XAI_API_KEY` 필요 |
| `--use_grok_cli` | Grok 구독 할당량으로 Grok CLI 사용 |
| `--force` | 재번역 강제 |
| `--keep_filename` | 원래 파일 이름 유지 |
| `--news` | 뉴스 모드: 영어 인용문 보호, 언어별 국기 처리 |
| `--add_translation_note` | 번역 참고 사항 추가 |
| `--note_position` | 참고 사항 위치: `top`, `bottom`(기본값) 또는 `both` |
| `--note_format` | 참고 사항 형식: `legacy`(기본값, 굵은 문단) 또는 `marker` |
| `--include_model` | 출력 파일에 모델 이름 포함 |
| `--reasoning_effort` | GPT-5.x 추론 수준: `none`/`low`/`medium`/`high`/`xhigh` |

> **6개의 Provider 플래그는 서로 배타적입니다.** 이전에는 두 개를 함께 사용해도
> 조용히 허용되었고 첫 번째로 테스트된 항목이 선택되었습니다. 따라서 구독 할당량으로
> 요청한 번역(`--use_codex`, `--use_grok_cli`)이 아무런 경고 없이 사용량 기반 과금으로
> 처리될 수 있었습니다. 이제 `argparse`는 이러한 조합을 거부합니다.

### 번역 참고 사항: 위치 및 형식

`--add_translation_note`를 사용하면 translator가 참고 사항을 위, 아래 또는 양쪽에 배치할 수
있으며, 일반 텍스트 형식(하위 호환) 또는 Markdown 플러그인이 처리할 수 있는
`marker` 형식으로 만들 수 있습니다.

**위치**(`--note_position`):

- `bottom`(기본값): 기존과 같이 파일 끝에 참고 사항을 추가합니다.
- `top`: **YAML front matter 뒤에** 참고 사항을 삽입합니다(Astro Content Collections,
  gray-matter 등의 안전한 처리를 위해).
- `both`: 위와 아래에 모두 참고 사항을 삽입합니다(LLM 호출 한 번으로 내용을
  재사용하여 두 위치에 배치).

**형식**(`--note_format`):

- `legacy`(기본값): 굵은 문단 `**...**` — v1.8과 완전히 동일한 동작(byte-for-byte).
  Hugo, GitHub, GitLab 및 모든 Markdown renderer와 호환됩니다.
- `marker`: 보이지 않는 Markdown link reference definition(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에
  굵은 blockquote를 추가합니다. GitHub/GitLab에서 기본적으로 읽을 수 있으며, Astro 측의
  remark 플러그인이 빌드 시 처리하여 스타일이 적용된 배너를 만들 수 있습니다
  (jls42.org 블로그 참조).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### 기본 모델(2026년)

| Provider | 품질(기본값) | 경제 모드(`--eco`) |
| -------- | ---------------------- | ----------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |

> **장문 번역 권장 사항**: `--use_gemini`(기본값 = `gemini-3.7-flash`)는
> 라틴 문자가 아닌 언어(PL, JA, ZH, AR, HI)의 스크립트에서 Markdown 구조를 충실하게
> 보존하며, `--news` 모드에서도 placeholder의 정확성을 유지합니다. 일본어로
> 번역한 이 README에서 측정한 결과, 약 6배 더 짧은 지연 시간으로 `gemini-3.1-pro-preview`와
> 동일한 구조(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존)를
> 유지했습니다. OpenAI는 하위 호환성을 위해 계속 기본값으로 사용됩니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

**gpt-5.6-luna로 프랑스어에서 한국어로 번역된 기사.**
