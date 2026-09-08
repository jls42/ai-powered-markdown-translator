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

**OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini**, **Grok (xAI)**을 사용하는 Markdown 파일 번역기입니다. API를 사용하거나, 사용량에 따른 과금 없이 ChatGPT (Codex) 또는 Grok 구독 할당량을 이용하거나, 오픈 소스 에이전트인 **OpenCode**를 통해 로컬 모델(Ollama), 무료 제공자, 구독(GitHub Copilot 등), 키 방식 등 원하는 제공자를 사용할 수 있습니다.

이 Python 스크립트는 서식, 코드 블록 및 front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **다중 제공자**: 5개 API(OpenAI, Mistral, Claude, Gemini, Grok) + 사용량에 따른 과금 없이 구독으로 사용하는 2개 CLI인 Codex (ChatGPT)와 Grok + OpenCode에 구성된 모든 제공자와 로컬 모델을 지원하는 OpenCode(오픈 소스, MIT)
- **2026년 모델**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하는 `--eco` 옵션
- **단일 파일**: 파일 하나만 번역하는 `--file` 옵션
- **지능형 분할**: 모델별 token 제한에 맞춰 긴 텍스트 처리
- **코드 보존**: 코드 블록과 inline code(`` `...` ``) 보존
- **파일 이름**: 원래 이름을 유지하는 `--keep_filename` 옵션
- **뉴스 모드**: 뉴스 기사에서 영어 인용문을 보호하고 국기 이모지를 처리하는 `--news` 옵션
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 주석**: 문서 끝에 선택적으로 주석 추가

## 설치

### 도구 사용

```bash
pip install ai-powered-markdown-translator
```

이제 `aipmt` 명령을 어디서나 사용할 수 있습니다. Python 스크립트
디렉터리가 `PATH`에 없다면 `python -m aipmt`도 정확히 같은
작업을 수행합니다. Python 3.10 이상이 필요합니다.

다른 패키지와 격리하여 설치하려면 다음을 실행합니다.

```bash
pipx install ai-powered-markdown-translator
```

### 프로젝트에 기여

개발에는 복제한 저장소가 계속 필요합니다. 테스트와 28개 번역,
모든 품질 도구가 이곳에 들어 있습니다.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`은 테스트된 환경을 정확히 반영하여 **모든 버전이 완전히 고정된 lock 파일**입니다.
`pyproject.toml`에 게시된 버전 범위는 의도적으로 더 넓게 설정되어
다른 패키지에 제약을 가하지 않습니다.

### 품질 도구(선택 사항이지만 권장)

프로젝트는 잘못된 서식, 취약점 또는 비밀 정보가 포함된 코드의 commit을 방지하기 위해 [`pre-commit`](https://pre-commit.com)을 사용합니다. 설치 방법은 다음과 같습니다.

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성 hook: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (복잡도), detect-secrets (API 키), mypy (점진적 타입 검사), Opengrep (SAST), pip-audit (의존성 CVE), unittest. 자세한 내용은 `CLAUDE.md`의 _Quality / pre-commit_ 섹션을 참조하세요.

## 구성

키는 우선순위가 높은 순서대로 **세 위치**에서 검색됩니다.
각 위치는 앞선 위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일시적 재정의 |
| 2   | 현재 디렉터리(또는 상위 디렉터리)의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | **한 번 설치하면 어디서나 적용**   |

`pip install` 이후 가장 간단한 방법은 세 번째입니다.

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

환경 변수가 절대 경로를 지정하면 이 파일은 `XDG_CONFIG_HOME`을 따르며
그렇지 않으면 명세에 따라 무시됩니다. Windows에서는 `%APPDATA%`을
따릅니다.

두 번째 방법은 저장소에 자체 키가 있을 때 유용합니다. 저장소 루트의 `.env`이
사용자 구성을 변경하지 않고 우선 적용됩니다. 환경에 이미 정의된
변수는 이 둘보다 우선합니다.

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

키를 찾지 못하면 명령은 호출 trace를 표시하지 않고
세 위치와 각각의 정확한 경로를 나열합니다.

`GEMINI_API_KEY`은 `GOOGLE_API_KEY`의 대안으로 허용됩니다(AI
Studio 규칙). 선택적 변수: `XAI_BASE_URL`(xAI endpoint, 기본값
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(Anthropic 호출당 초 단위 시간, 기본값
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX`(Grok CLI 섹션 참조), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT`(OpenCode 섹션 참조), `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT`(OpenRouter 섹션 참조).
`regen_translations.sh` 측 변수: `REGEN_PROVIDER`(기본값 `codex`, 구독 방식),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API`(과금되는 API를 사용하려면 반드시 재정의해야 함),
`REGEN_JOB_TIMEOUT`(job당 제한 시간, 기본값 600초, Codex에서는 1,800초).

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### ChatGPT 구독으로 번역(`--use_codex`)

