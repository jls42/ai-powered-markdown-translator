# AI 기반 Markdown 번역기

🌍 [프랑스어](README.md) | [영어](README-en.md) | [스페인어](README-es.md) | [중국어](README-zh.md) | [독일어](README-de.md) | [일본어](README-ja.md) | [한국어](README-ko.md) | [아랍어](README-ar.md) | [힌디어](README-hi.md) | [이탈리아어](README-it.md) | [네덜란드어](README-nl.md) | [폴란드어](README-pl.md) | [포르투갈어](README-pt.md) | [루마니아어](README-ro.md) | [스웨덴어](README-sv.md)

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

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기입니다.

이 Python 스크립트는 서식, 코드 블록 및 front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **다중 Provider**: 4개 API(OpenAI, Mistral, Claude, Gemini) 및 ChatGPT 구독 기반 Codex CLI 지원
- **2026년 모델**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하는 `--eco` 옵션
- **단일 파일**: 파일 하나만 번역하는 `--file` 옵션
- **지능형 분할**: 모델별 token 한도를 적용하여 긴 텍스트 처리
- **코드 보존**: 코드 블록과 inline 코드(`` `...` ``)를 모두 보존
- **파일 이름**: 원래 이름을 유지하는 `--keep_filename` 옵션
- **뉴스 모드**: 뉴스 기사에서 영어 인용문을 보호하고 국기를 처리하는 `--news` 옵션
- **.env 설정**: API 키를 위한 `.env` 파일 지원
- **번역 주석**: 문서 끝에 선택적으로 주석 추가

## 설치

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 품질 도구(선택 사항이지만 권장)

