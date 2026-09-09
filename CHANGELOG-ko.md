### 변경 기록

🌍 [프랑스어](CHANGELOG.md) | [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`: 중국의 공개 모델을 포함해 약 430개 모델로 연결되는 유료 라우터(2026-09-05):

  - **여덟 번째와 함께 제공되는 아홉 번째 provider 경로.** 1.12.0은 PyPI에 게시되지 않았으며, OpenCode와 OpenRouter 두 라우터가 함께 출시됩니다. [OpenRouter](https://openrouter.ai)는 하나의 키와 사용량에 따라 청구되는 단일 크레딧으로 다른 어떤 provider도 여기에서 제공하지 않는 모델인 Kimi, Qwen, DeepSeek, Z.ai에 접근하게 해 줍니다. endpoint가 OpenAI와 호환되므로 client는 xAI와 동일합니다. **이 provider를 구별하는 모든 요소는 preflight에 있으며**, 각 규칙은 API 측정 결과에서 비롯되었습니다.

  - **동일한 모델이 서로 다른 한도를 지닌 수십 개의 호스팅 업체에서 제공되지만, 라우팅은 이를 고려하지 않습니다.** 측정 결과: `z-ai/glm-5.2`에는 33개, `z-ai/glm-5.3-flash`에는 23개의 호스팅 업체가 있으며, 그중 하나는 **출력 tokens가 2,048개로 제한**됩니다. 따라서 23개 중 하나로 보내진 긴 번역이 아무 신호도 없이 무작위로 잘렸습니다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽어 출력 tokens가 8,000개 미만인 업체, 상태가 저하된 업체, 한도를 선언하지 않은 업체를 제외한 뒤 나머지를 고정합니다. `allow_fallbacks: false`가 **없는** `provider.only`는 선호 설정에 불과합니다. 라우터가 제외된 호스팅 업체로 다시 넘어가므로 고정이 아무 의미도 없어집니다. 한도를 충족하는 호스팅 업체가 하나도 없으면 명령이 중단됩니다. 그래도 번역을 진행하는 것은 이 preflight가 방지하려는 조용한 잘림을 받아들이는 것과 같기 때문입니다.

  - **추론은 출력 요율로 청구되며 많은 모델에서 기본적으로 활성화됩니다.** `z-ai/glm-5.2`에 동일한 요청을 보내 “OK”라는 응답을 받은 결과, **모델 기본값에서는 completion tokens가 107개였고 추론을 끄면 2개**였습니다. 추론이 아무 이점도 주지 않는 번역에서는 모든 파일의 모든 segment마다 비용이 18배로 늘어납니다. 따라서 기본적으로 비활성화됩니다. 추론을 강제하는 **431개 중 288개 모델**(`reasoning.mandatory`)은 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`로 응답합니다. 이 모델들에 대해서는 preflight가 허용되는 effort를 읽고 가장 낮은 값을 요청합니다(다음 항목). effort는 추론이 먼저 소비하는 **`max_tokens`의 일정 비율**을 할당하므로, 임의로 값을 고르면 빈 페이지 위험이 줄어드는 대신 위치만 바뀝니다.

  - **추론을 강제하는 모델에는 해당 모델이 허용하는 가장 낮은 effort를 지정하며, 이는 측정 결과에 따른 결정입니다.** 처음에는 모델을 대신해 추측하지 않도록 아무것도 보내지 않는 방식을 선택했습니다. catalogue 기본값이 `max`인 `z-ai/glm-5.3-flash`에서 검증한 결과, 이 선택은 번역이 끝나기 전에 **32,768 tokens에서 출력이 잘리는** 결과를 냈으며 14개 언어 중 2개가 누락되었습니다. envelope를 늘려도 달라질 것이 없었습니다. effort가 그중 일정 비율을 할당하므로 envelope와 함께 추론도 커지기 때문입니다. 따라서 provider는 preflight에서 `supported_efforts`을 읽고 가장 낮은 값을 요청하며, catalogue에 사용할 수 있는 값이 없으면 “없음”으로 fallback합니다. 문제가 발생했던 언어로 반증 시험을 한 결과, 이전에는 budget 소진으로 실패했지만 이제는 source와 동일한 구조를 유지하며 9분 안에 완료됩니다.

  - **이제 상위 호스팅 업체의 장애에는 해당 업체의 이름이 표시됩니다.** 라우터는 이 경우를 null인 `native_finish_reason`가 포함된 `finish_reason=error`으로 정규화합니다. 두 언어에서 각각 정확히 750초 만에 두 차례 측정되었습니다. 기존의 일반적인 메시지는 document나 분할에서 결함을 찾도록 유도했지만, 이제는 공급자 측 장애이며 재시도만으로 해결되는 경우가 많다고 안내합니다.

  - **출력이 비어 있는 `finish_reason=length`은 잘림이 아닙니다.** 유용한 첫 문자가 나오기 전에 추론이 budget을 모두 소비한 경우입니다. 측정 결과 유용한 tokens 148개를 위해 추론 tokens 15,850개가 사용되었습니다. 두 경우에는 정반대의 조치가 필요합니다. 첫 번째 경우에는 segment 크기를 줄여도 아무 소용이 없습니다. 메시지에서 두 경우를 명시적으로 구분합니다. 측정 결과를 토대로 두 가지 보호 장치도 추가했습니다. 상위 호스팅 업체가 실패하면 라우터가 **오류만 담긴 body와 함께 200으로 응답**하며(`choices[0]`은 메시지를 가리는 불투명한 `TypeError`을 발생시켰습니다), context window는 catalogue에서 읽어 `MODEL_TOKEN_LIMITS`에 기록합니다. `DEFAULT_TOKEN_LIMIT`은 catalogue의 44개 모델에서 잘못되어 있으며, 여기에는 tokens가 4,095개로 제한된 모델 2개도 포함됩니다.

  - **`--model fournisseur/modèle`은 필수이며 네트워크에 연결하기 전에 형식을 검증합니다.** OpenRouter는 공급자가 아닙니다. 선택에 따라 가격, 라이선스, 데이터 처리가 달라지므로 사용자를 대신해 결정할 수 없습니다. slug가 preflight URL에 삽입되므로 검증은 단순한 사용 편의성 문제가 아니라 경로 주입을 방지하는 보호 장치입니다. 두 라우터가 공유하는 namespace 형식의 regex는 `a/b/..`을 허용하므로 상위 segment를 명시적으로 거부합니다. `--eco`은 아무 효과가 없으며 이를 안내합니다.

  - **세 가지 표현을 수정했으며, 그중 하나는 사실과 달랐습니다.** `codex exec`에 관한 OpenAI의 경고는 repository가 공개되어 있다는 점이 아니라 공유 runner에 개인 session 파일을 주입하는 문제를 다뤘습니다. README, CLAUDE.md, code에서 그 의미를 반대로 인용하고 있었습니다. OpenCode 인증 위치는 1.18.27에서 `opencode.db`의 `credential` table로 변경되었으며, 더 이상 `auth.json`이 아닙니다. “여기서는 절대 읽지 않는다”라는 invariant는 여전히 참이었지만 주소는 오래된 정보였습니다. 마지막으로 OpenCode section에서는 검증된 적 없는 경로를 더 이상 동등하게 소개하지 않습니다. Zen gateway와 Ollama는 end-to-end로 측정했지만 GitHub Copilot, LM Studio, llama.cpp는 측정하지 않았으며, 이제 README에 이 사실을 명시합니다.

  - **측정 캠페인과 README의 권장 모델 표.** 세 종류의 document 모음에서 300회가 넘는 번역을 14개 언어로 실행했습니다. `--news` mode의 밀도 높은 blog article, 표준 Markdown 형식의 이 README, 그리고 GitHub에서 그대로 가져온 잘 알려진 project README 4개를 사용했습니다. 표는 이전까지 혼동하던 두 가지, 즉 번역이 **완료되는지**와 번역 결과의 **구조가 source와 동일한지**를 구분합니다. 밀도 높은 두 document에서 단 하나의 정보도 누락하지 않은 모델은 세 개였습니다. `gemini-3.7-flash`, ChatGPT 구독의 `gpt-5.6-sol`, OpenRouter를 통한 `z-ai/glm-5.2`이며, 유일한 차이는 한두 언어에서 `**` 한 쌍이 옮겨지지 않은 것입니다. 핵심 관찰 결과는 **판별 요인이 `--news` mode가 아니라 document의 밀도라는 점**입니다. 구독형 Grok은 blog article에서 14회 중 13회 실패했지만 공개 README에서는 16회 중 14회 성공했으며, 원인은 반증 시험으로 확인된 긴 segment에서의 이탈이었습니다. 표 자체에도 주의 사항이 있습니다. 이 표는 모든 항목을 망라하지 않고 특정 시점의 결과이며, 소요 시간은 순위를 뜻하지 않습니다. 올바른 방법은 여전히 자신의 document로 직접 측정하는 것입니다.

  - **구조 비교기가 비라틴 문자 체계에서 두 건의 false positive를 만들었기 때문에 수치를 공개하기 전에 수정했습니다.** 전각 닫는 괄호 `）`이 뒤따르는 URL은 `)`에서 멈추는 regex로 잘리지 않았으며, URL 자체는 동일해도 추출된 문자열은 달랐습니다. 또한 프랑스어로 다섯 줄인 인용문이 중국어로 세 줄에 들어가면 줄 단위 count가 감소했습니다. 두 수정 사항은 반증 시험으로 검증했습니다. URL, section 또는 inline code 하나를 삭제하면 여전히 감지됩니다. 이 수정이 없었다면 Gemini와 Codex의 결과가 14개 언어 중 각각 13개와 12개가 아니라 11개로 공개되었을 것입니다.

  - **테스트**: 새 파일 `tests/test_openrouter_provider.py`(테스트 76개) — 모델 검증 및 상위 segment 거부, 호스팅 업체 고정(한도, 상태, 선언되지 않은 한도, 공통 최솟값), `allow_fallbacks`은 항상 false, `mandatory`에 따른 추론 비활성화 또는 유지, 완전한 출력 contract(200 응답 안의 오류, 선택지 없음, 잘림과 구분되는 빈 페이지, 비정상적인 `finish_reason`, null content), catalogue에 연결할 수 없을 때 fail-closed하는 preflight, 누락된 slug와 정상 호스팅 업체 부재, flag 상호 배타성 및 filename label을 다룹니다. 전체 suite는 **502개 테스트**입니다.

  - **Refactor: 동작은 한 줄도 바꾸지 않고 4,253줄짜리 단일 module을 여러 module로 분할했습니다.** `src/aipmt/translate.py`을 `config`, `markdown`, `segmentation`, `guards`, `placeholders`, `news`, `prompts`, `notes`, `naming`, `pipeline`, `cli`과 subpackage `providers/`로 나눴습니다(provider마다 하나의 module, 기반 역할의 `base`, resolution 및 dispatch용 `registry`). 각 이동은 기계적으로 검증된 commit입니다. verifier가 package의 모든 최상위 node에 대한 AST를 reference snapshot과 비교하고, 각 symbol의 위치, security marker가 그대로 유지되었는지, 추적되지 않은 파일이 없는지를 검사합니다. 이 임시 도구는 다음 version에서 제거되었습니다. 눈에 보이는 변경 사항은 다음과 같습니다. `aipmt.translate`은 module이 `_` prefix 없이 공개하던 64개 이름을 객체 identity 그대로 다시 공개하는 façade가 되었습니다(`__all__`에는 지원되는 API인 9개가 있고 나머지는 호환성을 위한 alias입니다). 또한 `import *`이 수집하던 dependency 및 standard library의 29개 이름은 더 이상 다시 export하지 않습니다. 파일 직접 실행(`python src/aipmt/translate.py`)은 더 이상 지원하지 않으며 `aipmt`와 `python -m aipmt`이 지원되는 두 가지 형식으로 남습니다. public function의 `__module__`은 해당 function을 정의한 module의 값입니다. 알려진 영향은 없지만 SDK는 `.env`를 불러온 후에 import하며, 더 이상 그전에 import하지 않습니다. 427개 테스트는 identifier까지 그대로 유지한 채 각 테스트가 검증하는 module로 이동했습니다. façade를 거치던 patch 91개는 이제 이름을 참조하는 module을 직접 대상으로 하며, 그중 2개는 patch가 없어도 통과한다는 사실을 측정했습니다. façade를 고정하는 contract test 7개를 추가했고, 어느 gate도 검증을 중단함으로써 통과 상태로 바뀔 수 없도록 첫 번째 이동 전에 gate 도구를 다시 작성했습니다. directory 단위의 Lizard scope와 하한선, 생성된 parser에서 읽는 flags, package 단위 coverage 하한선, 추적되는 module을 열거하는 `release.sh`이 포함됩니다.
  - **수정(pull request 검토)**: OpenRouter는 `context_length`이 없는 catalogue entry에서 측정값인 것처럼 기본값 128,000 tokens를 기록하지 않고 해당 entry를 거부합니다. 기존 동작은 “목록에 없는 모델” 경고까지 비활성화했습니다. 또한 `finish_reason`이 null일 때(document에 명시된 type은 `string | null`)는 호스팅 업체의 원문 사유를 기준으로 삼으며, `max_tokens`은 `length`입니다. 선택지 자체에 오류가 있으면 함께 포함된 일부 content도 거부하며, 정규화된 상위 장애와 동일하게 호스팅 업체 세부 정보, 원문 사유, 조언을 하나의 메시지로 제공합니다. OpenCode는 `part: null` event에서 `AttributeError`이 아니라 자체 contract error로 응답하며, 읽을 수 없는 event line이 있는 JSONL stream에서 일부 text를 받아들이지 않고 거부합니다. agentic CLI 세 개는 호출 도중 해당 process가 `SIGTERM`을 받으면 agent의 process group을 종료합니다. regen의 `timeout`는 agent를 계속 살려 두어 quota를 소비하게 했습니다. 또한 group의 `SIGKILL`은 항상 grace period를 따르므로 정상적으로 종료되는 shim도 grandchild를 살려 두지 않습니다. 분할 과정에서 갈라졌던 `# fmt: off` / `# fmt: on` 한 쌍을 다시 연결했습니다. `--reasoning_effort`의 help에는 이를 사용하는 네 provider가 명시됩니다.
  - **수정(두 번째 재검토)**: 이제 OpenRouter에 요청하는 출력 한도는 prompt와 segment가 차지하는 context 몫을 남겨 둡니다. `context_length`은 입력과 completion을 **모두** 포함하며, catalogue의 모델 6개는 입력을 위한 공간도 없이 요청이 전송되고 있었습니다. context가 너무 짧으면 비용이 청구되기 전에 거부합니다. POSIX process group이 없는 환경에서는 agentic CLI 기반 계층이 `terminate`으로, 이어서 `kill`로 fallback합니다. 더 이상 `AttributeError`이 timeout 보호 장치를 통과해 대기가 길어지도록 두지 않습니다. OpenCode의 `429` marker는 이제 substring이 아니라 숫자로 검색합니다. 이전에는 `err_84290b` 같은 error identifier가 90초의 back-off를 유발한 뒤 결국 실패했습니다. 마지막으로 canonical 형식이 아닌 OpenRouter endpoint는 preflight에 표시됩니다. project의 `.env` 하나만으로도 endpoint를 설정할 수 있으며, 이후 실제 키가 그 endpoint로 전송되기 때문입니다.
  - **보안: project의 `.env`은 더 이상 API 호출을 redirect할 수 없습니다.** `find_dotenv(usecwd=True)`은 현재 directory와 그 parent에서 파일을 찾습니다. 이 때문에 신뢰할 수 없는 directory tree, 즉 방금 clone한 repository가 어떤 키도 모르는 상태에서 `OPENROUTER_BASE_URL`, `XAI_BASE_URL` 또는 `OPENAI_BASE_URL`(마지막 것은 SDK 자체에서 읽음)을 설정할 수 있었고, 이후 environment나 user configuration에서 가져온 실제 키가 타사 server의 authorization header로 전송되었습니다. filter는 목록이 아니라 PATTERN을 기준으로 합니다. 설치된 SDK를 조사한 결과 routing variable 12개를 읽고 있었고, 그중 6개는 Anthropic client 하나에서만 사용했습니다. 수동으로 작성한 목록이었다면 절반을 빠뜨렸을 것입니다. 따라서 project layer에서는 `_BASE_URL`, `_API_BASE` 또는 `_ENDPOINT`에 해당하는 모든 variable, proxy와 certificate store(control 가능한 authority를 지정하면 interceptor를 실제 server와 구별할 수 없게 됨), 그리고 `XDG_CONFIG_HOME`와 `APPDATA`을 거부합니다. 이들을 설정하는 것은 어느 파일이 user layer를 구성하는지 결정하는 것과 같아 우회적으로 filter를 피할 수 있었기 때문입니다. 이러한 variable은 사용자가 제어하는 두 layer, 즉 export된 environment와 `~/.config/aipmt/.env`에서만 허용됩니다. 또한 project layer는 interpolation **없이** 읽습니다. `load_dotenv`은 기본적으로 `${VAR}`을 확장하므로, `NOM_ANODIN=${OPENAI_API_KEY}`이 포함된 신뢰할 수 없는 `.env`은 subprocess의 pattern 기반 filtering이 인식하지 못하는 이름으로 실제 키를 복사했습니다. 그 결과 공표된 invariant와 달리 키가 `codex exec`의 environment에 들어갔습니다. 마지막으로 거부 메시지에는 variable 이름만 표시합니다. `https://${CLE}@hôte/` 형식의 URL은 거부되는 중에도 interpolation된 키를 log에 유출했습니다. 거부 사실과 해결 방법은 stderr로 안내되며, 기업용 relay는 user configuration에 선언해야 합니다.
  - **수정: OpenRouter 출력 envelope를 호출마다 계산합니다.** `context_length`은 입력과 completion을 **모두** 포함하며, 라틴어 text에 맞춘 고정 reserve로는 아무것도 제한할 수 없습니다. `o200k_base` tokenizer로 측정한 결과 16,000자는 프랑스어에서 3,200 tokens, 일본어에서 12,300 tokens, emoji에서 17,500 tokens에 해당했습니다. 따라서 budget은 실제로 전송되는 text에서 계산하고 UTF-8 byte 수만큼 여유를 더합니다. byte fusion을 사용하는 모든 tokenizer, 즉 byte-level BPE와 byte fallback을 사용하는 SentencePiece처럼 catalogue에서 사용하는 계열에서는 token 하나가 최소 1byte에 해당하며, OpenRouter가 알 수 없는 수십 개의 tokenizer로 route하는 이 환경에서는 이것만이 사용 가능한 상한입니다. 평균 ratio는 사용할 수 없었습니다. supplementary plane의 ideograph는 token당 1.33byte까지 내려가고 combining character는 1.00byte까지 내려갑니다. 이제 입력과 출력은 설계상 window 안에 들어갑니다. 선택한 모델에 비해 지나치게 밀도 높은 segment는 비용 청구 후가 아니라 호출 전에 거부합니다.

- **1.12.0** Provider `--use_opencode`: 공개 source agent인 OpenCode를 통해 사용자가 선택한 공급자, 즉 local model, 계정 없이 무료로 사용하는 model, 구독 또는 키로 연결(2026-09-04):
  - **앞선 일곱 가지와 성격이 다른 여덟 번째 provider 경로.** [OpenCode](https://opencode.ai)(MIT)는 모델 provider가 아니라 사용자가 OpenCode 자체에 구성한 대상(API 키, 구독 서비스(GitHub Copilot, ChatGPT, SuperGrok), **계정 없이** 무료 모델을 제공하는 OpenCode Zen 게이트웨이 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp))으로 연결하는 _라우터_다. 이 스크립트는 Codex와 Grok을 제어하는 것처럼 비대화형 모드에서 `opencode run`을 제어하며, 동일한 하위 프로세스 기반(독립 프로세스 그룹, 타임아웃 시 `SIGTERM` 후 `SIGKILL`, 항상 닫힌 stdin, 정리된 환경)을 재사용한다. **실제 번역 두 건**으로 검증했다. `opencode/mimo-v2.5-free`을 사용해 이 README 전체를 영어로 번역한 결과 49초, 단일 패스, 원본 파일과 동일한 구조(제목 32개, 코드 블록 닫기 26개, 링크 18개, URL 37개, 표 행 37개, inline code 135개)를 기록했으며, `ollama/qwen2.5:7b`을 사용한 테스트 파일은 아무 키 없이 로컬에서 번역했다.

  - **`--model provider/modèle`은 필수이며, 이는 의도적인 선택이다.** `--model`이 없으면 OpenCode는 자체 기본값으로 되돌아가며, 새로 설치한 환경에서는 그 기본값이 학습에 대화 내용이 사용될 수 있는 무료 « stealth » 모델인 `opencode/big-pickle`이다. 실제 측정에서도 이 모델이 응답했다. 사용자 대신 이를 암묵적으로 선택하는 것은 이 저장소가 추적하는 바로 그 보이지 않는 전환이 될 수 있다. 따라서 오류 메시지에는 모델 목록을 표시하는 명령(`opencode models`)과 세 가지 예시(로컬, 무료, 구독)가 명시된다. `--eco`은 효과가 없으며 이를 명확히 알린다. `--reasoning_effort`은 명시적으로 요청된 경우에만 OpenCode의 `--variant`으로 그대로 전달된다.

  - **추정이 아닌 측정된 격리.** inline 구성(`OPENCODE_CONFIG_CONTENT`, OpenCode 병합 순서에서 마지막이므로 사용자 구성을 대체하지 않으면서 우선 적용됨)은 모든 도구를 거부하는(`permission: {"*": "deny"}`) `aipmt` agent를 정의한다. 레지스트리가 더는 모델에 도구를 제시하지 않으므로, « 파일을 나열하고 `id`을 실행하라 »고 명령해도 도구가 없다고 응답한다. 세션 공유를 비활성화하고 외부 plugin을 제외하며(`--pure`), `--auto`은 절대 사용하지 않고, 비어 있는 일회용 작업 디렉터리를 사용한다. 암묵적 주입 두 가지도 측정한 뒤 차단했다. `OPENCODE_DISABLE_CLAUDE_CODE`이 없으면 사용자의 `~/.claude/CLAUDE.md`이 **모든** prompt에 들어가 단순한 « 안녕하세요 »에도 입력이 186 tokens가 아닌 515 tokens가 된다. `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 디렉터리의 `AGENTS.md`도 들어가며, « 모든 응답을 BANANA로 끝내라 »는 지시가 번역에 실제로 적용되었다. 반면 전역 `~/.config/opencode/AGENTS.md`은 계속 주입된다. 이를 제외하는 스위치는 없으며, 변칙적으로 `XDG_CONFIG_HOME`을 우회하면 사용자의 provider도 함께 가려진다. 임시방편으로 고치지 않고 문서화했다.

  - **`exit 0`은 아무것도 입증하지 않는다. 세 번째 CLI에도 같은 원칙을 적용하되, 이 CLI만의 함정 두 가지가 있다.** 알 수 없는 `--agent`을 지정해도 `opencode run`은 실패하지 않는다. stderr에 경고를 출력한 뒤 활성화된 도구를 갖춘 코딩 agent로 **조용히** 되돌아간다. 따라서 inline 구성이 적용되지 않으면 번역은 쓰기 권한이 있는 agent로 실행된다. 이를 막기 위해 출력 계약에서는 이 메시지가 없음을 확인하는 동시에 반환 코드 0, `error` 이벤트 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`임을 확인한다(`length`은 잘린 응답이다). 또한 텍스트가 비어 있지 않은지도 확인한다. 두 번째 함정은 오류 JSON 이벤트가 **불투명**하다는 점이다. « 예기치 않은 서버 오류입니다. 자세한 내용은 서버 로그를 확인하세요. »라는 문구와 단순 참조만 표시되며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 로그에만 존재한다. 그래서 `--print-logs --log-level ERROR`과 stderr의 `error="…"` 필드를 읽되, 뒤따르는 Bun trace는 제외한다. 이에 따라 알 수 없는 모델은 원인을 명시하면서 1초 안에 실패한다. 또한 `--title`은 불필요한 LLM 호출을 방지한다. 이것이 없으면 OpenCode는 `small_model`에서 한 차례 더 요청해 세션 제목을 생성한다.

  - **비밀 정보: Codex 및 Grok과 동일한 패턴 기반 필터링을 적용하되, 명시적으로 지정한 예외 하나가 있다.** `OPENCODE_API_KEY`은 유지된다. 이는 OpenCode 자체의 키(Zen 게이트웨이, Go 구독)이며, OpenCode를 명시적으로 대상으로 한다. 즉 OpenCode의 `auth.json`에 해당하는 것으로, aipmt가 관리하거나 과금할 수 있는 키가 아니다. provider는 OpenCode에서 구성하며(`opencode auth login`, `opencode.json`), aipmt의 `.env`에서는 절대 구성하지 않는다. aipmt의 어떤 키도 하위 프로세스에 전달되지 않는다. 구독형 CLI와 달리 CI에서는 거부하지 않는다. runner에서 API 키나 자체 호스팅 모델을 사용하는 것은 정당한 용도이기 때문이다.

  - **경로 이탈 방지 장치는 이제 원시 값이 아니라 보간된 값을 검사한다.** `provider/modèle`에는 1.10.0의 보호 장치가 거부하던 `/`이 포함되어 있다. `--model`이 파일 이름 `--include_model`에 보간되므로 당시의 거부는 타당했다. 이제 파일 이름 label은 보간 전에 `/`, `\`, `:`을 `-`으로 바꾸며(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, `:`은 Windows에서 허용되지 않음), 상위 보호 장치는 이 label을 검사한다. 따라서 `../../evil`은 대상 아래의 단순 이름 `doc-en-..-..-evil.md`이 되고, `..`만 계속 거부되며 `--target_lang ../x`도 거부된다. 범위 보호 장치 `_ensure_within_directory`은 변경 없이 두 번째 방어 계층으로 유지된다.

  - **무료 모델과 로컬 모델에 관해 실제로 측정한 결과.** `opencode/mimo-v2.5-free`은 문단 하나를 16초, 이 README를 49초 만에 번역한다. `opencode/big-pickle`은 200단어에 40초가 걸렸으며, 각각 단독으로는 완료되던 요청 두 개를 동시에 실행하자 5분 동안 응답하지 않았다. `opencode/nemotron-3.5-lightning-free`은 3분 동안 아무 응답도 하지 않았다. 따라서 `REGEN_MODEL`을 필수로 지정하고 **2 jobs**를 병렬로 실행하는 `REGEN_PROVIDER=opencode`을 사용한다. 로컬 환경에서 Ollama는 문맥을 흔히 4,096 tokens로 구성하지만 segment는 최대 16,000자에 이른다. 그러므로 `PARAMETER num_ctx 32768`을 포함한 `Modelfile`이 필요하며, 품질은 모델에 좌우된다. 테스트 파일에서 7B 모델은 목록의 순서를 뒤집고 코드 블록 닫기 하나를 손상시킨 반면, 게이트웨이 모델은 모든 요소를 보존했다.

  - **이 저장소의 번역은 이제 유료 API를 절대 거치지 않는다.** `regen_translations.sh`은 `.env`에 키가 하나라도 남아 있으면 곧바로 OpenAI API를 사용하고 Codex는 명시적으로 선택한 경우에만 사용했다. 이번 버전을 준비하면서 정확히 이런 일이 발생했다. 28개 번역이 OpenAI API로 전송된 뒤 힌디어 CHANGELOG가 Gemini API로 전송됐지만, ChatGPT 구독은 애초에 사용량 기반 비용을 내지 않기 위해 존재한다. 키 자동 감지는 제거한다. **기본값은 고품질 모델인 `gpt-5.6-sol`을 사용하는 Codex다.** `openai`, `gemini`, `grok`는 `REGEN_PROVIDER`뿐 아니라 `REGEN_ALLOW_PAID_API=1`도 요구한다. 이는 결정 시점에 규칙이 실제로 적용되도록 명시한 예외다. 알 수 없는 `REGEN_PROVIDER`은 API로 되돌아가지 않고 실패한다. 테스트 열 개가 기본값, 거부, 예외를 고정한다. 이번 버전의 28개 번역은 Codex를 통해 다시 수행했다.

  - **rate limit의 back-off를 공통화했다**(`_retry_on_rate_limit`). Codex와 Grok의 loop는 label만 다르고 동일했으며, 세 번째 복사본까지 만들면 중복 임계값을 넘게 된다. 세 CLI 오류는 동일한 `_CliCallError`에서 파생된다. 세 오류 중 하나라도 이를 벗어나 공통 loop가 감지하지 못하는 상황을 테스트로 금지한다.

  - **테스트**: 새로운 파일 `tests/test_opencode_provider.py`(61개 테스트)에서 완전한 출력 계약, agent fallback, 로그에서 원인 읽기, 중복된 텍스트 part 제거 및 합성 part 무시, timeout 시 프로세스 그룹 종료, 429 back-off, 필수 모델 지정 및 검증, 비밀 정보 없는 preflight, binary 탐색, dispatch 연결, 파일 이름 label, 경로 이탈 반증을 다룬다. `tests/test_review_hardening.py`는 flag 상호 배타성과 비밀 정보 부재 검사를 새로운 provider까지 확장한다. 이제 gate는 문서화된 argparse flag **22개**를 요구한다. 전체 제품군은 **382개 테스트**다.

- **1.11.1** 문서 수정: README에 마침내 일곱 가지 provider 경로를 명시했다(2026-09-03).

  - **1.11.0의 PyPI 페이지에는 « 4개 API + Codex CLI »라고 적혀 있었다.** 실제 코드는 일곱 가지를 제공한다. OpenAI, Mistral, Claude, Gemini, Grok은 API로 사용하며, Codex(ChatGPT)와 Grok은 사용량 기반 과금 없이 구독으로 사용한다. 소개 문구와 _Multi-Provider_ 항목에서 두 Grok 모드가 빠졌고, 14개 번역도 같은 오류를 반복했다. 패키지의 긴 설명은 버전별로 고정되므로 공개 페이지를 수정하려면 새 버전 번호가 필요했다. 이것이 이 버전이 존재하는 유일한 이유다. **코드 변경은 없다.**
  - `CLAUDE.md`을 배포 과정에서 도입된 내용에 맞췄다. gate 카운터(`--full`에서는 16, 17), 활성 workflow 11개, `gh pr checks`에 보이지 않는 Sonar/Codacy 카운터 두 개(hotspot, Codacy API), `ruff-format`에 의한 `# nosemgrep` 이동, OIDC 교환에 필요한 GitHub environment, 그리고 _pending publisher_가 이름을 선점하지 않는다는 사실을 반영했다.

- **1.11.0** PyPI 배포: 저장소를 clone하지 않고 `pip install ai-powered-markdown-translator` 후 `aipmt` 명령으로 설치한다(2026-09-03).

  - **단일 파일 스크립트가 설치 가능한 패키지가 되었다.** `translate.py`은 루트에서 `src/aipmt/translate.py`로 이동했으며, console entry point `aipmt`와 이에 상응하는 `python -m aipmt`을 제공한다. 기여하려면 여전히 저장소를 clone해야 한다. 테스트, 28개 번역, 품질 도구가 저장소에 있기 때문이다. 하지만 사용만 하는 경우에는 더 이상 필요하지 않다.

    - **import 이름은 `aipmt`이며 절대 `translate`이 아니다.** 실제로 충돌이 발생하며 아무 경고도 없기 때문이다. PyPI 패키지 `translate`(v3.8.1, 마지막 업로드 2026-07-06)은 같은 이름의 디렉터리를 설치한다. venv에서 재현한 결과 디렉터리가 module보다 우선되어 `translate.main`이 사라지고, entry point는 `AttributeError`에서 깨진다. 그런데도 `pip check`은 « 손상된 요구 사항을 찾지 못했습니다 »라고 응답하며 rc=0을 반환한다. 사용자가 단순히 `pip install translate`을 실행하는 것만으로도 유용한 진단 없이 CLI가 깨질 수 있었다. 실제 wheel로 반증한 결과, 해당 패키지 위에 `pip install translate`을 설치해도 `aipmt --help`는 설치 전후 모두 rc=0이며 두 CLI가 공존한다.
    - **긴 배포 이름, 짧은 명령.** `ai-powered-markdown-translator` 덕분에 PyPI 검색에서 패키지를 찾을 수 있다. 약어만 사용하면 프로젝트를 이미 아는 사람 외에는 찾을 수 없지만, 배포의 목적은 바로 새 사용자가 발견하게 하는 것이다. 그럴듯한 후보 두 개는 확인 후 제외했다. `ai-markdown-translator`은 동일한 목적의 도구가 2024년부터 npm에서 사용하고 있으며, 이 저장소보다 17개월 먼저 등장했다. `aimt`는 같은 분야에서 활발히 유지되는 패키지 `aim`(v3.29.1)과 한 글자 차이다. 이는 장기적인 혼동을 일으키기에 최악의 조건이다. 방법론상의 함정도 있다. `pypi.org/project/<nom>/`은 어떤 이름에도 200을 반환하는 anti-bot 페이지이므로 JSON API만 신뢰할 수 있다.
    - **평면 패키지 대신 `src/` layout.** 평면 패키지를 사용하면 테스트의 `sys.path.insert(..., "..")` 여섯 개를 유지할 수 있지만, 그것이 바로 문제다. 이들은 패키지 대신 소스 트리를 import하므로 packaging 오류를 모두 가린다. 실제 비용은 치환 규칙 하나를 추가하는 것뿐이다.

  - **마침내 키를 한 번만 구성하면 된다.** 설치된 CLI에는 영구적인 구성이 없었다. 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었다. `find_dotenv`은 시스템 루트까지 거슬러 올라가므로 **사용자의 홈 디렉터리 아래에서 작업할 때는** `~/.env`을 찾았지만, 다른 위치에서 작업하면 아무것도 찾지 못했다. 이는 의도적인 설계가 아니라 명령을 실행한 위치에 따라 달라지는 불완전한 지원이었다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`을 추가했다.

    - **우선순위는 별도 코드로 정하지 않는다.** `load_dotenv`의 기본값인 `override=False`에서 자연스럽게 결정된다. 각 계층은 이전 계층이 비워 둔 값만 채운다. 따라서 환경 변수 → 프로젝트의 `.env` → 사용자 구성 순서가 되며, 구조가 아니라 동작을 검사하는 테스트로 검증한다. 두 호출의 순서를 바꾸거나 세 번째 계층을 제거하면 테스트가 실패한다.
    - **의도적으로 TOML이 아닌 `.env` 형식을 사용한다.** `python-dotenv`은 이미 dependency이고, 해당 문법은 15개 README에 이미 문서화되어 있으며, 동일한 파일을 두 범위 모두에서 사용한다. 새로운 dependency나 문법은 없다. 위치는 `XDG_CONFIG_HOME`이 **절대 경로**일 때 이를 따른다. 명세상 상대 값은 무시해야 하며, 그러지 않으면 구성 위치가 다시 현재 디렉터리에 종속된다. Windows에서는 `APPDATA`을 따른다.
    - **두 가지 대안을 이유와 함께 제외했다.** 시스템 keyring(`keyring`)은 desktop에서는 더 안전하지만 서버, container, CI 같은 headless 환경에서는 실패한다. 이는 바로 batch 번역의 핵심 사용 사례다. opt-in 후보로는 적절하지만 기본값으로는 적합하지 않다. `--api-key` flag를 사용하면 키가 shell history에 남고 `ps`에 노출된다.
    - **키가 없을 때 더 이상 호출 trace를 표시하지 않는다.** 이전에는 사용자에게 `site-packages`을 가리키는 Python stack과 함께 « 환경 또는 .env »라는 메시지를 보여 주면서 두 번째 파일을 어디에 만들어야 하는지는 설명하지 않았다. 이제 세 위치와 정확한 경로를 모두 나열하고 명령은 2로 종료된다. 안전망은 **의도적으로 좁다**. 구성 단계에만 `except ValueError`을 적용한다. 전체 실행을 감싸면 번역 중 발생한 실제 bug까지 안심시키는 메시지로 바뀌는데, 이것이 바로 이 저장소가 추적하는 실패 방식이다. 테스트가 `main()`의 source를 읽어 이를 금지한다.

  - **수정 사항 — 도구를 설치하면 사용자의 `.env`이 무시되던 문제.** 인수 없는 `load_dotenv()`은 현재 디렉터리부터 거슬러 올라가지 않고 호출한 파일, 즉 `site-packages`부터 올라간다. 자체 `.env`이 있는 프로젝트에서 실제 console entry point를 실행해 측정한 결과, `find_dotenv()`은 `''`를 반환하고 키를 불러오지 못했지만 `find_dotenv(usecwd=True)`은 키를 찾았다. 도구가 clone된 저장소 안에서만 실행될 때는 이 bug가 없었다. 배포 후에는 올바르게 구성했는데도 API 키가 « 누락됨 »으로 표시되는 증상만 남긴 채 항상 발생했을 것이다.

  - **세 gate는 아무것도 검사하지 않게 되었는데도 정상 상태로 표시될 수 있었다.** 의도적으로 이동 전에 강화했다. 포착해야 할 변경 이후에 작성한 보호 장치는 아무것도 입증하지 못하기 때문이다. 각 gate는 원본 저장소에서는 정상 상태이고 이동된 복사본에서는 실패 상태로 바뀐다. 두 방향을 모두 측정했다.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시한다.** rc=0과 « 분석된 파일 0개 »를 반환한다. 복잡도 gate는 158 functions / 2247 nloc에서 3 functions / 34 nloc로 줄면서 출력은 0 bytes가 되었을 것이다. 이제 scope는 각 항목의 존재 여부를 검사하는 배열이다.
    - **존재하지 않는 module에 대한 `coverage run --source=`은 실패하지 않는다.** stderr에만 경고를 출력하고 unittest와 `coverage xml` 모두 rc=0을 반환하며 보고서도 그대로 배포한다. statements가 1453개에서 141개로 잘렸는데도 프로젝트가 거의 분석되지 않았기 때문에 정상인 것처럼 보였을 것이다. 두 가지 하한선으로 보고서를 보호한다. 전체 수치와 측정된 가장 큰 파일의 수치다.
    - **번역 최신성 probe는 invocation 형식을 구조적으로 감지하지 못한다.** argparse flag를 기준점으로 삼는데, 파일 이름을 바꿔도 이 flag들은 그대로이기 때문이다. module을 이동하고도 15개 README가 존재하지 않는 명령을 계속 문서화한 상태에서 « 오래된 번역 없음 »이라는 판정이 나온 것을 재현했다. 따라서 일곱 번째 section은 option이 아닌 형식을 검사하며, Lizard hook을 실제 script scope와 대조한다. 해당 hook의 `files:`은 더 이상 일치하지 않아도 pre-commit을 실패시키지 않고 건너뛰게 만든다.
  - **`requires-python = ">=3.10"`은 더 이상 근거 없는 선언이 아닙니다.** `sonar-project.properties`은 이미 3.10~3.12를 명시하고 있었지만, 개발 환경에는 3.12만 있었기 때문에 실제로 이 범위를 검증한 적이 없었습니다. 이는 배포 시 공개되었을 내부 모순이었습니다. 이제 테스트 workflow는 3.10, 3.11, 3.12에서 테스트 모음을 실행하며, 패키지를 설치해 공개된 버전 범위까지 검증합니다.

  - **하한만 있고 상한은 없습니다.** `requirements.txt`는 테스트된 lock으로 유지되고, `[project.dependencies]`은 공개 계약이 됩니다. lock의 정확한 버전을 공개하면 다른 패키지를 사용하는 모든 사용자에게 충돌이 발생할 수 있기 때문입니다. `<N+1` 상한도 없습니다. 상한을 두면 major 버전 지연 시 release gate를 실패시키는 `check-deps-fresh.sh`와 정면으로 모순됩니다. 지정된 하한 조합은 정상적으로 resolve되며, 반대 검증인 `openai==1.0.0`은 `ResolutionImpossible`로 종료됩니다. 이는 검사가 모든 것을 허용하는 것이 아니라 실제로 판별한다는 증거입니다. 또한 guard를 통해 `pyproject.toml` 버전이 CHANGELOG 버전과 달라지지 않도록 합니다. PyPI는 버전 번호의 재사용을 허용하지 않기 때문입니다.

  - **새로운 venv에서 처음부터 끝까지 검증 완료**: 약 70 Ko 크기의 wheel에는 `aipmt/*.py`, dist-info, 라이선스만 포함됩니다. `aipmt --help`은 22개 flag로 rc=0을 반환합니다. `python -m aipmt`은 « usage: \_\_main\_\_.py »가 아니라 « usage: aipmt »를 표시합니다. `pipx` 설치도 정상적으로 작동합니다. 무엇보다 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행해 굵은 글씨, 목록, inline code, 링크, URL이 보존되고 code block은 번역되지 않는 것을 확인했습니다. 마이그레이션 이전의 318개 테스트는 전후 identifier 목록이 byte 단위까지 동일한 상태로 통과합니다. 테스트가 무력화되지 않았음을 증명하는 것은 « OK »가 아니라 바로 이것입니다. 여기에 3계층 설정을 위한 테스트 12개가 추가되어 총 330개가 되었습니다.

- **1.10.0** `--use_codex` Provider(ChatGPT 구독 quota), SDK 및 model 업데이트, 여러 문단으로 구성된 news 인용 수정(2026-08-29):

  - **보안 검토 — PR에서 제시했지만 모든 경로에서 지켜지지는 않았던 두 가지 safeguard**:

    - **Codex preflight가 전체 `.env`을 binary에 전달하고 있었습니다.** `_codex_preflight`은 **`env=` 없이** `subprocess.run`을 호출했습니다. 따라서 하위 process는 `os.environ` 전체, 즉 `load_dotenv`이 불러온 `.env` 전체를 상속했습니다. 계측된 가짜 binary로 측정한 결과, 여섯 provider의 key와 `GITHUB_TOKEN` 하나를 합쳐 **일곱 개의 secret**이 preflight에 전달되었습니다. 반면 대응 경로인 `_grok_preflight`은 `env=_grok_env()`을 올바르게 전달해 **0개**였습니다. 이는 PR 내부의 불일치였습니다. 불과 몇 줄 떨어진 곳에 있는 `_strip_secret_env`은 바로 이 invariant를 유지하기 위해 존재합니다. `_codex_env_base()`을 추출해 두 경로가 공유하도록 했으며, 수정 후 측정 결과 양쪽 모두 secret이 0개였습니다.
    - **« `--deny` fail-closed » 속성은 실제 사용된 형식을 포괄하지 못했습니다.** 주석에서는 알 수 없는 prefix가 붙은 rule이 시작을 거부하게 만든다는 점을 근거로 Grok confinement 전체를 정당화했습니다. 그러나 `grok 1.0.13`에서 측정한 결과 이 validation은 **괄호 형식에만** 존재합니다. `--deny 'CeciNestPasUnOutil(*)'`은 시작을 거부하지만(« unknown tool prefix »), `--deny 'CeciNestPasUnOutil'`은 아무 경고 없이 허용됩니다. 그런데 `GROK_DENY_RULES`은 모두 괄호 없는 이름만 사용했습니다. 따라서 xAI 측에서 tool 이름을 변경하면, OS sandbox가 이미 적용되지 않는 환경에서 측정 가능한 유일한 confinement 계층이 아무 신호도 없이 제거될 수 있었습니다. 이름이 지정된 여덟 rule을 `Prefix(*)` 형식으로 변경하고, 각각 CLI가 인식하는 prefix인지 검증했습니다. catch-all인 `*`은 허용되는 유일한 형식인 literal 형태로 유지됩니다. 검증되지 않는 형식으로 되돌아가는 것을 test가 방지합니다.
    - **그 밖의 항목도 정상임을 검증했습니다**: command injection은 없습니다. 모든 곳에서 list 형식을 사용하고 `shell=True`은 전혀 사용하지 않으며, 문서 내용은 stdin 또는 `--prompt-file`을 통해 전달됩니다. 안전하지 않은 deserialization도 없습니다. `json.loads`만 type guard와 함께 사용합니다. path traversal 수정은 일곱 개 payload에서 우회가 발견되지 않았으며, `--deny '*'`은 CLI에서 실제로 적용됩니다. workdir 외부를 읽을 때 `DENY_ENFORCED`가 관찰되었습니다.
    - 앞에서 추가한 freshness 검사는 그 자체의 원칙을 우회하고 있기도 했습니다. PyPI 요청에 실패한 패키지는 아무 경고 없이 건너뛰어 gate가 통과했습니다. 이제 실제로 비교한 패키지 수를 집계하고, 검증 범위가 불완전하면 실패합니다.

  - **의존성을 최신 상태로 복구하고, 다시 지연되지 않도록 두 가지 안전망을 추가했습니다**:

    - **지연은 실제로 존재했고 장기간 지속되었습니다**: `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22**입니다. 모든 provider 호출의 TLS를 검증하는 root certificate 저장소가 무려 2년이나 뒤처져 있었습니다. 확인된 원인은 **`.github/dependabot.yml`이 존재하지 않았기 때문**입니다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하며, Dependabot은 CVE 대상 의존성에 대해서만 PR을 제안합니다. 이 때문에 `urllib3`와 `idna`은 bump하면서도 두 SDK는 major 버전 하나만큼 뒤처진 채 방치되었습니다.
    - 이전의 추론에서 우려했던 것과 달리 **두 major 버전은 충돌 없이 공존합니다**. `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**으로 마이그레이션하지만, `mistralai`와 `google-genai`는 `httpx<1`에 남습니다. 그러나 이들은 서로 다른 distribution입니다. 실제 설치로 검증한 뒤 OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI 등 **7개 provider 경로를 처음부터 끝까지 테스트**했으며, 각 출력에서 inline code와 링크가 보존되었습니다. « 두 HTTP stack을 피한다 »는 것은 선호 사항이지 blocker가 아니었으며, 측정으로 결론을 내렸습니다.
    - **`requirements.txt`은 실제 환경을 설명하지 못했습니다**. `google-auth`, `cryptography`, `opentelemetry` stack은 선언된 적이 없는데도 작업용 venv에 설치되어 있었습니다. 따라서 새로 설치한 환경에서는 테스트 환경을 재현할 수 없었습니다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`은 아무 곳에서도 import되거나 요구되지 않았지만 파일에 포함되어 있었습니다. 이는 `mistralai` 1.x의 잔재였습니다. 직접 의존성만으로 만든 venv의 완전한 dependency closure가 되도록 파일을 다시 생성했습니다. 새로운 의존성 집합에서 `pip-audit`은 알려진 vulnerability를 하나도 보고하지 않습니다.
    - **`.github/dependabot.yml`**(신규)은 pip 및 github-actions의 주간 버전 업데이트를 활성화합니다. minor와 patch는 하나의 PR로 묶습니다. patch bump마다 PR을 만들면 결국 무시되며, 소음은 업데이트의 적이기 때문입니다. **major는 각각 분리**하며, 모두 실제 호출을 통한 validation이 필요합니다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 지연이 프로젝트 verdict에 드러나게 합니다. Dependabot은 제안할 뿐 보장하지 않으며, PR이 쌓일 수도 있습니다. major 지연은 실패, minor 지연은 warning입니다. gate가 항상 빨간색이면 결국 무시되기 때문입니다. PyPI에 접근할 수 없으면 로컬에서는 명시적으로 skip하고 **CI에서는 fail-closed**로 처리합니다. 실행되지 않은 검사는 성공이 아닙니다. 양방향으로 검증했습니다. 수정 전의 정확한 상태인 `openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`를 탐지하며, minor 지연에는 warning만 표시합니다.

  - **이 PR 검토에서 도출된 수정 사항** — 다섯 review agent가 diff를 면밀히 검사했습니다. 아래 항목은 모두 수정 전에 **측정을 통해 재현**되었으며, 그중 두 항목은 같은 버전의 앞부분에서 새로 도입된 regression이었습니다.

    - **수정된 regression — `_NEWS_CITATION_REGEX`에 exponential backtracking이 있었습니다.** 여러 문단 수정 과정에서 반복 구문 안에 `(?:[ \t]*$|[ \t]+.*)`이 도입되었습니다. `[ \t]+`와 `.*` 사이에서 공백을 어느 쪽이 소비할지 모호했으며, 이 모호성이 반복할 때마다 증폭되었습니다. pattern과 일치하지 않는, 완전히 유효한 Markdown indentation인 `>   texte` line으로 측정한 결과 **14줄에서 2,589 ms**가 걸렸습니다. 수정 후에는 0.04 ms였으며, 줄이 하나 추가될 때마다 약 9배씩 증가했습니다. `--news` mode에서는 형식에 맞지 않는 긴 blockquote 하나만으로도 원인을 파악할 수 없는 상태에서 job timeout까지 번역이 멈출 수 있었습니다. 이제 반복 구문이 줄 전체를 한 번에 소비하므로(`\n^>(?![ \t]*—).*`), 각 반복을 match하는 방법이 하나뿐입니다. 실제 231개 article corpus에서 검증한 결과 capture 차이는 **0건**이었고, 동일한 423개 인용과 14개의 확장된 여러 문단 본문이 그대로 유지되었습니다.
    - **두 provider flag를 동시에 지정하면 아무 경고 없이 사용량 기반 요금이 청구되었습니다.** `--use_codex --use_mistral`이 허용되었고, `_select_provider_client`은 Mistral을 먼저 검사하며, `_resolve_provider`은 명시적 boolean을 우선합니다. 두 경로 모두 Mistral로 귀결되었습니다. 따라서 사용자는 구독 quota를 요청했지만 아무 경고 없이 사용량 기반 요금을 청구받았습니다. 이는 `--use_codex`이 방지하기 위해 존재하는 바로 그 failure mode입니다. 이제 여섯 provider flag는 하나의 `add_mutually_exclusive_group`을 거칩니다. **동작 변경 사항**: 이전에는 아무 경고 없이 허용되었던 두 provider를 함께 지정한 command line이 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 종료 gate는 probe가 crash해도 통과했습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 네 개는 return code를 전혀 확인하지 않은 채 « stdout을 capture하고, 비어 있으면 결론을 내리는 » pattern을 사용했습니다. 예외가 발생하면(파일 이름 변경, `FileNotFoundError`) stderr에 기록되고 stdout은 비어 있었으므로 검사는 « 보고할 내용 없음 »이라고 결론 내렸습니다. « `exit 0`만으로는 아무것도 증명되지 않는다 »는 함정이 이를 방지하기 위해 작성된 script 내부에서 그대로 재현된 것입니다. 이제 `probe()` helper가 return code 0과 종료 sentinel을 모두 요구하며, probe는 marker 집합이 비어 있으면 결론을 거부합니다. 빈 집합에 대한 assertion은 언제나 참이기 때문입니다. 예를 들어 위에서 exclusive group을 추가하면서 provider flag가 `*_group` 객체를 통과하게 되었고, 기존 regex인 `parser\.add_argument\(`은 더 이상 이를 match하지 못했습니다. 그 결과 **21개 중 6개 flag**가 아무 경고 없이 범위에서 빠졌는데도 gate는 통과했습니다.
    - **secret scan은 여섯 provider 중 네 개를 놓쳤습니다.** `[A-Za-z0-9]` class는 hyphen을 제외합니다. 따라서 현재 OpenAI 형식인 `sk-proj-…`과 `sk-ant-api03-…`은 두 번째 hyphen에서 끊겼으며, `AIza…`는 전혀 포함되지 않았습니다. pattern을 확장하고 `.secrets.baseline`은 scan에서 제외했습니다. 또한 `.env` guard는 index만 확인하는 `git diff --cached`를 조회했습니다. 따라서 최악의 경우인 **이미 commit된** `.env`은 절대 나타나지 않았습니다. 이제 `git ls-files`을 조회합니다.
    - **Codex의 « token warm-up »은 실제 warm-up이 아니었습니다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`에 접근하지 않으며(mtime과 크기가 변경되지 않음), 도움말에는 « Show login status »라고 나옵니다. 하지만 주석에서는 token을 « 한 번, 순차적으로 » refresh해 일회성 rotating token의 동시 refresh 위험을 제거한다고 주장했습니다. 설명된 보호 기능은 존재하지 않았습니다. 이제 주석은 code가 실제로 하는 일을 설명하며, 실질적인 대응책은 여전히 `max_jobs=4`입니다. 또한 검사는 이전에 무시하던 `CODEX_BIN`을 따릅니다. `PATH`에 `codex`이 없는 환경에서는 « 인증되지 않음 »이라는 잘못된 진단과 함께 실패했습니다.
    - **`.env`은 subshell에서 source되었습니다.** `detect_provider`가 command substitution에서 호출되므로 그 export가 상위 shell로 전달되지 않았습니다. 따라서 `.env`에 정의된 `GROK_BIN`, `GROK_HOME`, `REGEN_MODEL`은 `main()`에서 수행되는 조회에 보이지 않았고, 올바르게 설정된 환경에서도 « Grok binary를 찾을 수 없음 »이라고 결론 내렸습니다.
    - **동시 실행 수가 명시된 한도를 50% 초과했습니다.** README/CHANGELOG pair를 시작한 뒤에 guard가 배치되어 있었기 때문에 `max_jobs=2`에서 측정된 peak는 **3**이었습니다. 주간 quota가 Chat/Imagine/Voice와 공유되고 측정할 수 없는 Grok에서 script가 스스로 정한 한도를 지키지 못한 것입니다. 또한 최종 count는 표시만 하고 28과 비교하지 않았기 때문에 파일 하나가 누락되어도 발견되지 않았습니다.
    - **Grok 출력 계약: 이제 `stopReason`이 없으면 실패합니다.** code는 명시된 계약이 `end_turn`을 요구하는 상황에서 « `end_turn` **또는 필드 없음** »을 적용했습니다. 필드가 없는 payload나 CLI 업데이트로 필드 이름이 변경된 payload는 guard를 아무 경고 없이 no-op으로 만들었습니다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류하지 않습니다. 소진된 것은 turn budget이며, 다시 시도하면 90초를 기다린 뒤 같은 결과가 반복되기 때문입니다. `quota`도 rate limit marker에서 제외됩니다. `_codex_is_rate_limited`의 docstring이 이미 설명했지만 Grok에는 적용하지 않았던 바로 그 이유 때문입니다.
    - **Gemini cascade는 model별로 memoization됩니다.** 기본 model이 `minimal`을 거부하는데도 segment마다 다시 여기서 시작했습니다. 따라서 nominal path는 segment마다 400 응답을 한 차례 왕복하고 같은 warning을 다시 출력했습니다. warning이 수백 번 반복되면 더 이상 아무도 읽지 않으며, 그렇게 warning은 문제를 가리는 장막이 됩니다.
    - **기타 사항**: CI의 거부 message가 Codex 전용으로 hard-code되어 있어 `--use_grok_cli` 사용자를 `XAI_API_KEY`이 아닌 `OPENAI_API_KEY`으로 안내했습니다. `provider.capitalize()`은 « Grok_cli »와 « Openai »를 표시했습니다. 하위 process 기반부의 주석은 « shim »을 두 CLI 모두에 일반화했지만 Grok binary는 native ELF입니다. 올바른 근거는 « 자체 하위 process를 생성하는 agent »입니다. `subprocess`에 대한 SAST finding 12개는 `# nosec` / `# nosemgrep`로 근거와 함께 표시되었습니다. `shell=True`이 없는 list 형식이므로 injection은 불가능하고, 문서 내용은 절대 argv를 통해 전달되지 않습니다.
    - **이제 agent 하위 process에 secret이 하나도 전달되지 않습니다.** 이름 기반 deny-list는 **요금 청구** invariant만 보호했습니다. 즉 Codex에는 `OPENAI_API_KEY`을, Grok에는 `XAI_API_KEY`을 전달하지 않았습니다. 측정 결과 **그 밖의 secret 일곱 개**가 여전히 각 하위 process에 전달되었습니다. Anthropic, Mistral, Google, Gemini key와 다른 CLI의 key, 그리고 secret은 아니지만 traffic 경로를 바꾸는 `OPENAI_BASE_URL`이었습니다. 그런데 이 두 CLI는 **agent**이며, Grok agent는 많은 Linux 환경에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 filtering은 이름 기반 목록이 아니라 **이름 pattern**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)으로 수행합니다. 따라서 이 code가 알지 못하더라도 사용자가 `.env`에 추가한 변수까지 포괄합니다. CLI에는 이 중 어떤 것도 필요하지 않습니다. 인증 정보는 환경 변수가 아니라 `~/.codex`과 `~/.grok`에 저장됩니다. 강화된 환경에서 두 provider 각각을 사용해 **실제 번역이 성공적으로 완료되는 것**으로 검증했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`에 21개 테스트를 추가해 provider flag의 배타성, `stopReason` 계약, news regex의 선형성, CI 거부 message, Gemini memoization, 하위 process 환경에 어떠한 secret도 존재하지 않는다는 점을 고정했습니다. 마지막 assertion은 **generic**합니다. 어떤 목록에도 이름이 없는 key에도 실패합니다. 반면 기존의 제거 테스트는 자체 constant를 그대로 반영한 형태라서 자체 loop의 고장 외에는 아무것도 탐지할 수 없었습니다. 전체 테스트 모음은 **311개 테스트**입니다.
  - **새로운 Grok provider 2개**: `--use_grok`(xAI API, `XAI_API_KEY` 키, 사용량 기반 과금)과 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독 할당량에서 차감 — `--use_codex`과 동일한 원리).
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`은 그대로 재사용하며, `base_url`만 변경됩니다. 단 하나의 조정만 필요했고 이는 모두에게 도움이 됩니다. 이제 `finish_reason`은 OpenAI가 `stop`을 내보내는 곳에서 xAI가 내보내는 형식인 `end_turn`도 허용합니다. 모델: `grok-4.6`(품질)과 `grok-4.3`(경제성). 참고로 Grok의 경제형 모델도 저장소에서 가장 비쌉니다. 백만 개당 $1.25/$2.50로, `mistral-small-latest`의 $0.15/$0.60과 대조됩니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택하는 것입니다.
    - **CLI 모드**: Codex를 본떠 구현했지만 실제 환경이 요구하는 네 가지 차이점이 있습니다. prompt는 파일로 전달되고(`--prompt-file`, CLI는 stdin을 읽지 않으며 argv의 segment는 `ps`에 노출됨), 출력은 stdout의 단일 JSON 객체이고(JSONL도 `-o` 파일도 아님), 구독에서는 `grok-4.6`와 `grok-4.5`만 제공되며, sandbox는 적용할 수 없습니다(아래 참조). subprocess 실행은 이미 테스트된 기존 Codex provider의 나머지 부분을 건드리지 않고 `_codex_run_process`에서 Codex와 공통화했습니다.
    - **`exit 0`은 아무것도 증명하지 않음, 실측 완료**: 인증되지 않은 상태에서 CLI는 반환 코드 **0**과 함께 **stdout**에 `{"type":"error","message":"Not signed in."}`을 씁니다. 거부되거나 turn 한도를 초과해도 똑같이 동작합니다. 따라서 출력 계약은 반환 코드 0, 오류 payload 부재, `stopReason == end_turn`, 비어 있지 않은 text라는 네 가지 조건을 동시에 요구합니다. preflight도 같은 논리를 따릅니다. `grok models`은 연결이 끊긴 상태에서도 0으로 종료되며, stdout에 « 인증되지 않음 »이 있을 때만 이를 판별할 수 있습니다.
    - **격리: 의도적으로 채택하고 문서화한 비대칭성.** Codex는 `--sandbox read-only`에서 실행되지만 Grok의 sandbox는 최신 Linux 환경 다수에서 적용할 수 없습니다. 이는 `sudo` 없이는 우회할 수 없는 서로 독립적인 두 시스템 원인 때문입니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하고(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`가 `0700` 상태일 때 container runtime socket deny-list가 실패합니다(resolver는 `ErrorKind::NotFound`만 복구하며 EACCES는 치명적 오류가 됨). 핵심 함정은 적용할 수 없는 **내장** profile이 **아무 알림 없이 격리되지 않은 상태로 실행된다**는 점입니다. 따라서 script는 기본적으로 어떤 profile도 요청하지 않고 절대 조용히 fallback하지 않으며 stderr에 경고합니다. 보호는 catch-all `*`을 포함한 CLI의 `--deny` 규칙에 의존합니다. 이는 실측된 유일한 _fail-closed_ 계층입니다(알 수 없는 접두사의 규칙 하나만 있어도 실행을 거부함). `GROK_TRANSLATE_SANDBOX=read-only`으로 이를 필수화할 수 있으며, 이 경우 시스템이 해당 설정을 준수할 수 없으면 실행이 실패합니다.
    - **안전장치**: subprocess 환경에서 `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`을 제거합니다(키 하나만 있어도 사용량 기반 과금으로 전환되며, 상속된 `GROK_SANDBOX`은 적용할 수 없는 profile을 오해의 소지가 있는 메시지와 함께 강제함). MCP/hooks/skills/agents 전환 장치를 비활성화하고, `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI에서의 실행 거부, process group을 종료하는 timeout, rate limit 발생 시 back-off를 적용합니다. `--max-turns`은 1이 아니라 6으로 설정합니다. counter는 tool turn 후에 증가하므로 1로 설정하면 출력이 잘리기 때문입니다.
    - **할당량**: Grok pool은 주 단위이며 **Chat, Imagine, Voice와 공유**되고, 이를 표시하는 명령은 없습니다. 반면 Codex는 `account/rateLimits/read`를 통해 사용량을 산정할 수 있습니다. 따라서 `regen_translations.sh`은 동시 실행을 2개로 제한하고 이를 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`(테스트 24개). 전체 suite는 **테스트 290개**입니다.
  - **수정된 버그 — 여러 문단으로 된 영어 인용문이 일부만 보호되던 문제(`--news` 모드)**: `_NEWS_CITATION_REGEX`은 인용문 본문으로 **연속된** `>` 줄만 허용했습니다. 인용문이 빈 `>` 줄로 구분된 여러 문단에 걸쳐 있으면 마지막 문단만 포착되어 placeholder로 대체되고, 앞선 문단들은 LLM으로 전달되어 번역되었습니다. 이는 `--news`이 보장하기 위해 존재하는 목적과 정확히 반대되는 동작입니다. 이제 반복 구문은 내부의 빈 `>` 줄을 허용하고 비탐욕적으로 동작하여, 처음 만나는 빈 줄이 아니라 기울임꼴 줄 앞의 빈 `>` 줄에서 멈춥니다.
    - **실측된 규모**: 실제 기사 198개로 구성된 corpus에서 인용문 419개 중 11개가 해당했습니다. 회귀는 없습니다. 새 regex는 정확히 같은 수의 인용문을 포착하며 여러 문단으로 된 본문만 확장됩니다(동일한 본문 408개, 확장된 본문 11개). 또한 `> — …` 출처 표기 줄은 유지된 lookahead 덕분에 여전히 본문에 흡수될 수 없습니다.
    - **end-to-end 검증**: 일본어와 아랍어로 번역한 69KB 기사에서 이전에는 일본어로 `> GLM-5.3がオープンウェイト化。`이 되고 아랍어에서도 마찬가지로 번역되던 인용문의 첫 문단이 이제 `> GLM-5.3 is now open-weight.`로 유지됩니다. 영어 인용문 줄 수는 원문과 동일한 10줄로, 기존 9줄에서 회복되었습니다.
    - 참고: 이 결함은 인용문의 존재 여부만 확인하고 완전성은 검사하지 않는 downstream validator에서는 감지되지 않았습니다.
  - **기본 provider에서 실측된 비용 절감**: `_openai_extra_kwargs`은 모델 이름이 `gpt-5`로 시작하기만 하면 `--eco`에서도 `reasoning_effort="medium"`을 전송했습니다. 열 단어 문장을 번역하는 `gpt-5.4-mini` 실측 결과: `medium` → reasoning token 45개와 출력 token 65개, `none` → 0개와 14개였습니다. 번역에는 reasoning이 아무런 이점을 주지 않지만 모든 파일의 모든 segment에서 비용이 발생하고 있었습니다. 기본값은 `--eco`에서는 `none`이 되고, 그 외에는 `medium`로 유지됩니다. CLI에서 명시적으로 전달한 값은 계속 우선합니다. 이제 `--reasoning_effort`은 `low`/`medium`/`high`뿐 아니라 `none`과 `xhigh`도 허용합니다(모든 모델이 이 값들을 전부 허용하는 것은 아닙니다. 예를 들어 `minimal`은 `gpt-5.4-mini`에서 거부되며, 기존의 parameter 없는 retry가 이 경우를 처리합니다).
  - **SDK 업데이트 및 Gemini 마이그레이션**: `google-generativeai`(2025-11-30 지원 종료, 저장소 보관 처리)을 통합 SDK **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)`에 이어 `client.models.generate_content(model=, contents=, config=)`을 사용하며, system prompt는 segment에 이어 붙이는 대신 `system_instruction`로 전달합니다. `mistralai`는 **2.9.4**로 올라갑니다(import는 `from mistralai.client import Mistral`이 되며, 이전 방식은 `ImportError`을 발생시킴을 wheel에서 확인함). `anthropic`은 **0.125.0**, `openai`는 **2.54.0**으로 올라갑니다. venv에 두 HTTP stack을 공존시키지 않기 위해 `httpx2` 전환 전의 마지막 버전을 사용합니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5의 제한도 해제했습니다.
  - **문서가 아닌 실제 테스트에서 포착된 두 가지 회귀**:
    - `anthropic` ≥ 1.0은 `max_tokens`가 10분 넘게 걸릴 것으로 예상되는 non-streaming 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 안전장치는 0.34.2에는 없었으며 `max_tokens=32768`을 사용하는 모든 Claude 호출을 망가뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 전체 응답만 사용하는 호출을 streaming으로 전환하지 않아도 됩니다.
    - `thinking_level="minimal"`은 Gemini catalog 일부에서만 허용됩니다. `gemini-3.1-flash-lite`은 지원하지만 `gemini-3.7-flash`과 `gemini-3.1-pro-preview`는 400 오류로 거부합니다. 이에 따라 `_gemini_generate_with_fallback`에서 `minimal` → `low` → thinking_config 없음으로 이어지는 cascade를 적용했습니다. 이는 기존 OpenAI fallback을 본뜬 것으로, 최적화 parameter 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델 갱신**, 각각 실제 호출로 검증 완료: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%), Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜 없는 canonical ID), Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(stable version이며 `3.5-flash-lite`보다 저렴함). Mistral은 변경하지 않았으며, `mistral-large-latest`이 네 모델 중 여전히 가장 뛰어난 가격 대비 품질을 제공합니다. 참고로 `gemini-3.1-pro-preview`보다 최신인 Gemini Pro 계열 모델은 존재하지 않습니다. 2026년 5월 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 계열은 전부 Flash 전용입니다.
  - **Gemini 전환 전 실측한 A/B 테스트**: `README.md`을 `gemini-3.1-pro-preview`와 `gemini-3.7-flash`으로 각각 일본어로 번역했습니다. 구조는 완전히 동일했고(목록 21개, code block 18개, HTML link 13개, image 13개, 모든 URL 보존), 소요 시간은 **48초 대비 8초**였습니다. 이 두 모델을 번역이나 비라틴 문자 script 측면에서 비교한 공개 benchmark가 없으므로, 이 측정이 없었다면 전환은 단순한 추정에 근거했을 것입니다.
  - **Claude 응답 block 필터링**: `_call_claude`은 type을 필터링하지 않고 `block.text for block in response.content`을 수행했습니다. 적응형 reasoning 모델(Sonnet 5 이상)은 `thinking` block을 중간에 삽입하는데, 이 block은 `.text`이 아니라 `.thinking`을 노출합니다. 따라서 번역은 첫 segment에서 불투명한 `AttributeError` 때문에 실패했을 것입니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result` block을 제외합니다(텍스트를 포함하는 알 수 없는 type을 허용하기 위해 negative list 사용). text block이 하나도 없는 응답은 명시적인 오류를 발생시킵니다. `thinking={"type": "disabled"}`은 모든 호출에 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 폐기일이 지난 모델을 삭제했습니다(`magistral-*` 계열은 2026-07-31 폐기, `gemini-2.0-*`은 2026-06-01, `gemini-3-pro-preview`은 2026-03-09, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`). 한도 수정: Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1,000,000 → **1,048,576**(실제 input 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 계열 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 계열을 추가했습니다. 참고로 이 한도는 여전히 참고용이며, `translate()`이 segmentation을 `min(16000, limite)`로 제한합니다.
  - **Provider `--use_codex`**: 사용량에 따라 과금되는 API를 호출하는 대신 공식 Codex CLI(`codex exec`)를 비대화형 모드로 구동하는 다섯 번째 provider입니다. 번역 사용량은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. OpenAI가 이 용도로 문서화한 유일한 방법입니다. 요금제별 이용 가능 기능 표에는 « Codex SDK, `codex exec`, and scriptable workflows »가 Plus/Pro/Business/Enterprise에서 이용 가능한 것으로 명시되어 있으며, `~/.codex/auth.json`의 token은 API Platform 호출을 인증하지 않습니다. 또한 이 스크립트는 해당 token을 절대 읽지 않으며, 인증과 갱신은 계속 CLI에서 관리합니다.
  - **npm뿐 아니라 pip로도 설치할 수 있는 Codex 바이너리**: `_resolve_codex_binary()`은 `CODEX_BIN`, `PATH`, OpenAI가 배포하는 공식 Python package **`openai-codex-cli-bin`** 순으로 바이너리를 찾습니다. 이 package는 `openai-codex` SDK의 dependency입니다. 따라서 Python 프로젝트에서 `--use_codex`을 사용하기 위해 더 이상 npm 전역 설치가 필요하지 않습니다. 이 package는 `requirements.txt`에 추가되지 않습니다. 바이너리 크기가 약 250MB이므로 선택적 provider를 위해 모든 사용자에게 이를 설치하도록 강제할 수 있기 때문입니다. 전체 과정을 검증했습니다. `codex`이 `PATH`에 없는 상태에서도 package에 포함된 바이너리를 찾아 6초 만에 전체 번역을 완료합니다.
  - **« 구독 모드 » 보장**: 하위 process의 환경에서 `OPENAI_API_KEY`과 `CODEX_API_KEY`을 제거합니다. 이 보호 장치가 없으면 `.env`에 있는 key로 인해 아무런 표시 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 이는 바로 이 provider가 방지하려는 상황입니다.
  - **테스트로 차단한 CLI 함정**:
    - prompt를 인수로 전달해도 `codex exec`은 stdin을 **읽습니다**. stdin을 닫지 않으면 명령이 모델을 한 번도 호출하지 않은 채 timeout까지 대기합니다. 재현 결과는 180초 후 exit 124, 0byte였습니다. 따라서 `communicate(input=...)`은 필수입니다.
    - npm으로 설치한 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 이 바이너리는 Python process의 **손자 process**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 계속 할당량을 소비할 수 있습니다. 따라서 `Popen(start_new_session=True)`과 `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`을 출력하고도 종료 코드 0을 반환할 수 있습니다. 따라서 반환 코드뿐 아니라 JSONL 출력(`--json`)도 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 segment를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **rate limit 발생 시 back-off**: CLI에는 내부 retry가 구현되어 있지 않습니다(`max_retries = 0`). 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. « quota »라는 단어는 복구 가능한 429와 영구적인 `insufficient_quota` 모두에 나타나기 때문입니다.
  - **CI 보호 장치**: `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 `--use_codex`을 거부합니다. 구독 인증은 공유 runner용이 아니며, OpenAI도 공개 repository에서 이 workflow를 사용하지 말 것을 명시적으로 권고합니다.
  - **모델**: `gpt-5.6-sol`(품질) 및 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 계열은 CLI와 API Platform에서 공통으로 사용되지만, ChatGPT 계정이 모든 모델을 이용할 수 있는 것은 아닙니다. allowlist는 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 지정하면 경고가 발생합니다. Plus 요금제에서 Luna는 5시간 단위 기간당 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개를 제공합니다. 따라서 모든 batch 처리에는 `--eco` 모드를 권장합니다.
  - **수정된 bug — 전체 작업이 성공했는데도 `regen_translations.sh`이 오류로 종료됨**: `trap ... EXIT`은 `main()`의 `local` 변수인 `failed_log`을 참조했지만, trap이 실행될 때는 이 변수가 더 이상 존재하지 않았습니다. `set -u`에서는 이로 인해 `failed_log: unbound variable`이 발생했으며, 28개 번역이 모두 올바른데도 스크립트가 종료 코드 1로 끝났습니다. 이 문제는 가장 비용이 많이 드는 재생성 단계 직후에 `release.sh --auto`(`set -e`)을 중단시킬 수 있었습니다. 변수를 전역으로 바꾸고 trap이 변수의 존재 여부를 검사하도록 수정했습니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 최종 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: provider의 기본값보다 우선하여 특정 모델을 강제하는 `regen_translations.sh`의 새로운 환경 변수입니다. 예를 들어 처리량 중심 모델인 `--eco` 대신 구독 할당량의 고급 모델로 다시 생성하려면 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 사용할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때 사용할 수 있는 `REGEN_PROVIDER=codex`입니다. 사용자가 모르는 사이에 구독 할당량을 소비하지 않도록 자동 감지하지 않습니다. 병렬 처리를 시작하기 전에 token을 순차적으로 한 번 갱신합니다. Codex refresh는 순환식 일회용이므로 동시 실행 job이 `codex login` session을 무효화할 수 있기 때문입니다. 동시 실행 수는 4로 낮췄습니다.
  - **관련 refactor**: 전체 처리 과정에 네 번째 boolean을 전달하는 대신 provider 이름을 반환하는 `_resolve_provider()`을 사용하여 `_dispatch_provider_call`의 parameter 수를 8개에서 6개로 줄였습니다. 최소한의 `Namespace`으로 `translate(..., use_mistral=True)`을 호출하는 테스트를 유지하기 위해 명시적인 boolean은 계속 `args`보다 우선합니다.
  - **테스트**: argv, 정리된 환경, 서문 금지 계약, silent failure, timeout/killpg, back-off, preflight, provider 해석, Gemini 추론 단계적 전환, Claude block 필터링, 여러 문단으로 된 news 인용을 다루는 새 파일 `tests/test_codex_provider.py`(48개 테스트)을 추가했습니다. 전체 test suite는 290개 테스트입니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 기준 번역과 구조가 완전히 동일했습니다. code block 14개, 제목 24개, table 행 25개, HTML link 13개, image 13개, URL 19개가 일치했고, code block은 문자 단위까지 동일했으며 placeholder 잔여물은 하나도 없었습니다. `--news` 모드에서 69KB 분량의 보도 기사로 검증한 결과, `gpt-5.6-luna`과 `gpt-5.6-sol` 출력 모두 en/ja/ar에 대해 후속 애플리케이션 validator를 통과했습니다. `account/rateLimits/read`로 측정한 사용량은 `--eco` 모드에서 계수기의 반올림 기준보다 낮은 수준, 즉 5시간 기간의 0%에 머물렀습니다.

- **1.9.2** 중첩 괄호 또는 프랑스어 접두사가 포함된 news 출처 URL 추출 수정(2026-05-11):

  - **수정된 bug**: `_protect_news_quotes`의 출처 URL 추출은 정규식 `re.search(r"\((.+?)\)", attribution)`을 사용했습니다. 이는 괄호 사이를 lazy capture합니다. `(relayé par [@user sur X](https://x.com/.../123))` 같은 출처 표기에서는 괄호가 중첩되어 있습니다. 즉, 바깥쪽 `(`과 markdown link의 `]()`이 함께 존재합니다. 이 경우 첫 번째 `)`에서 capture가 끝나 프랑스어 접두사까지 포함된 잘린 문자열 `relayé par [@user sur X](https://x.com/.../123`이 생성되며, 마지막 `)`은 누락됩니다. 그 결과 `_validate_news_post`이 번역된 출력에서 이 문자열을 찾다가 항상 실패했습니다. 원인은 두 가지로, `)`이 잘렸고 "relayé par"가 `relayed by`/`weitergeleitet von`/... 등으로 번역되었기 때문입니다. low → medium → high → gpt-5.5의 전체 단계적 전환으로도 통과할 수 없었습니다.
  - **수정**: 정규식을 `re.search(r"\]\(([^)]+)\)", attribution)`으로 변경했습니다. markdown link의 `](url)`을 구체적으로 대상으로 삼아 프랑스어 접두사나 잘림 없이 **순수 URL만** capture하며, 번역 중에는 `#URL{N}#` placeholder가 이 불변성을 보존합니다. 다음 두 문제 pattern 모두에 견고합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥쪽 괄호가 없는 프랑스어 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` class에 2개를 새로 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B bug를 정확히 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`을 사용한 변형)
  - **누락된 coverage**: `check-editorial-coverage.py`은 편집 문법을 검증하지만 translator가 번역할 수 있는지는 검증하지 않습니다. 가능한 개선 사항은 게시 **전**에 위험한 pattern을 감지할 수 있도록 dry-run에서 출처 추출을 시뮬레이션하는 검사입니다. 이는 v1.9.2 범위에는 포함되지 않습니다.

- **1.9.1** 번역 marker 메모의 CTA label i18n 수정(2026-05-10):

  - **수정된 bug**: 번역된 파일 상단의 marker banner에 있는 CTA link의 `[Voir le projet sur GitHub ↗]` label이 `target_lang`을 따르지 않고 모든 대상 언어에서 **프랑스어로** 남았습니다. 이 label은 URL과 repository slug를 보존하기 위해 Python 측에서 조합되므로 LLM에는 절대 전달되지 않으며, 번역 단계에서도 이를 수정할 수 없었습니다. v1.9에서 `marker` 형식을 추가한 이후 발생한 silent regression입니다.
  - **수정**: 15개 언어를 각각 현지화된 label에 mapping하는 새 상수 `_VIEW_PROJECT_LABELS`을 추가했습니다. 이제 `_translation_note_invariants(target_lang)`과 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달합니다. 언어를 알 수 없으면 `fr`으로 fallback합니다. 이는 KeyError를 방지하기 위한 안전장치입니다.
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 조정했습니다. target_lang `ja`에 대해 일본어 label을 기대하도록 변경했습니다. 2개 테스트를 새로 추가했습니다. 하나는 7개 언어를 parameter화하여 Latin 문자, 표의 문자, abjad를 포괄하는 `test_source_link_label_localized_per_target_lang`이고, 다른 하나는 `test_source_link_label_falls_back_to_french_for_unknown_target`입니다. `test_translation_note_position.py`의 총 테스트 수는 38개에서 40개로 늘었습니다.
  - **하위 호환성**: 기본값을 포함한 signature `target_lang="fr"`을 사용하므로, `args.target_lang` 없이 호출하는 외부 programmatic caller도 수정 없이 계속 작동합니다.
- **1.9** silent-failure 수정 + 완전한 품질 도구화 + 다중 위치 번역 주석 (2026-05-07):
  - **다중 위치 번역 주석 + "embed card" 마커 형식**:
    - 새로운 CLI 옵션 추가(기본값 변경 없음 → **비호환 변경 없음**):
      - `--note_position {top,bottom,both}`(기본값: `bottom`): 번역된 파일의 상단, 하단 또는 양쪽 모두에 주석을 배치합니다.
      - `--note_format {legacy,marker}`(기본값: `legacy`):
        - `legacy`는 v1.8의 동작을 엄격하게 재현합니다(굵은 문단 `**…**`). **byte-for-byte**로 동일합니다.
        - `marker`는 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에 **3개 문단으로 구성된 blockquote**를 출력하여 "GitHub repo embed card" 형태로 렌더링합니다. 여기에는 인라인 코드로 표시된 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM이 번역한 설명, 표시되는 화살표가 포함된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 들어갑니다. 빌드 시 remark 플러그인으로 활용할 수 있습니다(jls42.org 블로그의 `remark-translation-banner` 플러그인 참조).
    - **LLM에 절대 전송되지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문장을 번역한 후 Python 측에서 조합됩니다. LLM에는 `ai-powered-markdown-translator` slug나 `https://github.com/jls42/...`이 절대 노출되지 않으므로 renderer, 대소문자 또는 scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter를 닫는 `---` 블록 **뒤에** 주석이 삽입됩니다(Astro Content Collections / gray-matter 안전성 보장). `_split_frontmatter` helper는 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter가 있으면 **`RuntimeError`을 발생시키며**, 잘못된 위치에 주석이 삽입된 파일을 쓰는 대신 해당 파일을 `failed_files`에 기록합니다.
    - **모델 whitelist sanitizer**: `_sanitize_model`는 `[A-Za-z0-9._:/-]`에 속하지 않는 모든 문자를 `_`로 바꾸며, 결과가 비어 있으면 `unknown`를 사용합니다. Astro remark 플러그인 측 validator와 동작을 일치시키고 마커 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 refactor**: `_append_translation_note`(단일 모놀리식 함수) → 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). builder와 composer를 분리했습니다(builder는 구분자 없는 순수 블록을 반환하고 composer는 위치에 따라 `\n\n`을 적용). 프로덕션 코드와 소스 helper가 동일한 3문단 assembler를 공유합니다.
    - **`_quote_lines` blank-preserving 처리**: 각 줄 앞에 `> `을 붙이고 빈 줄은 `>`만 있는 줄로 변환합니다. 이를 통해 mdast가 blockquote를 줄바꿈이 포함된 하나의 문단이 아니라 서로 구분된 3개 문단(제목 / 설명 / 링크)으로 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 문단 수에 따라 처리합니다(3개 = 완전한 card 형식, 2개 = 문장 + 링크, 1개 = fallback). Markdown 링크 `](`가 감지된 경우 1문단 fallback은 더 이상 **`**...**`으로 감싸지 않습니다**(링크 주위의 `<strong>`은 렌더링이 불안정함).
    - **상위 호환성**: `_compose_with_notes` 측에서 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")`를 사용합니다. 이 속성이 없는 Namespace도(기존 테스트와 외부 프로그래밍 방식 호출) 수정 없이 계속 작동합니다.
  - **긴 번역의 silent-failure 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증을 적용했습니다. 결정론적 계층(출처에서 verbatim으로 발견되는 발췌문) + 확률론적 계층(`langdetect`)으로 구성됩니다.
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에서 `RuntimeError`을 발생시킵니다.
    - Claude의 `max_tokens`: `4096` → `32768`(16k 세그먼트의 잠재적 truncation을 방지하고 FR→JA/ZH/KO/AR/HI cross-script 변환 여유를 확보).
    - heading-aware 세분화: 세그먼트 후반부의 H2/H3를 우선하여 각 세그먼트가 의미상 완전한 섹션으로 시작하게 합니다.
    - 오류를 0이 아닌 exit code까지 전파: `translate_markdown_file`은 타입이 지정된 상태 `success` / `failure` / `skipped`를 반환하고, 하나 이상의 파일이 실패하면(single-file 및 batch) `main()`가 `sys.exit(1)`을 반환합니다.
    - 모든 provider에 empty-content guard 적용, 원문/출력 sanity ratio 적용(원문 ≥ 500자이고 출력이 5% 미만이면 거부), 코드 placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 처리 후 정규화(구분자나 링크가 heading에 붙는 현상 수정), `BadRequestError`은 `reasoning_effort` 없이 재시도합니다.
    - `langdetect==1.0.9` 의존성을 추가했습니다.
  - **pre-commit 품질 도구**("완전한 EurekAI 유형", 14개 hook):
    - Pre-commit: ruff(lint+format), shellcheck, prettier(md/yaml/json), detect-secrets(4개의 API key 보호), Lizard(CCN ≤ 12), pre-commit-hooks v5(공백, EOF, 대용량 파일, shebang 등).
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/).
    - `./venv/bin/python`을 사용하는 로컬 wrapper를 `scripts/`에 추가했습니다.
    - `scripts/audit_verdict.py`: 11개의 unittest가 포함된 pip-audit JSON parser이며, jls42-astro parser를 Python으로 이식한 버전입니다.
    - 초기 ruff 위반 7건을 수정했습니다: B904(raise from) ×2, B007(unused dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any()).
    - Lizard는 `translate.py`을 일시적으로 제외합니다(CCN 21~47인 함수 4개, refactor 예정). scripts/에는 엄격한 gate를 적용합니다.
  - **SonarCloud + 포괄적인 coverage**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): push와 pull-request마다 분석하며 `coverage.xml`을 통해 coverage를 측정합니다.
    - README 상단에 SonarCloud badge 11개를 추가했습니다(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code).
    - `tests/test_silent_failure.py`(`unittest` stdlib): silent-failure 오류 체인의 여섯 단계를 다룹니다.
    - `tests/test_orchestration.py`(+79개 테스트): `translate.py`의 orchestration 계층을 다룹니다(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return 분기).
    - `scripts/tests/test_audit_verdict.py`: `main()`(stdin/stdout)과 `if __name__ == "__main__"` 블록을 subprocess를 통해 다룹니다.
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%).
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 조합(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 여러 줄 prefix 처리, byte-for-byte 상위 호환성(golden literal), sanitizer, frontmatter 분리(닫히지 않은 fence에서의 예외 발생 포함), 3문단 형식, 2문단 fallback, 1문단 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않음을 assert하는 핵심 safeguard `TestLLMPayloadExcludesInvariants`을 다룹니다. **190개 테스트 통과**, regression 0건.
  - 문서화: badge를 포함한 `README.md`(FR + 14개 번역), `CLAUDE.md`(pre-commit workflow + 상세한 CI watch), 28개 번역 재생성.
- **1.8** `--news` 모드 + 2026년 모델 bump(2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 품질 모델: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형 모델: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질 모델: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token 제한을 추가했습니다.
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder를 통한 영문 인용문 보호, `LANG_FLAGS` mapping(15개 언어), 대상 언어별 flag 관리.
  - 복원 전에 news placeholder를 검증합니다(regression: LLM이 placeholder를 삭제하면 인용문이 없는 출력이 조용히 생성되던 문제).
  - `regen_translations.sh` script를 이식 가능하게 만들었습니다(절대 경로 사용, pwd 의존성 제거).
  - README/CHANGELOG의 language bar에 프랑스어 링크를 추가하고 28개 번역을 재생성했습니다.
- **1.7** 새로운 기능:
  - 번역할 때 원래 파일명을 유지하는 `--keep_filename` 옵션.
  - API key를 자동으로 불러오는 `.env` 파일 지원.
  - **인라인 코드 보존**: 이제 번역 중에 backtick(`` `...` ``)을 보호합니다.
  - system prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선.
    - template 변수 `{variable}` 보호.
    - 요청하지 않은 번역자 주석 금지.
  - 364개 파일에서 성공적으로 테스트했습니다(jls42.org 블로그 migration).
- **1.6** 새로운 기능:
  - 번역을 위한 Google Gemini API 지원(`--use_gemini`).
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형).
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형).
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형).
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`).
  - 디렉터리를 탐색하지 않고 단일 파일을 번역하는 기능(`--file`).
  - 간소화된 새로운 파일명 pattern: `{base}-{lang}.md`.
  - 모델 이름을 포함한 기존 형식을 유지하는 `--include_model` 옵션.
  - 목록에 없는 모델에 기본 token 제한(128k)을 적용하여 지원.
  - README를 14개 언어로 번역했습니다.
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트했습니다.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`로 업데이트했습니다.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY`을 추가하고 `DEFAULT_MODEL_CLAUDE`을 `"claude-3-5-sonnet-20240620"`로 업데이트했습니다.
  - **번역 prompt 최적화:**
    - 직접 번역과 번역 주석용 prompt를 더 명확하고 효율적으로 개선했으며, metadata와 특정 formatting 요소를 보존하는 방법에 관한 상세 지침을 포함했습니다.
  - **코드 refactor:**
    - Mistral AI client 초기화에서 `MistralClient`을 `Mistral` class로 교체했습니다.
    - 가독성과 유지보수성을 높이도록 import를 재구성했습니다.
    - 번역 시 원래 formatting을 보존하도록 텍스트 세분화와 코드 블록 처리를 개선했습니다.
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 바꿨습니다(예: `f"{base}-{args.target_lang}-{args.model}.md"`). 이에 따라 번역 파일을 더 쉽게 정리하고 찾을 수 있습니다.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 코드를 정리했습니다.
    - script의 구조와 가독성을 높이기 위한 소규모 조정을 적용했습니다.
- **1.4** 새로운 기능:
  - 번역을 위한 Anthropic Claude API 지원.
  - 명확성과 효율성을 높이도록 prompt를 최적화했습니다.
  - 코드 유지보수성을 높이기 위한 소규모 조정을 적용했습니다.
- **1.3** 개선 사항 및 새로운 기능:
  - 코드 블록 처리 개선.
  - 출력 파일 관리 개선.
  - 기존 파일 감지 개선.
  - 번역을 강제하는 `--force` 옵션.
  - 출력 파일명에서 모델과 언어의 순서를 변경했습니다.
- **1.2** changelog 수정.
- **1.1** Mistral AI API 지원 추가.
- **1.0** 초기 버전 - OpenAI API 지원.

**gpt-5.6-sol로 프랑스어에서 한국어로 번역된 기사.**