이 provider는 API 키를 전혀 사용하지 않습니다. 공식 Codex CLI를 비대화형
모드로 구동하므로 번역 사용량은 이미 결제한 ChatGPT 구독(Plus, Pro,
Business 등)의 할당량에서 차감됩니다. 이는 OpenAI가 이 용도로 문서화한
유일한 방법입니다. `~/.codex/auth.json`의 token은 API Platform 호출을 인증하지
않으며, 이 스크립트는 해당 token을 읽지도 않습니다.

**필수 조건:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

바이너리는 `CODEX_BIN` 변수, `PATH`,
Python package `openai-codex-cli-bin` 순서로 검색됩니다. 마지막 항목은 의도적으로
`requirements.txt`에 포함되지 않습니다. 크기가 약 250MB라서 선택적 provider를 위해
모든 사용자에게 설치를 강제하게 되기 때문입니다.

**알아둘 사항:**

- **API 키는 사용되지 않습니다.** `OPENAI_API_KEY`과 `CODEX_API_KEY`은
  하위 프로세스 환경에서 제거되므로 `.env`에 키가 있어도 번역이
  사용량 기반 과금 방식으로 전환되지 않습니다.
- **segment 하나는 요금제의 5시간 창에서 ‘로컬 메시지’ 하나로 계산됩니다.**
  품질 모델(`gpt-5.6-sol`, Plus에서 5시간당 10~100개 메시지)보다
  `--eco`(모델 `gpt-5.6-luna`, Plus에서 5시간당 250~2,000개 메시지)을
  사용하세요.
- API 직접 호출보다 **느립니다**. README 전체 번역에 직접 호출은 몇 초가
  걸리는 반면 약 45초가 걸립니다.
- **CI에서는 거부됩니다**(`CI` 또는 `GITHUB_ACTIONS`가 정의된 경우).
  구독 인증은 개인 session 파일을 사용하며, 이를 공유 runner에 옮기면
  그 안에서 실행되는 모든 항목이 재사용할 수 있는 신원 정보를 두는 것과
  같습니다. 이 경로에서는 API 키를 사용하세요.
- 환경 변수: `CODEX_BIN`(바이너리의 명시적 경로) 및
  `CODEX_TIMEOUT`(segment당 초 단위 시간, 기본값 `600`).

### Grok 구독으로 번역(`--use_grok_cli`)

공식 **Grok Build** CLI를 사용한다는 점을 제외하면 `--use_codex`과 같은
원리입니다. 번역 사용량은 token 단위로 과금되는 대신 Grok 구독
(SuperGrok / X Premium+) 할당량에서 차감됩니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**격리 — 사용 전에 읽으세요.** 이 provider는 구조적으로 `--use_codex`보다
**취약하며**, 이는 의도된 선택입니다.

- Codex는 시스템이 강제하는 경계인 `--sandbox read-only`에서 실행됩니다.
- Grok sandbox는 최근의 많은 Linux 환경에서 **적용되지 않을 수 있습니다**.
  Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며,
  `/run/podman`이 `0700`에 있으면 컨테이너 runtime socket의
  deny-list가 실패합니다. 그런데 적용할 수 없는 **내장** 프로필은
  **아무 알림 없이 격리되지 않은 상태로** 시작됩니다.
- 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않으며,
  **조용히 fallback하지 않습니다**. 대신 경고를 표시합니다. 격리는 CLI의
  `--deny` 규칙(catch-all `*` 포함)에 의존합니다.
  이는 측정된 유일한 _fail-closed_ 계층으로, 알 수 없는 규칙이 있으면
  보호를 알리지 않고 제거하는 대신 시작을 거부합니다.
