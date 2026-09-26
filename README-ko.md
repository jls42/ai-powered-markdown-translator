# AI 기반 Markdown 번역기

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 코드 품질</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

코드 블록, 인라인 코드, URL, 앵커, 표 및 front matter와 같은 구조를 보존하면서 Markdown 파일을 한 언어에서 다른 언어로 번역합니다. 5개의 API, 종량제 과금이 없는 3개의 구독 서비스, 2개의 라우터 등 모델을 호출하는 10가지 방법과 각 모델이 실제로 무엇을 보존하는지에 대한 공개된 측정값을 제공합니다.

## 요약

- **10가지 공급자 경로**: OpenAI, Mistral, Claude, Gemini 및 Grok API; 종량제 과금이 없는 ChatGPT(Codex), Grok 및 Google(Antigravity) 구독; OpenCode(오픈 소스, 무료 또는 로컬) 및 OpenRouter(400개 이상의 모델) 라우터.
- **토큰 유실로 인한 오류 방지**: 호출 전 코드 블록, 인라인 코드, URL, 앵커 및 인용문이 토큰으로 대체되며 반환 시 검증됩니다. 하나라도 누락되면 파일이 저장되지 않습니다.
- **긴 문서 지원**: 모델의 컨텍스트 창 크기에 맞춘 문서 분할.
- **`--news` 모드**: 모니터링/뉴스 기사를 위해 영어 인용문을 보호하고 언어별 국기 플래그를 처리합니다.
- **`--eco` 모드**: 더 빠르고 저렴한 모델을 사용합니다.
- **번역 노트**: 선택 사항으로 상단, 하단 또는 양쪽 모두에 추가 가능.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 이상. 저장소에서 직접 설치하는 방법은 [기여하기](#기여하기)를 참조하세요.

## 설정

키는 우선순위가 높은 곳부터 낮은 순으로 세 곳에서 읽어오며, 각각은 이전 위치에서 비어 있는 항목만 채웁니다.

|     | 위치                                          | 용도                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                                     | CI, 컨테이너, 일회성 재정의           |
| 2   | 현재 디렉터리(또는 상위 디렉터리)의 `.env` | 프로젝트 전용 키                      |
| 3   | `~/.config/aipmt/.env`                                 | 한 번 설치하면 어디서나 유효함        |

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

`GOOGLE_API_KEY` 대신 `GEMINI_API_KEY`도 지원됩니다. 사용자 파일은 `XDG_CONFIG_HOME`(절대 경로만 해당) 및 Windows의 경우 `%APPDATA%`을 따릅니다. 키가 없으면 명령어가 세 위치를 모두 나열합니다.

**프로젝트의 `.env` 파일은 호출을 리디렉션하거나 실행할 프로그램을 선택할 수 없습니다.** 이 파일은 키만 제공할 뿐 대상이나 바이너리는 제공하지 않습니다. `_BASE_URL`, `_API_BASE`, `_ENDPOINT` 또는 `_BIN`(`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, 프록시(`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), 인증서 저장소(`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) 및 `XDG_CONFIG_HOME` / `APPDATA` 관련 변수는 경고와 함께 무시됩니다. 복제된 저장소가 첫 번역 실행 시 사용자의 키를 탈취하거나 자체 프로그램을 실행하도록 유도해서는 안 되기 때문입니다. 또한 이 파일은 보간 없이 읽히므로, `NOM=${OPENAI_API_KEY}`가 키를 복사하지 않습니다. 이러한 변수는 환경 변수나 `~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(호출당 초, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`(기본값 600), `GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`), `GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT`(기본값 900), `OPENCODE_BIN`, `OPENCODE_TIMEOUT`(기본값 600), `OPENROUTER_BASE_URL`(`https://` 필요), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각각에 대한 자세한 내용은 해당 공급자 섹션에 설명되어 있습니다.

## 시작하기

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

스페인어로 번역된 `document.md`는 `--target_dir` 디렉터리에 `document-es.md`를 생성합니다. `--include_model`를 사용하면 `document-es-gpt-5.6-terra.md`가 됩니다. 원본 파일명을 유지하는 `--keep_filename`를 사용하지 않는 한, 확장자는 항상 `.md`로 변경됩니다(`article.mdx`는 `article-en.md`가 됨). 이미 존재하는 번역본은 `--force` 옵션이 없으면 건너뜁니다.

종료 코드: 모두 성공했거나 건너뛴 경우 `0`, 실패한 파일이 남아 있는 경우 `1`(표준 에러 출력에 목록 표시), 설정 문제인 경우 `2`. 실패한 파일은 저장되지 않으며, 파일 쓰기 자체가 실패하더라도 임시 파일로 작성된 후 이름이 변경되므로 파일이 손상되지 않습니다. 다시 실행하기만 하면 됩니다.

## 어떤 모델을 선택해야 할까

두 개의 실제 문서를 각 모델을 통해 동일한 14개 언어로 번역하여 측정한 결과입니다. **숫자는 14개 언어 중 번역이 정상적으로 작성되고 원본과 비교해 누락이나 변경이 전혀 없는 언어의 수입니다.**

| 모델                 | 접근 방법                         | 정보 밀도가 높은 모니터링 기사 | 본 README    | 차이점 및 발생 언어 수                                                                                                                |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API 키                    | ✅ 14/14                | ⚠️ 13/14     | 14개 중 1개 언어: 굵은 글씨 단어 1개 추가 (ja)                                                                                         |
| **Gemini 3.7 Flash** | Google 구독 (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 14개 중 1개 언어: 굵은 글씨 단어 1개 누락 (ko)                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT 구독 또는 OpenAI 키 | ✅ 14/14                | ⚠️ 12/14     | 14개 중 2개 언어: 굵은 글씨 단어 1개 누락 (ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter 키                    | ✅ 14/14                | ⚠️ 11/14     | 14개 중 3개 언어: 굵은 글씨 단어 1개 누락 (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic API 키                 | ⚠️ 11/14                | ⚠️ 12/14     | 기사에서 3개 언어: 코드 블록 추가 발생 (es, de, hi); 본 README에서 2개: 링크 마크업 유실 (sv), 굵은 글씨 단어 1개 (zh) |
| Qwen 3.7 Flash       | OpenRouter 키                    | ❌ 8/14                 | ⚠️ 10/14     | 기사에서 1개 언어 거부됨, 5개 언어 변형 발생; 본 README에서 약 40개 단어가 `code`로 처리됨 (ar)                       |
| Grok 4.6             | Grok 구독                   | ❌ 8/14                 | 평가 불가     | 14개 중 5개 언어 거부됨(인라인 코드 및 URL 렌더링 실패); 네덜란드어는 전반적으로 변형됨                                  |
| GPT-OSS 20B          | 로컬 모델 (Ollama)             | ❌ 7/14                 | 재측정 안 됨 | 14개 중 4개 언어 거부됨: 모델이 프랑스어 구문을 그대로 남겨 가드에 의해 차단됨                                     |
| MiMo v2.5 (무료)  | OpenCode Zen, 계정 불필요         | ❌ 11/14                | 재측정 안 됨 | 1개 언어 거부됨; 폴란드어에서 섹션 1개 유실                                                                                     |
| Mistral Large        | Mistral API 키                   | ❌ 5/14                 | ❌ 1/14      | **전체 섹션 누락 발생**: 기사에서 1개 언어 (hi), 본 README에서 3개 언어 (ar, hi, ko) — 그리고 기사에서 3개 언어 거부됨   |
| DeepSeek V4 Flash    | OpenRouter 키                    | ❌ 3/14                 | 재측정 안 됨 | 14개 중 10개 언어 거부됨; 언어당 37분 소요                                                                                    |

|     | 기호 설명                                                                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14개 언어가 모두 번역되었으며, 원본과 달라진 부분이 전혀 없음                                                                                                         |
| ⚠️  | 14개 언어가 모두 번역됨; 달라진 부분은 굵은 글씨, `code`, 대괄호가 빠진 링크 등 **마크업** 수준임. 본문 텍스트, URL, 코드 블록, 섹션 누락 없음 |
| ❌  | 최소 1개 언어가 번역되지 못함(파일이 거부되어 작성되지 않음) **또는** 작성된 파일에서 내용 누락이 발생함                                                                      |

핵심 요약:

- **거부된 번역은 손상된 번역이 아닙니다.** 반환 시 토큰이 누락되면 파일이 작성되지 않으며 해당 언어는 거부된 것으로 간주됩니다. 기사 번역 시 Grok에서 발생한 현상으로, 5개의 비라틴 문자 언어 중 첫 번째 분할 세그먼트부터 4개의 인라인 코드와 3개의 URL이 누락되었습니다.
- **이 안전망은 제목, 표, front matter 및 일반 텍스트를 검사하지는 않습니다.** 섹션을 삭제하는 모델이 결과를 반환하면 도구는 이를 그대로 작성합니다(Mistral의 경우가 이에 해당). 이러한 요소는 토큰으로 대체할 수 없으며 현재의 가드가 제어하지 않습니다. `scripts/compare_structure.py`는 손실된 섹션을 감지할 수 있지만 사후에만 확인 가능합니다.
- **Grok은 본 README에 대한 점수가 없습니다**: 12개 언어 번역 후 CLI 세션이 만료되었으며(그중 11개는 차이 없음), 중단된 테스트는 점수를 매기지 않습니다.
- **언어보다 문서의 밀도가 더 중요합니다.** Grok은 일반적인 README에서는 잘 작동하지만 네덜란드어를 포함하여 링크가 많은 기사에서는 실패합니다.

날짜 및 문서 정보: "본 README" 열은 이 파일의 고정 리비전(785줄, 인라인 코드 285개, 표 89줄, 이후 수정됨)을 대상으로 2026년 9월 9일에 측정되었습니다. 단, Antigravity 행은 1.14.0과 함께 출시된 더 짧은 리비전(600줄, 인라인 코드 257개, 표 85줄)을 대상으로 9월 26일에 측정되었습니다. "정보 밀도가 높은 모니터링 기사" 열은 589줄 분량의 기사를 대상으로 진행한 9월 4~5일의 테스트 결과입니다(단, Grok 행은 동일 모니터링의 다른 판본으로 9월 9일에 재측정, Antigravity 행은 동일 기사로 9월 26일에 측정됨). 전체 표, 소요 시간 및 프로토콜은 [상세 측정 결과](#상세-측정)에서 확인할 수 있습니다.

## 모든 옵션

| 옵션                     | 설명                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일 (`--source_dir`의 대안)                                             |
| `--source_dir`           | Markdown 파일이 포함된 소스 디렉터리 (기본값: `content/posts`)                                   |
| `--target_dir`           | 번역된 파일이 저장될 출력 디렉터리 (기본값: `traductions_en`)                                    |
| `--source_lang`          | 원본 언어 (기본값: `fr`)                                                                                  |
| `--target_lang`          | 대상 언어 (기본값: `en`)                                                                                   |
| `--model`                | 사용할 특정 모델                                                                                  |
| `--eco`                  | 경제적인 모델 사용                                                                              |
| `--use_mistral`          | Mistral AI API 사용                                                                                     |
| `--use_claude`           | Claude API 사용                                                                                         |
| `--use_gemini`           | Gemini API 사용                                                                                         |
| `--use_grok`             | xAI (Grok) API 사용 — `XAI_API_KEY` 필요                                                           |
| `--use_codex`            | ChatGPT 구독 할당량 기반으로 Codex CLI 사용                                                    |
| `--use_grok_cli`         | Grok 구독 할당량 기반으로 Grok CLI 사용                                                        |
| `--use_antigravity`      | Google AI Pro 또는 Ultra 구독 할당량 기반으로 Antigravity CLI(`agy`) 사용                       |
| `--use_opencode`         | OpenCode(오픈 소스)에 구성된 공급자를 통해 OpenCode 사용; `--model provider/modèle` 필요 |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                          |
| `--force`                | 강제 재번역                                                                                       |
| `--keep_filename`        | 원본 파일 이름 유지                                                                          |
| `--news`                 | 뉴스 모드: 영어 인용문 보호, 언어별 국기 플래그 처리                                      |
| `--add_translation_note` | 번역 노트 추가                                                                                |
| `--note_position`        | 노트 위치: `top`, `bottom`(기본값), 또는 `both`                                                     |
| `--note_format`          | 노트 형식: `legacy`(기본값, 굵은 단락) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 강도: `none`/`low`/`medium`/`high`/`xhigh`                                         |

9개의 `--use_*` 플래그는 상호 배타적입니다. 두 개 이상을 함께 지정할 수 없습니다.

## 공급자

### API 방식: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 옵션은 각 제공업체의 절약형 요금제로 전환합니다.

| 제공업체 | 품질 (기본값) | 절약형 (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` (`--model` 사용 시 `terra` 및 `luna`도 지원) | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |
| Antigravity | `gemini-3.7-flash-medium` | `gemini-3.7-flash-low` |
| OpenCode | `--model provider/modèle` 필수 | 동일 — `--eco` 적용 안 됨 |
| OpenRouter | `--model fournisseur/modèle` 필수 | 동일 — `--eco` 적용 안 됨 |

### ChatGPT 구독 사용: `--use_codex`

공식 Codex CLI를 제어합니다. 번역은 API 키나 종량제 과금 없이 ChatGPT 구독 쿼터에서 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 실행 파일은 `CODEX_BIN`, 그 다음 `PATH`, 그 다음 패키지 `openai-codex-cli-bin` 순으로 검색됩니다. `~/.codex/auth.json`은 절대 읽히지 않습니다.
- 하위 프로세스 환경에서 `OPENAI_API_KEY` 및 `CODEX_API_KEY`가 제거됩니다. 키가 존재하더라도 API로 전환되지 않습니다.
- 각 세그먼트는 5시간 기간 내에서 최소 1개의 "메시지"를 소모하며, 유효성 검사에 실패하여 재시도할 경우 2개를 소모합니다. OpenAI의 예상치에 따르면 Plus 요금제 기준으로 `gpt-5.6-luna`(`--eco`)는 5시간당 250~2,000개, `gpt-5.6-sol`는 10~100개의 메시지입니다.
- `--model gpt-5.6-terra` 및 `--model gpt-5.6-luna`도 구독을 통해 전달됩니다. 계정에 권한이 없는 모델은 400 오류("model is not supported when using Codex with a ChatGPT account")를 반환합니다.
- API보다 느리며, 문서가 길어질수록 차이가 커집니다. 이 README의 경우 `gpt-5.6-sol` 사용 시 언어당 중앙값 6분 46초가 소요된 반면, `gemini-3.7-flash`는 36초였습니다.
- CI 환경(`CI` 또는 `GITHUB_ACTIONS` 정의됨)에서는 거부됩니다. 구독 인증에는 개인 세션 파일이 사용되므로 공유 러너에 두어서는 안 됩니다.
- 환경 변수: `CODEX_BIN`, `CODEX_TIMEOUT` (세그먼트당 초 단위 시간, 기본값 600).

### Grok 구독 사용: `--use_grok_cli`

공식 Grok Build CLI를 사용하는 동일한 원리로, SuperGrok 또는 X Premium+ 구독에서 작동합니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex보다 약한 격리.** Grok의 OS 샌드박스는 최신 Linux 환경(AppArmor, 컨테이너 런타임 소켓 등)의 상당수에서 적용되지 않으며, 프로필을 적용할 수 없는 경우 경고 없이 비격리 상태로 시작됩니다. 따라서 스크립트는 기본적으로 프로필을 요청하지 않고 이를 알린 후, 알림 없이 보호를 제거하는 대신 실행을 거부하는 유일한 계층인 포괄적(catch-all) 규칙 `*`를 포함한 CLI의 `--deny` 규칙에 의존합니다. `GROK_TRANSLATE_SANDBOX=read-only`는 OS 샌드박스를 요구하며, 머신이 이를 충족할 수 없으면 실행이 실패합니다.
- 쿼터는 주간 단위로 Chat, Imagine, Voice와 공유되며, 이를 조회할 수 있는 명령어가 없습니다. 따라서 배치 작업이 사전 알림 없이 대화형 사용량을 소진할 수 있습니다.
- 환경 변수: `GROK_BIN`, `GROK_HOME`(CLI 디렉터리, 기본값 `~/.grok`), `GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`.

### Google 구독 사용: `--use_antigravity`

Antigravity의 공식 CLI인 `agy`를 사용하는 동일한 원리입니다. Google AI Pro 또는 Ultra 구독자의 경우 번역이 토큰 단위로 과금되는 대신 구독 쿼터에서 차감됩니다. 이는 해당 쿼터를 활용하는 유일한 경로입니다. Gemini CLI는 2026년 6월 18일부로 해당 계정 지원을 중단했으며([공지](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)), Antigravity SDK는 API 키 또는 Google Cloud 프로젝트만 허용합니다.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **유료 과금 경로가 열려 있지 않습니다.** agy는 사용자 환경에서 닫힌 목록의 변수들(`PATH`, 언어 및 표준시, 터미널, ID, 프록시 및 인증서, 세션 버스)만 전달받고 키는 일체 전달받지 않습니다. agy의 여러 변수는 아무런 표시 없이 호출 경로를 전환할 수 있으며(테스트 결과: 하나는 문서를 서드파티 게이트웨이로 전송하고, 다른 하나는 과금되는 Google Cloud 프로젝트로 전송함), 거부 목록 방식은 매번 검토할 때마다 누락이 발생했습니다. 모든 세그먼트 시작 전, 쿼터를 소모하지 않는 `agy -p /config`를 통해 API 키나 Google Cloud 프로젝트 없이 유료 AI 크레딧이 비활성화되어 있음을 확인해야 합니다(설정이 없으면 거부됨). 그렇지 않으면 번역이 진행되지 않습니다. 또한 각 호출의 로그에서 구독 상태(`authMethod=consumer`)가 확인되어야 하며, 그렇지 않으면 응답이 거부됩니다.
- **격리.** 각 호출은 도구가 없는 번역 에이전트와 함께 격리된 일회용 개인 디렉터리에서 실행됩니다. 사용자의 기존 agy 설정, 규칙, 플러그인, MCP 서버 및 훅(hook)은 유입되지 않고, 기록에 아무것도 추가되지 않으며, 인증 정보는 키체인에 유지되어 aipmt가 절대 읽지 않습니다. 에이전트를 찾을 수 없으면 agy는 경고 없이 코딩 에이전트와 도구로 대체되므로, 로그의 전체 라인에서 올바른 에이전트가 확인되어야 하며(문서 내에서 이 메시지를 인용한 것은 대체할 수 없음), 그렇지 않으면 거부됩니다.
- **플랫폼**: 키체인이 있는 세션(D-Bus 세션 버스, Secret Service)의 Linux. macOS도 지원되나 별도 측정되지는 않았습니다. Windows(agy가 각 호출을 격리하는 변수를 읽지 못함) 및 세션 버스가 없는 Linux(SSH 세션, 컨테이너, 서버: agy가 토큰을 `~/.gemini` 파일에 저장하지만 격리로 인해 가려짐)에서는 거부됩니다. 로그인 코드를 기다리며 1분 동안 대기하는 대신 실행 전에 사유와 함께 거부됩니다.
- **모델**: `agy models`에서 지원하는 모델. Gemini 모델은 이름에 추론 강도가 포함되어 있습니다(`gemini-3.7-flash-low`…). 접미사가 없는 이름은 호출 전에 거부되며 `--reasoning_effort`는 적용되지 않습니다. 두 가지 기본값은 14개 언어에 대한 테스트를 거쳐 확정되었습니다([상세 측정]((#상세-측정)) 참조). Claude 및 GPT-OSS는 훨씬 더 작은 별도의 쿼터를 가집니다(Flash의 경우 호출당 약 0.05%인 반면, 측정된 호출당 5시간 기간의 약 1% 소모).
- **쿼터**: 그룹별로 토큰 비용에 비례하여 5시간 윈도우 및 주간 윈도우가 적용됩니다. 작성자의 계정에서 32회 번역 테스트를 측정한 결과, 40,000자 README 기준 `gemini-3.7-flash-medium`로 5시간 윈도우의 약 0.5%를 소모했습니다. 주간 한도는 등급에 따라 다릅니다. 재시도는 agy가 재시도 가능하다고 보고한 항목을 따르며, 그렇지 않은 경우 소진된 윈도우는 재시도되지 않고 `/usage`에 표시된 초기화 시점까지 각 파일이 실패 처리됩니다.
- **API보다 느림**: 밀도 높은 측정용 글 기준, Gemini 3.7 Flash는 구독 방식에서 언어당 중앙값 3분 14초가 걸린 반면, API는 1분 18초가 걸렸습니다.
- **중단**: Ctrl-C를 누르거나 터미널을 닫으면 agy가 쿼터를 소모하며 작업을 끝까지 마치는 대신 명령어와 함께 즉시 중단됩니다. 이는 Codex, Grok CLI, OpenCode도 마찬가지입니다. `nohup`에서는 번역이 계속 진행됩니다.
- CI 환경(`CI` 또는 `GITHUB_ACTIONS` 정의됨)에서는 거부됩니다. 인증 정보가 개인 키체인에 저장되기 때문입니다. 러너에서는 `GOOGLE_API_KEY`와 함께 `--use_gemini`를 사용하십시오.
- 환경 변수: `AGY_BIN`(지정하지 않으면 `PATH`, 그 다음 `~/.local/bin/agy`), `AGY_TIMEOUT`(시작 시간을 포함한 세그먼트당 초 단위 시간, 기본값 900).

**이용약관: 계정에 대한 책임은 사용자에게 있습니다.** [Antigravity 이용약관](https://antigravity.google/terms)(섹션 6) 및 [FAQ](https://antigravity.google/docs/faq/)에서는 Antigravity 로그인 정보를 사용하여 서드파티 소프트웨어(Claude Code, OpenClaw, OpenCode 등이 명시됨)를 통해 서비스에 접근하는 것을 금지하고 있으며, 위반 시 계정이 정지될 수 있습니다. aipmt는 토큰을 읽거나 재사용하지 않고, Google이 스크립트 및 CI용으로 문서화한 [헤드리스 모드](https://antigravity.google/docs/cli/headless/)로 공식 바이너리를 실행합니다. Google 관계자는 개인 작업을 위해 로컬 스크립트에서 `agy -p`를 실행하는 것이 "표준적"이라고 언급했으나([공식 포럼, 2026년 9월 25일자 비공식 답변](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)), 이와 같이 배포되는 도구의 사용에 대해서는 명확한 규정이 없습니다.

**공개 문서 전용.** 동일한 이용약관의 섹션 5에 따르면, 유료 구독을 포함하여 주고받은 프롬프트, 응답, 메타데이터 등의 상호작용 내역은 Google 제품 개선 및 머신러닝 학습에 사용될 수 있으며 인간 검토자에 의해 검토될 수 있습니다. 이를 거부하려면 효과가 문서화되지 않은 `enableTelemetry` 설정을 사용해야 하지만 aipmt는 이를 설정하지 않으며, agy의 격리 환경에는 사용자의 기존 agy 설정이 전달되지 않습니다. 기밀 정보는 절대 전달하지 마십시오.

### 원하는 제공업체 사용: `--use_opencode`

[OpenCode](https://opencode.ai)는 자체 구성된 제공업체(API 키, 구독, OpenCode Zen 게이트웨이(계정 불필요 무료 모델), 로컬 모델)로 라우팅하는 오픈 소스(MIT) 코드 에이전트입니다. 여기서는 Zen과 Ollama 두 가지 경로를 엔드투엔드로 측정했습니다.

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

`--model`는 필수입니다. 이 옵션이 없으면 OpenCode가 대화 내용이 학습에 사용될 수 있는 무료 모델로 대체되며, 이러한 선택을 임의로 대신하지 않습니다.

각 호출 시 격리 조치:

- 사용자 설정보다 우선하는 인라인 구성이 모든 도구가 비활성화(`permission: { "*": "deny" }`)되고 세션 공유가 비활성화된 `aipmt` 에이전트를 정의하며, `--pure`로 설정되고 절대 `--auto`가 적용되지 않습니다.
- 비어 있는 일회용 작업 디렉터리를 사용하며 `OPENCODE_DISABLE_PROJECT_CONFIG` 및 `OPENCODE_DISABLE_CLAUDE_CODE`가 설정됩니다. 이 설정이 없으면 OpenCode가 현재 디렉터리의 `AGENTS.md`와 `~/.claude/CLAUDE.md`를 프롬프트에 주입합니다. 전역 `~/.config/opencode/AGENTS.md`는 계속 주입되며 OpenCode에서는 이를 제외할 수 없습니다.
- 출력 계약: 반환 코드 0, `error` 이벤트 없음, 도구 호출 없음, 마지막 단계 `stop`, 비어 있지 않은 텍스트, 그리고 `aipmt` 에이전트가 실제로 로드됨 — 알 수 없는 `--agent`가 지정되어도 OpenCode는 실패하지 않고 코딩 에이전트로 조용히 대체됩니다.
- OpenCode 자체 키인 `OPENCODE_API_KEY`를 제외하고 `aipmt`의 어떤 키도 전달되지 않습니다. 제공업체 설정은 `aipmt`의 `.env`가 아닌 OpenCode 내에서 구성됩니다.

참고 사항:

- Zen의 무료 모델은 수시로 변경되고 제한 사항이 문서화되어 있지 않으며, 대화 내용이 학습에 사용될 수 있으므로 비공개 콘텐츠가 아닌 공개 문서에만 사용해야 합니다.
- 세그먼트 길이가 최대 16,000자에 이르므로 로컬 모델은 최소 16k 토큰의 컨텍스트를 제공해야 합니다. Ollama는 종종 4,096으로 설정되므로 `PARAMETER num_ctx 32768`가 포함된 `Modelfile`를 사용해야 합니다.
- `--eco`는 적용되지 않으며, `--reasoning_effort`는 OpenCode의 `--variant`로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 환경 변수: `OPENCODE_BIN`(지정하지 않으면 `PATH`, 그 다음 `~/.opencode/bin/opencode`), `OPENCODE_TIMEOUT`(세그먼트당 초 단위 시간, 기본값 600). `OPENCODE_CONFIG`는 OpenCode에 그대로 전달됩니다.

`~/.config/opencode/opencode.json`에서 Ollama를 통한 로컬 모델 구성 예시:

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

`reasoningEffort: "none"`는 Ollama가 이러한 모델에서 기본적으로 활성화하며 Modelfile로는 비활성화할 수 없는 추론 기능을 끕니다. 6개 단어로 된 문장에서 측정한 결과: 옵션이 없을 때는 919개의 추론 토큰과 68초가 소요되었으나, 옵션을 사용했을 때는 9개 토큰에 불과했습니다.

### 400개 이상의 모델 지원: `--use_openrouter`

OpenRouter는 단일 크레딧을 기반으로 타사가 호스팅하는 모델(여기서 다른 제공업체가 제공하지 않는 중국 오픈 소스 모델 포함)을 종량제로 연결해 주는 라우터입니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`는 필수입니다. 과금이 발생하기 전에 실행되는 사전 점검을 통해 라우팅의 두 가지 특성을 처리합니다:

- **동일한 모델이라도 서로 다른 한도를 가진 수십 개의 호스팅 업체에서 제공됩니다** — `z-ai/glm-5.3-flash`의 경우 23개 호스팅 업체 중 하나는 최대 출력 토큰이 2,048개로 제한되어 있습니다. 사전 점검 단계에서 `/api/v1/models/{modèle}/endpoints`를 읽어 출력 토큰이 8,000개 미만이거나 상태가 저하된 호스팅 업체를 제외하고 나머지를 `allow_fallbacks: false`로 고정합니다.
- **추론 토큰은 출력 요율로 과금됩니다** — `z-ai/glm-5.2`의 "OK" 응답 기준 2토큰 대신 107토큰이 소모됩니다. 추론은 기본적으로 비활성화되며, 추론이 강제되는 모델에는 허용되는 최저 추론 강도가 지정됩니다(카탈로그 기본값을 사용하면 번역이 끝나기 전에 출력이 한도에 도달할 수 있음). `--reasoning_effort` 설정이 항상 우선 적용됩니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 컨텍스트 윈도우 크기는 카탈로그에서 가져옵니다. 16,400 토큰 미만의 모델은 호출 전에 거부됩니다(프롬프트와 세그먼트에 8,400 토큰, 최소 8,000 출력 토큰).
- 카탈로그에 슬러그가 없거나, 카탈로그에 연결할 수 없거나, 한도를 충족하는 호스팅 업체가 없으면 명령이 중단됩니다.
- 출력이 비어 있는 `finish_reason=length`는 잘림이 아니라 추론에 의해 버짓이 소진된 경우이며, 오류 메시지에서 이를 구분하여 표시합니다.
- `--eco`는 적용되지 않습니다.
- 환경 변수: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>), `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30).

### 번역 고지

`--add_translation_note`는 `bottom`(기본값), `top`(front matter 뒤) 또는 `both`(`--note_position`) 위치에 `legacy`(굵은 글씨 단락, 기본값) 또는 `marker`(`--note_format`) 형식으로 고지 문구를 추가합니다. `marker` 형식은 보이지 않는 마크다운 참조 정의인 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` 뒤에 굵은 인용문이 붙는 형태입니다. GitHub에서 읽을 수 있으며 remark 플러그인을 통해 빌드 시 활용할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정

모든 측정치는 `aipmt`를 사용하여 14개 언어(en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi)로 실제로 실행한 번역 결과입니다. **작성됨**은 가드를 통과한 파일 수를 나타내며, **차이 없음**은 `scripts/compare_structure.py`에서 아무런 차이도 감지되지 않은 파일(섹션, 소제목, 링크, 고유 URL, 코드 블록, 인라인 코드, 표 행, 인용 블록, 굵은 글씨 단어의 수가 동일함) 수를 의미합니다.

"차이 없음"은 "동일함"이 아니라 "감지된 것이 없음"을 의미합니다. 비교 도구는 내용을 읽지 않고 요소의 개수만 셉니다. 삭제된 레벨 4 제목, 변경된 인라인 코드 텍스트, 바뀐 플래그 등을 감지하지 않으며, 언어의 품질을 평가하지 않습니다.

### 고밀도 모니터링 기사, `--news` 모드

[jls42.org의 AI 모니터링](https://jls42.org/fr/news) 기사 1건:
589줄, 140개 링크, 21개 섹션, 3개 보호된 영어 인용문. 2026년
9월 4일~5일 측정 캠페인.

| 모델                                            | 접근 방식          | 작성 완료 | 불일치 없음   | 언어당 중앙값  |
| ----------------------------------------------- | ------------------ | --------- | ------------- | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14     | ✅ **14/14**  | 1분 18초       |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 구독        | 14/14     | ✅ **14/14**  | 3분 14초       |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 구독       | 14/14     | ✅ **14/14**  | 11분 28초      |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14     | ✅ **14/14**  | 5분 37초       |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14     | ✅ **14/14**  | 26분 23초      |
| `claude-sonnet-5`                               | Anthropic API      | 14/14     | ⚠️ 11/14      | 6분 31초       |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14     | ❌ 11/14      | 9분 27초       |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14     | ❌ 8/14       | 10분 09초      |
| `ollama/gpt-oss-20b-32k`                        | 로컬               | 10/14     | ❌ 7/14       | 12분 39초      |
| `mistral-large-latest`                          | Mistral API        | 11/14     | ❌ 5/14       | 5분 32초       |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14      | ❌ 3/14       | 37분 27초      |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 구독          | 1/14      | ❌ 1/14       | 23분 11초      |

Grok은 9월 9일에 동일한 모니터링의 다른 회차(356줄)를 대상으로
재측정되었습니다: 14개 언어 중 9개 작성 완료, 8개 불일치 없음. 상단 표에
표시된 수치가 바로 이 결과입니다. 중단된 세 번의 캠페인은 기록되지
않았습니다: 크레딧 부족으로 중단된 `qwen3.5-27b`(9개 언어) 및 `kimi-k2.6`(4개),
그리고 제공업체가 이후 수정한 추론 설정으로 인해 2건의 실패가 발생했던
`z-ai/glm-5.3-flash`입니다. OpenRouter 행은 `--use_openrouter` 이전 라우터 기본
설정으로 측정되었습니다. 제공된 공급자로 재측정한 `z-ai/glm-5.2` 역시
동일하게 14/14를 기록했습니다. 수치는 9월 10일에 현재 비교 도구로 다시
계산되었습니다: `qwen3.8-flash` 및 `qwen3.7-flash`은 첫 발표 대비 각각
1개 언어를 추가로 획득했으며, 나머지는 변경되지 않았습니다.

`--use_antigravity` 행은 9월 26일 동일한 기사를 대상으로 4개 번역을
병렬 실행하여 측정되었습니다. 영어의 경우 모델이 인용문 아래의 세 줄짜리
프랑스어 번역을 임의의 플래그를 추가하지 않고 자체적으로 제거했으며, 영어
인용문은 온전하게 유지되어 폴백 정리가 필요하지 않았습니다.
`--eco`(`gemini-3.7-flash-low`)에서는 4개 언어(en, ja, ar, hi)에
대해서만 측정했을 때: 4개 중 4개 작성 완료, 모두 불일치 없음, 중앙값
1분 52초를 기록했습니다.

### 이 프로젝트의 README, 표준 Markdown

2026년 9월 9일 고정 리비전: 785줄, 인라인 코드 285개, 코드 블록
닫기 40개, 표 89줄. 4개 번역 병렬 실행.

| 모델                                            | 작성 완료 | 불일치 없음 | 언어당 중앙값 | 차이점                                                                   |
| ----------------------------------------------- | --------- | ----------- | ------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`                              | 14/14     | ⚠️ 13/14    | 36초          | 굵은 글씨 단어 1개 (ja)                                                  |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14     | ⚠️ 13/14    | 1분 22초      | 굵은 글씨 단어 1개 (ko)                                                  |
| `claude-sonnet-5`                               | 14/14     | ⚠️ 12/14    | 2분 56초      | 링크 1개 (sv), 굵은 글씨 단어 1개 (zh)                                   |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14     | ⚠️ 12/14    | 6분 46초      | 굵은 글씨 단어 1개 (ar, ja)                                              |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14     | ⚠️ 11/14    | 2분 34초      | 굵은 글씨 단어 1개 (hi, ja, ko)                                          |
| `qwen/qwen3.7-flash`                            | 14/14     | ⚠️ 10/14    | 2분 17초      | 아랍어에서 인라인 코드 40개 추가됨; 굵은 글씨 (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14     | ❌ 1/14     | 2분 44초      | 섹션 1개 누락 (ar, hi, ko); 코드 블록 추가됨 (ja, ko, ro, zh)           |

중단된 두 번의 캠페인은 기록되지 않았습니다: Grok은 12개 언어(11개
불일치 없음) 후 CLI 세션 만료, `qwen3.8-flash`은 2개 후 호스팅 제공업체에서
HTTP 429 오류가 발생했습니다. `opencode/mimo-v2.5-free` 및 `ollama/gpt-oss-20b-32k`은
이번 리비전에서 재측정되지 않았으며, 277줄 더 짧았던 9월 4일~5일
리비전에서는 각각 14개 중 9개의 번역을 작성했고 그중 7개와 1개가
불일치 없음이었습니다.

`--use_antigravity` 행은 고정 리비전에서 측정되지 않고, 9월 26일에
1.14.0과 함께 릴리스된 버전(600줄, 인라인 코드 257개, 코드 블록 닫기 30개,
표 85줄)에서 측정되었습니다. 185줄 더 짧으므로 다른 행들과 직접 일대일
비교할 수는 없습니다.

### 잘 알려진 4개 프로젝트의 README

GitHub에서 그대로 가져온 FastAPI, Ollama, tldr-pages, Vue.js — 이전
두 문서보다 더 쉬운 문서들입니다. 이 캠페인은 어려움을 겪는 모델들을
대상으로 했으며, Gemini가 비교 기준으로 사용됩니다.

| 모델                          | 범위                       | 작성 완료 | 불일치 없음   |
| ----------------------------- | -------------------------- | --------- | ------------- |
| `gemini-3.7-flash`            | 4개 프로젝트 × 14개 언어   | 56/56     | ✅ **55/56**  |
| `opencode/mimo-v2.5-free`     | 4개 프로젝트 × 14개 언어   | 55/56     | ❌ 47/56      |
| `grok-4.6` (구독)        | 4개 프로젝트 × ar, hi, ja, zh | 16/16     | ❌ 14/16      |
| `ollama/gpt-oss-20b-32k`      | 4개 프로젝트 × ar, hi, ja, zh | 15/16     | ❌ 9/16       |

### 이 측정 결과가 의미하지 않는 것

- **완전한 순위가 아님**: OpenRouter 하나만 해도 400개가 넘는 모델을
  제공하지만, 측정된 것은 15개 정도에 불과합니다.
- **참고용 소요 시간**: 캠페인에 따라 3개에서 6개의 병렬 번역을
  실행했으며, 공급자의 처리량은 하루 중에도 달라집니다.
- **특정 시점의 관찰 결과**: 모델은 같은 이름 아래에서도 변경되며, 사용자의
  문서는 본 테스트 문서와 다릅니다.

고정된 파일 사본을 사용하여 본인의 문서에서 측정을 재현하려면:

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

두 줄 모두 필요합니다: `pip install -e .`이 없으면 `python -m aipmt`이
`No module named aipmt`을 반환합니다.

품질 도구 (선택 사항이지만 권장됨):

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 28개 번역(README 및 CHANGELOG, 14개 언어)은
`./regen_translations.sh --force`을 통해 재생성됩니다 — 기본적으로 ChatGPT 구독에서
Codex 및 `gpt-5.6-sol`을 사용하여 4개를 병렬로 처리합니다. `REGEN_PROVIDER` 및
`REGEN_MODEL`은 경로를 변경합니다: `antigravity`은 구독(Google)을
그대로 유지하며 예외 없이 통과됩니다. 유료 API(`openai`, `gemini`,
`grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다.
`REGEN_JOB_TIMEOUT`은 각 작업의 상한을 설정합니다(600초, Codex 및
Antigravity의 경우 1,800초). 도구에 대한 자세한 내용은 `CLAUDE.md`에
있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 발행되는 개인 블로그.
  [일간 AI 모니터링](https://jls42.org/fr/news)이 매일 이 도구로 번역되며,
  위 측정의 기준 문서로 사용됩니다.

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

## 면책 조항

이 프로그램은 GPL v3 제15조 및 제16조의 조건에 따라 **어떠한 보증도
없이** 배포됩니다: "있는 그대로" 제공되며 상품성이나 특정 목적에의
적합성에 대한 보증이 없으며, 작성자는 프로그램 사용으로 인해 발생하는 손해에
대해 책임을 지지 않습니다. 이 요약문보다 라이선스 원문이 우선합니다.

- **게시하기 전에 검토하세요.** 보호 기능은 코드 블록, 인라인 코드,
  URL, 앵커 및 `--news` 모드의 인용문에 적용되며, 제목, 표,
  프론트매터 또는 문장의 의미는 보호 대상에 포함되지 않습니다.
- **문서는 선택한 공급업체로 전송되며**, 해당 업체의 이용약관 및 데이터
  정책이 적용됩니다. 일부 무료 모델은 대화 내용을 학습에 재사용할 수 있으며,
  Antigravity의 약관에 따르면 유료 구독을 포함하여 Google이 데이터를
  재사용하고 사람에게 검토하도록 할 수 있습니다. 로컬 모델만이 머신 외부로
  데이터를 유출하지 않는 유일한 방법입니다.
- **API 호출 비용이 청구됩니다.** 이 프로그램은 지출 한도를 제한하지
  않습니다: 긴 문서, 실패 후 재시도 또는 추론을 많이 수행하는 모델은
  더 많은 비용이 발생합니다.
- **발표된 측정 수치는 특정 시점의 관찰 결과이며**, 보증이 아닙니다.

언급된 제품 및 회사 이름은 해당 소유자의 자산입니다. 이 프로젝트는 이들
중 어느 곳과도 제휴되어 있지 않습니다.

**gemini-3.7-flash-medium으로 프랑스어에서 한국어로 번역된 기사.**
