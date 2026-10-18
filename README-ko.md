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

코드 블록, 인라인 코드, URL, 앵커, 표, front matter 등의 구조를
보존하면서 Markdown 파일을 한 언어에서 다른 언어로 번역합니다.
모델을 호출하는 열한 가지 방법—다섯 가지 API, 사용량 기반 과금이 없는
네 가지 구독, 두 가지 라우터—과 각 모델이 실제로 보존하는 요소를
측정하여 공개한 결과를 제공합니다.

## 요약

- **열한 가지 provider 경로**: OpenAI, Mistral, Claude, Gemini, Grok API;
  사용량 기반 과금이 없는 ChatGPT(Codex), Grok, Google(Antigravity),
  Claude(Claude Code) 구독; OpenCode 라우터(오픈 소스, 무료 또는 로컬)와
  OpenRouter 라우터(400개 이상의 모델).
- **토큰 손실로 인한 잘못된 결과 방지**: 코드 블록, 인라인 코드,
  URL, 앵커, 인용문을 호출 전에 토큰으로 대체하고 응답 후 검증합니다.
  하나라도 누락되면 파일을 기록하지 않습니다.
- **긴 문서**: 모델의 컨텍스트 창에 맞춰 분할합니다.
- **`--news` 모드**: 모니터링 기사에 맞게 영어 인용문을 보호하고
  언어별 플래그를 처리합니다.
- **`--eco` 모드**: 더 빠르고 저렴한 모델을 사용합니다.
- 선택 사항인 **번역 주석**을 상단, 하단 또는 양쪽에 추가할 수 있습니다.