- OS sandbox를 **강제**하려면 `GROK_TRANSLATE_SANDBOX=read-only`을 사용하세요.
  시스템이 이를 지원하지 못하면 시작이 실패하며, 이것이 의도된
  동작입니다.

**할당량**: Grok pool은 **주 단위이며 Chat, Imagine, Voice와 공유**되고,
이를 확인하는 명령은 없습니다. 따라서 batch 처리는 아무 알림 없이
대화용 사용량을 소모할 수 있습니다. 이 때문에 동시 실행 수는 2로
제한되고 `regen_translations.sh`에 경고가 표시됩니다.

기타 변수: `GROK_BIN`(바이너리 경로), `GROK_TIMEOUT`(기본값 900초).

28개 번역을 다시 생성하려면 다음을 실행합니다.

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### OpenCode로 원하는 공급자를 통해 번역하기 (`--use_opencode`)

[OpenCode](https://opencode.ai)는 터미널에서 실행되는 **오픈 소스(MIT)** 코딩 에이전트입니다. 모델 공급자가 아니라 OpenCode 자체에 구성한 대상, 즉 API 키, 구독, 계정 없이 **무료 모델**을 제공하는 OpenCode Zen 게이트웨이 또는 **로컬** 모델로 연결하는 **라우터**입니다. 이 공급자는 비대화형 모드에서 `opencode run`을 실행하고 도구 없이 단 한 번의 왕복 호출로 제한합니다.

여기서는 이 가운데 **Zen 게이트웨이**와 로컬 **Ollama**라는 두 가지 경로를 종단 간 측정했습니다. OpenCode가 지원한다고 밝힌 다른 경로(GitHub Copilot, LM Studio, llama.cpp)도 이 공급자가 OpenCode와만 통신하므로 구조상 작동할 것으로 예상되지만, 실제 검증되지는 않았으며 이 README에는 검증한 내용만 기술합니다.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model`은 `provider/modèle` 형식으로 지정해야 하는 **필수 항목**입니다. OpenCode는 공급자가 아니므로 기본값을 대신 선택하지 않습니다. OpenCode 자체의 대체 동작은 대화 내용이 학습에 사용될 수 있는 무료 모델을 선택하는 것입니다.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**제한 — 스크립트가 호출할 때마다 수행하는 작업:**

- 사용자 구성보다 우선하는 인라인 구성(`OPENCODE_CONFIG_CONTENT`)이 **모든 도구를 거부하는**(`permission: { "*": "deny" }`) `aipmt` 에이전트를 정의합니다. 따라서 모델은 읽기, 쓰기, 명령 실행을 할 수 없으며, 측정 결과 이를 시도조차 하지 않았습니다. 세션 공유는 비활성화되고 `--pure`은 외부 플러그인을 제외하며, `--auto`은 절대 사용하지 않습니다.
- 호출은 `OPENCODE_DISABLE_PROJECT_CONFIG` 및 `OPENCODE_DISABLE_CLAUDE_CODE` 스위치를 적용한 **일회용 빈 디렉터리**에서 실행됩니다. 이 스위치가 없으면 OpenCode는 현재 디렉터리의 `AGENTS.md`과 사용자의 `~/.claude/CLAUDE.md`을 모든 프롬프트에 삽입합니다. 실제 측정에서는 `AGENTS.md`에 넣어 둔 “모든 답변을 BANANA로 끝내라”라는 지시가 번역에 적용되었습니다. 반면 `~/.config/opencode/AGENTS.md`의 전역 규칙은 계속 적용되며, OpenCode에서는 이를 제외할 수 없습니다.
- 출력 계약은 반환 코드 0, `error` 이벤트 없음, 도구 호출 없음, `stop` 상태로 완료된 마지막 단계, 비어 있지 않은 텍스트, 지정한 에이전트의 실제 로드를 모두 요구합니다. 알 수 없는 `--agent`이 있어도 OpenCode는 실패하지 않고 도구가 활성화된 코딩 에이전트로 **조용히 대체**합니다. 여기서는 `exit 0`도 아무것도 입증하지 못합니다.
- **aipmt 키는 하위 프로세스에 전달되지 않습니다**(Codex 및 Grok과 동일한 필터링). 유일하게 명시된 예외는 OpenCode 자체의 키(Zen, Go)인 `OPENCODE_API_KEY`입니다. 공급자는 aipmt의 `.env`이 아니라 OpenCode의 `opencode auth login`, `opencode.json`에서 구성합니다.

**알아둘 사항:**

- **Zen의 무료 모델은 “stealth” 모델 또는 기여자 제공 모델**로, 수시로 바뀌고 제한 사항이 문서화되어 있지 않으며 대화 내용이 학습에 사용될 수 있습니다. 공개 문서에는 적합하지만 비공개 콘텐츠에는 사용하지 않는 것이 좋습니다. 측정 결과 `opencode/mimo-v2.5-free`은 이 README를 한 번에 번역했지만, `opencode/big-pickle`은 더 느렸고 두 개의 동시 요청이 응답 없이 멈췄습니다.
- **로컬 모델은 최소 16 k의 컨텍스트를 제공해야 합니다.** 세그먼트가 최대 16,000자에 이르는 반면 Ollama는 기본값으로 4,096을 설정하는 경우가 많습니다. Ollama에서는 `PARAMETER num_ctx 32768`을 포함한 `Modelfile`을 만든 다음 `ollama create`을 사용합니다. 품질은 모델에 따라 달라집니다. 시험 파일에서 게이트웨이 모델은 모든 구조를 보존했지만, 7B 모델은 목록 순서를 뒤집고 코드 블록 닫기 구문을 손상했습니다.
- `--eco`은 아무 효과가 없습니다. 모델은 `--model`에서 정합니다. `--reasoning_effort`은 OpenCode의 `--variant`으로 그대로 전달되므로 모델이 이를 지원하는 경우에만 요청해야 합니다.
- 세션은 다른 모든 OpenCode 세션과 마찬가지로 OpenCode 데이터베이스(`~/.local/share/opencode/`)에 기록됩니다.
- 환경 변수: `OPENCODE_BIN`(바이너리의 명시적 경로이며, 없으면 `PATH` 후 `~/.opencode/bin/opencode` 사용) 및 `OPENCODE_TIMEOUT`(세그먼트당 제한 시간(초), 기본값 `600`). `OPENCODE_CONFIG`을 내보내더라도 `aipmt`이 이를 읽지는 않습니다. 값은 OpenCode에 그대로 전달되며 OpenCode가 이를 적용합니다.

**측정 예시: Ollama를 통한 로컬 모델**(RTX 3060 12 Go, RAM 62 Go, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

그런 다음 `~/.config/opencode/opencode.json`에서 공급자를 설정합니다.

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

`reasoningEffort: "none"`은 사소한 설정이 아닙니다. Ollama는 이러한 모델에서 추론을 기본적으로 활성화하며 Modelfile로는 이를 끌 수 없습니다. OpenCode를 통해 측정한 결과, “고양이가 매트 위에서 잔다”라는 문장은 이 옵션이 없을 때 추론에 919 tokens와 68초가 들었지만 옵션을 적용하면 9 tokens만 사용했습니다.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

589줄짜리 실제 블로그 글(링크 140개, 섹션 21개, `--news` 모드로 보호된 영어 인용문 3개)에 동일한 명령과 세 가지 모델을 사용한 결과입니다.

| 모델                                     | 소요 시간   | 구조                                                       | 차이점                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, 무료) | 4분 26초    | 원본과 동일                                                | 없음                                                                                      |
| `ollama/gemma4-12b-32k` (로컬)          | 10분 10초   | 링크, URL, 표, 태그, 굵은 글씨 및 인라인 코드가 동일       | 조작된 인용문 한 줄(🇺🇸 + 의역), 중복된 출처 표기                                         |
| `ollama/qwen3.5-9b-32k` (로컬)          | 8분 18초    | 링크, URL, 표 및 태그가 동일                               | 조작된 인용문 한 줄, 추가된 굵은 글씨와 인라인 코드 일부, 다시 처리된 세그먼트 하나       |

이 두 로컬 모델은 이후 **제외되었습니다**. 글 하나당 한 번의 자의적 변경만으로도 공개 번역용 모델로는 부적합하기 때문입니다. 다른 다섯 모델도 같은 이유 또는 시간 초과로 제외되었습니다(`gemma4:26b-a4b`, `qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). `gpt-oss:20b`만 유지되었지만, 이 모델조차 내용이 빽빽한 글에서는 일부 구절을 프랑스어로 남깁니다. 권장 모델 표를 참고하십시오.

