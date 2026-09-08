### 변경 로그

🌍 [프랑스어](CHANGELOG.md) | [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`: 중국의 공개 모델을 포함해 약 430개 모델로 연결되는 유료 라우터(2026-09-05):

  - **여덟 번째와 함께 제공되는 아홉 번째 provider 경로입니다.** 1.12.0은 PyPI에 게시되지 않았으며, OpenCode와 OpenRouter 두 라우터가 함께 출시됩니다. [OpenRouter](https://openrouter.ai)는 단일 사용량 기반 크레딧과 하나의 키로 다른 어떤 provider도 여기서 제공하지 않는 Kimi, Qwen, DeepSeek, Z.ai 등의 모델에 접근할 수 있게 합니다. endpoint가 OpenAI와 호환되므로 client는 xAI와 동일합니다. **이 provider를 구별하는 모든 것은 preflight에 있으며**, 각 규칙은 API에서 측정한 결과를 바탕으로 합니다.

  - **동일한 모델이 서로 다른 한도를 가진 수십 개의 호스팅 업체에서 제공되지만, 라우팅은 이를 고려하지 않습니다.** 측정 결과 `z-ai/glm-5.2`에는 33개, `z-ai/glm-5.3-flash`에는 23개의 호스팅 업체가 있으며, 그중 하나는 **출력이 2,048 tokens로 제한**됩니다. 따라서 23개 중 하나로 보내진 긴 번역이 아무 신호도 없이 무작위로 잘렸습니다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽고 출력 한도가 8,000 tokens 미만인 업체, 상태가 저하된 업체, 한도를 전혀 선언하지 않은 업체를 제외한 뒤 나머지를 고정합니다. `allow_fallbacks: false` **없는** `provider.only`은 선호 설정에 불과합니다. 라우터가 제외된 호스팅 업체로 되돌아가므로 고정은 아무 의미가 없어집니다. 한도를 충족하는 호스팅 업체가 하나도 없으면 명령이 중단됩니다. 그대로 번역하는 것은 이 preflight가 방지하려는 조용한 잘림을 받아들이는 것과 같기 때문입니다.

  - **추론은 출력 요금으로 청구되며 많은 모델에서 기본적으로 활성화됩니다.** `z-ai/glm-5.2`에 동일한 요청을 보내 “OK”라는 응답을 받은 결과, **모델 기본값에서는 completion tokens가 107개였고 추론을 끄면 2개였습니다**. 추론이 아무 도움도 되지 않는 번역에서는 모든 파일의 모든 segment마다 18배의 차이가 납니다. 따라서 기본적으로 비활성화됩니다. 추론을 강제하는 **431개 중 288개 모델**(`reasoning.mandatory`)은 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`로 응답합니다. 이러한 모델에 대해서는 preflight가 허용되는 effort를 읽고 가장 낮은 값을 요청합니다(다음 항목). effort는 추론이 먼저 소비하는 **`max_tokens`의 일정 비율**을 할당하므로, 임의의 값을 선택하면 빈 페이지가 발생할 위험을 줄이는 대신 옮겨 놓을 뿐입니다.

  - **추론을 강제하는 모델에는 해당 모델이 허용하는 가장 낮은 effort가 지정되며, 이는 측정을 통해 결정되었습니다.** 처음에는 모델 대신 추측하지 않기 위해 아무것도 보내지 않는 방식을 선택했습니다. catalogue 기본값이 `max`인 `z-ai/glm-5.3-flash`에서 검증한 결과, 이 선택은 번역이 끝나기 전에 **32,768 tokens에서 잘린 출력**을 생성했고 14개 언어 중 2개가 유실되었습니다. envelope를 늘려도 달라지는 것은 없었을 것입니다. effort가 그중 일정 비율을 할당하므로 추론도 함께 늘어나기 때문입니다. 따라서 provider는 preflight에서 `supported_efforts`을 읽고 가장 낮은 값을 요청하며, catalogue가 사용 가능한 값을 하나도 알리지 않으면 “없음”으로 fallback합니다. 문제가 발생했던 언어로 대조 검증한 결과, 이전에는 budget 소진으로 실패했지만 이제는 원본과 동일한 구조로 9분 만에 완료됩니다.

  - **이제 upstream 호스팅 업체의 장애에는 해당 업체의 이름이 표시됩니다.** 라우터는 이 경우를 null인 `native_finish_reason`가 포함된 `finish_reason=error`으로 정규화합니다. 두 언어에서 정확히 750초로 두 번 측정되었습니다. 기존의 일반적인 메시지는 문서나 분할 방식에서 문제를 찾게 했지만, 이제는 공급자 측 장애이며 재시도만으로 해결되는 경우가 많다고 알려 줍니다.

  - **출력이 비어 있는 `finish_reason=length`은 잘림이 아닙니다.** 이는 유용한 첫 글자가 나오기 전에 추론이 budget을 모두 소비한 경우입니다. 유용한 tokens 148개에 추론 tokens 15,850개가 사용된 것으로 측정되었습니다. 두 경우에는 정반대의 조치가 필요합니다. 첫 번째 경우에는 segment 크기를 줄여도 아무 소용이 없습니다. 메시지는 두 경우를 명시적으로 구분합니다. 측정 결과를 바탕으로 두 가지 guard도 추가되었습니다. upstream 호스팅 업체가 실패하면 라우터는 **오류만 담긴 본문과 함께 200으로 응답**하며(`choices[0]`은 메시지를 가리는 불투명한 `TypeError`을 발생시켰습니다), context window는 catalogue에서 읽어 `MODEL_TOKEN_LIMITS`에 기록됩니다. `DEFAULT_TOKEN_LIMIT`은 catalogue의 44개 모델에서 잘못되어 있으며, 그중 2개는 4,095 tokens로 제한됩니다.

  - **`--model fournisseur/modèle`은 필수이며 네트워크에 접근하기 전에 형식을 검증합니다.** OpenRouter는 공급자가 아닙니다. 모델 선택은 가격, 라이선스, 데이터 처리 방식에 영향을 미치므로 사용자를 대신해 결정할 수 없습니다. slug가 preflight URL에 삽입되므로 검증은 단순한 사용성 배려가 아니라 경로 삽입을 막는 guard입니다. 두 라우터가 공유하는 namespace regex는 `a/b/..`을 허용하므로 parent segment를 명시적으로 거부합니다. `--eco`은 아무 효과가 없으며 이를 알립니다.

  - **잘못된 내용 하나를 포함해 세 가지 표현을 바로잡았습니다.** `codex exec`에 대한 OpenAI의 경고는 공개 저장소 자체가 아니라 공유 runner에 개인 session 파일을 삽입하는 행위를 대상으로 했지만, README와 CLAUDE.md, 코드에서 그 의미가 반대로 인용되어 있었습니다. OpenCode의 인증 위치는 1.18.27에서 `auth.json`이 아니라 `opencode.db`의 `credential` 테이블로 변경되었습니다. “여기서는 절대 읽지 않는다”는 invariant는 여전히 맞았지만 주소가 오래되었습니다. 마지막으로 OpenCode 섹션에서는 검증되지 않은 경로를 더 이상 동등한 것으로 소개하지 않습니다. Zen gateway와 Ollama는 end-to-end로 측정했지만 GitHub Copilot, LM Studio, llama.cpp는 측정하지 않았으며, 이제 README에 그 사실이 명시됩니다.

  - **측정 캠페인과 README의 권장 모델 표입니다.** 세 가지 문서 세트, 즉 `--news` 모드의 밀도 높은 블로그 글, 표준 Markdown 형식의 이 README, GitHub에서 가져온 유명 프로젝트 README 4개를 그대로 사용해 14개 언어로 300회 넘는 번역을 실행했습니다. 표에서는 혼동되던 두 가지, 즉 번역이 **완료되는지**와 번역의 **구조가 원본과 동일한지**를 구분합니다. 밀도 높은 두 문서에서 단 한 번도 정보를 잃지 않은 모델은 세 개였습니다. `gemini-3.7-flash`, ChatGPT 구독의 `gpt-5.6-sol`, OpenRouter를 통한 `z-ai/glm-5.2`이며, 유일한 차이는 한두 언어에서 `**` 한 쌍이 반영되지 않은 것입니다. 핵심 관찰은 **구별 요인이 `--news` 모드가 아니라 문서의 밀도**라는 점입니다. 구독형 Grok은 블로그 글에서는 14번 중 13번 실패했지만 공개 README에서는 16번 중 14번 성공했으며, 대조 검증 결과 원인은 긴 segment에서 맥락을 놓치는 현상이었습니다. 표에는 자체 경고도 포함되어 있습니다. 표는 포괄적이지 않고 특정 시점의 결과이며, 소요 시간은 순위를 의미하지 않습니다. 올바른 접근법은 여전히 자신의 문서로 직접 측정하는 것입니다.

  - **구조 비교기가 비라틴 문자를 사용하는 표기 체계에서 두 건의 false positive를 생성했기 때문에 수치를 공개하기 전에 수정했습니다.** 전각 닫는 괄호 `）`이 뒤따르는 URL은 `)`에서 멈추는 regex로 잘리지 않았고, URL 자체는 같았지만 추출된 문자열은 달랐습니다. 또한 프랑스어로 5줄인 인용문이 중국어에서는 3줄이 되면서 줄 단위 개수가 줄었습니다. 두 수정 사항은 대조 검증을 거쳤습니다. URL, section 또는 inline code를 삭제하면 여전히 감지됩니다. 이 수정이 없었다면 Gemini와 Codex의 결과는 14개 언어 중 각각 13개와 12개가 아니라 11개로 공개되었을 것입니다.

  - **테스트**: 새로운 파일 `tests/test_openrouter_provider.py`(60개 테스트) — 모델 검증 및 parent segment 거부, 호스팅 업체 고정(한도, 상태, 미선언 한도, 공통 최솟값), 항상 false인 `allow_fallbacks`, `mandatory`에 따른 추론 비활성화 또는 유지, 완전한 출력 계약(200 응답 내부의 오류, 선택지 없음, 잘림과 구분되는 빈 페이지, 비정상적인 `finish_reason`, null 콘텐츠), catalogue에 연결할 수 없을 때 fail-closed로 동작하는 preflight, 누락된 slug 및 정상 호스팅 업체 부재, flag의 상호 배타성과 파일 이름 label을 검증합니다. 전체 suite는 **473개 테스트**입니다.

  - **리팩터링: 동작을 단 한 줄도 바꾸지 않고 4,253줄짜리 단일 module을 여러 module로 분리했습니다.** `src/aipmt/translate.py`을 `config`, `markdown`, `segmentation`, `guards`, `placeholders`, `news`, `prompts`, `notes`, `naming`, `pipeline`, `cli` 및 하위 package `providers/`로 나눴습니다(provider별 module 하나, 기반 역할의 `base`, resolution과 dispatch를 담당하는 `registry`). 각 이동은 기계적으로 검증되는 commit입니다. verifier가 package 내 모든 최상위 node의 AST를 reference snapshot과 비교하고, 각 symbol의 위치, 보안 marker가 글자 그대로 유지되었는지, 추적되지 않은 파일이 없는지를 확인합니다. 이 임시 도구는 다음 버전에서 제거되었습니다. 눈에 보이는 변경 사항은 다음과 같습니다. `aipmt.translate`은 `_` prefix 없이 기존 module이 노출했던 64개 이름을 객체 identity를 유지한 채 다시 노출하는 façade가 됩니다(`__all__`에는 지원되는 API인 9개가 있고 나머지는 호환성 alias입니다). 또한 `import *`이 수집하던 dependency 및 표준 library의 이름 29개를 더 이상 다시 export하지 않습니다. 파일의 직접 실행(`python src/aipmt/translate.py`)은 더 이상 지원되지 않으며 `aipmt`와 `python -m aipmt`이 지원되는 두 가지 형식으로 유지됩니다. public 함수의 `__module__`은 해당 함수를 정의한 module의 값입니다. SDK는 `.env`을 불러온 뒤 import되며 이전처럼 그보다 먼저 import되지 않지만, 알려진 영향은 없습니다. 427개 테스트의 identifier를 그대로 보존하면서 테스트 대상 module로 옮겼습니다. façade를 거치던 patch 91개는 이제 이름을 조회하는 module을 대상으로 합니다(이 중 2개는 patch가 없어도 통과한다는 것을 측정했습니다). contract 테스트 7개가 façade를 고정하며, 어떤 gate도 검사를 중단한 결과로 통과할 수 없도록 첫 이동 전에 gate 도구를 다시 작성했습니다. 여기에는 최솟값이 있는 디렉터리 단위 Lizard scope, 생성된 parser에서 읽는 flag, package 단위 coverage 최솟값, 추적 중인 module을 열거하는 `release.sh`이 포함됩니다.
  - **수정(pull request 검토)**: OpenRouter는 `context_length`이 없는 catalogue 항목에 측정값처럼 기본값 128,000 tokens를 기록하는 대신 해당 항목을 거부합니다. 기존 동작은 “목록에 없는 모델” 경고까지 비활성화했습니다. 또한 `finish_reason`이 null일 때(문서화된 type은 `string | null`)는 호스팅 업체의 원래 사유를 따르며, `max_tokens`은 `length`입니다. OpenCode는 `part: null` event에 대해 `AttributeError`이 아니라 자체 contract 오류로 응답하며, event line 하나를 읽을 수 없는 JSONL stream을 부분 text로 받아들이지 않고 거부합니다. 세 agentic CLI는 호출 중 해당 process가 `SIGTERM`을 받으면 agent group을 종료합니다. regen의 `timeout`는 agent가 살아남아 quota를 계속 소비하게 했습니다. 또한 정상적으로 종료되는 shim이 grandchild를 살려 두는 경우에도 group의 `SIGKILL`은 항상 grace period를 따릅니다. 분리 과정에서 나뉜 `# fmt: off` / `# fmt: on` 쌍을 다시 결합했습니다. `--reasoning_effort`의 help에는 이를 사용하는 provider 네 개가 명시됩니다.

- **1.12.0** Provider `--use_opencode`: 오픈 소스 agent인 OpenCode를 통해 사용자가 선택한 공급자로 연결 — 로컬 모델, 계정 없이 무료 사용, 구독 또는 키(2026-09-04):

  - **앞선 일곱 경로와는 성격이 다른 여덟 번째 provider 경로입니다.** [OpenCode](https://opencode.ai)(MIT)는 모델 공급자가 아니라 사용자가 OpenCode 자체에서 설정한 대상으로 연결하는 _라우터_입니다. 대상은 API 키, 구독(GitHub Copilot, ChatGPT, SuperGrok), **계정 없이** 무료 모델을 제공하는 OpenCode Zen gateway 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp)일 수 있습니다. script는 Codex와 Grok을 제어할 때처럼 비대화형 모드로 `opencode run`을 제어하며, 동일한 subprocess 기반을 재사용합니다(독립된 process group, timeout 시 `SIGTERM` 후 `SIGKILL`, 항상 닫힌 stdin, 정리된 environment). **실제 번역 두 건**으로 검증했습니다. `opencode/mimo-v2.5-free`을 통해 이 README 전체를 영어로 번역한 작업은 49초가 걸렸고 한 번의 pass로 완료되었으며, 원본 파일과 구조가 동일했습니다(제목 32개, code 종료 marker 26개, link 18개, URL 37개, table line 37개, inline code 135개). 또한 로컬의 `ollama/qwen2.5:7b`을 사용해 아무 키 없이 테스트 파일을 번역했습니다.

  - **`--model provider/modèle`은 필수이며 이는 사용자가 내려야 할 선택입니다.** `--model`이 없으면 OpenCode는 자체 기본값으로 fallback하며, 새로 설치한 환경에서는 대화 내용이 학습에 사용될 수 있는 무료 “stealth” 모델 `opencode/big-pickle`입니다. 측정 결과 실제로 이 모델이 응답했습니다. 사용자를 대신해 이를 조용히 선택하는 것은 이 저장소가 추적하는 바로 그 보이지 않는 전환에 해당합니다. 따라서 오류 메시지에는 모델을 나열하는 명령(`opencode models`)과 로컬, 무료, 구독 방식의 예시 세 가지가 표시됩니다. `--eco`은 아무 효과가 없으며 이를 알립니다. `--reasoning_effort`은 명시적으로 요청한 경우에만 OpenCode의 `--variant`으로 변경 없이 전달됩니다.

  - **가정한 것이 아니라 측정한 격리입니다.** inline 설정(`OPENCODE_CONFIG_CONTENT`은 OpenCode의 병합 순서에서 마지막이므로 사용자 설정을 대체하지 않으면서 우선합니다)은 모든 tool이 거부된(`permission: {"*": "deny"}`) agent `aipmt`을 정의합니다. registry는 tool을 모델에 아예 제안하지 않으며, “파일을 나열하고 `id`을 실행하라”는 지시를 받은 모델은 tool이 없다고 응답합니다. session 공유를 비활성화하고 외부 plugin을 제외하며(`--pure`), `--auto`은 절대 사용하지 않고 비어 있는 일회용 작업 디렉터리를 사용합니다. 조용히 일어나는 injection 두 가지를 측정해 차단했습니다. `OPENCODE_DISABLE_CLAUDE_CODE`이 없으면 사용자의 `~/.claude/CLAUDE.md`이 **모든** prompt에 들어갑니다(단순한 “안녕하세요”의 경우 입력 tokens가 186개에서 515개로 증가). `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 디렉터리의 `AGENTS.md`도 들어갑니다. “모든 응답을 BANANA로 끝내라”는 지시가 번역에 적용되는 것을 확인했습니다. 반면 전역 `~/.config/opencode/AGENTS.md`은 계속 삽입됩니다. 이를 제외하는 switch가 없으며, 변칙적으로 `XDG_CONFIG_HOME`을 사용해 우회하면 사용자의 공급자까지 숨겨집니다. 임시방편으로 손대는 대신 문서화했습니다.

  - **`exit 0`은 아무것도 증명하지 않습니다. 세 번째 CLI에도 같은 원칙을 적용하되, 이 CLI에만 있는 함정 두 가지를 처리했습니다.** 알 수 없는 `--agent`이 있어도 `opencode run`은 실패하지 않습니다. stderr에 경고를 표시한 뒤 tool이 활성화된 coding agent로 **조용히** fallback합니다. 따라서 inline 설정이 적용되지 않았다면 쓰기 권한이 있는 agent가 번역을 수행했을 것입니다. 출력 contract는 return code 0, `error` event 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`임(`length`은 잘린 응답입니다), text가 비어 있지 않음에 더해 이 메시지가 없는지도 검증합니다. 두 번째 함정은 error JSON event가 **불투명**하다는 점입니다. 단순한 reference와 함께 “Unexpected server error. Check server logs for details.”라고만 표시되며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 log에만 존재합니다. 이 때문에 `--print-logs --log-level ERROR`과 stderr의 `error="…"` field를 읽되 뒤따르는 Bun trace는 제외합니다. 따라서 알 수 없는 모델은 원인이 명시된 채 1초 만에 실패합니다. 아울러 `--title`은 불필요한 LLM 호출을 방지합니다. 이것이 없으면 OpenCode가 `small_model`에서 한 번 더 호출해 session 제목을 생성합니다.
  - **Secrets: Codex 및 Grok과 동일한 패턴 필터링을 적용하되, 이름이 지정된 예외 하나만 둡니다.** `OPENCODE_API_KEY`는 유지됩니다. 이는 OpenCode 자체의 키(Zen 게이트웨이, Go 구독)이며, 이름을 통해 OpenCode에 전달되는 키입니다. 즉, aipmt가 관리하거나 요금을 청구할 수 있는 키가 아니라 OpenCode의 `auth.json`에 해당합니다. 공급자는 OpenCode에서 설정하며(`opencode auth login`, `opencode.json`), aipmt의 `.env`에서는 절대 설정하지 않습니다. aipmt의 어떤 키도 하위 프로세스에 도달하지 않습니다. 구독 CLI와 달리 CI에서는 거부하지 않습니다. API 키나 runner에서 자체 호스팅되는 모델은 적법한 사용 방식이기 때문입니다.

  - **이제 경로 순회 방지 장치는 원시 값이 아니라 보간된 값을 검사합니다.** `provider/modèle`에는 1.10.0의 방지 장치가 거부했던 `/`가 포함되어 있습니다. 이는 타당한 동작이었습니다. `--model`이 파일 이름 `--include_model`에 보간되기 때문입니다. 이제 파일 이름 레이블은 보간 전에 `/`, `\`, `:`을 `-`로 바꿉니다(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, `:`은 Windows에서 허용되지 않음). 상위 방지 장치는 이 레이블을 검사합니다. 따라서 `../../evil`는 대상 아래의 단순한 이름 `doc-en-..-..-evil.md`이 되고, `..` 자체는 계속 거부되며 `--target_lang ../x`도 마찬가지입니다. `_ensure_within_directory` 범위 방지 장치는 변경 없이 두 번째 방어 계층으로 유지됩니다.

  - **무료 모델과 로컬 모델에서 실제로 측정한 결과입니다.** `opencode/mimo-v2.5-free`은 문단 하나를 16초, 이 README를 49초에 번역합니다. `opencode/big-pickle`은 200단어에 40초가 걸렸고, 개별적으로는 완료되던 요청 두 개를 동시에 실행했을 때 5분 동안 응답이 없었습니다. `opencode/nemotron-3.5-lightning-free`은 3분 동안 아무 응답도 하지 않았습니다. 따라서 `REGEN_PROVIDER=opencode`에서는 `REGEN_MODEL`가 필수이며 병렬 작업 수는 **2개**입니다. 로컬 환경에서 Ollama는 컨텍스트를 흔히 4,096 tokens로 설정하지만 세그먼트는 최대 16,000자에 이릅니다. 따라서 `PARAMETER num_ctx 32768`을 포함한 `Modelfile`가 필요하며, 품질은 모델에 따라 달라집니다. 시험 파일에서 7B 모델은 목록 순서를 뒤집고 코드 블록 닫기 구문을 훼손했지만, 게이트웨이 모델은 모든 구조를 보존했습니다.

  - **이 저장소의 번역은 이제 유료 API를 절대 거치지 않습니다.** `regen_translations.sh`는 `.env`에 키가 하나라도 남아 있으면 즉시 OpenAI API를 선택했고, Codex는 명시적으로 선택해야만 사용했습니다. 이번 버전을 준비하면서 실제로 바로 그 일이 발생했습니다. 28개 번역은 OpenAI API로 전송되었고, 이어서 힌디어 CHANGELOG는 Gemini API로 전송되었습니다. 사용량에 따라 비용을 지불하지 않으려고 ChatGPT 구독을 사용하는데도 말입니다. 키 자동 감지는 제거됩니다. **기본값은 품질 모델인 `gpt-5.6-sol`을 사용하는 Codex입니다.** `openai`, `gemini`, `grok`은 `REGEN_PROVIDER`뿐 아니라 `REGEN_ALLOW_PAID_API=1`도 요구합니다. 이는 선택이 이루어지는 시점에 규칙이 실제로 적용되도록 이름을 명시한 예외 승인입니다. 알 수 없는 `REGEN_PROVIDER`는 API로 대체되지 않고 실패합니다. 테스트 10개가 기본값, 거부, 예외 승인을 고정합니다. 이번 버전의 28개 번역은 Codex를 통해 다시 수행했습니다.

  - **rate limit에 대한 back-off를 공통화했습니다**(`_retry_on_rate_limit`). Codex와 Grok의 루프는 레이블만 다를 뿐 동일했으며, 세 번째 복사본을 만들면 중복 임계값을 넘었을 것입니다. 세 CLI 오류는 동일한 `_CliCallError`에서 파생됩니다. 테스트 하나가 세 오류 중 어느 하나라도 그 계층을 벗어나는 것을 금지합니다. 그렇지 않으면 공유 루프가 해당 오류를 더 이상 감지하지 못하기 때문입니다.

  - **테스트**: 새 파일 `tests/test_opencode_provider.py`(51개 테스트) — 전체 출력 계약, agent fallback, 로그에서 원인 읽기, 중복 제거된 텍스트 조각과 합성 조각 무시, 프로세스 그룹을 종료하는 timeout, 429 back-off, 필수 모델 및 모델 검증, secret 없는 preflight, 바이너리 해석, dispatch 연결, 파일 이름 레이블 및 경로 순회 반증 시험을 다룹니다. `tests/test_review_hardening.py`은 플래그 상호 배타성과 secret 부재 검사를 새 provider까지 확장합니다. 이제 gate는 문서화된 argparse **플래그 22개**를 요구합니다. 전체 제품군은 **382개 테스트**입니다.

- **1.11.1** 문서 수정: README에 마침내 일곱 가지 provider 경로를 명시했습니다(2026-09-03).

  - **1.11.0의 PyPI 페이지에는 “API 4개 + Codex CLI”라고 적혀 있었습니다.** 실제 코드는 일곱 가지를 제공합니다. OpenAI, Mistral, Claude, Gemini, Grok은 API를 통해 사용하고, Codex(ChatGPT)와 Grok은 사용량 기반 요금 없이 구독으로 사용합니다. 소개 문구와 _Multi-Provider_ 항목에서 Grok의 두 모드가 누락되었고, 14개 번역도 같은 오류를 반복했습니다. 패키지의 긴 설명은 버전별로 고정되므로 공개 페이지를 수정하려면 새 버전 번호가 필요했습니다. 이것이 이 버전의 유일한 존재 이유입니다. **코드 변경은 없습니다.**
  - `CLAUDE.md`은 게시 과정에서 도입된 사항에 맞게 조정되었습니다. gate 카운터(`--full`에서는 16, 17), 활성 workflow 11개, `gh pr checks`에서 보이지 않는 Sonar/Codacy 카운터 2개(hotspots, Codacy API), `ruff-format`에 따른 `# nosemgrep` 이동, OIDC 교환에 필요한 GitHub 환경, 그리고 _pending publisher_가 이름을 선점하지 않는다는 사실을 반영합니다.

- **1.11.0** PyPI 게시: 저장소를 clone하지 않고 `pip install ai-powered-markdown-translator`를 실행한 뒤 `aipmt` 명령을 사용합니다(2026-09-03).

  - **단일 파일 스크립트가 설치 가능한 패키지가 되었습니다.** `translate.py`는 루트에서 `src/aipmt/translate.py`로 이동했으며, console 진입점 `aipmt`과 이에 해당하는 `python -m aipmt`을 제공합니다. 기여하려면 여전히 저장소를 clone해야 합니다. 테스트, 28개 번역, 품질 도구가 저장소에 있기 때문입니다. 하지만 사용하는 데는 더 이상 clone이 필요하지 않습니다.

    - **import 이름은 항상 `aipmt`이며 절대 `translate`가 아닙니다.** 실제로 충돌이 발생하며 아무 경고도 없기 때문입니다. PyPI 패키지 `translate`(v3.8.1, 최근 업로드 2026-07-06)은 같은 이름의 디렉터리를 설치합니다. venv에서 재현한 결과 디렉터리가 모듈보다 우선하고, `translate.main`이 사라지며, 진입점은 `AttributeError`에서 깨집니다. 그런데도 `pip check`은 “No broken requirements found”라고 응답하고 rc=0을 반환합니다. 사용자가 단순히 `pip install translate`만 실행해도 유용한 진단 없이 CLI가 깨질 수 있었습니다. 실제 wheel로 수행한 반증 시험에서는 패키지 위에 `pip install translate`를 설치한 뒤에도 `aipmt --help`이 설치 전후 모두 rc=0을 반환했고, 두 CLI가 공존했습니다.
    - **배포 이름은 길고 명령은 짧습니다.** `ai-powered-markdown-translator` 덕분에 PyPI 검색에서 패키지를 찾을 수 있습니다. 약어만 사용하면 프로젝트를 이미 아는 사람이 아니고서는 찾을 수 없는데, 게시의 목적은 바로 새로운 사용자가 발견하도록 하는 것입니다. 가능성 있어 보이던 후보 두 개는 확인 후 제외했습니다. `ai-markdown-translator`은 동일한 목적의 도구가 2024년부터 npm에서 이미 사용 중이며 이 저장소보다 17개월 앞섭니다. `aimt`은 같은 분야의 활성 패키지 `aim`(v3.29.1)과 한 글자만 다릅니다. 장기적인 혼동을 유발하기에 최악의 조건입니다. 확인 방법에도 함정이 있습니다. `pypi.org/project/<nom>/`은 모든 이름에 대해 200을 반환하는 anti-bot 페이지이므로 JSON API만 신뢰할 수 있습니다.
    - **평면 패키지 대신 `src/` layout을 사용합니다.** 평면 패키지는 테스트의 `sys.path.insert(..., "..")` 여섯 개를 유지할 수 있었겠지만, 바로 그것이 문제입니다. 패키지가 아니라 소스 트리를 import하므로 패키징 오류를 모두 숨길 수 있기 때문입니다. 실제 비용은 치환 규칙 하나를 추가하는 것뿐입니다.

  - **이제 키를 한 번만 설정하면 계속 사용할 수 있습니다.** 설치된 CLI에는 영구적인 설정이 전혀 없었습니다. 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었습니다. `find_dotenv`는 실제로 시스템 루트까지 올라가므로 **사용자 홈 디렉터리 아래에서 작업할 때는** `~/.env`을 찾았지만, 다른 곳에서 작업하면 아무것도 찾지 못했습니다. 이는 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라지는 불완전한 지원이었습니다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`이 추가됩니다.

    - **우선순위는 별도 코드로 구현되지 않았으며**, `load_dotenv`의 기본값인 `override=False`에서 자연스럽게 결정됩니다. 각 계층은 이전 계층이 비워 둔 값만 채웁니다. 따라서 환경 변수 → 프로젝트의 `.env` → 사용자 설정 순서가 되며, 구조가 아니라 동작 테스트로 검증합니다. 두 호출의 순서를 바꾸거나 세 번째 계층을 제거하면 테스트가 실패합니다.
    - **TOML이 아니라 `.env` 형식을 사용한 것은 의도적인 결정입니다.** `python-dotenv`는 이미 의존성이며, 해당 문법은 README 15개에 이미 문서화되어 있고, 같은 파일을 두 범위에서 모두 사용할 수 있습니다. 새로운 의존성이나 문법은 없습니다. 위치는 `XDG_CONFIG_HOME`이 **절대 경로**일 때 이를 따릅니다. 사양에서는 상대 값을 무시하도록 요구하는데, 그렇지 않으면 설정 위치가 다시 현재 디렉터리에 따라 달라지기 때문입니다. Windows에서는 `APPDATA`을 따릅니다.
    - **두 가지 선택지를 이유와 함께 제외했습니다.** 시스템 keyring(`keyring`)은 데스크톱에서는 더 안전하지만 headless 환경, 즉 서버, 컨테이너, CI에서는 실패합니다. 이는 일괄 번역의 핵심 사용 사례와 정확히 겹칩니다. 선택 기능으로는 적합하지만 기본값으로는 부적합합니다. `--api-key` 플래그를 사용하면 키가 shell 기록에 남고 `ps`에도 노출됩니다.
    - **키가 없을 때 더 이상 호출 trace를 표시하지 않습니다.** 이전에는 사용자에게 `site-packages`을 가리키는 Python stack과 “환경 또는 .env”라고만 적힌 메시지를 보여 주었으며, 두 번째 파일을 어디에 생성해야 하는지는 알려 주지 않았습니다. 이제 세 위치와 각각의 정확한 경로를 나열하고 명령은 코드 2로 종료됩니다. 안전망은 **의도적으로 좁게** 설정되어 `except ValueError`가 설정 단계에만 적용됩니다. 실행 전체를 감싸면 번역 중 발생한 실제 버그가 안심시키는 메시지로 둔갑합니다. 이는 이 저장소가 추적하는 바로 그 실패 방식입니다. 테스트는 `main()`의 소스를 읽어 그런 처리를 금지합니다.

  - **수정 — 도구 설치 후 사용자의 `.env`이 무시되던 문제를 해결했습니다.** 인수 없는 `load_dotenv()`는 현재 디렉터리에서 위로 탐색하는 것이 아니라 호출한 파일, 즉 `site-packages`에서 위로 탐색합니다. 자체 `.env`을 가진 프로젝트에서 실제 console 진입점을 실행해 측정한 결과, `find_dotenv()`는 `''`을 반환하여 키를 불러오지 못했지만 `find_dotenv(usecwd=True)`은 이를 찾았습니다. 도구를 clone한 저장소 안에서만 실행할 때는 존재하지 않던 버그입니다. 게시 후에는 올바르게 설정했는데도 API 키가 “없다”는 증상만 보이며 항상 발생했을 것입니다.

  - **세 개의 gate가 아무것도 검증하지 않게 되었는데도 통과할 수 있었습니다.** 그래서 이동 전에 의도적으로 강화했습니다. 잡아내야 할 변경 이후에 작성한 방지 장치만으로는 아무것도 입증할 수 없기 때문입니다. 각 gate는 원래 저장소에서는 통과하고 마이그레이션된 복사본에서는 실패합니다. 양방향 모두 실제로 측정했습니다.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시합니다.** rc=0과 “0 file analyzed”를 반환합니다. 복잡도 gate는 158 functions / 2247 nloc에서 3 functions / 34 nloc로 줄어들면서 출력 파일 크기도 0바이트가 될 수 있었습니다. 이제 scope는 배열이며 각 항목의 존재 여부를 확인합니다.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`은 실패하지 않습니다.** stderr에만 경고하고 unittest와 `coverage xml` 모두 rc=0을 반환하며, statements가 1453개에서 141개로 잘린 보고서까지 그대로 게시합니다. 프로젝트 대부분이 분석되지 않았기 때문에 오히려 정상으로 보였을 것입니다. 두 가지 하한이 보고서를 보호합니다. 전체 수치와 측정된 가장 큰 파일입니다.
    - **번역 최신성 검사는 호출 형식에 구조적으로 무관심합니다.** 파일 이름 변경으로는 달라지지 않는 argparse 플래그를 기준으로 탐색하기 때문입니다. 실제로 모듈을 이동한 뒤에도 README 15개가 존재하지 않는 명령을 계속 안내했지만 판정은 “오래된 번역 없음”이었습니다. 따라서 일곱 번째 섹션은 옵션이 아니라 호출 **형식**을 확인하며, Lizard hook을 스크립트의 실제 scope와 대조합니다. `files:` 키가 더 이상 일치하지 않아도 pre-commit을 실패시키지 않고 해당 검사를 건너뛰기 때문입니다.

  - **`requires-python = ">=3.10"`은 더 이상 근거 없는 주장이 아닙니다.** `sonar-project.properties`는 이미 3.10-3.12 지원을 명시했지만 개발 환경에는 3.12만 있었고, 어떤 테스트도 다른 버전을 실행한 적이 없었습니다. 게시되었다면 이 내부 모순이 외부에 그대로 드러났을 것입니다. 이제 테스트 workflow는 3.10, 3.11, 3.12에서 제품군을 실행하며, **패키지** 자체를 설치하여 공개된 버전 범위까지 검증합니다.

  - **하한만 두고 상한은 두지 않습니다.** `requirements.txt`은 계속 테스트된 lock으로 유지되고, `[project.dependencies]`는 공개 계약이 됩니다. lock의 정확한 버전을 그대로 게시하면 다른 패키지를 함께 사용하는 모든 사용자에게 충돌을 일으킬 수 있습니다. `<N+1` 상한도 두지 않습니다. 그렇게 하면 major 버전 갱신이 늦을 때 release gate를 실패시키는 `check-deps-fresh.sh`과 정면으로 모순되기 때문입니다. 하한 집합은 정상적으로 의존성을 해석하며, 반증 시험 `openai==1.0.0`은 `ResolutionImpossible`로 종료됩니다. 이는 검사가 무엇이든 받아들이는 것이 아니라 실제로 구분한다는 증거입니다. 또한 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지는 것을 방지하는 장치가 있습니다. PyPI는 버전 번호 재사용을 허용하지 않기 때문입니다.

  - **새 venv에서 처음부터 끝까지 검증했습니다.** 약 70 Ko 크기의 wheel에는 `aipmt/*.py`, dist-info, 라이선스만 포함됩니다. `aipmt --help`은 플래그 22개와 함께 rc=0을 반환합니다. `python -m aipmt`는 “usage: \_\_main\_\_.py”가 아니라 “usage: aipmt”를 표시합니다. `pipx` 설치도 정상 작동합니다. 무엇보다도 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행하여 굵게 표시, 목록, inline code, 링크, URL이 보존되고 코드 블록은 번역되지 않음을 확인했습니다. 마이그레이션 전 318개 테스트가 전후 바이트 단위로 동일한 식별자 목록과 함께 통과했습니다. 단순한 “OK”가 아니라 바로 이것이 어떤 테스트도 무력화되지 않았다는 증거입니다. 3계층 설정을 위한 테스트 12개가 추가되어 총 330개가 되었습니다.

- **1.10.0** `--use_codex` provider(ChatGPT 구독 할당량), SDK 및 모델 업데이트, 여러 문단으로 된 news 인용 수정(2026-08-29):

  - **보안 검토 — PR이 도입했지만 모든 경로에서 지키지는 못했던 두 가지 방지 장치**:
    - **Codex preflight가 전체 `.env`을 바이너리에 전달했습니다.** `_codex_preflight`은 `env=` **없이 `subprocess.run`을 호출했습니다**. 따라서 하위 프로세스가 전체 `os.environ`, 즉 `load_dotenv`이 불러온 `.env` 전체를 상속했습니다. 계측된 가짜 바이너리로 측정한 결과, 여섯 provider의 키와 `GITHUB_TOKEN` 하나를 합쳐 **일곱 개의 secret**이 preflight에 도달했습니다. 반면 `env=_grok_env()`을 올바르게 전달한 대응 경로 `_grok_preflight`에서는 **0개**였습니다. 이 불일치는 PR 내부에 있었습니다. 불과 몇 줄 떨어진 곳에 바로 이 invariant를 유지하기 위한 `_strip_secret_env`이 존재합니다. `_codex_env_base()`을 추출해 두 경로가 공유하도록 했으며, 수정 후 측정값은 양쪽 모두 secret 0개입니다.
    - **‘`--deny` fail-closed’ 속성은 실제로 사용된 형식을 포괄하지 못했습니다.** 주석에서는 알 수 없는 prefix의 규칙이 시작을 거부하게 한다는 이유로 Grok confinement 전체를 정당화했습니다. `grok 1.0.13`에서 측정한 결과, 이 검증은 **괄호 형식에만** 존재합니다. `--deny 'CeciNestPasUnOutil(*)'`은 시작을 거부하지만(“unknown tool prefix”), `--deny 'CeciNestPasUnOutil'`은 아무 경고 없이 허용됩니다. 그런데 `GROK_DENY_RULES`은 bare name만 사용했습니다. 따라서 xAI 측에서 도구 이름을 변경하면 아무 신호도 없이 측정된 유일한 confinement 계층이 사라질 수 있었으며, 이는 이미 OS sandbox가 적용되지 않는 환경에서 발생합니다. 이름이 지정된 여덟 규칙은 이제 각각 CLI의 알려진 prefix인지 검증되는 `Prefix(*)` 형식을 사용합니다. catch-all `*`은 허용되는 유일한 형식인 literal 형식을 그대로 유지합니다. 테스트를 통해 검증되지 않는 형식으로 되돌아가는 일을 방지합니다.
    - **그 밖의 항목은 이상 없음이 확인되었습니다**. command injection은 없고(모든 곳에서 list 형식을 사용하며 `shell=True`은 전혀 사용하지 않고, 문서 내용은 stdin 또는 `--prompt-file`을 통해 전달), unsafe deserialization도 없습니다(type guard와 함께 `json.loads`만 사용). path traversal 수정에서는 일곱 개 payload를 대상으로 우회 방법을 찾지 못했으며, `--deny '*'`도 CLI에서 실제로 적용됩니다(workdir 밖을 읽을 때 `DENY_ENFORCED`이 관찰됨).
    - 위에서 추가한 freshness check는 부수적으로 자신의 원칙을 우회하고 있었습니다. PyPI 요청에 실패한 패키지를 조용히 건너뛰어 gate가 통과했습니다. 이제 실제로 비교한 패키지 수를 세며 coverage가 불완전하면 실패합니다.

  - **의존성을 최신화하고, 다시 뒤처지지 않도록 두 가지 안전장치를 추가했습니다**:

    - **지연은 실제였고 장기간 지속되었습니다**. `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22**로 올렸습니다. 모든 provider 호출에서 TLS를 검증하는 root certificate store가 2년이나 뒤처져 있었습니다. 확인된 원인은 **`.github/dependabot.yml`이 존재하지 않았기 때문**입니다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하며, Dependabot은 CVE 대상 의존성에 대해서만 PR을 제안합니다. 따라서 `urllib3`과 `idna`은 bump하면서도 두 SDK가 major version 하나만큼 뒤처지도록 방치한 이유가 설명됩니다.
    - 이전 추론에서 우려했던 것과 달리 **두 major version은 충돌 없이 공존합니다**. `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**로 이동하지만, `mistralai`과 `google-genai`는 `httpx<1`에 남으며 이들은 서로 다른 distribution입니다. 실제 설치 후 **7개 provider 경로 전체**를 end-to-end로 테스트해 확인했습니다. 대상은 OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI이며, 모든 출력에서 inline code와 link가 보존되었습니다. ‘HTTP stack 두 개를 피해야 한다’는 것은 선호 사항일 뿐 blocker가 아니었고, 측정으로 결론을 내렸습니다.
    - **`requirements.txt`은 실제 환경을 설명하지 못했습니다**. `google-auth`, `cryptography`, `opentelemetry` stack이 전혀 선언되지 않은 채 작업 venv에 설치되어 있었습니다. 따라서 fresh install로 테스트 환경을 재현할 수 없었습니다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`은 어디에서도 import되거나 요구되지 않는데도 포함되어 있었으며, `mistralai` 1.x의 잔재였습니다. 이 파일은 direct dependency만으로 구성한 venv의 완전한 closure로 다시 생성했습니다. 새 dependency set에서 `pip-audit`이 보고한 알려진 vulnerability는 없습니다.
    - **`.github/dependabot.yml`**(신규)은 pip과 github-actions의 주간 version update를 활성화합니다. minor와 patch는 하나의 PR로 묶습니다. patch bump마다 PR을 만들면 결국 무시되고, noise는 업데이트의 적이기 때문입니다. **major는 분리**하며 각각 실제 호출을 통한 검증이 필요합니다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 지연이 프로젝트 판정에 드러나게 합니다. Dependabot은 제안할 뿐 보장하지 않으며, PR이 쌓일 수 있습니다. major 지연은 실패, minor 지연은 경고로 처리합니다. gate가 항상 빨간색이면 결국 무시되기 때문입니다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 skip하고 **CI에서는 fail-closed**로 처리합니다. 실행되지 않은 검사는 성공이 아닙니다. 양방향으로 검증했습니다. 수정 전의 정확한 상태(`openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`)를 포착하고, minor 지연에는 경고만 표시합니다.

  - **이 PR의 review에서 도출된 수정 사항** — 다섯 review agent가 diff를 철저히 조사했습니다. 아래 항목은 모두 수정 전에 **측정을 통해 재현**했으며, 그중 두 개는 같은 version에서 앞서 도입된 regression이었습니다.

    - **수정된 regression — `_NEWS_CITATION_REGEX`에 exponential backtracking이 있었습니다.** multi-paragraph 수정에서 반복 내부에 `(?:[ \t]*$|[ \t]+.*)`을 도입했습니다. `[ \t]+`과 `.*` 사이의 공백 분배가 모호하며, 이 모호성이 반복할 때마다 증폭됩니다. pattern과 일치하지 않는 `>   texte` line에서 측정했습니다. 이는 완전히 유효한 Markdown indentation입니다. **14줄에 2,589ms**가 걸렸지만 수정 후에는 0.04ms였으며, 줄 하나를 추가할 때마다 약 9배씩 증가했습니다. `--news` mode에서는 형식에 맞지 않는 긴 blockquote 하나만으로도 원인을 파악할 수 없는 상태에서 job timeout까지 번역이 멈출 수 있었습니다. 이제 반복은 한 번에 line 전체를 소비하며(`\n^>(?![ \t]*—).*`), iteration마다 일치할 수 있는 방법이 하나뿐입니다. 실제 231개 article corpus에서 검증한 결과, capture 차이는 **0개**였고 동일한 citation 423개와 확장된 multi-paragraph body 14개가 그대로 유지되었습니다.
    - **두 provider flag를 동시에 사용하면 아무 경고 없이 사용량 기반 요금이 부과되었습니다.** `--use_codex --use_mistral`이 허용되었습니다. `_select_provider_client`는 Mistral을 먼저 검사하고, `_resolve_provider`은 명시적인 boolean에 우선순위를 주므로 둘 다 Mistral로 수렴했습니다. 사용자는 subscription quota를 요청했지만 아무 경고 없이 usage-based billing을 적용받았습니다. 이는 정확히 `--use_codex`이 방지하도록 만들어진 failure mode입니다. 이제 여섯 provider flag 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경 사항**: 지금까지 조용히 허용되었던 두 provider를 결합한 command line은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 종료 gate는 probe가 crash해도 통과했습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개가 return code를 전혀 확인하지 않은 채 ‘stdout을 capture하고 비어 있으면 결론을 내리는’ pattern을 따랐습니다. exception(이름이 변경된 파일, `FileNotFoundError`)은 stderr에 기록하고 stdout은 비워 두므로 검사가 ‘보고할 내용 없음’이라고 결론 내렸습니다. 이를 방지하려고 작성한 script 내부에서 ‘`exit 0`은 아무것도 증명하지 않는다’는 함정을 그대로 재현한 것입니다. 이제 helper `probe()`은 return code가 0이고 종료 sentinel도 있어야 한다고 강제하며, probe는 marker set이 비어 있으면 결론을 거부합니다. empty set에 대한 assertion은 항상 참이기 때문입니다. 예를 들어 위의 mutually exclusive group을 추가하면서 provider flag가 `*_group` object를 통과하게 되었고, 기존 regex `parser\.add_argument\(`는 더 이상 이를 match하지 못했습니다. **21개 flag 중 6개**가 조용히 범위 밖으로 빠졌지만 gate는 통과했습니다.
    - **secret scan은 provider 6개 중 4개를 놓쳤습니다.** `[A-Za-z0-9]` class는 hyphen을 제외합니다. 따라서 `sk-proj-…`(현재 OpenAI 형식)와 `sk-ant-api03-…`는 두 번째 hyphen에서 끊겼으며, `AIza…`은 대상에 포함되지 않았습니다. pattern을 확장하고 `.secrets.baseline`은 scan에서 제외했습니다. 또한 guard `.env`은 index만 확인하는 `git diff --cached`을 조회했습니다. 따라서 최악의 경우인 **이미 commit된** `.env`은 전혀 나타나지 않았습니다. 이제 `git ls-files`을 조회합니다.
    - **Codex의 ‘token warm-up’은 실제 warm-up이 아니었습니다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`을 건드리지 않으며(mtime과 size가 변경되지 않음), help에는 “Show login status”라고 적혀 있습니다. 그런데도 주석은 token을 ‘한 번, 순차적으로’ refresh해 일회용 rotating token의 동시 refresh 위험을 해소한다고 주장했습니다. 공언된 보호 기능은 존재하지 않았습니다. 이제 주석은 code가 실제로 하는 일을 설명하며, 실질적인 대책은 여전히 `max_jobs=4`입니다. 또한 이 검사는 이전에 무시하던 `CODEX_BIN`을 준수합니다. `PATH`에 `codex`이 없는 환경에서는 ‘인증되지 않음’으로 실패해 잘못된 진단을 내렸습니다.
    - **`.env`은 subshell에서 source되었습니다.** `detect_provider`가 command substitution 안에서 호출되므로 export가 상위 shell로 전달되지 않았습니다. `.env`에 정의된 `GROK_BIN`, `GROK_HOME`, `REGEN_MODEL`은 `main()`에서 수행하는 조회에 보이지 않았고, 올바른 구성에서도 ‘Grok 바이너리를 찾을 수 없음’이라고 결론 내렸습니다.
    - **동시성은 공언한 상한을 50% 초과했습니다.** guard가 README/CHANGELOG pair를 시작한 뒤에 배치되어 있었습니다. 측정된 최대치는 **`max_jobs=2`에서 3**이었습니다. 주간 quota를 Chat/Imagine/Voice와 공유하며 측정할 수도 없는 Grok에서 script가 스스로 정한 상한조차 지키지 못했습니다. 또한 최종 count는 표시만 하고 28과 비교하지 않아 파일 하나가 누락되어도 감지하지 못했습니다.
    - **Grok output contract: 이제 `stopReason`이 없으면 실패합니다.** 공언된 contract에서는 `end_turn`을 요구하지만, code는 ‘`end_turn` **또는 없음**’을 적용했습니다. field가 없는 payload나 CLI 업데이트로 field 이름이 바뀐 payload는 guard를 조용히 no-op으로 만들었습니다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류하지 않습니다. 이는 turn budget이 소진된 상태이므로 재시도해도 같은 결과가 발생하며 90초의 대기 비용만 들기 때문입니다. `quota`도 rate limit marker에서 제외했습니다. `_codex_is_rate_limited`의 docstring이 이미 설명했지만 Grok에서는 적용하지 않았던 이유 때문입니다.
    - **Gemini cascade를 model별로 memoize했습니다.** default model이 `minimal`를 거부하는데도 segment마다 여기서 다시 시작했습니다. 정상 경로에서도 segment마다 400 round trip 비용을 내고 동일한 경고를 다시 출력했습니다. 수백 번 반복되는 warning은 더 이상 읽히지 않으며, 그렇게 mask가 됩니다.
    - **기타**: CI의 거부 메시지가 Codex 전용으로 hard-code되어 `--use_grok_cli` 사용자를 `XAI_API_KEY`이 아니라 `OPENAI_API_KEY`으로 안내했습니다. `provider.capitalize()`은 ‘Grok_cli’와 ‘Openai’를 표시했습니다. subprocess 기반부의 주석은 ‘shim’을 두 CLI 모두에 일반화했지만 Grok 바이너리는 native ELF입니다. 올바른 근거는 ‘자체 하위 프로세스를 spawn하는 agent’입니다. `subprocess`의 SAST finding 12개에는 근거와 함께 `# nosec` / `# nosemgrep` 표시를 추가했습니다. `shell=True`을 사용하지 않는 list 형식이므로 injection은 불가능하며, 문서 내용은 argv를 통해 전달되지 않습니다.
    - **이제 agent subprocess에 어떤 secret도 들어가지 않습니다.** 이름 기반 deny-list는 **billing** invariant만 보호했습니다(`OPENAI_API_KEY` 없는 Codex, `XAI_API_KEY` 없는 Grok). 측정 결과 **다른 일곱 개의 secret**이 각 subprocess에 여전히 들어갔습니다. Anthropic, Mistral, Google, Gemini 키와 다른 CLI의 키, 그리고 secret은 아니지만 traffic을 다른 곳으로 보내는 `OPENAI_BASE_URL`입니다. 그런데 이 두 CLI는 **agent**이며, Grok agent는 많은 Linux 환경에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 filtering은 이름 기반 list가 아니라 **name pattern**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)으로 수행합니다. 따라서 이 code가 알지 못하더라도 사용자가 `.env`에 추가한 variable까지 포괄합니다. CLI에는 이들 중 어느 것도 필요하지 않습니다. 인증 정보는 환경 변수가 아니라 `~/.codex`과 `~/.grok`에 저장됩니다. 강화된 환경에서 두 provider 각각을 통해 **실제 번역을 성공적으로 완료**해 검증했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`에 21개 test를 추가해 provider flag의 exclusivity, `stopReason` contract, news regex의 linearity, CI 거부 메시지, Gemini memoization, subprocess 환경에 secret이 전혀 없음을 고정했습니다. 마지막 assertion은 **generic**합니다. 어떤 list에도 이름이 없는 key에도 실패합니다. 반면 기존 redaction test는 자체 constant를 그대로 비추는 구조여서 자신의 loop가 고장 난 경우 외에는 아무것도 감지할 수 없었습니다. 전체 suite는 **311개 test**입니다.
  - **새로운 Grok provider 2개**: `--use_grok`(xAI API, 키 `XAI_API_KEY`, 사용량 기준 과금)와 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독에서 차감 — `--use_codex`과 같은 원리).
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`은 그대로 재사용하며, `base_url`만 변경됩니다. 단 하나의 조정만 필요했고 모든 provider에 도움이 됩니다. 이제 `finish_reason`은 OpenAI가 `stop`를 내보내는 위치에서 xAI가 내보내는 형식인 `end_turn`도 허용합니다. 모델: `grok-4.6`(품질) 및 `grok-4.3`(경제형). 참고로 Grok의 경제형도 저장소에서 가장 비쌉니다. 백만 개당 $1.25/$2.50인 반면 `mistral-small-latest`는 $0.15/$0.60입니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택하는 것입니다.
    - **CLI 모드**: Codex를 본떠 구현했지만 실제 환경에서 요구되는 네 가지 차이가 있습니다. prompt는 파일로 전달됩니다(`--prompt-file`, CLI는 stdin을 읽지 않으며 argv에 포함된 segment는 `ps`에 노출될 수 있음). 출력은 stdout의 단일 JSON 객체입니다(JSONL도 아니고 `-o` 파일도 아님). 구독에서 제공되는 모델은 `grok-4.6`와 `grok-4.5`뿐이며, sandbox는 적용할 수 없습니다(아래 참조). subprocess 실행은 이미 테스트된 Codex provider의 나머지 부분을 건드리지 않고 `_codex_run_process`에서 Codex와 공통화했습니다.
    - **`exit 0`만으로는 아무것도 입증되지 않음, 실측 완료**: 인증되지 않은 상태에서도 CLI는 **stdout**에 `{"type":"error","message":"Not signed in."}`을 쓰고 종료 코드 **0**을 반환합니다. 거부되거나 turn 한도를 초과한 경우도 동일하게 동작합니다. 따라서 출력 계약은 다음 네 가지 조건을 동시에 요구합니다. 종료 코드 0, 오류 payload 없음, `stopReason == end_turn`, 비어 있지 않은 text. preflight도 같은 논리를 따릅니다. 연결이 끊긴 상태에서도 `grok models`는 0으로 종료되므로, stdout에 « 인증되지 않음 »이 있는지를 통해서만 판단할 수 있습니다.
    - **격리: 의도적으로 채택하고 문서화한 비대칭성.** Codex는 `--sandbox read-only`에서 실행되지만, Grok sandbox는 최신 Linux 환경의 상당수에서 적용할 수 없습니다. `sudo` 없이는 우회할 수 없는 서로 독립적인 두 가지 시스템 원인이 있습니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`가 `0700` 상태일 때 container runtime socket의 deny-list가 실패합니다(resolver는 `ErrorKind::NotFound`만 처리하며 EACCES는 치명적 오류가 됨). 핵심 함정은 적용할 수 없는 **내장** profile을 지정하면 **아무 알림 없이 격리되지 않은 상태로 실행된다**는 점입니다. 따라서 script는 기본적으로 어떤 profile도 요청하지 않고, 절대 조용히 fallback하지 않으며 stderr로 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하며 catch-all `*`도 포함됩니다. 이는 실측된 유일한 _fail-closed_ 계층입니다(알 수 없는 prefix의 규칙이 하나라도 있으면 시작이 거부됨). `GROK_TRANSLATE_SANDBOX=read-only`로 이를 필수화할 수 있으며, 이 경우 해당 machine에서 이를 준수할 수 없으면 시작에 실패합니다.
    - **안전장치**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`은 subprocess 환경에서 제거됩니다(key가 있으면 사용량 기준 과금으로 전환되고, 상속된 `GROK_SANDBOX`은 적용할 수 없는 profile을 오해의 소지가 있는 message와 함께 강제하기 때문). MCP/hooks/skills/agents switch는 비활성화되며, `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI에서의 실행 거부, process group을 종료하는 timeout, rate limit 발생 시 back-off가 적용됩니다. `--max-turns`는 1이 아니라 6으로 설정됩니다. counter가 tool turn 이후 증가하므로 1로 설정하면 출력이 잘리기 때문입니다.
    - **할당량**: Grok pool은 주간 단위이며 **Chat, Imagine, Voice와 공유**되고, 이를 표시하는 command가 없습니다. 반면 Codex는 `account/rateLimits/read`을 통해 사용량을 수치화할 수 있습니다. 따라서 `regen_translations.sh`는 동시 실행을 2개로 제한하고 이를 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`(테스트 24개). 전체 suite는 **테스트 290개**입니다.
  - **버그 수정 — 여러 문단으로 된 영어 인용문이 일부만 보호되던 문제(`--news` 모드)**: `_NEWS_CITATION_REGEX`은 인용문 본문으로 **연속된** `>` 줄만 허용했습니다. 인용문이 여러 문단에 걸쳐 있으면(빈 `>` 줄로 구분됨) 마지막 문단만 포착되어 placeholder로 대체되었고, 이전 문단은 LLM으로 전달되어 번역되었습니다. 이는 `--news`이 보장하려는 것과 정확히 반대되는 동작입니다. 이제 반복 구문은 내부의 빈 `>` 줄을 허용하고 비탐욕적으로 동작하므로, 처음 만난 빈 줄이 아니라 기울임꼴 줄 앞의 빈 `>`에서 멈춥니다.
    - **실측 규모**: 실제 article 198개로 구성된 corpus에서 인용문 419개 중 11개가 영향을 받았습니다. regression은 없습니다. 새 regex는 정확히 같은 수의 인용문을 포착하며 여러 문단으로 된 본문만 확장됩니다(본문 408개는 동일하고 11개는 확장됨). 또한 attribution 줄 `> — …`은 여전히 본문에 포함될 수 없습니다(lookahead 유지).
    - **end-to-end 검증**: 69KB article을 ja/ar로 번역했습니다. 이전에는 인용문의 첫 문단이 일본어에서 `> GLM-5.3がオープンウェイト化。`로 렌더링되고 아랍어에서도 마찬가지로 번역되었지만, 이제는 `> GLM-5.3 is now open-weight.`로 유지됩니다. 영어 인용문 줄 수는 source와 동일한 10줄로 돌아왔습니다(기존 9줄).
    - 참고: 이 결함은 인용문의 존재 여부만 확인하고 완전성은 검사하지 않는 downstream validator에서 감지되지 않았습니다.
  - **기본 provider에서 실측된 비용 절감**: `_openai_extra_kwargs`은 model 이름이 `gpt-5`로 시작하기만 하면 `--eco`에서도 `reasoning_effort="medium"`을 전송했습니다. 열 단어짜리 문장을 번역하도록 `gpt-5.4-mini`에서 측정한 결과, `medium`은 reasoning token 45개와 출력 token 65개를 사용했지만 `none`는 각각 0개와 14개를 사용했습니다. 번역에는 reasoning이 아무런 이점이 없으며, 모든 파일의 모든 segment마다 비용이 발생하고 있었습니다. 이제 기본값은 `--eco`에서 `none`이고, 그 외에는 `medium`로 유지됩니다. CLI에서 명시적으로 전달한 값은 계속 우선합니다. 이제 `--reasoning_effort`은 `low`/`medium`/`high`뿐 아니라 `none`과 `xhigh`도 허용합니다(모든 model이 모든 값을 허용하는 것은 아닙니다. 예를 들어 `minimal`는 `gpt-5.4-mini`에서 거부되며, 기존의 parameter 없는 retry가 이 경우를 처리합니다).
  - **SDK 업데이트 및 Gemini migration**: `google-generativeai`(지원이 2025-11-30에 종료되었고 저장소가 archive됨)은 통합 SDK **`google-genai`**로 대체됩니다. `genai.Client(api_key=...)` 다음 `client.models.generate_content(model=, contents=, config=)`을 사용하며, system prompt는 segment에 연결하는 대신 `system_instruction`로 전달됩니다. `mistralai`는 **2.9.4**로 올라갑니다(import는 `from mistralai.client import Mistral`로 변경되며, 이전 방식은 `ImportError`을 발생시킴. wheel에서 확인). `anthropic`는 **0.125.0**, `openai`은 **2.54.0**으로 올라갑니다. venv에 HTTP stack 두 개가 공존하지 않도록 `httpx2`로 전환되기 전의 마지막 version을 사용합니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5의 제한도 해제되었습니다.
  - **문서가 아니라 실제 테스트로 발견한 regression 2건**:
    - `anthropic` ≥ 1.0은 `max_tokens`상 10분을 초과할 것으로 예상되는 non-streaming 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 안전장치는 0.34.2에는 없었으며 `max_tokens=32768`을 사용하는 모든 Claude 호출을 망가뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 전체 response만 사용하는 호출을 streaming으로 전환하지 않아도 됩니다.
    - `thinking_level="minimal"`은 Gemini catalog 일부에서만 허용됩니다. `gemini-3.1-flash-lite`는 이를 지원하지만 `gemini-3.7-flash`와 `gemini-3.1-pro-preview`은 400으로 거부합니다. 따라서 기존 OpenAI fallback을 본떠 `_gemini_generate_with_fallback`에 `minimal` → `low` → thinking_config 없음의 cascade를 구현했습니다. 최적화 parameter 때문에 번역이 실패해서는 안 됩니다.
  - **기본 model 갱신**, 각각 실제 호출로 검증됨: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%), Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜 없는 canonical ID), Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(stable version이며 `3.5-flash-lite`보다 저렴함). Mistral은 변경되지 않았으며 `mistral-large-latest`이 여전히 네 가지 중 가격 대비 품질이 가장 좋습니다. 참고로 `gemini-3.1-pro-preview`보다 최신인 Pro 계열 Gemini model은 없습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 계열은 전부 Flash 전용입니다.
  - **Gemini 전환 전 실측 A/B**: `README.md`를 `gemini-3.1-pro-preview`과 `gemini-3.7-flash`으로 각각 일본어로 번역했습니다. 구조는 완전히 동일했으며(list 21개, code block 18개, HTML link 13개, image 13개, 모든 URL 보존), 소요 시간은 **48초 대비 8초**였습니다. 번역이나 비라틴 문자 script에서 두 model을 비교한 공개 benchmark가 없으므로, 이 측정이 없었다면 전환은 단순한 추정에 의존했을 것입니다.
  - **Claude response block filtering**: `_call_claude`은 type을 filtering하지 않고 `block.text for block in response.content`을 수행했습니다. adaptive reasoning model(Sonnet 5 이상)은 `thinking` block을 중간에 삽입하며, 이 block은 `.text`가 아니라 `.thinking`을 노출합니다. 따라서 첫 segment에서 불투명한 `AttributeError` 때문에 번역이 실패했을 것입니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result` block은 제외됩니다(텍스트를 포함하는 알 수 없는 type도 허용할 수 있도록 negative list 사용). 텍스트 block이 하나도 없는 response는 명시적인 error를 발생시킵니다. `thinking={"type": "disabled"}`은 모든 호출에 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 폐기 날짜가 지난 model을 제거했습니다(`magistral-*` 계열은 2026-07-31 폐기, `gemini-2.0-*`은 2026-06-01 폐기, `gemini-3-pro-preview`는 2026-03-09 폐기, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`). 제한 수정: Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1,000,000 → **1,048,576**(실제 input 제한), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 계열 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 계열을 추가했습니다. 참고로 이 제한들은 여전히 참고용이며, `translate()`가 segmentation을 `min(16000, limite)`으로 제한합니다.
  - **Provider `--use_codex`**: 사용량 기반으로 과금되는 API를 호출하는 대신 공식 Codex CLI(`codex exec`)를 비대화형 모드로 구동하는 다섯 번째 provider입니다. 번역은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. 이는 OpenAI가 이 용도로 문서화한 유일한 방식입니다. 플랜별 이용 가능 기능 표에는 « Codex SDK, `codex exec`, and scriptable workflows »가 Plus/Pro/Business/Enterprise에서 이용 가능한 것으로 나와 있으며, `~/.codex/auth.json`의 token은 API Platform 호출을 인증하지 않습니다. 또한 이 스크립트는 해당 token을 전혀 읽지 않으며, 인증과 갱신은 계속 CLI가 관리합니다.
  - **npm뿐 아니라 pip로도 설치할 수 있는 Codex 바이너리**: `_resolve_codex_binary()`은 `CODEX_BIN`, 이어서 `PATH`, 그다음 OpenAI가 배포하는 공식 Python 패키지 **`openai-codex-cli-bin`**에서 바이너리를 찾습니다. 이는 SDK `openai-codex`의 dependency입니다. 따라서 Python 프로젝트에서 `--use_codex`을 사용하기 위해 더 이상 전역 npm 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가되지 않습니다. 바이너리 크기가 약 250MB이므로 선택적 provider를 위해 모든 사용자에게 이를 강제하게 되기 때문입니다. 전체 과정 검증 완료: `PATH`에 `codex`이 없는 상태에서도 패키지에 포함된 바이너리를 찾아 전체 번역을 6초 만에 완료합니다.
  - **« 구독 모드 » 보장**: 하위 프로세스 환경에서 `OPENAI_API_KEY`과 `CODEX_API_KEY`을 제거합니다. 이 보호 장치가 없으면 `.env`에 존재하는 key 때문에 아무런 표시 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 이는 바로 이 provider가 방지하려는 상황입니다.
  - **테스트로 고정한 CLI 함정**:
    - prompt를 인수로 전달하더라도 `codex exec`은 stdin을 **계속** 읽습니다. stdin을 닫지 않으면 명령이 모델을 호출하지 않은 채 timeout까지 대기합니다. 재현 결과는 180초 후 exit 124, 0바이트였습니다. 따라서 `communicate(input=...)`은 필수입니다.
    - npm으로 설치한 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 이 바이너리는 Python process의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 할당량을 계속 소비할 수 있습니다. 따라서 `Popen(start_new_session=True)` + `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`을 출력하고도 종료 코드 0을 반환할 수 있습니다. 반환 코드뿐 아니라 JSONL 출력(`--json`)도 검사하며, 코드가 0인데 `-o` 파일이 없으면 빈 segment를 생성하는 대신 명시적 오류를 발생시킵니다.
  - **rate limit back-off**: CLI는 내부 retry를 전혀 구현하지 않습니다(`max_retries = 0`). 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. « quota »라는 단어가 복구 가능한 429와 영구적인 `insufficient_quota` 모두에 나타나기 때문입니다.
  - **CI 보호 장치**: `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 `--use_codex`을 거부합니다. 구독 인증은 공유 runner용으로 설계되지 않았으며, OpenAI도 공개 저장소에서 이 workflow를 명시적으로 권장하지 않습니다.
  - **모델**: `gpt-5.6-sol`(품질)과 `gpt-5.6-luna`(`--eco`)입니다. `gpt-5.6-*` 계열은 CLI와 API Platform에 공통으로 제공되지만, ChatGPT 계정으로 모든 모델을 사용할 수 있는 것은 아닙니다. allowlist는 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 지정하면 경고가 발생합니다. Plus 플랜에서 Luna는 5시간 window당 250~2,000개 message를 제공하지만 Sol은 10~100개입니다. 따라서 모든 batch 처리에는 `--eco` 모드를 권장합니다.
  - **수정된 버그 — 완전히 성공했는데도 `regen_translations.sh`이 오류로 종료됨**: `trap ... EXIT`은 `main()`의 `local` 변수인 `failed_log`을 참조했지만, trap 실행 시점에는 이 변수가 더 이상 존재하지 않았습니다. `set -u`에서는 이 때문에 `failed_log: unbound variable`이 발생하여 28개 번역이 모두 올바른데도 스크립트가 코드 1로 종료되었습니다. 이로 인해 재생성 직후 가장 비용이 큰 단계에서 `release.sh --auto`(`set -e`)이 중단될 수 있었습니다. 변수를 전역으로 바꾸고 trap에서 변수의 존재 여부를 검사하도록 했습니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 최종 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: provider의 기본값보다 우선하여 특정 모델을 강제하는 `regen_translations.sh`의 새로운 환경 변수입니다. 예를 들어 처리량 중심 모델인 `--eco` 대신 구독 할당량의 최고급 모델로 재생성하려면 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 지정할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때만 `REGEN_PROVIDER=codex`을 사용할 수 있습니다. 사용자가 모르는 사이 구독 할당량을 소비하지 않도록 자동 감지하지 않습니다. 병렬 처리를 시작하기 전에 token을 순차적으로 한 번 갱신합니다. Codex refresh는 순환형 일회용이므로 동시 job이 `codex login` session을 무효화할 수 있기 때문입니다. concurrency는 4로 낮춥니다.
  - **관련 refactor**: 전체 체인에 네 번째 boolean을 전달하는 대신 provider 이름을 반환하는 `_resolve_provider()`을 사용하여 `_dispatch_provider_call`의 parameter 수를 8개에서 6개로 줄였습니다. 최소한의 `Namespace`으로 `translate(..., use_mistral=True)`을 호출하는 테스트를 보존하기 위해 명시적 boolean은 계속 `args`보다 우선합니다.
  - **테스트**: argv, 정리된 환경, 서문 금지 contract, silent failure, timeout/killpg, back-off, preflight, provider 해석, Gemini reasoning cascade, Claude block 필터링, 여러 paragraph로 된 news citation을 다루는 새로운 파일 `tests/test_codex_provider.py`에 48개 테스트를 추가했습니다. 전체 suite는 290개 테스트입니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 참조 번역과 구조가 완전히 동일했습니다. code block 14개, 제목 24개, table row 25개, HTML link 13개, image 13개, URL 19개가 유지되었고, code block은 문자 단위까지 동일하며 placeholder 잔여물은 0개였습니다. `--news` 모드로 처리한 69KB news article에서는 `gpt-5.6-luna` 및 `gpt-5.6-sol` 출력이 en/ja/ar 모두에서 후속 애플리케이션 validator를 통과했습니다. `account/rateLimits/read`로 측정한 사용량은 `--eco` 모드에서 계수기의 반올림 기준 미만, 즉 5시간 window의 0%로 유지되었습니다.

- **1.9.2** 중첩 괄호 또는 프랑스어 접두사가 있는 news attribution URL 추출 수정(2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`의 attribution URL 추출은 regex `re.search(r"\((.+?)\)", attribution)`을 사용했습니다. 이는 괄호 사이를 lazy capture합니다. `(relayé par [@user sur X](https://x.com/.../123))` 형식의 attribution에서는 괄호가 중첩되어 있습니다. 즉, 바깥쪽 `(`과 Markdown link의 `]()`이 함께 존재합니다. 이 경우 capture가 처음 만난 `)`에서 중단되어 문자열이 잘리고 프랑스어 접두사까지 포함되었습니다. 결과는 마지막 `)`이 없는 `relayé par [@user sur X](https://x.com/.../123`이었습니다. 그 결과 `_validate_news_post`은 번역된 출력에서 이 문자열을 찾으려다 항상 실패했습니다. 원인은 `)`이 잘렸고 « relayé par »가 `relayed by`/`weitergeleitet von`/...로 번역되었다는 두 가지였습니다. low → medium → high → gpt-5.5 전체 cascade가 모두 통과할 수 없었습니다.
  - **수정**: regex를 `re.search(r"\]\(([^)]+)\)", attribution)`으로 변경했습니다. Markdown link의 `](url)`을 구체적으로 대상으로 삼아 프랑스어 접두사나 잘림 없이 **순수 URL만** capture합니다. 번역 중에는 placeholder `#URL{N}#`이 이를 불변으로 보존합니다. 다음 두 가지 문제 pattern을 모두 안정적으로 처리합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥쪽 괄호가 없는 프랑스어 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` class에 2개를 새로 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그를 그대로 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`이 포함된 변형)
  - **coverage 공백**: `check-editorial-coverage.py`은 편집 문법은 검증하지만 translator를 통한 번역 가능성은 검증하지 않습니다. 향후 가능한 개선 사항(v1.9.2 범위 밖)으로, publication **이전**에 위험한 pattern을 탐지하도록 dry-run에서 attribution 추출을 시뮬레이션하는 검사를 추가할 수 있습니다.

