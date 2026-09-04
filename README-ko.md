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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 악취"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복 코드 줄 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 줄 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini**, **Grok (xAI)**를 사용하는 Markdown 파일 번역기입니다. API, 사용량에 따른 별도 과금 없이 ChatGPT (Codex) 또는 Grok 구독 할당량, 또는 **OpenCode** 오픈 소스 에이전트를 통해 원하는 공급자로 번역할 수 있습니다. 공급자는 로컬 모델(Ollama), 무료 모델, 구독(GitHub Copilot 등) 또는 API 키를 사용할 수 있습니다.

이 Python 스크립트는 서식, 코드 블록, front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **다중 공급자**: 5개 API(OpenAI, Mistral, Claude, Gemini, Grok) + 사용량에 따른 별도 과금이 없는 2개의 구독 CLI — Codex (ChatGPT)와 Grok — + OpenCode(open source, MIT)를 통해 OpenCode에 구성된 모든 공급자 및 로컬 모델 사용 가능
- **2026년 모델**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 파일 하나만 번역하기 위한 `--file` 옵션
- **스마트 세분화**: 모델별 토큰 제한을 고려한 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드(`` `...` ``) 보존
- **파일 이름**: 원래 파일 이름을 유지하기 위한 `--keep_filename` 옵션
- **News 모드**: 뉴스 기사에서 영어 인용문을 보호하고 국기를 처리하기 위한 `--news` 옵션
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 메모**: 문서 끝에 선택적으로 메모 추가

## 설치

### 도구 사용

```bash
pip install ai-powered-markdown-translator
```

이제 `aipmt` 명령을 어디서나 사용할 수 있습니다. Python 스크립트 디렉터리가
`PATH`에 없다면 `python -m aipmt`이 정확히 같은 작업을 수행합니다. Python 3.10
이상 버전이 필요합니다.

다른 패키지와 격리된 설치를 사용하려면 다음을 실행합니다.

```bash
pipx install ai-powered-markdown-translator
```

### 프로젝트에 기여