로컬 번역 중 GPU 사용률은 98%, 전력은 170 W였으며 VRAM은 10 Go를 사용했습니다(모델과 32 k tokens 캐시가 모두 올라가 있었고 RAM으로 오프로드된 것은 없음). Ollama 서버는 RAM 7.5 Go를 사용했습니다. 90억~120억 개 매개변수 모델은 구조를 준수하지만 글마다 한 번씩 자의적으로 변경한 반면 게이트웨이 모델은 그런 변경을 전혀 하지 않았습니다. 게시 전 검토하거나 초안용으로만 사용하는 것이 좋습니다.

### OpenRouter를 통해 번역하기 (`--use_openrouter`)

OpenRouter는 타사가 호스팅하는 400개 이상의 모델 앞단에 위치한 **라우터**이며, 하나의 크레딧에서 사용량에 따라 요금이 청구됩니다. 단일 키로 다른 어느 공급자도 제공하지 않는 모델, 특히 중국의 오픈 모델에 접근할 수 있습니다.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

다음 두 가지 라우팅 특성이 구현 방식을 결정했으며, 둘 다 측정으로 확인할 수 있습니다.

- **동일한 모델이 서로 다른 한도를 가진 수십 개의 호스팅 업체에서 제공됩니다.** `z-ai/glm-5.3-flash`의 경우 23개 업체가 있으며, 그중 하나의 출력 한도는 2,048 tokens입니다. 아무런 대비가 없으면 23번 중 한 번꼴로 긴 번역이 라우팅에 따라 무작위로 잘리고 아무 신호도 표시되지 않았습니다. 사전 검사는 `/api/v1/models/{modèle}/endpoints`을 읽어 출력 한도가 8,000 tokens 미만이거나 상태가 저하된 업체를 제외한 뒤, 나머지를 `allow_fallbacks: false`으로 고정합니다. 이렇게 하지 않으면 라우터가 제외했던 업체로 다시 연결합니다.
- **추론에는 출력과 같은 요율로 요금이 부과됩니다.** `z-ai/glm-5.2`에 동일한 요청을 보내 “OK”라는 응답을 받았을 때 모델 기본 설정에서는 완료에 107 tokens가 들었지만, 추론을 끄면 2 tokens가 들었습니다. 따라서 이를 허용하는 모델에서는 추론이 기본적으로 비활성화됩니다. 추론을 강제하는 모델(`reasoning.mandatory`, 카탈로그의 431개 모델 중 288개)에는 기본 설정이 아니라 해당 모델이 허용한다고 명시한 **가장 낮은 추론 수준**을 적용합니다. `z-ai/glm-5.3-flash`의 기본값은 `max`이며, 번역이 끝나기 전에 출력 한도인 32,768 tokens를 모두 소진했습니다. 출력 한도를 늘려도 추론에 일정 비율을 할당하므로 결과는 달라지지 않았을 것입니다. `--reasoning_effort`은 계속 우선 적용되며, 추론을 강제하는 모델에 `none`을 지정하면 이를 우회하지 않고 오류로 알립니다.

