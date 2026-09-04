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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복된 줄(%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 줄 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini**, **Grok (xAI)**을 사용하는 Markdown 파일 번역기입니다. API를 사용하거나, 사용량별 과금 없이 ChatGPT(Codex) 또는 Grok 구독 할당량을 사용하거나, 오픈 소스 에이전트인 **OpenCode**를 통해 로컬 모델(Ollama), 무료 서비스, 구독 서비스(GitHub Copilot 등), API 키 중 원하는 제공자를 이용할 수 있습니다.

이 Python 스크립트는 서식, 코드 블록, front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **다중 제공자**: 5개 API(OpenAI, Mistral, Claude, Gemini, Grok) + 사용량별 과금 없이 구독으로 이용하는 2개 CLI인 Codex(ChatGPT)와 Grok + 로컬 모델을 포함해 OpenCode에 구성된 모든 제공자를 이용할 수 있는 오픈 소스 MIT 라이선스의 OpenCode
- **2026년 모델**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하는 `--eco` 옵션
- **단일 파일**: 파일 하나만 번역하는 `--file` 옵션
- **지능형 분할**: 모델별 token 제한에 맞춰 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드(`` `...` ``)를 모두 보존
- **파일 이름**: 원래 이름을 유지하는 `--keep_filename` 옵션
- **뉴스 모드**: 뉴스 기사에서 영어 인용문을 보호하고 국기 이모지를 처리하는 `--news` 옵션
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 주석**: 문서 끝에 선택적으로 주석 추가

## 설치

### 도구 사용

```bash
pip install ai-powered-markdown-translator
```

이제 `aipmt` 명령을 어디서든 사용할 수 있습니다. Python 스크립트
디렉터리가 `PATH`에 없다면 `python -m aipmt`도 정확히 같은
작업을 수행합니다. Python 3.10 이상이 필요합니다.

다른 패키지와 분리하여 설치하려면 다음을 실행합니다.

```bash
pipx install ai-powered-markdown-translator
```

### 프로젝트에 기여

개발하려면 복제한 저장소가 계속 필요합니다. 테스트, 28개 번역 및 모든
품질 도구가 이곳에 들어 있습니다.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`은 테스트된 환경을 정확히 반영하는 **모든 버전이 고정된 lock 파일**입니다.
`pyproject.toml`에 공개된 버전 범위는 의도적으로 더 넓으며,
다른 패키지에 제약을 가하지 않습니다.

### 품질 도구(선택 사항이지만 권장)

이 프로젝트는 잘못된 형식이나 취약점 또는 비밀 정보가 포함된 코드의 commit을 방지하기 위해 [`pre-commit`](https://pre-commit.com)을 사용합니다. 설치 방법은 다음과 같습니다.

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성화되는 hook: ruff(lint+format), shellcheck(bash), prettier(markdown/yaml/json), Lizard(복잡도), detect-secrets(API 키), mypy(점진적 타입 검사), Opengrep(SAST), pip-audit(종속성 CVE), unittest. 자세한 내용은 `CLAUDE.md`의 _품질 / pre-commit_ 섹션을 참조하세요.

## 구성

키는 우선순위가 높은 순서대로 **세 위치**에서 검색됩니다.
각 위치에서는 앞선 위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일회성 재정의 |
| 2   | 현재 디렉터리 또는 상위 디렉터리의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | **한 번 설치하면 어디서나 적용**   |

`pip install` 이후 가장 간단한 방법은 세 번째 방식입니다.

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
그렇지 않으면 명세에 따라 무시됩니다. Windows에서는 `%APPDATA%`을
따릅니다.

저장소에 자체 키가 있을 때는 두 번째 방식도 유용합니다. 저장소 루트의
`.env`이 사용자 구성을 수정하지 않고 우선 적용됩니다. 환경에
이미 정의된 변수는 두 구성보다 우선합니다.

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

키를 찾지 못하면 명령은 호출 추적을 표시하지 않고
세 위치와 각각의 정확한 경로를 나열합니다.

`GEMINI_API_KEY`은 AI Studio 관례인 `GOOGLE_API_KEY`의 대체 변수로 사용할 수
있습니다. 선택적 변수는 `XAI_BASE_URL`(xAI endpoint, 기본값
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(Anthropic 호출당 시간, 기본값
900초), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX`(Grok CLI 섹션 참조), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT`(OpenCode 섹션 참조)입니다.
`regen_translations.sh` 관련 변수는 `REGEN_PROVIDER`(기본값 `codex`, 구독 사용),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API`(유료 API 사용 시 필수 재정의),
`REGEN_JOB_TIMEOUT`(작업당 제한 시간, 기본값 600초, Codex에서는 1,800초)입니다.

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

이 provider는 API 키를 전혀 사용하지 않습니다. 공식 Codex CLI를 비대화형
모드로 제어하므로 번역 사용량은 이미 결제한 ChatGPT 구독(Plus, Pro,
Business 등)의 할당량에서 차감됩니다. OpenAI가 이 용도로 문서화한 유일한
방법입니다. `~/.codex/auth.json`의 token은 API Platform 호출을 인증하지 않으며,
이 스크립트에서는 아예 읽지 않습니다.

**필수 조건:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

바이너리는 `CODEX_BIN` 변수, `PATH`, Python 패키지
`openai-codex-cli-bin` 순으로 검색합니다. 마지막 패키지는 의도적으로
`requirements.txt`에 포함하지 않았습니다. 약 250MB에 달해 선택적 provider를
위해 모든 사용자가 설치해야 하기 때문입니다.

**알아둘 사항:**

- **API 키를 사용하지 않습니다.** 하위 프로세스 환경에서 `OPENAI_API_KEY`와
  `CODEX_API_KEY`를 제거하므로 `.env`에 키가 있더라도 번역이
  사용량별 과금으로 전환되지 않습니다.
- **segment 하나는 요금제의 5시간 창에서 «로컬 메시지» 하나에 해당합니다.**
  품질 모델(`gpt-5.6-sol`, Plus에서 5시간당 10~100개 메시지)보다
  `--eco` 모델(`gpt-5.6-luna`, Plus에서 5시간당 250~2,000개 메시지)을
  사용하세요.
- API 직접 호출보다 **느립니다**. README 전체에 약 45초가 걸리며,
  직접 호출은 몇 초면 됩니다.
- **CI에서는 거부됩니다**(`CI` 또는 `GITHUB_ACTIONS`이 정의된 경우).
  구독 인증은 공유 runner용이 아니며 OpenAI도 공개 저장소에서 이
  workflow를 권장하지 않습니다. 이 경로에서는 API 키를 사용하세요.
- 환경 변수: `CODEX_BIN`(명시적 바이너리 경로)와
  `CODEX_TIMEOUT`(segment당 시간, 기본값 `600`초).

### Grok 구독으로 번역(`--use_grok_cli`)

공식 **Grok Build** CLI를 사용한다는 점을 제외하면 `--use_codex`과
같은 원리입니다. 번역 사용량은 token 단위로 과금되지 않고 Grok 구독
(SuperGrok / X Premium+) 할당량에서 차감됩니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**격리 — 사용 전에 읽어야 합니다.** 이 provider는 구조적으로
`--use_codex`보다 **취약하며**, 이는 의도된 선택입니다.

- Codex는 시스템이 강제하는 경계인 `--sandbox read-only`에서 실행됩니다.
- Grok sandbox는 최근 Linux 컴퓨터 다수에서 **적용되지 않을 수 있습니다**.
  Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며,
  `/run/podman`가 `0700`에 있으면 컨테이너 runtime socket의
  deny-list가 실패합니다. 그런데 적용할 수 없는 **내장** profile은
  **아무 알림 없이 격리되지 않은 상태로** 시작됩니다.
- 따라서 스크립트는 기본적으로 어떤 profile도 요청하지 않으며,
  **절대로 조용히 fallback하지 않고** 경고를 표시합니다. 격리는 CLI의
  `--deny` 규칙(포괄 규칙인 `*` 포함)에 의존합니다.
  측정 결과 이것이 유일한 _fail-closed_ 계층으로, 알 수 없는 규칙이 있으면
  보호를 알리지 않고 제거하는 대신 시작을 거부합니다.
- 운영체제 sandbox를 **강제**하려면 `GROK_TRANSLATE_SANDBOX=read-only`을 사용하세요.
  컴퓨터에서 이를 지원하지 못하면 의도한 대로 시작이 실패합니다.

**할당량**: Grok pool은 **주 단위이며 Chat, Imagine, Voice와 공유**되고,
이를 확인하는 명령은 없습니다. 따라서 일괄 처리가 아무런 알림 없이
대화용 사용량을 잠식할 수 있습니다. 이런 이유로 동시 실행 수를 2개로
제한하고 `regen_translations.sh`에 경고를 표시합니다.

기타 변수: `GROK_BIN`(바이너리 경로), `GROK_TIMEOUT`(기본값 900초).

28개 번역을 다시 생성하려면 다음을 실행합니다.

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### OpenCode를 사용해 원하는 제공자로 번역(`--use_opencode`)

[OpenCode](https://opencode.ai)는 terminal에서 작동하는 **오픈 소스(MIT)** 코드
에이전트입니다. 모델 provider가 아니라 OpenCode 자체에 구성한
provider로 연결하는 **router**입니다. API 키, 구독(GitHub Copilot,
ChatGPT, SuperGrok), **계정 없이** 무료 모델을 제공하는 OpenCode Zen
gateway 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp)을 사용할 수
있습니다. 이 provider는 `opencode run`을 비대화형 모드로 제어하며,
도구 없이 단 한 번의 왕복 호출로 제한합니다.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model`은 `provider/modèle` 형식으로 **반드시 지정해야 합니다**.
OpenCode는 provider가 아니므로 기본값을 대신 선택하지 않습니다.
OpenCode 자체 fallback은 대화 내용이 학습에 사용될 수 있는 무료
모델이기 때문입니다.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**격리 — 스크립트가 매 호출마다 수행하는 작업:**

- 사용자 구성보다 우선하는 inline 구성(`OPENCODE_CONFIG_CONTENT`)에서
  **모든 도구가 거부된**(`permission: { "*": "deny" }`) `aipmt` 에이전트를
  정의합니다. 모델은 읽기, 쓰기, 명령 실행을 할 수 없으며, 측정 결과
  그러한 작업을 시도조차 하지 않습니다. 세션 공유는 비활성화되고
  `--pure`가 외부 plugin을 제외하며, `--auto`는 절대 사용하지
  않습니다.
- 호출은 **비어 있는 일회용 디렉터리**에서 `OPENCODE_DISABLE_PROJECT_CONFIG` 및
  `OPENCODE_DISABLE_CLAUDE_CODE` 스위치와 함께 실행됩니다. 이 스위치가 없으면 OpenCode는
  현재 디렉터리의 `AGENTS.md`과 사용자의 `~/.claude/CLAUDE.md`을 모든 prompt에
  삽입합니다. 측정 결과 `AGENTS.md`에 넣은 «모든 응답을 BANANA로
  끝내라»라는 지시가 번역에 적용되었습니다. 반면 `~/.config/opencode/AGENTS.md`의 전역
  규칙은 계속 적용됩니다. OpenCode에서는 이를 제외할 수 없습니다.
- 출력 계약은 반환 코드 0, `error` event 없음, 도구 호출 없음,
  마지막 단계가 `stop`으로 완료됨, 비어 있지 않은 텍스트,
  에이전트가 실제로 로드됨을 모두 요구합니다. 알 수 없는 `--agent`은
  OpenCode를 실패시키지 않고 도구가 활성화된 코딩 에이전트로 **조용히
  fallback합니다**. 여기서는 `exit 0`도 아무것도 입증하지 못합니다.
- 명시적으로 예외 처리된 `OPENCODE_API_KEY`을 제외하면 **aipmt 키는 하위
  프로세스로 전달되지 않습니다**(Codex 및 Grok과 동일한 필터링).
  `OPENCODE_API_KEY`은 OpenCode 자체의 키(Zen, Go)입니다. provider는 aipmt의
  `.env`이 아니라 OpenCode에서 구성합니다(`opencode auth login`,
  `opencode.json`).

**알아둘 사항:**

- **Zen의 무료 모델은 «stealth» 또는 contributor 모델**이며 자주 바뀌고
  제한이 문서화되어 있지 않으며, 대화 내용이 학습에 사용될 수 있습니다.
  공개 문서에는 적합하지만 비공개 콘텐츠에는 피해야 합니다. 측정 결과
  `opencode/mimo-v2.5-free`은 이 README를 한 번에 번역했으며, `opencode/big-pickle`은 더
  느렸고 두 개의 동시 요청이 응답 없이 멈췄습니다.
- **로컬 모델은 최소 16k context를 제공해야 합니다.** segment 길이가 최대
  16,000자이기 때문입니다. 반면 Ollama는 기본적으로 4,096으로 구성되는
  경우가 많습니다. Ollama에서는 `PARAMETER num_ctx 32768`을 포함한 `Modelfile`을
  만든 다음 `ollama create`을 실행하세요. 품질은 모델에 따라 달라집니다.
  시험 파일에서 7B 모델은 목록 순서를 뒤집고 코드 블록의 닫는 fence를
  손상시켰지만 gateway 모델은 모든 구조를 보존했습니다.
- `--eco`은 아무 효과가 없습니다. 모델은 `--model`에서
  지정합니다. `--reasoning_effort`은 OpenCode의 `--variant`로 그대로
  전달되므로 모델이 이를 지원할 때만 요청하세요.
- 세션은 다른 OpenCode 세션과 마찬가지로 OpenCode 데이터베이스
  (`~/.local/share/opencode/`)에 기록됩니다.
- 환경 변수: `OPENCODE_BIN`(명시적 바이너리 경로, 지정하지 않으면
  `PATH`, 그다음 `~/.opencode/bin/opencode`)과 `OPENCODE_TIMEOUT`
  (segment당 시간, 기본값 `600`초). `OPENCODE_CONFIG`을 export하면
  해당 값이 적용됩니다.

**측정 예시: Ollama를 통한 로컬 모델**(RTX 3060 12GB, RAM 62GB, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

그런 다음 `~/.config/opencode/opencode.json`에서 provider를 구성합니다.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"`은 사소한 설정이 아닙니다. Ollama는 Gemma 4와 Qwen 3.5에서
추론을 기본적으로 활성화하며 Modelfile로 이를 끌 수 없습니다. OpenCode를
통한 측정 결과 이 옵션이 없으면 «고양이가 매트 위에서 잔다»를 처리하는 데
추론 token 919개와 68초가 걸렸지만, 옵션을 사용하면 9 token만 걸렸습니다.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

589줄, 링크 140개, 섹션 21개, `--news` 모드로 보호한 영어 인용문
3개가 포함된 실제 블로그 글에 같은 명령을 세 모델로 실행한 결과입니다.

| 모델                                   | 소요 시간       | 구조                                                  | 차이                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, 무료) | 4분 26초  | 원본과 동일                                      | 없음                                                                                     |
| `ollama/gemma4-12b-32k` (로컬)          | 10분 10초 | 링크, URL, 표, tag, 굵은 글씨, 인라인 코드가 동일 | 만들어 낸 인용문 한 줄(🇺🇸 + 바꿔 쓴 문장), 중복된 출처 표시               |
| `ollama/qwen3.5-9b-32k` (로컬)          | 8분 18초  | 링크, URL, 표, tag가 동일                    | 만들어 낸 인용문 한 줄, 추가된 굵은 글씨와 인라인 코드 일부, 다시 처리된 segment 하나 |

