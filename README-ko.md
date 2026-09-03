# AI 기반 Markdown 번역기

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 코드 품질</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="품질 게이트 상태"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="보안 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="신뢰성 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="유지 관리성 등급"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="커버리지"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="취약점"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="버그"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 냄새"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복 코드 비율 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 줄 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini**, **Grok (xAI)**를 사용하는 Markdown 파일 번역기입니다. API를 사용하거나, 사용량별 과금 없이 ChatGPT (Codex) 또는 Grok 구독 할당량으로 사용할 수 있습니다.

이 Python 스크립트는 서식, 코드 블록 및 front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **다중 Provider**: 5개 API (OpenAI, Mistral, Claude, Gemini, Grok) + 사용량별 과금 없는 2개 구독 CLI — Codex (ChatGPT) 및 Grok
- **2026 모델**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 파일 하나를 번역하기 위한 `--file` 옵션
- **지능형 세분화**: 모델별 토큰 제한을 고려한 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드 (`` `...` ``) 보존
- **파일 이름**: 원본 이름을 유지하기 위한 `--keep_filename` 옵션
- **News 모드**: 뉴스 기사에서 영어 인용문을 보호하고 언어별 국기를 처리하기 위한 `--news` 옵션
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 메모**: 문서 끝에 선택적으로 메모 추가

## 설치

### 도구 사용

```bash
pip install ai-powered-markdown-translator
```

이제 `aipmt` 명령을 어디서나 사용할 수 있습니다. Python 스크립트 디렉터리가
`PATH`에 없다면 `python -m aipmt`이 정확히 같은 작업을 수행합니다. Python 3.10
이상 필요합니다.

다른 패키지와 분리된 설치를 사용하려면 다음을 실행합니다.

```bash
pipx install ai-powered-markdown-translator
```

### 프로젝트에 기여

