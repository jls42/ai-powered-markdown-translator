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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="테스트 커버리지"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="취약점"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="버그"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 스멜"></a>
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
코드 블록, 인라인 코드, URL, 앵커, 표, 프런트 매터 등의 구조를
보존합니다. 모델 호출 방법은 API 다섯 가지, 사용량별
과금이 없는 구독 네 가지, 라우터 두 가지로 총 열한 가지이며, 각
모델이 실제로 무엇을 보존하는지 측정한 결과도 공개합니다.

## 한눈에 보기

- **열한 가지 제공업체 이용 경로**: OpenAI, Mistral, Claude, Gemini, Grok API;
  사용량별 과금이 없는 ChatGPT (Codex), Grok, Google (Antigravity), Claude (Claude
  Code) 구독; OpenCode 라우터(오픈 소스, 무료 또는 로컬)와 OpenRouter 라우터
  (400개 이상의 모델).
- **토큰 유실로 인한 손상 방지**: 코드 블록, 인라인 코드,
  URL, 앵커, 인용문을 호출 전에 토큰으로 대체하고
  응답을 받은 뒤 검증합니다. 하나라도 누락되면 파일을 저장하지 않습니다.
- **긴 문서**: 모델의 컨텍스트 창에 맞춰 분할합니다.
- **`--news` 모드**: 동향 기사에 맞춰 영어 인용문을 보호하고
  언어별로 플래그를 처리합니다.