## 설치

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 이상이 필요합니다. 저장소에서 설치하려면
[기여하기](#기여하기)를 참조하세요.

## 구성

키는 우선순위가 높은 순서대로 세 위치에서 읽으며, 각 위치는 앞선
위치에서 비어 있는 값만 채웁니다.

|     | 위치                                            | 용도                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 환경 변수                     | CI, 컨테이너, 일시적 재정의 |
| 2   | 현재 디렉터리(또는 상위 디렉터리)의 `.env` | 프로젝트별 키            |
| 3   | `~/.config/aipmt/.env`                        | 한 번 설치하면 어디서나 적용       |

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

`GOOGLE_API_KEY` 대신 `GEMINI_API_KEY`도 사용할 수 있습니다. 사용자 파일은
`XDG_CONFIG_HOME`(절대 경로만 허용)과 Windows의 `%APPDATA%`을 따릅니다.
키가 없으면 명령이 세 위치를 나열합니다.

**프로젝트의 `.env`은 호출을 다른 곳으로 보내거나 실행할 프로그램을
선택할 수 없습니다.** 이 파일은 키만 제공하며 대상이나 바이너리는 제공하지
않습니다. 따라서 `_BASE_URL`, `_API_BASE`, `_ENDPOINT` 또는
`_BIN`의 모든 변수(`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`,
`AGY_BIN`), `GROK_HOME`, 프록시(`HTTP_PROXY`, `HTTPS_PROXY`,
`ALL_PROXY`), 인증서 저장소(`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`), 그리고 `XDG_CONFIG_HOME` / `APPDATA`은 경고와 함께
무시됩니다. 복제한 저장소가 사용자의 키를 가로채거나 첫 번역 때 자체
프로그램을 실행하게 해서는 안 됩니다. 또한 이 파일은 보간 없이 읽히므로
`NOM=${OPENAI_API_KEY}`에 키가 복사되지 않습니다. 이러한 변수는 환경이나
`~/.config/aipmt/.env`에 설정하세요.

선택적 변수: `XAI_BASE_URL`(기본값 `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT`(호출당 초, 기본값 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(기본값 600), `GROK_BIN`, `GROK_HOME`(기본값 `~/.grok`),
`GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`,
`AGY_TIMEOUT`(기본값 900), `OPENCODE_BIN`, `OPENCODE_TIMEOUT`(기본값 600),
`OPENROUTER_BASE_URL`(`https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900),
`OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30). 각 변수는 해당 provider 섹션에서 자세히
설명합니다.

## 시작하기

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`을 스페인어로 번역하면 `--target_dir`에
`document-es.md`이 생성되고, `--include_model`을 사용하면 `document-es-gpt-5.6-terra.md`이
생성됩니다. 확장자는 항상 `.md`이 되므로 `article.mdx`은
`article-en.md`이 됩니다. 단, `--keep_filename`을 사용하면 원래 이름을
유지합니다. 이미 존재하는 번역은 `--force`이 없으면 건너뜁니다.

종료 코드: 모두 성공하거나 건너뛴 경우 `0`, 실패한 파일이
남아 있는 경우 `1`(표준 오류 출력에 목록 표시), 구성에 문제가
있는 경우 `2`입니다. 기록 자체가 실패하더라도 실패한 파일은
절대 기록하지 않습니다. 내용을 옆에 기록한 다음 이름을 변경하기
때문입니다. 다시 실행하기만 하면 됩니다.

## 어떤 모델을 선택할 것인가

실제 문서 두 개를 각 모델로 동일한 열네 개 언어로 번역해 측정했습니다.
**수치는 열네 개 언어 중 번역이 기록되었으며 원본과 다른 요소가 전혀 없는
언어의 수입니다.**

| 모델                | 접근 방법                 | 밀도 높은 모니터링 기사 | 이 README    | 다른 점과 해당 언어 수                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google 구독(Antigravity)   | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 다른 점 없음                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API 키                 | ✅ 14/14                | ✅ 14/14     | 두 문서 모두 다른 점 없음                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API 키                    | ✅ 14/14                | ⚠️ 13/14     | 14개 언어 중 1개: 굵게 표시된 단어 하나 추가(ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google 구독(Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 14개 언어 중 1개: 굵게 표시된 단어 하나 누락(ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT 구독 또는 OpenAI 키 | ✅ 14/14                | ⚠️ 12/14     | 14개 언어 중 2개: 굵게 표시된 단어 하나 누락(ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter 키                    | ✅ 14/14                | ⚠️ 11/14     | 14개 언어 중 3개: 굵게 표시된 단어 하나 누락(hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude 구독(Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 기사에서는 14개 언어 중 1개: 굵게 표시된 단어 하나 추가(zh); 이 README에서는 1개: 표의 한 줄이 앞줄에 붙어 표시상 숨겨짐(ar)            |
| Claude Haiku 4.5      | Claude 구독(Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 기사에서는 3개 언어: 섹션 제목이 1단계로 바뀜(en, pl, ro); 이 README에서는 비교기가 감지한 차이는 없지만 영어 내부 링크가 중복됨 |
| Claude Sonnet 5       | Anthropic API 키                 | ⚠️ 11/14                | ⚠️ 12/14     | 기사에서는 3개 언어: 코드 블록 하나가 생김(es, de, hi); 이 README에서는 2개: 링크 하나의 마크업 누락(sv), 굵게 표시된 단어 하나(zh)                              |
| Claude Haiku 4.5      | Anthropic API 키                 | ⚠️ 7/14                 | ✅ 14/14     | 기사에서는 7개 언어: 섹션 제목이 1단계로 바뀜—일본어에서는 프랑스어로 남음; 이 README에서는 다른 점 없음                                              |
| Claude Haiku 5.5      | Anthropic API 키                 | ⚠️ 11/14                | ❌ 12/14     | 기사에서는 3개 언어: 섹션 제목의 단계가 바뀌거나 중복됨(ja, ko, zh); 이 README에서는 2개 언어가 거부되고 인라인 코드가 누락됨(ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter 키                    | ❌ 8/14                 | ⚠️ 10/14     | 기사에서는 1개 언어가 거부되고 다른 5개 언어에 차이가 있음; 이 README에서는 약 40개 단어가 `code`으로 표시됨(ar)                                                    |
| Grok 4.6              | Grok 구독                   | ❌ 8/14                 | 평가하지 않음     | 인라인 코드와 URL이 반환되지 않아 14개 언어 중 5개가 거부됨; 네덜란드어는 전체에 차이가 있음                                                               |
| GPT-OSS 20B           | 로컬 모델(Ollama)             | ❌ 7/14                 | 재측정하지 않음 | 14개 언어 중 4개가 거부됨: 모델이 프랑스어 구절을 남겨 보호 장치가 중단함                                                                  |
| MiMo v2.5 (무료)   | OpenCode Zen, 계정 불필요         | ❌ 11/14                | 재측정하지 않음 | 1개 언어가 거부됨; 폴란드어에서 섹션 하나가 누락됨                                                                                                                  |
| Mistral Large         | Mistral API 키                   | ❌ 5/14                 | ❌ 1/14      | **섹션 전체가 사라짐**: 기사에서는 1개 언어(hi), 이 README에서는 3개 언어(ar, hi, ko)—기사에서는 추가로 3개 언어가 거부됨                                |
| DeepSeek V4 Flash     | OpenRouter 키                    | ❌ 3/14                 | 재측정하지 않음 | 14개 언어 중 10개가 거부됨; 언어당 37분                                                                                                                 |
| Claude Opus 5.5       | Claude 구독(Claude Code)   | ❌ 0/14                 | ✅ 14/14     | 생물학 단신 때문에 Opus 보호 장치가 14개 언어 모두에서 기사를 거부함; 이 README에서는 다른 점 없음                                               |

|     | 기호의 의미                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 열네 개 언어 모두 번역되었으며 원본과 다른 점이 전혀 없음                                                                                                                                       |
| ⚠️  | 열네 개 언어 모두 번역됨; 다른 점은 굵게 표시된 단어, `code`, 대괄호를 잃은 링크 같은 **마크업**임. 텍스트, URL, 코드 블록, 섹션은 하나도 누락되지 않음 |
| ❌  | 하나 이상의 언어를 번역하지 못해 파일이 거부되고 기록되지 **않았거나**, 기록된 파일에 내용이 누락됨                                                                      |

여기서 기억할 점:

- **거부된 번역은 손상된 번역이 아닙니다.** 응답에서 토큰이 누락되면 파일을
  기록하지 않고 해당 언어를 거부된 것으로 계산합니다. Grok이 기사에서 겪는
  문제가 바로 이것입니다. 라틴 문자를 사용하지 않는 다섯 개 언어에서는 첫
  번째 세그먼트부터 인라인 코드 네 개와 URL 세 개가 누락됩니다.
- **문장 하나 때문에 모델이 문서 전체를 거부할 수 있습니다.** Opus 5.5는
  이 README를 차이 하나 없이 번역하지만 모니터링 기사는 하나도 번역하지
  못합니다. 생물학 단신 하나에서 보호 장치가 응답을 중단하기 때문입니다.
  파일은 기록되지 않으며 aipmt가 그 이유를 알려 줍니다.
- **이 안전망은 제목, 표, front matter, 텍스트를 보호하지 않습니다.**
  모델이 섹션을 삭제해도 도구는 아무 문제 없이 파일을 기록합니다.
  Mistral이 그런 경우입니다. 이러한 요소는 토큰으로 대체할 수 없으며
  현재 보호 장치는 이를 검사하지 않습니다. `scripts/compare_structure.py`은 누락된
  섹션을 감지하지만 사후에만 가능합니다.
- **Grok은 이 README에 대한 평가가 없습니다**: CLI 세션이 열두 개 언어
  이후 만료되었고, 그중 열한 개는 차이가 없었습니다. 중단된 측정은
  평가하지 않습니다.
- **언어보다 문서의 밀도가 더 중요합니다.** Grok은 일반적인 README는
  처리하지만 링크가 많은 기사에서는 실패하며, 네덜란드어에서도
  마찬가지입니다.

날짜와 문서: 「이 README」 열은 2026년 9월 9일 이 파일의 고정된
리비전(785줄, 인라인 코드 285개, 표 89줄)에서 측정했으며 이후 수정되었습니다.
단, Antigravity와 Claude Code 행은 더 짧은 1.14.0 공개 리비전(600줄,
인라인 코드 257개, 표 85줄)에서 9월 26일 측정했고, Claude Sonnet 5.5,
Haiku 5.5 및 API를 통한 Haiku 4.5 행은 같은 리비전에서 10월 18일
측정했습니다. 「밀도 높은 모니터링 기사」 열은 589줄짜리 기사를 대상으로
9월 4일과 5일에 수행한 측정에서 가져왔습니다. 단, Grok 행은 같은
모니터링 기사의 다른 판에서 9월 9일 재측정했고, Antigravity와 Claude
Code 행은 같은 기사에서 9월 26일 측정했으며, 앞서 언급한 Claude 세 행은
10월 18일 측정했습니다. 전체 표, 소요 시간, 측정 절차는
[상세 측정 결과](#상세-측정-결과)에 있습니다.
## 모든 옵션

| 옵션                   | 설명                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 번역할 단일 Markdown 파일(`--source_dir`의 대안)                                             |
| `--source_dir`           | Markdown 파일이 포함된 원본 디렉터리(기본값: `content/posts`)                                   |
| `--target_dir`           | 번역된 파일의 출력 디렉터리(기본값: `traductions_en`)                                    |
| `--source_lang`          | 원본 언어(기본값: `fr`)                                                                                  |
| `--target_lang`          | 대상 언어(기본값: `en`)                                                                                   |
| `--model`                | 사용할 특정 모델                                                                                  |
| `--eco`                  | 경제형 모델 사용                                                                              |
| `--use_mistral`          | Mistral AI API 사용                                                                                     |
| `--use_claude`           | Claude API 사용                                                                                         |
| `--use_gemini`           | Gemini API 사용                                                                                         |
| `--use_grok`             | xAI(Grok) API 사용 — `XAI_API_KEY` 필요                                                           |
| `--use_codex`            | ChatGPT 구독 할당량으로 Codex CLI 사용                                                    |
| `--use_grok_cli`         | Grok 구독 할당량으로 Grok CLI 사용                                                        |
| `--use_antigravity`      | Google AI Pro 또는 Ultra 구독 할당량으로 Antigravity CLI(`agy`) 사용                       |
| `--use_claude_code`      | Claude Pro 또는 Max 구독 할당량으로 Claude Code CLI(`claude -p`) 사용                      |
| `--use_opencode`         | OpenCode에 설정된 공급자로 OpenCode(오픈 소스) 사용. `--model provider/modèle` 필요 |
| `--use_openrouter`       | OpenRouter 사용 — `OPENROUTER_API_KEY` 및 `--model fournisseur/modèle` 필요                          |
| `--force`                | 재번역 강제                                                                                       |
| `--keep_filename`        | 원래 파일 이름 유지                                                                          |
| `--news`                 | 뉴스 모드: 영어 인용문을 보호하고 언어별 플래그 처리                                      |
| `--add_translation_note` | 번역 주석 추가                                                                                |
| `--note_position`        | 주석 위치: `top`, `bottom`(기본값) 또는 `both`                                                     |
| `--note_format`          | 주석 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`                                            |
| `--include_model`        | 출력 파일에 모델 이름 포함                                                            |
| `--reasoning_effort`     | GPT-5.x 추론 노력 수준: `none`/`low`/`medium`/`high`/`xhigh`                                         |

9개의 `--use_*` 플래그는 상호 배타적이므로 두 개를 함께 사용하면
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

`--eco`은 각 공급자의 경제형 등급으로 전환합니다.

| 공급자    | 품질형(기본값)                                      | 경제형(`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                   | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`(`--model`을 통해 `terra` 및 `luna`도 가능) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, 노력 수준 `low`                                | 동일 — `--eco`은 효과 없음 |
| OpenCode    | `--model provider/modèle` 필수                 | 동일 — `--eco`은 효과 없음 |
| OpenRouter  | `--model fournisseur/modèle` 필수              | 동일 — `--eco`은 효과 없음 |

### ChatGPT 구독 사용: `--use_codex`

공식 Codex CLI를 구동합니다. 번역 사용량은 API 키나 사용량 기반 과금 없이
ChatGPT 구독 할당량에서 차감됩니다.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 실행 파일은 `CODEX_BIN`, 그다음 `PATH`, 그다음
  `openai-codex-cli-bin` 패키지 순으로 검색됩니다. `~/.codex/auth.json`은 절대 읽지 않습니다.
- `OPENAI_API_KEY` 및 `CODEX_API_KEY`은 하위 프로세스의 환경에서
  제거됩니다. 키가 있어도 API로 전환되지 않습니다.
- 각 세그먼트는 5시간 창에서 최소 하나의 « 메시지 »를 소모하며,
  검증에 실패해 재시도하면 두 개를 소모합니다. OpenAI가 제시한 추정치는
  Plus 요금제에서 `gpt-5.6-luna`(`--eco`)의 경우 5시간당
  250~2,000개, `gpt-5.6-sol`의 경우 10~100개입니다.
- `--model gpt-5.6-terra` 및 `--model gpt-5.6-luna`도
  구독을 통해 처리됩니다. 계정에 사용 권한이 없는 모델은 400 « model is
  not supported when using Codex with a ChatGPT account » 오류를 반환합니다.
- API보다 느리고 문서가 길수록 격차가 커집니다. 이 README에서는
  언어당 중앙값이 `gpt-5.6-sol`의 경우 6분 46초인 반면
  `gemini-3.7-flash`은 36초입니다.
- CI에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS`이 설정된 경우). 구독 인증은
  개인 세션 파일을 사용하므로 공유 runner에 둘 수 없습니다.
- 변수: `CODEX_BIN`, `CODEX_TIMEOUT`(세그먼트당 초, 기본값 600).

### Grok 구독 사용: `--use_grok_cli`

공식 Grok Build CLI를 사용하는 동일한 방식으로, SuperGrok 또는
X Premium+ 구독을 이용합니다.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex보다 약한 격리.** Grok의 OS sandbox는 최신 Linux 환경의 많은
  시스템에서 적용되지 않으며(AppArmor, 컨테이너 runtime socket),
  적용할 수 없는 프로필은 아무 알림 없이 비격리 상태로 시작됩니다.
  따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않고 이를 알린 뒤,
  CLI의 `--deny` 규칙에 의존합니다. 여기에는 catch-all인
  `*`도 포함되며, 이는 보호 기능을 알리지 않고 제거하는 대신 시작을 거부하는
  유일한 계층입니다. `GROK_TRANSLATE_SANDBOX=read-only`은 OS sandbox를 요구하며,
  시스템이 이를 충족할 수 없으면 시작에 실패합니다.
- 할당량은 주 단위이며 Chat, Imagine, Voice와 공유되고 이를 확인할 수 있는
  명령도 없습니다. 따라서 일괄 작업이 아무 신호 없이 대화용 사용량을
  잠식할 수 있습니다.
- 변수: `GROK_BIN`, `GROK_HOME`(CLI 디렉터리, 기본값 `~/.grok`),
  `GROK_TIMEOUT`(기본값 900), `GROK_TRANSLATE_SANDBOX`.

### Google 구독 사용: `--use_antigravity`

Antigravity의 공식 CLI인 `agy`을 사용하는 동일한 방식입니다. Google
AI Pro 또는 Ultra 유료 사용자는 토큰 단위로 과금되는 대신 번역 사용량이
구독 할당량에서 차감됩니다. 이 할당량을 이용하는 유일한 경로입니다. Gemini CLI는
2026년 6월 18일부터 이러한 계정을 더 이상 지원하지 않으며
([공지](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
Antigravity SDK는 API 키 또는 Google Cloud 프로젝트만 허용합니다.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **유료 경로가 열려 있지 않습니다.** agy에는 사용자의
  환경에서 제한된 변수 목록만 전달됩니다. 여기에는 `PATH`, 언어와 시간대,
  터미널, 신원, proxy와 인증서, 세션 bus가 포함되지만 키는 포함되지 않습니다.
  agy의 여러 변수는 아무 표시 없이 호출 경로를 전환하기 때문입니다. 측정 결과
  한 변수는 문서를 타사 gateway로 보내고 다른 변수는 요금이 청구되는
  Google Cloud 프로젝트로 보냈으며, 거부 목록은 검토할 때마다 일부를
  빠뜨렸습니다. 어떤 세그먼트든 처리하기 전에 할당량을 소모하지 않는
  `agy -p /config`에서 API 키나 Google Cloud 프로젝트가 없는 상태로
  유료 AI credit이 비활성화되었음을 보여야 합니다. 설정이 없으면 거부된 것으로
  간주하며, 그렇지 않으면 아무것도 번역하지 않습니다. 이후 각 호출의
  log가 구독 사용(`authMethod=consumer`)을 입증해야 하며, 그렇지 않으면
  응답이 거부됩니다.
- **격리.** 각 호출은 도구가 없는 번역 agent와 함께 비공개 일회용
  개인 디렉터리에서 실행됩니다. 사용자의 설정, 규칙, plugin, MCP server 및
  agy hook은 그곳에 들어가지 않고, 사용 기록에도 아무것도 추가되지 않으며,
  연결 정보는 aipmt가 절대 읽지 않는 keyring에 남습니다.
  agent를 찾지 못하면 agy는 아무 알림 없이 코딩 agent와 그 도구로
  되돌아갑니다. 따라서 log의 한 줄 전체가 올바른 agent를 확인해야 하며,
  이 메시지를 인용하는 문서로는 이를 대신할 수 없습니다. 그렇지 않으면 거부됩니다.
- **플랫폼**: keyring이 있는 세션의 Linux(D-Bus 세션 bus, Secret Service).
  macOS도 허용되지만 측정되지는 않았습니다. 각 호출을 격리하는 변수를 agy가
  읽지 않는 Windows와 세션 bus가 없는 Linux(SSH 세션, 컨테이너, 서버)에서는
  거부됩니다. 이러한 환경에서 agy는 token을 `~/.gemini`의 파일에 저장하지만
  격리 때문에 이 파일이 보이지 않습니다. 연결 코드를 기다리며 1분을 허비하지 않도록
  실행 전에 원인과 함께 거부됩니다.
- **모델**: `agy models`의 모델입니다. Gemini 모델은 이름에 노력 수준이
  포함됩니다(`gemini-3.8-flash-medium` 등). 접미사가 없는 이름은 호출 전에 거부되며,
  `--reasoning_effort`은 효과가 없습니다. 기본값은 `gemini-3.8-flash-medium`이고
  `--eco`에서는 `gemini-3.7-flash-low`입니다. 이 값을 확정한 실험은
  [상세 측정](#상세-측정-결과)에 설명되어 있습니다. Claude와 GPT-OSS는
  훨씬 적은 별도 할당량을 갖습니다. 측정된 호출당 5시간 창의 약 1%를
  소모하는 반면 Flash는 0.05%를 소모합니다.
- **할당량**: 그룹별로 5시간 창과 주간 창이 있으며 token 비용에
  비례합니다. 작성자의 계정에서 측정한 결과, 원본 문자 100만 자당 5시간 창의
  약 16 point를 `gemini-3.8-flash-medium`에서, 14 point를 `gemini-3.7-flash-medium`에서,
  낮은 노력 수준에서는 7~8 point를 소모했습니다. 따라서 40,000자인 README는
  0.5 point보다 조금 더 소모합니다. 주간 한도는 등급에 따라 달라집니다.
  재시도는 agy가 재시도 가능하다고 선언한 항목을 따릅니다. 별도 선언이 없으면
  소진된 창에 대해서는 절대 재시도하지 않습니다. `/usage`에 표시된
  초기화 시점까지 각 파일의 처리가 실패합니다.
- **API보다 느림**: 측정 내용을 담은 고밀도 문서에서 언어당 중앙값은
  `gemini-3.8-flash-medium`의 경우 3분 59초, `gemini-3.7-flash-medium`의 경우
  3분 14초인 반면, API를 통한 Gemini 3.7 Flash는 1분 18초입니다.
- **중단**: Ctrl-C를 누르거나 터미널을 닫으면 agy가 할당량을 사용해 작업을
  끝마치도록 방치하지 않고 명령과 함께 중단됩니다. Codex, Grok CLI 및 OpenCode도
  마찬가지입니다. `nohup`에서는 번역이 계속됩니다.
- CI에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS`이 설정된 경우). 연결 정보가
  개인 keyring에 있기 때문입니다. runner에서는 `--use_gemini`와 `GOOGLE_API_KEY`을
  사용합니다.
- 변수: `AGY_BIN`(없으면 `PATH`, 그다음 `~/.local/bin/agy`),
  `AGY_TIMEOUT`(시작 시간을 포함한 세그먼트당 초, 기본값 900).

**이용약관에 대한 책임은 사용자 계정에 있습니다.** 
[Antigravity 이용약관](https://antigravity.google/terms)(제6조)과
[FAQ](https://antigravity.google/docs/faq/)는 Antigravity 연결을 이용해
타사 소프트웨어로 서비스에 접근하는 것을 금지하며, Claude Code,
OpenClaw 및 OpenCode가 그 예로 명시되어 있습니다. 위반 시 계정이 정지될 수 있습니다. aipmt는
token을 읽거나 재사용하지 않습니다. Google이 스크립트와 CI용으로
문서화한 [headless 모드](https://antigravity.google/docs/cli/headless/)에서
공식 실행 파일을 실행합니다. Google 관계자는 개인 작업을 위해 로컬 스크립트에서
`agy -p`을 실행하는 것을 « 표준적 »이라고 평가했습니다
([공식 포럼, 2026년 9월 25일, 비계약적 답변](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)).
그러나 이와 같이 배포되는 도구의 경우를 명확히 판단하는 문서는 없습니다.

**공개 문서에만 사용하세요.** 같은 약관의 제5조에 따르면 유료 구독을
포함하여 대화 내용(prompt, 응답, metadata)이 Google의 제품 및 기계 학습
개선에 사용되고 사람이 검토할 수 있습니다. 제외하려면 효과가 문서화되지 않은
`enableTelemetry` 설정을 사용해야 하지만, aipmt는 이 설정을 적용하지 않습니다.
agy 설정은 격리 환경으로 전달되지 않습니다. 기밀 정보는 절대 처리하지 마세요.
### Claude 구독을 통한 사용: `--use_claude_code`

Claude Code의 공식 CLI인 `claude`를 `-p` 모드로 사용할 때도 원리는 같습니다. Claude Pro 또는 Max 구독자는 번역 비용이 토큰 단위로 청구되는 대신 구독 할당량에서 차감됩니다. 사용량에 따라 요금이 부과되는 Anthropic API인 `--use_claude`과 혼동하지 마세요.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **유료 경로는 하나도 열려 있지 않으며, 모든 호출이 이를 증명합니다.** Claude Code는 사용자의 환경에서 제한된 변수 목록만 받습니다. API 키, 토큰, 클라우드 제공업체 정보, aipmt를 실행한 Claude Code 세션 표시자는 받지 않습니다. 첫 번째 세그먼트 전에 `claude auth status`가 Console 키 없이 구독 연결을 표시해야 하며, 할당량을 전혀 소모하지 않는 `/usage`가 이를 입증해야 합니다. 이후 각 호출도 초기화 이벤트에서 이를 입증하며, 그렇지 않으면 응답이 거부됩니다.
- **‘추가 사용량’을 비활성화하세요**(claude.ai, 설정 → 사용량). 그래야 비용을 0유로로 유지할 수 있습니다. 이 기능이 활성화되어 있으면 할당량 기간이 소진된 뒤 이를 대신해 작동하며 오류를 표시하지 않고 요금을 청구합니다. aipmt는 호출의 할당량 내역에서 이를 감지하는 즉시 번역을 중단하지만, 해당 호출 자체는 이미 계산됩니다.
- **Claude Code 세션과 할당량을 공유합니다.** 각 호출은 5시간 및 주간 기간의 사용량을 보고합니다. 80%를 넘으면(`AIPMT_CLAUDE_MAX_UTILIZATION`) 업무에 사용할 할당량을 소진하지 않도록 추가 세그먼트를 실행하지 않습니다.
- **격리.** 각 호출은 도구 없이 비공개 일회용 디렉터리에서 개인화가 비활성화된 모드로 실행됩니다. 사용자의 `CLAUDE.md`, plugins, hooks, MCP 서버 또는 설정을 불러오지 않으며 세션의 어떤 내용도 보관하지 않습니다. 첨부 파일 기능도 차단됩니다. 문서 안의 `@chemin`는 텍스트로만 남고 어떤 파일도 열지 않습니다(측정 완료).
- **모델**: 기본값은 `sonnet`, 노력 수준은 `low`이며 `--eco`에서도 같습니다. 이 경로에서는 `--eco`가 아무것도 바꾸지 않습니다. 같은 문서로 측정했을 때 `haiku`은 막을 수 없는 추론을 수행해 비용은 아주 조금 저렴하면서 속도는 두 배 느렸고, `opus`은 생물학 콘텐츠를 거부합니다(다음 항목 참조). 두 모델 모두 `--model`을 통해 계속 사용할 수 있으며, 이 별칭들은 각 제품군의 최신 모델을 가리킵니다. `fable`와 `[1m]` 변형은 유료 크레딧을 사용하므로 거부됩니다. `--reasoning_effort`는 노력 수준을 설정하지만 번역에는 아무 이점이 없습니다. 측정된 추론량은 없거나 거의 없습니다.
- **Opus는 일부 생물학 콘텐츠를 거부합니다.** 보호 장치가 Sonnet보다 엄격하며, Anthropic의 오류 메시지는 “생물학 연구와 인접한 작업이 때때로 감지될 수 있다”고 경고합니다. 측정 결과, 생성된 분자 279개를 다룬 짧은 모니터링 기사가 14개 언어 모두에서 전체 문서의 거부를 일으켰습니다. 아무것도 기록되지 않습니다. aipmt는 잘린 응답을 거부하고 보호 장치를 원인으로 명시한 뒤 `--model sonnet`를 권장합니다.
- CI에서는 거부됩니다(`CI` 또는 `GITHUB_ACTIONS`가 정의된 경우). Windows에서도 거부됩니다(측정하지 않음).
- 변수: `AIPMT_CLAUDE_BIN`(없으면 `PATH`, 그다음 `~/.local/bin/claude`), `AIPMT_CLAUDE_TIMEOUT`(세그먼트당 초, 기본값 900), `AIPMT_CLAUDE_MAX_UTILIZATION`(기본값 0.8), `CLAUDE_CONFIG_DIR`(Claude Code 계정이며 프로젝트의 `.env`에서는 절대 가져오지 않음). 작업 디렉터리는 `XDG_CACHE_HOME/aipmt/claude-code` 아래에 생성됩니다(기본값 `~/.cache`).

**이용 약관: 사용자의 계정에 책임이 귀속됩니다.** [Claude Code 법률 안내 페이지](https://code.claude.com/docs/en/legal-and-compliance)는 “최종 사용자가 수정되지 않은 Claude Code 바이너리에 자신의 Claude 구독으로 로그인하는 것”을 금지하지 않습니다. aipmt는 공식 바이너리를 실행하고 토큰을 절대 읽지 않으므로 바로 이 방식에 해당합니다. 그러나 Anthropic은 “타사 개발자가 사용자를 대신해 Free, Pro 또는 Max 요금제 자격 증명으로 요청을 라우팅하는 것을 허용하지 않으며”, “오픈 소스 프로젝트를 포함한” 타사 도구에는 API 키 사용을 권장하고, 사용량을 유료 크레딧에서 차감할 권리를 보유합니다([Claude 도움말](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)). 배포된 도구가 바이너리를 실행하는 경우에 관해서는 어떤 문서도 명확한 결론을 내리지 않습니다.

**데이터**: Free, Pro 및 Max 계정에서는 개인정보 보호 설정이 허용하는 경우 Claude Code에도 모델 학습이 적용됩니다([데이터 안내 페이지](https://code.claude.com/docs/en/data-usage)). aipmt는 로컬 대화 기록을 전혀 보관하지 않습니다(`--no-session-persistence`). 기밀 정보는 처리하지 마세요.

### 원하는 제공업체로 연결: `--use_opencode`

[OpenCode](https://opencode.ai)는 내부에 설정된 제공업체로 요청을 라우팅하는 오픈 소스(MIT) 코딩 에이전트입니다. API 키, 구독, OpenCode Zen 게이트웨이(계정 없이 사용할 수 있는 무료 모델) 또는 로컬 모델을 사용할 수 있습니다. 여기서는 Zen과 Ollama라는 두 경로를 처음부터 끝까지 측정했습니다.

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

`--model`는 필수입니다. 지정하지 않으면 OpenCode가 대화 내용을 학습에 사용할 수 있는 무료 모델로 대체하며, 이 선택을 사용자를 대신해 결정하지 않습니다.

각 호출의 격리 방식은 다음과 같습니다.

- 사용자 설정보다 우선하는 인라인 설정에서 모든 도구가 거부된(`permission: { "*": "deny" }`) `aipmt` 에이전트를 정의하고, 세션 공유를 비활성화하며, `--pure`를 사용하고 `--auto`는 절대 사용하지 않습니다.
- 비어 있는 일회용 작업 디렉터리를 사용하고 `OPENCODE_DISABLE_PROJECT_CONFIG`와 `OPENCODE_DISABLE_CLAUDE_CODE`를 설정합니다. 이를 설정하지 않으면 OpenCode가 현재 디렉터리의 `AGENTS.md`와 `~/.claude/CLAUDE.md`를 prompt에 삽입합니다. 전역 `~/.config/opencode/AGENTS.md`는 계속 삽입되며 OpenCode에서는 이를 제외할 수 없습니다.
- 출력 계약은 종료 코드 0, `error` 이벤트 없음, 도구 호출 없음, 마지막 단계가 `stop`, 비어 있지 않은 텍스트, 그리고 `aipmt` 에이전트가 실제로 로드되었을 것을 요구합니다. 알 수 없는 `--agent`를 지정해도 OpenCode는 실패하지 않고 조용히 코딩 에이전트로 대체합니다.
- `OPENCODE_API_KEY`인 OpenCode 자체 키를 제외하고 `aipmt` 키는 전혀 전달하지 않습니다. 제공업체는 `aipmt`의 `.env`가 아니라 OpenCode에서 설정합니다.

알아둘 사항:

- Zen의 무료 모델은 수시로 바뀌고 제한도 문서화되어 있지 않으며, 대화 내용이 학습에 사용될 수 있습니다. 공개 문서에는 적합하지만 비공개 콘텐츠에는 적합하지 않습니다.
- 세그먼트가 최대 16,000자이므로 로컬 모델은 최소 16k tokens의 컨텍스트를 제공해야 합니다. Ollama는 이를 4,096으로 설정하는 경우가 많으므로 `PARAMETER num_ctx 32768`가 포함된 `Modelfile`를 사용하세요.
- `--eco`는 아무 효과가 없습니다. `--reasoning_effort`는 OpenCode의 `--variant`로 그대로 전달됩니다.
- OpenCode는 각 세션을 `~/.local/share/opencode/`에 기록합니다.
- 변수: `OPENCODE_BIN`(없으면 `PATH`, 그다음 `~/.opencode/bin/opencode`), `OPENCODE_TIMEOUT`(세그먼트당 초, 기본값 600). `OPENCODE_CONFIG`는 OpenCode에 그대로 전달됩니다.

`~/.config/opencode/opencode.json`에서 Ollama를 통해 로컬 모델을 사용하는 예:

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

`reasoningEffort: "none"`는 Ollama가 이 모델들에서 기본적으로 활성화하며 Modelfile로는 비활성화할 수 없는 추론을 끕니다. 여섯 단어로 된 문장에서 측정한 결과, 이 옵션이 없으면 추론에 919 tokens와 68초가 걸렸지만 옵션을 사용하면 9 tokens만 사용했습니다.

### 400개가 넘는 모델로 연결: `--use_openrouter`

OpenRouter는 하나의 크레딧으로 사용량에 따라 요금을 부과하며 타사가 호스팅하는 모델로 요청을 전달하는 라우터입니다. 여기에는 다른 어떤 provider도 제공하지 않는 중국산 오픈 모델도 포함됩니다.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`는 필수입니다. 요금이 부과되기 전에 실행되는 preflight가 라우팅의 두 가지 특성을 처리합니다.

- **같은 모델도 출력 한도가 서로 다른 수십 곳의 호스팅 업체에서 제공합니다.** `z-ai/glm-5.3-flash`에는 출력이 2,048 tokens로 제한된 곳을 포함해 23개 업체가 있습니다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽고 출력 한도가 8,000 tokens 미만이거나 상태가 저하된 업체를 제외한 뒤, 나머지를 `allow_fallbacks: false`로 고정합니다.
- **추론은 출력 요율로 과금됩니다.** `z-ai/glm-5.2`의 “확인” 응답에서 일반 출력은 2 tokens였지만 추론에는 107 tokens가 들었습니다. 추론은 기본적으로 비활성화됩니다. 추론을 강제하는 모델에는 해당 모델이 허용하는 가장 낮은 노력 수준을 적용합니다. 카탈로그 기본값을 사용하면 번역이 끝나기 전에 출력 한도를 모두 소진할 수 있습니다. `--reasoning_effort`가 지정되어 있으면 항상 우선합니다.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 컨텍스트 창은 카탈로그에서 가져옵니다. 16,400 tokens 미만인 모델은 호출 전에 거부됩니다. prompt와 세그먼트에 8,400, 출력에 최소 8,000이 필요합니다.
- 카탈로그에 없는 slug, 접속할 수 없는 카탈로그 또는 한도를 충족하는 호스팅 업체의 부재는 명령을 중단시킵니다.
- 출력이 비어 있는 `finish_reason=length`는 잘린 응답이 아니라 추론에 소모된 예산입니다. 메시지에서 두 경우를 구분합니다.
- `--eco`는 아무 효과가 없습니다.
- 변수: `OPENROUTER_API_KEY`(<https://openrouter.ai/keys>), `OPENROUTER_BASE_URL`(기본값 `https://openrouter.ai/api/v1`, `https://` 필수), `OPENROUTER_TIMEOUT`(기본값 900), `OPENROUTER_PREFLIGHT_TIMEOUT`(기본값 30).

### 번역 주석

`--add_translation_note`는 `bottom`(기본값), `top`(front matter 다음) 또는 `both`(`--note_position`) 위치에 주석을 추가합니다. 형식은 `legacy`(굵은 문단, 기본값) 또는 `marker`(`--note_format`)입니다. `marker` 형식은 보이지 않는 Markdown 참조 정의인 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` 뒤에 굵은 인용문이 오는 방식입니다. GitHub에서 읽을 수 있고 빌드 시 remark plugin으로 처리할 수 있습니다.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 상세 측정 결과

모든 측정은 `aipmt`를 사용해 실제로 실행한 14개 언어 번역입니다: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi. **기록됨**은 보호 검사를 통과해 파일이 기록된 경우를 뜻하고, **차이 없음**은 `scripts/compare_structure.py`에서 아무 차이도 발견하지 못한 경우를 뜻합니다. 섹션, 소제목, 링크, 고유 URL, 코드 블록, 인라인 코드, 표 행, 인용 블록 및 굵은 단어의 수가 모두 같다는 의미입니다.

“차이 없음”은 “아무것도 감지되지 않음”을 뜻할 뿐 “동일함”을 뜻하지 않습니다. 비교기는 요소의 내용을 읽지 않고 개수만 셉니다. 따라서 삭제된 수준 4 제목, 바뀐 인라인 코드 텍스트, 교체된 깃발, 괄호가 하나 더 붙어 아무 곳에도 연결되지 않는 내부 링크인 `[texte]((#ancre))`를 감지하지 못하며 언어의 적절성도 판단하지 않습니다.

### 밀도 높은 모니터링 기사, `--news` 모드

[jls42.org의 AI 모니터링](https://jls42.org/fr/news) 한 호를 사용했습니다. 589줄, 링크 140개, 섹션 21개, 보호된 영어 인용문 3개로 구성되며, 2026년 9월 4일과 5일에 측정했습니다.

| 모델                                          | 접근 방식              | 기록됨 | 차이 없음   | 언어당 중앙값 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1분 18초     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 구독  | 14/14   | ✅ **14/14** | 3분 59초     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 구독  | 14/14   | ✅ **14/14** | 3분 14초     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3분 37초     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 구독 | 14/14   | ✅ **14/14** | 11분 28초    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5분 37초     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26분 23초    |
| `sonnet` (`--use_claude_code`)                  | Claude 구독  | 14/14   | ⚠️ 13/14     | 6분 49초     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6분 31초     |
| `haiku` (`--use_claude_code`)                   | Claude 구독  | 14/14   | ⚠️ 11/14     | 15분 54초    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2분 54초     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6분 00초     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9분 27초     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10분 09초    |
| `ollama/gpt-oss-20b-32k`                        | 로컬              | 10/14   | ❌ 7/14      | 12분 39초    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5분 32초     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37분 27초    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 구독    | 1/14    | ❌ 1/14      | 23분 11초    |
| `opus` (`--use_claude_code`)                    | Claude 구독  | 0/14    | ❌ 0/14      | —              |

Grok는 9월 9일에 같은 모니터링의 다른 호(356줄)를 대상으로 다시 측정했습니다. 14개 언어 중 9개가 기록되었고 8개는 차이가 없었습니다. 맨 위 표에는 이 수치가 반영되어 있습니다. 중단된 캠페인 세 건은 포함하지 않았습니다. `qwen3.5-27b`(9개 언어)과 `kimi-k2.6`(4개 언어)은 크레딧이 부족했고, `z-ai/glm-5.3-flash`의 두 실패는 provider가 현재 수정 중인 추론 설정에서 비롯되었습니다. OpenRouter 행은 `--use_openrouter` 이전에 라우터의 기본 설정으로 측정했습니다. 함께 제공되는 provider로 `z-ai/glm-5.2`을 다시 측정한 결과도 동일하게 14/14였습니다. 수치는 9월 10일에 현재 비교기로 다시 계산했습니다. `qwen3.8-flash`과 `qwen3.7-flash`은 최초 공개 결과보다 각각 한 언어씩 늘었으며, 나머지는 그대로입니다.

`--use_antigravity` 행은 9월 26일에 같은 기사를 대상으로 번역 네 개를 병렬로 실행해 측정했습니다. 오전에는 `gemini-3.7-flash-medium`, 오후에는 `gemini-3.8-flash-medium`을 사용했습니다. 영어 번역에서 두 모델 모두 인용문 아래의 프랑스어 번역 세 줄을 스스로 제거했고 깃발을 만들어내지 않았으며, 영어 인용문은 온전히 보존되었습니다. 따라서 대체 정리 기능이 할 일은 없었습니다. `--eco`(`gemini-3.7-flash-low`)에서는 네 개 언어(en, ja, ar, hi)만 측정했습니다. 4개 모두 기록되었고 모두 차이가 없었으며 중앙값은 1분 52초였습니다. 같은 날 더 최근인 9월 25일자 모니터링 호(438줄, 영어 인용문 2개)를 대상으로 블로그 외부에서 `gemini-3.7-flash-medium`를 사용해 대조 실험을 진행했습니다. 14개 언어가 모두 기록되었고 모두 차이가 없었으며 언어당 87~128초가 걸렸습니다.

`--use_claude_code` 행은 9월 26일에 같은 기사를 대상으로 `low` 노력 수준에서 번역 네 개를 병렬로 실행해 측정했습니다. `sonnet`에서는 14개 언어 모두 영어 인용문이 온전히 보존되었고, 영어 번역에서는 모델이 프랑스어 번역 줄을 스스로 제거했으며 깃발을 만들어내지 않았습니다. `opus`은 어떤 언어도 기록하지 못했습니다. 각 언어에서 결합 부위를 위해 생성된 분자 279개를 다룬 짧은 기사 때문에 마지막 세그먼트에서 보호 장치가 응답을 중단했습니다. 이 짧은 기사만 따로 전송해도 “생물학” 범주로 거부되었지만 `sonnet`는 모든 언어로 번역했습니다. `haiku`은 14개 언어를 모두 기록했으나 세 개 언어(en, pl, ro)에서 섹션 제목 하나가 수준 2에서 수준 1로 바뀌었습니다. 막을 수 없는 추론이 출력 tokens의 61%를 차지했기 때문에 `sonnet`보다 두 배 넘게 오래 걸렸습니다.

`claude-sonnet-5-5`, `claude-haiku-5-5` 및 `claude-haiku-4-5` 행은 10월 18일에 Anthropic API를 통해 같은 기사를 대상으로 모델별로 번역 네 개를 병렬 실행해 측정했습니다. Sonnet 5.5는 추론 비활성화를 거부합니다. aipmt는 이 모델이 허용하는 가장 낮은 설정을 전송하며, 응답에는 추론 내용이 전혀 포함되지 않습니다. 14개 언어를 모두 차이 없이 기록했고 어떤 세그먼트도 다시 처리하지 않았습니다. 영어 번역에서는 프랑스어 번역 줄을 스스로 제거했으며 깃발을 만들어내지 않았고, 영어 인용문은 모든 언어에서 온전히 보존되었습니다. Haiku 5.5는 적응형 추론을 사용해 측정했습니다. 추론을 끄면 프랑스어 문단 전체를 그대로 남겨 보호 검사에서 거부되었으며, 14개 언어 중 3개만 기록되었습니다. 두 Haiku 모두 같은 짧은 기사에서 문제를 일으켰습니다. Haiku 5.5는 일본어, 한국어 및 중국어에서 제목 수준을 바꾸거나 제목을 중복 생성했고, Haiku 4.5는 일곱 개 언어에서 제목을 수준 1로 바꾸었으며 일본어 번역에서는 프랑스어로 남겼습니다. 두 문서를 14개 언어로 번역하는 비용은 Haiku 4.5가 3.67달러, Haiku 5.5가 0.57달러, Sonnet 5.5가 9.21달러였습니다.
### 이 프로젝트의 README, 표준 Markdown

2026년 9월 9일에 고정된 리비전: 785줄, 인라인 코드 285개, 블록 닫기 40개, 표 89줄. 번역 4개를 병렬로 실행했습니다.

| 모델                                            | 작성됨 | 차이 없음 | 언어당 중앙값 | 차이점                                                                   |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1분 43초       | 없음                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1분 48초       | 없음                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4분 02초       | 비교기 기준으로는 없음; 내부 링크 중복(en)                               |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1분 18초       | 없음                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2분 06초       | 없음                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36초           | 굵게 표시된 단어 하나(ja)                                                |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1분 22초       | 굵게 표시된 단어 하나(ko)                                                |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2분 20초       | 표 한 줄이 이전 줄에 붙음(ar)                                            |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2분 56초       | 링크 하나(sv), 굵게 표시된 단어 하나(zh)                                 |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6분 46초       | 굵게 표시된 단어 하나(ar, ja)                                            |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2분 34초       | 굵게 표시된 단어 하나(hi, ja, ko)                                        |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2분 17초       | 아랍어에 인라인 코드 40개 추가; 굵게 표시된 단어(hi, ja, ko)             |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1분 14초       | 2개 언어 거부(ar, hi): 반환 과정에서 인라인 코드 유실                     |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2분 44초       | 섹션 하나 유실(ar, hi, ko); 코드 블록 추가(ja, ko, ro, zh)                |

중단된 두 번의 실행은 평가하지 않았습니다. Grok은 12개 언어 이후 CLI 세션이 만료되었고(그중 11개는 차이 없음), `qwen3.8-flash`은 두 번 실행한 뒤 호스팅 제공업체에서 HTTP 429가 발생했습니다. `opencode/mimo-v2.5-free`과 `ollama/gpt-oss-20b-32k`은 이 리비전에서 다시 측정하지 않았습니다. 277줄 더 짧았던 9월 4일과 5일의 리비전에서는 각각 14개 언어 중 9개 번역을 작성했으며, 그중 차이가 없었던 번역은 각각 7개와 1개였습니다.

`--use_antigravity`과 `--use_claude_code` 행은 고정된 리비전에서 측정하지 않고 9월 26일에 1.14.0과 함께 공개된 리비전에서 측정했으며, `claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-haiku-4-5` 행은 10월 18일에 같은 리비전에서 측정했습니다. 해당 리비전은 600줄, 인라인 코드 257개, 블록 닫기 30개, 표 85줄입니다. 185줄 더 짧기 때문에 다른 행과 항목별로 직접 비교할 수 없지만, 이 행들끼리는 서로 비교할 수 있습니다. 비교기가 검사하지 않는 내부 링크의 경우 `gemini-3.8-flash-medium`은 14개 언어 모두에서 링크를 온전히 유지했고, `gemini-3.7-flash-medium`은 이탈리아어에서 링크를 깨뜨렸습니다. `sonnet`와 `opus`은 모든 언어에서 링크를 온전히 유지했고, `haiku`은 영어에서 링크를 중복시켰습니다. `claude-sonnet-5-5`과 `claude-haiku-4-5`은 14개 언어 모두에서 링크를 온전히 유지했으며, `claude-haiku-5-5`은 작성한 12개 언어에서 모두 온전히 유지했습니다.

### 잘 알려진 프로젝트의 README 네 개

GitHub에서 원문 그대로 가져온 FastAPI, Ollama, tldr-pages, Vue.js의 README로, 앞선 두 문서보다 쉬운 문서들입니다. 이 실행은 어려움을 겪은 모델을 대상으로 했으며, Gemini는 비교 기준으로 사용했습니다.

| 모델                      | 범위                       | 작성됨 | 차이 없음    |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 프로젝트 4개 × 언어 14개   | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 프로젝트 4개 × 언어 14개   | 55/56   | ❌ 47/56     |
| `grok-4.6` (구독)   | 프로젝트 4개 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 프로젝트 4개 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 이 측정 결과가 의미하지 않는 것

- **포괄적인 순위가 아닙니다**: OpenRouter에서만 400개가 넘는 모델을 제공하며, 측정한 모델은 약 15개입니다.
- **소요 시간은 참고치입니다**: 실행에 따라 번역 3~6개를 병렬로 처리했으며, 제공업체의 처리량은 하루 중에도 달라집니다.
- **특정 시점의 관찰 결과입니다**: 모델은 같은 이름으로도 변경되며, 여러분의 문서는 저희 문서와 다릅니다.

여러분의 문서에서 측정을 재현하려면 고정된 파일 사본에서 다음을 실행하십시오.

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

두 줄 모두 필요합니다. `pip install -e .`이 없으면 `python -m aipmt`은 `No module named aipmt`이라고 응답합니다.

선택 사항이지만 권장되는 품질 관리 도구:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

저장소의 번역 28개(README와 CHANGELOG, 14개 언어)는 `./regen_translations.sh --force`으로 다시 생성됩니다. 기본 ChatGPT 구독에서 Codex와 `gpt-5.6-sol`을 사용하며, 4개를 병렬로 처리합니다. `REGEN_PROVIDER`과 `REGEN_MODEL`은 경로를 변경합니다. `antigravity`은 Google 구독을 그대로 사용하며 별도 허용 없이 실행됩니다. 유료 API(`openai`, `gemini`, `grok`, `openrouter`)는 `REGEN_ALLOW_PAID_API=1` 없이는 거부됩니다. `REGEN_JOB_TIMEOUT`은 각 작업의 상한을 설정합니다(600초, Codex와 Antigravity에서는 1,800초). 도구에 관한 자세한 내용은 `CLAUDE.md`에 있습니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** — 15개 언어로 게시되는 개인 블로그입니다. 이 도구로 매일 번역되는 [일일 AI 동향](https://jls42.org/fr/news)은 위 측정의 기준 문서로도 사용됩니다.

## 작성자

Julien LE SAUX  
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)를 참조하십시오.

## 경고

이 프로그램은 GPL v3의 제15조 및 제16조에 따라 **어떠한 보증도 없이** 배포됩니다. 상품성이나 특정 목적에 대한 적합성 보증 없이 « 있는 그대로 » 제공되며, 작성자는 사용으로 인해 발생하는 손해에 대해 책임지지 않습니다. 라이선스 원문이 이 요약보다 우선합니다.

- **게시하기 전에 검토하십시오.** 보호 기능은 코드 블록, 인라인 코드, URL, 앵커, `--news` 모드의 인용문에 적용되며, 제목, 표, front matter 또는 문장의 의미에는 적용되지 않습니다.
- **여러분의 문서는 선택한 제공업체로 전송되며**, 해당 업체의 이용 약관과 데이터 정책이 적용됩니다. 일부 무료 모델은 여러분의 대화를 학습에 재사용할 수 있으며, Antigravity의 약관은 유료 구독을 포함해 Google이 대화를 재사용하고 사람이 검토하게 할 수 있도록 허용합니다. 컴퓨터 외부로 데이터를 전혀 내보내지 않는 유일한 방법은 로컬 모델을 사용하는 것입니다.
- **API 호출 비용은 여러분에게 청구됩니다.** 이 프로그램은 지출 상한을 설정하지 않습니다. 긴 문서, 실패 후 재시도 또는 추론을 많이 하는 모델에는 더 많은 비용이 듭니다.
- **공개된 측정 결과는 특정 시점의 관찰 결과일 뿐**, 보증이 아닙니다.

언급된 제품명과 회사명은 각 소유자의 자산입니다. 이 프로젝트는 그 어느 곳과도 제휴되어 있지 않습니다.

**gpt-5.6-sol을 사용하여 프랑스어에서 한국어로 번역된 기사.**