개발하려면 복제한 저장소가 여전히 필요합니다. 테스트, 28개 번역 및 모든 품질 도구가
이곳에 있습니다.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`은 테스트된 환경을 정확히 반영하는 **완전히 고정된 lock 파일**입니다.
`pyproject.toml`에 게시된 범위는 의도적으로 더 넓게 설정되어 있으며, 다른 패키지에
아무것도 강제하지 않습니다.

### 품질 도구 (선택 사항이지만 권장)

이 프로젝트는 서식이 잘못되었거나 취약하거나 비밀 정보가 포함된 코드의 커밋을 방지하기 위해
[`pre-commit`](https://pre-commit.com)을 사용합니다. 설치 방법:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성화된 Hook: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard
(복잡도), detect-secrets (API 키), mypy (점진적 타입 지정), Opengrep (SAST), pip-audit
(CVE 의존성), unittest. 자세한 내용은 `CLAUDE.md`의 _Quality / pre-commit_ 섹션을
참조하세요.

## 구성

키는 우선순위가 높은 순서대로 **세 곳**에서 검색됩니다.
각 위치는 이전 위치에서 비어 있는 부분만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일시적인 예외 |
| 2   | 현재 디렉터리(또는 상위 디렉터리)의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | **한 번 설치하면 어디서나 사용**   |

`pip install` 이후에는 세 번째 방법이 가장 간단합니다.

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

이 파일은 변수가 절대 경로를 가리킬 때 `XDG_CONFIG_HOME`을 따르며
(그렇지 않으면 사양에 따라 무시됨), Windows에서는 `%APPDATA%`을 따릅니다.

저장소에 자체 키가 있을 때는 두 번째 방법도 유용합니다. 저장소 루트의
`.env`은 사용자 구성을 변경하지 않고도 사용자 구성보다 우선합니다.
환경에 이미 정의된 변수는 두 구성보다 우선합니다.

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

키를 찾지 못하면 명령은 호출 추적을 표시하지 않고 정확한 경로와 함께 세 위치를 나열합니다.

`GEMINI_API_KEY`은 `GOOGLE_API_KEY`의 대안으로 허용됩니다 (AI
Studio 규칙). 선택적 변수: `XAI_BASE_URL` (xAI 엔드포인트, 기본값
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (Anthropic 호출당 초, 기본값
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
그리고 `GROK_TRANSLATE_SANDBOX` (Grok CLI 섹션 참조). `regen_translations.sh` 측에서는
`REGEN_PROVIDER`, `REGEN_MODEL`, 그리고 `REGEN_JOB_TIMEOUT` (작업당 제한, 기본값 600초)을
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

### ChatGPT 구독으로 번역 (`--use_codex`)

이 Provider는 API 키를 사용하지 않습니다. 공식 Codex CLI를 비대화형 모드로 제어하므로,
번역 비용은 이미 결제한 ChatGPT 구독(Plus, Pro, Business 등)의 할당량에서 차감됩니다.
이는 이 용도를 위해 OpenAI가 문서화한 유일한 방법입니다. `~/.codex/auth.json`의 토큰은
Platform API 호출을 인증하지 않으며, 이 스크립트는 해당 토큰을 읽지도 않습니다.

**사전 요구 사항:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

바이너리는 다음 순서로 검색됩니다: `CODEX_BIN` 변수, `PATH`,
그다음 Python 패키지 `openai-codex-cli-bin`. 마지막 패키지는 의도적으로 `requirements.txt`에
포함되지 않습니다. 용량이 약 250MB이므로 선택적 Provider를 위해 모든 사용자에게
설치를 강제하게 되기 때문입니다.

**알아둘 점:**

- **API 키는 사용되지 않습니다.** `OPENAI_API_KEY` 및 `CODEX_API_KEY`은 하위 프로세스의
  환경에서 제거되므로, `.env`에 키가 있어도 번역이 사용량별 과금으로 전환되지
  않습니다.
- **세그먼트 하나는 요금제의 5시간 창에서 하나의 « 로컬 메시지 »입니다.**
  품질 모델(`gpt-5.6-sol`, 5시간당 10~100개 메시지)보다
  `--eco` (모델 `gpt-5.6-luna`, Plus에서 5시간당 250~2,000개 메시지)을
  사용하세요.
- API 호출보다 **느립니다**. 실시간 호출에서는 몇 초면 되는 완전한 README에 약 45초가
  걸립니다.
- CI에서는 거부됩니다 (`CI` 또는 `GITHUB_ACTIONS`이 정의된 경우). 구독 인증은
  공유 runner용이 아니며, OpenAI는 공개 저장소에서 이 workflow를 권장하지 않습니다.
  이 경로에서는 API 키를 사용하세요.
- 환경 변수: `CODEX_BIN` (바이너리의 명시적 경로) 및 `CODEX_TIMEOUT` (세그먼트당 초,
  기본값 `600`).

### Grok 구독으로 번역 (`--use_grok_cli`)

`--use_codex`와 동일한 원리이며, 공식 **Grok Build** CLI를 사용합니다. 번역은 토큰별로
과금되지 않고 Grok 구독(SuperGrok / X Premium+) 할당량에서 차감됩니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**격리 — 사용 전에 읽으세요.** 이 Provider는 구조적으로 **`--use_codex`보다
취약**하며, 이는 의도된 설계입니다.

- Codex는 시스템이 강제하는 경계인 `--sandbox read-only`에서 실행됩니다.
- Grok의 sandbox는 최근 많은 Linux 환경에서 적용되지 않을 수 있습니다. Ubuntu 24.04부터
  AppArmor가 권한 없는 user namespace를 차단하며, `/run/podman`가 `0700`인
  경우 컨테이너 runtime 소켓의 deny-list도 실패합니다. 그런데 적용할 수 없는 **통합**
  프로필은 **조용히 비격리 상태로** 시작됩니다.
- 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않으며, **절대로 조용히 대체하지
  않습니다**. 경고를 표시합니다. 격리는 CLI의 `--deny` 규칙(`*`
  catch-all 포함)에 의존합니다. 이는 측정된 유일한 _fail-closed_ 계층으로, 알 수 없는
  규칙이 보호 기능을 알리지 않고 제거하는 대신 시작을 거부하게 합니다.
- OS sandbox를 **강제**하려면 `GROK_TRANSLATE_SANDBOX=read-only`를 사용하세요. 시스템이 이를 적용할 수 없으면
  시작이 실패하며, 이것이 의도된 동작입니다.

**할당량**: Grok 풀은 **주간 단위이며** Chat, Imagine, Voice와 공유되고, 이를 읽을 수 있는
명령은 없습니다. 따라서 일괄 처리가 아무런 표시 없이 대화 사용량을 줄일 수 있습니다.
이 때문에 동시성이 2로 제한되며 `regen_translations.sh`에 경고가 표시됩니다.

기타 변수: `GROK_BIN` (바이너리 경로), `GROK_TIMEOUT` (기본값 900초).

28개 번역을 재생성하려면:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### 경제 모드

더 빠르고 저렴한 모델을 사용합니다 (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite).

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션                   | 설명                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 번역할 단일 Markdown 파일                                       |
| `--source_dir`           | Markdown 파일이 포함된 원본 디렉터리                        |
| `--target_dir`           | 번역된 파일의 출력 디렉터리                          |
| `--source_lang`          | 원본 언어 (기본값: `fr`)                                             |
| `--target_lang`          | 대상 언어 (기본값: `en`)                                              |
| `--model`                | 사용할 특정 모델                                             |
| `--eco`                  | 경제적인 모델 사용                                         |
| `--use_mistral`          | Mistral AI API 사용                                                |
| `--use_claude`           | Claude API 사용                                                    |
| `--use_gemini`           | Gemini API 사용                                                    |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용               |
| `--use_grok`             | xAI (Grok) API 사용 — `XAI_API_KEY` 필요                      |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                   |
| `--force`                | 재번역 강제                                                  |
| `--keep_filename`        | 원본 파일 이름 유지                                     |
| `--news`                 | 뉴스 모드: EN 인용문 보호, 언어별 국기 처리 |
| `--add_translation_note` | 번역 메모 추가                                           |
| `--note_position`        | 메모 위치: `top`, `bottom` (기본값), 또는 `both`                |
| `--note_format`          | 메모 형식: `legacy` (기본값, 굵은 단락) 또는 `marker`       |
| `--include_model`        | 출력 파일에 모델 이름 포함                       |
| `--reasoning_effort`     | GPT-5.x 추론 노력: `none`/`low`/`medium`/`high`/`xhigh`    |

> **여섯 개 Provider 플래그는 상호 배타적입니다.** 이전에는 두 개를 함께 사용해도
> 조용히 허용되었으며, 먼저 검사한 항목으로 처리되었습니다. 그 결과 구독 할당량으로
> 요청한 번역(`--use_codex`, `--use_grok_cli`)이 경고 없이 사용량별 과금으로 처리될 수
> 있었습니다. 이제 `argparse`은 이 조합을 거부합니다.

### 번역 메모: 위치 및 형식

`--add_translation_note`을 사용하면 translator가 메모를 위, 아래 또는 양쪽에 배치할 수 있으며,
일반 텍스트 형식(하위 호환) 또는 Markdown plugin에서 사용할 수 있는 `marker`
형식으로 작성할 수 있습니다.

**위치** (`--note_position`):

- `bottom` (기본값): 기존 방식과 같이 파일 끝에 메모를 추가합니다.
- `top`: **YAML frontmatter 뒤에** 메모를 삽입합니다 (Astro Content Collections,
  gray-matter 등의 안전성).
- `both`: 위와 아래에 모두 메모를 삽입합니다 (LLM 호출 한 번으로 동일한 내용을
  두 위치에 재사용).

**형식** (`--note_format`):

- `legacy` (기본값): 굵은 단락 `**...**` — v1.8과 완전히 동일한 동작이며
  byte-for-byte 호환됩니다. Hugo, GitHub, GitLab 및 모든 Markdown renderer와 호환됩니다.
- `marker`: 보이지 않는 Markdown link reference definition
  (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 굵은 blockquote를 배치합니다. GitHub/GitLab에서 기본적으로
  읽을 수 있으며, Astro 측 remark plugin이 빌드 시 이를 활용해 스타일이 적용된 배너를
  생성할 수 있습니다 (jls42.org 블로그 참조).

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

### 기본 모델 (2026)

| Provider | 품질 (기본값)       | 경제적 (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **장문 번역 권장 사항**: `--use_gemini` (기본값 = `gemini-3.7-flash`)은 라틴 문자가
> 아닌 언어(PL, JA, ZH, AR, HI)의 스크립트에서도 Markdown 구조를 충실하게 보존합니다.
> placeholder 보존이 중요한 `--news` 모드에서도 마찬가지입니다. 일본어로 번역한
> 이 README에서 측정한 결과, 약 6배 더 짧은 지연 시간으로 `gemini-3.1-pro-preview`와 동일한
> 구조(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존)를
> 유지했습니다. 하위 호환성을 위해 OpenAI가 여전히 기본값입니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그 (15개 언어)

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

**gpt-5.6-luna로 프랑스어에서 한국어로 번역된 글.**