- **`--eco` 모드**: 빠르고 저렴한 모델을 사용합니다.
- 선택 사항인 **번역 안내문**을 문서 상단, 하단 또는 양쪽에 넣을 수 있습니다.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 이상이 필요합니다. 저장소에서 설치하려면
[기여하기](#기여하기)를 참고하세요.

## 설정

키는 다음 세 위치에서 우선순위가 높은 순서대로 읽습니다. 각 위치에서는
앞선 위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일회성 재정의 |
| 2   | 현재 디렉터리 또는 상위 디렉터리의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | 한 번 설정하면 어디서나 적용       |

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
따릅니다. 키가 없으면 명령이 세 위치를 나열합니다.

**프로젝트의 `.env`은 호출을 다른 곳으로 보내거나 실행할 프로그램을
선택할 수 없습니다.** 이 파일은 키만 제공하며, 목적지나 실행 파일은 지정하지 않습니다.
`_BASE_URL`, `_API_BASE`, `_ENDPOINT`, `_BIN` 계열의 모든 변수(`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, 프록시(`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), 인증서 저장소(`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), `XDG_CONFIG_HOME` /
`APPDATA`은 이 파일에서 무시되며 경고가 표시됩니다. 복제한 저장소가
키를 가로채거나 첫 번역 시 자체 프로그램을 실행하게
해서는 안 됩니다. 이 파일은 변수 보간 없이 읽기도 합니다.
`NOM=${OPENAI_API_KEY}`은 이 파일에서 키를 복사하지 않습니다. 이러한 변수는
환경이나 `~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT`(호출당 초 단위, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(기본값 600), `GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`), `GROK_TIMEOUT`
(기본값 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT`(기본값 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT`(기본값 600), `OPENROUTER_BASE_URL`
(`https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900),
`OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각 변수의 자세한 내용은
해당 제공업체 절에 나와 있습니다.

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
`--include_model`을 사용하면 `document-es-gpt-5.6-terra.md`이 됩니다. 확장자는
항상 `.md`가 됩니다. 예를 들어 `article.mdx`은 `article-en.md`가 됩니다.
단, `--keep_filename`을 사용하면 원래 이름을 유지합니다. 이미 번역이 있으면
`--force`을 지정하지 않는 한 건너뜁니다.

종료 코드: 모두 성공하거나 건너뛰었으면 `0`, 실패한 파일이 남아 있으면
`1`(목록은 표준 오류로 출력), 설정 문제라면 `2`입니다.
실패한 파일은 저장하지 않으며, 저장 작업 자체가 실패해도 마찬가지입니다.
내용을 옆의 임시 파일에 쓴 다음 이름을 변경합니다. 다시 실행하면 됩니다.

## 모델 선택

실제 문서 두 개를 각 모델로 동일한 열네 언어로 번역해
측정했습니다. **수치는 열네 언어 중 번역 파일이 저장되었고
원본과 차이가 없는 언어의 수입니다.**

| 모델                | 이용 방법                 | 밀도 높은 동향 기사 | 이 README    | 차이점 및 해당 언어 수                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google 구독 (Antigravity)   | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 차이 없음                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API 키                 | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 차이 없음                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API 키                    | ✅ 14/14                | ⚠️ 13/14     | 14개 언어 중 1개: 굵게 표시된 단어 하나 추가 (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google 구독 (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 14개 언어 중 1개: 단어 하나의 굵은 표시 누락 (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT 구독 또는 OpenAI 키 | ✅ 14/14                | ⚠️ 12/14     | 14개 언어 중 2개: 단어 하나의 굵은 표시 누락 (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter 키                    | ✅ 14/14                | ⚠️ 11/14     | 14개 언어 중 3개: 단어 하나의 굵은 표시 누락 (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude 구독 (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 기사에서 14개 언어 중 1개: 굵게 표시된 단어 하나 추가 (zh); 이 README에서 1개: 표의 한 행이 이전 행에 붙어 화면에서 보이지 않음 (ar)            |
| Claude Haiku 4.5      | Claude 구독 (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 기사에서 3개 언어: 절 제목 하나가 1단계로 변경됨 (en, pl, ro); 이 README는 비교 도구상 차이가 없지만 내부 링크가 영어로 중복됨 |
| Claude Sonnet 5       | Anthropic API 키                 | ⚠️ 11/14                | ⚠️ 12/14     | 기사에서 3개 언어: 코드 블록 하나 추가 (es, de, hi); 이 README에서 2개: 링크 하나의 마크업 누락 (sv), 단어 하나의 굵은 표시 차이 (zh)                              |
| Claude Haiku 4.5      | Anthropic API 키                 | ⚠️ 7/14                 | ✅ 14/14     | 기사에서 7개 언어: 절 제목 하나가 1단계로 변경됨 — 일본어에서는 프랑스어로 남음; 이 README는 차이 없음                                              |
| Claude Haiku 5.5      | Anthropic API 키                 | ⚠️ 11/14                | ❌ 12/14     | 기사에서 3개 언어: 절 제목 하나의 단계가 변경되거나 중복됨 (ja, ko, zh); 이 README에서 2개 언어는 인라인 코드 유실로 거부됨 (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter 키                    | ❌ 8/14                 | ⚠️ 10/14     | 기사에서 1개 언어 거부, 다른 5개 언어는 차이 발생; 이 README에서 약 40개 단어가 `code`으로 표시됨 (ar)                                                    |
| Grok 4.6              | Grok 구독                   | ❌ 8/14                 | 미평가     | 14개 언어 중 5개는 인라인 코드와 URL이 반환되지 않아 거부됨; 네덜란드어는 모든 항목에서 차이 발생                                                               |
| GPT-OSS 20B           | 로컬 모델 (Ollama)             | ❌ 7/14                 | 재측정하지 않음 | 14개 언어 중 4개 거부: 모델이 프랑스어 구절을 남겨 보호 장치가 차단함                                                                  |
| MiMo v2.5 (무료)   | OpenCode Zen, 계정 불필요         | ❌ 11/14                | 재측정하지 않음 | 1개 언어 거부; 폴란드어에서 절 하나 유실                                                                                                                  |
| Mistral Large         | Mistral API 키                   | ❌ 5/14                 | ❌ 1/14      | **절 하나가 통째로 사라짐**: 기사에서 1개 언어 (hi), 이 README에서 3개 언어 (ar, hi, ko) — 기사에서 3개 언어도 거부됨                                |
| DeepSeek V4 Flash     | OpenRouter 키                    | ❌ 3/14                 | 재측정하지 않음 | 14개 언어 중 10개 거부; 언어당 37분                                                                                                                 |
| Claude Opus 5.5       | Claude 구독 (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | 생물학 단신 때문에 Opus의 보호 장치가 14개 언어 모두에서 기사를 거부함; 이 README는 차이 없음                                               |

|     | 기호의 의미                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 열네 언어 모두 번역되었으며 원본과 차이가 없음                                                                                                                                       |
| ⚠️  | 열네 언어 모두 번역됨; 차이는 단어의 굵은 표시, `code`, 대괄호가 사라진 링크 등 **마크업**에 있음. 본문, URL, 코드 블록, 절은 누락되지 않음 |
| ❌  | 하나 이상의 언어를 번역하지 못함 — 파일이 거부되어 저장되지 않음 — **또는** 저장된 파일에 내용이 누락됨                                                                      |

이 결과에서 알아둘 점:

- **번역 거부는 번역 손상과 다릅니다.** 응답에서 토큰이
  누락되면 파일을 저장하지 않으며 해당 언어는
  거부된 것으로 집계합니다. Grok의 기사 번역이 이에 해당합니다. 비라틴 문자
  체계 다섯 개에서 첫 번째 구간부터 인라인 코드 네 개와
  URL 세 개가 유실되었습니다.
- **모델은 문장 하나 때문에 문서 전체를 거부할 수 있습니다.** Opus 5.5는
  이 README를 차이 없이 번역하지만 동향 기사는 하나도 번역하지
  못합니다. 생물학 단신에서 보호 장치가 응답을 차단하기 때문입니다. 파일은
  저장되지 않으며 aipmt가 그 이유를 알려줍니다.
- **이 보호 장치는 제목, 표, 프런트 매터,
  본문까지 보호하지는 않습니다.** 모델이 절 하나를 삭제해도 도구는 그 파일을
  그대로 저장합니다. Mistral이 이에 해당합니다. 이러한 요소는
  토큰으로 대체할 수 없으며 현재의 보호 장치는 이를 검사하지 않습니다.
  `scripts/compare_structure.py`은 누락된 절을 감지하지만 사후 검사입니다.
- **이 README에 대한 Grok 평가는 없습니다**: 열두 언어를 처리한 뒤 CLI
  세션이 만료되었으며, 그중 열한 언어는 차이가 없었습니다. 중단된 측정에는 점수를 매기지 않습니다.
- **언어보다 문서의 밀도가 더 큰 영향을 줍니다.** Grok은 일반적인
  README는 처리하지만 링크가 많은 기사에서는 네덜란드어를
  포함해 제대로 처리하지 못합니다.

측정 날짜 및 문서: « 이 README » 열은 2026년 9월 9일에
이 파일의 고정된 리비전(785줄, 인라인 코드 285개, 표
89행)으로 측정했으며 이후 수정되었습니다. 단, Antigravity와 Claude Code 행은
9월 26일에 1.14.0과 함께 공개된 더 짧은 리비전
(600줄, 인라인 코드 257개, 표 85행)으로 측정했으며, API를 이용한 Claude
Sonnet 5.5, Haiku 5.5, Haiku 4.5 행은 10월 18일에
같은 리비전으로 측정했습니다. « 밀도 높은 동향 기사 » 열은
9월 4일과 5일에 589줄의 기사로 진행한 측정 결과입니다. 단, Grok 행은
9월 9일에 같은 동향 기사의 다른 판으로 재측정했고, Antigravity와
Claude Code 행은 9월 26일에 같은 기사로 측정했으며, 위의 세
Claude 행은 10월 18일에 측정했습니다. 전체 표, 소요 시간, 측정 절차는
[상세 측정 결과](#상세-측정-결과)에 있습니다.
## 모든 옵션

| 옵션                   | 설명                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일 (`--source_dir`의 대안)                                             |
| `--source_dir`           | Markdown 파일이 있는 원본 디렉터리 (기본값: `content/posts`)                                   |
| `--target_dir`           | 번역된 파일의 출력 디렉터리 (기본값: `traductions_en`)                                    |
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
| `--use_opencode`         | OpenCode에 설정된 제공업체를 통해 OpenCode (오픈 소스) 사용; `--model provider/modèle` 필수 |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                          |
| `--force`                | 강제로 다시 번역                                                                                       |
| `--keep_filename`        | 원본 파일 이름 유지                                                                          |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 플래그 관리                                      |
| `--add_translation_note` | 번역 주석 추가                                                                                |
| `--note_position`        | 주석 위치: `top`, `bottom` (기본값) 또는 `both`                                                     |
| `--note_format`          | 주석 형식: `legacy` (기본값, 굵은 글씨 문단) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 수준: `none`/`low`/`medium`/`high`/`xhigh`                                         |

아홉 개의 `--use_*` 플래그는 서로 배타적입니다. 두 개를 함께 사용하면
거부됩니다.

## 제공업체

### API 사용: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`은 각 제공업체의 저비용 등급으로 전환합니다.

| 제공업체    | 고품질 (기본값)                                                     | 저비용 (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (`--model`를 통해 `gpt-5.6-sol`, `terra`, `luna`도 사용 가능) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                                           | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, 추론 수준 `low`                                               | 동일 — `--eco` 적용 안 됨 |
| OpenCode    | `--model provider/modèle` 필수                                | 동일 — `--eco` 적용 안 됨 |
| OpenRouter  | `--model fournisseur/modèle` 필수                             | 동일 — `--eco` 적용 안 됨 |

### ChatGPT 구독 사용: `--use_codex`

공식 Codex CLI를 실행합니다. API 키나 사용량별 과금 없이
ChatGPT 구독 할당량에서 번역 사용량이 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 실행 파일은 `CODEX_BIN`, `PATH`, `openai-codex-cli-bin` 패키지
  순서로 찾습니다. `~/.codex/auth.json`은 읽지 않습니다.
- 하위 프로세스 환경에서 `OPENAI_API_KEY` 및 `CODEX_API_KEY`를
  제거합니다. 키가 있어도 API로 전환되지 않습니다.
- 각 세그먼트는 5시간 사용 한도에서 최소 한 건의 « 메시지 »를 소비합니다. 검증에
  실패하여 재시도하면 두 건을 소비합니다. OpenAI가 제시한 추정치는
  Plus 요금제에서 `gpt-5.6-luna` (`--eco`)의 경우 5시간당 250-2 000건,
  `gpt-5.6-sol`의 경우 10-100건입니다.
- 1.16.3까지 기본값이었던 `--model gpt-5.6-sol`, `--model gpt-5.6-terra`,
  `--model gpt-5.6-luna`도 구독을 통해 사용합니다.
- 서버에서 429가 반환되어도 파일이 유실되지 않습니다. Codex가 자동으로 다시 연결하고,
  aipmt는 해당 차례가 끝날 때까지 기다립니다. 끝내 429로 실패하면 세그먼트를
  30초 후, 이어서 60초 후에 재시도합니다. 계정에서 사용할 수 없는 모델은 400 오류와
  « ChatGPT 계정으로 Codex를 사용할 때 지원되지 않는 모델입니다 »라는 메시지를 반환합니다.
- API보다 느리며, 문서가 길수록 차이가 커집니다. 이 README에서
  `gpt-5.6-sol`의 언어당 중앙값은 6분 46초인 반면,
  `gemini-3.7-flash`은 36초입니다.
- CI에서는 거부됩니다 (`CI` 또는 `GITHUB_ACTIONS`가 설정된 경우). 구독 인증에는
  개인 세션 파일을 사용하므로 공유 실행기에 두어서는 안 됩니다.
- 변수: `CODEX_BIN`, `CODEX_TIMEOUT` (세그먼트당 초 단위 시간, 기본값 600).

### Grok 구독 사용: `--use_grok_cli`

공식 Grok Build CLI를 통해 SuperGrok 또는
X Premium+ 구독을 사용하는 동일한 방식입니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex보다 격리가 약합니다.** Grok의 운영체제 샌드박스는
  최근 Linux 환경 중 상당수에서 적용되지 않으며 (AppArmor, 컨테이너
  런타임 소켓), 적용할 수 없는 프로필은 아무 알림 없이 격리되지 않은 상태로
  시작됩니다. 따라서 스크립트는 기본적으로 프로필을 요청하지 않고 이 사실을 알리며,
  포괄 규칙인 `*`을 포함한 CLI의 `--deny` 규칙에 의존합니다. 이 규칙은
  보호를 몰래 해제하는 대신 시작을 거부하는 유일한 계층입니다.
  `GROK_TRANSLATE_SANDBOX=read-only`은 운영체제 샌드박스를 요구하며, 시스템이 이를
  적용할 수 없으면 시작에 실패합니다.
- 할당량은 주 단위이며 Chat, Imagine, Voice와 공유됩니다. 이를
  조회하는 명령은 없습니다. 따라서 일괄 작업이 아무 알림 없이 대화용
  할당량을 소비할 수 있습니다.
- 변수: `GROK_BIN`, `GROK_HOME` (CLI 디렉터리, 기본값 `~/.grok`),
  `GROK_TIMEOUT` (기본값 900), `GROK_TRANSLATE_SANDBOX`.

### Google 구독 사용: `--use_antigravity`

Antigravity의 공식 CLI인 `agy`을 사용하는 동일한 방식입니다. Google
AI Pro 또는 Ultra 구독자는 토큰별 과금 대신 구독
할당량에서 번역 사용량이 차감됩니다. 이 할당량을 사용할 수 있는 유일한 경로입니다. Gemini CLI는
2026년 6월 18일부터 해당 계정을 더 이상 지원하지 않으며
([공지](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
Antigravity SDK는 API 키 또는 Google Cloud 프로젝트만 허용합니다.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **유료 과금 경로는 모두 차단됩니다.** agy에는 환경 변수 중
  허용 목록에 있는 항목만 전달됩니다. `PATH`, 언어 및 시간대,
  터미널, 사용자 정보, 프록시 및 인증서, 세션 버스만 전달되며 키는 전달되지 않습니다.
  여러 환경 변수가 아무 알림 없이 호출 경로를 바꾸기 때문입니다. 측정 결과,
  한 변수는 문서를 제삼자 게이트웨이로 보내고, 다른 변수는 과금되는
  Google Cloud 프로젝트로 보냈습니다. 차단 목록 방식은 검토할 때마다 누락이 발견되었습니다.
  세그먼트를 처리하기 전에 할당량을 소비하지 않는 `agy -p /config`에서
  유료 인공지능 크레딧이 비활성화되어 있고 API 키와 Google Cloud 프로젝트가 없음을
  확인해야 합니다. 설정이 누락되어도 거부하며, 이 조건을 충족하지 않으면 아무것도 번역하지 않습니다.
  이후 각 호출의 로그에서 구독 사용 (`authMethod=consumer`)이 확인되어야 하며, 그렇지 않으면
  응답을 거부합니다.
- **격리.** 각 호출은 도구가 없는 번역 에이전트를 사용해
  비공개 임시 홈 디렉터리에서 실행됩니다. agy의 개인 설정, 규칙,
  플러그인, MCP 서버, 훅은 전달되지 않으며, 사용자 기록에도 아무것도 추가되지 않습니다.
  로그인 정보는 키링에 남고 aipmt는 이를 읽지 않습니다.
  에이전트를 찾지 못하면 agy는 아무 알림 없이 코딩 에이전트와
  도구로 돌아갑니다. 따라서 로그의 한 줄 전체가 올바른 에이전트를 확인해 주어야 합니다.
  문서에 인용된 해당 메시지는 이를 대신할 수 없으며, 확인되지 않으면 거부합니다.
- **플랫폼**: 키링이 있는 세션의 Linux
  (D-Bus 세션 버스, Secret Service). macOS도 허용하지만 측정하지는 않았습니다.
  Windows에서는 agy가 각 호출을 격리하는 환경 변수를 읽지 않으므로 거부합니다.
  세션 버스가 없는 Linux 환경인 SSH 세션, 컨테이너, 서버에서도 거부합니다. 이 환경에서 agy는
  `~/.gemini`의 파일에 토큰을 저장하는데, 격리로 인해 해당 파일이 가려집니다.
  로그인 코드를 기다리며 1분을 보내는 대신, 실행 전에 원인을 알리고
  거부합니다.
- **모델**: `agy models`에 있는 모델을 사용합니다. Gemini는 모델 이름에 추론 수준이
  포함됩니다 (`gemini-3.8-flash-medium` 등). 접미사가 없는 이름은 호출 전에 거부하며,
  `--reasoning_effort`는 적용되지 않습니다. 기본값은 `gemini-3.8-flash-medium`이며,
  `--eco`에서는 `gemini-3.7-flash-low`입니다. 이 기본값을 정한 측정 작업은
  [상세 측정](#상세-측정-결과)에 설명되어 있습니다. Claude와 GPT-OSS는
  별도의 훨씬 적은 할당량을 사용합니다. 측정된 호출당 사용량은 5시간 한도의
  약 1 %인 반면, Flash는 0,05 %입니다.
- **할당량**: 그룹별로 5시간 한도와 주간 한도가 있으며,
  토큰 비용에 비례해 차감됩니다. 작성자의 계정에서 측정한 결과, 원본 100만 문자당
  5시간 한도의 약 16퍼센트포인트를 `gemini-3.8-flash-medium`에서,
  14퍼센트포인트를 `gemini-3.7-flash-medium`에서, 7~8퍼센트포인트를 낮은
  추론 수준에서 소비합니다. 따라서 40 000자 README는
  0.5퍼센트포인트를 조금 넘게 소비합니다. 주간 한도는 요금 등급에 따라 달라집니다. 재시도는
  agy가 재시도 가능하다고 표시한 경우에 따릅니다. 그렇지 않으면 한도를 소진한 경우
  재시도하지 않습니다. `/usage`에 표시된 초기화 시점까지
  모든 파일의 처리가 실패합니다.
- **API보다 느립니다**: 측정에 사용한 정보 밀도가 높은 문서에서 언어당
  중앙값은 `gemini-3.8-flash-medium`의 경우 3분 59초,
  `gemini-3.7-flash-medium`의 경우 3분 14초인 반면, API를 통한 Gemini 3.7 Flash는 1분 18초입니다.
- **중단**: Ctrl-C를 누르거나 터미널을 닫으면 명령과 함께 agy도
  중지되어, 할당량을 소비하며 해당 차례를 끝까지 처리하지 않습니다.
  Codex, Grok CLI, OpenCode도 동일합니다. `nohup`에서는 번역이 계속됩니다.
- CI에서는 거부됩니다 (`CI` 또는 `GITHUB_ACTIONS`가 설정된 경우). 로그인 정보가
  개인 키링에 저장되기 때문입니다. 실행기에서는 `--use_gemini`과 `GOOGLE_API_KEY`을 사용하세요.
- 변수: `AGY_BIN` (없으면 `PATH`, 그다음 `~/.local/bin/agy`),
  `AGY_TIMEOUT` (시작 시간을 포함한 세그먼트당 초 단위 시간, 기본값 900).

**이용 약관: 사용자의 계정에 책임이 따릅니다.**
[Antigravity 이용 약관](https://antigravity.google/terms) (제6조)과
[자주 묻는 질문](https://antigravity.google/docs/faq/)은 Antigravity 로그인 정보를 이용해
제삼자 소프트웨어로 서비스에 접근하는 것을 금지하며, 위반 시 계정이 정지될 수 있습니다.
Claude Code, OpenClaw, OpenCode가 명시적으로 언급되어 있습니다. aipmt는
토큰을 읽거나 재사용하지 않습니다. Google이
스크립트와 CI용으로 문서화한 [헤드리스 모드](https://antigravity.google/docs/cli/headless/)에서
공식 실행 파일을 실행합니다. Google의 한 구성원은 자신의 작업을 위해
로컬 스크립트에서 `agy -p`을 실행하는 것을 « 통상적인 사용 »으로 보았습니다
([공식 포럼, 2026년 9월 25일, 계약상 구속력이 없는 답변](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)).
그러나 이 도구처럼 배포되는 도구의 경우를 명확히 규정한 문서는 없습니다.

**공개 문서만 사용하세요.** 같은 약관의 제5조에 따르면,
프롬프트, 응답, 메타데이터를 포함한 상호작용 내용은 유료 구독에서도
Google 제품과 기계 학습 개선에 사용될 수 있으며,
사람이 검토할 수도 있습니다. 이를 거부하려면
`enableTelemetry` 설정을 사용해야 하지만, 그 효과는 문서화되어 있지 않으며 aipmt는 이를 설정하지 않습니다.
agy의 개인 설정은 격리 환경에 전달되지 않습니다. 기밀 정보는 절대 입력하지 마세요.
### Claude 구독 이용: `--use_claude_code`

Claude Code의 공식 CLI인 `claude`을 `-p` 모드로 사용할 때도 원리는 같습니다.
Claude Pro 또는 Max 유료 구독자는 번역 비용이 토큰 단위로 청구되는 대신
구독 할당량에서 차감됩니다.
사용량에 따라 요금이 청구되는 Anthropic API인 `--use_claude`과
혼동하지 마세요.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **유료 과금 경로는 모두 차단되며, 호출마다 이를 확인합니다.** Claude
  Code에는 환경 변수의 제한된 목록만 전달됩니다. API 키,
  토큰, 클라우드 제공업체 정보, aipmt를 실행한 Claude Code 세션의
  표식은 전달되지 않습니다. 첫 번째 구간을 처리하기 전에 `claude auth status`에서
  Console 키 없이 구독으로 연결되었음이 표시되어야 하며, 할당량을 전혀 소모하지 않는
  `/usage`으로 이를 확인해야 합니다. 이후 각 호출도 초기화 이벤트에서
  이를 확인하며, 그렇지 않으면 응답을 거부합니다.
- **‘추가 사용’을 비활성화하세요**(claude.ai, 설정 → 사용량). 그래야
  비용이 0유로로 유지됩니다. 활성화되어 있으면 일정 기간의 할당량이 소진된 뒤
  자동으로 추가 사용으로 전환되어 오류 표시 없이 요금이 청구됩니다. aipmt는 호출의
  할당량 보고에 이 사실이 표시되는 즉시 번역을 중단하지만, 해당 호출은 이미 과금된 상태입니다.
- **Claude Code 세션과 할당량을 공유합니다.** 각 호출은
  5시간 및 주간 할당량 사용 현황을 보고합니다. 사용량이 80 %를 넘으면
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) 추가 구간을 실행하지 않아
  업무에 필요한 할당량이 소진되는 것을 방지합니다.
- **격리.** 각 호출은 도구 없이 비공개 임시 디렉터리에서
  사용자 설정을 적용하지 않는 모드로 실행됩니다. 사용자의 `CLAUDE.md`, 플러그인,
  훅, MCP 서버, 설정을 불러오지 않으며
  세션 정보도 보관하지 않습니다. 첨부 파일 기능은 비활성화됩니다. 문서에 있는
  `@chemin`은 텍스트로 남으며 파일을 열지 않습니다(실측 확인).
- **모델**: 기본값은 `sonnet`이며, 추론 강도는 `low`입니다. `--eco`에서도
  동일합니다. 이 경로에서는 `--eco`이 아무 영향도 주지 않습니다. 같은 문서로 측정했을 때 `haiku`은
  추론을 끌 수 없어 두 배 느렸지만
  비용은 조금만 낮았고, `opus`은 생물학 관련 내용을 거부했습니다(다음
  항목 참조). 두 모델 모두 `--model`으로 사용할 수 있으며, 이 별칭은
  각 계열의 최신 모델을 가리킵니다. `fable`과 `[1m]` 변형은 유료 크레딧을
  사용하므로 거부됩니다. `--reasoning_effort`은 추론 강도를 설정하지만,
  번역에는 이점이 없습니다. 측정된 추론량은 없거나 거의 없었습니다.
- **Opus는 일부 생물학 관련 내용을 거부합니다.** 안전장치가
  Sonnet보다 엄격하며, Anthropic의 오류 메시지는
  ‘생물학 연구와 인접한 작업을 간혹 차단할 수 있다’고 안내합니다. 실측 결과,
  생성된 분자 279개를 다룬 짧은 동향 기사 때문에 14개 언어 모두에서
  기사 번역이 거부되었습니다. 파일은 기록되지 않습니다. aipmt는 잘린 응답을 거부하고,
  안전장치가 원인임을 알리며 `--model sonnet`을 권장합니다.
- CI(`CI` 또는 `GITHUB_ACTIONS`이 설정된 경우)와 Windows(미측정)에서는 거부됩니다.
- 변수: `AIPMT_CLAUDE_BIN`(없으면 `PATH`, 그다음 `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT`(구간당 초, 기본값 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION`(기본값 0.8), `CLAUDE_CONFIG_DIR`(Claude Code
  계정이며, 프로젝트의 `.env`에서는 절대 가져오지 않음). 작업 디렉터리는
  `XDG_CACHE_HOME/aipmt/claude-code` 아래에 생성됩니다(기본값 `~/.cache`).

**이용 약관: 책임은 사용자의 계정에 따릅니다.**
[Claude Code 법적 안내 페이지](https://code.claude.com/docs/en/legal-and-compliance)는
‘최종 사용자가 자신의 Claude 구독으로 수정되지 않은 Claude Code 바이너리에
로그인하는 것’을 금지하지 않습니다. aipmt는 공식 바이너리를 실행하고
토큰을 전혀 읽지 않으므로 이에 해당합니다. 하지만 Anthropic은 ‘타사 개발자가 […]
사용자를 대신해 Free, Pro 또는 Max 요금제의 인증 정보를 통해 요청을 전달하는 것’을
허용하지 않으며, ‘오픈 소스 프로젝트를 포함한’ 타사 도구에는 API 키 사용을
권장하고, 해당 사용량을 유료 크레딧에서 차감할 권리를
유보합니다
([Claude 도움말](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
배포된 도구가 바이너리를 실행하는 경우를 명확히 규정한 문구는 없습니다.

**데이터**: Free, Pro 및 Max 계정에서는 개인정보 설정에서 허용한 경우
Claude Code에도 모델 학습이 적용됩니다
([데이터 안내 페이지](https://code.claude.com/docs/en/data-usage)). aipmt는
로컬 대화 기록을 보관하지 않습니다(`--no-session-persistence`). 기밀 정보는
입력하지 마세요.

### 원하는 제공업체 이용: `--use_opencode`

[OpenCode](https://opencode.ai)는 오픈 소스(MIT) 코딩 에이전트로,
내부에 설정된 제공업체로 요청을 전달합니다. API 키, 구독,
OpenCode Zen 게이트웨이(계정 없이 사용하는 무료 모델) 또는 로컬 모델을 사용할 수 있습니다.
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

`--model`은 필수입니다. 없으면 OpenCode가 대화 내용을 학습에 사용할 수 있는
무료 모델로 대체하기 때문이며, 이 선택은
사용자를 대신해 내리지 않습니다.

각 호출의 격리 방식:

- 사용자 설정보다 우선하는 인라인 설정으로 모든 도구가 거부된
  `aipmt` 에이전트를 정의합니다(`permission: { "*": "deny" }`). 세션 공유를 비활성화하고,
  `--pure`을 사용하며 `--auto`은 절대 사용하지 않습니다.
- 비어 있는 임시 작업 디렉터리를 사용하고 `OPENCODE_DISABLE_PROJECT_CONFIG`과
  `OPENCODE_DISABLE_CLAUDE_CODE`를 설정합니다. 이 설정이 없으면 OpenCode는 현재 디렉터리의
  `AGENTS.md`과 `~/.claude/CLAUDE.md`을 프롬프트에 삽입합니다.
  전역 `~/.config/opencode/AGENTS.md`은 계속 삽입됩니다. OpenCode에서는
  이를 제외할 수 없습니다.
- 출력 조건: 종료 코드 0, `error` 이벤트 없음, 도구 호출
  없음, 마지막 단계가 `stop`, 비어 있지 않은 텍스트, `aipmt` 에이전트가
  실제로 로드되었는지 확인합니다. 알 수 없는 `--agent`을 지정해도 OpenCode는 실패하지 않고,
  아무 알림 없이 코딩 에이전트로 대체합니다.
- OpenCode 자체의 키인 `OPENCODE_API_KEY`을 제외하면 `aipmt`의
  키는 전달되지 않습니다. 제공업체는 OpenCode에서 설정하며,
  `aipmt`의 `.env`에서 설정하지 않습니다.

알아둘 사항:

- Zen의 무료 모델은 수시로 바뀌고, 제한 사항이 문서화되어 있지 않으며,
  대화 내용이 학습에 사용될 수 있습니다. 공개 문서에 사용하고
  비공개 콘텐츠에는 사용하지 마세요.
- 구간 길이가 최대 16 000자이므로 로컬 모델은 최소 16 k 토큰의
  컨텍스트를 제공해야 합니다. Ollama는 흔히 4 096으로 설정하므로,
  `PARAMETER num_ctx 32768`이 설정된 `Modelfile`을 사용하세요.
- `--eco`은 아무 영향이 없습니다. `--reasoning_effort`는 OpenCode의
  `--variant`으로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 변수: `OPENCODE_BIN`(없으면 `PATH`, 그다음 `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT`(구간당 초, 기본값 600). `OPENCODE_CONFIG`은
  OpenCode에 그대로 전달됩니다.

`~/.config/opencode/opencode.json`에서 Ollama를 통해 로컬 모델을 사용하는 예시:

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

`reasoningEffort: "none"`은 Ollama가 이 모델들에서 기본적으로 활성화하는 추론을
끕니다. 이 추론은 Modelfile로 비활성화할 수 없습니다.
여섯 단어로 된 문장으로 측정한 결과, 옵션이 없으면 추론 토큰 919개와
68초가 필요했고, 옵션을 사용하면 토큰 9개가 필요했습니다.

### 400개 이상의 모델 이용: `--use_openrouter`

OpenRouter는 하나의 충전 잔액으로 타사에서 호스팅하는
모델을 이용하는 사용량 기반 과금 라우터입니다. 여기에는 이 도구의 다른
제공업체가 제공하지 않는 중국의 공개 모델도 포함됩니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`은 필수입니다. 과금 전에 실행되는 사전 점검이
라우팅의 두 가지 특성을 처리합니다.

- **동일한 모델을 서로 다른 한도를 가진 수십 개 호스팅 업체가 제공합니다.**
  `z-ai/glm-5.3-flash`에는 호스팅 업체가 23곳 있으며, 그중 한 곳은 출력이
  2 048토큰으로 제한됩니다. 사전 점검은 `/api/v1/models/{modèle}/endpoints`을 읽어
  출력 한도가 8 000토큰 미만이거나 상태가 저하된 업체를 제외하고,
  나머지를 `allow_fallbacks: false`으로 고정합니다.
- **추론에는 출력 요금이 부과됩니다.** `z-ai/glm-5.2`의
  ‘OK’ 응답에서 2토큰 대신 107토큰이 사용되었습니다. 추론은 기본적으로 꺼집니다.
  추론이 필수인 모델에는 허용되는 가장 낮은 강도를 적용합니다. 목록의
  기본값을 사용하면 번역이 끝나기 전에 출력 한도가 소진될 수 있기 때문입니다.
  `--reasoning_effort`이 항상 우선합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 컨텍스트 한도는 모델 목록에서 가져옵니다. 16 400토큰 미만인 모델은
  호출 전에 거부됩니다. 프롬프트와 구간에 8 400토큰,
  출력에 최소 8 000토큰이 필요합니다.
- 목록에 없는 슬러그, 접근할 수 없는 목록, 필요한 한도를 충족하는
  호스팅 업체가 없는 경우에는 명령을 중단합니다.
- 출력이 비어 있는 `finish_reason=length`은 잘림이 아니라
  추론으로 예산을 소진한 경우이며, 메시지에서 이를 구분합니다.
- `--eco`은 아무 영향이 없습니다.
- 변수: `OPENROUTER_API_KEY`(<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://`
  필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (기본값 30).

### 번역 안내문

`--add_translation_note`는 `bottom`(기본값), `top`(프런트 매터 뒤)
또는 `both`(`--note_position`)에 안내문을 추가합니다. 형식은 `legacy`(굵은
문단, 기본값) 또는 `marker`(`--note_format`)입니다. `marker` 형식은
화면에 표시되지 않는 Markdown 참조 정의
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`에
굵은 인용문을 덧붙입니다. GitHub에서 읽을 수 있으며, 빌드 시
remark 플러그인으로 활용할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정 결과

모든 측정은 `aipmt`으로 실제 번역을 실행한 결과이며, 대상은
14개 언어입니다. 영어, 스페인어, 독일어, 이탈리아어, 포르투갈어, 네덜란드어, 폴란드어, 스웨덴어, 루마니아어, 일본어, 한국어, 중국어, 아랍어, 힌디어입니다.
**기록됨**은 검증을 통과해 기록된 파일 수이며, **차이
없음**은 `scripts/compare_structure.py`이 아무 차이도 감지하지 못한 파일 수입니다. 즉,
섹션, 소제목, 링크, 고유 URL, 코드 블록,
인라인 코드, 표 행, 인용 블록, 굵은 단어의 수가 같습니다.

‘차이 없음’은 ‘감지된 것이 없음’을 뜻하며 ‘동일함’을 뜻하지 않습니다. 비교기는
내용을 읽지 않고 요소의 개수만 셉니다. 4단계 제목이
삭제되거나, 인라인 코드의 내용이 바뀌거나, 국기가
교체되거나, 내부 링크에 닫는 괄호가 하나 더 붙어
`[texte]((#ancre))`처럼 아무 곳으로도 연결되지 않아도 감지하지 못합니다.
언어도 평가하지 않습니다.

### 정보 밀도가 높은 동향 기사, `--news` 모드

[jls42.org의 인공지능 동향](https://jls42.org/fr/news) 한 호를 사용했습니다.
589줄, 링크 140개, 섹션 21개, 보호된 영어 인용문 3개입니다.
2026년 9월 4일과 5일에 진행한 측정입니다.

| 모델                                          | 이용 방식              | 기록됨 | 차이 없음   | 언어별 중앙값 |
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

Grok은 9월 9일 같은 동향의 다른 호
(356줄)로 다시 측정했습니다. 14개 언어 중 9개가 기록되었으며, 8개는 차이가 없었습니다.
문서 앞부분의 표에는 이 수치가 나옵니다. 중단된 측정 세 건은
포함하지 않았습니다. `qwen3.5-27b`(9개 언어)와 `kimi-k2.6`(4개)는 잔액 부족으로,
`z-ai/glm-5.3-flash`은 제공업체가 이후 수정한 추론 설정 때문에
두 차례 실패했습니다. OpenRouter 행은
`--use_openrouter` 도입 전에 라우터 기본 설정으로 측정했습니다. 제공되는 제공업체 연동으로
다시 측정한 `z-ai/glm-5.2`은 동일하게 14/14를 기록했습니다. 수치는
9월 10일 현재 비교기로 재계산했습니다. `qwen3.8-flash`과
`qwen3.7-flash`은 최초 공개 때보다 각각 한 언어씩 늘었고,
나머지는 변동이 없습니다.

`--use_antigravity` 행은 9월 26일 같은 기사로
번역 네 개를 병렬 실행해 측정했습니다. 오전에는 `gemini-3.7-flash-medium`,
오후에는 `gemini-3.8-flash-medium`을 사용했습니다. 영어 번역에서는 두 모델 모두 인용문 아래의
프랑스어 번역 세 줄을 스스로 제거했고, 국기를 임의로 만들지 않았으며,
영어 인용문은 그대로 유지했습니다. 대체 정리 절차가 처리할 것은
없었습니다. `--eco`(`gemini-3.7-flash-low`)에서는 네 언어
(영어, 일본어, 아랍어, 힌디어)만 측정했습니다. 4개 중 4개가 기록되었고, 모두 차이가 없었으며,
중앙값은 1 min 52 s였습니다. 같은 날 더 최근 호인
9월 25일 동향(438줄, 영어 인용문 2개)을
`gemini-3.7-flash-medium`으로 블로그 밖에서 번역해 교차 확인했습니다. 14개 중 14개가
기록되었고, 모두 차이가 없었으며, 언어당 87~128 s가 걸렸습니다.

`--use_claude_code` 행은 9월 26일 같은 기사로
번역 네 개를 병렬 실행하고 추론 강도를 `low`으로 설정해 측정했습니다. `sonnet`에서는
14개 언어 모두에서 영어 인용문이 그대로 유지되었고, 영어 번역에서는
모델이 프랑스어 번역 줄을 스스로 제거했으며 국기를
임의로 만들지 않았습니다. `opus`은 어떤 언어도 기록하지 못했습니다. 모든 언어에서
결합 부위를 위해 생성한 분자 279개에 관한 짧은 기사 때문에
안전장치가 마지막 구간에서 응답을 중단했습니다. 이 짧은 기사를 단독으로 보내도
‘생물학’ 범주에 해당한다는 이유로 거부되었습니다. `sonnet`은 모든 언어로 번역했습니다. `haiku`은
14개 언어를 모두 기록했지만, 세 언어(영어, 폴란드어, 루마니아어)에서 섹션 제목이
2단계에서 1단계로 바뀌었습니다. 추론을 끌 수 없으며, 추론이
출력 토큰의 61 %를 차지해 `sonnet`보다 두 배 넘는 시간이 걸렸습니다.

`claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-haiku-4-5` 행은
10월 18일 Anthropic API로 같은 기사를 사용해 모델별로
번역 네 개를 병렬 실행하여 측정했습니다. Sonnet 5.5는 추론을 끄는 설정을
거부하므로, aipmt는 모델이 허용하는 가장 낮은 설정을 보내며
응답에는 추론이 전혀 포함되지 않습니다. 14개 언어를 모두 차이 없이 기록했고
어떤 구간도 재처리하지 않았습니다. 영어 번역에서는 프랑스어 번역 줄을
스스로 제거했고 국기를 임의로 만들지 않았으며, 영어 인용문은
모든 언어에서 그대로 유지되었습니다. Haiku 5.5는 적응형 추론을 사용해 측정했습니다.
추론을 끄면 문단 전체를 프랑스어로 남겨 검증에서 거부되었으며,
14개 언어 중 3개만 기록되었습니다. 두 Haiku 모델은 같은 짧은 기사에서 문제가 발생했습니다.
Haiku 5.5는 일본어, 한국어, 중국어에서 제목 수준을
바꾸거나 제목을 중복했고, Haiku 4.5는 일곱 언어에서 제목을 1단계로 바꾸었으며
일본어에서는 프랑스어로 남겼습니다. 두 문서를 14개 언어로 번역하는 비용은
Haiku 4.5가 3,67 $, Haiku 5.5가 0,57 $, Sonnet 5.5가 9,21 $였습니다.
### 이 프로젝트의 README, 표준 Markdown

2026년 9월 9일에 고정한 버전: 785줄, 인라인 코드 285개, 블록
종료 구분자 40개, 표 89줄. 번역 4개를 병렬로 실행했습니다.

| 모델                                          | 작성 완료 | 차이 없음 | 언어당 중앙값 | 차이점                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | 없음                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | 없음                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 비교 도구상 차이 없음; 내부 링크 중복 (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | 없음                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | 없음                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 단어 하나의 굵은 글씨 (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 단어 하나의 굵은 글씨 (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 표의 한 행이 이전 행에 붙음 (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | 링크 하나 (sv), 단어 하나의 굵은 글씨 (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 단어 하나의 굵은 글씨 (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 단어 하나의 굵은 글씨 (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 아랍어에서 인라인 코드 40개 추가; 굵은 글씨 (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2개 언어 거부 (ar, hi): 반환 결과에서 인라인 코드 유실        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | 섹션 하나 유실 (ar, hi, ko); 코드 블록 추가 (ja, ko, ro, zh) |

중단된 두 차례의 측정은 포함하지 않았습니다. Grok은 12개 언어를 처리한 뒤
명령줄 세션이 만료되었으며(11개는 차이 없음), `qwen3.8-flash`은 2개 언어를 처리한 뒤
호스팅 제공업체에서 HTTP 429 오류가 발생했습니다. `opencode/mimo-v2.5-free`과 `ollama/gpt-oss-20b-32k`은
이 버전에서 다시 측정하지 않았습니다. 277줄 더 짧았던 9월 4일과 5일
버전에서는 각각 14개 중 9개의 번역을 작성했고, 그중 차이가 없는 번역은 각각 7개와
1개였습니다.

`--use_antigravity`과 `--use_claude_code` 행은 고정한 버전이 아니라
9월 26일에 1.14.0과 함께 공개된 버전으로 측정했습니다. 그리고
`claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-haiku-4-5` 행은 10월 18일에
동일한 버전으로 측정했습니다. 해당 버전은 600줄, 인라인 코드 257개, 블록 종료 구분자 30개, 표
85줄입니다. 이 버전은
185줄 더 짧으므로 다른 행과 항목별로 직접 비교할 수는 없지만,
이 행들끼리는 서로 비교할 수 있습니다. 비교 도구가
검사하지 않는 내부 링크의 경우, `gemini-3.8-flash-medium`은
14개 언어 모두에서 그대로 유지했고, `gemini-3.7-flash-medium`은 이탈리아어에서 링크를 깨뜨렸습니다.
`sonnet`과 `opus`은 모든 언어에서 그대로 유지했고, `haiku`은
영어에서 링크를 중복시켰습니다. `claude-sonnet-5-5`과 `claude-haiku-4-5`은
14개 언어 모두에서 그대로 유지했으며, `claude-haiku-5-5`은 작성한 12개 언어에서 그대로 유지했습니다.

### 유명 프로젝트의 README 4개

FastAPI, Ollama, tldr-pages, Vue.js의 문서를 GitHub에서 그대로 가져왔습니다.
앞의 두 문서보다 쉬운 문서들입니다. 이번 측정은
어려움을 겪은 모델을 대상으로 했으며, Gemini를 비교 기준으로 삼았습니다.

| 모델                    | 범위                  | 작성 완료 | 차이 없음   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4개 프로젝트 × 14개 언어     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4개 프로젝트 × 14개 언어     | 55/56   | ❌ 47/56     |
| `grok-4.6` (구독)   | 4개 프로젝트 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4개 프로젝트 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 이 측정의 한계

- **전체 모델을 망라한 순위가 아닙니다**: OpenRouter에서만 400개 이상의
  모델을 제공하지만, 측정한 모델은 약 15개입니다.
- **소요 시간은 참고용입니다**: 측정마다 3~6개의 번역을 병렬로 실행했으며,
  제공업체의 처리 속도는 하루 중에도 달라집니다.
- **특정 시점의 관찰 결과입니다**: 같은 이름의 모델도 바뀌며,
  여러분의 문서는 저희 문서와 다릅니다.

여러분의 문서로 다시 측정하려면, 파일의 고정된 사본을 사용하세요.

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

품질 검사 도구는 선택 사항이지만 권장합니다.

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 번역 28개(README와 CHANGELOG, 14개 언어)는
`./regen_translations.sh --force`으로 다시 생성합니다. 기본적으로 ChatGPT 구독에서 Codex와 `gpt-6.1-sol`을 사용하며,
4개를 병렬로 실행합니다. `REGEN_PROVIDER`와
`REGEN_MODEL`은 사용 경로를 바꿉니다. `antigravity`는 Google
구독을 계속 사용하며 예외 허용 없이 실행됩니다. 과금되는 API(`openai`, `gemini`,
`grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다.
`REGEN_JOB_TIMEOUT`은 각 작업의 제한 시간을 설정합니다(600초, Codex와
Antigravity에서는 1,800초). 도구에 관한 자세한 내용은 `CLAUDE.md`에 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 게시되는 개인 블로그입니다.
  [매일 제공하는 인공지능 동향](https://jls42.org/fr/news)은 이 도구로 매일
  번역되며, 위 측정의 기준 문서로 사용됩니다.

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE 버전 3. [라이선스](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하세요.

## 주의 사항

이 프로그램은 GPL v3의 제15조와 제16조에 따라 **어떠한 보증도 없이**
배포됩니다. 상품성이나 특정 목적에 대한 적합성을 보증하지 않고
“있는 그대로” 제공되며, 사용으로 인해 발생하는 손해에 대해
작성자는 책임을 지지 않습니다. 이 요약보다
라이선스 원문이 우선합니다.

- **게시 전에 검토하세요.** 보호 기능은 코드 블록,
  인라인 코드, URL, 앵커, `--news` 모드의 인용문에 적용됩니다.
  제목, 표, 프런트 매터, 문장의 의미는 보호 대상에 포함되지 않습니다.
- **문서는 선택한 제공업체로 전송되며**, 해당 업체의 이용 약관과
  데이터 정책이 적용됩니다. 일부 무료 모델은
  대화 내용을 학습에 재사용할 수 있으며, Antigravity의 약관은
  유료 구독을 포함해 Google이 대화 내용을 재사용하고 사람이 검토하도록 허용합니다.
  데이터를 컴퓨터 밖으로 전혀 보내지 않는 유일한 방법은
  로컬 모델을 사용하는 것입니다.
- **API 호출 비용은 사용자에게 청구됩니다.** 이 프로그램은 지출
  한도를 설정하지 않습니다. 긴 문서, 실패 후 재시도, 추론을
  많이 하는 모델은 비용이 더 듭니다.
- **공개된 측정값은 특정 시점의 관찰 결과이며**, 보증이 아닙니다.

언급된 제품명과 회사명은 각 소유자에게 귀속됩니다.
이 프로젝트는 그 어느 곳과도 제휴 관계가 없습니다.

**gpt-6.1-sol로 프랑스어에서 한국어로 번역한 기사.**