- **1.9.1** 번역 marker note의 CTA label i18n 수정(2026-05-10):

  - **수정된 버그**: 번역 파일 상단의 marker banner에 있는 CTA link label `[Voir le projet sur GitHub ↗]`이 `target_lang`를 따르지 않고 모든 대상 언어에서 **프랑스어**로 남았습니다. URL과 repo slug를 보존하기 위해 Python 측에서 조립하므로 LLM에는 전혀 노출되지 않으며, 번역 단계에서도 이를 수정할 수 없었습니다. v1.9에서 `marker` 형식을 추가한 이후 발생한 silent regression입니다.
  - **수정**: 15개 언어를 각각의 현지화 label에 매핑하는 새로운 상수 `_VIEW_PROJECT_LABELS`을 추가했습니다. 이제 `_translation_note_invariants(target_lang)`와 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달합니다. 알 수 없는 언어에는 `fr` fallback을 사용합니다. 이는 안전성을 위한 것으로 KeyError가 발생하지 않습니다.
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 조정했습니다. target_lang `ja`에 일본어 label이 예상됩니다. 새 테스트 2개를 추가했습니다. 표의 문자, abjad, Latin script를 포함하는 7개 언어를 parameterize한 `test_source_link_label_localized_per_target_lang`과 `test_source_link_label_falls_back_to_french_for_unknown_target`입니다. 총계는 `test_translation_note_position.py`에서 38개가 아닌 40개 테스트입니다.
  - **하위 호환성**: 기본값이 있는 signature `target_lang="fr"`을 사용하므로 `args.target_lang` 없이 호출하는 외부 programmatic caller도 수정 없이 계속 동작합니다.