사전 검사는 **문제가 있으면 중단**되며 선택한 대상을 표시합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

카탈로그에 없는 slug, 접근할 수 없는 카탈로그 또는 요구 출력 한도를 충족하는 호스팅 업체의 부재는 요금이 청구되기 전에 명령을 중단시킵니다.

기타 사항:

- 컨텍스트 창은 상수가 아니라 카탈로그에서 가져옵니다. 세그먼트 분할은 4,095 tokens 모델을 포함해 실제 한도에 맞게 조정됩니다.
- `--eco`은 아무 효과가 없습니다. 모델은 `--model`에서 정합니다.
- 출력이 비어 있는 `finish_reason=length`은 잘림이 아니라 추론에 예산을 모두 소진한 경우입니다. 두 상황에는 서로 반대되는 조치가 필요하므로 메시지에서 이를 명시합니다.
- 환경 변수: `OPENROUTER_API_KEY`(키, <https://openrouter.ai/keys>에서 발급), `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://` 필수), `OPENROUTER_TIMEOUT`(호출당 제한 시간(초), 기본값 `900`) 및 `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 `30`).

### 경제 모드

더 빠르고 저렴한 모델(gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite)을 사용합니다.

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션                     | 설명                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일                                                                                     |
| `--source_dir`           | Markdown 파일이 들어 있는 원본 디렉터리                                                                       |
| `--target_dir`           | 번역된 파일을 저장할 출력 디렉터리                                                                             |
| `--source_lang`          | 원본 언어(기본값: `fr`)                                                                             |
| `--target_lang`          | 대상 언어(기본값: `en`)                                                                             |
| `--model`                | 사용할 특정 모델                                                                                              |
| `--eco`                  | 경제적인 모델 사용                                                                                            |
| `--use_mistral`          | Mistral AI API 사용                                                                                           |
| `--use_claude`           | Claude API 사용                                                                                               |
| `--use_gemini`           | Gemini API 사용                                                                                               |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용                                                                         |
| `--use_grok`             | xAI API(Grok) 사용 — `XAI_API_KEY` 필요                                                                       |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                                   |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                                                                             |
| `--use_opencode`         | OpenCode에 구성된 공급자를 통해 OpenCode(오픈 소스) 사용 — `--model provider/modèle` 필수                               |
| `--force`                | 강제로 다시 번역                                                                                              |
| `--keep_filename`        | 원래 파일 이름 유지                                                                                           |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 국기를 처리                                                         |
| `--add_translation_note` | 번역 주석 추가                                                                                               |
| `--note_position`        | 주석 위치: `top`, `bottom`(기본값) 또는 `both`                                       |
| `--note_format`          | 주석 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`                                             |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                                                    |
| `--reasoning_effort`     | GPT-5.x 추론 수준: `none`/`low`/`medium`/`high`/`xhigh`             |

> **여덟 개의 공급자 플래그는 상호 배타적입니다.** 이전에는 두 개를 함께 지정해도 조용히 허용되었으며 먼저 검사한 항목으로 결정되었습니다. 따라서 구독 할당량(`--use_codex`, `--use_grok_cli`)으로 요청한 번역이 아무런 경고 없이 사용량 기반 과금으로 처리될 수 있었습니다. 이제 `argparse`은 이러한 조합을 거부합니다.

### 번역 주석: 위치 및 형식

`--add_translation_note`을 사용하면 번역기가 주석을 위쪽, 아래쪽 또는 양쪽 모두에 배치하고, 단순 텍스트 형식(이전 버전과 호환)이나 Markdown 플러그인이 처리할 수 있는 `marker` 형식으로 만들 수 있습니다.

**위치**(`--note_position`):

- `bottom`(기본값): 기존 방식대로 파일 끝에 주석을 배치합니다.
- `top`: **YAML frontmatter 뒤에** 주석을 삽입합니다(Astro Content Collections, gray-matter 등의 안전성 보장).
- `both`: 위쪽과 아래쪽 모두에 주석을 삽입합니다(LLM은 한 번만 호출하고 두 위치에 같은 콘텐츠를 재사용).

**형식**(`--note_format`):

- `legacy`(기본값): 굵은 문단 `**...**` 형식으로, v1.8과 byte-for-byte로 완전히 동일하게 작동합니다. Hugo, GitHub, GitLab 및 모든 Markdown renderer와 호환됩니다.
- `marker`: 보이지 않는 Markdown link reference definition(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 굵은 blockquote를 배치합니다. GitHub/GitLab에서 기본적으로 읽을 수 있으며, Astro의 remark 플러그인이 빌드 과정에서 이를 처리하여 스타일이 적용된 배너를 만들 수 있습니다(blog jls42.org 참고).

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

| 공급자     | 품질(기본값)                              | 경제형(`--eco`)    |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` 필수          | 동일 — `--eco`은 효과 없음 |
| OpenRouter | `--model fournisseur/modèle` 필수          | 동일 — `--eco`은 효과 없음 |
## 제대로 성능을 내는 모델

문단 하나를 잘 번역하는 모델이라도 문서 전체의 구조를 반드시 보존하는 것은 아닙니다. 이 측정값은 위에서 확인할 수 있는 명령으로 세 가지 문서 모음과 14개 대상 언어(en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi)에 대해 **실제로 실행한 번역**에서 얻었습니다.

두 열은 서로 다른 내용을 나타냅니다. **작성 완료**는 번역이 끝나 스크립트의 무응답 실패 방지 검사를 통과한 파일 수입니다. **차이 없음**은 원본과 구조가 동일한 번역 수입니다. 섹션, 링크, URL, 블록 및 인라인 코드, 표, 인용문, 플래그가 모두 같아야 합니다.

### 밀도 높은 블로그 글, `--news` 모드

589줄, 링크 140개, 섹션 21개, 보호된 영어 인용문 3개입니다. 세 문서 중 가장 까다롭습니다. `--news` 모드는 Markdown 구조에 더해 플래그와 인용문에 관한 제약을 추가합니다.

| 모델                              | 접근 방식          | 작성 완료 | 차이 없음 | 언어당 중앙값 |
| --------------------------------- | ------------------ | --------- | --------- | ------------- |
| `gemini-3.7-flash`                | Google API         | 14/14     | **14/14** | 1분 18초      |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT 구독       | 14/14     | **14/14** | 11분 28초     |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14     | **14/14** | 5분 37초      |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14     | 13/14     | 26분 23초     |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14     | 12/14     | 15분 49초     |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9       | 7/9       | 20분 33초     |
| `claude-sonnet-5`                 | Anthropic API      | 14/14     | 11/14     | 6분 31초      |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14     | 11/14     | 9분 27초      |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14     | 7/14      | 10분 09초     |
| `ollama/gpt-oss-20b-32k`          | 로컬               | 10/14     | 7/14      | 12분 39초     |
| `mistral-large-latest`            | Mistral API        | 11/14     | 5/14      | 5분 32초      |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14      | 3/14      | 37분 27초     |
| `grok-4.6` (`--use_grok_cli`)     | Grok 구독          | 1/14      | 1/14      | 23분 11초     |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4       | 1/4       | 23분 00초     |

두 작업 묶음은 **크레딧 부족으로 중단**되었으며, 분모에 그 사실이 반영되어 있습니다. `qwen3.5-27b`은 9개 언어에서 중단되었고, `kimi-k2.6`는 4개 언어에서 중단되었습니다. 후자는 40분의 시간 초과와 두 번의 거부가 발생했으며 언어당 비용은 약 0.33달러였습니다.

OpenRouter 항목의 측정 방법에는 한 가지 유의점이 있습니다. 해당 항목들은 `--use_openrouter`가 생기기 전에 **라우터의 기본 설정**으로 측정되었습니다. 이후 `z-ai/glm-5.2`는 제공된 프로바이더와 비활성화된 추론 설정으로 다시 측정했으며, 정확히 동일한 14/14를 기록했습니다. `z-ai/glm-5.3-flash`는 라우터의 기본 출력 예산을 모두 사용해 두 번 실패했습니다. 이제 프로바이더는 이 모델들이 허용하는 가장 낮은 추론 수준을 요청하며, 실패했던 언어를 대상으로 한 대조 시험도 통과합니다.

### 이 프로젝트의 README, 표준 Markdown

508줄, 인라인 코드 219개, 블록 닫기 구문 40개, 표 45줄입니다. 여기서는 `--news` 모드를 사용하지 않았으며, 코드 밀도가 난도를 높입니다.

| 모델                          | 작성 완료 | 차이 없음 | 언어당 중앙값 |
| ----------------------------- | --------- | --------- | ------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14     | 11/14     | 1분 22초      |
| `gemini-3.7-flash`            | 14/14     | 13/14     | 21초          |
| `gpt-5.6-sol` (`--use_codex`) | 14/14     | 12/14     | 2분 04초      |
| `opencode/mimo-v2.5-free`     | 9/14      | 7/14      | 3분 25초      |
| `ollama/gpt-oss-20b-32k`      | 9/14      | 1/14      | 3분 38초      |

### 잘 알려진 프로젝트의 README 네 개

GitHub에서 그대로 가져온 FastAPI, Ollama, tldr-pages, Vue.js 문서입니다. 이 문서들은 앞의 두 문서보다 **더 쉬우며**, 표에서도 이를 확인할 수 있습니다.

| 모델                      | 범위                       | 작성 완료 | 차이 없음 |
| ------------------------- | -------------------------- | --------- | --------- |
| `opencode/mimo-v2.5-free` | 프로젝트 4개 × 언어 14개   | 55/56     | 47/56     |
| `grok-4.6` (구독)         | 프로젝트 4개 × ar, hi, ja, zh | 16/16     | 14/16     |
| `ollama/gpt-oss-20b-32k`  | 프로젝트 4개 × ar, hi, ja, zh | 15/16     | 9/16      |

### 여기서 얻을 수 있는 결론

- **세 모델은 밀도 높은 두 문서에서 정보를 한 번도 누락하지 않았습니다.** `gemini-3.7-flash`, ChatGPT 구독을 통한 `gpt-5.6-sol`, OpenRouter를 통한 `z-ai/glm-5.2`입니다. 표준 모드에서 발생한 유일한 차이는 한두 언어에서 `**` 한 쌍이 반영되지 않은 것이며, URL이나 코드 블록, 인용문이 누락된 적은 없습니다.
- **판별 요인은 `--news` 모드가 아니라 문서의 밀도입니다.** 구독형 Grok은 블로그 글에서 14번 중 13번 실패하지만, 공개 README에서는 16개 중 14개를 성공합니다. 실패 원인은 긴 구간에서의 번역 이탈이며, 대조 시험으로 확인했습니다. 해당 구간만 분리하면 올바르게 번역됩니다.
- **예상과 달리 비라틴 문자 체계가 경계선은 아닙니다.** `gpt-oss`은 아랍어, 일본어, 폴란드어뿐 아니라 **루마니아어**에서도 일부 구간을 프랑스어로 남깁니다. Mistral과 MiMo는 비라틴 문자 체계에서만 인라인 코드를 누락합니다.
- **추론을 꺼도 품질 저하는 없습니다.** `z-ai/glm-5.2`는 라우터의 기본 추론 활성화 상태와 `--use_openrouter`로 추론을 끈 상태 모두에서 14개 언어를 차이 없이 처리하면서, 청구되는 출력 토큰은 18분의 1로 줄였습니다. 이 측정 결과를 근거로 프로바이더의 기본 설정이 정해졌습니다.
- **느린 모델이 안전한 모델인 것은 아닙니다.** `deepseek-v4-flash-0731`는 언어당 37분이 걸리면서 14개 번역 중 4개만 성공했고, `qwen3.8-flash`는 거의 완벽한 결과를 내는 데 26분이 걸렸으며, Gemini는 1분 18초 만에 완벽한 결과를 냈습니다.

### 이 표가 의미하지 않는 것

- **포괄적인 순위표가 아닙니다.** OpenRouter 하나만 해도 400개가 넘는 모델을 제공하며, 여기서는 약 15개만 측정했습니다. 어떤 모델이 없다는 사실은 그 품질을 의미하지 않으며, 단지 시험하지 않았다는 뜻입니다.
- **이 측정값에는 날짜가 있습니다.** 2026년 9월 4일과 5일입니다. 같은 이름의 모델도 바뀌고, 호스팅 업체는 양자화와 한도를 조정하며, 새로운 모델이 매주 출시됩니다.
- **소요 시간으로 순위를 정할 수 없습니다.** 캠페인에 따라 3개에서 6개의 번역을 동시에 실행했으며, 공급자의 처리량도 하루 중 시간대에 따라 달라집니다. 소요 시간은 대략적인 규모만 보여줄 뿐 비교 기준은 아닙니다.
- **결과는 모델만큼이나 문서에도 좌우됩니다.** 같은 모델이 한 글에서는 14개 언어를 성공하고 이 README에서는 9개만 성공합니다. 여러분의 파일은 저희 파일과 다릅니다.
- **가장 좋은 방법은 여전히 직접 측정하는 것입니다.** 문서 하나를 대상 언어로 번역한 다음 섹션, 링크, 고유 URL, 코드 블록, 인라인 코드, 표 행의 개수를 비교해 구조를 확인하세요. 바로 이것이 위 프로토콜이 수행하는 작업이며, `aipmt`를 사용하는 하나의 반복문으로 구현할 수 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

**gpt-5.6-sol을 사용하여 프랑스어에서 한국어로 번역된 기사.**