개발하려면 복제한 저장소가 여전히 필요합니다. 테스트, 28개 번역본,
모든 품질 도구가 이곳에 있습니다.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`은 테스트된 환경을 정확히 반영하는 **완전히 고정된 lock 파일**입니다.
`pyproject.toml`에 게시된 범위는 의도적으로 더 넓게 설정되어 있으며, 다른 패키지에
아무것도 강제하지 않습니다.

### 품질 도구(선택 사항이지만 권장)

이 프로젝트는 서식이 잘못되었거나 취약하거나 비밀이 포함된 코드의 커밋을 막기 위해
[`pre-commit`](https://pre-commit.com)을 사용합니다. 설치 방법은 다음과 같습니다.

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성화된 훅: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard(복잡도), detect-secrets(API 키), mypy(점진적 타입 검사), Opengrep(SAST), pip-audit(CVE deps), unittest. 자세한 내용은 `CLAUDE.md`의 _Quality / pre-commit_ 섹션을 참조하세요.

## 구성

키는 우선순위가 높은 순서에서 낮은 순서로 **세 곳**에서 검색됩니다.
각 위치는 이전 위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일시적인 재정의 |
| 2   | 현재 디렉터리의 `.env`(또는 상위 디렉터리) | 프로젝트별 키            |
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

이 파일은 변수가 절대 경로를 가리킬 때 `XDG_CONFIG_HOME`을 따르며,
그렇지 않으면 사양에 따라 무시됩니다. Windows에서는 `%APPDATA%`을 따릅니다.

저장소에 자체 키가 있을 때는 두 번째 방법이 유용합니다. 저장소 루트의
`.env`은 사용자 구성을 변경하지 않고도 사용자 구성보다 우선합니다.
환경에 이미 정의된 변수는 두 설정 모두보다 우선합니다.

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

키를 찾지 못하면 명령은 호출 추적을 표시하지 않고 세 위치와 정확한 경로를 나열합니다.

`GEMINI_API_KEY`은 `GOOGLE_API_KEY`의 대안으로 사용할 수 있습니다(AI
Studio 규칙). 선택적 변수: `XAI_BASE_URL`(xAI 엔드포인트, 기본값
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(Anthropic 호출당 초, 기본값
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX`(Grok CLI 섹션 참조), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT`(OpenCode 섹션 참조). `regen_translations.sh` 측면에서는
`REGEN_PROVIDER`, `REGEN_MODEL`, `REGEN_JOB_TIMEOUT`(작업당 제한, 기본값 600초)가
사용됩니다.

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### ChatGPT 구독으로 번역(`--use_codex`)

이 공급자는 API 키를 사용하지 않습니다. 공식 Codex CLI를 비대화형 모드로
제어하므로 번역 비용은 이미 결제한 ChatGPT 구독(Plus, Pro, Business 등)의
할당량에서 차감됩니다. 이는 이 용도에 대해 OpenAI가 문서화한 유일한 방법입니다.
`~/.codex/auth.json`의 토큰은 Platform API 호출을 인증하지 않으며, 이 스크립트는
해당 토큰을 읽지도 않습니다.

**사전 요구 사항:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

바이너리는 다음 순서로 검색됩니다: `CODEX_BIN` 변수, `PATH`,
그다음 Python 패키지 `openai-codex-cli-bin`. 마지막 패키지는 의도적으로
`requirements.txt`에 포함되지 않습니다. 약 250MB이므로 선택적 공급자를 위해
모든 사용자에게 설치를 강제하게 되기 때문입니다.

**알아둘 점:**

- **API 키는 사용되지 않습니다.** `OPENAI_API_KEY`와 `CODEX_API_KEY`은
  하위 프로세스의 환경에서 제거됩니다. 따라서 `.env`에 키가 있어도
  번역이 사용량 기반 과금으로 전환되지 않습니다.
- **세그먼트 하나는 요금제의 5시간 창에서 하나의 ‘로컬 메시지’입니다.**
  품질 모델(`gpt-5.6-sol`, Plus에서 5시간당 10~100개 메시지)보다
  `--eco`(모델 `gpt-5.6-luna`, Plus에서 5시간당 250~2,000개 메시지)을
  사용하세요.
- API를 직접 호출하는 것보다 **느립니다**. 완전한 README 하나에 약 45초가
  걸리며, 직접 호출하면 몇 초면 됩니다.
- CI에서 거부됩니다(`CI` 또는 `GITHUB_ACTIONS`이 정의된 경우).
  구독 인증은 공유 러너용으로 설계되지 않았고 OpenAI도 공개 저장소에서 이
  워크플로를 사용하지 말 것을 권장합니다. 이 경로에서는 API 키를 사용하세요.
- 환경 변수: `CODEX_BIN`(바이너리의 명시적 경로), `CODEX_TIMEOUT`(세그먼트당
  초, 기본값 `600`).

### Grok 구독으로 번역(`--use_grok_cli`)

`--use_codex`와 동일한 원리로 공식 **Grok Build** CLI를 사용합니다. 번역은
토큰별로 과금되지 않고 Grok 구독(SuperGrok / X Premium+)에서 차감됩니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**격리 — 사용 전에 읽으세요.** 이 공급자는 구조적으로 `--use_codex`보다
**약하며**, 이는 의도된 사항입니다.

- Codex는 시스템이 강제하는 경계인 `--sandbox read-only`에서 실행됩니다.
- 최근 Linux 환경에서는 Grok 샌드박스가 많은 시스템에 적용되지 않을 수 있습니다.
  Ubuntu 24.04부터 AppArmor가 권한 없는 사용자 네임스페이스를 차단하며,
  `/run/podman`이 `0700`일 때 컨테이너 런타임 소켓의 거부 목록도
  실패합니다. 그런데 적용할 수 없는 **통합** 프로필은 아무 알림 없이
  **격리되지 않은 상태로** 시작됩니다.
- 따라서 스크립트는 기본적으로 프로필을 요청하지 않으며, 절대로 조용히
  대체하지 않습니다. 경고를 표시합니다. 격리는 CLI의 `--deny` 규칙
  (catch-all인 `*` 포함)에 의존합니다. 이는 측정된 유일한
  _fail-closed_ 계층으로, 알 수 없는 규칙이 보호를 알리지 않고 제거하는 대신
  시작을 거부하게 합니다.
- OS 샌드박스를 **강제**하려면 `GROK_TRANSLATE_SANDBOX=read-only`을 사용하세요. 시스템이 이를
  적용할 수 없으면 시작이 실패하며, 이것이 의도된 동작입니다.

**할당량**: Grok 풀은 **주간 단위이며** Chat, Imagine, Voice와 공유되고,
이를 확인할 수 있는 명령은 없습니다. 따라서 배치 처리가 아무런 표시 없이
대화 사용량을 소모할 수 있습니다. 이 때문에 동시 실행 수를 2로 제한하고
`regen_translations.sh`에 경고를 표시합니다.

기타 변수: `GROK_BIN`(바이너리 경로), `GROK_TIMEOUT`(기본값 900초).

28개 번역본을 다시 생성하려면 다음을 실행합니다.

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### OpenCode로 원하는 공급자를 사용해 번역(`--use_opencode`)

[OpenCode](https://opencode.ai)는 터미널에서 실행되는 **오픈 소스(MIT) 코드 에이전트**입니다.
모델 공급자는 아니며, OpenCode 자체에 구성한 공급자로 연결하는 **라우터**입니다.
API 키, 구독(GitHub Copilot, ChatGPT, SuperGrok), 무료 모델을 **계정 없이**
제공하는 OpenCode Zen 게이트웨이, 또는 로컬 모델(Ollama, LM Studio, llama.cpp)을
사용할 수 있습니다. 이 공급자는 `opencode run`을 비대화형 모드로 제어하고,
도구 없이 단 한 번의 왕복으로 호출을 제한합니다.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model`은 `provider/modèle` 형식으로 **필수**입니다. OpenCode는 공급자가
아니며, 사용자를 대신해 기본값을 선택하지 않습니다. 자체 대체 동작은 대화가
학습에 사용될 수 있는 무료 모델일 수 있습니다.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**격리 — 스크립트가 호출마다 수행하는 작업:**