- **1.9** 자동 실패 수정 + 완전한 품질 도구 체계 + 다중 위치 번역 주석 (2026-05-07):
  - **다중 위치 번역 주석 + "embed card" 마커 형식**:
    - 새로운 CLI 옵션 추가(기본값은 변경되지 않음 → **비호환 변경 없음**):
      - `--note_position {top,bottom,both}`(기본값: `bottom`): 번역된 파일의 위쪽, 아래쪽 또는 양쪽 모두에 주석을 배치합니다.
      - `--note_format {legacy,marker}`(기본값: `legacy`):
        - `legacy`은 v1.8 동작을 엄격하게 **바이트 단위로 동일하게** 재현합니다(굵은 단락 `**…**`).
        - `marker`은 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)와 함께 "GitHub 저장소 embed card" 형태로 렌더링되도록 구성된 **3개 단락의 인용문**을 출력합니다. 여기에는 인라인 코드로 된 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM이 번역한 설명, 표시되는 화살표가 포함된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 들어갑니다. 빌드 시 remark 플러그인에서 활용할 수 있습니다(jls42.org 블로그의 `remark-translation-banner` 플러그인 참조).
    - **LLM에 절대 전송되지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문구 번역 후 Python 측에서 조합됩니다. LLM에는 `ai-powered-markdown-translator` 슬러그나 `https://github.com/jls42/...`이 절대 노출되지 않으므로 renderer, 대소문자 또는 scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter를 닫는 `---` 블록 **뒤에** 주석이 삽입됩니다(Astro Content Collections / gray-matter 안전성). `_split_frontmatter` helper는 파일 시작 부분의 `---\n…\n---\n`을 감지하고 그 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter에는 **`RuntimeError`을 발생시켜**, 잘못된 위치에 주석이 삽입된 채 파일이 작성되는 대신 `failed_files`에 보고되도록 합니다.
    - **Whitelist 기반 모델 sanitizer**: `_sanitize_model`은 `[A-Za-z0-9._:/-]`에 속하지 않는 모든 문자를 `_`으로 바꾸며, 결과가 비어 있으면 `unknown`을 사용합니다. Astro의 remark 플러그인 측 validator와 일치시키고 마커 형식을 손상시킬 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 refactor**: `_append_translation_note`(단일 모놀리식 함수) → 순수 helper 7개(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). builder와 composer를 분리했습니다(builder는 구분자 없는 순수 블록을 반환하고 composer는 위치에 따라 `\n\n`을 적용). 프로덕션 코드와 소스 helper가 동일한 3개 단락 assembler를 공유합니다.
    - **공백 줄을 보존하는 `_quote_lines`**: 각 줄 앞에 `> `을 붙이고 빈 줄은 `>`만 있는 줄로 변환합니다. 이를 통해 mdast는 인용문을 줄바꿈만 포함한 하나의 단락이 아니라 서로 구분된 3개 단락(제목 / 설명 / 링크)으로 인식합니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 단락 수에 따라 달라집니다(3개 = 완전한 card 형식, 2개 = 문장 + 링크, 1개 = fallback). Markdown 링크 `](`이 감지되면 1개 단락 fallback을 더 이상 **`**...**`으로 감싸지 않습니다**(링크 주변의 `<strong>` 렌더링이 불안정하기 때문).
    - **상위 호환성**: `_compose_with_notes` 측의 `getattr(args, "note_position", "bottom")`과 `getattr(args, "note_format", "legacy")` — 해당 속성이 없는 Namespace도(기존 테스트, 외부 프로그래밍 방식 호출) 수정 없이 계속 작동합니다.
  - **긴 번역의 자동 실패 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 적용: 결정론적 계층(소스 일부가 그대로 발견되는지 검사) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k segment에서 잠재적인 truncation 방지, 교차 문자 체계 FR→JA/ZH/KO/AR/HI 여유 확보)
    - heading 인식 segmentation: segment 후반부의 H2/H3에 우선순위를 부여하여 각 segment가 의미상 완전한 section으로 시작하도록 함
    - 0이 아닌 exit code까지 오류 전파: `translate_markdown_file`은 형식화된 상태 `success` / `failure` / `skipped`을 반환하고, 하나 이상의 파일이 실패하면 `main()`이 `sys.exit(1)`을 반환(single-file 및 batch)
    - 모든 provider에 빈 콘텐츠 guard 적용, 소스/출력 sanity ratio 검사(500자 이상이며 5% 미만이면 거부), 코드 placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 처리 후 정규화(구분자/링크가 heading에 붙는 현상), `reasoning_effort` 없이 `BadRequestError` retry
    - `langdetect==1.0.9` 의존성 추가
  - **pre-commit 품질 도구 체계**("완전한 EurekAI 유형", hook 14개):
    - Pre-commit: ruff(lint+format), shellcheck, prettier(md/yaml/json), detect-secrets(API key 4개 보호), Lizard(CCN ≤ 12), pre-commit-hooks v5(공백, EOF, 대용량 파일, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `./venv/bin/python`을 사용하는 `scripts/`의 로컬 wrapper
    - `scripts/audit_verdict.py`: unittest 11개를 포함한 pip-audit JSON parser로, jls42-astro parser를 Python으로 이식한 버전
    - 초기 ruff 위반 7개 수정: B904(raise from) ×2, B007(사용하지 않는 dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard는 `translate.py`을 일시적으로 제외(CCN 21~47인 함수 4개, refactor 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 포괄적인 coverage**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): 모든 push 및 pull-request에서 분석하고 `coverage.xml`을 통해 coverage 수집
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability 등급, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` 표준 라이브러리): 자동 실패 오류 체인의 여섯 연결 고리를 다룸
    - `tests/test_orchestration.py`(테스트 79개 추가): `translate.py`의 orchestration 계층을 다룸(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return 분기)
    - `scripts/tests/test_audit_verdict.py`: subprocess를 통해 `main()`(stdin/stdout)과 `if __name__ == "__main__"` 블록의 coverage 확보
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 조합(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 여러 줄 접두사 적용, 바이트 단위로 동일한 하위 호환성(golden literal), sanitizer, frontmatter 분리(닫히지 않은 fence에서의 예외 발생 포함), 3개 단락 형식, 2개 단락 fallback, 1개 단락 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않음을 assert하는 중요한 보호 장치 `TestLLMPayloadExcludesInvariants`을 다룹니다. **테스트 190개 통과**, 회귀 0건.
  - 문서화: badge가 포함된 `README.md`(프랑스어 + 번역 14개), `CLAUDE.md`(pre-commit workflow + 상세 CI watch), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 갱신(2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 고품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 고품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token 제한 추가
  - 초기 `--news` 모드: placeholder `#NEWSQUOTE\d+#`을 통한 영어 인용문 보호, `LANG_FLAGS` mapping(15개 언어), 대상 언어별 flag 관리
  - 복원 전 news placeholder 검증(회귀: LLM이 placeholder를 삭제하면 인용문이 없는 출력이 아무 오류 없이 생성되었음)
  - `regen_translations.sh` script를 이식 가능하게 개선(절대 경로 사용, pwd 의존성 제거)
  - README/CHANGELOG의 언어 표시줄에 프랑스어 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원래 파일 이름을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **인라인 코드 보존**: 이제 번역 중 backtick(`` `...` ``)을 보호
  - system prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - template 변수 `{variable}` 보호
    - 요청하지 않은 번역자 주석 금지
  - 파일 364개에서 성공적으로 테스트(jls42.org 블로그 마이그레이션)
- **1.6** 새로운 기능:
  - 번역용 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(고품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(고품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(고품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 탐색하지 않고 단일 파일 번역(`--file`)
  - 간소화된 새로운 이름 지정 pattern: `{base}-{lang}.md`
  - 모델 이름을 포함한 기존 형식을 유지하는 `--include_model` 옵션
  - 목록에 없는 모델을 기본 token 제한(128k)으로 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`로 업데이트.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`로 업데이트.
  - **번역 prompt 최적화:**
    - 직접 번역과 번역 주석용 prompt의 명확성과 효율성을 높였으며, metadata와 특정 formatting 요소의 보존에 관한 상세 지침을 포함했습니다.
  - **코드 refactor:**
    - Mistral AI client 초기화를 위해 `MistralClient`을 `Mistral` class로 교체.
    - 가독성과 유지보수성 향상을 위해 import 재구성.
    - 번역 시 원래 formatting을 보존하도록 텍스트 segmentation 및 코드 블록 처리 개선.
  - **출력 파일 관리:**
    - 출력 파일 이름에서 모델과 언어의 순서를 바꿈(예: `f"{base}-{args.target_lang}-{args.model}.md"`)으로써 번역을 더 쉽게 정리하고 검색할 수 있도록 개선.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 코드 정리.
    - script 구조와 가독성을 개선하기 위한 사소한 조정.
- **1.4** 새로운 기능:
  - 번역용 Anthropic Claude API 지원
  - 명확성과 효율성 향상을 위한 prompt 최적화
  - 코드 유지보수성 향상을 위한 사소한 조정
- **1.3** 개선 사항 및 새로운 기능:
  - 코드 블록 처리 개선
  - 출력 파일 관리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일 이름에서 모델과 언어의 순서 변경
- **1.2** changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**gpt-5.6-sol을 사용하여 프랑스어에서 한국어로 번역된 기사.**