로컬 번역 중 GPU 사용률은 98%, 전력은 170W였고, VRAM은 10GB를
사용했습니다. 모델과 32k token cache가 모두 VRAM에 있었고 RAM으로
offload된 것은 없었으며, Ollama server는 RAM 7.5GB를 사용했습니다.
90억~120억 parameter 규모의 모델은 구조를 준수하지만 기사마다 한 번씩
자의적으로 변경하는 반면, gateway 모델은 그런 변경을 전혀 하지
않았습니다. 게시 전 검토하거나 초안 용도로만 사용하는 것이 좋습니다.

### 경제 모드

더 빠르고 저렴한 모델(gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite)을 사용합니다.

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### 옵션

| 옵션                   | 설명                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일                                                                            |
| `--source_dir`           | Markdown 파일이 포함된 소스 디렉터리                                                             |
| `--target_dir`           | 번역된 파일의 출력 디렉터리                                                               |
| `--source_lang`          | 소스 언어(기본값: `fr`)                                                                                  |
| `--target_lang`          | 대상 언어(기본값: `en`)                                                                                   |
| `--model`                | 사용할 특정 모델                                                                                  |
| `--eco`                  | 경제형 모델 사용                                                                              |
| `--use_mistral`          | Mistral AI API 사용                                                                                     |
| `--use_claude`           | Claude API 사용                                                                                         |
| `--use_gemini`           | Gemini API 사용                                                                                         |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용                                                    |
| `--use_grok`             | xAI API(Grok) 사용 — `XAI_API_KEY` 필요                                                           |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                                                        |
| `--use_opencode`         | OpenCode에 구성된 공급자와 함께 OpenCode(오픈 소스) 사용; `--model provider/modèle` 필요 |
| `--force`                | 강제로 다시 번역                                                                                       |
| `--keep_filename`        | 원본 파일명 유지                                                                          |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 플래그 처리                                      |
| `--add_translation_note` | 번역 주석 추가                                                                                |
| `--note_position`        | 주석 위치: `top`, `bottom`(기본값) 또는 `both`                                                     |
| `--note_format`          | 주석 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델명 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 노력 수준: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **7개의 공급자 플래그는 상호 배타적입니다.** 이전에는 두 개를 함께 사용해도
> 아무 경고 없이 허용되었으며, 먼저 검사된 항목으로 결정되었습니다. 따라서
> 구독 할당량을 사용하도록 요청된 번역(`--use_codex`, `--use_grok_cli`)이
> 아무런 경고 없이 사용량 기반 요금으로 청구될 수 있었습니다.
> 이제 `argparse`은 이러한 조합을 거부합니다.

