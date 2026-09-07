### 변경 로그

🌍 [프랑스어](CHANGELOG.md) | [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`: 중국의 오픈 모델을 포함해 약 430개 모델로 연결하는 유료 라우터(2026-09-05):

  - **아홉 번째 provider 경로이며, 여덟 번째 경로와 함께 제공됩니다.** 1.12.0은 PyPI에 게시되지 않았으며, 두 라우터 OpenCode와 OpenRouter가 함께 출시됩니다. [OpenRouter](https://openrouter.ai)는 단일 종량제 크레딧과 하나의 키만으로 여기의 다른 어떤 provider도 제공하지 않는 Kimi, Qwen, DeepSeek, Z.ai 등의 모델에 접근하게 해 줍니다. endpoint가 OpenAI와 호환되므로 client는 xAI와 동일합니다. **이 provider를 구별하는 모든 요소는 preflight에 있으며**, 각 규칙은 API 측정 결과에서 비롯되었습니다.

  - **같은 모델이 서로 다른 한도를 가진 수십 개의 호스팅 업체에서 제공되지만, 라우팅은 이를 인식하지 못합니다.** 측정 결과는 `z-ai/glm-5.2`에 33개, `z-ai/glm-5.3-flash`에 23개였으며, 그중 하나는 **출력 2,048 tokens**로 제한되어 있었습니다. 따라서 23개 중 하나로 전달되는 긴 번역은 아무 신호도 없이 무작위로 잘렸습니다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽고 출력 한도가 8,000 tokens 미만인 호스팅 업체, 상태가 저하된 업체, 한도를 선언하지 않은 업체를 제외한 다음 나머지를 고정합니다. `allow_fallbacks: false` **없는** `provider.only`은 선호 설정에 불과합니다. 라우터가 제외된 호스팅 업체로 되돌아가므로 고정은 아무 의미가 없어집니다. 한도를 충족하는 호스팅 업체가 하나도 없으면 명령이 중단됩니다. 그래도 번역을 진행하는 것은 이 preflight가 방지하려는 조용한 잘림을 받아들이는 것과 같습니다.

  - **추론에는 출력 요금이 부과되며, 많은 모델에서 기본으로 활성화되어 있습니다.** `z-ai/glm-5.2`에 동일한 요청을 보내 « OK »라는 응답을 받은 결과, **모델 기본 설정에서는 completion tokens가 107개였고 추론을 끄면 2개였습니다**. 추론이 아무 도움도 주지 않는 번역에서는 모든 파일의 모든 segment마다 18배의 차이가 납니다. 따라서 기본적으로 비활성화됩니다. 추론을 강제하는 **431개 중 288개 모델**(`reasoning.mandatory`)은 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`이라고 응답합니다. 이 모델들에는 추측한 effort를 보내는 대신 아무것도 보내지 않습니다. effort는 추론이 먼저 소비하는 **`max_tokens`의 일정 비율**을 할당하므로, 임의로 선택한 값은 빈 페이지 위험을 줄이지 않고 옮겨 놓을 뿐입니다.

  - **추론을 강제하는 모델에는 허용되는 가장 낮은 effort가 전달되며, 이는 측정을 통해 결정되었습니다.** 처음에는 모델을 대신해 추측하지 않도록 아무것도 보내지 않는 방식을 선택했습니다. catalogue 기본값이 `max`인 `z-ai/glm-5.3-flash`에서 검증한 결과, 이 선택은 번역이 끝나기 전에 **32,768 tokens에서 잘린 출력**을 생성했고 14개 언어 중 2개를 잃었습니다. 범위를 늘려도 달라지지 않았을 것입니다. effort가 그중 일정 비율을 할당하므로 추론도 범위와 함께 커지기 때문입니다. 따라서 provider는 preflight에서 `supported_efforts`을 읽어 가장 낮은 값을 요청하고, catalogue에 사용할 수 있는 값이 없으면 « 아무것도 보내지 않음 »으로 대체합니다. 문제가 발생했던 언어로 반증 시험을 수행한 결과, 이전에는 budget 소진으로 실패했지만 이제는 원본과 동일한 구조를 유지하며 9분 만에 완료됩니다.

  - **이제 upstream 호스팅 업체의 장애에는 해당 업체의 이름이 표시됩니다.** 라우터는 이 사례를 null `native_finish_reason`가 포함된 `finish_reason=error`으로 정규화합니다. 두 언어에서 각각 정확히 750초로 두 차례 측정되었습니다. 일반적인 메시지는 문서나 분할에서 결함을 찾게 만들었지만, 이제는 공급자 측 장애이며 재시도만으로 해결되는 경우가 많다고 안내합니다.

  - **출력이 비어 있는 `finish_reason=length`은 잘림이 아닙니다.** 첫 번째 유용한 문자가 나오기 전에 추론이 budget을 모두 소비한 것입니다. 유용한 tokens 148개에 추론 tokens 15,850개로 측정되었습니다. 두 사례에는 정반대의 조치가 필요합니다. 전자의 경우 segment 크기를 줄여도 소용이 없습니다. 메시지는 두 사례를 명시적으로 구분합니다. 측정 결과를 바탕으로 두 가지 보호 장치도 추가되었습니다. upstream 호스팅 업체가 실패하면 라우터는 **오류만 담긴 본문과 함께 200을 반환**하며(`choices[0]`은 메시지를 가리는 불투명한 `TypeError`을 발생시켰습니다), context window는 catalogue에서 읽어 `MODEL_TOKEN_LIMITS`에 기록합니다. `DEFAULT_TOKEN_LIMIT`은 catalogue의 44개 모델에서 잘못되어 있으며, 그중 두 모델은 4,095 tokens로 제한됩니다.

  - **`--model fournisseur/modèle`은 필수이며, 네트워크에 접근하기 전에 형식을 검증합니다.** OpenRouter는 공급자가 아닙니다. 이 선택은 가격, 라이선스, 데이터 처리에 영향을 주므로 사용자를 대신해 결정하지 않습니다. slug가 preflight URL에 삽입되므로 검증은 단순한 사용성 배려가 아니라 경로 삽입을 막는 보호 장치입니다. 두 라우터가 공유하는 namespace 형식의 regex는 `a/b/..`을 허용하므로 상위 segment를 명시적으로 거부합니다. `--eco`은 아무 효과가 없으며 그 사실을 알립니다.

  - **세 가지 표현을 수정했으며, 그중 하나는 사실과 달랐습니다.** `codex exec`에 관한 OpenAI의 경고는 공개 저장소가 아니라 공유 runner에 개인 session 파일을 삽입하는 문제를 다룬 것이었는데, README와 CLAUDE.md 및 코드에서 반대 의미로 인용되고 있었습니다. OpenCode 인증 위치는 1.18.27에서 변경되어 이제 `auth.json`이 아니라 `opencode.db`의 `credential` table에 있습니다. « 여기서는 절대 읽지 않는다 »라는 invariant는 여전히 참이지만 주소가 오래된 상태였습니다. 마지막으로 OpenCode 섹션은 더 이상 검증하지 않은 경로들을 동등한 것으로 소개하지 않습니다. Zen gateway와 Ollama는 처음부터 끝까지 측정했지만 GitHub Copilot, LM Studio, llama.cpp는 측정하지 않았으며, 이제 README에 이 사실이 명시됩니다.

  - **측정 캠페인을 수행하고 README에 권장 모델 표를 추가했습니다.** 세 가지 문서 세트, 즉 `--news` 모드의 밀도 높은 블로그 글, 표준 Markdown 형식의 이 README, GitHub에서 그대로 가져온 유명 프로젝트 README 네 개를 14개 언어로 번역하며 300회 넘게 실행했습니다. 표는 이전에 혼동하던 두 가지, 즉 **완료되는** 번역과 **구조가 원본과 동일한** 번역을 구분합니다. 밀도 높은 두 문서에서 단 한 번도 정보를 잃지 않은 모델은 세 개였습니다. `gemini-3.7-flash`, ChatGPT 구독을 통한 `gpt-5.6-sol`, OpenRouter를 통한 `z-ai/glm-5.2`이며, 유일한 차이는 한두 언어에서 `**` 한 쌍이 옮겨지지 않은 것이었습니다. 핵심 결론은 **판별 요소가 `--news` 모드가 아니라 문서의 밀도라는 것**입니다. 구독형 Grok은 블로그 글에서 14회 중 13회 실패했지만 공개 README에서는 16회 중 14회 성공했으며, 원인은 반증 시험으로 확인된 긴 segment에서의 이탈이었습니다. 표에는 자체 경고가 포함되어 있습니다. 이 표는 전체 목록이 아니며 특정 시점의 결과이고, 소요 시간은 순위를 의미하지 않으며, 올바른 접근법은 여전히 자신의 문서로 직접 측정하는 것입니다.

  - **구조 비교기가 비라틴 문자 체계에서 두 개의 false positive를 생성했으므로 수치를 게시하기 전에 수정했습니다.** 전각 닫는 괄호 `）`이 뒤따르는 URL은 `)`에서 멈추는 regex로 분리되지 않았고, 그 결과 URL은 동일한데도 추출된 문자열이 달랐습니다. 프랑스어로 다섯 줄인 인용문이 중국어에서는 세 줄에 들어가면서 줄 단위 집계가 감소하기도 했습니다. 두 수정 사항은 반증 시험으로 검증했습니다. URL, 섹션 또는 inline code를 제거하면 여전히 탐지됩니다. 이를 수정하지 않았다면 Gemini와 Codex의 결과는 각각 14개 언어 중 13개와 12개가 아니라 11개로 게시되었을 것입니다.

  - **테스트**: 새 파일 `tests/test_openrouter_provider.py`(39개 테스트) — 모델 검증 및 상위 segment 거부, 호스팅 업체 고정(한도, 상태, 선언되지 않은 한도, 공통 최솟값), 항상 false인 `allow_fallbacks`, `mandatory`에 따라 추론을 끄거나 유지하는 동작, 완전한 출력 contract(200에 포함된 오류, 선택지 없음, 잘림과 구분되는 빈 페이지, 비정상적인 `finish_reason`, null 콘텐츠), 접근할 수 없는 catalogue에서 fail-closed하는 preflight, 누락된 slug와 정상 호스팅 업체 부재, flag 상호 배타성 및 파일 이름 label을 다룹니다. 전체 suite는 **427개 테스트**입니다.

  - **Refactor: 동작을 단 한 줄도 바꾸지 않고 4,253줄짜리 단일 module을 여러 module로 분할했습니다.** `src/aipmt/translate.py`을 `config`, `markdown`, `segmentation`, `guards`, `placeholders`, `news`, `prompts`, `notes`, `naming`, `pipeline`, `cli` 및 하위 package `providers/`로 나눴습니다(provider별 module 하나, 기반 역할의 `base`, resolution과 dispatch를 위한 `registry`). 각 이동은 기계적으로 입증되는 하나의 commit입니다. 검증 도구는 package의 모든 최상위 node AST를 기준 snapshot과 비교하고, 각 symbol의 위치와 보안 marker가 verbatim으로 유지되는지 확인하며, 추적되지 않은 파일이 없는지 검증합니다. 이는 임시 도구로, 다음 버전에서 제거됩니다. 눈에 보이는 변경 사항은 다음과 같습니다. `aipmt.translate`은 module이 `_` prefix 없이 노출하던 64개 이름을 객체 identity 그대로 다시 노출하는 façade가 되며(`__all__`에 지원 API인 9개가 있고 나머지는 호환성 alias입니다), `import *`이 함께 가져오던 dependency 및 표준 library의 29개 이름은 더 이상 재노출하지 않습니다. 파일 직접 실행(`python src/aipmt/translate.py`)은 더 이상 지원되지 않으며 `aipmt`와 `python -m aipmt`이 지원되는 두 가지 형식으로 남습니다. public function의 `__module__`은 해당 function이 정의된 module을 가리킵니다. 알려진 영향 없이 SDK를 `.env` loading 이전이 아니라 이후에 import합니다. 427개 테스트는 identifier까지 그대로 유지하면서 실제로 실행하는 module로 이전했습니다. façade를 거치던 91개 patch는 이제 이름을 조회하는 module을 직접 대상으로 하며, 그중 9개는 patch가 없어도 계속 통과한다는 사실을 측정했습니다. 7개의 contract test가 façade를 고정하며, 어떤 gate도 검증을 중단한 채 통과할 수 없도록 첫 이동 **전에** gate 도구를 다시 작성했습니다. 여기에는 하한이 적용된 directory 단위 Lizard scope, 생성된 parser에서 읽는 flag, package별 coverage 하한, 추적되는 module을 열거하는 `release.sh`이 포함됩니다.

- **1.12.0** Provider `--use_opencode`: 오픈 소스 agent OpenCode를 사용자가 선택한 공급자에 연결 — 로컬 모델, 계정 없는 무료 모델, 구독 또는 키(2026-09-04):

  - **앞선 일곱 경로와 성격이 다른 여덟 번째 provider 경로입니다.** [OpenCode](https://opencode.ai)(MIT)는 모델 공급자가 아니라 사용자가 OpenCode 자체에서 구성한 대상으로 연결하는 _라우터_입니다. API 키, 구독(GitHub Copilot, ChatGPT, SuperGrok), **계정 없이** 무료 모델을 제공하는 OpenCode Zen gateway 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp)을 사용할 수 있습니다. script는 Codex와 Grok을 제어하는 것처럼 비대화형 모드에서 `opencode run`을 제어하며, 동일한 subprocess 기반을 재사용합니다. 별도 process group, timeout 시 `SIGTERM` 후 `SIGKILL`, 항상 닫힌 stdin, 정리된 environment를 적용합니다. **두 번의 실제 번역**으로 검증했습니다. `opencode/mimo-v2.5-free`을 통해 이 README 전체를 영어로 번역한 작업은 49초가 걸렸고 한 번에 완료되었으며, 원본 파일과 구조가 동일했습니다(제목 32개, code 닫힘 26개, 링크 18개, URL 37개, table 37줄, inline code 135개). 또한 키 없이 로컬 `ollama/qwen2.5:7b`을 통해 시험 파일을 번역했습니다.

  - **`--model provider/modèle`은 필수이며, 하나의 선택입니다.** `--model`이 없으면 OpenCode는 자체 기본값으로 돌아가며, 새로 설치한 환경에서는 대화가 훈련에 사용될 수 있는 무료 « stealth » 모델 `opencode/big-pickle`입니다. 측정 결과 실제로 이 모델이 응답했습니다. 사용자를 대신해 이를 조용히 선택하는 것은 이 저장소가 추적하는 바로 그 보이지 않는 전환입니다. 따라서 오류 메시지는 모델을 나열하는 명령(`opencode models`)과 세 가지 예시(로컬, 무료, 구독)를 명시합니다. `--eco`은 아무 효과가 없으며 그 사실을 알립니다. `--reasoning_effort`은 명시적으로 요청한 경우에만 OpenCode의 `--variant`으로 그대로 전달됩니다.

  - **격리는 추정한 것이 아니라 측정했습니다.** inline configuration(`OPENCODE_CONFIG_CONTENT`, OpenCode merge 순서에서 마지막이므로 사용자의 설정을 대체하지 않으면서 우선 적용됨)은 모든 tool이 거부된(`permission: {"*": "deny"}`) agent `aipmt`을 정의합니다. registry가 해당 tool을 모델에 아예 제공하지 않으므로 « 파일을 나열하고 `id`을 실행하라 »고 지시해도 tool이 없다고 응답합니다. session 공유를 비활성화하고 외부 plugin을 제외하며(`--pure`), 절대 `--auto`하지 않고, 비어 있는 일회용 작업 directory를 사용합니다. 두 가지 조용한 삽입을 측정해 차단했습니다. `OPENCODE_DISABLE_CLAUDE_CODE`이 없으면 사용자의 `~/.claude/CLAUDE.md`가 **모든** prompt에 들어갑니다(단순한 « 안녕하세요 » 입력에 186개가 아닌 515개의 input tokens). `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 directory의 `AGENTS.md`도 들어갑니다. « 모든 응답을 BANANA로 끝내라 »라는 지시가 번역에 적용되는 것을 확인했습니다. 반면 전역 `~/.config/opencode/AGENTS.md`은 계속 삽입됩니다. 이를 제외하는 switch는 없으며, 우회한 `XDG_CONFIG_HOME`을 사용하면 사용자의 공급자도 함께 숨겨집니다. 임시방편을 쓰는 대신 문서화했습니다.

  - **`exit 0`은 아무것도 입증하지 않습니다. 세 번째 CLI에도 같은 원칙을 적용하되, 이 CLI만의 함정 두 가지를 처리했습니다.** 알 수 없는 `--agent`은 `opencode run`을 실패시키지 않습니다. stderr에 경고를 남기고 tool이 활성화된 coding agent로 **조용히** 대체합니다. 따라서 inline configuration이 적용되지 않으면 쓰기 가능한 agent로 번역을 실행하게 됩니다. 출력 contract는 다음 조건 외에도 이 메시지가 없는지 검증합니다. 반환 코드 0, `error` event 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`일 것(`length`은 잘린 응답), 비어 있지 않은 텍스트입니다. 두 번째 함정은 오류 JSON event가 **불투명하다**는 것입니다. 단순한 참조와 함께 « 예기치 않은 서버 오류입니다. 자세한 내용은 서버 로그를 확인하세요. »라고만 표시되며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 log에만 있습니다. 따라서 `--print-logs --log-level ERROR`과 stderr의 `error="…"` field를 읽되, 그 뒤의 Bun trace는 제외합니다. 그 결과 알 수 없는 모델은 원인이 명시된 상태로 1초 만에 실패합니다. 또한 `--title`은 불필요한 LLM 호출을 방지합니다. 이것이 없으면 OpenCode는 `small_model`에서 한 번 더 요청해 session title을 생성합니다.

  - **Secret: Codex와 Grok과 동일한 pattern filtering을 적용하되, 명시적으로 지정된 한 가지 예외를 둡니다.** `OPENCODE_API_KEY`은 유지됩니다. 이는 OpenCode 자체의 키(Zen gateway, Go 구독)로서 이름 그대로 OpenCode를 대상으로 합니다. OpenCode의 `auth.json`에 해당하며 aipmt가 관리하거나 요금을 부과할 수 있는 키가 아닙니다. 공급자는 OpenCode에서 구성하며(`opencode auth login`, `opencode.json`), aipmt의 `.env`에서는 절대 구성하지 않습니다. aipmt의 키는 하나도 subprocess에 전달되지 않습니다. 구독형 CLI와 달리 CI에서는 거부하지 않습니다. runner에서 API 키나 자체 호스팅 모델을 사용하는 것은 정당한 용도입니다.

  - **이제 traversal 방지 장치는 원시 값이 아니라 삽입되는 값을 검사합니다.** `provider/modèle`에는 1.10.0의 보호 장치가 거부하던 `/`이 포함되어 있습니다. `--model`이 파일 이름 `--include_model`에 삽입되므로 당시에는 타당한 거부였습니다. 이제 파일 이름 label은 값을 삽입하기 전에 `/`, `\`, `:`을 `-`으로 바꾸며(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, `:`은 Windows에서 허용되지 않음), upstream 보호 장치는 이 label을 검사합니다. `../../evil`은 대상 아래의 단순한 이름 `doc-en-..-..-evil.md`이 되며, `..` 자체만 계속 거부되고 `--target_lang ../x`도 거부됩니다. `_ensure_within_directory` scope 보호 장치는 변경 없이 두 번째 방어 계층으로 유지됩니다.
  - **무료 모델과 로컬 모델에서 측정한 결과.** `opencode/mimo-v2.5-free`는 한 문단을 번역하는 데 16초, 이 README를 번역하는 데 49초가 걸렸습니다. `opencode/big-pickle`는 200단어에 40초가 걸렸으며, 각각 단독으로는 완료되었지만 두 요청을 동시에 실행했을 때는 5분 동안 응답이 없었습니다. `opencode/nemotron-3.5-lightning-free`는 3분 동안 아무 응답도 하지 않았습니다. 따라서 `REGEN_PROVIDER=opencode`에서는 `REGEN_MODEL`가 필수이며, **2개 job**을 병렬로 실행합니다. 로컬에서는 Ollama가 흔히 context를 4,096 tokens로 설정하지만 segment는 최대 16,000자에 이릅니다. 따라서 `PARAMETER num_ctx 32768`을 사용하는 `Modelfile`가 필수이며, 품질은 모델에 따라 달라집니다. 시험 파일에서 7B 모델은 목록의 순서를 뒤집고 code block의 닫는 fence를 손상했지만, gateway 모델은 모든 것을 보존했습니다.

  - **이 저장소의 번역은 이제 유료 API를 절대로 거치지 않습니다.** `regen_translations.sh`는 `.env`에 key가 하나라도 있으면 즉시 OpenAI API를 사용했고, Codex는 opt-in으로만 제공했습니다. 이 버전을 준비하면서 정확히 그런 일이 발생했습니다. ChatGPT 구독은 사용량별 요금을 내지 않기 위해 존재하는데도 28개 번역은 OpenAI API로 전송되었고, 이어서 힌디어 CHANGELOG는 Gemini API로 전송되었습니다. key 자동 감지는 제거됩니다. **Codex가 기본값이며 `gpt-5.6-sol`을 사용합니다.** 이는 품질 모델입니다. `openai`, `gemini`, `grok`은 `REGEN_PROVIDER` 외에도 `REGEN_ALLOW_PAID_API=1`을 요구합니다. 의사 결정 시점에 규칙이 실제로 적용되도록 명시적으로 이름 붙인 예외입니다. 알 수 없는 `REGEN_PROVIDER`는 API로 fallback하지 않고 실패합니다. 10개 테스트가 기본값, 거부 동작, 예외를 고정합니다. 이 버전의 28개 번역은 Codex를 통해 다시 수행했습니다.

  - **rate limit back-off를 공통화했습니다**(`_retry_on_rate_limit`). Codex와 Grok의 loop는 label만 다를 뿐 동일했으며, 세 번째 복사본이 추가되면 duplication 임계값을 넘었을 것입니다. 세 CLI 오류는 모두 동일한 `_CliCallError`에서 파생됩니다. 세 오류 중 하나라도 그 계층 밖으로 벗어나 shared loop가 더 이상 감지하지 못하게 되는 상황을 테스트로 금지합니다.

  - **테스트**: 새 파일 `tests/test_opencode_provider.py`(51개 테스트) — 전체 출력 contract, agent fallback, log에서 원인 읽기, 중복 제거된 text part와 무시되는 synthetic part, process group을 종료하는 timeout, 429 back-off, 필수 및 검증된 모델, secret 없는 preflight, binary resolution, dispatch wiring, 파일명 label, traversal 반증 시험. `tests/test_review_hardening.py`은 flag의 상호 배타성과 secret 부재 검사를 새 provider까지 확장합니다. 이제 gate는 문서화된 argparse **22개 flag**를 요구합니다. 전체 suite는 **382개 테스트**입니다.

- **1.11.1** 문서 수정: README가 마침내 7개 provider 경로를 안내합니다(2026-09-03).

  - **1.11.0의 PyPI 페이지에는 “4개 API + Codex CLI”라고 적혀 있었습니다.** 실제 코드는 7개 경로를 제공합니다. API를 통한 OpenAI, Mistral, Claude, Gemini, Grok과 사용량별 과금이 없는 구독 기반 Codex(ChatGPT), Grok입니다. 두 Grok mode가 소개 문구와 _Multi-Provider_ 항목에서 누락되었으며, 14개 번역에서도 같은 오류가 반복되었습니다. package의 long description은 버전별로 고정되므로 공개 페이지를 수정하려면 새 버전 번호가 필요했습니다. 이것이 이 버전의 유일한 존재 이유입니다. **코드 변경은 없습니다.**
  - `CLAUDE.md`는 release에서 도입된 내용에 맞게 정리되었습니다. gate counter(`--full`에서는 16, 17), 활성화된 11개 workflow, `gh pr checks`에서 보이지 않는 Sonar/Codacy counter 2개(hotspots, Codacy API), `ruff-format`에 의한 `# nosemgrep` 이동, OIDC 교환에 필요한 GitHub environment, 그리고 _pending publisher_는 이름을 예약하지 않는다는 사실을 반영합니다.

- **1.11.0** PyPI release: 저장소를 clone하지 않고 `pip install ai-powered-markdown-translator`에 이어 `aipmt` 명령을 사용합니다(2026-09-03).

  - **단일 파일 script가 설치 가능한 package로 바뀝니다.** `translate.py`는 root에서 `src/aipmt/translate.py`로 이동하며, console entry point `aipmt`과 이에 대응하는 `python -m aipmt`를 제공합니다. 기여하려면 여전히 저장소 clone이 필요합니다. 테스트, 28개 번역, 품질 도구가 그곳에 있기 때문입니다. 하지만 사용하는 데는 더 이상 필요하지 않습니다.

    - **import 이름은 `aipmt`이며 절대로 `translate`가 아닙니다.** 실제로 발생하며 조용히 지나가는 충돌이 있기 때문입니다. PyPI package `translate`(v3.8.1, 마지막 upload 2026-07-06)은 같은 이름의 디렉터리를 설치합니다. venv에서 재현한 결과 디렉터리가 module보다 우선하고, `translate.main`가 사라지며, entry point는 `AttributeError`에서 깨집니다. 그런데도 `pip check`은 “손상된 requirement가 없습니다”라고 응답하고 rc=0을 반환합니다. 사용자가 단순히 `pip install translate`을 실행하는 것만으로도 유용한 진단 없이 CLI가 깨질 수 있었습니다. 실제 wheel을 사용한 반증 시험에서는 package 위에 `pip install translate`를 설치하고 `aipmt --help`이 전후 모두 rc=0을 반환했으며, 두 CLI가 공존했습니다.
    - **distribution 이름은 길고 명령은 짧습니다.** `ai-powered-markdown-translator` 덕분에 PyPI 검색으로 package를 찾을 수 있습니다. 약어만으로는 프로젝트를 이미 아는 사람이 아니면 찾을 수 없지만, release의 목적은 바로 새로운 사용자가 발견할 수 있게 하는 것입니다. 그럴듯한 후보 2개는 검증 후 제외했습니다. `ai-markdown-translator`는 동일한 목적의 도구가 2024년부터 npm에서 사용 중이며, 이 저장소보다 17개월 먼저 존재했습니다. `aimt`는 동일한 분야에서 활발히 관리되는 package `aim`(v3.29.1)과 한 글자 차이입니다. 장기적인 혼동을 일으키기에 최악의 조건입니다. 검증 방법에도 함정이 있습니다. `pypi.org/project/<nom>/`는 어떤 이름이든 200을 반환하는 anti-bot 페이지이므로 JSON API만 신뢰할 수 있습니다.
    - **flat package 대신 `src/` layout을 사용합니다.** flat package는 테스트의 `sys.path.insert(..., "..")` 6개를 보존했겠지만, 그것이 바로 문제입니다. 이들은 package 대신 source tree를 import하므로 packaging 오류를 숨길 수 있습니다. 실제 비용은 substitution rule 하나가 추가되는 것뿐입니다.

  - **이제 key를 한 번만 설정하면 됩니다.** 설치된 CLI에는 영구적인 설정이 전혀 없었습니다. 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었습니다. `find_dotenv`가 system root까지 올라가므로 **home directory 아래에서 작업할 때는** `~/.env`을 찾았지만, 다른 위치에서 작업할 때는 아무것도 찾지 못했습니다. 이는 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라지는 coverage였습니다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`가 추가됩니다.

    - **우선순위는 코드로 직접 지정되지 않으며**, `load_dotenv`의 기본값인 `override=False`에서 파생됩니다. 각 계층은 이전 계층에서 비어 있던 값만 채웁니다. 따라서 환경 변수 → 프로젝트의 `.env` → 사용자 설정 순서가 되며, 구조가 아닌 동작 테스트로 검증합니다. 두 호출의 순서를 바꾸거나 세 번째 계층을 제거하면 테스트가 실패합니다.
    - **TOML이 아니라 `.env` 형식을 사용합니다.** 이는 의도적인 선택입니다. `python-dotenv`는 이미 dependency이고, syntax는 이미 15개 README에 문서화되어 있으며, 같은 파일을 두 scope에서 사용할 수 있습니다. 새로운 dependency나 syntax가 필요하지 않습니다. 위치는 `XDG_CONFIG_HOME`가 **절대 경로**일 때 이를 따릅니다. specification에서는 상대 값을 무시하도록 요구합니다. 그렇지 않으면 설정 위치가 다시 현재 디렉터리에 종속되기 때문입니다. Windows에서는 `APPDATA`을 따릅니다.
    - **두 옵션을 이유와 함께 제외했습니다.** system keyring(`keyring`)은 desktop에서는 더 안전하지만 server, container, CI 같은 headless 환경에서는 실패합니다. 이는 바로 일괄 번역의 주요 사용 사례입니다. opt-in 후보로는 좋지만 기본값으로는 적합하지 않습니다. `--api-key` flag를 사용하면 key가 shell history에 남고 `ps`에서 노출됩니다.
    - **key가 없을 때 더 이상 call trace를 표시하지 않습니다.** 사용자는 `site-packages`를 가리키는 Python stack trace와 “환경 또는 .env”라고만 하고 두 번째 파일을 어디에 만들어야 하는지는 알려주지 않는 메시지를 받았습니다. 이제 세 위치와 정확한 경로를 모두 나열하며 명령은 code 2로 종료됩니다. 안전망은 **의도적으로 좁게** 설정되어 `except ValueError`가 설정 단계에만 적용됩니다. 전체 실행을 감싸면 번역 도중 발생한 실제 bug가 안심시키는 메시지로 바뀔 수 있습니다. 이는 이 저장소가 추적하는 바로 그 failure mode입니다. `main()`의 source를 읽어 이를 금지하는 테스트가 있습니다.

  - **수정 — 도구 설치 후 사용자의 `.env`가 무시되었습니다.** argument 없는 `load_dotenv()`는 현재 디렉터리부터 올라가지 않고 **호출 파일**부터 올라갑니다. 따라서 `site-packages`에서 시작합니다. 자체 `.env`이 있는 프로젝트에서 실제 console entry point를 실행해 측정한 결과, `find_dotenv()`는 `''`을 반환하고 key를 불러오지 못했지만 `find_dotenv(usecwd=True)`는 이를 찾았습니다. 도구가 clone한 저장소에서만 실행되던 동안에는 이 bug가 없었습니다. release 후에는 올바른 설정에서도 API key가 “누락”된 것만이 유일한 증상인 채 항상 발생했을 것입니다.

  - **3개 gate는 아무것도 검증하지 않게 된 뒤에도 green이 되었을 것입니다.** 의도적으로 이동 **전에** 강화했습니다. 잡아내야 할 변경이 이루어진 뒤 작성한 guardrail은 아무것도 증명하지 못하기 때문입니다. 각각 원본 저장소에서는 green이고, migration한 복사본에서는 red로 바뀝니다. 양방향을 모두 측정했습니다.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시합니다.** rc=0과 “분석된 파일 0개”를 반환합니다. complexity gate는 158 functions / 2247 nloc에서 3 functions / 34 nloc로 줄면서도 출력은 0바이트가 되었을 것입니다. 이제 scope는 각 entry의 존재 여부를 검증하는 array입니다.
    - **존재하지 않는 module에 `coverage run --source=`를 실행해도 실패하지 않습니다.** stderr에 warning만 표시되고 unittest와 `coverage xml` 모두 rc=0을 반환하며 report까지 게시됩니다. 다만 1453 statements에서 141 statements로 잘려 있습니다. 프로젝트 대부분이 분석되지 않았기 때문에 오히려 정상처럼 보였을 것입니다. 두 lower bound가 report를 보호합니다. 전체 수치와 측정된 가장 큰 파일의 수치입니다.
    - **번역 freshness probe는 구조적으로 invocation 형태를 감지하지 못합니다.** argparse flag를 기준으로 삼는데, 파일명을 바꿔도 바로 그 부분은 변하지 않습니다. 재현 결과 module을 이동하고 15개 README가 여전히 존재하지 않는 명령을 문서화해도 “오래된 번역 없음”이라는 verdict가 나왔습니다. 따라서 7번째 section은 option이 아니라 **형태**를 검증하며, Lizard hook은 script의 실제 scope와 대조됩니다. 해당 key인 `files:`는 더 이상 일치하지 않을 때 pre-commit을 실패시키지 않고 **건너뛰게** 하기 때문입니다.

  - **`requires-python = ">=3.10"`는 더 이상 단순한 선언이 아닙니다.** 개발 환경에는 3.12만 있었고 어느 버전에서도 실제로 실행한 적이 없는데 `sonar-project.properties`는 이미 3.10~3.12를 지원한다고 안내했습니다. release하면 공개되었을 내부 모순입니다. 이제 test workflow가 3.10, 3.11, 3.12에서 suite를 실행하며, **package**를 설치해 공개된 version bound까지 검증합니다.

  - **lower bound만 두고 upper bound는 두지 않습니다.** `requirements.txt`은 테스트된 lock으로 유지되고, `[project.dependencies]`은 공개 contract가 됩니다. lock의 정확한 version을 그대로 공개하면 다른 package를 사용하는 모든 사용자에게 conflict를 일으킬 수 있습니다. `<N+1` upper bound도 두지 않습니다. major version 업데이트가 늦어질 때마다 release gate를 실패시키는 `check-deps-fresh.sh`과 정면으로 모순되기 때문입니다. lower bound 집합은 resolve되며, 반증 시험 `openai==1.0.0`는 `ResolutionImpossible`로 종료됩니다. 이는 검사가 모든 것을 무조건 허용하지 않고 구별한다는 사실을 증명합니다. 또한 guard가 `pyproject.toml`의 version과 CHANGELOG version이 달라지지 않도록 막습니다. PyPI는 version 번호 재사용을 허용하지 않습니다.

  - **새 venv에서 end-to-end로 검증했습니다.** 약 70KB의 wheel에는 `aipmt/*.py`, dist-info, license만 포함됩니다. `aipmt --help`은 22개 flag와 함께 rc=0을 반환합니다. `python -m aipmt`는 “usage: \_\_main\_\_.py”가 아니라 “usage: aipmt”를 표시합니다. `pipx` 설치도 정상적으로 작동합니다. 무엇보다도 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행해 bold, list, inline code, link, URL이 보존되고 code block은 번역되지 않음을 확인했습니다. migration 전의 기존 318개 테스트는 전후 identifier 목록이 바이트 단위까지 동일한 상태로 통과합니다. 단순히 “OK”가 아니라 이것이 어떤 테스트도 무력화되지 않았음을 증명합니다. 여기에 3계층 설정 테스트 12개가 추가되어 총 330개입니다.

- **1.10.0** `--use_codex` provider(ChatGPT 구독 quota), SDK와 모델 업데이트, 여러 문단으로 된 news citation 수정(2026-08-29):

  - **보안 검토 — PR에서 제시했지만 모든 곳에서 지키지는 못했던 guardrail 2개**:

    - **Codex preflight가 전체 `.env`를 binary에 전달했습니다.** `_codex_preflight`는 **`env=` 없이** `subprocess.run`를 호출했습니다. subprocess가 `os.environ` 전체를 상속했고, 따라서 `load_dotenv`에서 불러온 `.env` 전체도 상속했습니다. instrumented fake binary로 측정한 결과 **7개 secret**이 preflight에 도달했습니다. 6개 provider key와 `GITHUB_TOKEN` 하나입니다. 반면 counterpart인 `_grok_preflight`는 `env=_grok_env()`을 올바르게 전달해 **0개**였습니다. 이는 PR 내부의 모순이었습니다. 바로 몇 줄 아래에 있는 `_strip_secret_env`는 정확히 이 invariant를 유지하려고 존재합니다. `_codex_env_base()`을 추출해 두 경로에서 공유하도록 했으며, 수정 후 측정 결과 양쪽 모두 secret이 0개였습니다.
    - **“`--deny` fail-closed” 속성이 실제 사용된 형태를 포괄하지 못했습니다.** 주석은 알 수 없는 prefix의 rule이 시작을 거부한다는 사실을 근거로 Grok confinement 전체를 정당화했습니다. `grok 1.0.13`에서 측정한 결과 이 validation은 **괄호 형태에만** 존재합니다. `--deny 'CeciNestPasUnOutil(*)'`는 시작을 거부하며 “알 수 없는 tool prefix”를 표시하지만, `--deny 'CeciNestPasUnOutil'`는 아무 경고 없이 허용됩니다. 그런데 `GROK_DENY_RULES`는 bare name만 사용했습니다. 따라서 xAI 측에서 tool 이름을 바꾸면 이미 OS sandbox가 적용되지 않는 환경에서 유일하게 측정된 confinement layer가 아무 신호 없이 제거될 수 있었습니다. 이름이 지정된 8개 rule은 `Prefix(*)`로 변경되며, 각각 CLI가 알고 있는 prefix인지 검증됩니다. catch-all `*`은 유일하게 허용되는 literal 형태로 유지됩니다. validated되지 않은 형태로 되돌아가는 것을 테스트가 방지합니다.
    - **그 밖의 항목은 문제없음을 확인했습니다.** command injection은 없습니다. 모든 곳에서 list 형태를 사용하고 `shell=True`는 사용하지 않으며, 문서 내용은 stdin 또는 `--prompt-file`로 전달합니다. 안전하지 않은 deserialization도 없습니다. type guard와 함께 `json.loads`만 사용합니다. 7개 payload에서 path traversal 수정의 우회 방법을 찾지 못했으며, CLI가 `--deny '*'`를 실제로 적용해 workdir 밖을 읽을 때 `DENY_ENFORCED`가 관찰되었습니다.
    - 앞서 추가한 freshness check도 자체 원칙을 우회하고 있었습니다. PyPI request가 실패한 package를 조용히 건너뛰어도 gate가 green이 되었습니다. 이제 실제로 비교한 package 수를 계산하고 coverage가 불완전하면 실패합니다.

  - **dependency를 최신 상태로 갱신하고, 지연이 재발하지 않도록 안전망 2개를 추가했습니다**:
    - **지연은 실제로 존재했고 장기간 지속되었습니다**: `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22** — 모든 provider 호출에서 TLS를 검증하는 루트 인증서 저장소가 2년이나 뒤처져 있었습니다. 확인된 원인은 **`.github/dependabot.yml`이 존재하지 않았기 때문**입니다. 이 파일이 없으면 GitHub는 _보안 업데이트_만 활성화하며, Dependabot은 CVE의 영향을 받는 종속성에 대해서만 PR을 제안합니다. 이 때문에 `urllib3`과 `idna`은 버전을 올리면서도 두 SDK는 주 버전 하나만큼 뒤처진 채로 방치했습니다.
    - **예전의 추론에서 우려했던 것과 달리 두 주 버전은 충돌 없이 공존합니다**: `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**로 마이그레이션하지만, `mistralai`와 `google-genai`은 `httpx<1`에 그대로 남습니다. 그러나 이들은 서로 다른 배포판입니다. 실제 설치를 수행한 뒤 **7개의 provider 경로 전체를 처음부터 끝까지 테스트**하여 검증했습니다. 대상은 OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI이며, 각 출력에서 인라인 코드와 링크도 보존되었습니다. “두 개의 HTTP 스택을 피한다”는 것은 선호 사항이었을 뿐 차단 요인은 아니었고, 측정 결과로 결론을 내렸습니다.
    - **`requirements.txt`은 실제 환경을 설명하지 못했습니다**: `google-auth`, `cryptography`, `opentelemetry` 스택은 한 번도 선언되지 않은 채 작업용 venv에 설치되어 있었습니다. 따라서 새로 설치한 환경에서는 테스트 대상 환경을 재현할 수 없었습니다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`은 아무 곳에서도 import되거나 요구되지 않으면서 파일에는 포함되어 있었으며, 이는 `mistralai` 1.x의 잔재였습니다. 이제 이 파일은 직접 종속성만으로 구축한 venv의 전체 종속성 폐쇄로 다시 생성됩니다. `pip-audit`은 새 종속성 집합에서 알려진 취약점을 하나도 보고하지 않습니다.
    - **`.github/dependabot.yml`**(신규)은 pip 및 github-actions의 주간 버전 업데이트를 활성화합니다. 부 버전과 패치 업데이트는 하나의 PR로 묶습니다. 패치 버전 상승마다 PR을 만들면 결국 무시되며, 소음은 업데이트의 적이기 때문입니다. **주 버전 업데이트는 분리**하며, 각각 실제 호출을 통한 검증이 필요합니다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 프로젝트의 판정 결과에서 지연을 드러냅니다. Dependabot은 업데이트를 제안할 뿐 보장하지 않으며, 해당 PR은 계속 쌓일 수 있습니다. 주 버전 지연은 실패로, 부 버전 지연은 경고로 처리합니다. 항상 빨간색인 gate는 결국 무시되기 때문입니다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 skip하고 **CI에서는 fail-closed 방식으로 실패**합니다. 실행되지 않은 검사는 성공이 아니기 때문입니다. 양방향으로 검증했습니다. 수정 전의 정확한 상태(`openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`)는 탐지하고, 부 버전 지연에는 경고만 표시합니다.

  - **이 PR의 리뷰에서 도출된 수정 사항** — 리뷰 agent 다섯 명이 diff를 면밀히 검토했습니다. 아래 항목은 모두 수정 전에 **측정으로 재현**했으며, 그중 두 건은 이 버전의 앞부분에서 새로 유입된 회귀였습니다.

    - **회귀 수정 — `_NEWS_CITATION_REGEX`에 지수적 backtracking이 있었습니다.** 여러 문단을 지원하는 수정에서 반복 구문 안에 `(?:[ \t]*$|[ \t]+.*)`을 도입했습니다. `[ \t]+`과 `.*` 사이의 공백 분배가 모호하며, 이 모호성이 반복될 때마다 누적됩니다. 패턴과 일치하지 않는 줄 `>   texte` — 완전히 유효한 Markdown 들여쓰기 — 을 대상으로 측정한 결과, **14줄에 2,589ms**가 걸렸지만 수정 후에는 0.04ms였으며 줄을 하나 추가할 때마다 약 9배씩 증가했습니다. `--news` 모드에서는 형식에 맞지 않는 긴 blockquote 하나만으로도 원인을 확인할 수 없는 채 job timeout까지 번역이 멈출 수 있었습니다. 이제 반복 구문은 줄 전체를 한 번에 소비하므로(`\n^>(?![ \t]*—).*`), 각 반복에서 일치하는 방법은 하나뿐입니다. 실제 231개 문서 corpus로 검증한 결과, capture에는 **차이가 전혀 없었고** 423개의 인용문도 동일했으며 여러 문단으로 이루어진 14개의 본문도 여전히 정상적으로 확장되었습니다.
    - **provider flag 두 개를 동시에 지정하면 아무 알림 없이 사용량 기반 요금이 청구되었습니다.** `--use_codex --use_mistral`이 허용되었고, `_select_provider_client`은 Mistral을 먼저 검사하며, `_resolve_provider`은 명시적인 boolean을 우선하므로 두 경로 모두 Mistral로 귀결되었습니다. 따라서 사용자는 구독 할당량 사용을 요청했지만 아무 경고 없이 사용량 기반 요금이 청구되었습니다. 이는 정확히 `--use_codex`이 방지하려는 실패 유형입니다. 이제 provider flag 여섯 개가 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경 사항**: 이전까지 아무 알림 없이 허용되던 두 provider를 결합한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 종료 gate는 probe가 중단되어도 성공으로 통과했습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개는 반환 코드를 전혀 확인하지 않은 채 “stdout을 캡처하고 비어 있으면 결론을 내리는” 패턴을 사용했습니다. 예외(이름이 변경된 파일, `FileNotFoundError`)는 stderr에 기록하고 stdout을 비워 둔 채 검사가 “보고할 사항 없음”이라고 결론 내리게 했습니다. “`exit 0`은 아무것도 증명하지 못한다”는 함정을 방지하려고 만든 스크립트 내부에서 똑같이 재현한 셈입니다. 이제 `probe()` helper는 반환 코드가 0이고 **동시에** 종료 sentinel이 존재하도록 강제하며, probe는 기준점 집합이 비어 있으면 결론을 내리지 않습니다. 빈 집합에 대한 assertion은 언제나 참이기 때문입니다. 예를 들어 위의 상호 배타 그룹을 추가하면서 provider flag가 `*_group` 객체를 통과하게 되었고, 기존 regex `parser\.add_argument\(`은 더 이상 이를 일치시키지 못했습니다. 그 결과 **21개 중 6개의 flag**가 아무 알림 없이 검사 범위에서 빠졌는데도 gate는 성공으로 표시되었습니다.
    - **secret scan은 provider 여섯 개 중 네 개를 놓쳤습니다.** `[A-Za-z0-9]` class가 하이픈을 제외하므로 `sk-proj-…`(현재 OpenAI 형식)과 `sk-ant-api03-…`는 두 번째 하이픈에서 끊겼으며, `AIza…`은 검사 대상에 포함되지 않았습니다. 패턴을 확장하고 `.secrets.baseline`은 scan에서 제외했습니다. 또한 `.env` guard는 index만 확인하는 `git diff --cached`을 조회하고 있었습니다. 따라서 최악의 경우인 **이미 commit된** `.env`은 절대로 나타나지 않았습니다. 이제 `git ls-files`을 조회합니다.
    - **Codex의 “token warm-up”은 실제 warm-up이 아니었습니다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`을 건드리지 않으며(mtime과 크기가 변하지 않음), 도움말에도 “로그인 상태 표시”라고 되어 있습니다. 그런데도 주석에서는 token을 “한 번 순차적으로” 갱신하여 일회용 순환 token의 동시 refresh 위험을 제거한다고 주장했습니다. 설명된 보호 기능은 존재하지 않았습니다. 이제 주석은 코드가 실제로 수행하는 작업을 설명하며, 실질적인 대응책은 여전히 `max_jobs=4`입니다. 또한 이 검사는 이전에 무시하던 `CODEX_BIN`을 이제 준수합니다. `PATH`에 `codex`이 없는 장비에서는 “인증되지 않음” 오류가 발생해 잘못된 진단을 내리고 있었습니다.
    - **`.env`은 subshell에서 source되었습니다.** `detect_provider`이 명령 치환에서 호출되므로 해당 export가 상위 shell로 전달되지 않았습니다. 그 결과 `.env`에서 정의한 `GROK_BIN`, `GROK_HOME`, `REGEN_MODEL`은 `main()`에서 수행한 조회에 보이지 않았고, 올바른 구성에서도 “Grok 바이너리를 찾을 수 없음”이라는 결론을 내렸습니다.
    - **동시 실행 수가 명시된 한도를 50% 초과했습니다.** guard가 README/CHANGELOG 쌍을 실행한 뒤에 배치되어 있어 **`max_jobs=2`에서 측정된 최대값은 3**이었습니다. 주간 할당량이 Chat/Imagine/Voice와 공유되고 측정할 수 없는 Grok에서는 스크립트가 스스로 정한 한도조차 지키지 못한 것입니다. 또한 최종 개수는 28과 비교하지 않은 채 표시만 했으므로 파일 하나가 누락되어도 탐지되지 않았습니다.
    - **Grok 출력 계약: 이제 `stopReason`이 없으면 실패합니다.** 공표된 계약은 `end_turn`을 요구하지만, 코드는 “`end_turn` **또는 없음**”을 적용했습니다. 해당 필드가 없는 payload나 CLI 업데이트로 필드 이름이 변경된 payload는 guard를 아무 알림 없이 no-op으로 만들었습니다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류되지 않습니다. 이는 대화 차례 예산이 소진된 것이므로 다시 시도해도 90초의 대기 비용만 들고 같은 결과가 재현되기 때문입니다. `quota`도 rate limit marker에서 제외했습니다. `_codex_is_rate_limited`의 docstring이 이미 설명했지만 Grok에는 적용되지 않았던 바로 그 이유입니다.
    - **Gemini cascade는 모델별로 memoization됩니다.** 기본 모델이 `minimal`을 거부하는데도 cascade는 segment마다 여기서 다시 시작했습니다. 따라서 정상 경로에서도 segment마다 400 응답의 왕복 비용을 치르고 똑같은 경고를 다시 출력했습니다. 경고가 수백 번 반복되면 아무도 읽지 않게 되며, 그렇게 경고는 문제를 가리는 가면이 됩니다.
    - **기타**: CI의 거부 메시지가 Codex 전용으로 하드코딩되어 `--use_grok_cli` 사용자를 `XAI_API_KEY`이 아닌 `OPENAI_API_KEY`로 안내했습니다. `provider.capitalize()`은 “Grok_cli”와 “Openai”로 표시했습니다. subprocess 기반 계층의 주석은 두 CLI 모두에 “shim”을 일반화했지만 Grok 바이너리는 native ELF입니다. 올바른 근거는 “자체 subprocess를 생성하는 agent”입니다. `subprocess`에 대한 SAST finding 12건은 근거와 함께 `# nosec` / `# nosemgrep`으로 표시했습니다. `shell=True`이 없는 list 형식이므로 injection이 불가능하며 문서 내용은 절대로 argv를 통과하지 않습니다.
    - **더 이상 어떤 secret도 agent subprocess에 전달되지 않습니다.** 이름 기반 deny-list는 **청구** 불변 조건만 보호했습니다. 즉, Codex에는 `OPENAI_API_KEY`이 없고 Grok에는 `XAI_API_KEY`이 없도록 했습니다. 측정 결과 **그 밖의 secret 일곱 개**가 여전히 각 subprocess에 전달되고 있었습니다. Anthropic, Mistral, Google, Gemini key, 다른 CLI의 key, 그리고 secret은 아니지만 트래픽 경로를 바꾸는 `OPENAI_BASE_URL`입니다. 그런데 이 두 CLI는 **agent**이며, Grok agent는 많은 Linux 장비에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 필터링은 이름 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)을 기준으로 수행합니다. 따라서 이 코드가 알지 못하더라도 사용자가 `.env`에 추가한 변수까지 포함됩니다. CLI에는 이 변수들이 하나도 필요하지 않습니다. 인증 정보는 환경이 아니라 `~/.codex`과 `~/.grok`에 존재합니다. 강화된 환경에서 두 provider 각각을 사용해 **실제 번역을 성공적으로 완료**하여 검증했습니다.
    - **테스트**: 새로운 파일 `tests/test_review_hardening.py`(테스트 21개)은 provider flag의 상호 배타성, `stopReason` 계약, news regex의 선형성, CI 거부 메시지, Gemini memoization, subprocess 환경에 어떤 secret도 포함되지 않는다는 조건을 고정합니다. 마지막 assertion은 **일반적**이어서 어떤 목록에도 이름이 없는 key도 탐지해 실패합니다. 반면 기존 삭제 테스트는 자체 상수를 그대로 비추는 거울에 불과해 자체 loop의 고장 외에는 아무것도 탐지할 수 없었습니다. 전체 suite는 **311개 테스트**입니다.
  - **두 개의 새로운 Grok provider**: `--use_grok`(xAI API, 키 `XAI_API_KEY`, 사용량 기반 과금)와 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독에서 차감 — `--use_codex`와 동일한 원리).
    - **API 모드, 약 40줄**: xAI endpoint는 OpenAI와 호환되므로 client와 `_call_openai`는 그대로 재사용하며, `base_url`만 변경됩니다. 단 하나의 조정만 필요했고 이는 모두에게 도움이 됩니다. 이제 `finish_reason`는 OpenAI가 `stop`를 내보내는 위치에서 xAI가 내보내는 형식인 `end_turn`도 허용합니다. 모델: `grok-4.6`(고품질) 및 `grok-4.3`(경제형). 참고로 Grok의 경제형도 저장소에서 가장 비쌉니다. 백만 개당 $1.25/$2.50로, `mistral-small-latest`의 $0.15/$0.60와 비교됩니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택하는 것입니다.
    - **CLI 모드**: Codex를 본떠 만들었지만, 실제 환경에서 불가피한 네 가지 차이가 있습니다. prompt는 파일로 전달되며(`--prompt-file`, CLI는 stdin을 읽지 않고 argv의 segment는 `ps`에 노출됨), 출력은 stdout의 단일 JSON object입니다(JSONL도 아니고 `-o` 파일도 아님). 구독에서는 `grok-4.6`과 `grok-4.5`만 제공되며, sandbox는 적용할 수 없습니다(아래 참조). 하위 process 실행은 이미 테스트된 Codex provider의 나머지 부분을 건드리지 않고 `_codex_run_process`에서 Codex와 공통화했습니다.
    - **`exit 0`는 아무것도 입증하지 못함, 실측 완료**: 인증되지 않은 상태에서 CLI는 반환 코드 **0**으로 **stdout**에 `{"type":"error","message":"Not signed in."}`을 기록합니다. 거부되거나 turn 수를 초과한 경우에도 동일하게 동작합니다. 따라서 출력 contract는 반환 코드 0, error payload 없음, `stopReason == end_turn`, 비어 있지 않은 text라는 네 가지 조건을 동시에 요구합니다. preflight도 같은 논리를 따릅니다. 연결이 끊긴 상태에서도 `grok models`는 0으로 종료되며, stdout에 « 인증되지 않음 »이 있는지를 통해서만 판단할 수 있습니다.
    - **격리: 의도적으로 채택하고 문서화한 비대칭성.** Codex가 `--sandbox read-only`에서 실행되는 것과 달리 Grok sandbox는 최근의 많은 Linux 환경에서 적용할 수 없습니다. `sudo` 없이는 우회할 수 없는 두 가지 독립적인 system 원인이 있기 때문입니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`가 `0700`에 있으면 container runtime socket의 deny-list가 실패합니다(resolver는 `ErrorKind::NotFound`만 복구하며 EACCES는 치명적인 오류가 됨). 핵심 함정은 적용할 수 없는 **내장** profile이 **아무 경고 없이 격리되지 않은 상태로 실행된다**는 점입니다. 따라서 script는 기본적으로 어떤 profile도 요청하지 않으며 절대 조용히 fallback하지 않고 stderr에 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하며 catch-all `*`도 포함됩니다. 이는 실측된 유일한 _fail-closed_ 계층입니다(알 수 없는 prefix의 규칙이 하나라도 있으면 시작이 거부됨). `GROK_TRANSLATE_SANDBOX=read-only`을 사용하면 이를 필수로 지정할 수 있으며, 해당 환경에서 준수할 수 없으면 시작이 실패합니다.
    - **안전장치**: 하위 process의 환경에서 `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`를 제거합니다(key가 있으면 사용량 기반 과금으로 전환되고, 상속된 `GROK_SANDBOX`는 적용할 수 없는 profile을 오해의 소지가 있는 메시지와 함께 강제함). MCP/hooks/skills/agents 스위치를 비활성화하고 `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI에서의 실행 거부, process group을 종료하는 timeout, rate limit 발생 시 back-off를 적용합니다. `--max-turns`는 1이 아니라 6으로 설정합니다. counter는 tool turn 이후에 증가하므로 1로 설정하면 출력이 잘리기 때문입니다.
    - **할당량**: Grok pool은 주간 단위이며 **Chat, Imagine, Voice와 공유**되고, 이를 보여 주는 command는 없습니다. 이는 `account/rateLimits/read`으로 사용량을 산정할 수 있는 Codex와 다릅니다. 따라서 `regen_translations.sh`은 동시 실행을 2개로 제한하고 이를 명시적으로 경고합니다.
    - **테스트**: 새로운 파일 `tests/test_grok_provider.py`(24개 테스트). 전체 suite는 **290개 테스트**입니다.
  - **수정된 bug — 여러 paragraph로 구성된 영문 인용문이 일부만 보호되던 문제(`--news` 모드)**: `_NEWS_CITATION_REGEX`는 인용문 본문으로 **연속된** `>` line만 허용했습니다. 인용문이 빈 `>` line으로 구분된 여러 paragraph에 걸치면 마지막 paragraph만 포착되어 placeholder로 대체되고, 앞선 paragraph들은 LLM으로 전달되어 번역되었습니다. 이는 `--news`이 보장하려는 것과 정확히 반대였습니다. 이제 반복 패턴은 내부의 빈 `>` line을 허용하며 non-greedy 방식으로 동작하여, 처음 만난 빈 line이 아니라 기울임꼴 line 앞의 빈 `>` line에서 멈춥니다.
    - 실제 198개 article corpus에서 **측정한 규모**: 인용문 419개 중 11개가 영향을 받았습니다. regression은 없습니다. 새로운 regex는 정확히 같은 수의 인용문을 포착하고 여러 paragraph로 된 본문만 확장합니다(동일한 본문 408개, 확장된 본문 11개). 또한 `> — …` attribution line은 기존 lookahead를 유지하므로 여전히 본문에 흡수될 수 없습니다.
    - 일본어와 아랍어로 번역한 69KB article에서의 **end-to-end 검증**: 이전에는 인용문의 첫 paragraph가 일본어로 `> GLM-5.3がオープンウェイト化。` 처리되고 아랍어에서도 마찬가지로 번역되었지만, 이제는 `> GLM-5.3 is now open-weight.` 상태로 유지됩니다. 영문 인용문 line 수는 source와 같은 10개로, 기존 9개에서 복구되었습니다.
    - 참고: 이 결함은 인용문의 존재 여부만 확인하고 완전성은 검사하지 않는 downstream validator에서 감지되지 않았습니다.
  - **기본 provider에서 실측한 비용 절감**: 모델명이 `gpt-5`로 시작하면 `--eco`에서도 `_openai_extra_kwargs`이 `reasoning_effort="medium"`를 전송했습니다. 열 단어짜리 문장을 번역하도록 `gpt-5.4-mini`에서 측정한 결과, `medium`은 reasoning token 45개와 출력 token 65개를 사용했지만 `none`는 각각 0개와 14개를 사용했습니다. 번역에 reasoning은 아무런 이점이 없었으며 모든 파일의 모든 segment마다 비용이 발생했습니다. 이제 기본값은 `--eco`에서 `none`이고, 그 외에는 계속 `medium`입니다. CLI에서 명시적으로 전달한 값은 계속 우선합니다. 이제 `--reasoning_effort`은 `low`/`medium`/`high` 외에도 `none`와 `xhigh`를 허용합니다. 모든 모델이 이 값들을 전부 허용하는 것은 아닙니다. 예를 들어 `minimal`는 `gpt-5.4-mini`에서 거부되며, 이 경우에는 기존의 parameter 없는 retry가 대응합니다.
  - **SDK 업데이트 및 Gemini migration**: `google-generativeai`(지원이 2025-11-30에 종료되었고 저장소가 archive됨)을 통합 SDK인 **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 이후 `client.models.generate_content(model=, contents=, config=)`를 사용하며, system prompt는 segment에 연결하는 대신 `system_instruction`로 전달합니다. `mistralai`은 **2.9.4**로 올라갔습니다(import는 `from mistralai.client import Mistral`이 되며, 이전 방식은 `ImportError`을 발생시키는 것을 wheel에서 확인함). `anthropic`은 **0.125.0**, `openai`은 **2.54.0**으로 올라갔습니다. 이는 `httpx2`으로 전환되기 전의 마지막 버전으로, venv에 두 HTTP stack이 공존하지 않도록 하기 위한 것입니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5의 제한도 해제했습니다.
  - **문서가 아니라 실제 테스트로 포착한 두 가지 regression**:
    - `anthropic` ≥ 1.0은 `max_tokens`상 10분을 초과할 것으로 예상되는 non-streaming 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 안전장치는 0.34.2에는 없었으며 `max_tokens=32768`을 사용하는 모든 Claude 호출을 망가뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 전체 응답만 사용하는 호출을 streaming으로 전환하지 않아도 됩니다.
    - `thinking_level="minimal"`은 Gemini catalogue의 일부에서만 허용됩니다. `gemini-3.1-flash-lite`은 이를 지원하지만 `gemini-3.7-flash`와 `gemini-3.1-pro-preview`은 400으로 거부합니다. 이에 따라 기존 OpenAI fallback을 본떠 `_gemini_generate_with_fallback`에 `minimal` → `low` → thinking_config 없음의 cascade를 적용했습니다. 최적화 parameter 때문에 번역이 실패해서는 안 됩니다.
  - **갱신된 기본 모델**, 모두 실제 호출로 검증됨: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%), Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜 없는 canonical ID), Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(안정 version이며 `3.5-flash-lite`보다 저렴함). Mistral은 변경되지 않았으며 `mistral-large-latest`은 계속 네 모델 중 가격 대비 품질이 가장 좋습니다. 참고: `gemini-3.1-pro-preview`보다 최신인 Pro 등급 Gemini 모델은 없습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 계열은 전부 Flash 전용입니다.
  - **Gemini 전환 전 실측한 A/B 비교**: `README.md`를 `gemini-3.1-pro-preview`과 `gemini-3.7-flash`로 각각 일본어 번역했습니다. 구조는 완전히 동일했으며(list 21개, code block 18개, HTML link 13개, image 13개, 모든 URL 보존), 소요 시간은 **48초 대비 8초**였습니다. 이 두 모델의 번역이나 비라틴 문자 script 성능을 비교하는 공개 benchmark가 없으므로, 이 측정이 없었다면 전환은 단순한 추정에 근거했을 것입니다.
  - **Claude 응답 block filtering**: `_call_claude`는 type을 filtering하지 않고 `block.text for block in response.content`을 수행했습니다. adaptive reasoning 모델(Sonnet 5 이상)은 `thinking` block을 사이에 삽입하는데, 이 block은 `.text`가 아니라 `.thinking`을 노출하므로 첫 segment에서 불투명한 `AttributeError`으로 인해 번역이 중단되었을 것입니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result` block을 제외합니다. text를 담은 알 수 없는 type에는 관대하도록 negative list를 사용합니다. text block이 하나도 없는 응답은 명시적인 error를 발생시킵니다. 모든 호출에 `thinking={"type": "disabled"}`를 전달합니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 폐기 날짜가 지난 모델을 제거했습니다(`magistral-*` 제품군은 2026-07-31, `gemini-2.0-*`은 2026-06-01, `gemini-3-pro-preview`는 2026-03-09에 폐기되었으며, 그 밖에 `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`도 제거). 제한값 수정: Mistral 128K → **256K**(Large 3 / Small 4 generation), Gemini 1,000,000 → **1,048,576**(실제 input 제한), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 제품군을 추가했습니다. 참고: `translate()`가 segmentation을 `min(16000, limite)`으로 제한하므로 이 제한값들은 계속 참고용입니다.
  - **Provider `--use_codex`**: 사용량 기반으로 과금되는 API를 호출하는 대신 공식 Codex CLI(`codex exec`)를 비대화식 모드로 구동하는 다섯 번째 provider입니다. 번역 사용량은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. 이는 OpenAI가 이 용도로 문서화한 유일한 방법입니다. 요금제별 제공 여부 표에는 « Codex SDK, `codex exec`, and scriptable workflows »가 Plus/Pro/Business/Enterprise에서 제공되는 것으로 나와 있지만, `~/.codex/auth.json`의 token으로는 API Platform 호출을 인증할 수 없습니다. 또한 이 스크립트는 해당 token을 전혀 읽지 않으며, 인증과 갱신은 계속 CLI가 관리합니다.
  - **npm뿐 아니라 pip로도 설치할 수 있는 Codex 바이너리**: `_resolve_codex_binary()`는 `CODEX_BIN`, 이어서 `PATH`, 마지막으로 OpenAI가 배포하는 공식 Python package **`openai-codex-cli-bin`**(`openai-codex` SDK의 dependency)에서 바이너리를 찾습니다. 따라서 Python 프로젝트에서 `--use_codex`을 사용하기 위해 더 이상 npm 전역 설치가 필요하지 않습니다. 이 package는 `requirements.txt`에 추가되지 않습니다. 바이너리 용량이 약 250MB이므로 선택 사항인 provider 때문에 모든 사용자에게 이를 강제하게 되기 때문입니다. 전체 과정을 검증했습니다. `codex`가 `PATH`에 없어도 패키징된 바이너리를 찾아 6초 만에 전체 번역을 완료합니다.
  - **« 구독 모드 » 보장**: `OPENAI_API_KEY`과 `CODEX_API_KEY`은 하위 process의 환경에서 제거됩니다. 이 보호 장치가 없으면 `.env`에 있는 key로 인해 아무런 표시 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 이는 바로 이 provider가 방지하려는 상황입니다.
  - **테스트로 방지한 CLI 함정**:
    - prompt를 인수로 전달해도 `codex exec`은 stdin을 **계속** 읽습니다. stdin을 닫지 않으면 명령은 모델을 한 번도 호출하지 않은 채 timeout까지 대기합니다(재현 결과: 180초 후 exit 124, 0바이트). 따라서 `communicate(input=...)`은 필수입니다.
    - npm으로 설치된 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 이 바이너리는 Python process의 **손자 process**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 계속 할당량을 소비할 수 있습니다. 그래서 `Popen(start_new_session=True)` + `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`을 내보내고도 0으로 종료될 수 있습니다. 반환 코드뿐 아니라 JSONL 출력(`--json`)도 검사하며, 코드가 0인데 `-o` 파일이 없으면 빈 segment를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **rate limit 시 back-off**: CLI에는 내부 retry가 구현되어 있지 않습니다(`max_retries = 0`). 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. « quota »라는 단어는 복구 가능한 429와 최종적인 `insufficient_quota` 양쪽에 모두 나타나기 때문입니다.
  - **CI 보호 장치**: `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 `--use_codex`이 거부됩니다. 구독 인증은 공유 runner용이 아니며, OpenAI도 공개 저장소에서 이 workflow를 사용하지 말라고 명시적으로 권고합니다.
  - **모델**: `gpt-5.6-sol`(품질) 및 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 계열은 CLI와 API Platform에서 공통으로 사용되지만, ChatGPT 계정으로 모든 모델을 이용할 수 있는 것은 아닙니다. allowlist는 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 사용하면 경고가 표시됩니다. Plus 요금제에서 Luna는 5시간 window당 250~2,000개의 message를 제공하는 반면 Sol은 10~100개를 제공합니다. 따라서 모든 batch 처리에는 `--eco` 모드를 권장합니다.
  - **수정된 버그 — 전체 작업에 성공해도 `regen_translations.sh`이 오류로 종료됨**: `trap ... EXIT`은 trap 실행 시점에는 더 이상 존재하지 않는 `main()`의 `local` 변수인 `failed_log`을 참조했습니다. `set -u`에서는 이로 인해 `failed_log: unbound variable`이 발생하여 28개 번역이 모두 올바른데도 스크립트가 1로 종료되었습니다. 그 결과 가장 비용이 많이 드는 단계인 재생성 직후에 `release.sh --auto`(`set -e`)이 중단될 수 있었습니다. 변수를 전역으로 변경하고 trap에서 변수의 존재 여부를 검사하도록 했습니다. 유용한 부수 효과로, 지금까지 이 오류에 가려졌던 실제 번역 실패가 종료 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: provider의 기본값보다 우선하여 특정 모델을 강제하는 `regen_translations.sh`의 새로운 환경 변수입니다. 예를 들어 처리량 중심 모델인 `--eco` 대신 구독 할당량의 고급 모델로 재생성하려면 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 사용할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때 사용할 수 있는 `REGEN_PROVIDER=codex`입니다. 사용자가 모르는 사이에 구독 할당량을 소비하지 않도록 자동 감지하지 않습니다. 병렬 처리를 시작하기 전에 token을 순차적으로 한 번 갱신합니다. Codex refresh는 회전식 일회용이므로 동시 job이 `codex login` session을 무효화할 수 있기 때문입니다. 동시 실행 수는 4로 줄어듭니다.
  - **관련 refactor**: 전체 처리 과정에 네 번째 boolean을 전달하는 대신 provider 이름을 반환하는 `_resolve_provider()`을 사용하여 `_dispatch_provider_call`의 parameter 수를 8개에서 6개로 줄였습니다. 최소한의 `Namespace`으로 `translate(..., use_mistral=True)`을 호출하는 테스트를 보존하기 위해 명시적인 boolean은 계속 `args`보다 우선합니다.
  - **테스트**: argv, 정리된 환경, 서문 방지 계약, silent failure, timeout/killpg, back-off, preflight, provider 탐색, Gemini reasoning cascade, Claude block 필터링 및 여러 문단으로 된 news 인용을 다루는 새 파일 `tests/test_codex_provider.py`(48개 테스트)을 추가했습니다. 전체 test suite는 290개 테스트입니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 참조 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 행 25개, HTML link 13개, image 13개, URL 19개, 문자 단위까지 동일한 코드 블록, 남은 placeholder 0개). 69KB 분량의 보도 기사에 `--news` 모드를 사용했을 때 `gpt-5.6-luna`과 `gpt-5.6-sol` 출력 모두 en/ja/ar에서 후속 application validator를 통과했습니다. `account/rateLimits/read`을 통해 측정한 사용량은 `--eco` 모드에서 계수기의 반올림 임계값 미만(5시간 window의 0%)으로 유지되었습니다.

- **1.9.2** 중첩 괄호 또는 프랑스어 접두사가 있는 news 출처 URL 추출 수정(2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`에서 출처 URL을 추출할 때 regex `re.search(r"\((.+?)\)", attribution)`(괄호 사이의 lazy capture)을 사용했습니다. `(relayé par [@user sur X](https://x.com/.../123))`과 같은 출처 표기에서는 괄호가 중첩되어 있습니다. 즉, 바깥쪽 `(`과 Markdown link의 `]()`이 겹칩니다. 이 때문에 capture가 처음 만난 `)`에서 멈춰 문자열이 잘리고 프랑스어 접두사까지 포함된 `relayé par [@user sur X](https://x.com/.../123`이 생성되었으며, 끝의 `)`은 누락되었습니다. 그 결과 `_validate_news_post`이 번역 출력에서 이 문자열을 찾으려다 항상 실패했습니다. 이유는 두 가지로, `)`이 잘렸고 "relayé par"가 `relayed by`/`weitergeleitet von`/... 등으로 번역되었기 때문입니다. low → medium → high → gpt-5.5의 전체 cascade가 모두 통과하지 못했습니다.
  - **수정 사항**: regex를 `re.search(r"\]\(([^)]+)\)", attribution)`으로 변경했습니다. Markdown link의 `](url)`을 구체적으로 대상으로 삼아 프랑스어 접두사나 잘림 없이 **순수 URL만** capture하며, 이 불변성은 번역 중 `#URL{N}#` placeholder로 보존됩니다. 다음 두 가지 문제 pattern을 모두 안정적으로 처리합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥쪽 괄호가 없는 프랑스어 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` class에 2개를 새로 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그를 정확히 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`을 사용한 변형)
  - **누락된 적용 범위**: `check-editorial-coverage.py`은 편집 문법을 검증하지만 translator를 통한 번역 가능성은 검증하지 않습니다. 향후 개선 사항(v1.9.2 범위 외)으로는 출처 추출을 dry-run으로 시뮬레이션하여 게시 **전에** 위험한 pattern을 감지하는 검사를 추가할 수 있습니다.

- **1.9.1** 번역 marker 안내문의 CTA label i18n 수정(2026-05-10):

  - **수정된 버그**: 번역 파일 상단의 marker banner에 있는 CTA link의 `[Voir le projet sur GitHub ↗]` label이 `target_lang`을 따르지 않고 모든 대상 언어에서 **프랑스어**로 남아 있었습니다. URL과 저장소 slug를 보존하기 위해 Python 측에서 조립되므로 LLM에는 전혀 노출되지 않으며, 그 결과 번역 단계에서 이를 바로잡을 수 없었습니다. v1.9에서 `marker` 형식을 추가한 뒤 발생한 silent regression입니다.
  - **수정 사항**: 15개 언어를 각각의 현지화 label에 매핑하는 새로운 상수 `_VIEW_PROJECT_LABELS`을 추가했습니다. 이제 `_translation_note_invariants(target_lang)`와 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달합니다. 알 수 없는 언어에는 `fr`을 fallback으로 사용합니다(안전성을 위한 처리이며 KeyError가 발생하지 않음).
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 조정했습니다(target_lang `ja` → 예상 일본어 label). 테스트 2개를 새로 추가했습니다. `test_source_link_label_localized_per_target_lang`(라틴 문자, 표의 문자, abjad를 포함한 7개 언어로 parameter화) 및 `test_source_link_label_falls_back_to_french_for_unknown_target`입니다. 전체 테스트는 `test_translation_note_position.py`에서 38개에서 40개로 늘었습니다.
  - **하위 호환성**: 기본값 `target_lang="fr"`을 포함한 signature를 사용하므로 `args.target_lang` 없이 호출하는 외부 programmatic caller도 수정 없이 계속 작동합니다.
- **1.9** 무음 실패 수정 + 종합 품질 도구 + 다중 위치 번역 메모 (2026-05-07):
  - **다중 위치 번역 메모 + "embed card" marker 형식**:
    - 새로운 CLI 옵션 추가(기본값 유지 → **비호환 변경 없음**):
      - `--note_position {top,bottom,both}`(기본값: `bottom`): 번역된 파일의 상단, 하단 또는 양쪽에 메모를 배치합니다.
      - `--note_format {legacy,marker}`(기본값: `legacy`):
        - `legacy`은 v1.8 동작을 엄격하게 재현합니다(굵은 문단 `**…**`). **byte-for-byte** 방식입니다.
        - `marker`는 보이지 않는 Markdown link reference definition(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 "GitHub repo embed card" 형태로 렌더링되도록 구성된 **3개 문단의 blockquote**를 출력합니다. 여기에는 inline code로 된 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM이 번역한 설명, 표시되는 화살표가 포함된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 들어갑니다. 빌드 시 remark plugin에서 활용할 수 있습니다(jls42.org 블로그 → `remark-translation-banner` plugin 참조).
    - **LLM에 절대 전송되지 않는 불변 요소**: repo 제목과 GitHub URL은 설명 문구를 번역한 후 Python 측에서 조합됩니다. LLM은 `ai-powered-markdown-translator` slug나 `https://github.com/jls42/...`를 절대 보지 않으므로 renderer, 대소문자 또는 scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter를 닫는 `---` 블록 **뒤에** 메모를 삽입합니다(Astro Content Collections / gray-matter 안전성). `_split_frontmatter` helper는 파일 시작 부분의 `---\n…\n---\n`를 감지하여 무결성을 보존하며, 닫는 fence 없이 열린 frontmatter에는 **`RuntimeError`을 발생시킵니다**. 따라서 잘못된 위치에 메모가 있는 파일을 작성하지 않고 해당 파일을 `failed_files`에 포함합니다.
    - **모델 sanitizer whitelist**: `_sanitize_model`은 `[A-Za-z0-9._:/-]`에 포함되지 않은 모든 문자를 `_`로 바꾸며, 결과가 비어 있으면 `unknown`을 사용합니다. Astro remark plugin 측 validator와 일치시키고 marker 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 refactor**: `_append_translation_note`(단일 monolithic 함수) → 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). Builder와 composer를 분리했습니다(builder는 구분자 없는 순수 블록을 반환하고 composer는 위치에 따라 `\n\n`을 적용). 프로덕션 코드와 source helper가 동일한 3개 문단 assembler를 공유합니다.
    - **`_quote_lines` blank-preserving**: 각 줄 앞에 `> `을 붙이고 빈 줄은 `>`만 있는 줄로 변환합니다. 이를 통해 mdast가 blockquote를 줄바꿈이 있는 하나의 문단이 아니라 서로 구분된 3개 문단(제목 / 설명 / 링크)으로 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 문단 수에 따라 처리합니다(3개 = 완전한 card 형식, 2개 = 문구 + 링크, 1개 = fallback). 1개 문단 fallback은 Markdown 링크 `](`가 감지되면 더 이상 **`**...**`로 감싸지 않습니다**(링크 주위에 `<strong>`을 적용하면 렌더링이 불안정함).
    - **상위 호환성**: `_compose_with_notes` 측에서 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")`을 사용합니다. 해당 attribute가 없는 Namespace(기존 테스트, 외부 프로그래밍 호출)도 수정 없이 계속 작동합니다.
  - **긴 번역의 무음 실패 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 적용: 결정론적 계층(원문 발췌가 그대로 발견되는지 확인) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k segment에서 잠재적인 truncation 방지, FR→JA/ZH/KO/AR/HI 교차 문자 체계 변환을 위한 여유 확보)
    - Heading-aware segmentation: segment 후반부의 H2/H3에 우선순위를 부여하여 각 segment가 완전한 의미 단위의 section으로 시작하도록 함
    - 오류를 0이 아닌 exit code까지 전파: `translate_markdown_file`은 typed status인 `success` / `failure` / `skipped`를 반환하며, 하나 이상의 파일이 실패하면 `main()`에서 `sys.exit(1)` 적용(single-file 및 batch)
    - 모든 provider에 empty-content guard 적용, source/output sanity ratio 적용(500자 이상이며 5% 미만이면 거부), code placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 후 정규화(heading에 붙은 구분자/링크), `reasoning_effort` 없이 `BadRequestError` retry
    - `langdetect==1.0.9` dependency 추가
  - **Pre-commit 품질 도구**("완전한 EurekAI 유형", hook 14개):
    - Pre-commit: ruff(lint+format), shellcheck, prettier(md/yaml/json), detect-secrets(API key 4개 보호), Lizard(CCN ≤ 12), pre-commit-hooks v5(whitespace, EOF, large-files, shebangs 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `./venv/bin/python`을 사용하는 로컬 wrapper를 `scripts/`에 배치
    - `scripts/audit_verdict.py`: 11개의 unittest를 갖춘 pip-audit JSON parser로, jls42-astro parser를 Python에 맞게 이식
    - 초기 ruff 위반 7개 수정: B904(raise from) ×2, B007(unused dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard는 `translate.py`을 일시적으로 제외(CCN 21~47인 함수 4개, refactor 예정)하며 scripts/에는 엄격한 gate 적용
  - **SonarCloud + 종합 coverage**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): push 및 pull-request마다 분석하고 `coverage.xml`을 통해 coverage 측정
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` stdlib): 무음 실패 오류 체인의 여섯 단계를 다룸
    - `tests/test_orchestration.py`(+79개 테스트): `translate.py`의 orchestration 계층을 다룸(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return branch)
    - `scripts/tests/test_audit_verdict.py`: subprocess를 통해 `main()`(stdin/stdout) 및 `if __name__ == "__main__"` 블록의 coverage 확보
    - **새 코드의 coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 matrix(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 여러 줄 prefix 처리, byte-for-byte 하위 호환성(golden literal), sanitizer, frontmatter 분할(닫히지 않은 fence에서의 raise 포함), 3개 문단 형식, 2개 문단 fallback, 1개 문단 + Markdown 링크 guard와 제목+URL이 LLM에 절대 전송되지 않음을 assert하는 핵심 safeguard `TestLLMPayloadExcludesInvariants`을 다룹니다. **테스트 190개 통과**, regression 0건.
  - 문서: badge가 포함된 `README.md`(프랑스어 + 번역 14개), `CLAUDE.md`(pre-commit workflow + 상세 CI 감시), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 버전 상향(2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token 한도 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder로 영문 인용문 보호, `LANG_FLAGS` mapping(15개 언어), 대상 언어별 flag 처리
  - 복원 전 news placeholder 검증(regression: LLM이 placeholder를 삭제하면 인용문이 없는 출력이 무음으로 생성되었음)
  - `regen_translations.sh` script의 이식성 확보(절대 경로 사용, pwd dependency 제거)
  - README/CHANGELOG의 language bar에 프랑스어 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원래 파일명을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **Inline code 보존**: 이제 번역 중 backtick(`` `...` ``)을 보호
  - System prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - template 변수 `{variable}` 보호
    - 요청하지 않은 번역자 메모 금지
  - 364개 파일에서 성공적으로 테스트(jls42.org 블로그 migration)
- **1.6** 새로운 기능:
  - 번역을 위한 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 순회하지 않는 단일 파일 번역(`--file`)
  - 간소화된 새로운 명명 pattern: `{base}-{lang}.md`
  - 모델명이 포함된 기존 형식을 유지하는 `--include_model` 옵션
  - 목록에 없는 모델을 기본 token 한도(128k)로 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`로 업데이트.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`로 업데이트.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`로 업데이트.
  - **번역 prompt 최적화:**
    - 직접 번역 및 번역 메모용 prompt에 metadata와 특정 formatting 요소의 보존에 관한 상세 지침을 포함하여 명확성과 효율성을 높였습니다.
  - **Code refactor:**
    - Mistral AI client 초기화를 위해 `MistralClient`을 `Mistral` class로 교체했습니다.
    - 가독성과 유지보수성을 높이기 위해 import를 재구성했습니다.
    - 번역 시 원래 formatting을 보존할 수 있도록 텍스트 segmentation과 code block 처리를 개선했습니다.
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 반대로 변경하여(예: `f"{base}-{args.target_lang}-{args.model}.md"`) 번역 파일의 정리와 검색을 더 쉽게 했습니다.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 code를 정리했습니다.
    - script 구조와 가독성을 개선하기 위해 소폭 조정했습니다.
- **1.4** 새로운 기능:
  - 번역을 위한 Anthropic Claude API 지원
  - 명확성과 효율성을 높이기 위한 prompt 최적화
  - code 유지보수성을 개선하기 위한 소폭 조정
- **1.3** 개선 사항 및 새로운 기능:
  - Code block 처리 개선
  - 출력 파일 관리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 모델과 언어의 순서를 반대로 변경
- **1.2** changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 최초 버전 - OpenAI API 지원

**gpt-5.6-sol을 사용하여 프랑스어에서 한국어로 번역된 기사.**