프로젝트는 서식이 잘못되었거나 취약하거나 비밀 정보가 포함된 코드의 commit을 방지하기 위해 [`pre-commit`](https://pre-commit.com)을 사용합니다. 설치 방법:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성 hook: ruff(lint+format), shellcheck(bash), prettier(markdown/yaml/json), Lizard(복잡도), detect-secrets(API 키), mypy(점진적 타입 검사), Opengrep(SAST), pip-audit(CVE 종속성), unittest. 자세한 내용은 `CLAUDE.md`의 _Quality / pre-commit_ 섹션을 참조하세요.

## 설정

프로젝트 루트에 `.env` 파일을 만들거나 환경 변수를 설정하세요.

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

`GEMINI_API_KEY`은 `GOOGLE_API_KEY`의 대안으로 사용할 수 있습니다(AI
Studio 규칙). 선택적 변수: `XAI_BASE_URL`(xAI endpoint, 기본값
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(Anthropic 호출당 초, 기본값
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
그리고 `GROK_TRANSLATE_SANDBOX`(Grok CLI 섹션 참조).

## 사용법

### 단일 파일 번역

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 디렉터리 번역

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### ChatGPT 구독으로 번역(`--use_codex`)

이 provider는 API 키를 전혀 사용하지 않습니다. 공식 Codex CLI를
비대화형 모드로 제어하므로 번역 사용량은 이미 결제한
ChatGPT 구독(Plus, Pro, Business 등)의 quota에서 차감됩니다. 이는 이 용도로
OpenAI가 문서화한 유일한 방법입니다. `~/.codex/auth.json` token은
Platform API 호출을 인증하지 않으며, 이 스크립트에서는 아예 읽지도 않습니다.

**필수 조건:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

바이너리는 `CODEX_BIN` 변수, `PATH`,
Python package `openai-codex-cli-bin` 순서로 검색됩니다. 마지막 항목은 의도적으로
`requirements.txt`에 포함하지 않았습니다. 용량이 약 250MB이므로 선택적
provider를 위해 모든 사용자에게 설치하도록 강제하게 되기 때문입니다.

**알아둘 사항:**

- **API 키를 전혀 사용하지 않습니다.** `OPENAI_API_KEY`와 `CODEX_API_KEY`은
  하위 프로세스의 환경에서 제거되므로 `.env`에 키가
  있어도 번역이 종량제 결제로 전환되지 않습니다.
- **segment 하나 = 5시간 plan 창의 «로컬 메시지» 하나**입니다.
  품질 모델(`gpt-5.6-sol`, 5시간당 메시지 10~100개)보다
  `--eco`(모델 `gpt-5.6-luna`, Plus에서 5시간당 메시지 250~2,000개)를 사용하세요.
- API 직접 호출보다 **느립니다**. README 전체 하나에 약 45초가 걸리며,
  직접 호출하면 몇 초 정도입니다.
- CI에서는 **거부됩니다**(`CI` 또는 `GITHUB_ACTIONS`이 정의된 경우). 구독 기반
  인증은 공유 runner용이 아니며, OpenAI는 공개 repository에서 이
  workflow를 권장하지 않습니다. 이 경로에서는 API 키를 사용하세요.
- 환경 변수: `CODEX_BIN`(명시적 바이너리 경로) 및
  `CODEX_TIMEOUT`(segment당 초, 기본값 `600`).

### Grok 구독으로 번역(`--use_grok_cli`)

공식 **Grok Build** CLI를 사용하는 `--use_codex`과 동일한 원리입니다.
번역 사용량은 token 단위로 청구되는 대신 Grok 구독(SuperGrok / X Premium+)에서
차감됩니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**격리 — 사용 전에 읽으세요.** 이 provider는 구조적으로 `--use_codex`보다
**취약**하며, 이는 의도된 사항입니다.

- Codex는 시스템이 강제하는 경계인 `--sandbox read-only`에서 실행됩니다.
- 최근의 많은 Linux 환경에서는 Grok sandbox를 **적용할 수 없습니다**.
  Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며,
  `/run/podman`이 `0700`에 있으면 container runtime socket의 deny-list가
  작동하지 않습니다. 그런데 적용할 수 없는 **내장** profile은
  **격리되지 않은 상태로 조용히** 시작됩니다.
- 따라서 스크립트는 기본적으로 어떠한 profile도 요청하지 않으며, **절대 조용히
  fallback하지 않습니다**. 대신 경고를 표시합니다. 격리는 CLI의
  `--deny` 규칙(catch-all `*` 포함)에 의존합니다. 이는 측정된 유일한
  _fail-closed_ 계층으로, 알 수 없는 규칙이 있으면 보호를 알리지 않고
  제거하는 대신 시작을 거부합니다.
- OS sandbox를 **강제하려면** `GROK_TRANSLATE_SANDBOX=read-only`을 사용하세요.
  시스템이 이를 지원하지 못하면 시작이 실패하며, 이것이 의도된
  동작입니다.

**Quota**: Grok pool은 **주 단위이며 Chat, Imagine 및
Voice와 공유**되고, 이를 확인할 수 있는 명령은 없습니다. 따라서 batch 처리는
아무런 알림 없이 대화 용도의 사용량을 잠식할 수 있습니다. 이 때문에
동시 실행 수를 2로 제한하고 `regen_translations.sh`에 경고를 표시합니다.

기타 변수: `GROK_BIN`(바이너리 경로), `GROK_TIMEOUT`(기본값 900초).

28개 번역을 다시 생성하려면:

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
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션                   | 설명                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 번역할 단일 Markdown 파일                                       |
| `--source_dir`           | Markdown 파일이 포함된 원본 디렉터리                        |
| `--target_dir`           | 번역된 파일의 출력 디렉터리                          |
| `--source_lang`          | 원본 언어(기본값: `fr`)                                             |
| `--target_lang`          | 대상 언어(기본값: `en`)                                              |
| `--model`                | 사용할 특정 모델                                             |
| `--eco`                  | 경제형 모델 사용                                         |
| `--use_mistral`          | Mistral AI API 사용                                                |
| `--use_claude`           | Claude API 사용                                                    |
| `--use_gemini`           | Gemini API 사용                                                    |
| `--use_codex`            | ChatGPT 구독 quota로 Codex CLI 사용               |
| `--use_grok`             | xAI API(Grok) 사용 — `XAI_API_KEY` 필요                      |
| `--use_grok_cli`         | Grok 구독 quota로 Grok CLI 사용                   |
| `--force`                | 재번역 강제                                                  |
| `--keep_filename`        | 원래 파일 이름 유지                                     |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 국기를 처리 |
| `--add_translation_note` | 번역 주석 추가                                           |
| `--note_position`        | 주석 위치: `top`, `bottom`(기본값) 또는 `both`                |
| `--note_format`          | 주석 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`       |
| `--include_model`        | 출력 파일에 모델 이름 포함                       |
| `--reasoning_effort`     | GPT-5.x 추론 노력 수준: `none`/`low`/`medium`/`high`/`xhigh`     |

### 번역 주석: 위치와 형식

`--add_translation_note`을 사용하면 translator가 주석을 위쪽, 아래쪽 또는 양쪽에 배치할 수 있으며, 이전 버전과 호환되는 일반 텍스트 형식이나 Markdown plugin에서 사용할 수 있는 `marker` 형식으로 만들 수 있습니다.

**위치**(`--note_position`):

- `bottom`(기본값): 기존과 같이 파일 끝에 주석을 배치합니다.
- `top`: 주석을 **YAML frontmatter 뒤에** 삽입합니다(Astro Content Collections, gray-matter 등의 안전성 보장).
- `both`: 위와 아래 양쪽에 주석을 삽입합니다(LLM 호출은 한 번만 수행하고 두 위치에서 콘텐츠를 재사용).

**형식**(`--note_format`):

- `legacy`(기본값): 굵은 문단 `**...**` — v1.8과 byte-for-byte로 완전히 동일하게 동작합니다. Hugo, GitHub, GitLab 및 모든 Markdown renderer와 호환됩니다.
- `marker`: 보이지 않는 Markdown link reference definition(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 굵은 blockquote를 배치합니다. GitHub/GitLab에서 기본적으로 읽을 수 있으며, Astro 측의 remark plugin이 build 시 이를 활용하여 스타일이 적용된 banner를 생성할 수 있습니다(jls42.org blog 참조).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### 기본 모델(2026년)

| Provider | 품질(기본값)       | 경제형(`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **장문 번역 권장 사항**: `--use_gemini`(기본값 = `gemini-3.7-flash`)은 라틴 문자가 아닌 문자 체계(PL, JA, ZH, AR, HI)에서도 Markdown 구조를 충실하게 보존하며, placeholder 충실도가 중요한 `--news` 모드에서도 마찬가지입니다. 이 README의 일본어 번역에서 측정한 결과, `gemini-3.1-pro-preview`과 동일한 구조(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존)를 약 6배 낮은 latency로 제공했습니다. 이전 버전과의 호환성을 위해 OpenAI가 기본값으로 유지됩니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 blog(15개 언어)

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE)를 참조하세요.

**gpt-5.6-sol로 프랑스어에서 한국어로 번역된 기사.**