### 번역 주석: 위치 및 형식

`--add_translation_note`을 사용하면 번역기가 주석을 위쪽, 아래쪽 또는 양쪽 모두에 배치할 수 있으며, 단순 텍스트 형식(이전 버전과 호환)이나 Markdown 플러그인에서 처리할 수 있는 `marker` 형식으로 렌더링할 수 있습니다.

**위치**(`--note_position`):

- `bottom`(기본값): 기존과 마찬가지로 파일 끝에 주석을 배치합니다.
- `top`: 주석을 **YAML 프런트매터 뒤에** 삽입합니다(Astro Content Collections, gray-matter 등의 안전성 보장).
- `both`: 주석을 위쪽과 아래쪽 모두에 삽입합니다(LLM 호출은 한 번만 수행하며 두 위치에 같은 콘텐츠를 재사용).

**형식**(`--note_format`):

- `legacy`(기본값): 굵은 문단 `**...**` — v1.8과 바이트 단위로 완전히 동일한 동작입니다. Hugo, GitHub, GitLab 및 모든 Markdown 렌더러와 호환됩니다.
- `marker`: 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 굵은 인용문을 배치합니다. GitHub/GitLab에서 기본적으로 읽을 수 있으며, Astro 측의 remark 플러그인이 빌드 과정에서 이를 활용해 스타일이 적용된 배너를 생성할 수 있습니다(jls42.org 블로그 참조).

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

| 공급자 | 품질(기본값)                      | 경제형(`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` 필수 | 동일 — `--eco`은 효과 없음 |

> **장문 번역 권장 사항**: `--use_gemini`(기본값 = `gemini-3.7-flash`)은 라틴 문자가 아닌 문자 체계(PL, JA, ZH, AR, HI)에서 Markdown 구조를 충실하게 보존하며, 플레이스홀더의 정확성이 중요한 `--news` 모드에서도 마찬가지입니다. 이 README의 일본어 번역에서 측정한 결과, `gemini-3.1-pro-preview`과 구조가 동일하면서(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존) 지연 시간은 약 6배 짧았습니다. 이전 버전과의 호환성을 위해 OpenAI가 기본값으로 유지됩니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

**gpt-5.6-sol로 프랑스어에서 한국어로 번역된 글.**
