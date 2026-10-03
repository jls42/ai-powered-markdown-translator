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

코드 블록, 인라인 코드, URL, 앵커, 표, 프론트매터를 포함한 구조를 보존하면서 마크다운 파일을 한 언어에서 다른 언어로 번역합니다. 모델을 호출하는 11가지 방법(5개의 API, 사용량 기반 과금이 없는 4개의 구독 서비스, 2개의 라우터)과 각 모델이 실제로 무엇을 보존하는지에 대해 공개된 측정 결과를 제공합니다.

## 요약

- **11가지 제공자(provider) 경로**: OpenAI, Mistral, Claude, Gemini, Grok API; 사용량 기반 과금이 없는 ChatGPT(Codex), Grok, Google(Antigravity), Claude(Claude Code) 구독 서비스; OpenCode(오픈 소스, 무료 또는 로컬) 및 OpenRouter(400개 이상의 모델) 라우터.
- **토큰 누락으로 인한 왜곡 방지**: 호출 전에 코드 블록, 인라인 코드, URL, 앵커 및 인용문이 토큰으로 대체되며 반환 시 검증됩니다. 하나라도 누락되면 파일이 작성되지 않습니다.
- **긴 문서 처리**: 모델의 컨텍스트 창에 따른 세분화(분할).
- **`--news` 모드**: 모니터링/트렌드 기사를 위해 영어 인용문을 보호하고 언어별 플래그를 관리합니다.
- **`--eco` 모드**: 빠르고 비용 효율적인 모델.
- 상단, 하단 또는 양쪽 모두에 선택 가능한 **번역 노트**.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 이상. 저장소에서 설치하는 방법은 [기여하기](#기여하기)를 참조하세요.

## 설정

키는 우선순위가 높은 순서대로 세 곳에서 읽히며, 이전 단계에서 비어 있는 항목만 다음 단계에서 채웁니다.

|     | 위치                                          | 용도                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                                     | CI, 컨테이너, 일회성 재정의           |
| 2   | 현재(또는 상위) 디렉터리의 `.env`      | 프로젝트 전용 키                      |
| 3   | `~/.config/aipmt/.env`                        | 한 번 설치하면 어디서나 유효함        |

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

`GOOGLE_API_KEY` 대신 `GEMINI_API_KEY`를 사용할 수 있습니다. 사용자 파일은 `XDG_CONFIG_HOME`(절대 경로만 해당) 및 Windows의 `%APPDATA%`을 따릅니다. 키가 없으면 명령어가 세 위치를 모두 나열합니다.

**프로젝트의 `.env`은 호출을 리디렉션하거나 실행할 프로그램을 선택할 수 없습니다.** 키만 제공할 뿐 대상이나 바이너리는 절대 제공하지 않습니다. `_BASE_URL`, `_API_BASE`, `_ENDPOINT` 또는 `_BIN`의 모든 변수(`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, 프록시(`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), 인증서 저장소(`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) 및 `XDG_CONFIG_HOME` / `APPDATA`은 경고와 함께 무시됩니다. 복제된 저장소가 키를 가로채거나 첫 번째 번역 시 자체 프로그램을 실행하도록 해서는 안 됩니다. 또한 이 파일은 보간(interpolation) 없이 읽히므로 `NOM=${OPENAI_API_KEY}`가 키를 복사하지 않습니다. 이러한 변수는 환경 변수 또는 `~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`), `CLAUDE_TIMEOUT`(호출당 초, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`(기본값 600), `GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`), `GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT`(기본값 900), `OPENCODE_BIN`, `OPENCODE_TIMEOUT`(기본값 600), `OPENROUTER_BASE_URL`(`https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각 변수는 해당 제공자 섹션에 자세히 설명되어 있습니다.

## 시작하기

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

스페인어로 번역된 `document.md`은 `--target_dir` 내의 `document-es.md`을 생성하며, `--include_model`을 지정하면 `document-es-gpt-5.6-terra.md`이 됩니다. 원래 이름을 유지하는 `--keep_filename`를 제외하고 확장자는 항상 `.md`로 변경됩니다(`article.mdx`은 `article-en.md`가 됨). 이미 존재하는 번역본은 `--force` 옵션이 없으면 건너뜁니다.

종료 코드: 모두 성공했거나 건너뛴 경우 `0`, 실패한 파일이 남아 있는 경우(표준 오류에 목록 출력) `1`, 설정에 문제가 있는 경우 `2`. 쓰기 자체가 실패하더라도 실패한 파일은 절대 작성되지 않습니다. 내용은 임시로 작성된 후 이름이 변경됩니다. 다시 실행하기만 하면 됩니다.

## 어떤 모델을 선택해야 할까요

실제 문서 2개를 대상으로 각 모델이 동일한 14개 언어로 번역하여 측정한 결과입니다. **숫자는 14개 언어 중 번역이 정상적으로 작성되고 원본과 비교해 차이가 전혀 없는 언어의 수입니다.**

| 모델 | 접근 방법 | 정보 밀도가 높은 기사 | 이 README | 차이점 및 해당 언어 수 |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Google 구독(Antigravity) | ✅ 14/14 | ✅ 14/14 | 두 문서 모두 차이 없음 |
| **Gemini 3.7 Flash** | Google API 키 | ✅ 14/14 | ⚠️ 13/14 | 14개 중 1개 언어: 굵은 글씨 단어 1개 추가(ja) |
| **Gemini 3.7 Flash** | Google 구독(Antigravity) | ✅ 14/14 | ⚠️ 13/14 | 14개 중 1개 언어: 굵은 글씨 단어 1개 누락(ko) |
| **GPT-5.6 Sol** | ChatGPT 구독 또는 OpenAI 키 | ✅ 14/14 | ⚠️ 12/14 | 14개 중 2개 언어: 굵은 글씨 단어 1개 누락(ar, ja) |
| **GLM-5.2** | OpenRouter 키 | ✅ 14/14 | ⚠️ 11/14 | 14개 중 3개 언어: 굵은 글씨 단어 1개 누락(hi, ja, ko) |
| Claude Sonnet 5 | Claude 구독(Claude Code) | ⚠️ 13/14 | ⚠️ 13/14 | 기사에서 14개 중 1개 언어: 굵은 글씨 단어 1개 추가(zh); 이 README에서 1개: 표 행이 이전 행에 붙어 화면에 숨겨짐(ar) |
| Claude Haiku 4.5 | Claude 구독(Claude Code) | ⚠️ 11/14 | ✅ 14/14 | 기사에서 14개 중 3개 언어: 섹션 제목이 1단계로 변경됨(en, pl, ro); 이 README에서는 비교기 기준으로 차이 없으나 내부 링크가 영어로 중복됨 |
| Claude Sonnet 5 | Anthropic API 키 | ⚠️ 11/14 | ⚠️ 12/14 | 기사에서 14개 중 3개 언어: 예기치 않은 코드 블록 생성(es, de, hi); 이 README에서 2개: 마크업이 누락된 링크(sv), 굵은 글씨 단어(zh) |
| Qwen 3.7 Flash | OpenRouter 키 | ❌ 8/14 | ⚠️ 10/14 | 기사에서 1개 언어 거부됨, 5개 언어에서 차이 발생; 이 README에서는 약 40개 단어가 `code` 처리됨(ar) |
| Grok 4.6 | Grok 구독 | ❌ 8/14 | 미평가 | 14개 중 5개 언어 거부됨(인라인 코드 및 URL 반환 실패); 네덜란드어는 전반적으로 일탈함 |
| GPT-OSS 20B | 로컬 모델(Ollama) | ❌ 7/14 | 재측정 안 됨 | 14개 중 4개 언어 거부됨: 프랑스어 구문이 그대로 남아 있어 가드(guard)에 의해 차단됨 |
| MiMo v2.5 (무료) | OpenCode Zen(계정 필요 없음) | ❌ 11/14 | 재측정 안 됨 | 1개 언어 거부됨; 폴란드어에서 섹션 1개 유실 |
| Mistral Large | Mistral API 키 | ❌ 5/14 | ❌ 1/14 | **전체 섹션 누락**: 기사에서 14개 중 1개 언어(hi), 이 README에서 3개(ar, hi, ko) — 기사에서 3개 언어 거부됨 |
| DeepSeek V4 Flash | OpenRouter 키 | ❌ 3/14 | 재측정 안 됨 | 14개 중 10개 언어 거부됨; 언어당 37분 소요 |
| Claude Opus 5.5 | Claude 구독(Claude Code) | ❌ 0/14 | ✅ 14/14 | 생물학 단신 기사로 인해 Opus 가드레일에 의해 14개 전 언어에서 기사 거부됨; 이 README에서는 차이 없음 |

|     | 기호의 의미                                                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14개 언어가 모두 번역되었으며, 원본과 일치함                                                                                                                                                          |
| ⚠️  | 14개 언어가 모두 번역됨; 차이점은 굵은 글씨 단어, `code`, 대괄호가 누락된 링크 등 **마크업** 수준임. 누락된 텍스트, URL, 코드 블록, 섹션은 없음                                            |
| ❌  | 최소 1개 이상의 언어가 번역되지 못함(파일이 거부되어 작성되지 않음) **또는** 작성된 파일에서 일부 콘텐츠가 누락됨                                                                                    |

핵심 요약:

- **거부된 번역은 손상된 번역이 아닙니다.** 반환 시 토큰이 누락되면 파일이 작성되지 않으며 해당 언어는 거부된 것으로 처리됩니다. 기사 번역 시 Grok에서 발생한 문제가 바로 이것입니다. 5개의 비라틴 문자 언어에서 첫 번째 세그먼트부터 4개의 인라인 코드와 3개의 URL이 누락되었습니다.
- **모델이 단 한 문장 때문에 문서 전체를 거부할 수도 있습니다.** Opus 5.5는 이 README를 오차 없이 번역하지만, 트렌드 기사는 전혀 번역하지 못했습니다. 생물학 관련 단신 기사로 인해 가드레일이 응답을 중단시켰기 때문입니다. 파일은 작성되지 않으며, aipmt가 그 이유를 알려줍니다.
- **이 안전망은 제목, 표, 프론트매터 및 텍스트를 감지하지 않습니다.** 모델이 특정 섹션을 삭제하더라도 도구는 아무 문제 없이 파일을 작성합니다(Mistral의 경우가 이에 해당). 이러한 요소는 토큰으로 대체할 수 없으며 현재 가드가 이를 검사하지 않습니다. `scripts/compare_structure.py`이 누락된 섹션을 감지할 수 있지만 이는 사후 확인일 뿐입니다.
- **Grok은 이 README에 대한 점수가 없습니다**: 12개 언어(그중 11개는 차이 없음) 번역 후 CLI 세션이 만료되었습니다. 중단된 테스트는 평가 점수를 매기지 않습니다.
- **언어보다 문서의 밀도가 더 중요합니다.** Grok은 일반적인 README에서는 잘 작동하지만 네덜란드어를 포함하여 링크가 많은 기사에서는 실패합니다.

날짜 및 문서: "이 README" 열은 2026년 9월 9일에 이 파일의 고정 리비전(785줄, 인라인 코드 285개, 표 89줄, 이후 수정됨)을 기준으로 측정되었습니다. 단, Antigravity 및 Claude Code 행은 1.14.0과 함께 출시된 더 짧은 리비전(600줄, 인라인 코드 257개, 표 85줄)을 기준으로 9월 26일에 측정되었습니다. "정보 밀도가 높은 기사" 열은 589줄 기사를 대상으로 한 9월 4~5일 테스트 결과입니다. 단, Grok 행은 동일한 트렌드 기사의 다른 에디션을 대상으로 9월 9일에 재측정되었고, Antigravity 및 Claude Code 행은 동일한 기사를 대상으로 9월 26일에 측정되었습니다. 전체 표, 소요 시간 및 프로토콜은 [상세 측정 결과](#상세-측정-결과)에서 확인할 수 있습니다.

## 모든 옵션

| 옵션                   | 설명                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일 (`--source_dir`의 대안)                                             |
| `--source_dir`           | Markdown 파일이 포함된 소스 디렉터리 (기본값: `content/posts`)                                   |
| `--target_dir`           | 번역된 파일의 출력 디렉터리 (기본값: `traductions_en`)                                    |
| `--source_lang`          | 소스 언어 (기본값: `fr`)                                                                                  |
| `--target_lang`          | 대상 언어 (기본값: `en`)                                                                                   |
| `--model`                | 사용할 특정 모델                                                                                  |
| `--eco`                  | 경제형 모델 사용                                                                              |
| `--use_mistral`          | Mistral AI API 사용                                                                                     |
| `--use_claude`           | Claude API 사용                                                                                         |
| `--use_gemini`           | Gemini API 사용                                                                                         |
| `--use_grok`             | xAI (Grok) API 사용 — `XAI_API_KEY` 필요                                                           |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용                                                    |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                                                        |
| `--use_antigravity`      | Google AI Pro 또는 Ultra 구독 할당량으로 Antigravity CLI (`agy`) 사용                       |
| `--use_claude_code`      | Claude Pro 또는 Max 구독 할당량으로 Claude Code CLI (`claude -p`) 사용                      |
| `--use_opencode`         | OpenCode(오픈 소스)를 사용하여 OpenCode에 구성된 제공자로 연결; `--model provider/modèle` 필수 |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                          |
| `--force`                | 강제 재번역                                                                                       |
| `--keep_filename`        | 원본 파일 이름 유지                                                                          |
| `--news`                 | 뉴스 모드: EN 인용문 보호, 언어별 플래그 처리                                      |
| `--add_translation_note` | 번역 안내 문구 추가                                                                                |
| `--note_position`        | 안내 문구 위치: `top`, `bottom` (기본값), 또는 `both`                                                     |
| `--note_format`          | 안내 문구 형식: `legacy` (기본값, 굵은 단락) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 노력: `none`/`low`/`medium`/`high`/`xhigh`                                         |

9개의 `--use_*` 플래그는 상호 배타적입니다. 두 개를 함께 조합하는 것은
허용되지 않습니다.

## 제공자

### API 방식: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 플래그는 각 제공자의 경제형 티어로 전환합니다.

| 제공자      | 품질 (기본값)                                      | 경제형 (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (`--model`을 통한 `terra` 및 `luna`도 지원) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, 추론 노력 `low`                                | 동일함 — `--eco` 효과 없음 |
| OpenCode    | `--model provider/modèle` 필수                 | 동일함 — `--eco` 효과 없음 |
| OpenRouter  | `--model fournisseur/modèle` 필수              | 동일함 — `--eco` 효과 없음 |

### ChatGPT 구독 기반: `--use_codex`

공식 Codex CLI를 제어합니다. 번역은 API 키나 종량제 결제 없이 ChatGPT 구독
할당량에서 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 바이너리는 `CODEX_BIN`, `PATH`, `openai-codex-cli-bin` 패키지
  순으로 검색됩니다. `~/.codex/auth.json`은 읽히지 않습니다.
- 하위 프로세스 환경에서 `OPENAI_API_KEY` 및 `CODEX_API_KEY`가 제거되므로,
  키가 존재하더라도 API로 전환되지 않습니다.
- 각 세그먼트는 5시간 기간의 "메시지" 최소 1개를 소모하며, 유효성 검사에 실패하여
  재시도하는 경우 2개가 소모됩니다. OpenAI는 예상치로 Plus 플랜 기준 `gpt-5.6-luna`
  (`--eco`)의 경우 5시간당 250~2,000개, `gpt-5.6-sol`의 경우 10~100개라고 발표했습니다.
- `--model gpt-5.6-terra` 및 `--model gpt-5.6-luna` 역시 구독을 거칩니다. 계정 권한이 없는
  모델의 경우 400 "model is not supported when using Codex with a ChatGPT account" 오류를 반환합니다.
- API보다 느리며, 문서가 길어질수록 격차가 커집니다. 이 README를 기준으로
  중앙값 기준 언어당 `gpt-5.6-sol`는 6분 46초가 소요된 반면, `gemini-3.7-flash`는
  36초가 소요되었습니다.
- CI 환경에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS` 정의됨). 구독 인증은
  개인 세션 파일로 이루어지므로 공유 러너에 둘 수 없습니다.
- 환경 변수: `CODEX_BIN`, `CODEX_TIMEOUT` (세그먼트당 시간(초), 기본값 600).

### Grok 구독 기반: `--use_grok_cli`

SuperGrok 또는 X Premium+ 구독을 통해 공식 Grok Build CLI로 동일한 원리를 적용합니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex보다 약한 격리 수준.** Grok의 OS 샌드박스는 최신 Linux 시스템
  (AppArmor, 컨테이너 런타임 소켓 등) 다수에서 적용되지 않으며, 적용할 수 없는
  프로필은 사용자에게 알리지 않고 격리되지 않은 상태로 자동 시작됩니다. 따라서 이 스크립트는
  기본적으로 프로필을 요청하지 않고 이를 고지하며, CLI의 `--deny` 규칙
  (예고 없이 보호를 해제하는 대신 시작을 거부하는 유일한 계층인 포괄적 `*` 포함)에
  의존합니다. `GROK_TRANSLATE_SANDBOX=read-only`는 OS 샌드박스를 강제하며, 머신이 이를 충족하지 못하면
  시작에 실패합니다.
- 할당량은 Chat, Imagine, Voice와 공유되는 주간 단위이며 이를 확인하는 명령어가
  없습니다. 일괄 작업 실행 시 별도의 알림 없이 대화형 사용량이 차감될 수 있습니다.
- 환경 변수: `GROK_BIN`, `GROK_HOME` (CLI 디렉터리, 기본값 `~/.grok`),
  `GROK_TIMEOUT` (기본값 900), `GROK_TRANSLATE_SANDBOX`.

### Google 구독 기반: `--use_antigravity`

Antigravity 공식 CLI인 `agy`를 사용하여 동일한 원리를 적용합니다. Google
AI Pro 또는 Ultra를 구독 중인 경우 토큰별 과금 대신 구독 할당량에서 번역이
차감됩니다. 이는 해당 할당량을 활용할 수 있는 유일한 경로입니다. Gemini CLI는
2026년 6월 18일부로 해당 계정 지원을 중단했으며([공지](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
Antigravity SDK는 API 키 또는 Google Cloud 프로젝트만 허용합니다.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **유료 결제 경로를 완전히 차단합니다.** agy는 사용자의 환경에서 사전에 지정된
  환경 변수 목록만 전달받습니다(`PATH`, 언어 및 표준시, 터미널, ID,
  프록시 및 인증서, 세션 버스). 키는 일절 전달되지 않습니다. agy의 일부 환경 변수는
  화면 표시 없이 호출 대상을 변경하며(실측 결과: 하나는 문서를 서드파티 게이트웨이로 전송하고,
  다른 하나는 유료 청구되는 Google Cloud 프로젝트로 전송함), 차단 목록 방식은 검토할 때마다
  누락이 발생했습니다. 각 세그먼트 시작 전 할당량을 소모하지 않는 `agy -p /config`를 통해
  유료 AI 크레딧이 비활성화되어 있고 API 키나 Google Cloud 프로젝트가 없는지 확인해야 합니다.
  설정이 없으면 즉시 거부되며 번역이 진행되지 않습니다. 또한 각 호출의 로그에서
  구독 상태(`authMethod=consumer`)가 확인되어야 하며, 그렇지 않으면 응답이 거부됩니다.
- **격리.** 각 호출은 도구가 없는 번역 전용 에이전트와 함께 일회용 개인 디렉터리에서
  실행됩니다. 사용자의 기존 agy 설정, 규칙, 플러그인, MCP 서버, 훅은 유입되지 않으며,
  기록에도 아무것도 추가되지 않습니다. 연결 상태는 키체인에 유지되며 aipmt는 이를 절대
  읽지 않습니다. 에이전트를 찾을 수 없는 경우 agy는 별도 안내 없이 코딩 에이전트 및 도구로
  폴백합니다. 따라서 로그의 한 줄 전체가 올바른 에이전트를 확인해야 하며(해당 메시지를
  인용하는 문서는 인정되지 않음), 그렇지 않으면 거부됩니다.
- **지원 플랫폼**: 키체인이 있는 세션(D-Bus 세션 버스, Secret Service)이 구비된 Linux.
  macOS도 허용되나 실측 테스트는 거치지 않았습니다. 각 호출을 격리하는 환경 변수를 읽지 못하는
  Windows와 세션 버스가 없는 Linux(SSH 세션, 컨테이너, 서버 등: agy가 격리로 인해 숨겨지는
  `~/.gemini` 파일에 토큰을 저장함)에서는 거부됩니다. 로그인 코드 대기로 1분을 낭비하는 대신
  실행 전 원인과 함께 거부됩니다.
- **모델**: `agy models`에 나열된 모델. Gemini 모델은 이름에 추론 노력이 포함되어
  있습니다(`gemini-3.8-flash-medium` 등). 접미사가 없는 이름은 호출 전에 거부되며,
  `--reasoning_effort`는 적용되지 않습니다. 기본값은 `gemini-3.8-flash-medium`이며,
  `--eco`에서는 `gemini-3.7-flash-low`입니다. 이를 결정한 테스트 작업은
  [상세 측정 결과](#상세-측정-결과)에 설명되어 있습니다. Claude와 GPT-OSS는
  훨씬 작은 독자적인 할당량을 가집니다. 실측 호출당 Flash가 0.05%를 소모하는 반면,
  이들은 5시간 기간의 약 1%를 소모합니다.
- **할당량**: 그룹별로 5시간 기간 및 주간 기간이 적용되며 토큰 비용에 비례합니다.
  작성자 계정 기준으로 측정한 결과는 소스 문자 100만 자당 5시간 기간 기준으로 `gemini-3.8-flash-medium`에서
  약 16포인트, `gemini-3.7-flash-medium`에서 14포인트, 낮은 추론 노력에서는 7~8포인트가 소모되었습니다.
  즉, 4만 자 분량의 README는 0.5포인트를 조금 넘게 소모합니다. 주간 한도는 티어에 따라 다릅니다.
  재시도는 agy가 재시도 가능하다고 보고한 내용을 따릅니다. 할당량이 소진된 경우
  재시도하지 않으며, `/usage`에 표시되는 초기화 시점까지 각 파일 처리가 실패합니다.
- **API보다 느린 속도**: 측정에 사용된 밀도 높은 기사 기준, 중앙값 언어당 처리 시간은
  `gemini-3.8-flash-medium`에서 3분 59초, `gemini-3.7-flash-medium`에서 3분 14초였던 반면,
  Gemini 3.7 Flash API는 1분 18초였습니다.
- **작업 중단**: Ctrl-C를 누르거나 터미널을 닫으면 agy가 할당량을 소모하며 작업을 끝까지
  수행하는 대신 명령어와 함께 즉시 중단됩니다. Codex, Grok CLI, OpenCode도 동일하게 동작합니다.
  `nohup` 환경에서는 번역이 계속 진행됩니다.
- CI 환경에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS` 정의됨). 인증 정보가
  개인 키체인에 저장되기 때문입니다. 러너에서는 `GOOGLE_API_KEY`와 함께 `--use_gemini`를 사용하세요.
- 환경 변수: `AGY_BIN` (없는 경우 `PATH`, 그 다음 `~/.local/bin/agy`),
  `AGY_TIMEOUT` (시작 시간 포함 세그먼트당 시간(초), 기본값 900).

**이용약관: 사용자 계정에 대한 책임.**
[Antigravity 이용약관](https://antigravity.google/terms)(섹션 6) 및
[FAQ](https://antigravity.google/docs/faq/)에서는 Antigravity 연결을 통해
서드파티 소프트웨어(Claude Code, OpenClaw, OpenCode 명시)로 서비스에 접근하는 것을 금지하며,
위반 시 계정이 정지될 수 있습니다. aipmt는 토큰을 읽거나 재사용하지 않으며, Google이
스크립트 및 CI용으로 문서화한 [헤드리스 모드](https://antigravity.google/docs/cli/headless/)로
공식 바이너리를 실행합니다. Google 관계자는 자신의 작업을 위해 로컬 스크립트에서
`agy -p`를 실행하는 것을 "표준적인 방식"이라고 언급한 바 있으나
([공식 포럼, 2026년 9월 25일, 비계약적 답변](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)),
이와 같이 배포되는 도구의 사용에 대해 명확한 유권해석을 내린 규정은 없습니다.

**공개 문서에만 사용하십시오.** 동일 약관 섹션 5에 따르면, 프롬프트, 응답, 메타데이터를
포함한 상호작용 내용은 유료 구독을 포함하여 Google의 제품 및 머신러닝 개선에 사용될 수
있으며 사람에 의해 검토될 수 있습니다. 데이터 수집 거부는 `enableTelemetry` 설정을 통해
이루어지나, 동작 방식이 문서화되어 있지 않으며 aipmt는 이를 설정하지 않습니다. 사용자의
agy 설정은 격리 환경으로 전달되지 않습니다. 기밀 문서는 절대 처리하지 마십시오.

### Claude 구독 사용: `--use_claude_code`

`-p` 모드의 Claude Code 공식 CLI인 `claude`도 원리는 동일합니다. Claude Pro 또는 Max 구독자라면 번역 비용이 토큰별로 청구되는 대신 구독 쿼터에서 차감됩니다. 사용량 기반으로 요금이 청구되는 Anthropic의 API인 `--use_claude`과 혼동해서는 안 됩니다.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **유료 결제 경로가 열려 있지 않으며, 각 호출이 이를 증명합니다.** Claude Code는 사용자의 환경에서 제한된 변수 목록만 전달받습니다. API 키, 토큰, 클라우드 제공업체 정보, aipmt가 실행된 Claude Code 세션 식별자 등은 일절 전달되지 않습니다. 첫 번째 세그먼트 전, `claude auth status`에서 Console 키 없이 구독 연결 상태를 보여주어야 하며, 쿼터를 소모하지 않는 `/usage`가 이를 증명해야 합니다. 또한 각 호출은 초기화 이벤트에서 이를 다시 확인하며, 그렇지 않으면 응답이 거부됩니다.
- **추가 요금 0원을 유지하려면 "extra usage"를 비활성화하세요** (claude.ai, Settings → Usage). 활성화되어 있으면 한도가 소진되었을 때 자동으로 전환되어 오류 표시 없이 요금이 청구됩니다. aipmt는 호출 시 쿼터 확인을 통해 한도 소진이 감지되는 즉시 번역을 중단하지만, 해당 호출은 이미 사용량에 포함됩니다.
- **Claude Code 세션과 쿼터 공유.** 각 호출은 5시간 창 및 주간 쿼터 사용량을 보고합니다. 본 작업에 사용할 한도가 소진되지 않도록 80%(`AIPMT_CLAUDE_MAX_UTILIZATION`)를 초과하면 더 이상 세그먼트를 실행하지 않습니다.
- **격리(Confinement).** 각 호출은 도구 없이, 일회용 비공개 디렉터리에서 사용자 지정이 없는 모드로 실행됩니다. 사용자의 `CLAUDE.md`, 플러그인, 훅(hook), MCP 서버, 설정은 로드되지 않으며, 세션에서 아무것도 유지되지 않습니다. 첨부 파일은 차단됩니다. 문서 내의 `@chemin`은 텍스트로만 유지되며 어떤 파일도 열지 않습니다(측정 완료).
- **모델**: 기본값은 `sonnet`이며, 노력 수준(effort)은 `low`, `--eco`에서도 마찬가지입니다. 이 경로에서는 `--eco`가 아무런 영향을 주지 않습니다. 동일한 문서에서 측정한 결과, `haiku`는 강제된 추론으로 인해 2배 더 느리며 비용 절감 효과는 미미하고, `opus`는 생물학 관련 콘텐츠를 거부합니다(다음 항목 참조). 두 모델 모두 `--model`를 통해 접근할 수 있으며, 이 별칭은 해당 패밀리의 최신 모델을 따릅니다. `fable` 및 `[1m]` 변형은 유료 크레딧으로 전환되므로 거부됩니다. `--reasoning_effort`는 노력 수준을 조정하지만, 번역에는 거의 도움이 되지 않으며 측정된 추론량도 거의 전무합니다.
- **Opus는 특정 생물학 콘텐츠를 거부합니다.** 가드레일이 Sonnet보다 엄격하며, Anthropic의 오류 메시지에서도 "can sometimes flag biology-research-adjacent work"(생물학 연구 관련 작업이 감지될 수 있음)라고 경고합니다. 측정 결과: 생성된 279개 분자에 관한 간단한 모니터링 기사 하나로 인해 14개 언어 모두에서 글 전체가 거부되었습니다. 아무것도 작성되지 않습니다. aipmt는 잘린 응답을 거부하고 해당 가드레일을 명시하며 `--model sonnet` 사용을 권장합니다.
- CI 환경(`CI` 또는 `GITHUB_ACTIONS` 정의됨) 및 Windows(측정되지 않음)에서는 거부됩니다.
- 변수: `AIPMT_CLAUDE_BIN`(없는 경우 `PATH`, 그 다음 `~/.local/bin/claude`), `AIPMT_CLAUDE_TIMEOUT`(세그먼트당 초, 기본값 900), `AIPMT_CLAUDE_MAX_UTILIZATION`(기본값 0.8), `CLAUDE_CONFIG_DIR`(Claude Code 계정, 프로젝트의 `.env`에서는 가져오지 않음), 작업 디렉터리는 `XDG_CACHE_HOME/aipmt/claude-code` 아래 위치(기본값 `~/.cache`).

**이용 약관: 사용자 본인의 계정에 책임이 따릅니다.** [Claude Code 법적 안내 페이지](https://code.claude.com/docs/en/legal-and-compliance)에서는 "an end user from signing in to the unmodified Claude Code binary with their own Claude subscription"(최종 사용자가 자신의 Claude 구독을 사용하여 수정되지 않은 Claude Code 바이너리에 로그인하는 것)을 금지하지 않습니다. 공식 바이너리를 실행하고 토큰을 직접 읽지 않는 aipmt의 동작 방식이 바로 이에 해당합니다. 하지만 Anthropic은 "does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users"(서드파티 개발자가 사용자를 대신하여 Free, Pro, Max 플랜 자격 증명을 통해 요청을 라우팅하는 것)을 허용하지 않으며, "including open-source projects"(오픈 소스 프로젝트 포함) 서드파티 도구에 대해서는 API 키 사용을 선호하고, 이러한 사용량을 유료 크레딧에서 차감할 권리를 보유합니다([Claude 고객지원](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)). 바이너리를 로컬에서 실행하는 배포 도구에 대한 명확한 유권해석은 아직 없습니다.

**데이터**: Free, Pro, Max 계정의 경우 개인정보 보호 설정에서 허용된 경우 모델 학습이 Claude Code에도 적용됩니다([데이터 관련 안내 페이지](https://code.claude.com/docs/en/data-usage)). aipmt는 로컬 전사 기록을 전혀 보관하지 않습니다(`--no-session-persistence`). 기밀 내용은 전송하지 마세요.

### 원하는 제공업체로 연결: `--use_opencode`

[OpenCode](https://opencode.ai)는 내부에 구성된 제공업체(API 키, 구독, 계정 없이 무료 모델을 제공하는 OpenCode Zen 게이트웨이 또는 로컬 모델)로 라우팅하는 오픈 소스(MIT) 코드 에이전트입니다. 여기서는 Zen과 Ollama 두 가지 경로를 처음부터 끝까지 측정했습니다.

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

`--model`는 필수입니다. 이 옵션이 없으면 OpenCode가 대화 내용이 학습에 사용될 수 있는 무료 모델로 폴백될 수 있으며, 이러한 선택을 임의로 결정하지 않습니다.

각 호출 시 격리 조치:

- 사용자 설정보다 우선 적용되는 인라인 설정을 통해 모든 도구가 거부된(`permission: { "*": "deny" }`) `aipmt` 에이전트를 정의하며, 세션 공유 비활성화, `--pure` 적용, `--auto`는 절대 사용하지 않습니다.
- 일회용 빈 작업 디렉터리에 `OPENCODE_DISABLE_PROJECT_CONFIG` 및 `OPENCODE_DISABLE_CLAUDE_CODE`를 배치합니다. 그렇지 않으면 OpenCode가 현재 디렉터리의 `AGENTS.md`와 `~/.claude/CLAUDE.md`를 프롬프트에 주입합니다. 전역 `~/.config/opencode/AGENTS.md`는 계속 주입되며, OpenCode에서는 이를 제외할 수 없습니다.
- 출력 조건(출력 계약): 반환 코드 0, `error` 이벤트 없음, 도구 호출 없음, 마지막 단계가 `stop`, 빈 텍스트 아님, `aipmt` 에이전트가 정상 로드됨(알 수 없는 `--agent`가 지정되어도 OpenCode는 실패하지 않고 기본 코딩 에이전트로 조용히 전환됨).
- OpenCode 자체 키인 `OPENCODE_API_KEY`를 제외하고는 어떤 `aipmt` 키도 전송되지 않습니다. 제공업체 설정은 `aipmt`의 `.env`가 아닌 OpenCode 내에서 구성됩니다.

참고 사항:

- Zen의 무료 모델은 유동적이고 문서화되지 않은 제한이 있으며 대화 내용이 학습에 사용될 수 있으므로, 비공개 콘텐츠가 아닌 공개 문서 번역에만 적합합니다.
- 로컬 모델은 세그먼트 길이가 최대 16,000자에 달하므로 최소 16k 토큰의 컨텍스트를 제공해야 합니다. Ollama는 보통 4,096으로 설정되어 있으므로 `PARAMETER num_ctx 32768`를 포함한 `Modelfile`를 사용해야 합니다.
- `--eco`는 효과가 없으며, `--reasoning_effort`는 OpenCode의 `--variant`로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 변수: `OPENCODE_BIN`(없는 경우 `PATH`, 그 다음 `~/.opencode/bin/opencode`), `OPENCODE_TIMEOUT`(세그먼트당 초, 기본값 600). `OPENCODE_CONFIG`는 OpenCode로 그대로 전달됩니다.

Ollama를 통한 로컬 모델 예시(`~/.config/opencode/opencode.json`):

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

`reasoningEffort: "none"`는 이러한 모델에서 Ollama가 기본적으로 활성화하고 Modelfile로는 비활성화할 수 없는 추론(thinking) 과정을 차단합니다. 6개 단어로 된 문장에서 측정한 결과: 옵션이 없을 때는 919 토큰의 추론과 68초가 소요되었으나, 옵션을 사용했을 때는 9 토큰에 불과했습니다.

### 400개 이상의 모델로 연결: `--use_openrouter`

OpenRouter는 단일 크레딧을 통해 사용량 기반으로 요금을 청구하는 라우터로, 서드파티가 호스팅하는 모델(여기서 다른 제공업체는 지원하지 않는 중국의 오픈 모델 포함)을 연결합니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`는 필수입니다. 요금이 청구되기 전에 실행되는 사전 검사(preflight)는 라우팅의 두 가지 특성을 처리합니다:

- **동일한 모델이라도 한도 설정이 제각각인 수십 개의 호스팅 업체에서 제공됩니다.** — 예를 들어 `z-ai/glm-5.3-flash`의 경우 23개 호스팅 업체 중 하나는 출력 토큰 한도가 2,048개에 불과합니다. 사전 검사는 `/api/v1/models/{modèle}/endpoints`를 읽어 출력 토큰이 8,000개 미만이거나 상태가 저하된 호스팅 업체를 제외하고 나머지를 `allow_fallbacks: false`로 고정합니다.
- **추론 토큰은 출력 요율로 청구됩니다.** — `z-ai/glm-5.2`에서 "OK" 응답 하나에 2토큰 대신 107토큰이 소모되기도 합니다. 추론은 기본적으로 비활성화되어 있으며, 추론이 강제되는 모델에는 허용 가능한 가장 낮은 노력 수준이 전달됩니다. 카탈로그 기본값을 그대로 두면 번역이 완료되기 전에 출력이 포화 상태에 이를 수 있기 때문입니다. `--reasoning_effort` 설정이 항상 우선합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 컨텍스트 윈도우 크기는 카탈로그에서 가져옵니다. 16,400 토큰 미만인 모델은 호출 전에 거부됩니다(프롬프트 및 세그먼트용 8,400개, 최소 출력용 8,000개).
- 카탈로그에 없는 슬러그, 카탈로그 접근 불가, 최소 한도를 충족하는 호스팅 업체 부재 시 명령이 중단됩니다.
- 출력이 빈 상태에서 `finish_reason=length`가 발생하는 것은 잘림(truncation)이 아니라 추론에 예산이 소진된 경우이며, 오류 메시지에서 이를 명확히 구분합니다.
- `--eco`는 효과가 없습니다.
- 변수: `OPENROUTER_API_KEY`(<https://openrouter.ai/keys>), `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://` 필요), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30).

### 번역 노트

`--add_translation_note`는 노트를 추가하며, 위치는 `bottom`(기본값), `top`(front matter 뒤) 또는 `both`(`--note_position`)에 배치할 수 있고, 형식은 `legacy`(굵은 글씨 단락, 기본값) 또는 `marker`(`--note_format`)입니다. `marker` 형식은 보이지 않는 마크다운 참조 정의인 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` 뒤에 굵은 글씨 인용문이 이어지는 형태입니다. GitHub에서 읽을 수 있으며 빌드 시 remark 플러그인에서 활용할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정 결과

모든 측정치는 `aipmt`를 사용하여 14개 언어(en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi)로 실제 수행한 번역 결과입니다. **작성됨**은 검증 가드를 통과한 파일 수를 세며, **불일치 없음**은 `scripts/compare_structure.py`가 아무런 차이점도 발견하지 않은 파일 수를 의미합니다. 즉, 섹션, 소제목, 링크, 고유 URL, 코드 블록, 인라인 코드, 표 행, 인용 블록, 굵은 글씨 단어의 수가 동일함을 뜻합니다.

"불일치 없음"은 "완전히 동일함"이 아니라 "감지된 차이가 없음"을 의미합니다. 비교 도구는 내용을 읽지 않고 요소의 개수만 세기 때문입니다. 레벨 4 제목의 삭제, 대체된 인라인 코드 텍스트, 바뀐 플래그, 괄호가 하나 더 들어가 어디로도 연결되지 않는 내부 링크(`[texte]((#ancre))`) 등을 감지하지 않으며, 언어의 품질을 평가하지도 않습니다.

### 고밀도 모니터링 기사, `--news` 모드

[jls42.org AI 모니터링](https://jls42.org/fr/news) 한 편: 589행, 140개 링크, 21개 섹션, 보호된 영어 인용문 3개. 2026년 9월 4일~5일 테스트.

| 모델 | 접근 방식 | 작성됨 | 불일치 없음 | 중앙값/언어 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1분 18초 |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 구독 | 14/14 | ✅ **14/14** | 3분 59초 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 구독 | 14/14 | ✅ **14/14** | 3분 14초 |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT 구독 | 14/14 | ✅ **14/14** | 11분 28초 |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5분 37초 |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26분 23초 |
| `sonnet` (`--use_claude_code`) | Claude 구독 | 14/14 | ⚠️ 13/14 | 6분 49초 |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6분 31초 |
| `haiku` (`--use_claude_code`) | Claude 구독 | 14/14 | ⚠️ 11/14 | 15분 54초 |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9분 27초 |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10분 09초 |
| `ollama/gpt-oss-20b-32k` | 로컬 | 10/14 | ❌ 7/14 | 12분 39초 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5분 32초 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37분 27초 |
| `grok-4.6` (`--use_grok_cli`) | Grok 구독 | 1/14 | ❌ 1/14 | 23분 11초 |
| `opus` (`--use_claude_code`) | Claude 구독 | 0/14 | ❌ 0/14 | — |

Grok은 9월 9일 동일한 모니터링의 다른 회차(356행)에서 다시 측정되었습니다: 14개 중 9개 언어 작성됨, 8개 불일치 없음. 상단 표에 표시된 수치가 바로 이 결과입니다. 중단된 세 차례의 테스트는 기록되지 않았습니다: 크레딧 부족으로 중단된 `qwen3.5-27b`(9개 언어) 및 `kimi-k2.6`(4개), 그리고 두 건의 실패가 추론 설정 때문이었으며 이후 제공업체가 수정한 `z-ai/glm-5.3-flash`입니다. OpenRouter 행은 `--use_openrouter` 이전 라우터의 기본 설정으로 측정되었습니다. 제공된 프로바이더로 재측정한 `z-ai/glm-5.2` 역시 동일하게 14/14를 기록했습니다. 수치는 9월 10일 현재의 비교 도구로 재계산되었습니다: 최초 공개 대비 `qwen3.8-flash`와 `qwen3.7-flash`가 각각 1개 언어를 추가로 통과했으며, 나머지는 변동이 없습니다.

`--use_antigravity` 행은 9월 26일 동일한 기사에서 4개의 병렬 번역으로 측정되었습니다: 오전에 `gemini-3.7-flash-medium`, 오후에 `gemini-3.8-flash-medium`. 영어 번역 시 각 모델은 플래그를 임의로 추가하지 않고 인용문 아래의 세 줄짜리 프랑스어 번역을 스스로 제거했으며 영어 인용문도 온전하게 유지되어 폴백 정리가 필요하지 않았습니다. `--eco`(`gemini-3.7-flash-low`)에서는 4개 언어(en, ja, ar, hi)만 테스트하여 4개 모두 작성됨, 전 언어 불일치 없음, 중앙값 1분 52초를 기록했습니다. 같은 날 9월 25일자 최신 모니터링 기사(438행, 2개 영어 인용문)를 블로그 외부에서 `gemini-3.7-flash-medium`로 번역하여 교차 검증을 진행했습니다: 14개 모두 작성됨, 전 언어 불일치 없음, 언어당 87~128초가 소요되었습니다.

`--use_claude_code` 행은 9월 26일 동일한 기사에서 노력 수준 `low`로 4개의 병렬 번역을 진행하여 측정했습니다. `sonnet`의 경우 14개 언어 모두에서 영어 인용문이 온전하게 유지되었으며, 영어 번역에서 모델이 플래그를 지어내지 않고 프랑스어 번역 줄을 직접 삭제했습니다. `opus`는 단 하나의 언어도 작성하지 못했습니다: 결합 부위를 위해 생성된 279개 분자에 관한 단신 기사 때문에 모든 언어의 마지막 세그먼트에서 가드레일이 응답을 중단시켰습니다. 이 단신만 따로 전송해도 "bio" 범주로 분류되어 거부되지만, `sonnet`는 모든 언어에서 정상 번역했습니다. `haiku`는 14개 언어를 모두 작성했으나, 3개 언어(en, pl, ro)에서 섹션 제목 레벨이 2에서 1로 변경되었습니다. 또한 강제 추론이 적용되어 출력 토큰의 61%를 차지함에 따라 `sonnet`에 비해 2배 이상의 시간이 소요되었습니다.

### 이 프로젝트의 README, 표준 Markdown

2026년 9월 9일 고정 리비전: 785행, 인라인 코드 285개, 블록 닫기 40개, 표 89행. 병렬 번역 4회.

| 모델                                            | 작성됨 | 불일치 없음 | 언어당 중앙값 | 차이점                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1분 43초     | 없음                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1분 48초     | 없음                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4분 02초     | 비교기 기준 없음; 내부 링크 중복됨 (en)                   |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36초           | 굵은 글씨 단어 1개 (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1분 22초     | 굵은 글씨 단어 1개 (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2분 20초     | 이전 행에 붙은 표 행 1개 (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2분 56초     | 링크 1개 (sv), 굵은 글씨 단어 1개 (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6분 46초     | 굵은 글씨 단어 1개 (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2분 34초     | 굵은 글씨 단어 1개 (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2분 17초     | 아랍어에서 인라인 코드 40개 추가됨; 굵은 글씨 (hi, ja, ko)                   |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2분 44초     | 누락된 섹션 1개 (ar, hi, ko); 코드 블록 추가됨 (ja, ko, ro, zh) |

중단된 두 테스트는 기록되지 않았습니다: 12개 언어(11개 언어 불일치 없음) 진행 후 CLI 세션이 만료된 Grok, 2개 언어 진행 후 호스팅 업체로부터 HTTP 429 오류를 반환받은 `qwen3.8-flash`. `opencode/mimo-v2.5-free` 및 `ollama/gpt-oss-20b-32k`은 이번 리비전에서 재측정되지 않았습니다. 277행 더 짧았던 9월 4일과 5일 리비전에서는 각각 14개 중 9개의 번역을 작성했으며, 불일치가 없었던 것은 각각 7개와 1개였습니다.

`--use_antigravity` 및 `--use_claude_code` 행은 고정 리비전에서 측정되지 않고, 9월 26일 1.14.0과 함께 게시된 리비전(600행, 인라인 코드 257개, 블록 닫기 30개, 표 85행)에서 측정되었습니다. 185행 더 짧기 때문에 다른 행들과 일대일로 비교할 수는 없지만, 이들 행끼리는 상호 비교가 가능합니다. 비교기가 검사하지 않는 내부 링크의 경우, `gemini-3.8-flash-medium`은 14개 언어 모두에서 온전하게 유지했고, `gemini-3.7-flash-medium`은 이탈리아어에서 깨뜨렸습니다. `sonnet` 및 `opus`은 모든 언어에서 온전하게 유지한 반면, `haiku`은 영어에서 중복 생성했습니다.

### 잘 알려진 프로젝트의 4개 README

GitHub에서 그대로 가져온 FastAPI, Ollama, tldr-pages 및 Vue.js — 이전 두 문서보다 수월한 문서들입니다. 이 테스트는 처리 성능이 다소 떨어지는 모델들을 대상으로 진행되었으며, Gemini가 비교 기준으로 사용되었습니다.

| 모델                    | 범위                  | 작성됨 | 불일치 없음   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4개 프로젝트 × 14개 언어     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4개 프로젝트 × 14개 언어     | 55/56   | ❌ 47/56     |
| `grok-4.6` (구독)   | 4개 프로젝트 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4개 프로젝트 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 이 측정 결과가 의미하지 않는 것

- **완전한 순위가 아님**: OpenRouter 하나만 해도 400개 이상의 모델을 제공하며, 여기서는 약 15개 모델만 측정되었습니다.
- **참고용 소요 시간**: 테스트에 따라 3개에서 6개의 번역을 병렬로 진행했으며, 제공업체의 처리량은 하루 중에도 달라집니다.
- **특정 시점의 관찰 결과**: 모델은 같은 이름 아래에서도 변경되며, 사용자의 문서는 테스트 문서와 다릅니다.

파일의 고정 사본을 사용하여 보유한 문서에서 측정을 재현하려면:

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

두 줄 모두 필요합니다: `pip install -e .`이 없으면 `python -m aipmt`은 `No module named aipmt`을 반환합니다.

선택 사항이지만 권장되는 품질 도구:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 28개 번역(README 및 CHANGELOG, 14개 언어)은 `./regen_translations.sh --force`으로 다시 생성됩니다. 기본적으로 ChatGPT 구독을 사용하는 Codex와 `gpt-5.6-sol`을 통해 4개 작업을 병렬로 실행합니다. `REGEN_PROVIDER` 및 `REGEN_MODEL`은 경로를 변경합니다. `antigravity`은 Google 구독을 유지하며 예외 없이 통과하고, 유료 API(`openai`, `gemini`, `grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다. `REGEN_JOB_TIMEOUT`은 각 작업의 제한 시간을 설정합니다(기본 600초, Codex 및 Antigravity에서는 1,800초). 도구에 대한 자세한 내용은 `CLAUDE.md`에 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 발행되는 개인 블로그입니다. 이곳의 [일일 AI 모니터링](https://jls42.org/fr/news)은 매일 이 도구로 번역되며, 위 측정의 참조 문서로 사용됩니다.

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

## 면책 조항

이 프로그램은 GPL v3 제15조 및 제16조의 조건에 따라 **어떠한 보증도 없이** 배포됩니다. 상품성 또는 특정 목적에의 적합성에 대한 묵시적 보증을 포함하여 일체의 보증 없이 "있는 그대로" 제공되며, 작성자는 프로그램 사용으로 인해 발생하는 손해에 대해 책임을 지지 않습니다. 이 요약본보다 라이선스 본문이 우선합니다.

- **게시하기 전에 다시 검토하세요.** 보호 장치는 코드 블록, 인라인 코드, URL, 앵커 및 `--news` 모드의 인용문에 적용되며, 제목, 표, 프론트 매터 또는 문장의 의미는 보호하지 않습니다.
- **문서는 선택한 제공업체로 전송되며**, 해당 제공업체의 이용 약관 및 데이터 정책이 적용됩니다. 일부 무료 모델은 대화 내용을 학습에 재사용할 수 있으며, Antigravity 약관에 따르면 유료 구독을 포함하여 Google이 데이터를 재사용하고 사람이 검토하도록 허용할 수 있습니다. 로컬 모델만이 머신 외부로 데이터를 전혀 유출하지 않는 유일한 방법입니다.
- **API 호출 비용은 사용자에게 청구됩니다.** 이 프로그램은 지출 한도를 제한하지 않으므로 문서가 길거나 실패 후 재시도하거나 추론을 많이 수행하는 모델일수록 더 많은 비용이 발생합니다.
- **게시된 측정 결과는 특정 시점의 관찰 결과일 뿐**, 보증이 아닙니다.

언급된 제품 및 회사 이름은 해당 소유자의 자산입니다. 이 프로젝트는 그중 어느 곳과도 제휴 관계가 없습니다.

**gemini-3.8-flash-medium으로 프랑스어에서 한국어로 번역된 기사.**
