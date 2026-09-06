### 변경 이력

🌍 [프랑스어](CHANGELOG.md) | [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`: 중국의 공개 모델을 포함한 약 430개 모델로 연결되는 유료 라우터(2026-09-05):

  - **아홉 번째 provider 경로이며, 여덟 번째 경로와 함께 제공됩니다.** 1.12.0은 PyPI에 게시되지 않았습니다. 두 라우터인 OpenCode와 OpenRouter가 함께 출시됩니다. [OpenRouter](https://openrouter.ai)는 하나의 키로 여기의 다른 어떤 provider도 제공하지 않는 Kimi, Qwen, DeepSeek, Z.ai 등의 모델에 접근하게 해 주며, 사용량에 따라 과금되는 하나의 크레딧을 사용합니다. endpoint가 OpenAI와 호환되므로 client는 xAI와 동일합니다. **이 provider를 구별하는 모든 요소는 preflight에 있으며**, 각 규칙은 API에서 측정한 결과에 기반합니다.

  - **동일한 모델을 서로 다른 한도를 가진 수십 개의 호스팅 업체가 제공하지만, 라우팅은 이를 인식하지 못합니다.** 측정 결과 `z-ai/glm-5.2`에는 33개, `z-ai/glm-5.3-flash`에는 23개의 호스팅 업체가 있었으며, 그중 하나의 **출력 한도는 2,048 tokens**이었습니다. 따라서 23개 업체를 통한 긴 번역은 아무런 신호도 없이 무작위로 잘렸습니다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽고 출력 한도가 8,000 tokens 미만인 업체, 상태가 저하된 업체, 한도를 선언하지 않은 업체를 제외한 뒤 나머지를 고정합니다. `allow_fallbacks: false`가 **없는** `provider.only`은 선호 설정일 뿐입니다. 라우터는 제외된 호스팅 업체로 다시 전환하므로 고정은 아무 의미가 없어집니다. 한도를 충족하는 호스팅 업체가 하나도 없으면 명령이 중단됩니다. 그래도 번역을 계속하는 것은 이 preflight가 방지하려는 조용한 잘림을 받아들이는 것과 같기 때문입니다.

  - **추론은 출력 요율로 과금되며, 많은 모델에서 기본적으로 활성화되어 있습니다.** `z-ai/glm-5.2`에 동일한 요청을 보내 “OK” 응답을 측정한 결과, **모델 기본값에서는 completion tokens가 107개였고 추론을 끄면 2개였습니다**. 추론이 아무런 이점도 주지 않는 번역에서는 모든 파일의 모든 segment마다 비용이 18배가 됩니다. 따라서 기본적으로 비활성화됩니다. 추론을 강제하는 **431개 중 288개 모델**(`reasoning.mandatory`)은 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`으로 응답합니다. 이 모델들에는 임의로 추측한 effort를 보내는 대신 아무것도 보내지 않습니다. effort는 추론이 먼저 소비하는 **`max_tokens`의 일정 비율**을 할당하므로, 무작위로 값을 정하면 빈 페이지가 발생할 위험을 줄이는 대신 옮길 뿐입니다.

  - **추론을 강제하는 모델에는 해당 모델이 허용하는 가장 낮은 effort가 전달되며, 이는 측정을 통해 결정되었습니다.** 처음에는 모델을 대신해 추측하지 않도록 아무것도 보내지 않는 방식을 선택했습니다. catalogue 기본값이 `max`인 `z-ai/glm-5.3-flash`에서 검증한 결과, 이 선택은 번역이 끝나기 전에 출력이 **32,768 tokens에서 잘리는** 결과를 낳았고, 14개 언어 중 2개가 유실되었습니다. 한도를 늘려도 달라지지 않았을 것입니다. effort가 한도의 일정 비율을 할당하므로 한도가 커지면 추론도 함께 커지기 때문입니다. 따라서 provider는 preflight에서 `supported_efforts`을 읽어 가장 낮은 값을 요청하고, catalogue에 사용할 수 있는 값이 없으면 “없음”으로 대체합니다. 문제가 발생했던 언어로 대조 검증한 결과, 이전에는 예산 소진으로 실패했지만 이제는 원본과 동일한 구조를 유지하며 9분 만에 완료됩니다.

  - **이제 upstream 호스팅 업체의 장애가 해당 업체의 이름과 함께 표시됩니다.** 라우터는 이 경우를 null인 `native_finish_reason`와 함께 `finish_reason=error`으로 정규화합니다. 두 언어에서 두 번 측정했으며, 모두 정확히 750초였습니다. 일반적인 메시지는 문서나 분할 방식의 결함을 찾게 만들었지만, 이제는 공급자 측 장애이며 재시도만으로 해결되는 경우가 많다고 알립니다.

  - **출력이 비어 있는 `finish_reason=length`은 잘림이 아닙니다.** 첫 번째 유효 문자가 나오기 전에 추론이 예산을 모두 소비한 경우입니다. 유효 출력 148 tokens에 앞서 추론에 15,850 tokens가 사용된 것으로 측정되었습니다. 두 경우에는 정반대의 조치가 필요합니다. 전자의 경우 segment 크기를 줄여도 소용이 없습니다. 메시지는 두 경우를 명확히 구분합니다. 측정 결과에 따른 보호 장치도 두 가지 추가되었습니다. upstream 호스팅 업체가 실패하면 라우터는 **오류만 담긴 본문과 함께 200으로 응답**하며(`choices[0]`은 메시지를 가리는 불투명한 `TypeError`을 발생시켰습니다), context window는 catalogue에서 읽어 `MODEL_TOKEN_LIMITS`에 기록됩니다. catalogue의 44개 모델에서는 `DEFAULT_TOKEN_LIMIT`가 잘못되어 있으며, 그중 두 개의 한도는 4,095 tokens입니다.

  - **`--model fournisseur/modèle`은 필수이며, 네트워크에 접근하기 전에 형식을 검증합니다.** OpenRouter는 공급자가 아닙니다. 이 선택에는 가격, 라이선스, 데이터 처리가 수반되므로 사용자를 대신해 결정할 수 없습니다. slug가 preflight URL에 보간되기 때문에 검증은 단순한 사용성 배려가 아니라 경로 주입을 방지하는 보호 장치입니다. 두 라우터가 공통으로 사용하는 namespace 형식의 regex는 `a/b/..`을 허용하므로 상위 segment는 명시적으로 거부됩니다. `--eco`은 아무 효과가 없으며 그 사실을 알립니다.

  - **세 가지 표현을 바로잡았으며, 그중 하나는 사실과 달랐습니다.** `codex exec`에 관한 OpenAI의 경고는 공개 저장소 자체가 아니라 공유 runner에 개인 session 파일을 주입하는 문제를 가리켰습니다. README, CLAUDE.md, 코드에서는 그 의미가 반대로 인용되어 있었습니다. OpenCode의 인증 위치는 1.18.27에서 `opencode.db`의 `credential` table로 변경되었으며, 더 이상 `auth.json`이 아닙니다. “여기서는 절대 읽지 않는다”는 불변 조건은 여전히 참이었지만 주소가 오래되었습니다. 마지막으로 OpenCode section에서는 검증한 적 없는 경로를 더 이상 동등한 것으로 소개하지 않습니다. Zen gateway와 Ollama는 처음부터 끝까지 측정했지만 GitHub Copilot, LM Studio, llama.cpp는 그렇지 않았으며, 이제 README에 이 사실이 명시되어 있습니다.

  - **측정 캠페인을 수행하고 README에 권장 모델 표를 추가했습니다.** 세 종류의 문서 모음, 즉 `--news` 모드로 작성된 밀도 높은 블로그 글, 표준 Markdown 형식의 이 README, GitHub에서 원본 그대로 가져온 유명 프로젝트 README 네 개를 14개 언어로 번역하여 300회 넘게 실행했습니다. 표는 이전에 혼동했던 두 가지, 즉 **완료된** 번역과 원본과 **구조가 동일한** 번역을 구분합니다. 밀도 높은 두 문서에서 단 하나의 정보도 잃지 않은 모델은 세 개였습니다. `gemini-3.7-flash`, ChatGPT 구독의 `gpt-5.6-sol`, OpenRouter를 통한 `z-ai/glm-5.2`입니다. 유일한 차이는 한두 언어에서 `**` 한 쌍이 반영되지 않은 것입니다. 핵심 결론은 **구별 요인이 `--news` 모드가 아니라 문서의 밀도라는 점**입니다. 구독형 Grok은 블로그 글에서 14회 중 13회 실패했지만 공개 README에서는 16회 중 14회 성공했습니다. 원인은 긴 segment에서의 이탈이었으며 대조 검증으로 확인했습니다. 표 자체에도 주의 사항이 있습니다. 이 표는 전체를 포괄하지 않고 특정 시점의 결과이며, 소요 시간은 순위를 의미하지 않습니다. 올바른 방법은 여전히 자신의 문서로 직접 측정하는 것입니다.

  - **비라틴 문자 체계에서 두 건의 오탐을 일으켰기 때문에 수치를 게시하기 전에 구조 비교기를 수정했습니다.** 전각 닫는 괄호 `）`이 뒤따르는 URL은 `)`에서 멈추는 regex로 분리되지 않았으며, 이로 인해 URL은 동일해도 추출된 문자열이 달랐습니다. 프랑스어로 다섯 줄인 인용문이 중국어로 세 줄에 들어가면서 줄 단위 집계가 감소하기도 했습니다. 두 수정 사항 모두 대조 검증을 거쳤습니다. URL, section 또는 inline code를 삭제하면 여전히 감지됩니다. 이 수정이 없었다면 Gemini와 Codex의 결과는 각각 14개 언어 중 13개와 12개가 아니라 11개로 게시되었을 것입니다.

  - **테스트**: 새로운 `tests/test_openrouter_provider.py` 파일(테스트 39개) — 모델 검증 및 상위 segment 거부, 호스팅 업체 고정(한도, 상태, 미선언 한도, 공통 최솟값), 항상 false인 `allow_fallbacks`, `mandatory`에 따른 추론 비활성화 또는 유지, 전체 출력 계약(200 응답 내 오류, 선택지 없음, 빈 페이지와 잘림의 구분, 비정상적인 `finish_reason`, null 콘텐츠), catalogue에 연결할 수 없을 때 fail-closed되는 preflight, 누락된 slug 및 정상 호스팅 업체 부재, flag 상호 배타성과 파일명 label을 검증합니다. 전체 test suite는 **427개 테스트**입니다.

- **1.12.0** Provider `--use_opencode`: open source agent인 OpenCode를 통해 사용자가 선택한 공급자에 연결 — 로컬 모델, 계정 없이 무료 사용, 구독 또는 키(2026-09-04):

  - **여덟 번째 provider 경로이며, 앞선 일곱 경로와는 성격이 다릅니다.** [OpenCode](https://opencode.ai)(MIT)는 모델 공급자가 아니라 사용자가 OpenCode 자체에 구성한 대상, 즉 API key, 구독(GitHub Copilot, ChatGPT, SuperGrok), 계정 **없이** 무료 모델을 제공하는 OpenCode Zen gateway 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp)로 연결하는 _라우터_입니다. script는 Codex와 Grok을 제어하는 것처럼 비대화형 모드에서 `opencode run`을 제어하고, 동일한 subprocess 기반 구조를 재사용합니다. 별도의 process group, timeout 시 `SIGTERM` 실행 후 `SIGKILL` 실행, 항상 닫힌 stdin, 정리된 환경이 적용됩니다. **두 건의 실제 번역**으로 검증했습니다. `opencode/mimo-v2.5-free`을 통해 이 README 전체를 영어로 번역한 결과 49초가 걸렸고 단 한 번에 완료되었으며 원본 파일과 구조가 동일했습니다(제목 32개, code 종료부 26개, 링크 18개, URL 37개, table 행 37개, inline code 135개). 또한 키 없이 로컬의 `ollama/qwen2.5:7b`을 통해 시험 파일을 번역했습니다.

  - **`--model provider/modèle`은 필수이며, 명시적인 선택입니다.** `--model`이 없으면 OpenCode는 자체 기본값으로 돌아가며, 새로 설치한 환경에서는 대화 내용이 학습에 사용될 수 있는 무료 “stealth” 모델인 `opencode/big-pickle`이 기본값입니다. 측정 결과 실제로 이 모델이 응답했습니다. 사용자를 대신해 이를 조용히 선택하는 것은 이 저장소가 추적하는 바로 그 보이지 않는 전환입니다. 따라서 오류 메시지는 모델을 나열하는 명령(`opencode models`)과 세 가지 예시(로컬, 무료, 구독)를 명시합니다. `--eco`은 아무 효과가 없으며 그 사실을 알립니다. `--reasoning_effort`은 명시적으로 요청한 경우에만 OpenCode의 `--variant`으로 변경 없이 전달됩니다.

  - **격리는 가정하지 않고 측정했습니다.** inline 구성(`OPENCODE_CONFIG_CONTENT`, OpenCode의 병합 순서에서 마지막이므로 사용자의 구성을 대체하지 않으면서 우선 적용됨)은 모든 도구를 거부하는(`permission: {"*": "deny"}`) `aipmt` agent를 정의합니다. registry가 도구를 모델에 아예 제시하지 않으므로 “파일을 나열하고 `id`을 실행하라”는 요구를 받아도 도구가 없다고 응답합니다. session 공유는 비활성화되고 외부 plugins는 제외되며(`--pure`), `--auto`은 절대 사용하지 않고 작업 디렉터리는 비어 있는 일회용 공간입니다. 조용히 발생하는 두 가지 주입을 측정해 차단했습니다. `OPENCODE_DISABLE_CLAUDE_CODE`이 없으면 사용자의 `~/.claude/CLAUDE.md`가 **모든** prompt에 들어갑니다. 간단한 “안녕하세요”에도 입력 tokens가 186개에서 515개로 늘어났습니다. `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 디렉터리의 `AGENTS.md`도 들어갑니다. “모든 응답을 BANANA로 끝내라”는 지시가 번역에 적용된 사례가 있었습니다. 반면 전역 `~/.config/opencode/AGENTS.md`은 계속 주입됩니다. 이를 제외하는 switch가 없으며, 우회적으로 `XDG_CONFIG_HOME`을 사용하면 사용자의 공급자까지 숨겨집니다. 임시방편으로 처리하는 대신 문서화했습니다.

  - **`exit 0`은 아무것도 증명하지 않습니다. 세 번째 CLI에도 동일한 원칙을 적용하되, 이 CLI에는 고유한 함정이 두 가지 있습니다.** 알 수 없는 `--agent`을 전달해도 `opencode run`은 실패하지 않습니다. stderr에 경고를 표시한 뒤 도구가 활성화된 coding agent로 **조용히** 대체합니다. inline 구성이 적용되지 않았다면 쓰기가 가능한 agent로 번역이 진행되었을 것입니다. 따라서 출력 계약은 이 메시지가 없음을 확인하는 것 외에도 종료 코드 0, `error` 이벤트 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`일 것(`length`은 잘린 응답임), 비어 있지 않은 텍스트를 검증합니다. 두 번째 함정은 오류 JSON 이벤트가 **불투명하다**는 것입니다. 단순한 참조와 함께 “예기치 않은 서버 오류입니다. 자세한 내용은 서버 로그를 확인하세요.”라고만 표시되며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 log에만 존재합니다. 이 때문에 `--print-logs --log-level ERROR`을 사용하고 그 뒤에 이어지는 Bun trace를 제외한 stderr의 `error="…"` field를 읽습니다. 따라서 알 수 없는 모델은 원인이 명시된 상태로 1초 만에 실패합니다. `--title`은 불필요한 LLM 호출도 방지합니다. 이것이 없으면 OpenCode가 `small_model`에서 한 번 더 요청하여 session 제목을 생성합니다.

  - **비밀 정보는 Codex 및 Grok과 동일하게 pattern으로 필터링하되, 이름으로 지정된 한 가지 예외가 있습니다.** `OPENCODE_API_KEY`은 유지됩니다. 이는 OpenCode 자체의 키(Zen gateway, Go 구독)이며 이름 그대로 OpenCode에 전달됩니다. OpenCode의 `auth.json`에 해당하는 것으로, aipmt가 관리하거나 과금할 수 있는 키가 아닙니다. 공급자는 OpenCode에서 구성하며(`opencode auth login`, `opencode.json`), aipmt의 `.env`에서는 절대 구성하지 않습니다. aipmt의 어떤 키도 subprocess에 도달하지 않습니다. 구독형 CLI와 달리 CI에서는 거부하지 않습니다. runner에서 API key나 자체 호스팅 모델을 사용하는 것은 정당한 사용 방식입니다.

  - **이제 traversal 방지 보호 장치는 원시 값이 아니라 보간되는 값을 검사합니다.** `provider/modèle`에는 1.10.0의 보호 장치가 거부했던 `/`이 포함되어 있습니다. `--model`이 파일명 `--include_model`에 보간되므로 당시의 거부는 타당했습니다. 이제 파일명 label은 어떤 보간보다 먼저 `/`, `\`, `:`을 `-`으로 바꿉니다(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, `:`은 Windows에서 허용되지 않음). upstream 보호 장치는 이 label을 검사합니다. `../../evil`은 대상 아래의 단순한 이름 `doc-en-..-..-evil.md`이 되고, `..`만 여전히 거부되며 `--target_lang ../x`도 거부됩니다. `_ensure_within_directory`의 범위 보호 장치는 변경 없이 두 번째 계층으로 유지됩니다.

  - **무료 모델과 로컬 모델에 관해 측정한 결과입니다.** `opencode/mimo-v2.5-free`은 문단 하나를 16초, 이 README를 49초 만에 번역합니다. `opencode/big-pickle`은 200단어에 40초가 걸리며, 개별 요청은 각각 완료되었지만 동시 요청 두 개에는 5분 동안 응답하지 않았습니다. `opencode/nemotron-3.5-lightning-free`은 3분 동안 아무 응답도 하지 않았습니다. 따라서 `REGEN_PROVIDER=opencode`에는 `REGEN_MODEL`이 필수이며 병렬 **job은 2개**입니다. 로컬 환경에서 Ollama는 segment가 최대 16,000자임에도 context를 4,096 tokens로 구성하는 경우가 많습니다. 따라서 `PARAMETER num_ctx 32768`를 사용하는 `Modelfile`이 필요하며, 품질은 모델에 따라 달라집니다. 시험 파일에서 7B 모델은 list 순서를 뒤집고 code block 종료부를 손상했지만 gateway 모델은 모든 요소를 보존했습니다.

  - **이 저장소의 번역은 더 이상 유료 API를 거치지 않습니다.** `regen_translations.sh`은 `.env`에 키가 있으면 곧바로 OpenAI API를 사용했으며 Codex는 opt-in으로만 제공했습니다. 이번 버전을 준비하면서 정확히 이런 일이 발생했습니다. 사용량에 따라 비용을 내지 않기 위해 ChatGPT 구독이 존재하는데도 28개 번역이 OpenAI API를 통해 실행되었고, 이어서 힌디어 CHANGELOG는 Gemini API를 통해 실행되었습니다. 키 자동 감지는 제거됩니다. **기본값은 품질 모델인 `gpt-5.6-sol`을 사용하는 Codex입니다.** `openai`, `gemini`, `grok`은 `REGEN_PROVIDER` 외에 `REGEN_ALLOW_PAID_API=1`도 요구합니다. 이는 결정 시점에 규칙이 실제로 적용되도록 이름을 부여한 예외 승인입니다. 알 수 없는 `REGEN_PROVIDER`은 API로 대체되지 않고 실패합니다. 테스트 열 개가 기본값, 거부, 예외 승인을 고정합니다. 이 버전의 번역 28개는 Codex를 통해 다시 수행했습니다.

  - **rate limit에 대한 back-off를 공통화했습니다**(`_retry_on_rate_limit`). Codex와 Grok의 loop는 label만 다르고 동일했으며, 세 번째 복사본을 만들면 중복 기준치를 넘었을 것입니다. 세 CLI 오류는 동일한 `_CliCallError`에서 파생됩니다. 테스트는 세 오류 중 어느 하나라도 이 계층을 벗어나는 것을 금지합니다. 벗어나면 공유 loop가 해당 오류를 더 이상 감지하지 못하기 때문입니다.
  - **테스트**: 새 파일 `tests/test_opencode_provider.py`(51개 테스트) — 완전한 출력 계약, 에이전트 폴백, 로그에서 읽은 원인, 중복 제거된 텍스트 파트와 무시되는 합성 파트, 프로세스 그룹을 종료하는 타임아웃, 429에 대한 백오프, 필수 및 검증된 모델, 비밀 정보 없는 프리플라이트, 바이너리 해석, 디스패치 연결, 파일명 레이블 및 경로 순회 반증 테스트. `tests/test_review_hardening.py`은 플래그의 상호 배타성과 비밀 정보 부재 검사를 새 provider까지 확장한다. 이제 gate는 문서화된 argparse **플래그 22개**를 요구한다. 전체 제품군은 **382개 테스트**다.

- **1.11.1** 문서 수정: 마침내 README에 7가지 provider 경로가 명시되었다(2026-09-03).

  - **1.11.0의 PyPI 페이지에는 「API 4개 + Codex CLI」라고 적혀 있었다.** 코드는 7가지를 제공한다. API를 통한 OpenAI, Mistral, Claude, Gemini, Grok과 사용량 기반 과금 없이 구독으로 사용하는 Codex(ChatGPT) 및 Grok이다. 소개 문구와 _Multi-Provider_ 항목에 두 Grok 모드가 빠져 있었고, 14개 번역에서도 같은 오류가 반복되었다. 패키지의 긴 설명은 버전별로 고정되므로 공개 페이지를 수정하려면 새 버전 번호가 필요했다. 이것이 이 버전의 유일한 존재 이유다. **코드 변경은 없다.**
  - `CLAUDE.md`은 릴리스에서 도입된 내용과 일치하도록 정비되었다. gate 카운터(`--full`에서는 16, 17), 활성 workflow 11개, `gh pr checks`에 표시되지 않는 Sonar/Codacy 카운터 2개(hotspot, Codacy API), `ruff-format`에 의한 `# nosemgrep` 하나의 이동, OIDC 교환에 필요한 GitHub environment, 그리고 _pending publisher_가 이름을 선점하지 않는다는 사실이 반영되었다.

- **1.11.0** PyPI 릴리스: 저장소를 복제하지 않고 `pip install ai-powered-markdown-translator` 후 `aipmt` 명령 실행(2026-09-03).

  - **단일 파일 스크립트가 설치 가능한 패키지가 되었다.** `translate.py`은 루트에서 `src/aipmt/translate.py`로 이동하며, console entry point `aipmt`과 이에 상응하는 `python -m aipmt`를 제공한다. 기여하려면 여전히 저장소를 복제해야 한다. 테스트, 28개 번역, 품질 도구가 그곳에 있기 때문이다. 하지만 사용하는 데는 더 이상 복제가 필요하지 않다.

    - **import 이름은 `aipmt`이며 절대 `translate`이 아니다.** 충돌이 실제로 발생하며 아무 경고도 없기 때문이다. PyPI 패키지 `translate`(v3.8.1, 마지막 업로드 2026-07-06)은 같은 이름의 디렉터리를 설치한다. venv에서 재현한 결과 디렉터리가 모듈보다 우선하고, `translate.main`가 사라지며, entry point가 `AttributeError`에서 깨진다. 그런데도 `pip check`는 「깨진 요구 사항이 없습니다」라고 응답하며 rc=0을 반환한다. 사용자가 단순히 `pip install translate`을 실행하는 것만으로도 유용한 진단 없이 CLI가 깨질 수 있었다. 실제 wheel을 사용한 반증 테스트에서는 해당 패키지 위에 `pip install translate`을 설치했고, 전후 모두 `aipmt --help`이 rc=0이었으며 두 CLI가 공존했다.
    - **긴 배포 이름, 짧은 명령어.** `ai-powered-markdown-translator` 덕분에 PyPI 검색으로 패키지를 찾을 수 있다. 약어만으로는 이미 프로젝트를 아는 사람이 아니면 찾을 수 없으며, 이번 릴리스의 목적은 바로 검색을 통해 발견되도록 하는 데 있다. 그럴듯한 후보 2개는 확인 후 제외했다. `ai-markdown-translator`은 같은 목적의 도구가 2024년부터 npm에서 이미 사용 중이며 이 저장소보다 17개월 앞선다. `aimt`은 같은 분야에서 활발히 유지되는 패키지 `aim`(v3.29.1)과 글자 하나만 다르다. 지속적인 혼동을 일으키기에 최악의 조건이다. 방법론상의 함정도 있었다. `pypi.org/project/<nom>/`은 어떤 이름에도 200을 반환하는 안티봇 페이지이므로 JSON API만 신뢰할 수 있다.
    - **평면 패키지 대신 `src/` layout.** 평면 패키지는 테스트의 `sys.path.insert(..., "..")` 6개를 유지할 수 있었겠지만, 바로 그것이 문제다. 이 설정은 패키지가 아니라 소스 트리를 import하므로 패키징 오류를 모두 숨길 수 있다. 실제 비용은 치환 규칙 하나를 추가하는 것뿐이다.

  - **이제 키를 한 번만 설정하면 된다.** 설치된 CLI에는 영구 설정이 전혀 없었다. 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었다. `find_dotenv`은 시스템 루트까지 거슬러 올라가므로 **홈 디렉터리 아래에서 작업할 때는** `~/.env`을 찾았지만, 다른 위치에서 작업할 때는 아무것도 찾지 못했다. 이는 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라지는 설정 범위였다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`가 추가되었다.

    - **우선순위는 코드에 명시되어 있지 않으며**, `load_dotenv`의 기본값인 `override=False`에서 자연스럽게 도출된다. 각 계층은 앞선 계층이 비워 둔 값만 채운다. 따라서 환경 변수 → 프로젝트의 `.env` → 사용자 설정 순서가 된다. 이는 구조가 아니라 동작 테스트로 검증된다. 두 호출의 순서를 바꾸거나 세 번째 계층을 제거하면 테스트가 실패한다.
    - 의도적으로 TOML이 아닌 **`.env` 형식**을 사용한다. `python-dotenv`는 이미 의존성이며, 해당 문법은 15개 README에 이미 문서화되어 있고, 같은 파일을 두 범위에서 모두 사용할 수 있다. 새로운 의존성이나 문법은 없다. 위치는 `XDG_CONFIG_HOME`가 **절대 경로**일 때 이를 따르고, Windows에서는 `APPDATA`을 따른다. 사양상 상대 값은 무시해야 한다. 그렇지 않으면 설정 위치가 다시 현재 디렉터리에 종속되기 때문이다.
    - **두 가지 선택지는 이유와 함께 제외했다.** 시스템 keyring(`keyring`)은 데스크톱에서는 더 안전하지만 headless 환경, 즉 서버, 컨테이너, CI에서는 실패한다. 이는 바로 일괄 번역의 주된 사용 사례다. 선택 기능으로는 적합하지만 기본값으로는 부적합하다. `--api-key` 플래그는 키를 shell history에 남기고 `ps`에 노출한다.
    - **키가 없을 때 더 이상 호출 스택을 표시하지 않는다.** 이전에는 `site-packages`을 가리키는 Python stack trace와 함께 「환경 또는 .env」를 언급하면서 두 번째 파일을 어디에 만들어야 하는지는 알려 주지 않는 메시지가 표시되었다. 이제 세 위치와 각각의 정확한 경로를 열거하며, 명령은 코드 2로 종료된다. 안전망은 **의도적으로 좁게** 설정했다. `except ValueError`은 설정 단계에만 적용된다. 전체 실행을 감싸면 번역 도중 발생한 실제 버그가 안심시키는 메시지로 바뀌는데, 이는 이 저장소가 추적하는 바로 그 실패 방식이다. 테스트는 이를 금지하기 위해 `main()`의 소스를 읽는다.

  - **수정 — 도구를 설치하면 사용자의 `.env`이 무시되었다.** 인수 없는 `load_dotenv()`은 현재 디렉터리부터 거슬러 올라가지 않고 호출한 파일, 즉 `site-packages`부터 거슬러 올라간다. 자체 `.env`이 있는 프로젝트에서 실제 console entry point를 실행해 측정한 결과, `find_dotenv()`은 `''`을 반환하고 키를 불러오지 못했지만 `find_dotenv(usecwd=True)`는 키를 찾았다. 도구가 복제된 저장소에서만 실행될 때는 이 버그가 존재하지 않았다. 릴리스 후에는 올바르게 설정했는데도 API 키가 「누락」되었다는 증상만 남긴 채 항상 발생했을 것이다.

  - **세 개의 gate는 아무것도 검증하지 않게 되었어도 통과했을 것이다.** 의도적으로 이동 전에 강화했다. 잡아내야 할 변경이 끝난 뒤에 작성한 안전장치는 아무것도 증명하지 못하기 때문이다. 각 gate는 원래 저장소에서는 통과하고 마이그레이션된 복사본에서는 실패한다. 양방향 모두 측정했다.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시한다.** rc=0과 「분석된 파일 0개」를 반환한다. 복잡도 gate는 158개 함수/2247 nloc에서 3개 함수/34 nloc로 줄고 출력은 0바이트가 되었을 것이다. 이제 scope는 각 항목의 존재 여부를 검증하는 배열이다.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`은 실패하지 않는다.** stderr에만 경고하고 unittest와 `coverage xml` 모두 rc=0을 반환하며 보고서까지 게시된다. statements가 1453개에서 141개로 잘린 상태다. 거의 분석되지 않았기 때문에 프로젝트가 정상으로 보였을 것이다. 두 가지 하한이 보고서를 지킨다. 전체 수와 측정된 가장 큰 파일의 수다.
    - **번역 최신성 probe는 호출 형식을 구조적으로 인식하지 못한다.** argparse 플래그를 기준으로 삼는데, 파일명을 바꿔도 플래그는 변하지 않기 때문이다. 재현 결과 모듈을 이동하고 15개 README에 존재하지 않는 명령을 계속 문서화해도 「오래된 번역 없음」이라는 판정이 나왔다. 따라서 일곱 번째 섹션에서는 옵션이 아닌 호출 **형식**을 검증하며, Lizard hook은 스크립트의 실제 scope와 대조된다. `files:` 키는 더 이상 일치하지 않아도 pre-commit을 실패시키지 않고 해당 검사를 **건너뛴다**.

  - **`requires-python = ">=3.10"`은 더 이상 검증되지 않은 주장이 아니다.** `sonar-project.properties`는 개발 환경에 3.12만 있었고 실제로 아무 버전도 테스트하지 않았는데도 이미 3.10~3.12를 명시했다. 릴리스로 공개될 뻔한 내부 모순이었다. 이제 test workflow가 3.10, 3.11, 3.12에서 제품군을 실행하며, **패키지**를 설치하므로 공개된 버전 범위도 함께 검증한다.

  - **하한만 두고 상한은 두지 않는다.** `requirements.txt`는 테스트되는 lock으로 유지되고, `[project.dependencies]`은 공개 계약이 된다. lock의 정확한 버전을 그대로 게시하면 다른 패키지를 사용하는 모든 사용자에게 충돌을 일으킬 수 있다. `<N+1` 상한도 두지 않는다. 이는 major 업데이트 지연 시 release gate를 실패시키는 `check-deps-fresh.sh`과 정면으로 모순되기 때문이다. 하한 집합은 올바르게 해석되며, 반증 테스트 `openai==1.0.0`는 `ResolutionImpossible`으로 종료된다. 이는 검사가 모든 것을 허용하지 않고 구별해 낸다는 증거다. 또한 안전장치는 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지는 것을 금지한다. PyPI는 버전 번호 재사용을 허용하지 않기 때문이다.

  - **새 venv에서 처음부터 끝까지 검증했다.** 약 70KB의 wheel에는 `aipmt/*.py`, dist-info, 라이선스만 포함된다. `aipmt --help`은 22개 플래그와 함께 rc=0을 반환한다. `python -m aipmt`는 「usage: \_\_main\_\_.py」가 아닌 「usage: aipmt」를 표시한다. `pipx` 설치도 정상 작동한다. 무엇보다 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행해 굵은 글씨, 목록, inline code, 링크와 URL이 보존되고 code block은 번역되지 않는 것을 확인했다. 마이그레이션 전의 318개 테스트는 전후 식별자 목록이 바이트 단위로 완전히 같은 상태에서 통과한다. 테스트가 무력화되지 않았음을 증명하는 것은 「OK」가 아니라 바로 이것이다. 3계층 설정을 위한 테스트 12개가 추가되어 총 330개가 되었다.

- **1.10.0** `--use_codex` provider(ChatGPT 구독 quota), SDK 및 모델 업데이트, 여러 문단에 걸친 news 인용 수정(2026-08-29).

  - **보안 검토 — PR에서 마련했지만 모든 곳에서 지키지는 못한 두 가지 안전장치**:

    - **Codex 프리플라이트가 `.env` 전체를 바이너리에 전달했다.** `_codex_preflight`은 `env=` 없이 `subprocess.run`을 호출했다. 따라서 하위 프로세스는 `os.environ` 전체를 상속했고, 그 결과 `load_dotenv`이 불러온 `.env` 전체도 상속했다. 계측된 가짜 바이너리로 측정한 결과 **7개의 비밀 정보**, 즉 6개 provider의 키와 `GITHUB_TOKEN` 하나가 프리플라이트에 도달했다. 반면 대응하는 `_grok_preflight`는 `env=_grok_env()`을 올바르게 전달해 비밀 정보가 **0개**였다. 이는 PR 내부의 불일치였다. 불과 몇 줄 떨어진 곳에 바로 이 불변 조건을 지키기 위한 `_strip_secret_env`이 존재하기 때문이다. `_codex_env_base()`을 추출해 두 경로에서 공유하도록 했다. 수정 후 측정 결과 양쪽 모두 비밀 정보가 0개였다.
    - **「`--deny` fail-closed」 속성이 실제 사용 형식을 다루지 못했다.** 주석은 알 수 없는 prefix의 규칙이 시작을 거부한다는 점을 Grok 격리 전체의 근거로 들었다. `grok 1.0.13`에서 측정한 결과 이 검증은 **괄호 형식에만** 존재했다. `--deny 'CeciNestPasUnOutil(*)'`은 시작을 거부하지만(「알 수 없는 도구 prefix」), `--deny 'CeciNestPasUnOutil'`는 아무 경고 없이 허용된다. 그런데 `GROK_DENY_RULES`은 괄호 없이 이름만 사용했다. 따라서 xAI가 도구 이름을 바꾸면 OS sandbox조차 적용되지 않는 환경에서 유일하게 측정된 격리 계층이 아무 신호 없이 제거될 수 있었다. 이름이 지정된 8개 규칙을 `Prefix(*)`로 바꾸고 각각 CLI가 인식하는 prefix인지 검증한다. catch-all `*`는 유일하게 허용되는 literal 형식을 유지한다. 테스트는 검증되지 않는 형식으로 되돌아가는 것을 막는다.
    - **그 밖의 부분도 안전한 것으로 검증했다.** command injection은 없으며 모든 곳에서 리스트 형식을 사용하고 `shell=True`은 절대 사용하지 않는다. 문서 내용은 stdin 또는 `--prompt-file`로 전달된다. 안전하지 않은 deserialization도 없으며 타입 검사와 함께 `json.loads`만 사용한다. 7개 payload에서 우회할 수 없는 경로 순회 수정도 확인했다. `--deny '*'`가 CLI에 실제로 적용되어 workdir 밖을 읽을 때 `DENY_ENFORCED`이 관찰되었다.
    - 앞에서 추가한 최신성 검사는 자체 원칙도 우회하고 있었다. PyPI 요청이 실패한 패키지를 아무 경고 없이 건너뛰고 gate는 통과했다. 이제 실제로 비교한 패키지 수를 세며 coverage가 불완전하면 실패한다.

  - **의존성을 최신 상태로 올리고, 다시 뒤처지지 않도록 두 가지 안전망을 추가했다**:

    - **지연은 실제로 존재했고 오래 지속되었다.** `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22**로 업데이트했다. 모든 provider 호출의 TLS를 검증하는 root certificate store는 2년이나 뒤처져 있었다. 확인된 원인은 **`.github/dependabot.yml`가 존재하지 않았다는 것**이다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하며, Dependabot은 CVE의 영향을 받는 의존성에만 PR을 제안한다. 그래서 `urllib3`와 `idna`은 올렸지만 두 SDK는 major 버전 하나만큼 뒤처지게 내버려 둔 이유가 설명된다.
    - **이전 추론에서 우려했던 것과 달리 두 major 버전은 충돌 없이 공존한다.** `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**로 마이그레이션하지만, `mistralai`과 `google-genai`은 `httpx<1`에 남는다. 그러나 이들은 서로 다른 distribution이다. 실제 설치로 검증한 뒤 **7개 provider 경로 모두를 처음부터 끝까지 테스트했다.** OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI 각각의 출력에서 inline code와 링크가 보존되었다. 「HTTP stack 두 개를 피한다」는 것은 선호 사항이지 제약 조건이 아니었다. 측정으로 결론을 내렸다.
    - **`requirements.txt`은 실제 환경을 설명하지 못했다.** `google-auth`, `cryptography`, `opentelemetry` stack은 작업 venv에 설치되어 있었지만 선언된 적이 없었다. 따라서 새로 설치한 환경은 테스트 환경을 재현하지 못했다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`는 아무 곳에서도 import하거나 요구하지 않는데도 파일에 포함되어 있었다. `mistralai` 1.x의 잔재였다. 이 파일은 직접 의존성만으로 구축한 venv의 완전한 closure로 다시 생성했다. `pip-audit`은 새 구성에서 알려진 취약점을 하나도 보고하지 않는다.
    - **`.github/dependabot.yml`**(신규)는 pip 및 github-actions의 주간 버전 업데이트를 활성화한다. minor와 patch 업데이트는 하나의 PR로 묶는다. patch 업데이트마다 PR을 하나씩 만들면 결국 무시되며, 소음은 업데이트의 적이기 때문이다. **major 업데이트는 분리하며**, 각각 실제 호출을 통한 검증이 필요하다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 지연을 프로젝트 판정에 드러낸다. Dependabot은 제안할 뿐 보장하지 않으며 PR이 쌓일 수도 있다. major 지연은 실패로 처리한다. minor는 경고만 표시한다. 계속 빨간 gate는 결국 무시되기 때문이다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 건너뛰고 **CI에서는 fail-closed**한다. 실행되지 않은 검사는 성공이 아니다. 양방향으로 검증했다. 수정 전의 정확한 상태인 `openai 2.54.0→3.6.0`와 `certifi 2024.8.30→2026.7.22`를 감지하며, minor 업데이트에는 경고만 표시한다.

  - **이 PR 검토에서 나온 수정 사항** — 5개의 검토 에이전트가 diff를 철저히 살폈다. 아래 항목은 모두 수정 전에 **측정을 통해 재현**했으며, 그중 2개는 이 버전의 앞부분에서 새로 도입된 회귀였다.
    - **회귀 수정 — `_NEWS_CITATION_REGEX`에 지수적 백트래킹이 있었습니다.** 여러 문단 수정에서 반복문에 `(?:[ \t]*$|[ \t]+.*)`이 도입되었습니다. `[ \t]+`과 `.*` 사이의 공백 분배가 모호했고, 이 모호성은 반복할 때마다 증폭되었습니다. 패턴과 일치하지 않는, 완전히 유효한 Markdown 들여쓰기인 `>   texte` 줄에서 측정한 결과, **14줄에 2,589ms**가 걸렸지만 수정 후에는 0.04ms였으며 줄을 추가할 때마다 약 9배씩 증가했습니다. `--news` 모드에서는 길고 규격에 맞지 않는 blockquote 하나만으로도 식별 가능한 원인 없이 작업 시간 초과까지 번역이 멈췄습니다. 이제 반복문은 전체 줄을 한 덩어리로 소비하므로(`\n^>(?![ \t]*—).*`), 반복마다 일치시킬 수 있는 방법이 하나뿐입니다. 실제 231개 문서 말뭉치에서 검증한 결과, 캡처 차이는 **전혀 없었고**, 동일한 423개 인용문이 유지되었으며 여러 문단으로 된 14개 본문도 계속 확장됩니다.
    - **두 provider 플래그를 동시에 사용하면 아무런 알림 없이 사용량 기반으로 요금이 청구되었습니다.** `--use_codex --use_mistral`이 허용되었고, `_select_provider_client`은 Mistral을 먼저 검사하며 `_resolve_provider`는 명시적 불리언에 우선순위를 부여했기 때문에 둘 다 Mistral로 수렴했습니다. 따라서 사용자는 구독 할당량을 요청했지만 아무런 경고 없이 사용량 기반 요금이 청구되었습니다. 이는 바로 `--use_codex`이 방지하기 위해 존재하는 실패 방식입니다. 이제 여섯 개의 provider 플래그는 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경**: 이전까지 조용히 허용되던 두 provider를 결합한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 종료 gate는 자체 검사가 실패해도 통과 상태가 되었습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개는 반환 코드를 전혀 확인하지 않은 채 “stdout을 캡처하고 비어 있으면 결론을 내리는” 패턴을 따랐습니다. 예외가 발생하면(파일 이름 변경, `FileNotFoundError`) stderr에 기록되고 stdout은 비어 있었으므로 검사는 “보고할 내용 없음”으로 결론 내렸습니다. 이를 방지하려고 작성한 스크립트 내부에서 “`exit 0`은 아무것도 증명하지 않는다”는 함정이 재현된 것입니다. 이제 `probe()` helper는 반환 코드가 0이고 **동시에** 종료 sentinelle이 있을 것을 강제하며, 검사 지점 집합이 비어 있으면 결론을 거부합니다. 빈 집합에 대한 assertion은 항상 참이기 때문입니다. 입증 사례로, 위의 상호 배타적 그룹을 추가하면서 provider 플래그가 `*_group` 객체를 통하게 되었고 기존 regex인 `parser\.add_argument\(`은 더 이상 이를 일치시키지 못했습니다. 그 결과 **21개 중 6개 플래그**가 아무런 알림 없이 범위에서 빠졌는데도 gate는 통과 상태였습니다.
    - **secret 스캔이 여섯 provider 중 네 개를 놓쳤습니다.** `[A-Za-z0-9]` 클래스는 하이픈을 제외하므로 `sk-proj-…`(현재 OpenAI 형식)과 `sk-ant-api03-…`은 두 번째 하이픈에서 끊겼고, `AIza…`은 적용 대상에 포함되지 않았습니다. 패턴을 확장하고 `.secrets.baseline`는 스캔에서 제외했습니다. 또한 `.env` guard는 index만 보는 `git diff --cached`을 조회했습니다. 따라서 최악의 경우인 **이미 커밋된** `.env`은 절대 나타나지 않았습니다. 이제 `git ls-files`을 조회합니다.
    - **Codex의 “token warm-up”은 실제 warm-up이 아니었습니다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`을 건드리지 않으며 mtime과 크기도 변하지 않습니다. 도움말에는 “Show login status”라고 되어 있습니다. 그런데 주석에서는 token을 “한 번 순차적으로” 갱신하여 일회용 순환 token의 동시 refresh 위험을 제거한다고 주장했습니다. 설명된 보호 기능은 존재하지 않았습니다. 이제 주석은 코드가 실제로 하는 일을 설명하며, 진짜 대응책은 여전히 `max_jobs=4`입니다. 또한 검사는 이전에 무시하던 `CODEX_BIN`을 준수합니다. `PATH`에 `codex`이 없는 환경에서는 “인증되지 않음”으로 실패하여 오해를 부르는 진단을 내렸습니다.
    - **`.env`을 subshell에서 source했습니다.** `detect_provider`이 명령 치환에서 호출되므로 해당 export가 상위 shell에 전달되지 않았습니다. `.env`에 정의된 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`는 `main()`에서 수행한 읽기에 보이지 않았고, 올바른 설정에서도 “Grok 바이너리를 찾을 수 없음”으로 결론 내렸습니다.
    - **동시 실행 수가 명시된 상한을 50% 초과했습니다.** guard가 README/CHANGELOG 쌍을 실행한 뒤에 배치되어 있었기 때문에 `max_jobs=2`에서 측정된 최대치는 **3**이었습니다. 주간 할당량이 Chat/Imagine/Voice와 공유되고 측정할 수 없는 Grok에서는 스크립트가 자체적으로 정한 상한조차 지키지 못한 셈입니다. 한편 최종 개수는 표시만 하고 28과 비교하지 않아 파일 하나가 빠져도 감지되지 않았습니다.
    - **Grok 출력 계약: 이제 `stopReason`이 없으면 실패합니다.** 명시된 계약에서는 `end_turn`을 요구하지만 코드는 “`end_turn` **또는 없음**”을 적용했습니다. 해당 필드가 없는 payload나 CLI 업데이트로 필드 이름이 변경된 payload는 guard를 아무런 알림 없이 no-op으로 만들었습니다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류되지 않습니다. 이는 turn budget이 소진된 것이므로 재시도하면 90초를 기다리는 비용을 들이고도 같은 결과가 반복됩니다. `quota`도 rate limit marker에서 제외했습니다. `_codex_is_rate_limited`의 docstring에 이미 명시되어 있었지만 Grok에는 적용되지 않았던 이유 때문입니다.
    - **Gemini cascade는 모델별로 memoization됩니다.** 기본 모델이 거부하는데도 각 segment마다 `minimal`부터 다시 시작했습니다. 따라서 정상 경로에서 segment마다 400 응답 왕복 비용을 치르고 같은 경고를 다시 출력했습니다. 수백 번 반복되는 warning은 더 이상 읽히지 않으며, 그렇게 경고가 가림막이 됩니다.
    - **기타**: CI의 거부 메시지가 Codex용으로 하드코딩되어 `--use_grok_cli` 사용자를 `XAI_API_KEY`이 아니라 `OPENAI_API_KEY`으로 안내했습니다. `provider.capitalize()`은 “Grok_cli”와 “Openai”를 표시했습니다. subprocess 기반부의 주석은 “shim”을 두 CLI 모두에 일반화했지만 Grok 바이너리는 네이티브 ELF입니다. 올바른 근거는 “자체 subprocess를 생성하는 agent”입니다. `subprocess`에 대한 SAST finding 12개는 근거와 함께 `# nosec` / `# nosemgrep`로 표시되었습니다. `shell=True` 없는 목록 형식에서는 injection이 불가능하며 문서 내용은 argv를 절대 거치지 않습니다.
    - **이제 agentic subprocess에는 어떤 secret도 전달되지 않습니다.** 이름 기반 deny-list는 **요금 청구** 불변 조건만 보호했습니다. Codex에는 `OPENAI_API_KEY`이 없고 Grok에는 `XAI_API_KEY`가 없도록 했습니다. 측정 결과 **다른 secret 7개**가 여전히 모든 subprocess에 전달되었습니다. Anthropic, Mistral, Google, Gemini 키, 다른 CLI의 키, 그리고 secret은 아니지만 트래픽 경로를 바꾸는 `OPENAI_BASE_URL`입니다. 그런데 이 두 CLI는 **agent**이며, Grok agent는 많은 Linux 환경에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 필터링은 이름 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)을 기준으로 수행됩니다. 따라서 코드가 알지 못해도 사용자가 `.env`에 추가한 변수까지 포함됩니다. CLI에는 어떤 변수도 필요하지 않습니다. 인증 정보는 환경 변수가 아니라 `~/.codex`와 `~/.grok`에 있습니다. 강화된 환경에서 두 provider를 각각 사용해 **실제 번역을 성공적으로 완료하여** 검증했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`의 테스트 21개가 provider 플래그의 상호 배타성, `stopReason` 계약, news regex의 선형성, CI 거부 메시지, Gemini memoization, subprocess 환경에 모든 secret이 존재하지 않음을 고정합니다. 마지막 assertion은 **일반적**이어서 어떤 목록에도 이름이 없는 키에도 실패합니다. 기존 제거 테스트는 자체 상수를 그대로 비추는 거울이어서 자체 반복문의 고장 외에는 아무것도 감지할 수 없었습니다. 전체 suite는 **311개 테스트**입니다.

  - **새 Grok provider 두 개**: `--use_grok`(xAI API, 키 `XAI_API_KEY`, 사용량 기반 요금)과 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독에서 차감되며 `--use_codex`과 같은 원리).
    - **API 모드, 약 40줄**: xAI endpoint는 OpenAI와 호환되므로 client와 `_call_openai`을 그대로 재사용하고 `base_url`만 변경합니다. 단 하나의 조정만 필요했으며 모든 provider에 도움이 됩니다. 이제 `finish_reason`은 OpenAI가 `stop`을 내보내는 위치에서 xAI가 내보내는 형식인 `end_turn`을 허용합니다. 모델: `grok-4.6`(품질)과 `grok-4.3`(경제성). 참고로 Grok의 경제형 모델은 여전히 저장소에서 가장 비쌉니다. 100만 token당 $1.25/$2.50이며 `mistral-small-latest`은 $0.15/$0.60입니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택합니다.
    - **CLI 모드**: Codex를 본떠 만들었지만 실제 환경에서 요구되는 네 가지 차이가 있습니다. prompt는 파일로 전달되고(`--prompt-file`, CLI가 stdin을 읽지 않으며 segment를 argv에 넣으면 `ps`에 표시됨), 출력은 stdout의 단일 JSON 객체이며 JSONL도 `-o` 파일도 아닙니다. 구독에서는 `grok-4.6`과 `grok-4.5`만 제공되고, sandbox는 적용할 수 없습니다(아래 참조). subprocess 실행은 `_codex_run_process`에서 Codex와 함께 공통화했으며, 이미 테스트된 Codex provider의 나머지 부분은 건드리지 않았습니다.
    - **`exit 0`은 아무것도 증명하지 않는다는 것을 측정으로 확인했습니다**: 인증되지 않은 상태에서 CLI는 반환 코드 **0**과 함께 `{"type":"error","message":"Not signed in."}`을 **stdout**에 씁니다. 거부나 turn 초과도 동일하게 동작합니다. 따라서 출력 계약은 네 가지 조건을 동시에 요구합니다. 반환 코드 0, 오류 payload 없음, `stopReason == end_turn`, 비어 있지 않은 텍스트입니다. preflight도 같은 논리를 따릅니다. `grok models`은 연결이 끊긴 상태에서도 0으로 종료되므로 stdout에 “not authenticated”가 있는지만으로 판단할 수 있습니다.
    - **격리: 비대칭성을 의도적으로 수용하고 문서화했습니다.** Codex는 `--sandbox read-only`에서 실행되지만 Grok sandbox는 최근의 많은 Linux 환경에서 적용할 수 없습니다. 이는 `sudo` 없이는 우회할 수 없는 서로 독립적인 두 시스템 원인 때문입니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`이 `0700`에 있으면 container runtime socket의 deny-list가 실패합니다. resolver는 `ErrorKind::NotFound`만 처리하며 EACCES는 치명적 오류가 됩니다. 핵심 함정은 적용할 수 없는 **내장** 프로필이 아무런 알림 없이 **격리되지 않은 상태로 실행된다**는 점입니다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않고 절대 조용히 fallback하지 않으며 stderr에 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하고 catch-all `*`도 포함합니다. 이는 측정 결과 _fail-closed_로 동작하는 유일한 계층입니다. 알 수 없는 접두사의 규칙 하나만 있어도 시작을 거부합니다. `GROK_TRANSLATE_SANDBOX=read-only`을 사용하면 이를 필수로 지정할 수 있으며, 시스템이 준수할 수 없으면 시작에 실패합니다.
    - **보호 장치**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`은 subprocess 환경에서 제거됩니다. 키가 있으면 사용량 기반 요금으로 전환되고, 상속된 `GROK_SANDBOX`은 적용할 수 없는 프로필을 강제하면서 오해를 부르는 메시지를 냅니다. MCP/hooks/skills/agents 스위치는 비활성화하고 `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI에서의 거부, process group을 종료하는 timeout, rate limit용 back-off를 적용했습니다. `--max-turns`은 1이 아니라 6으로 고정됩니다. 카운터는 tool turn 뒤에 증가하므로 1로 설정하면 출력이 잘립니다.
    - **할당량**: Grok pool은 주간 단위이며 **Chat, Imagine, Voice와 공유**되고 이를 표시하는 명령은 없습니다. 이는 `account/rateLimits/read`으로 사용량을 산출할 수 있는 Codex와 다릅니다. 따라서 `regen_translations.sh`은 동시 실행을 2로 제한하고 이를 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`에 테스트 24개를 추가했습니다. 전체 suite는 **290개 테스트**입니다.
  - **버그 수정 — 여러 문단으로 된 영어 인용문이 일부만 보호되었습니다(`--news` 모드)**: `_NEWS_CITATION_REGEX`은 인용문 본문으로 **연속된** `>` 줄만 허용했습니다. 인용문이 빈 `>` 줄로 구분된 여러 문단에 걸치면 마지막 문단만 캡처되어 placeholder로 대체되고, 앞 문단은 LLM으로 전달되어 번역된 상태로 돌아왔습니다. 이는 `--news`이 보장하려는 것과 정확히 반대입니다. 이제 반복문은 내부의 빈 `>` 줄을 허용하고 non-greedy 방식으로 동작하여, 처음 만난 빈 줄이 아니라 이탤릭체 줄 앞의 빈 `>`에서 멈춥니다.
    - **측정된 규모**: 실제 문서 198개의 말뭉치에서 인용문 419개 중 11개가 영향을 받았습니다. 회귀는 없습니다. 새 regex는 정확히 같은 수의 인용문을 캡처하고 여러 문단으로 된 본문만 확장합니다. 본문 408개는 동일하고 11개가 확장되었습니다. 귀속 표시 줄 `> — …`은 여전히 본문에 흡수될 수 없습니다(lookahead 유지).
    - **end-to-end 증명**: ja/ar로 번역한 69ko 문서에서, 이전에는 인용문의 첫 문단이 일본어로 `> GLM-5.3がオープンウェイト化。`이 되고 아랍어에서도 마찬가지로 번역되었지만 이제는 `> GLM-5.3 is now open-weight.` 상태로 유지됩니다. 영어 인용문 줄 수는 9줄에서 원문과 같은 10줄로 돌아왔습니다.
    - 참고: 이 결함은 후속 validator에서 감지되지 않았습니다. validator는 인용문의 존재만 확인하고 완전성은 검사하지 않기 때문입니다.
  - **기본 provider에서 측정된 비용 절감**: `_openai_extra_kwargs`은 모델이 `gpt-5`으로 시작하기만 하면 `--eco`에서도 `reasoning_effort="medium"`을 전송했습니다. 열 단어짜리 문장을 번역하도록 `gpt-5.4-mini`에서 측정한 결과, `medium`은 reasoning token 45개와 출력 token 65개를 사용했지만 `none`는 각각 0개와 14개를 사용했습니다. 번역에는 reasoning이 아무런 이점을 주지 않는데도 모든 파일의 모든 segment에서 비용을 지불하고 있었습니다. 이제 기본값은 `--eco`에서 `none`이고 그 외에는 `medium`입니다. CLI에서 명시적으로 전달된 값은 계속 우선합니다. 이제 `--reasoning_effort`은 `low`/`medium`/`high`뿐 아니라 `none`와 `xhigh`도 허용합니다. 모든 값이 모든 모델에서 허용되는 것은 아닙니다. 예를 들어 `minimal`은 `gpt-5.4-mini`에서 거부되며, 기존의 매개변수 없는 retry가 이 경우를 처리합니다.
  - **SDK 업데이트 및 Gemini 마이그레이션**: `google-generativeai`(지원이 2025-11-30에 종료되고 저장소가 보관 처리됨)을 통합 SDK인 **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 다음 `client.models.generate_content(model=, contents=, config=)`을 사용하며, system prompt는 segment에 이어 붙이는 대신 `system_instruction`으로 전달됩니다. `mistralai`은 **2.9.4**로 올라갔고 import는 `from mistralai.client import Mistral`으로 변경됩니다. 이전 방식은 wheel에서 확인한 대로 `ImportError`을 발생시킵니다. `anthropic`는 **0.125.0**, `openai`는 **2.54.0**으로 올렸습니다. 두 HTTP stack이 venv에 공존하지 않도록 `httpx2`으로 전환하기 전의 마지막 버전들입니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5의 제한도 해제했습니다.
  - **문서가 아니라 실제 테스트로 포착한 회귀 두 건**:
    - `anthropic` ≥ 1.0은 `max_tokens`이 10분을 초과할 것으로 예상되는 non-streaming 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 guard는 0.34.2에는 없었고 `max_tokens=32768`을 사용하는 모든 Claude 호출을 중단시켰습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정했습니다. 전체 응답만 사용하는 호출을 streaming으로 전환할 필요가 없습니다.
    - `thinking_level="minimal"`은 Gemini 카탈로그 일부에서만 허용됩니다. `gemini-3.1-flash-lite`은 지원하지만 `gemini-3.7-flash`과 `gemini-3.1-pro-preview`은 400 응답으로 거부합니다. 따라서 OpenAI의 기존 fallback을 본떠 `_gemini_generate_with_fallback`, 즉 `minimal` → `low` → thinking_config 없음으로 이어지는 cascade를 적용했습니다. 최적화 매개변수 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델 갱신**, 각각 실제 호출로 검증: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%), Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜 없는 canonical ID), Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(안정 버전이며 `3.5-flash-lite`보다 저렴함).
 Mistral은 변경되지 않았으며, `mistral-large-latest`은 여전히 네 가지 중 가장 뛰어난 가성비를 제공합니다. 참고: `gemini-3.1-pro-preview`보다 최신인 Pro급 Gemini 모델은 없습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 제품군은 모두 Flash 전용입니다.
  - **Gemini 전환 전 측정한 A/B 테스트**: `README.md`을 `gemini-3.1-pro-preview`과 `gemini-3.7-flash`로 각각 일본어로 번역했습니다. 구조는 완전히 동일했으며(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존), 소요 시간은 **48초 대비 8초**였습니다. 번역이나 비라틴 문자권에서 이 두 모델을 비교한 공개 벤치마크가 없으므로, 이 전환은 그렇지 않았다면 단순한 추정에 의존했을 것입니다.
  - **Claude 응답 블록 필터링**: `_call_claude`은 유형을 필터링하지 않고 `block.text for block in response.content`을 수행했습니다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 중간에 삽입하며, 이 블록은 `.text`이 아닌 `.thinking`을 노출합니다. 따라서 첫 번째 세그먼트에서 불투명한 `AttributeError` 때문에 번역이 실패했을 것입니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result` 블록은 제외되며(텍스트를 포함한 알 수 없는 유형은 허용하기 위해 제외 목록 방식 사용), 텍스트 블록이 하나도 없는 응답은 명시적인 오류를 발생시킵니다. 모든 호출에 `thinking={"type": "disabled"}`이 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 지원 종료일이 지난 모델을 제거했습니다(`magistral-*` 제품군은 2026-07-31, `gemini-2.0-*`은 2026-06-01, `gemini-3-pro-preview`는 2026-03-09에 종료되었으며, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`도 제거). 한도 수정: Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1,000,000 → **1,048,576**(실제 입력 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 제품군을 추가했습니다. 참고: `translate()`이 세그먼트 분할을 `min(16000, limite)`으로 제한하므로 이 한도들은 여전히 참고용입니다.

  - **`--use_codex` Provider**: 사용량에 따라 과금되는 API를 호출하는 대신 공식 Codex CLI(`codex exec`)를 비대화형 모드로 구동하는 다섯 번째 Provider입니다. 번역 사용량은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. OpenAI가 이 용도로 문서화한 유일한 경로입니다. 요금제별 이용 가능 기능 표에는 Plus/Pro/Business/Enterprise에서 “Codex SDK, `codex exec`, 스크립트화 가능한 워크플로”를 사용할 수 있다고 명시되어 있으며, `~/.codex/auth.json`의 토큰은 API Platform 호출 인증에 사용할 수 없습니다. 또한 이 스크립트는 해당 토큰을 읽지 않으며, 인증과 갱신은 계속 CLI가 관리합니다.
  - **이제 npm뿐 아니라 pip로도 설치 가능한 Codex 바이너리**: `_resolve_codex_binary()`은 `CODEX_BIN`, `PATH`, 그리고 OpenAI가 배포하는 공식 Python 패키지 **`openai-codex-cli-bin`** 순서로 바이너리를 검색합니다. 이 패키지는 `openai-codex` SDK의 의존성입니다. 따라서 이제 Python 프로젝트에서 `--use_codex`을 사용하기 위해 npm 전역 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가하지 않았습니다. 바이너리 크기가 약 250MB여서 선택적 Provider를 위해 모든 사용자에게 설치를 강제하게 되기 때문입니다. 전체 흐름을 검증했습니다. `codex`이 `PATH`에 없는 상태에서도 패키지에 포함된 바이너리를 찾아 6초 만에 전체 번역을 완료했습니다.
  - **“구독 모드” 보장**: 하위 프로세스 환경에서 `OPENAI_API_KEY`과 `CODEX_API_KEY`을 제거합니다. 이 보호 장치가 없으면 `.env`에 존재하는 키로 인해 아무런 가시적 알림 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 바로 이것을 방지하기 위해 이 Provider가 존재합니다.
  - **테스트로 방지한 CLI 함정**:
    - 프롬프트를 인수로 전달해도 `codex exec`은 stdin을 **계속** 읽습니다. stdin을 닫지 않으면 모델을 한 번도 호출하지 않은 채 제한 시간까지 명령이 대기합니다(재현 결과: 180초 후 exit 124, 0바이트). 따라서 `communicate(input=...)`은 필수입니다.
    - npm으로 설치된 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 이 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 계속 할당량을 소비할 수 있습니다. 이 때문에 `Popen(start_new_session=True)`과 `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`을 출력하고도 종료 코드 0을 반환할 수 있습니다. 따라서 반환 코드뿐 아니라 JSONL 출력(`--json`)도 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **Rate limit 백오프**: CLI는 내부 재시도를 구현하지 않습니다(`max_retries = 0`). 분류는 하위 문자열이 아닌 JSON 페이로드 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. “quota”라는 단어는 복구 가능한 429와 영구적인 `insufficient_quota` 모두에 나타나기 때문입니다.
  - **CI 보호 장치**: `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 `--use_codex`을 거부합니다. 구독 인증은 공유 runner용으로 설계되지 않았으며, OpenAI도 공개 저장소에서 이 워크플로를 사용하지 말라고 명시적으로 권고합니다.
  - **모델**: `gpt-5.6-sol`(품질)과 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 제품군은 CLI와 API Platform에서 공통으로 사용되지만, ChatGPT 계정으로 모든 모델을 사용할 수 있는 것은 아닙니다. 허용 목록은 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 사용하면 경고가 표시됩니다. Plus 요금제에서 Luna는 5시간 단위로 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개를 제공합니다. 따라서 모든 일괄 처리에는 `--eco` 모드를 권장합니다.
  - **수정된 버그 — 전체 작업에 성공했는데도 `regen_translations.sh`이 오류로 종료됨**: `trap ... EXIT`은 `main()`의 `local` 변수인 `failed_log`을 참조했지만, trap이 실행되는 시점에는 이 변수가 더 이상 존재하지 않았습니다. `set -u`에서 이 때문에 `failed_log: unbound variable`이 발생하여 28개 번역이 모두 올바른데도 스크립트가 종료 코드 1로 끝났습니다. 그 결과 가장 비용이 큰 단계인 재생성 직후 `release.sh --auto`(`set -e`)가 중단될 수 있었습니다. 변수를 전역으로 변경하고 trap에서 변수의 존재 여부를 검사하도록 했습니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 종료 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: `regen_translations.sh`의 새로운 환경 변수로, Provider의 기본값보다 우선하여 특정 모델을 강제로 사용합니다. 예를 들어 대량 처리용 `--eco` 모델 대신 구독 할당량의 최고급 모델로 재생성하려면 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 사용할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 선택했을 때만 `REGEN_PROVIDER=codex`을 사용할 수 있습니다. 사용자가 모르는 사이 구독 할당량을 소비하지 않도록 자동 감지는 절대 하지 않습니다. 병렬 처리를 시작하기 전에 토큰을 순차적으로 한 번 갱신합니다. Codex 갱신 토큰은 순환형이며 일회용이므로 동시 작업이 `codex login` 세션을 무효화할 수 있기 때문입니다. 동시 실행 수는 4로 제한됩니다.
  - **관련 리팩터링**: 전체 호출 체인에 네 번째 boolean을 전달하는 대신 Provider 이름을 반환하는 `_resolve_provider()`을 사용하여 `_dispatch_provider_call`의 매개변수를 8개에서 6개로 줄였습니다. 최소한의 `Namespace`로 `translate(..., use_mistral=True)`을 호출하는 테스트를 보존하기 위해 명시적 boolean은 계속 `args`보다 우선합니다.
  - **테스트**: argv, 정제된 환경, 서문 금지 계약, 조용한 실패, timeout/killpg, 백오프, 사전 점검, Provider 해석, Gemini 추론 단계적 전환, Claude 블록 필터링, 여러 문단으로 된 뉴스 인용을 다루는 새 파일 `tests/test_codex_provider.py`(48개 테스트)을 추가했습니다. 전체 테스트 모음은 290개입니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 기준 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 25행, HTML 링크 13개, 이미지 13개, URL 19개, 코드 블록은 문자 단위로 동일, placeholder 잔여물 0개). 69KB 분량의 뉴스 기사에서 `--news` 모드를 사용했을 때 `gpt-5.6-luna`과 `gpt-5.6-sol` 출력 모두 en/ja/ar용 후속 애플리케이션 validator를 통과했습니다. `account/rateLimits/read`를 통해 측정한 사용량은 `--eco` 모드에서 카운터 반올림 임계값 미만(5시간 기간의 0%)으로 유지되었습니다.

- **1.9.2** 중첩 괄호 또는 FR 접두사가 있는 뉴스 출처 표시 URL 추출 수정(2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`에서 출처 표시 URL을 추출할 때 정규식 `re.search(r"\((.+?)\)", attribution)`을 사용했습니다(괄호 사이를 lazy capture). `(relayé par [@user sur X](https://x.com/.../123))`과 같은 출처 표시에서는 괄호가 중첩되어 있으므로(`(`의 바깥쪽 괄호와 Markdown 링크의 `]()`), 처음 만나는 `)`에서 캡처가 끝났습니다. 그 결과 문자열이 잘리고 FR 접두사까지 포함된 `relayé par [@user sur X](https://x.com/.../123`이 생성되었으며, 마지막 `)`은 누락되었습니다. 이 때문에 `_validate_news_post`가 번역 출력에서 이 문자열을 찾다가 항상 실패했습니다. 원인은 `)`이 잘린 데다 “relayé par”가 `relayed by`/`weitergeleitet von`/… 등으로 번역되었기 때문입니다. low → medium → high → gpt-5.5의 전체 단계적 전환이 모두 통과할 수 없었습니다.
  - **수정 사항**: 정규식을 `re.search(r"\]\(([^)]+)\)", attribution)`로 변경했습니다. Markdown 링크의 `](url)`을 구체적으로 대상으로 삼아 FR 접두사나 잘림 없이 **순수 URL만** 캡처하며, 번역 중에는 `#URL{N}#` placeholder로 이 불변성이 보존됩니다. 다음 두 가지 문제 패턴을 모두 안정적으로 처리합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥쪽 괄호가 없는 FR 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 새 테스트 2개를 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그를 정확히 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`이 포함된 변형)
  - **테스트 범위의 공백**: `check-editorial-coverage.py`은 편집 문법은 검증하지만 translator가 번역할 수 있는지는 검증하지 않습니다. 향후 개선 사항(v1.9.2 범위 밖)으로, 게시 **전에** 위험한 패턴을 감지하도록 dry-run에서 출처 표시 추출을 시뮬레이션하는 검사를 추가할 수 있습니다.

- **1.9.1** 번역 메모 marker의 CTA label i18n 수정(2026-05-10):

  - **수정된 버그**: 번역 파일 상단의 marker 배너에 있는 CTA 링크의 `[Voir le projet sur GitHub ↗]` label이 `target_lang`을 따르지 않고 모든 대상 언어에서 **프랑스어**로 남아 있었습니다. LLM은 이 label을 전혀 보지 못합니다. 저장소 URL과 slug를 보존하기 위해 Python 측에서 조립되기 때문에 번역 단계에서 이를 바로잡을 수 없었습니다. v1.9에서 `marker` 형식을 추가한 이후 발생한 조용한 회귀였습니다.
  - **수정 사항**: 15개 언어를 각 현지화 label에 매핑하는 새로운 상수 `_VIEW_PROJECT_LABELS`을 추가했습니다. 이제 `_translation_note_invariants(target_lang)`와 `_assemble_translation_note_paragraphs(phrase, target_lang)`가 대상 언어를 전달합니다. 언어를 알 수 없는 경우 `fr`으로 대체합니다(KeyError 방지).
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 조정했습니다(target_lang `ja` → 예상 일본어 label). 새 테스트 2개를 추가했습니다. `test_source_link_label_localized_per_target_lang`(라틴 문자, 표의 문자, 아브자드 문자를 포함한 7개 언어를 매개변수화)과 `test_source_link_label_falls_back_to_french_for_unknown_target`입니다. 총 테스트 수는 `test_translation_note_position.py`에서 38개가 아닌 40개입니다.
  - **하위 호환성**: 기본값이 있는 `target_lang="fr"` 시그니처를 사용하므로 `args.target_lang` 없이 호출하는 외부 프로그래밍 호출자는 변경 없이 계속 작동합니다.
- **1.9** silent-failure 수정 + 완전한 품질 도구 체계 + 다중 위치 번역 노트 (2026-05-07):
  - **다중 위치 번역 노트 + "embed card" 마커 형식**:
    - 새로운 CLI 옵션 추가(기본값 변경 없음 → **호환성 유지**):
      - `--note_position {top,bottom,both}`(기본값: `bottom`): 번역된 파일의 상단, 하단 또는 양쪽 모두에 노트를 배치합니다.
      - `--note_format {legacy,marker}`(기본값: `legacy`):
        - `legacy`은 v1.8의 동작을 엄격히 그대로 재현합니다(굵은 단락 `**…**`). **byte-for-byte** 수준으로 동일합니다.
        - `marker`은 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 "GitHub repo embed card" 형태로 렌더링되도록 구성된 **3개 단락의 blockquote**를 출력합니다. 여기에는 inline code로 표시된 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM이 번역한 설명, 화살표가 표시되는 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 포함됩니다. 빌드 시 remark plugin으로 활용할 수 있습니다(jls42.org 블로그의 `remark-translation-banner` plugin 참조).
    - **LLM에 절대 전송되지 않는 불변 요소**: repo 제목과 GitHub URL은 설명 문구가 번역된 후 Python 측에서 조합됩니다. LLM은 `ai-powered-markdown-translator` slug와 `https://github.com/jls42/...`을 절대 보지 않으므로 renderer, 대소문자, scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 노트가 YAML frontmatter를 닫는 `---` 블록 **뒤에** 삽입됩니다(Astro Content Collections / gray-matter 안전성 보장). `_split_frontmatter` helper는 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 보존합니다. 닫는 fence가 없는 열린 frontmatter에서는 **`RuntimeError`을 발생시키며**, 노트가 잘못된 위치에 삽입된 파일을 기록하는 대신 해당 파일이 `failed_files`에 보고됩니다.
    - **Whitelist 기반 모델 sanitizer**: `_sanitize_model`은 `[A-Za-z0-9._:/-]`에 포함되지 않은 모든 문자를 `_`로 바꾸며, 결과가 비어 있으면 `unknown`을 사용합니다. Astro remark plugin 측 validator와 동작을 일치시키고 marker 형식을 손상시킬 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 refactor**: `_append_translation_note`(단일 monolithic 함수) → 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). builder와 composer를 분리했습니다(builder는 구분자 없는 순수 블록을 반환하고, composer는 위치에 따라 `\n\n`을 적용). production 코드와 source helper가 동일한 3단락 assembler를 공유합니다.
    - **공백을 보존하는 `_quote_lines`**: 각 줄 앞에 `> `을 붙이고 빈 줄은 `>`만 있는 줄로 변환합니다. 이를 통해 mdast가 blockquote를 줄바꿈이 포함된 단일 단락이 아니라 서로 구분된 3개 단락(제목 / 설명 / 링크)으로 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 단락 수에 따라 동작합니다(3개 = 완전한 card 형식, 2개 = 문구 + 링크, 1개 = fallback). Markdown 링크 `](`가 감지되면 1단락 fallback은 더 이상 내용을 **`**...**`으로 감싸지 않습니다**(링크 주위의 `<strong>` 렌더링이 불안정하기 때문).
    - **하위 호환성**: `_compose_with_notes` 측에서 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")`을 사용합니다. 이 속성이 없는 Namespace도(기존 테스트 및 외부의 programmatic 호출) 수정 없이 계속 작동합니다.
  - **긴 번역에서 발생하는 silent-failure 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 추가: 결정론적 계층(원문 발췌문이 그대로 남았는지 탐지) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에서 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k segment의 잠재적 truncation 방지 및 FR→JA/ZH/KO/AR/HI cross-script 변환 여유 확보)
    - heading 인식 segmentation: segment 후반부의 H2/H3를 우선하여 각 segment가 완전한 의미 단위의 section으로 시작하도록 개선
    - 오류를 0이 아닌 exit code까지 전파: `translate_markdown_file`이 typed status `success` / `failure` / `skipped`을 반환하며, 하나 이상의 파일이 실패하면 `main()`이 `sys.exit(1)`을 실행(single-file 및 batch 모두 적용)
    - 모든 provider에 empty-content guard 적용, source/output sanity ratio 검사(원문 ≥ 500자이고 출력이 5% 미만이면 거부), code placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 처리 후 정규화(heading에 붙은 구분자/링크 분리), `reasoning_effort` 없이 `BadRequestError` retry
    - `langdetect==1.0.9` dependency 추가
  - **Pre-commit 품질 도구 체계**("완전한 EurekAI 유형", hook 14개):
    - Pre-commit: ruff(lint+format), shellcheck, prettier(md/yaml/json), detect-secrets(API key 4개 보호), Lizard(CCN ≤ 12), pre-commit-hooks v5(공백, EOF, 대용량 파일, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `./venv/bin/python`을 사용하는 local wrapper를 `scripts/`에 배치
    - `scripts/audit_verdict.py`: unittest 11개가 포함된 pip-audit JSON parser로, jls42-astro parser를 Python으로 port한 버전
    - 초기 ruff 위반 7건 수정: B904(raise from) ×2, B007(unused dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard에서 `translate.py`을 일시적으로 제외(CCN 21~47인 함수 4개, refactor 예정). scripts/에는 엄격한 gate 적용
  - **SonarCloud + 포괄적 coverage**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): push와 pull-request마다 분석하며 `coverage.xml`을 통해 coverage 수집
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` stdlib): silent-failure 오류 체인의 6개 연결 지점을 모두 검증
    - `tests/test_orchestration.py`(+79개 테스트): `translate.py`의 orchestration 계층을 검증(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return branch)
    - `scripts/tests/test_audit_verdict.py`: subprocess를 통해 `main()`(stdin/stdout) 및 `if __name__ == "__main__"` 블록의 coverage 확보
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 조합(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 여러 줄 prefix 처리, byte-for-byte 하위 호환성(golden literal), sanitizer, frontmatter 분리(닫히지 않은 fence에서 raise하는 경우 포함), 3단락 형식, 2단락 fallback, 1단락 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않는다고 assert하는 핵심 안전장치 `TestLLMPayloadExcludesInvariants`을 검증합니다. **190개 테스트 통과**, regression 0건.
  - 문서화: badge가 포함된 `README.md`(프랑스어 + 번역 14개), `CLAUDE.md`(pre-commit workflow + 상세한 CI 감시), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 업데이트(2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 고품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 고품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token limit 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder를 통한 영어 인용문 보호, `LANG_FLAGS` mapping(15개 언어), 대상 언어별 flag 관리
  - 복원 전 news placeholder 검증 추가(regression 방지: placeholder를 삭제한 LLM이 인용문 없는 출력을 조용히 생성하던 문제)
  - `regen_translations.sh` script의 이식성 확보(절대 경로 사용, pwd dependency 제거)
  - README/CHANGELOG의 language bar에 프랑스어 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원본 파일명을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **Inline code 보존**: 이제 번역 중 backtick(`` `...` ``)이 보호됩니다.
  - system prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - template variable `{variable}` 보호
    - 요청하지 않은 번역자 주석 금지
  - 364개 파일에서 성공적으로 테스트 완료(jls42.org 블로그 migration)
- **1.6** 새로운 기능:
  - 번역용 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(고품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(고품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(고품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 탐색하지 않는 단일 파일 번역(`--file`)
  - 간소화된 새로운 naming pattern: `{base}-{lang}.md`
  - 모델명이 포함된 이전 형식을 유지하는 `--include_model` 옵션
  - 목록에 없는 모델을 기본 token limit(128k)로 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`로 업데이트.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`로 업데이트.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`로 업데이트.
  - **번역 prompt 최적화:**
    - 직접 번역 및 번역 노트용 prompt를 더 명확하고 효율적으로 개선했으며, metadata와 특정 서식 요소 보존에 관한 상세 지침을 포함했습니다.
  - **코드 refactor:**
    - Mistral AI client 초기화에 사용하던 `MistralClient`을 `Mistral` class로 교체했습니다.
    - 가독성과 유지보수성을 높이도록 import를 재구성했습니다.
    - 번역 중 원래 서식을 보존하도록 텍스트 segmentation과 code block 처리를 개선했습니다.
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 반대로 변경했습니다(예: `f"{base}-{args.target_lang}-{args.model}.md"`). 이를 통해 번역 파일을 더 쉽게 정리하고 찾을 수 있습니다.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 코드를 정리했습니다.
    - script의 구조와 가독성을 개선하기 위한 소규모 조정을 적용했습니다.
- **1.4** 새로운 기능:
  - 번역용 Anthropic Claude API 지원
  - 명확성과 효율성을 높이기 위한 prompt 최적화
  - 코드 유지보수성을 개선하기 위한 소규모 조정
- **1.3** 개선 사항 및 새로운 기능:
  - code block 처리 개선
  - 출력 파일 관리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 모델과 언어의 순서를 반대로 변경
- **1.2** changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 최초 버전 - OpenAI API 지원

**gpt-5.6-sol을 사용해 프랑스어에서 한국어로 번역된 기사.**