- 사용자의 설정보다 우선하는 인라인 구성(`OPENCODE_CONFIG_CONTENT`)은 `aipmt`
  에이전트를 정의하고 **모든 도구를 거부**합니다(`permission: { "*": "deny" }`).
  모델은 읽거나 쓰거나 명령을 실행할 수 없으며, 측정 결과 실제로 이를 시도하지도
  않습니다. 세션 공유는 비활성화되고, `--pure`가 외부 플러그인을
  차단하며, `--auto`은 절대 사용하지 않습니다.
- 호출은 `OPENCODE_DISABLE_PROJECT_CONFIG` 및 `OPENCODE_DISABLE_CLAUDE_CODE` 스위치와 함께 **비어 있는 임시
  디렉터리**에서 실행됩니다. 이 스위치가 없으면 OpenCode는 현재 디렉터리의
  `AGENTS.md`과 사용자의 `~/.claude/CLAUDE.md`을 모든 프롬프트에 주입합니다.
  측정 결과, `AGENTS.md`에 넣어 둔 “모든 응답을 BANANA로 끝내라”라는
  지시가 번역에 적용되었습니다. 반면 `~/.config/opencode/AGENTS.md`의 전역 규칙은 계속
  적용됩니다. OpenCode에서는 이를 제외할 수 없습니다.
- 출력 계약은 다음을 모두 요구합니다. 반환 코드 0, `error` 이벤트 없음,
  도구 호출 없음, `stop`으로 종료된 마지막 단계, 비어 있지 않은 텍스트,
  실제로 로드된 에이전트. 알 수 없는 `--agent`은 OpenCode를 실패시키지
  않고 도구가 활성화된 코딩 에이전트로 **조용히 대체**됩니다. 이 경우
  `exit 0`도 아무것도 입증하지 않습니다.
- **aipmt 키는 하위 프로세스에 전달되지 않습니다.** Codex 및 Grok과 동일하게
  필터링되며, 유일한 명시적 예외는 OpenCode 자체의 키인 `OPENCODE_API_KEY`입니다
  (Zen, Go). 공급자는 `.env`이 아니라 OpenCode(`opencode auth login`,
  `opencode.json`)에서 구성합니다.

**알아둘 점:**

- Zen의 무료 모델은 변동하는 ‘stealth’ 또는 기여자 모델이며 제한 사항이
  문서화되지 않았고, 대화가 학습에 사용될 수 있습니다. 공개 문서에는 적합하지만
  비공개 콘텐츠에는 피해야 합니다. 측정 결과 `opencode/mimo-v2.5-free`은 이 README를
  한 번에 번역했지만, `opencode/big-pickle`은 더 느렸고 두 개의 동시 요청은 응답 없이
  남았습니다.
- 로컬 모델은 최소 **16k 컨텍스트**를 제공해야 합니다. 세그먼트 길이가 최대
  16,000자이기 때문입니다. 반면 Ollama는 기본값으로 4,096을 설정하는 경우가
  많습니다. Ollama에서는 `PARAMETER num_ctx 32768`과 함께 `Modelfile`을 사용한 후
  `ollama create`를 실행하세요. 품질은 모델에 따라 달라집니다. 테스트 파일에서
  7B 모델은 목록 순서를 뒤집고 코드 블록 닫기를 손상시켰지만, 게이트웨이 모델은
  모든 것을 보존했습니다.
- `--eco`은 효과가 없습니다(`--model`의 모델이 사용됨).
  `--reasoning_effort`는 OpenCode의 `--variant`으로 그대로 전달되므로, 모델이
  이를 알고 있을 때만 요청해야 합니다.
- 세션은 모든 OpenCode 세션과 마찬가지로 OpenCode 데이터베이스
  (`~/.local/share/opencode/`)에 기록됩니다.
- 환경 변수: `OPENCODE_BIN`(바이너리의 명시적 경로, 그렇지 않으면
  `PATH` 다음에 `~/.opencode/bin/opencode`), `OPENCODE_TIMEOUT`(세그먼트당 초,
  기본값 `600`). 내보낸 경우 `OPENCODE_CONFIG`이 적용됩니다.

