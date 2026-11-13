# 인공지능 기반 Markdown 번역기

🌍 [프랑스어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [영어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [스페인어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [중국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [독일어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [일본어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [아랍어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [힌디어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [이탈리아어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [네덜란드어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [폴란드어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [포르투갈어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [루마니아어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [스웨덴어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 코드 품질</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="품질 게이트 상태"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="보안 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="신뢰성 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="유지보수성 등급"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="코드 커버리지"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="취약점"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="버그"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 악취"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복 줄 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 줄 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdown 파일을 한 언어에서 다른 언어로 번역하면서
코드 블록, 인라인 코드, URL, 앵커, 표, 프런트 매터의
구조를 보존합니다. 모델을 호출하는 방법은 열한 가지입니다.
API 다섯 가지, 사용량에 따른 과금이 없는 구독 네 가지,
라우터 두 가지를 지원하며, 각 모델이 실제로 무엇을 보존하는지 측정한 결과를 공개합니다.

## 핵심 요약

- **열한 가지 제공업체 접근 경로**: OpenAI, Mistral, Claude, Gemini, Grok API;
  사용량에 따른 과금이 없는 ChatGPT (Codex), Grok, Google (Antigravity), Claude (Claude
  Code) 구독; OpenCode 라우터(오픈 소스, 무료 또는 로컬)와 OpenRouter 라우터
  (400개 이상의 모델).
- **토큰 하나가 사라져도 손상된 결과를 저장하지 않음**: 코드 블록, 인라인 코드,
  URL, 앵커, 인용문을 호출 전에 토큰으로 대체하고
  응답을 받은 뒤 확인합니다. 하나라도 빠지면 파일을 저장하지 않습니다.
- **긴 문서**: 모델의 컨텍스트 창에 맞춰 분할합니다.
- **`--news` 모드**: 동향 분석 기사를 위해 영어 인용문을 보호하고
  언어별로 플래그를 처리합니다.
- **`--eco` 모드**: 빠르고 저렴한 모델을 사용합니다.
- **번역 안내문**을 선택적으로 문서 위, 아래 또는 양쪽에 넣을 수 있습니다.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 이상이 필요합니다. 저장소에서 설치하려면
[기여하기](#기여하기)를 참조하세요.

## 설정

키는 다음 세 곳에서 우선순위 순으로 읽습니다. 각 위치에서는
앞선 위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일회성 재정의 |
| 2   | 현재 디렉터리 또는 상위 디렉터리의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | 한 번 설정하여 모든 곳에서 사용       |

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

`GOOGLE_API_KEY` 대신 `GEMINI_API_KEY`도 사용할 수 있습니다. 사용자
파일은 `XDG_CONFIG_HOME`(절대 경로만 허용)과 Windows의 `%APPDATA%`을
따릅니다. 키가 없으면 명령어가 세 위치를 나열합니다.

**프로젝트의 `.env`에서는 호출을 다른 곳으로 보내거나 실행할 프로그램을
선택할 수 없습니다.** 이 파일은 키만 제공하며 대상 주소나 실행 파일은 지정하지 않습니다.
`_BASE_URL`, `_API_BASE`, `_ENDPOINT`, `_BIN` 계열의 모든 변수(`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, 프록시(`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), 인증서 저장소(`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), `XDG_CONFIG_HOME` /
`APPDATA`은 이 파일에서 무시되며 경고가 표시됩니다. 복제한 저장소가
키를 가로채거나 첫 번역에서 자체 프로그램을
실행하게 해서는 안 됩니다. 이 파일은 변수 보간 없이 읽습니다.
따라서 `NOM=${OPENAI_API_KEY}`은 키를 복사하지 않습니다. 이러한 변수는
환경 변수나 `~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT`(호출당 초 단위, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(기본값 600), `GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`), `GROK_TIMEOUT`
(기본값 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT`(기본값 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT`(기본값 600), `OPENROUTER_BASE_URL`
(`https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900),
`OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각 변수의 자세한 설명은
해당 제공업체 절에 있습니다.

## 시작하기

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`을 스페인어로 번역하면 `--target_dir`에 `document-es.md`이 생성됩니다.
`--include_model`을 사용하면 `document-es-gpt-5.6-terra.md`이 생성됩니다. 확장자는
항상 `.md`가 됩니다. 예를 들어 `article.mdx`은 `article-en.md`이 됩니다.
단, `--keep_filename`를 사용하면 원래 이름을 유지합니다. 이미 존재하는 번역은
`--force` 없이는 건너뜁니다.

종료 코드: 모두 성공했거나 건너뛰었으면 `0`, 실패한 파일이 남아 있으면
`1`(표준 오류에 목록 출력), 설정에 문제가 있으면 `2`입니다.
실패한 파일은 저장하지 않습니다. 저장 자체가 실패하는 경우도 마찬가지입니다.
내용을 옆의 임시 파일에 쓴 뒤 이름을 바꾸므로, 다시 실행하면 됩니다.

## 어떤 모델을 선택할까

실제 문서 두 개를 각 모델로 동일한 열네 개 언어로 번역하여
측정했습니다. **숫자는 열네 개 언어 중 번역 파일이 저장되었고
원문과 차이가 없었던 언어의 수입니다.**

| 모델                | 접근 방법                 | 정보 밀도가 높은 동향 분석 기사 | 이 README    | 차이점과 해당 언어 수                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google 구독 (Antigravity)   | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 차이 없음                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API 키                 | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 차이 없음                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API 키                    | ✅ 14/14                | ⚠️ 13/14     | 14개 중 1개 언어: 굵게 표시된 단어 하나 추가 (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google 구독 (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 14개 중 1개 언어: 단어 하나의 굵은 표시 누락 (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT 구독 또는 OpenAI 키 | ✅ 14/14                | ⚠️ 12/14     | 14개 중 2개 언어: 단어 하나의 굵은 표시 누락 (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter 키                    | ✅ 14/14                | ⚠️ 11/14     | 14개 중 3개 언어: 단어 하나의 굵은 표시 누락 (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude 구독 (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 기사에서 14개 중 1개 언어: 굵게 표시된 단어 하나 추가 (zh); 이 README에서 1개 언어: 표의 한 행이 앞 행에 붙어 화면에 표시되지 않음 (ar)            |
| Claude Haiku 4.5      | Claude 구독 (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 기사에서 3개 언어: 절 제목 하나가 1단계로 변경됨 (en, pl, ro); 이 README에서는 비교 도구가 차이를 찾지 못했지만 내부 링크가 영어로 중복됨 |
| Claude Sonnet 5       | Anthropic API 키                 | ⚠️ 11/14                | ⚠️ 12/14     | 기사에서 3개 언어: 코드 블록 하나 추가 (es, de, hi); 이 README에서 2개 언어: 링크 마크업 누락 (sv), 단어 하나의 굵은 표시 변경 (zh)                              |
| Claude Haiku 4.5      | Anthropic API 키                 | ⚠️ 7/14                 | ✅ 14/14     | 기사에서 7개 언어: 절 제목 하나가 1단계로 변경됨 — 일본어에서는 프랑스어로 남음; 이 README에서는 차이 없음                                              |
| Claude Haiku 5.5      | Anthropic API 키                 | ⚠️ 11/14                | ❌ 12/14     | 기사에서 3개 언어: 절 제목 하나의 단계가 변경되거나 중복됨 (ja, ko, zh); 이 README에서 2개 언어 거부, 인라인 코드 누락 (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter 키                    | ❌ 8/14                 | ⚠️ 10/14     | 기사에서 1개 언어 거부, 다른 5개 언어에서 차이 발생; 이 README에서는 약 40개 단어가 `code`으로 표시됨 (ar)                                                    |
| Grok 4.6              | Grok 구독                   | ❌ 8/14                 | 평가하지 않음     | 인라인 코드와 URL을 반환하지 않아 14개 중 5개 언어 거부; 네덜란드어는 모든 항목에서 차이 발생                                                               |
| GPT-OSS 20B           | 로컬 모델 (Ollama)             | ❌ 7/14                 | 재측정하지 않음 | 14개 중 4개 언어 거부: 모델이 일부 구절을 프랑스어로 남겨 검증 장치가 차단함                                                                  |
| MiMo v2.5 (무료)   | OpenCode Zen, 계정 불필요         | ❌ 11/14                | 재측정하지 않음 | 1개 언어 거부; 폴란드어에서 절 하나 누락                                                                                                                  |
| Mistral Large         | Mistral API 키                   | ❌ 5/14                 | ❌ 1/14      | **절 전체가 사라짐**: 기사에서 1개 언어 (hi), 이 README에서 3개 언어 (ar, hi, ko) — 기사에서는 3개 언어 거부도 발생                                |
| DeepSeek V4 Flash     | OpenRouter 키                    | ❌ 3/14                 | 재측정하지 않음 | 14개 중 10개 언어 거부; 언어당 37분                                                                                                                 |
| Claude Opus 5.5       | Claude 구독 (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | 생물학 단신 때문에 Opus의 안전장치가 기사 번역을 14개 언어 모두에서 거부; 이 README에서는 차이 없음                                               |

|     | 기호의 의미                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 열네 개 언어 모두 번역되었으며 원문과 차이 없음                                                                                                                                       |
| ⚠️  | 열네 개 언어 모두 번역됨; 차이는 **마크업**에 있음 — 단어 하나의 굵은 표시, `code` 하나, 대괄호가 사라진 링크 등. 텍스트, URL, 코드 블록, 절은 누락되지 않음 |
| ❌  | 적어도 한 언어를 번역하지 못함 — 파일이 거부되어 저장되지 않음 — **또는** 저장된 파일에서 내용이 누락됨                                                                      |

여기서 알 수 있는 점:

- **거부된 번역은 손상된 번역이 아닙니다.** 응답에 토큰이
  빠져 있으면 파일을 저장하지 않고 해당 언어를
  거부된 것으로 집계합니다. 기사 번역에서 Grok에 이런 일이 발생했습니다.
  비라틴 문자 체계를 사용하는 다섯 언어에서 첫 구간부터 인라인 코드 네 개와
  URL 세 개가 사라졌습니다.
- **모델은 문장 하나 때문에 문서 전체를 거부할 수 있습니다.** Opus 5.5는
  이 README를 차이 없이 번역하지만 동향 분석 기사는 하나도 번역하지 못합니다.
  생물학 단신에서 안전장치가 응답을 중단하기 때문입니다. 파일은
  저장되지 않으며 aipmt가 이유를 알려 줍니다.
- **이 보호 장치는 제목, 표, 프런트 매터,
  텍스트까지 보호하지는 않습니다.** 모델이 절 하나를 삭제해도 도구는
  그 파일을 그대로 저장합니다. Mistral이 그런 경우입니다. 이러한 요소는
  토큰으로 대체할 수 없으며 현재 검증 장치는 이를 검사하지 않습니다.
  `scripts/compare_structure.py`은 누락된 절을 감지하지만 사후에만 가능합니다.
- **이 README에 대한 Grok의 평가는 없습니다**: 열두 개 언어를 처리한 뒤
  CLI 세션이 만료되었으며, 그중 열한 개 언어에서는 차이가 없었습니다.
  중단된 측정에는 점수를 매기지 않습니다.
- **언어보다 문서의 정보 밀도가 더 중요합니다.** Grok은 일반적인
  README에서는 잘 작동하지만 링크가 많은 기사에서는 제대로 처리하지 못합니다.
  네덜란드어에서도 마찬가지입니다.

날짜와 문서: « 이 README » 열은 2026년 9월 9일에
이 파일의 고정된 개정본(785줄, 인라인 코드 285개, 표 89행)으로
측정했으며, 이후 문서가 수정되었습니다. 다만 Antigravity와 Claude Code 행은
9월 26일에 1.14.0과 함께 공개된 더 짧은 개정본
(600줄, 인라인 코드 257개, 표 85행)으로 측정했고, API를 사용한 Claude
Sonnet 5.5, Haiku 5.5, Haiku 4.5 행은 10월 18일에
같은 개정본으로 측정했습니다. « 정보 밀도가 높은 동향 분석 기사 » 열은
9월 4일과 5일에 589줄짜리 기사로 진행한 측정 결과입니다. 다만 Grok 행은
9월 9일에 같은 동향 분석 기사의 다른 호로 재측정했고, Antigravity와
Claude Code 행은 9월 26일에 같은 기사로 측정했으며, 앞서 언급한 Claude 세 행은
10월 18일에 측정했습니다. 전체 표, 소요 시간, 측정 절차는
[상세 측정 결과](#상세-측정-결과)에 있습니다.
## 모든 옵션

| 옵션                   | 설명                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일 (`--source_dir` 대신 사용)                                             |
| `--source_dir`           | Markdown 파일이 있는 원본 디렉터리 (기본값: `content/posts`)                                   |
| `--target_dir`           | 번역된 파일을 저장할 출력 디렉터리 (기본값: `traductions_en`)                                    |
| `--source_lang`          | 원본 언어 (기본값: `fr`)                                                                                  |
| `--target_lang`          | 대상 언어 (기본값: `en`)                                                                                   |
| `--model`                | 사용할 특정 모델                                                                                  |
| `--eco`                  | 저비용 모델 사용                                                                              |
| `--use_mistral`          | Mistral AI API 사용                                                                                     |
| `--use_claude`           | Claude API 사용                                                                                         |
| `--use_gemini`           | Gemini API 사용                                                                                         |
| `--use_grok`             | xAI (Grok) API 사용 — `XAI_API_KEY` 필요                                                           |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용                                                    |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                                                        |
| `--use_antigravity`      | Google AI Pro 또는 Ultra 구독 할당량으로 Antigravity CLI (`agy`) 사용                       |
| `--use_claude_code`      | Claude Pro 또는 Max 구독 할당량으로 Claude Code CLI (`claude -p`) 사용                      |
| `--use_opencode`         | OpenCode에 설정된 공급자에 연결하여 OpenCode (오픈 소스) 사용; `--model provider/modèle` 필수 |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                          |
| `--force`                | 강제로 다시 번역                                                                                       |
| `--keep_filename`        | 원래 파일 이름 유지                                                                          |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 플래그 처리                                      |
| `--add_translation_note` | 번역 안내문 추가                                                                                |
| `--note_position`        | 안내문 위치: `top`, `bottom` (기본값), 또는 `both`                                                     |
| `--note_format`          | 안내문 형식: `legacy` (기본값, 굵은 글씨 문단) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 강도: `none`/`low`/`medium`/`high`/`xhigh`                                         |

아홉 개의 `--use_*` 플래그는 서로 배타적입니다. 두 개를 함께 사용하면
거부됩니다.

## 공급자

### API 사용: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`은 각 공급자의 저비용 등급으로 전환합니다.

| 공급자    | 고품질 (기본값)                                                     | 저비용 (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (`--model`를 통해 `gpt-5.6-sol`, `terra`, `luna`도 사용 가능) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | 동일 — `--eco` 효과 없음 |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, 추론 강도 `low`                                               | 동일 — `--eco` 효과 없음 |
| OpenCode    | `--model provider/modèle` 필수                                | 동일 — `--eco` 효과 없음 |
| OpenRouter  | `--model fournisseur/modèle` 필수                             | 동일 — `--eco` 효과 없음 |

### ChatGPT 구독 사용: `--use_codex`

공식 Codex CLI를 실행합니다. API 키나 사용량 기반 과금 없이
번역 사용량이 ChatGPT 구독 할당량에서 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 실행 파일은 `CODEX_BIN`, `PATH`, `openai-codex-cli-bin` 패키지 순서로
  찾습니다. `~/.codex/auth.json`은 절대 읽지 않습니다.
- 하위 프로세스 환경에서 `OPENAI_API_KEY`와 `CODEX_API_KEY`를
  제거합니다. 키가 있어도 API로 전환되지 않습니다.
- 각 구간은 5시간 사용 한도의 « 메시지 »를 최소 한 개 소비하며, 검증에
  실패해 재시도하면 두 개를 소비합니다. OpenAI가 제시한 추정치는
  Plus 요금제에서 `gpt-5.6-luna` (`--eco`)의 경우 5시간당 250-2 000개,
  `gpt-5.6-sol`의 경우 10-100개 메시지입니다.
- 1.16.3까지 기본값이었던 `--model gpt-5.6-sol`, `--model gpt-5.6-terra`,
  `--model gpt-5.6-luna`도 구독을 통해 사용합니다.
- 서버에서 429 오류가 발생해도 파일이 유실되지 않습니다. Codex는 자동으로 재연결하고,
  aipmt는 해당 차례가 끝날 때까지 기다립니다. 끝내 429 오류가 해결되지 않으면
  30초, 그다음 60초 후에 구간을 재시도합니다. 계정에 사용 권한이 없는 모델은
  400 오류와 함께 « ChatGPT 계정으로 Codex를 사용할 때는 지원되지 않는 모델입니다 »라는 메시지를 반환합니다.
- API보다 느리며 문서가 길어질수록 차이가 커집니다. 이 README에서는
  `gpt-5.6-sol`의 언어당 중앙값이 6분 46초인 반면,
  `gemini-3.7-flash`은 36초입니다.
- CI에서는 거부됩니다 (`CI` 또는 `GITHUB_ACTIONS`가 설정된 경우). 구독 인증에는
  개인 세션 파일을 사용하므로 공유 실행기에 두어서는
  안 됩니다.
- 변수: `CODEX_BIN`, `CODEX_TIMEOUT` (구간당 초, 기본값 600).

### Grok 구독 사용: `--use_grok_cli`

공식 Grok Build CLI를 통해 SuperGrok 또는 X Premium+ 구독을 사용하는
동일한 방식입니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Codex보다 격리가 약합니다.** Grok의 운영체제 샌드박스는
  많은 최신 Linux 환경에서 적용되지 않으며 (AppArmor, 컨테이너 런타임
  소켓), 적용할 수 없는 프로필은 아무 알림 없이 격리되지 않은 상태로
  시작됩니다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않고, 이를 알린 뒤
  포괄 규칙인 `*`을 포함한 CLI의 `--deny` 규칙에 의존합니다. 이 규칙은
  알리지 않고 보호를 해제하는 대신 시작을 거부하는 유일한
  계층입니다. `GROK_TRANSLATE_SANDBOX=read-only`은 운영체제 샌드박스를 필수로 요구하며, 해당 컴퓨터에서
  적용할 수 없으면 시작에 실패합니다.
- 할당량은 주간 단위이며 Chat, Imagine, Voice와 공유됩니다. 이를
  조회할 수 있는 명령은 없으므로, 일괄 작업이 아무 알림 없이 대화용
  사용량을 소모할 수 있습니다.
- 변수: `GROK_BIN`, `GROK_HOME` (CLI 디렉터리, 기본값 `~/.grok`),
  `GROK_TIMEOUT` (기본값 900), `GROK_TRANSLATE_SANDBOX`.

### Google 구독 사용: `--use_antigravity`

Antigravity의 공식 CLI인 `agy`을 사용하는 동일한 방식입니다. Google
AI Pro 또는 Ultra 유료 구독자는 토큰 단위 과금 대신
구독 할당량에서 번역 사용량이 차감됩니다. 이 할당량을 사용하는 유일한 경로입니다. Gemini CLI는
2026년 6월 18일부터 이 계정들을 더 이상 지원하지 않으며
([공지](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
Antigravity SDK는 API 키 또는 Google Cloud 프로젝트만 허용합니다.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **유료 과금 경로를 모두 차단합니다.** agy에 전달되는 환경 변수는
  `PATH`, 언어 및 시간대, 터미널, 사용자 정보, 프록시 및 인증서, 세션 버스 등
  정해진 목록으로 제한되며, 키는 전달되지 않습니다.
  agy의 여러 변수는 아무 표시 없이 호출 경로를 바꿉니다. 실제 측정에서
  한 변수는 문서를 외부 게이트웨이로, 다른 변수는 과금되는 Google Cloud
  프로젝트로 전송했습니다. 차단 목록 방식은 검토할 때마다 빠진 변수가 발견되었습니다.
  각 구간을 처리하기 전에 할당량을 소모하지 않는 `agy -p /config`을 통해
  유료 AI 크레딧이 비활성화되어 있고 API 키와 Google Cloud 프로젝트가 없는지 확인해야 합니다.
  설정이 없으면 거부하며, 조건을 충족하지 않으면 아무것도 번역하지 않습니다. 이후 각
  호출 로그에서도 구독 사용 (`authMethod=consumer`)이 확인되어야 하며, 그렇지 않으면
  응답을 거부합니다.
- **격리.** 각 호출은 도구가 없는 번역 에이전트와 함께
  비공개 일회용 개인 디렉터리에서 실행됩니다. 사용자의 agy 설정, 규칙,
  플러그인, MCP 서버, 훅은 반영되지 않고, 기록에도 아무것도 추가되지
  않습니다. 로그인 정보는 키링에 남으며 aipmt는 이를 절대 읽지 않습니다.
  지정한 에이전트를 찾지 못하면 agy는 아무 알림 없이 코딩 에이전트와
  그 도구로 전환합니다. 올바른 에이전트임을 로그 한 줄 전체가 확인해 주어야 하며,
  문서에 해당 메시지가 인용되어 있는 것으로는 대체할 수 없습니다. 확인되지 않으면 거부합니다.
- **플랫폼**: 키링이 있는 세션의 Linux (D-Bus 세션 버스,
  Secret Service). macOS도 허용하지만 측정한 적은 없습니다. Windows에서는
  agy가 호출별 격리에 사용하는 변수를 읽지 않으므로 거부됩니다.
  세션 버스가 없는 Linux 환경인 SSH 세션, 컨테이너, 서버에서도 거부됩니다. 이런 환경에서는
  agy가 `~/.gemini`의 파일에 토큰을 저장하는데, 격리로 인해 이 파일이 가려집니다.
  거부 사유는 실행 전에 표시되므로 로그인 코드를
  1분 동안 기다릴 필요가 없습니다.
- **모델**: `agy models`에 있는 모델입니다. Gemini는 이름에 추론 강도가 포함됩니다
  (`gemini-3.8-flash-medium` 등). 접미사가 없는 이름은 호출 전에 거부되며,
  `--reasoning_effort`은 효과가 없습니다. 기본값은 `gemini-3.8-flash-medium`이고,
  `--eco`에서는 `gemini-3.7-flash-low`입니다. 이 값을 결정한 측정 작업은
  [상세 측정](#상세-측정-결과)에 설명되어 있습니다. Claude와 GPT-OSS는
  별도의 훨씬 작은 할당량을 사용합니다. 측정된 호출당 5시간
  사용 한도의 약 1 %를 소비하며, Flash는 0,05 %입니다.
- **할당량**: 그룹별로 5시간 한도와 주간 한도가 있으며,
  토큰 비용에 비례하여 차감됩니다. 작성자 계정에서 측정한 결과, 원문 100만 자당
  5시간 사용 한도의 약 16퍼센트포인트를 `gemini-3.8-flash-medium`에서,
  14퍼센트포인트를 `gemini-3.7-flash-medium`에서, 7~8퍼센트포인트를
  낮은 추론 강도에서 소비했습니다. 따라서 40 000자 README는
  0.5퍼센트포인트를 조금 넘게 소비합니다. 주간 한도는 등급에 따라 달라집니다. 재시도는
  agy가 재시도 가능하다고 표시한 경우에 따릅니다. 그런 표시가 없다면 소진된 한도에 대해서는
  재시도하지 않습니다. `/usage`에 표시된 초기화 시점까지
  각 파일 처리가 실패합니다.
- **API보다 느림**: 내용이 밀도 높은 측정용 문서에서 언어당
  중앙값은 `gemini-3.8-flash-medium`에서 3분 59초,
  `gemini-3.7-flash-medium`에서 3분 14초였습니다. 반면 API를 통한 Gemini 3.7 Flash는 1분 18초였습니다.
- **중단**: Ctrl-C를 누르거나 터미널을 닫으면 agy도 명령과 함께
  종료되므로, 현재 차례를 끝내느라 할당량을 계속 소비하지 않습니다.
  Codex, Grok CLI, OpenCode도 동일합니다. `nohup`에서는 번역이 계속됩니다.
- CI에서는 거부됩니다 (`CI` 또는 `GITHUB_ACTIONS`가 설정된 경우). 로그인 정보는
  개인 키링에 저장됩니다. 실행기에서는 `--use_gemini`과 `GOOGLE_API_KEY`을 사용하세요.
- 변수: `AGY_BIN` (없으면 `PATH`, 그다음 `~/.local/bin/agy`),
  `AGY_TIMEOUT` (시작 시간을 포함한 구간당 초, 기본값 900).

**이용 약관: 책임은 본인 계정에 따릅니다.**
[Antigravity 약관](https://antigravity.google/terms) (제6조)과
[자주 묻는 질문](https://antigravity.google/docs/faq/)은 Antigravity 로그인 정보를 이용해
타사 소프트웨어로 서비스에 접근하는 것을 금지하며, 위반 시 계정이 정지될 수 있습니다.
여기에는 Claude Code, OpenClaw, OpenCode가 명시되어 있습니다. aipmt는
토큰을 읽거나 재사용하지 않습니다. Google이 스크립트와 CI용으로
문서화한 [헤드리스 모드](https://antigravity.google/docs/cli/headless/)에서
공식 실행 파일을 실행합니다. Google 관계자는 자신의 작업을 위해 로컬 스크립트에서
`agy -p`을 실행하는 것을 « 일반적 »이라고 평가했습니다
([공식 포럼, 2026년 9월 25일, 계약상 효력이 없는 답변](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)).
이 도구처럼 배포되는 도구의 경우를 명확히 판단한 문서는 없습니다.

**공개 문서만 사용하세요.** 같은 약관 제5조에 따르면
프롬프트, 응답, 메타데이터 등의 상호작용은 유료 구독에서도
Google의 제품 및 기계 학습 개선에 사용되거나
사람이 검토할 수 있습니다. 이를 거부하려면
`enableTelemetry` 설정을 사용해야 하지만 그 효과는 문서화되어 있지 않으며, aipmt는 이 설정을 적용하지 않습니다.
사용자의 agy 설정도 격리 환경에 반영되지 않습니다. 기밀 정보는 절대 전달하지 마세요.
### Claude 구독 이용: `--use_claude_code`

Claude Code의 공식 CLI인 `claude`을 `-p` 모드로 사용할 때도 같은 원리가 적용됩니다.
Claude Pro 또는 Max 구독자는 번역 비용이 토큰 단위로 청구되는 대신
구독 할당량에서 차감됩니다. 사용량에 따라 요금이 청구되는
Anthropic API인 `--use_claude`과 혼동하지 마세요.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **유료 경로는 모두 차단되며, 모든 호출에서 이를 확인합니다.** Claude
  Code에는 환경 변수 중 명시적으로 허용된 목록만 전달됩니다.
  API 키, 토큰, 클라우드 공급자 정보, aipmt를 실행한 Claude Code
  세션의 표식은 전달되지 않습니다. 첫 번째 구간을 처리하기 전에 `claude auth status`에서
  Console 키 없이 구독으로 연결되었음이 표시되어야 하며, 할당량을
  소비하지 않는 `/usage`으로 이를 확인해야 합니다. 이후 각 호출에서도
  초기화 이벤트를 통해 이를 확인하며, 확인되지 않으면 응답을 거부합니다.
- **‘추가 사용’을 비활성화하세요**(claude.ai, 설정 → 사용량).
  그래야 비용이 0유로로 유지됩니다. 이 기능이 활성화되어 있으면
  사용 시간대의 할당량이 소진된 뒤에도 오류 없이 유료 사용으로 전환됩니다.
  aipmt는 호출의 할당량 보고에서 이를 감지하는 즉시 번역을 중단하지만, 해당 호출은 이미 과금된 상태입니다.
- **Claude Code 세션과 할당량을 공유합니다.** 각 호출은
  5시간 및 주간 사용량을 보고합니다. 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`)를 초과하면 업무에 필요한 할당량을
  소진하지 않도록 추가 구간을 시작하지 않습니다.
- **격리 실행.** 각 호출은 도구 없이, 비공개 임시 디렉터리에서
  사용자 설정을 적용하지 않는 모드로 실행됩니다. 사용자의 `CLAUDE.md`, 플러그인,
  훅, MCP 서버, 설정을 불러오지 않으며 세션 정보도 보관하지 않습니다.
  첨부 파일 기능도 꺼져 있습니다. 문서 안의 `@chemin`은
  텍스트로만 남으며 파일을 열지 않습니다(측정으로 확인).
- **모델**: 기본값은 `sonnet`이며, 추론 강도는 `low`입니다. `--eco`에서도 동일합니다.
  이 경로에서는 `--eco`이 아무 영향도 주지 않습니다. 같은 문서로 측정했을 때 `haiku`은
  추론을 끌 수 없어 두 배 느린 반면,
  비용은 아주 조금만 낮았습니다. `opus`은 생물학 관련 콘텐츠를 거부합니다(다음
  항목 참고). 두 모델 모두 `--model`으로 사용할 수 있으며, 이 별칭은
  각 계열의 최신 모델을 가리킵니다. `fable`과 `[1m]` 변형은
  유료 크레딧을 사용하므로 거부됩니다. `--reasoning_effort`은 추론 강도를 설정하지만,
  번역에서는 이점이 없습니다. 측정된 추론량은 없거나 거의 없었습니다.
- **Opus는 일부 생물학 관련 콘텐츠를 거부합니다.** 안전 장치가
  Sonnet보다 엄격하며, Anthropic 오류 메시지는
  ‘생물학 연구와 관련된 작업이 간혹 감지될 수 있다’고 알립니다. 측정 결과,
  생성된 분자 279개에 관한 짧은 동향 소식 때문에 14개
  언어 모두에서 기사 번역이 거부되었습니다. 파일은 작성되지 않습니다. aipmt는 잘린 응답을 거부하고,
  안전 장치가 원인임을 명시하며 `--model sonnet`을 권장합니다.
- CI 환경(`CI` 또는 `GITHUB_ACTIONS` 설정 시)과 Windows에서는 거부됩니다(미측정).
- 변수: `AIPMT_CLAUDE_BIN`(없으면 `PATH`, 그다음 `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT`(구간당 초 단위 제한, 기본값 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION`(기본값 0.8), `CLAUDE_CONFIG_DIR`(Claude Code의
  계정이며, 프로젝트의 `.env`에서는 가져오지 않음). 작업 디렉터리는
  `XDG_CACHE_HOME/aipmt/claude-code` 아래에 생성됩니다(기본값 `~/.cache`).

**이용 약관: 책임은 본인 계정에 따릅니다.**
[Claude Code 법적 고지 페이지](https://code.claude.com/docs/en/legal-and-compliance)는
‘최종 사용자가 자신의 Claude 구독으로 수정되지 않은 Claude Code 바이너리에
로그인하는 것’을 금지하지 않습니다. aipmt는 공식
바이너리를 실행하고 토큰을 읽지 않으므로 여기에 해당합니다. 하지만 Anthropic은
‘외부 개발자가 […] 사용자를 대신하여 Free, Pro 또는 Max 요금제의
인증 정보로 요청을 전달하는 것을 허용하지 않으며’, ‘오픈 소스 프로젝트를
포함한’ 외부 도구에는 API 키 사용을 권장하고, 해당 사용량을
유료 크레딧에서 차감할 권리를 보유합니다
([Claude 도움말](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
배포된 도구가 바이너리를 실행하는 경우를 명확히 판단하는 조항은 없습니다.

**데이터**: Free, Pro, Max 계정에서는 개인정보 보호 설정에서 허용한 경우
Claude Code의 데이터도 모델 학습에 사용됩니다
([데이터 안내 페이지](https://code.claude.com/docs/en/data-usage)). aipmt는
로컬에 대화 기록을 보관하지 않습니다(`--no-session-persistence`). 기밀 정보는
입력하지 마세요.

### 원하는 공급자 이용: `--use_opencode`

[OpenCode](https://opencode.ai)는 오픈 소스(MIT) 코딩 에이전트로,
내부에 설정된 공급자로 요청을 전달합니다. API 키, 구독,
OpenCode Zen 게이트웨이(계정 없이 사용하는 무료 모델), 로컬 모델을 이용할 수 있습니다.
여기서는 Zen과 Ollama 두 경로를 처음부터 끝까지 측정했습니다.

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

`--model`은 필수입니다. 지정하지 않으면 OpenCode가 대화 내용을
학습에 사용할 수 있는 무료 모델로 전환하기 때문입니다. 이 선택을
사용자 대신 내리지는 않습니다.

각 호출의 격리 방식:

- 사용자 설정보다 우선하는 인라인 설정으로 `aipmt` 에이전트를 정의합니다.
  모든 도구를 차단하고(`permission: { "*": "deny" }`), 세션 공유를
  비활성화하며, `--pure`을 사용하고 `--auto`은 사용하지 않습니다.
- 비어 있는 임시 작업 디렉터리를 사용하고 `OPENCODE_DISABLE_PROJECT_CONFIG`과
  `OPENCODE_DISABLE_CLAUDE_CODE`를 설정합니다. 이 설정이 없으면 OpenCode는
  현재 디렉터리의 `AGENTS.md`과 `~/.claude/CLAUDE.md`을 프롬프트에 삽입합니다.
  전역 `~/.config/opencode/AGENTS.md`은 계속 삽입됩니다. OpenCode에는
  이를 제외하는 기능이 없습니다.
- 출력 조건: 반환 코드 0, `error` 이벤트 없음, 도구
  호출 없음, 마지막 단계가 `stop`, 비어 있지 않은 텍스트, `aipmt` 에이전트가
  실제로 로드됨. 알 수 없는 `--agent`을 지정해도 OpenCode는 실패하지 않고,
  별도 알림 없이 코딩 에이전트로 전환합니다.
- OpenCode 자체의 키인 `OPENCODE_API_KEY`을 제외하고는
  `aipmt`의 키를 전달하지 않습니다. 공급자는 `aipmt`의
  `.env`이 아니라 OpenCode에서 설정합니다.

알아둘 사항:

- Zen의 무료 모델은 수시로 바뀌고 제한 사항이 문서화되어 있지 않으며,
  대화 내용이 학습에 사용될 수 있습니다. 공개 문서에 사용하고,
  비공개 콘텐츠에는 사용하지 마세요.
- 로컬 모델은 최소 16 k 토큰의 컨텍스트를 지원해야 합니다. 구간 하나가
  최대 16 000자이기 때문입니다. Ollama는 보통 4 096으로 설정하므로,
  `Modelfile`에서 `PARAMETER num_ctx 32768`을 사용하세요.
- `--eco`은 아무 영향도 주지 않습니다. `--reasoning_effort`는 OpenCode의
  `--variant`으로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 변수: `OPENCODE_BIN`(없으면 `PATH`, 그다음 `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT`(구간당 초 단위 제한, 기본값 600). `OPENCODE_CONFIG`은
  OpenCode에 그대로 전달됩니다.

`~/.config/opencode/opencode.json`에서 Ollama로 로컬 모델을 사용하는 예:

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

`reasoningEffort: "none"`은 Ollama가 이 모델들에서 기본으로 활성화하는
추론을 끕니다. Modelfile로는 이 추론을 끌 수 없습니다. 여섯 단어로 된
문장을 측정한 결과, 이 옵션이 없으면 추론 토큰 919개와 68초가 필요했고, 옵션을 사용하면 토큰 9개가 필요했습니다.

### 400개 이상의 모델 이용: `--use_openrouter`

OpenRouter는 하나의 크레딧 잔액으로 외부 호스팅 모델에
요청을 전달하고 사용량에 따라 요금을 청구하는 라우터입니다. 여기에는 이 문서의 다른
공급자에서는 제공하지 않는 중국의 공개 모델도 포함됩니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`은 필수입니다. 요금이 발생하기 전에 실행되는 사전 점검에서
라우팅의 두 가지 특성을 처리합니다.

- **동일한 모델을 서로 다른 한도로 수십 개의 호스팅 업체가 제공합니다.**
  `z-ai/glm-5.3-flash`의 경우 호스팅 업체는 23개이며, 그중 한 곳은
  출력 토큰 한도가 2 048개입니다. 사전 점검은 `/api/v1/models/{modèle}/endpoints`를 읽고,
  출력 토큰 한도가 8 000개 미만이거나 서비스 상태가 저하된 업체를 제외한 뒤,
  나머지를 `allow_fallbacks: false`으로 고정합니다.
- **추론은 출력 요율로 과금됩니다.** `z-ai/glm-5.2`의
  ‘OK’ 응답에서는 토큰 2개에 비해 107개가 사용되었습니다. 추론은 기본적으로 꺼집니다.
  추론이 필수인 모델에는 허용되는 가장 낮은 강도를 설정합니다. 카탈로그의 기본값을 사용하면
  번역이 끝나기 전에 출력 한도를 소진할 수 있기 때문입니다.
  `--reasoning_effort`이 항상 우선합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 컨텍스트 창 크기는 카탈로그에서 가져옵니다. 16 400토큰 미만인 모델은
  호출 전에 거부됩니다. 프롬프트와 구간에 8 400토큰,
  출력에 최소 8 000토큰이 필요합니다.
- 슬러그가 카탈로그에 없거나, 카탈로그에 접속할 수 없거나,
  필요한 한도를 충족하는 호스팅 업체가 없으면 명령을 중단합니다.
- 빈 출력과 함께 `finish_reason=length`이 발생하면 잘림이 아니라
  추론으로 토큰 예산을 소진한 것입니다. 메시지에서 이를 구분해 알립니다.
- `--eco`은 아무 영향도 주지 않습니다.
- 변수: `OPENROUTER_API_KEY`(<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://`
  필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (기본값 30).

### 번역 안내문

`--add_translation_note`는 `bottom`(기본값), `top`(프런트 매터
뒤) 또는 `both`(`--note_position`) 위치에 안내문을 추가합니다. 형식은 `legacy`(굵은
문단, 기본값) 또는 `marker`(`--note_format`)입니다. `marker` 형식은
보이지 않는 Markdown 참조 정의인
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
뒤에 굵은 인용문을 붙입니다. GitHub에서 읽을 수 있으며, 빌드 시
remark 플러그인으로 처리할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정 결과

모든 측정은 `aipmt`로 실제 실행한 번역이며,
대상은 14개 언어입니다. 영어, 스페인어, 독일어, 이탈리아어, 포르투갈어, 네덜란드어, 폴란드어, 스웨덴어, 루마니아어, 일본어, 한국어, 중국어, 아랍어, 힌디어입니다.
**작성됨**은 검증을 통과하여 작성된 파일 수이며, **차이
없음**은 `scripts/compare_structure.py`에서 아무 문제도 발견하지 못한 파일 수입니다. 즉,
섹션, 부제목, 링크, 서로 다른 URL, 코드 블록,
인라인 코드, 표 행, 인용 블록, 굵은 단어의 수가 같습니다.

‘차이 없음’은 ‘감지된 것이 없음’을 뜻하며 ‘동일함’을 뜻하지는 않습니다. 비교기는
내용을 읽지 않고 요소 수만 셉니다. 4단계 제목이
삭제되거나, 인라인 코드의 내용이 바뀌거나, 국기가
바뀌거나, 내부 링크에 닫는 괄호가 하나 더 붙어
`[texte]((#ancre))`처럼 어디로도 연결되지 않아도 감지하지 못합니다.
언어도 판별하지 않습니다.

### 내용이 밀도 높은 동향 기사, `--news` 모드

[jls42.org의 AI 동향](https://jls42.org/fr/news) 한 호:
589줄, 링크 140개, 섹션 21개, 보호된 영어 인용문 3개.
2026년 9월 4일과 5일에 측정했습니다.

| 모델                                          | 이용 방식              | 작성됨 | 차이 없음   | 언어당 중앙값 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 구독  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 구독  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 구독 | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude 구독  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude 구독  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | 로컬              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 구독    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude 구독  | 0/14    | ❌ 0/14      | —              |

Grok는 9월 9일 같은 동향의 다른 호
(356줄)로 다시 측정했습니다. 14개 언어 중 9개가 작성되었고, 8개에서 차이가 없었습니다.
상단 표에는 이 수치를 사용했습니다. 중단된 측정 세 건은
포함하지 않았습니다. `qwen3.5-27b`(9개 언어)와 `kimi-k2.6`(4개)는 크레딧 부족으로 중단되었고,
`z-ai/glm-5.3-flash`의 두 차례 실패는 이후 공급자가 수정한
추론 설정 때문에 발생했습니다. OpenRouter 항목은
`--use_openrouter` 도입 전 라우터 기본 설정으로 측정했습니다. 배포된 공급자 구현으로
다시 측정한 `z-ai/glm-5.2`도 동일하게 14/14를 기록했습니다. 수치는
9월 10일 현재 비교기로 다시 계산했습니다. `qwen3.8-flash`와
`qwen3.7-flash`은 최초 게시 때보다 각각 한 언어씩 늘었고,
나머지는 바뀌지 않았습니다.

`--use_antigravity` 항목은 9월 26일 같은
기사로 번역 네 개를 병렬 실행하여 측정했습니다. 오전에는 `gemini-3.7-flash-medium`,
오후에는 `gemini-3.8-flash-medium`을 측정했습니다. 영어 번역에서는 두 모델 모두
인용문 아래의 프랑스어 번역 세 줄을 스스로 삭제했고, 국기를 임의로 추가하지 않았으며,
영어 인용문을 그대로 보존했습니다. 따라서 대체 정리 절차가
처리할 것은 없었습니다. `--eco`(`gemini-3.7-flash-low`)에서는 네 언어
(영어, 일본어, 아랍어, 힌디어)만 측정했습니다. 4개 중 4개가 작성되었고, 모두 차이가 없었으며,
중앙값은 1 min 52 s였습니다. 같은 날 더 최근 호인
9월 25일자 동향(438줄, 영어 인용문 2개)으로 교차 검증했습니다.
블로그 외부에서 `gemini-3.7-flash-medium`으로 번역한 결과,
14개 중 14개가 작성되었고, 모두 차이가 없었으며, 언어당 87~128 s가 걸렸습니다.

`--use_claude_code` 항목은 9월 26일 같은
기사로 번역 네 개를 병렬 실행하여, 추론 강도 `low`에서 측정했습니다. `sonnet`은
14개 언어 모두에서 영어 인용문을 그대로 보존했고, 영어 번역에서는
프랑스어 번역 줄을 스스로 삭제했으며 국기를 임의로 추가하지 않았습니다.
`opus`은 어떤 언어도 작성하지 못했습니다. 결합 부위를 대상으로
생성한 분자 279개에 관한 짧은 소식 때문에 모든 언어에서 마지막 구간의
응답이 안전 장치에 의해 중단되었습니다. 이 소식만 따로 보내도
‘생물학’ 범주로 거부되었습니다. `sonnet`은 모든 언어로 번역했습니다. `haiku`는
14개 언어를 모두 작성했지만, 세 언어(영어, 폴란드어, 루마니아어)에서는 섹션 제목이
2단계에서 1단계로 바뀌었습니다. 추론을 끌 수 없으며, 추론이 출력
토큰의 61 %를 차지해 `sonnet`보다 두 배 이상 오래 걸렸습니다.

`claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-haiku-4-5` 항목은
10월 18일 Anthropic API로 같은 기사를 번역하여 측정했으며,
모델마다 번역 네 개를 병렬 실행했습니다. Sonnet 5.5는
추론 비활성화를 허용하지 않습니다. aipmt는 허용되는 가장 낮은 설정을 전달하며,
응답에는 추론이 포함되지 않았습니다. 14개 언어 모두 차이 없이 작성했고
구간을 재시도하지도 않았습니다. 영어 번역에서는 프랑스어 번역
줄을 스스로 삭제하고 국기를 임의로 추가하지 않았으며, 모든 언어에서 영어 인용문을
그대로 보존했습니다. Haiku 5.5는 적응형 추론을 사용해 측정했습니다.
추론을 끄면 문단 전체를 프랑스어로 남겨 검증에서 거부되었고,
14개 언어 중 3개만 작성되었습니다. 두 Haiku 모델은 같은 짧은 소식에서 문제를 일으켰습니다.
Haiku 5.5는 일본어, 한국어, 중국어에서 제목 단계를 바꾸거나 제목을 중복했고,
Haiku 4.5는 일곱 언어에서 제목을 1단계로 바꾸고,
일본어에서는 제목을 프랑스어로 남겼습니다. 두 문서를 14개 언어로 번역하는 데 든 비용은
Haiku 4.5가 3.67 $, Haiku 5.5가 0.57 $, Sonnet 5.5가 9.21 $였습니다.
### 이 프로젝트의 README, 표준 Markdown

2026년 9월 9일에 고정한 리비전: 785줄, 인라인 코드 285개, 블록
종료 구분자 40개, 표의 행 89개. 번역 네 개를 병렬로 실행.

| 모델                                          | 작성 완료 | 차이 없음 | 언어당 중앙값 | 차이 내용                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | 없음                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | 없음                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 비교 도구 기준으로는 없음; 내부 링크 중복 (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | 없음                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | 없음                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 굵게 표시된 단어 하나 (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 굵게 표시된 단어 하나 (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 표의 한 행이 이전 행에 붙음 (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | 링크 하나 (sv), 굵게 표시된 단어 하나 (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 굵게 표시된 단어 하나 (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 굵게 표시된 단어 하나 (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 아랍어에서 인라인 코드 40개 추가; 굵게 표시 (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2개 언어 거부 (ar, hi): 반환 결과에서 인라인 코드 누락        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | 섹션 하나 누락 (ar, hi, ko); 코드 블록 추가 (ja, ko, ro, zh) |

중단된 두 차례의 측정은 집계하지 않았습니다. Grok은 열두 언어 처리 후 CLI 세션이
만료되었고(열한 언어는 차이 없음), `qwen3.8-flash`은 두 언어 처리 후
호스팅 제공업체에서 HTTP 429가 발생했습니다. `opencode/mimo-v2.5-free`과 `ollama/gpt-oss-20b-32k`은
이 리비전에서 다시 측정하지 않았습니다. 277줄 더 짧았던 9월 4일과 5일의 리비전에서는
각각 14개 중 9개 번역을 작성했으며, 그중 차이가 없는 번역은 각각 7개와
1개였습니다.

`--use_antigravity` 및 `--use_claude_code` 행은 고정된 리비전에서 측정하지 않고,
9월 26일에 1.14.0과 함께 게시된 리비전에서 측정했습니다. 그리고
`claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-haiku-4-5` 행은 10월 18일에
같은 리비전에서 측정했습니다. 이 리비전은 600줄, 인라인 코드 257개, 블록 종료 구분자 30개,
표의 행 85개로 구성됩니다.
185줄 더 짧으므로 다른 행들과 항목별로 직접 비교할 수는 없지만,
이 행들끼리는 서로 비교할 수 있습니다. 비교 도구가 검사하지 않는 내부 링크의 경우,
`gemini-3.8-flash-medium`은 열네 언어 모두에서 그대로 유지했고,
`gemini-3.7-flash-medium`은 이탈리아어에서 링크를 깨뜨렸습니다.
`sonnet`과 `opus`은 모든 언어에서 그대로 유지했고, `haiku`은
영어에서 링크를 중복시켰습니다. `claude-sonnet-5-5`과 `claude-haiku-4-5`은
열네 언어 모두에서 그대로 유지했고, `claude-haiku-5-5`은 작성한 열두 언어에서 그대로 유지했습니다.

### 잘 알려진 프로젝트 네 개의 README

GitHub에서 그대로 가져온 FastAPI, Ollama, tldr-pages, Vue.js 문서로,
앞의 두 문서보다 쉽습니다. 이번 측정은 어려움을 보인 모델들을 대상으로 했으며,
Gemini는 비교 기준으로 사용했습니다.

| 모델                    | 범위                  | 작성 완료 | 차이 없음   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4개 프로젝트 × 14개 언어     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4개 프로젝트 × 14개 언어     | 55/56   | ❌ 47/56     |
| `grok-4.6` (구독)   | 4개 프로젝트 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4개 프로젝트 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 이 측정의 한계

- **모든 모델을 망라한 순위가 아닙니다**: OpenRouter에서만 400개 이상의
  모델을 제공하지만, 측정한 모델은 약 15개입니다.
- **소요 시간은 참고용입니다**: 측정에 따라 번역 세 개에서 여섯 개를 병렬로
  실행하며, 제공업체의 처리 속도는 하루 중에도 달라집니다.
- **특정 시점의 관찰 결과입니다**: 같은 이름의 모델도 바뀌며, 여러분의
  문서는 저희 문서와 다릅니다.

여러분의 문서로 다시 측정하려면, 파일의 고정된 사본에서 다음을 실행하세요.

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

두 줄 모두 필요합니다. `pip install -e .`이 없으면 `python -m aipmt`이
`No module named aipmt`이라고 응답합니다.

품질 관리 도구는 선택 사항이지만 권장합니다.

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 번역 28개(README와 CHANGELOG, 열네 언어)는
`./regen_translations.sh --force`으로 다시 생성합니다. 기본적으로 ChatGPT 구독에서 Codex와
`gpt-6.1-sol`을 사용하며, 네 개를 병렬로 실행합니다. `REGEN_PROVIDER`와
`REGEN_MODEL`은 실행 경로를 바꿉니다. `antigravity`은 Google 구독을
계속 사용하므로 별도의 예외 허용 없이 실행됩니다. 사용량에 따라 요금이 청구되는 API
(`openai`, `gemini`, `grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다.
`REGEN_JOB_TIMEOUT`은 각 작업의 시간을 제한합니다(600 s, Codex와
Antigravity에서는 1 800 s). 도구에 관한 자세한 내용은 `CLAUDE.md`에 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 게시되는 개인 블로그입니다.
  [일일 AI 동향](https://jls42.org/fr/news)은 이 도구로 매일
  번역되며, 위 측정의 기준 문서로 사용됩니다.

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE 버전 3. [라이선스](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

## 주의 사항

이 프로그램은 GPL v3의 제15조와 제16조에 따라 **어떠한 보증도 없이**
배포됩니다. 상품성이나 특정 목적에 대한 적합성의 보증 없이
“있는 그대로” 제공되며, 사용으로 인해 발생하는 손해에 대해
작성자는 책임을 지지 않습니다. 라이선스 원문이 이 요약보다
우선합니다.

- **게시하기 전에 다시 읽어보세요.** 보호 대상은 코드 블록,
  인라인 코드, URL, 앵커, `--news` 모드의 인용문입니다. 제목,
  표, 프런트 매터, 문장의 의미는 보호 대상에 포함되지 않습니다.
- **문서는 선택한 제공업체로 전송되며**, 해당 업체의 이용 약관과
  데이터 정책이 적용됩니다. 일부 무료 모델은 대화 내용을 학습에
  재사용할 수 있으며, Antigravity의 약관은 유료 구독을 포함해 Google이
  대화 내용을 재사용하고 사람이 검토하도록 허용합니다.
  로컬 모델만이 어떤 데이터도 기기 밖으로 보내지 않는 유일한 방법입니다.
- **API 호출 요금은 사용자에게 청구됩니다.** 이 프로그램은 지출
  상한을 설정하지 않습니다. 긴 문서, 실패 후 재시도, 추론량이 많은
  모델은 비용이 더 많이 듭니다.
- **게시된 측정값은 특정 시점의 관찰 결과이며**, 보증이 아닙니다.

언급된 제품명과 회사명은 각 소유자에게 귀속됩니다.
이 프로젝트는 이들 중 어느 곳과도 제휴 관계가 없습니다.

**gpt-6.1-sol로 프랑스어에서 한국어로 번역된 기사.**