### 경제 모드

더 빠르고 저렴한 모델(gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite)을 사용합니다.

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### 옵션

| 옵션 | 설명 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file` | 번역할 단일 Markdown 파일 |
| `--source_dir` | Markdown 파일이 포함된 소스 디렉터리 |
| `--target_dir` | 번역된 파일의 출력 디렉터리 |
| `--source_lang` | 소스 언어 (기본값: `fr`) |
| `--target_lang` | 대상 언어 (기본값: `en`) |
| `--model` | 사용할 특정 모델 |
| `--eco` | 경제적인 모델 사용 |
| `--use_mistral` | Mistral AI API 사용 |
| `--use_claude` | Claude API 사용 |
| `--use_gemini` | Gemini API 사용 |
| `--use_codex` | ChatGPT 구독 할당량으로 Codex CLI 사용 |
| `--use_grok` | xAI (Grok) API 사용 — `XAI_API_KEY` 필요 |
| `--use_grok_cli` | Grok 구독 할당량으로 Grok CLI 사용 |
| `--use_opencode` | OpenCode에서 구성된 공급자로 OpenCode(오픈 소스) 사용; `--model provider/modèle` 필요 |
| `--force` | 재번역 강제 |
| `--keep_filename` | 원본 파일 이름 유지 |
| `--news` | 뉴스 모드: EN 인용문을 보호하고 언어별 플래그 처리 |
| `--add_translation_note` | 번역 메모 추가 |
| `--note_position` | 메모 위치: `top`, `bottom` (기본값) 또는 `both` |
| `--note_format` | 메모 형식: `legacy` (기본값, 굵은 단락) 또는 `marker` |
| `--include_model` | 출력 파일에 모델 이름 포함 |
| `--reasoning_effort` | GPT-5.x 추론 노력: `none`/`low`/`medium`/`high`/`xhigh` |

> **공급자 플래그 7개는 상호 배타적입니다.** 두 개를 함께 지정해도 이전에는 조용히 허용되었으며, 먼저 검사된 항목으로 처리되었습니다. 따라서 구독 할당량으로 요청한 번역(`--use_codex`, `--use_grok_cli`)이 아무런 경고 없이 사용량 기반 과금으로 처리될 수 있었습니다.
> 이제 `argparse`는 이러한 조합을 거부합니다.

### 번역 메모: 위치 및 형식

`--add_translation_note`를 사용하면 translator가 메모를 위쪽, 아래쪽 또는 양쪽에 배치할 수 있으며, 일반 텍스트 형식(하위 호환) 또는 Markdown 플러그인이 사용할 수 있는 `marker` 형식으로 작성할 수 있습니다.

**위치** (`--note_position`):

- `bottom` (기본값): 기존 방식처럼 파일 끝에 메모를 추가합니다.
- `top`: **YAML frontmatter 뒤**에 메모를 삽입합니다(Astro Content Collections, gray-matter 등과의 호환성).
- `both`: 위쪽과 아래쪽에 모두 메모를 삽입합니다(LLM 호출은 한 번만 수행하고 내용을 두 위치에 재사용).

**형식** (`--note_format`):

- `legacy` (기본값): 굵은 단락 `**...**` — v1.8과 바이트 단위로 완전히 동일한 동작입니다. Hugo, GitHub, GitLab 및 모든 Markdown renderer와 호환됩니다.
- `marker`: 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 굵은 blockquote를 추가합니다. GitHub/GitLab에서 기본적으로 읽을 수 있으며, Astro 측 remark 플러그인이 빌드 시 이를 활용해 스타일이 적용된 배너를 생성할 수 있습니다(jls42.org 블로그 참조).

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

### 기본 모델(2026)

| 공급자 | 품질(기본값) | 경제형 (`--eco`) |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |
| OpenCode | 필수 `--model provider/modèle` | 동일 — `--eco`은 효과 없음 |

> **장문 번역 권장 사항**: `--use_gemini` (기본값 = `gemini-3.7-flash`)은 비라틴 문자 스크립트(PL, JA, ZH, AR, HI)에서 Markdown 구조를 충실하게 보존하며, placeholder의 정확성이 중요한 `--news` 모드에서도 마찬가지입니다. 일본어로 번역한 이 README를 기준으로 측정한 결과, 약 6배 낮은 지연 시간으로 `gemini-3.1-pro-preview`와 동일한 구조(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존)를 유지했습니다. 하위 호환성을 위해 OpenAI가 여전히 기본값입니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX  
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

**gpt-5.6-luna를 사용하여 프랑스어에서 한국어로 번역된 기사.**
