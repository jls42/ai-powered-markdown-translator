### 변경 기록

🌍 [프랑스어](CHANGELOG.md) | [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.13.1** 종속성 최신성: 지연을 더는 못 보고 지나칠 수 있는 경고로 두지 않음(2026-09-09):

  - **집계되지 않는 경고는 놓치기 마련이다.** `check-deps-fresh.sh`에서는 며칠 전부터 `openai`과 `anthropic`가 뒤처졌다고 알렸지만, gate의 요약 줄은 실패만 집계했다. 따라서 몇 줄 위에 지연이 표시되어 있어도 “준비 완료: 검사 N개 통과”라고 알렸다. 마지막 줄을 읽는 사람은, 누구나 그렇게 하듯이, 이를 알 수 없었다. 이제 판정에 경고 수가 표시되며, 전용 카운터가 경고를 발생하는 즉시 출력하는 대신 집계한다.
  - **지연된 버전에는 릴리스 노트가 함께 표시된다.** 버전 번호만으로는 무엇이 바뀌었는지 알 수 없으며, 적절한 파일을 직접 찾아야 하는 번거로움이야말로 이 단계를 건너뛰게 하는 원인이다. 이제 검사는 지연된 각 패키지의 CHANGELOG 주소를 주 버전과 부 버전 모두에 대해 이유와 함께 표시한다. SDK의 부 버전 업데이트에서도 이미 이 프로젝트가 의존하는 항목이 변경된 적이 있기 때문이다.
  - **`openai` 3.8.0 → 3.10.0 및 `anthropic` 1.3.0 → 1.4.0, 고정하기 전에 릴리스 노트를 검토했다.** OpenAI 쪽에서는 해당 버전 범위에 동작 변경이 하나뿐이었다. 부동소수점 범위를 넘는 숫자형 `Retry-After` 헤더가 더는 짧은 backoff로 대체되지 않고, 재시도 없이 원래 오류를 반환한다. 이 프로젝트가 의존하는 부분에는 변경이 없었다. 추가 필드에 대한 모델의 허용 여부가 그대로임을 두 태그의 코드에서 확인했으므로, OpenRouter가 선택 항목에 추가하는 `native_finish_reason`과 `error`도 계속 통과한다. Anthropic 쪽에서는 SDK가 `httpx2`을 기대하는 곳에 `httpx` 패키지의 객체가 전달되면 명시적인 `TypeError`로 거부하는 새로운 보호 로직이 추가되었다. 이 프로젝트는 부동소수점 값만 전달함을 확인했다. 10분을 넘는 비스트리밍 호출을 거부하는 규칙은 두 버전에서 바이트 단위로 동일하다. 이를 면제하는 것은 명시적인 `timeout`이 맞으며, 이 모델의 32,768 tokens은 기준값인 21,333을 넘는다.
  - **검증 완료**: 업데이트된 버전에서 502개 + 31개 테스트 모음 통과, `requirements.txt` 잠금 결과가 설치 상태와 일치함(고정 항목 41개), 그리고 각 SDK로 실제 호출 수행(OpenAI 및 Claude). `--news` 모드의 문서에서 원본과 동일한 구조를 확인했다.

- **1.13.0** `--use_openrouter` provider: 중국산 오픈 모델을 포함한 약 430개 모델로 연결하는 유료 라우터(2026-09-05):

  - **아홉 번째 provider 경로를 여덟 번째 경로와 함께 제공한다.** 1.12.0은 PyPI에 게시되지 않았다. 두 라우터인 OpenCode와 OpenRouter가 함께 출시된다. [OpenRouter](https://openrouter.ai)를 사용하면 단일 키와 사용량 기반으로 청구되는 하나의 크레딧을 통해 여기의 다른 어떤 provider도 제공하지 않는 Kimi, Qwen, DeepSeek, Z.ai 등의 모델에 접근할 수 있다. endpoint가 OpenAI와 호환되므로 xAI와 같은 클라이언트를 사용한다. **이 provider를 구별하는 모든 요소는 preflight에 있으며**, 각 규칙은 API 측정 결과에 근거한다.

  - **같은 모델이 서로 다른 한도를 가진 수십 개의 호스팅 업체에서 제공되지만, 라우팅은 이를 고려하지 않는다.** 측정 결과 `z-ai/glm-5.2`에는 33개, `z-ai/glm-5.3-flash`에는 23개의 호스팅 업체가 있었으며, 그중 하나는 **출력이 2,048 tokens으로 제한**되어 있었다. 따라서 긴 번역은 23번 중 한 번꼴로 무작위로 잘렸고, 어떠한 신호도 없었다. preflight는 `/api/v1/models/{modèle}/endpoints`을 읽고 출력 한도가 8,000 tokens 미만인 업체, 상태가 저하된 업체, 한도를 선언하지 않은 업체를 제외한 뒤 나머지를 고정한다. `allow_fallbacks: false`가 **없는** `provider.only`은 단순한 선호 설정일 뿐이다. 라우터가 제외된 업체로 다시 전환하므로 고정이 아무 의미가 없어진다. 한도를 충족하는 호스팅 업체가 하나도 없으면 명령이 중단된다. 그래도 번역을 진행하는 것은 이 preflight가 방지하려는 무음 잘림을 받아들이는 것과 같다.

  - **추론은 출력 요금으로 청구되며 많은 모델에서 기본적으로 활성화되어 있다.** `z-ai/glm-5.2`에 같은 요청을 보내 “OK”라는 응답을 받은 결과, **모델 기본값에서는 completion tokens이 107개였지만 추론을 끄면 2개**였다. 추론이 아무런 이점도 주지 않는 번역에서는 모든 파일의 모든 segment마다 비용이 18배로 늘어난다. 따라서 기본적으로 비활성화된다. 추론이 필수인 **431개 모델 중 288개**는(`reasoning.mandatory`) `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`를 반환한다. 이러한 모델에는 preflight에서 허용되는 effort를 읽고 가장 낮은 값을 요청한다(다음 항목 참조). effort는 추론이 우선 소비하는 **`max_tokens`의 일정 비율**을 할당하므로, 값을 임의로 선택하면 빈 페이지 위험을 줄이는 대신 옮겨 놓을 뿐이다.

  - **추론이 필수인 모델에는 해당 모델이 허용하는 가장 낮은 effort를 사용하며, 이는 측정 결과에 따른 결정이다.** 처음에는 모델을 대신해 추측하지 않도록 아무것도 보내지 않기로 했다. 카탈로그 기본값이 `max`인 `z-ai/glm-5.3-flash`에서 검증한 결과, 이 선택은 번역이 끝나기 전에 **32,768 tokens에서 출력이 잘리는** 결과를 낳았다. 14개 언어 중 2개가 유실되었다. 전체 한도를 늘려도 달라지는 것은 없었을 것이다. effort가 한도의 일정 비율을 할당하므로 추론도 함께 늘어나기 때문이다. 따라서 provider는 preflight에서 `supported_efforts`을 읽고 가장 낮은 값을 요청하며, 카탈로그에 사용할 수 있는 값이 없으면 “없음”으로 대체한다. 문제가 발생했던 언어로 반대 검증을 수행한 결과, 이전에는 budget 소진으로 실패했지만 이제는 9분 안에 원본과 동일한 구조로 완료된다.

  - **이제 upstream 호스팅 업체의 장애에는 해당 업체의 이름이 표시된다.** 라우터는 이 경우를 null인 `native_finish_reason`이 포함된 `finish_reason=error`로 정규화한다. 두 언어에서 두 번 측정한 결과 정확히 750초에 발생했다. 일반적인 오류 메시지는 문서나 분할 방식의 문제를 찾게 만들었다. 이제는 공급자 측 장애이며 재시도만으로 해결되는 경우가 많다고 안내한다.

  - **출력이 비어 있는 `finish_reason=length`는 잘림이 아니다.** 첫 번째 유효 문자가 나오기 전에 추론이 budget을 모두 소비한 것이다. 측정 결과 유효한 tokens 148개를 생성하기 위해 추론 tokens 15,850개가 사용되었다. 두 경우에는 정반대의 조치가 필요하다. 전자의 경우 segment 크기를 줄여도 아무 소용이 없다. 이제 메시지에서 두 경우를 명확히 구분한다. 측정에서 도출된 보호 로직도 두 개 추가했다. upstream 호스팅 업체가 실패하면 라우터는 **오류만 담긴 본문과 함께 200을 반환**한다(`choices[0]`은 메시지를 가리는 불투명한 `TypeError`을 발생시켰다). 또한 context window를 카탈로그에서 읽어 `MODEL_TOKEN_LIMITS`에 기록한다. `DEFAULT_TOKEN_LIMIT`은 카탈로그의 44개 모델에서 잘못된 값이며, 여기에는 4,095 tokens으로 제한된 모델 두 개도 포함된다.

  - **`--model fournisseur/modèle`는 필수이며 네트워크에 연결하기 전에 형식을 검증한다.** OpenRouter는 공급자가 아니다. 모델 선택에는 가격, 라이선스, 데이터 처리가 수반되므로 사용자를 대신해 선택하지 않는다. slug가 preflight URL에 보간되므로 검증은 단순한 사용성 배려가 아니라 경로 삽입을 막는 보호 장치다. 두 라우터가 공통으로 사용하는 namespace 형식의 정규식은 `a/b/..`를 허용하므로 상위 segment를 명시적으로 거부한다. `--eco`는 아무 효과가 없으며 그 사실을 안내한다.

  - **잘못된 내용 하나를 포함해 표현 세 가지를 수정했다.** `codex exec`에 관한 OpenAI의 경고는 저장소의 공개 여부가 아니라 공유 runner에서 개인 session 파일이 삽입되는 문제를 다룬 것이었다. README, CLAUDE.md, 코드에서 이 경고를 반대 의미로 인용하고 있었다. OpenCode의 인증 위치는 1.18.27에서 변경되었다(`opencode.db`의 `credential` table이며 더는 `auth.json`이 아니다). “여기서는 절대 읽지 않는다”라는 불변 조건은 여전히 맞았지만 위치 정보가 오래된 상태였다. 마지막으로 OpenCode 섹션은 이제 검증된 적 없는 경로를 동등한 선택지로 소개하지 않는다. Zen gateway와 Ollama는 전체 과정을 측정했지만 GitHub Copilot, LM Studio, llama.cpp는 측정하지 않았으며, 이제 README에 이 사실을 명시한다.

  - **대규모 측정과 README의 권장 모델 table.** 세 가지 문서 모음으로 300회가 넘는 번역을 14개 언어에 대해 수행했다. `--news` 모드의 밀도 높은 블로그 글, 표준 Markdown 형식의 이 README, 그리고 GitHub에서 그대로 가져온 유명 프로젝트 README 4개를 사용했다. table은 이전에 혼동했던 두 가지를 구분한다. 번역이 **완료되는 경우**와 번역의 **구조가 원본과 동일한 경우**다. 밀도 높은 두 문서에서 단 하나의 정보도 유실하지 않은 모델은 세 개였다. `gemini-3.7-flash`, ChatGPT 구독의 `gpt-5.6-sol`, OpenRouter를 통한 `z-ai/glm-5.2`다. 이들의 유일한 차이는 한두 개 언어에서 `**` 한 쌍이 옮겨지지 않은 것이었다. 핵심 결론은 **판별 요인이 `--news` 모드가 아니라 문서의 밀도**라는 점이다. 구독을 통한 Grok은 블로그 글에서 14번 중 13번 실패했지만 공개 README에서는 16번 중 14번 성공했다. 원인은 긴 segment에서의 이탈이며 반대 검증으로 확인했다. table에는 자체 주의 사항도 포함된다. 이 결과는 모든 모델을 포괄하지 않고 특정 시점의 측정이며, 소요 시간은 순위를 뜻하지 않는다. 가장 적절한 방법은 여전히 자신의 문서로 직접 측정하는 것이다.

  - **구조 비교기가 비라틴 문자에서 두 건의 거짓 양성을 생성했으므로 수치를 공개하기 전에 수정했다.** URL 뒤에 전각 괄호 `）`가 붙으면 `)`에서 멈추는 정규식이 이를 분리하지 못해 URL은 동일한데도 추출된 문자열이 달라졌다. 또한 프랑스어로 다섯 줄인 인용문이 중국어에서는 세 줄에 들어가 줄 단위 집계가 감소했다. 두 수정 사항은 반대 검증을 거쳤다. URL, 섹션 또는 inline code를 삭제하면 여전히 감지된다. 수정하지 않았다면 Gemini와 Codex의 결과는 각각 14개 언어 중 13개와 12개가 아니라 둘 다 11개로 공개되었을 것이다.

  - **테스트**: 새로운 파일 `tests/test_openrouter_provider.py`(테스트 76개) — 모델 검증 및 상위 segment 거부, 호스팅 업체 고정(한도, 상태, 미선언 한도, 공통 최솟값), `allow_fallbacks`은 항상 false, `mandatory`에 따라 추론 비활성화 또는 유지, 완전한 출력 계약(200 응답 내 오류, 선택 항목 없음, 빈 페이지와 잘림 구분, 비정상적인 `finish_reason`, null 콘텐츠), 카탈로그에 연결할 수 없을 때 preflight fail-closed, slug 누락 및 정상 호스팅 업체 부재, flag 상호 배타성 및 파일명 레이블. 전체 테스트 모음은 **502개 테스트**다.
  - **리팩터링: 4,253줄짜리 단일 모듈을 동작 코드는 한 줄도 바꾸지 않고 여러 모듈로 분할했습니다.** `src/aipmt/translate.py`은 `config`, `markdown`, `segmentation`, `guards`, `placeholders`, `news`, `prompts`, `notes`, `naming`, `pipeline`, `cli` 및 하위 패키지 `providers/`으로 나뉩니다(provider마다 모듈 하나, 기반이 되는 `base`, 해석과 dispatch를 담당하는 `registry`). 각 이동은 기계적으로 증명되는 commit입니다. 검증기가 패키지의 모든 최상위 노드 AST를 참조 snapshot과 비교하고, 각 symbol의 위치와 안전 marker가 원문 그대로 유지되는지, 추적되지 않은 파일이 없는지를 확인합니다. 이 임시 도구는 다음 버전에서 제거됩니다. 눈에 보이는 변경 사항은 다음과 같습니다. `aipmt.translate`은 이제 모듈이 `_` 접두사 없이 노출하던 64개 이름을 객체 identity 그대로 다시 노출하는 façade가 됩니다(`__all__`이 그중 9개를 포함하며 지원되는 API이고, 나머지는 호환성 alias입니다). 또한 `import *`가 한꺼번에 가져오던 dependency 및 표준 library의 이름 29개를 더 이상 다시 export하지 않습니다. 파일을 직접 실행하는 방식(`python src/aipmt/translate.py`)은 더 이상 존재하지 않으며, `aipmt`과 `python -m aipmt`만 지원되는 두 가지 형식으로 남습니다. 공개 함수의 `__module__`은 해당 함수가 정의된 모듈의 값입니다. SDK는 `.env`을 불러온 뒤 import되며 이전처럼 그 전에 import되지 않지만, 알려진 영향은 없습니다. 427개 test는 identifier까지 그대로 유지한 채 실제로 실행하는 모듈로 이전되었습니다. façade를 거치던 patch 91개는 이제 해당 이름을 조회하는 모듈을 대상으로 합니다(그중 2개는 patch가 없어도 통과함을 측정했습니다). façade를 고정하는 contract test 7개가 추가되었고, 검증을 중단함으로써 gate가 통과하는 일이 없도록 첫 번째 이동에 앞서 gate 도구를 다시 작성했습니다. directory 단위 Lizard scope와 하한선, 구성된 parser에서 읽는 flag, package별 coverage 하한선, 추적되는 모듈을 열거하는 `release.sh`이 적용됩니다.
  - **수정(pull request 검토)**: OpenRouter는 `context_length`이 없는 catalog 항목에 128,000 tokens의 기본값을 측정값처럼 기록하지 않고 이를 거부합니다. 이전 동작은 “목록에 없는 모델” 경고까지 꺼 버렸습니다. 또한 `finish_reason`이 null일 때(문서화된 type은 `string | null`)는 provider의 원본 사유를 그대로 따르며, `max_tokens`은 `length`가 됩니다. 선택 항목 자체에 포함된 오류는 함께 제공된 부분 content를 거부하며, 정규화된 upstream 장애와 동일하게 provider 세부 정보, 원본 사유, 조언을 합친 message를 표시합니다. OpenCode는 `part: null` event에 대해 `AttributeError`이 아니라 자체 contract 오류로 응답하며, 읽을 수 없는 event line이 포함된 JSONL stream은 부분 text를 받아들이지 않고 거부합니다. 세 agent형 CLI는 호출 중 해당 process가 `SIGTERM`을 받으면 agent의 group을 종료합니다. regen의 `timeout`은 agent가 살아남아 quota를 소비하게 했습니다. group의 `SIGKILL`에는 언제나 유예 시간이 적용되며, 정상적으로 종료되는 shim은 그 하위 process를 살려 둡니다. 분할 과정에서 갈라졌던 `# fmt: off` / `# fmt: on` pair를 다시 결합했습니다. `--reasoning_effort` 도움말에는 이를 사용하는 네 provider의 이름이 명시됩니다.
  - **수정(두 번째 재검토)**: 이제 OpenRouter에 요청하는 출력 상한은 prompt와 segment가 차지하는 context 몫을 확보합니다. `context_length`은 입력과 completion을 모두 포함하지만, catalog의 모델 6개는 입력을 위한 공간도 없이 요청이 전송되고 있었습니다. context가 너무 짧으면 비용이 청구되기 전에 거부됩니다. agent형 CLI 기반 계층은 POSIX process group이 없는 환경에서 `AttributeError`가 timeout guard를 통과하여 대기가 길어지도록 두지 않고 `terminate`, 이어서 `kill`으로 fallback합니다. OpenCode의 `429` marker는 이제 substring이 아니라 숫자로 검색됩니다. 이전에는 `err_84290b` 같은 error identifier가 90초의 back-off를 유발한 뒤 결국 실패했습니다. 마지막으로 표준형이 아닌 OpenRouter endpoint가 preflight에 표시됩니다. project의 `.env`만으로도 endpoint를 설정할 수 있으며, 이후 실제로 전송될 key가 사용됩니다.
  - **보안: project의 `.env`은 더 이상 API 호출을 redirect할 수 없습니다.** `find_dotenv(usecwd=True)`은 현재 directory와 그 parent에서 파일을 찾습니다. 따라서 방금 clone한 repository 같은 신뢰할 수 없는 directory tree가 key를 전혀 알지 못한 채 `OPENROUTER_BASE_URL`, `XAI_BASE_URL` 또는 `OPENAI_BASE_URL`(마지막 것은 SDK 자체가 읽음)를 설정할 수 있었고, 이후 environment나 user configuration에서 가져온 실제 key가 제3자 server의 authorization header로 전송되었습니다. filter는 목록이 아니라 패턴을 기준으로 합니다. 설치된 SDK를 조사한 결과 routing variable 12개가 읽히며, 그중 6개는 Anthropic client 하나만 사용합니다. 직접 작성한 열거 목록이었다면 절반을 빠뜨렸을 것입니다. 따라서 `_BASE_URL`, `_API_BASE` 또는 `_ENDPOINT`에 해당하는 모든 variable과 proxy, certificate store는 project layer에서 거부됩니다. 제어되는 인증 기관을 지정하면 interceptor를 실제 server와 구별할 수 없기 때문입니다. `XDG_CONFIG_HOME`과 `APPDATA`도 거부됩니다. 이를 설정하는 것은 어떤 파일을 user layer로 간주할지 결정하는 것과 같아 우회적으로 filter를 회피할 수 있기 때문입니다. 이러한 variable은 사용자가 제어하는 두 layer, 즉 export된 environment와 `~/.config/aipmt/.env`에서만 허용됩니다. 또한 project layer는 interpolation 없이 읽힙니다. `load_dotenv`은 기본적으로 `${VAR}`을 확장하며, `NOM_ANODIN=${OPENAI_API_KEY}`을 포함한 신뢰할 수 없는 `.env`은 실제 key를 subprocess의 패턴 기반 filter가 인식하지 못하는 이름으로 복사했습니다. 그러면 해당 key가 명시된 invariant를 위반하여 `codex exec`의 environment로 들어갔습니다. 마지막으로 거부 message에는 variable 이름만 표시됩니다. `https://${CLE}@hôte/` 형식의 URL은 거부되는 상황에서도 interpolation된 key를 log에 유출했습니다. 거부 사실과 해결 방법은 stderr에 출력됩니다. 기업용 relay는 user configuration에 선언해야 합니다.
  - **수정: OpenRouter의 출력 envelope를 호출마다 계산합니다.** `context_length`은 입력과 completion을 모두 포함하며, 라틴 문자 text에 맞춘 고정 reserve로는 아무것도 제한할 수 없습니다. `o200k_base` tokenizer로 측정했을 때 16,000자는 프랑스어에서 3,200 tokens이지만 일본어에서는 12,300 tokens, emoji에서는 17,500 tokens입니다. 따라서 budget은 실제로 전송되는 text에서 산출하고 UTF-8 byte 수만큼 여유를 더합니다. byte fusion tokenizer, 즉 byte 수준 BPE와 byte fallback을 사용하는 SentencePiece처럼 catalog에서 쓰는 계열에서는 token 하나가 적어도 1 byte에 해당하며, OpenRouter가 알 수 없는 수십 개 tokenizer로 routing하는 이 상황에서 사용할 수 있는 유일한 상한입니다. 평균 ratio는 어떤 것도 적합하지 않았습니다. 보조 평면의 ideogram은 token당 1.33 bytes까지 내려가고 combining character는 1.00 byte까지 내려갑니다. 이제 입력과 출력은 구조적으로 window 안에 들어갑니다. 선택한 모델에 비해 지나치게 조밀한 segment는 비용 청구 후가 아니라 호출 전에 거부됩니다.

- **1.12.0** Provider `--use_opencode`: 선택한 provider로 연결하는 open source agent OpenCode — local model, 계정 없는 무료 이용, subscription 또는 key(2026-09-04):

  - **성격이 앞선 일곱 가지와 다른 여덟 번째 provider 경로입니다.** [OpenCode](https://opencode.ai)(MIT)는 model provider가 아니라 사용자가 OpenCode 자체에 구성한 대상으로 연결하는 _router_입니다. 대상은 API key, subscription(GitHub Copilot, ChatGPT, SuperGrok), 계정 **없이** 무료 model을 제공하는 OpenCode Zen gateway 또는 **local** model(Ollama, LM Studio, llama.cpp)일 수 있습니다. script는 Codex와 Grok을 제어하는 것처럼 `opencode run`을 non-interactive mode로 제어하며 동일한 subprocess 기반 계층을 재사용합니다. 독립된 process group, timeout 시 `SIGTERM`에 이어 `SIGKILL`, 항상 닫힌 stdin, 정제된 environment가 적용됩니다. **실제 번역 두 건**으로 검증했습니다. `opencode/mimo-v2.5-free`을 통해 이 README 전체를 영어로 번역한 작업은 49초가 걸렸고 단 한 번의 pass로 source file과 동일한 구조(제목 32개, code 종료 marker 26개, link 18개, URL 37개, table line 37개, inline code 135개)를 보존했습니다. 또한 `ollama/qwen2.5:7b`을 통해 test file을 어떤 key도 없이 local에서 번역했습니다.

  - **`--model provider/modèle`은 필수이며, 이는 의도적인 선택입니다.** `--model`이 없으면 OpenCode는 자체 기본값으로 fallback합니다. 새 installation에서는 대화를 training에 사용할 수 있는 무료 “stealth” model인 `opencode/big-pickle`이 기본값이며, 측정 결과 실제로 이 model이 응답했습니다. 사용자를 대신해 이를 조용히 선택하는 것은 이 repository가 추적하는 보이지 않는 전환과 정확히 같은 종류의 문제입니다. 따라서 error message에는 model을 나열하는 command(`opencode models`)와 local, 무료, subscription의 세 가지 예시를 명시합니다. `--eco`은 효과가 없으며 그 사실을 알립니다. `--reasoning_effort`은 명시적으로 요청한 경우에만 OpenCode의 `--variant`으로 그대로 전달됩니다.

  - **격리는 가정한 것이 아니라 측정한 것입니다.** inline configuration(`OPENCODE_CONFIG_CONTENT`, OpenCode의 merge 순서에서 마지막이므로 user configuration을 대체하지 않으면서 우선함)은 모든 tool이 거부되는(`permission: {"*": "deny"}`) agent `aipmt`을 정의합니다. registry는 더 이상 tool을 model에 제공하지도 않으므로 “파일을 나열하고 `id`을 실행하라”는 지시를 받아도 tool이 없다고 답합니다. session 공유는 비활성화되고 외부 plugin은 제외되며(`--pure`), `--auto`은 절대 사용하지 않고, 일회용 빈 working directory를 사용합니다. 두 가지 암묵적 injection을 측정하여 차단했습니다. `OPENCODE_DISABLE_CLAUDE_CODE`이 없으면 사용자의 `~/.claude/CLAUDE.md`이 **모든** prompt에 들어갑니다(단순한 “안녕하세요”에도 입력이 186 tokens에서 515 tokens으로 증가). `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 directory의 `AGENTS.md`도 들어갑니다. “모든 응답을 BANANA로 끝내라”는 instruction이 번역에 실제로 적용되었습니다. 반면 global `~/.config/opencode/AGENTS.md`은 계속 injection됩니다. 이를 차단하는 switch는 없으며, 우회적인 `XDG_CONFIG_HOME`으로 피하면 사용자의 provider도 함께 숨겨집니다. 임시변통 대신 이 사실을 문서화했습니다.

  - **`exit 0`만으로는 아무것도 입증되지 않습니다. 세 번째 CLI에도 같은 원칙을 적용하되, 이 CLI만의 함정 두 가지가 있습니다.** 알 수 없는 `--agent`을 사용해도 `opencode run`은 실패하지 않습니다. stderr에 warning을 표시하고 tool이 활성화된 coding agent로 **조용히** fallback합니다. inline configuration이 적용되지 않더라도 번역이 파일을 작성할 수 있는 agent와 함께 실행될 수 있다는 뜻입니다. 따라서 출력 contract는 return code 0, `error` event 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`임(`length`은 잘린 응답), 비어 있지 않은 text라는 조건에 더해 이 message가 없는지도 확인합니다. 두 번째 함정은 error JSON event가 **불투명**하다는 점입니다. 단순한 reference와 함께 “예기치 않은 server 오류입니다. 자세한 내용은 server log를 확인하세요.”라고만 표시되며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 log에만 존재합니다. 그래서 `--print-logs --log-level ERROR`와 stderr의 `error="…"` field를 읽되 그 뒤에 이어지는 Bun trace는 제외합니다. 이에 따라 알 수 없는 model은 원인이 명시된 채 1초 안에 실패합니다. 또한 `--title`은 불필요한 LLM 호출을 방지합니다. 이 option이 없으면 OpenCode가 `small_model`을 한 차례 더 호출하여 session title을 생성합니다.

  - **Secret: Codex 및 Grok과 같은 패턴 기반 filter를 사용하되, 명시된 한 가지 예외가 있습니다.** `OPENCODE_API_KEY`은 유지됩니다. 이는 OpenCode 자체의 key(Zen gateway, Go subscription)로, 그 이름대로 OpenCode에 전달됩니다. 즉, OpenCode의 `auth.json`에 해당하며 aipmt가 관리하거나 비용을 청구할 수 있는 key가 아닙니다. provider는 OpenCode에서 구성하며(`opencode auth login`, `opencode.json`), aipmt의 `.env`에서는 구성하지 않습니다. aipmt의 key는 어떤 것도 subprocess에 도달하지 않습니다. subscription형 CLI와 달리 CI에서는 거부하지 않습니다. runner에서 API key나 self-hosted model을 사용하는 것은 정당한 용도이기 때문입니다.

  - **이제 traversal 방지 guard는 원시 값이 아니라 interpolation된 값을 검사합니다.** `provider/modèle`에는 1.10.0의 guard가 거부하던 `/`이 포함됩니다. `--model`이 file name `--include_model` 안에서 interpolation되므로 당시 거부는 타당했습니다. 이제 file name label은 interpolation 전에 `/`, `\`, `:`을 `-`으로 바꾸며(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, `:`은 Windows에서 허용되지 않음), upstream guard는 이 label을 검사합니다. `../../evil`은 대상 아래의 단순한 이름 `doc-en-..-..-evil.md`이 되고, `..`만 계속 거부되며 `--target_lang ../x`도 거부됩니다. `_ensure_within_directory` scope guard는 변경 없이 두 번째 layer로 유지됩니다.

  - **무료 model과 local model에 관해 측정된 결과입니다.** `opencode/mimo-v2.5-free`은 문단 하나를 16초에, 이 README를 49초에 번역합니다. `opencode/big-pickle`은 200단어에 40초가 걸리며, 각각 단독으로는 완료되는 요청 두 개를 동시에 보냈을 때 5분 동안 응답하지 않았습니다. `opencode/nemotron-3.5-lightning-free`은 3분 동안 아무 응답도 하지 않았습니다. 따라서 `REGEN_PROVIDER=opencode`에서는 `REGEN_MODEL`이 필수이며 병렬 실행은 **2 jobs**입니다. local 측에서는 Ollama가 context를 흔히 4,096 tokens로 설정하지만 segment는 최대 16,000자입니다. 따라서 `PARAMETER num_ctx 32768`을 포함한 `Modelfile`이 필요하며, 품질은 model에 따라 달라집니다. test file에서 7B model은 list 순서를 뒤집고 code block 종료 marker를 손상했지만, gateway model은 모든 것을 보존했습니다.

  - **이 repository의 번역은 이제 유료 API를 절대 거치지 않습니다.** `regen_translations.sh`은 `.env`에 key가 하나라도 있으면 곧바로 OpenAI API를 사용하고 Codex는 opt-in으로만 제공했습니다. 이번 버전을 준비하면서 정확히 이 일이 발생했습니다. 28개 번역이 OpenAI API로 전송된 뒤 Hindi CHANGELOG는 Gemini API로 전송되었지만, 사용량 기반 비용을 내지 않기 위해 ChatGPT subscription을 사용하고 있었습니다. key 자동 감지는 제거됩니다. **Codex가 기본값이며 `gpt-5.6-sol`을 사용합니다.** 이는 품질 model입니다. `openai`, `gemini`, `grok`은 `REGEN_PROVIDER`과 함께 `REGEN_ALLOW_PAID_API=1`도 요구합니다. 결정 시점에 규칙이 실제로 적용되도록 명시적으로 이름 붙인 예외입니다. 알 수 없는 `REGEN_PROVIDER`은 API로 fallback하지 않고 실패합니다. test 10개가 기본값, 거부, 예외를 고정합니다. 이번 버전의 번역 28개는 Codex를 통해 다시 수행했습니다.

  - **rate limit의 back-off를 공통화했습니다**(`_retry_on_rate_limit`). Codex와 Grok의 loop는 label을 제외하면 동일했으며 세 번째 복사본을 만들면 중복 한도를 넘게 됩니다. 세 CLI의 error는 하나의 공통 `_CliCallError`에서 파생됩니다. 세 error 중 하나라도 이 계층을 벗어나면 공유 loop가 더 이상 이를 감지하지 못하므로, 이를 금지하는 test를 추가했습니다.

  - **Test**: 새로운 파일 `tests/test_opencode_provider.py`(61개 test) — 전체 출력 contract, agent fallback, log에서 읽는 원인, 중복 제거된 text part와 무시되는 synthetic part, process group을 종료하는 timeout, 429에 대한 back-off, 필수 및 검증 대상 model, secret 없는 preflight, binary 해석, dispatch 연결, file name label 및 traversal 반증을 다룹니다. `tests/test_review_hardening.py`은 flag의 상호 배타성과 secret 부재 검사를 새 provider까지 확장합니다. 이제 gate는 문서화된 argparse **flag 22개**를 요구합니다. 전체 suite는 **382개 test**입니다.

- **1.11.1** 문서 수정: README에 마침내 일곱 가지 provider 경로가 명시됩니다(2026-09-03):
  - **1.11.0의 PyPI 페이지에는 “4개 API + Codex CLI”라고 적혀 있었습니다.** 실제 코드는 7가지를 제공합니다. 사용량 기반 과금이 적용되는 API 방식의 OpenAI, Mistral, Claude, Gemini, Grok과 사용량 기반 과금 없이 구독으로 이용하는 Codex(ChatGPT), Grok입니다. 두 Grok 모드는 소개 문구와 _다중 제공자_ 항목에서 누락되었고, 14개 번역본도 같은 오류를 반복했습니다. 패키지의 긴 설명은 버전별로 고정되므로 공개 페이지를 수정하려면 새 버전 번호가 필요했습니다. 이것이 이번 버전의 유일한 존재 이유입니다. **코드 변경은 없습니다.**
  - `CLAUDE.md`은 릴리스에서 도입된 내용에 맞게 정비되었습니다. gate 카운터(`--full`에서 16, 17), 활성화된 11개 workflow, `gh pr checks`에 표시되지 않는 Sonar/Codacy 카운터 2개(hotspots, Codacy API), `ruff-format`에 의한 `# nosemgrep` 이동, OIDC 교환에 필요한 GitHub environment, 그리고 _pending publisher_가 이름을 선점하지 않는다는 사실이 반영되었습니다.

- **1.11.0** PyPI 릴리스: 저장소를 clone하지 않고 `pip install ai-powered-markdown-translator` 후 `aipmt` 명령 실행(2026-09-03):

  - **단일 파일 스크립트가 설치 가능한 패키지로 전환되었습니다.** `translate.py`가 루트에서 `src/aipmt/translate.py`로 이동했으며, console entry point `aipmt`와 이에 상응하는 `python -m aipmt`이 제공됩니다. 기여하려면 여전히 저장소를 clone해야 합니다. 테스트, 28개 번역본, 품질 도구가 그곳에 있기 때문입니다. 하지만 사용하는 데는 더 이상 필요하지 않습니다.

    - **import 이름은 `aipmt`이며 절대 `translate`가 아닙니다.** 실제로 조용히 발생하는 충돌이 있기 때문입니다. PyPI 패키지 `translate`(v3.8.1, 마지막 upload 2026-07-06)은 같은 이름의 디렉터리를 설치합니다. venv에서 재현한 결과, 디렉터리가 모듈보다 우선되어 `translate.main`이 사라지고 entry point가 `AttributeError`에서 깨졌지만, `pip check`은 rc=0으로 “깨진 요구 사항을 찾지 못했습니다”라고 응답했습니다. 사용자가 단순히 `pip install translate`만 설치했어도 활용 가능한 진단 정보 없이 CLI가 깨질 수 있었습니다. 실제 wheel을 사용한 반대 검증에서는 해당 패키지 위에 `pip install translate`를 설치한 뒤 `aipmt --help`이 전후 모두 rc=0이었고, 두 CLI가 함께 작동했습니다.
    - **distribution 이름은 길게, 명령은 짧게 정했습니다.** `ai-powered-markdown-translator`을 사용하면 PyPI 검색으로 패키지를 찾을 수 있습니다. 약어만으로는 프로젝트를 이미 아는 사람이 아니면 찾을 수 없는데, 이번 릴리스의 목적은 바로 검색을 통해 발견되게 하는 것입니다. 가능성 있어 보였던 두 후보는 검증 후 제외했습니다. `ai-markdown-translator`은 같은 목적의 도구가 2024년부터 npm에서 이미 사용 중이며, 이 저장소보다 17개월 앞섭니다. `aimt`은 같은 분야의 활성 패키지 `aim`(v3.29.1)과 한 글자밖에 차이 나지 않아 장기적인 혼동을 일으키기 가장 좋은 조건입니다. 방법론상 주의할 점도 있습니다. `pypi.org/project/<nom>/`은 어떤 이름에도 200을 반환하는 bot 차단 페이지이므로 JSON API만 신뢰할 수 있습니다.
    - **평면 패키지 대신 `src/` layout을 사용했습니다.** 평면 패키지는 테스트의 `sys.path.insert(..., "..")` 6개를 그대로 유지할 수 있었겠지만, 바로 그것이 문제입니다. 이 방식은 패키지가 아니라 source tree를 import하므로 패키징 오류를 모두 감출 수 있습니다. 실제 비용은 치환 규칙 하나가 추가되는 정도입니다.

  - **이제 키를 한 번만 설정하면 계속 사용할 수 있습니다.** 설치된 CLI에는 영구적인 설정이 전혀 없었고, 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었습니다. `find_dotenv`는 실제로 시스템 루트까지 거슬러 올라가므로 **사용자의 home 디렉터리 아래에서 작업할 때는** `~/.env`을 찾았지만, 다른 위치에서 작업하면 아무것도 찾지 못했습니다. 이는 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라지는 불완전한 지원이었습니다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`이 추가되었습니다.

    - **우선순위는 별도 코드로 작성되지 않았으며**, `load_dotenv`의 기본값인 `override=False`에서 자연스럽게 결정됩니다. 각 계층은 앞선 계층에서 비어 있던 값만 채웁니다. 따라서 환경 변수 → 프로젝트의 `.env` → 사용자 설정 순서가 되며, 구조가 아닌 동작 테스트로 검증합니다. 두 호출의 순서를 바꾸거나 세 번째 계층을 제거하면 테스트가 실패합니다.
    - **TOML이 아니라 `.env` 형식을 사용한 것은 의도적인 선택입니다.** `python-dotenv`는 이미 dependency이고, 해당 문법은 15개 README에 이미 문서화되어 있으며, 같은 파일을 두 scope에서 사용할 수 있습니다. 새로운 dependency나 문법은 추가되지 않습니다. 위치는 `XDG_CONFIG_HOME`가 **절대 경로일 때만** 이를 따릅니다. 사양상 상대 경로 값은 무시해야 하며, 그렇지 않으면 설정 위치가 다시 현재 디렉터리에 따라 달라지기 때문입니다. Windows에서는 `APPDATA`를 따릅니다.
    - **두 가지 대안과 제외한 이유도 명확합니다.** 시스템 keyring(`keyring`)은 데스크톱에서는 더 안전하지만 서버, container, CI 같은 headless 환경에서 실패합니다. 이는 바로 일괄 번역의 주요 사용 사례이므로 opt-in 방식으로는 좋은 후보지만 기본값으로는 적합하지 않습니다. `--api-key` flag는 키를 shell history에 남기고 `ps`에서도 보이게 합니다.
    - **키가 없을 때 더 이상 호출 trace가 표시되지 않습니다.** 이전에는 사용자가 `site-packages`을 가리키는 Python stack과 함께 “환경 또는 .env”라고만 명시하고 두 번째 파일을 어디에 만들어야 하는지는 알려 주지 않는 메시지를 받았습니다. 이제 세 위치와 정확한 경로를 모두 나열하고 명령은 2로 종료됩니다. 보호 범위는 **의도적으로 좁게** 설정되어 `except ValueError`가 설정 단계에만 적용됩니다. 전체 실행을 감싸면 번역 도중 발생한 실제 bug가 안심시키는 메시지로 바뀌는데, 이는 이 저장소가 추적하는 바로 그 실패 방식입니다. 이를 금지하기 위해 테스트가 `main()`의 source를 읽습니다.

  - **수정 사항 — 도구 설치 후 사용자의 `.env`이 무시되었습니다.** 인수 없는 `load_dotenv()`는 현재 디렉터리부터 거슬러 올라가는 것이 아니라 호출한 파일, 즉 `site-packages`부터 탐색합니다. 자체 `.env`가 있는 프로젝트에서 실제 console entry point를 실행해 측정한 결과, `find_dotenv()`는 `''`을 반환해 키를 불러오지 못했지만 `find_dotenv(usecwd=True)`는 이를 찾았습니다. 도구가 clone된 저장소 안에서만 실행될 때는 존재하지 않던 bug였지만, 릴리스 후에는 올바르게 설정했는데도 API 키가 “없다”는 유일한 증상과 함께 항상 발생했을 것입니다.

  - **세 gate는 아무것도 검증하지 않게 되었어도 녹색으로 통과했을 것입니다.** 따라서 이동 전에 의도적으로 강화했습니다. 잡아내야 할 변경 후에 작성된 safeguard는 아무것도 증명하지 못합니다. 각 gate는 원본 저장소에서는 녹색이고 이동된 복사본에서는 빨간색으로 바뀌며, 두 방향 모두 측정했습니다.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시합니다.** rc=0이며 “분석된 파일 0개”로 나옵니다. complexity gate는 158개 function / 2247 nloc에서 3개 function / 34 nloc로 줄어들고 출력은 0바이트가 되었을 것입니다. 이제 scope는 각 항목의 존재 여부를 확인하는 배열입니다.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`은 실패하지 않습니다.** stderr에만 경고를 출력하고 unittest와 `coverage xml` 모두 rc=0이며, 1453개 statement에서 141개로 잘린 보고서도 그대로 게시됩니다. 거의 분석되지 않았기 때문에 오히려 프로젝트가 정상으로 보였을 것입니다. 보고서는 전체 수와 측정된 가장 큰 파일이라는 두 하한선으로 보호됩니다.
    - **번역 최신성 probe는 구조적으로 호출 형식을 감지하지 못합니다.** argparse flag를 기준으로 고정되는데, 파일 이름을 바꿔도 바로 이 부분은 변하지 않습니다. 재현 결과, 모듈을 이동한 뒤에도 15개 README에는 존재하지 않는 명령이 계속 문서화되어 있었지만 판정은 “오래된 번역 없음”이었습니다. 따라서 7번째 section은 option이 아닌 호출 **형식**을 검증하며, Lizard hook은 script의 실제 scope와 대조됩니다. 해당 hook의 `files:`는 더 이상 일치하지 않아도 pre-commit을 실패시키지 않고 건너뛰게 만듭니다.

  - **`requires-python = ">=3.10"`은 더 이상 근거 없는 선언이 아닙니다.** 개발 환경에는 3.12만 있었고 한 번도 다른 버전에서 실행해 본 적이 없었지만, `sonar-project.properties`는 이미 3.10-3.12를 지원한다고 명시했습니다. 릴리스하면 공개될 내부 모순이었습니다. 이제 test workflow가 3.10, 3.11, 3.12에서 패키지 자체를 설치해 공개된 version bound까지 포함하여 suite를 실행합니다.

  - **하한선만 있고 상한선은 없습니다.** `requirements.txt`은 테스트된 lock으로 유지되고, `[project.dependencies]`는 공개 contract가 됩니다. lock의 정확한 version을 공개하면 다른 패키지를 함께 쓰는 모든 사용자의 환경에서 충돌을 일으킬 수 있습니다. `<N+1` 상한선도 없습니다. major version 지연 시 release gate를 실패시키는 `check-deps-fresh.sh`과 정면으로 모순되기 때문입니다. 설정된 하한선 조합은 정상적으로 resolve되며, 반대 검증인 `openai==1.0.0`은 `ResolutionImpossible`로 종료됩니다. 이는 검사가 모든 것을 허용하는 대신 실제로 구별한다는 증거입니다. 또한 guard가 `pyproject.toml`의 version과 CHANGELOG의 version이 달라지는 것을 금지합니다. PyPI에서는 version 번호를 재사용할 수 없습니다.

  - **새 venv에서 처음부터 끝까지 검증했습니다.** 약 70KB의 wheel에는 `aipmt/*.py`, dist-info, license만 포함되었습니다. `aipmt --help`은 22개 flag와 함께 rc=0이었고, `python -m aipmt`는 “usage: \_\_main\_\_.py”가 아니라 “usage: aipmt”를 표시했으며, `pipx` 설치도 정상적으로 작동했습니다. 무엇보다도 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행해 굵은 글씨, 목록, inline code, link, URL이 보존되고 code block은 번역되지 않음을 확인했습니다. migration 이전의 테스트 318개는 전후 identifier 목록이 바이트 단위까지 동일한 상태로 통과했습니다. 단순한 “OK”가 아니라 이것이 어떤 테스트도 무력화되지 않았음을 증명합니다. 3계층 설정 테스트 12개가 추가되어 총 330개가 되었습니다.

- **1.10.0** `--use_codex` provider(ChatGPT 구독 quota), SDK와 model 업데이트, 여러 문단으로 구성된 news citation 수정(2026-08-29):

  - **보안 검토 — PR에서 내세웠지만 모든 경로에서 지키지는 못했던 두 safeguard**:

    - **Codex preflight가 `.env` 전체를 binary로 전달했습니다.** `_codex_preflight`은 **`env=` 없이** `subprocess.run`을 호출했습니다. 따라서 subprocess가 `os.environ` 전체, 즉 `load_dotenv`이 불러온 `.env`의 모든 내용을 상속했습니다. 계측한 가짜 binary로 측정한 결과, 6개 provider의 키와 `GITHUB_TOKEN` 하나를 합친 **7개 secret**이 preflight에 전달되었습니다. 반면 `env=_grok_env()`를 올바르게 전달한 대응 경로 `_grok_preflight`에는 **하나도** 전달되지 않았습니다. 이는 PR 내부의 불일치였습니다. 바로 몇 줄 아래에 있는 `_strip_secret_env`는 정확히 이 invariant를 지키기 위해 존재합니다. `_codex_env_base()`을 추출해 두 경로가 공유하도록 했으며, 수정 후 측정 결과 양쪽 모두 전달된 secret은 0개였습니다.
    - **“`--deny` fail-closed” 속성은 실제 사용된 형식을 포함하지 않았습니다.** 주석에서는 알 수 없는 prefix를 가진 규칙이 시작을 거부한다는 점을 Grok confinement 전체의 근거로 삼았습니다. `grok 1.0.13`에서 측정한 결과, 이 validation은 **괄호를 사용한 형식에만** 존재했습니다. `--deny 'CeciNestPasUnOutil(*)'`는 시작을 거부하며 “알 수 없는 도구 접두사”라고 표시했지만, `--deny 'CeciNestPasUnOutil'`은 조용히 허용되었습니다. 그런데 `GROK_DENY_RULES`는 괄호 없는 이름만 사용했습니다. 따라서 xAI 측에서 tool 이름을 바꾸면 OS sandbox조차 적용되지 않는 시스템에서 아무런 신호 없이 유일하게 측정된 confinement 계층이 사라질 수 있었습니다. 이름이 지정된 8개 규칙은 각각 CLI에서 알려진 prefix로 검증되는 `Prefix(*)` 형식으로 변경했습니다. catch-all `*`은 허용되는 유일한 방식인 literal 형식으로 유지됩니다. 테스트가 validation되지 않는 형식으로 되돌아가는 것을 막습니다.
    - **그 밖의 항목도 문제없음을 검증했습니다.** 모든 곳에서 list 형식을 사용하고 `shell=True`는 전혀 사용하지 않으며, 문서 내용은 stdin 또는 `--prompt-file`를 통해 전달되므로 command injection은 없습니다. 안전하지 않은 deserialization도 없으며 type guard와 함께 `json.loads`만 사용합니다. 7개 payload로 시도한 path traversal 수정 우회도 발견되지 않았고, `--deny '*'`이 CLI에서 실제로 적용되어 workdir 밖을 읽을 때 `DENY_ENFORCED`이 관찰되었습니다.
    - 위에서 추가한 최신성 검사는 자체 원칙도 우회하고 있었습니다. PyPI 요청에 실패한 패키지를 조용히 건너뛰어 gate가 녹색으로 유지되었습니다. 이제 실제로 비교한 패키지 수를 계산하고 coverage가 불완전하면 실패합니다.

  - **Dependency를 최신화하고 같은 지연이 재발하지 않도록 두 safeguard를 추가했습니다.**

    - **지연은 실제였고 오래 지속되었습니다.** `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22**로 업데이트했습니다. 모든 provider 호출에서 TLS를 검증하는 root certificate store는 2년이나 뒤처져 있었습니다. 확인된 원인은 **`.github/dependabot.yml`가 존재하지 않았다는 것**입니다. 이 파일이 없으면 GitHub는 _security update_만 활성화하며, Dependabot은 CVE의 영향을 받는 dependency에 대해서만 PR을 제안합니다. 이 때문에 `urllib3`과 `idna`는 bump했지만 두 SDK는 major version 하나만큼 뒤처진 채 방치되었습니다.
    - **이전의 우려와 달리 두 major version은 충돌 없이 공존합니다.** `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**로 migration하지만, `mistralai`과 `google-genai`는 `httpx<1`에 남습니다. 그러나 이들은 서로 다른 distribution입니다. 실제 설치로 검증한 뒤 OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI라는 **7개 provider 경로를 처음부터 끝까지 테스트**했고, 각 출력에서 inline code와 link가 보존됨을 확인했습니다. “HTTP stack 두 개를 피한다”는 것은 선호 사항이지 blocker가 아니었으며, 측정으로 결론을 내렸습니다.
    - **`requirements.txt`은 실제 환경을 설명하지 못했습니다.** `google-auth`, `cryptography`, `opentelemetry` stack은 작업 venv에 설치되어 있었지만 선언된 적이 없었습니다. 따라서 새로 설치한 환경으로는 테스트된 환경을 재현할 수 없었습니다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`은 어떤 곳에서도 import되거나 요구되지 않았는데도 포함되어 있었으며, `mistralai` 1.x의 잔재였습니다. 파일은 직접 dependency만으로 구성된 venv의 완전한 closure로 다시 생성했습니다. 새 dependency 집합에서 `pip-audit`이 알려진 vulnerability를 하나도 보고하지 않았습니다.
    - **`.github/dependabot.yml`**(신규)은 pip과 github-actions의 주간 version update를 활성화합니다. minor와 patch는 하나의 PR로 묶습니다. patch bump마다 PR을 만들면 결국 무시되며, 소음은 업데이트의 적이기 때문입니다. **major는 각각 분리**되며 실제 호출을 통한 validation이 필요합니다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 지연을 프로젝트 판정에 드러냅니다. Dependabot은 제안할 뿐 보장하지 않으며 PR이 쌓일 수도 있습니다. major version 지연은 실패로, minor 지연은 경고로 처리합니다. 항상 빨간 gate는 결국 무시되기 때문입니다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 skip하고 **CI에서는 fail-closed**로 처리합니다. 실행되지 않은 검사는 성공이 아니기 때문입니다. 양방향으로 검증했습니다. 수정 전의 정확한 상태(`openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`)는 잡아내며 minor 지연에는 경고만 표시합니다.

  - **이 PR 검토에서 나온 수정 사항** — 5개 검토 agent가 diff를 철저히 조사했으며, 아래 항목은 모두 수정 전에 **측정을 통해 재현**되었습니다. 그중 2개는 이 버전의 앞선 변경에서 새로 도입된 regression이었습니다.
    - **수정된 회귀 — `_NEWS_CITATION_REGEX`에 지수적 백트래킹이 있었습니다.** 여러 문단 수정 과정에서 반복문 안에 `(?:[ \t]*$|[ \t]+.*)`이 도입되었습니다. `[ \t]+`과 `.*` 사이의 공백 분배가 모호하며, 이 모호성이 반복할 때마다 증폭되었습니다. 패턴과 일치하지 않는 `>   texte` 줄—완전히 유효한 Markdown 들여쓰기—에서 측정한 결과, **14줄에 2,589ms**가 걸렸지만 수정 후에는 0.04ms였으며, 줄이 하나 추가될 때마다 약 9배씩 증가했습니다. `--news` 모드에서는 길고 규격에 맞지 않는 blockquote 하나만으로도 원인을 파악할 수 없는 채 번역 작업이 timeout까지 멈출 수 있었습니다. 이제 반복문은 한 번에 전체 줄을 소비하므로(`\n^>(?![ \t]*—).*`), 각 반복에서 일치시킬 수 있는 방식이 하나뿐입니다. 실제 231개 문서 corpus에서 검증한 결과, 캡처 차이는 **0건**이었고 동일한 423개 인용문이 유지되었으며 여러 문단으로 구성된 14개 본문도 계속 확장되었습니다.
    - **두 provider flag를 동시에 지정하면 아무런 알림 없이 사용량 기반 요금이 청구되었습니다.** `--use_codex --use_mistral`이 허용되었습니다. `_select_provider_client`는 Mistral을 먼저 검사하고, `_resolve_provider`은 명시적 boolean을 우선하므로 둘 다 Mistral로 귀결되었습니다. 따라서 사용자는 구독 quota 사용을 요청했지만 아무런 경고 없이 사용량 기반 요금을 청구받았습니다. 이는 정확히 `--use_codex`이 방지하기 위해 존재하는 실패 방식입니다. 이제 여섯 provider flag 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경**: 이전까지 아무런 알림 없이 허용되던 두 provider를 결합한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 완료 gate는 probe가 실패해도 통과 상태가 되었습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개는 반환 코드를 전혀 확인하지 않은 채 ‘stdout을 캡처하고 비어 있으면 결론을 내리는’ 패턴을 따랐습니다. 예외가 발생하면(파일 이름 변경, `FileNotFoundError`) stderr에 기록되고 stdout은 빈 상태로 남아, 검사에서 ‘보고할 사항 없음’이라고 결론 내렸습니다. 이를 방지하려고 작성한 script 내부에서 ‘`exit 0`은 아무것도 증명하지 않는다’는 함정이 그대로 재현된 것입니다. 이제 `probe()` helper는 반환 코드 0과 종료 sentinel을 **모두** 요구하며, probe는 기준점 집합이 비어 있으면 결론을 내리지 않습니다. 빈 집합에 대한 assertion은 언제나 참이기 때문입니다. 실제로 위의 상호 배타적 그룹을 추가하면서 provider flag가 `*_group` 객체를 통하게 되었고, 기존 regex `parser\.add_argument\(`는 더 이상 이를 일치시키지 못했습니다. 그 결과 **21개 flag 중 6개**가 아무런 알림 없이 검사 범위에서 빠졌는데도 gate는 통과 상태였습니다.
    - **secret scan은 여섯 provider 중 네 개를 놓쳤습니다.** `[A-Za-z0-9]` class는 hyphen을 제외합니다. 따라서 `sk-proj-…`(현재 OpenAI 형식)와 `sk-ant-api03-…`는 두 번째 hyphen에서 끊겼고, `AIza…`은 검사 대상에 포함되지 않았습니다. 패턴을 확장하고 `.secrets.baseline`은 scan에서 제외했습니다. 또한 `.env` guard는 index만 보는 `git diff --cached`을 조회했습니다. 따라서 최악의 경우인 **이미 commit된** `.env`은 절대 나타나지 않았습니다. 이제 `git ls-files`을 조회합니다.
    - **Codex의 ‘token warm-up’은 실제 warm-up이 아니었습니다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`을 건드리지 않으며(mtime과 크기가 변경되지 않음), 도움말에도 ‘로그인 상태 표시’라고 나옵니다. 그런데도 주석에는 token을 ‘한 번, 순차적으로’ 갱신하여 일회용 rotating token의 동시 refresh 위험을 없앤다고 적혀 있었습니다. 명시된 보호 기능은 존재하지 않았습니다. 이제 주석은 코드가 실제로 하는 일을 설명하며, 실질적인 방어책은 여전히 `max_jobs=4`입니다. 또한 검사는 이전에 무시하던 `CODEX_BIN`을 준수합니다. `PATH`에 `codex`이 없는 환경에서는 ‘인증되지 않음’ 오류가 발생해 오해를 부르는 진단을 내렸습니다.
    - **`.env`이 subshell에서 source되었습니다.** `detect_provider`이 command substitution으로 호출되므로 export가 상위 shell에 전달되지 않았습니다. 그 결과 `.env`에 정의된 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`이 `main()` 내부의 읽기 작업에는 보이지 않았고, 올바른 구성에서도 ‘Grok binary를 찾을 수 없음’이라는 결론을 내렸습니다.
    - **동시 실행 수가 명시된 상한보다 50% 많았습니다.** guard가 README/CHANGELOG 쌍을 실행한 뒤에 배치되어 있었습니다. 측정된 최대치는 **`max_jobs=2`에서 3**이었습니다. 주간 quota가 Chat/Imagine/Voice와 공유되고 측정할 수도 없는 Grok에서는 script가 스스로 정한 상한조차 지켜지지 않은 것입니다. 한편 최종 개수는 표시만 하고 28과 비교하지 않았으므로, 파일이 누락되어도 감지되지 않았습니다.
    - **Grok 출력 계약: 이제 `stopReason`이 없으면 실패로 처리합니다.** 명시된 계약에서는 `end_turn`을 요구하지만, 코드는 ‘`end_turn` **또는 없음**’을 적용했습니다. 해당 field가 없는 payload나 CLI 업데이트로 field 이름이 변경된 payload는 guard를 아무런 알림 없이 no-op으로 만들었습니다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류되지 않으며, 이는 turn budget이 소진된 상태이므로 재시도해도 같은 결과를 내면서 90초의 대기 시간만 발생합니다. `quota`도 rate limit marker에서 제외했습니다. `_codex_is_rate_limited`의 docstring에는 이미 그 이유가 명시되어 있었지만 Grok에는 적용되지 않았습니다.
    - **Gemini cascade를 모델별로 memoization합니다.** 기본 모델이 `minimal`을 거부하는데도 segment마다 여기서 다시 시작했습니다. 정상 경로에서 segment마다 400 응답을 한 차례씩 불필요하게 기다리고 같은 경고를 다시 출력했습니다. 경고가 수백 번 반복되면 더 이상 읽히지 않으며, 그렇게 경고가 다른 문제를 가리는 장막이 됩니다.
    - **기타**: CI의 거부 메시지가 Codex용으로 hard-code되어 `--use_grok_cli` 사용자를 `XAI_API_KEY`이 아닌 `OPENAI_API_KEY`으로 안내했습니다. `provider.capitalize()`은 ‘Grok_cli’와 ‘Openai’를 표시했습니다. subprocess 기반 계층의 주석은 ‘shim’을 두 CLI에 모두 일반화했지만 Grok binary는 native ELF입니다. 올바른 근거는 ‘자체 subprocess를 생성하는 agent’입니다. `subprocess`에 대한 12개 SAST finding은 근거와 함께 `# nosec` / `# nosemgrep`로 표시했습니다. `shell=True`이 없는 list 형식이어서 injection이 불가능하고 문서 내용은 절대 argv를 거치지 않습니다.
    - **이제 agent subprocess에는 어떤 secret도 전달되지 않습니다.** 이름 기반 deny-list는 **과금** invariant만 보호했습니다. 즉 Codex에는 `OPENAI_API_KEY`이, Grok에는 `XAI_API_KEY`이 전달되지 않도록 했습니다. 측정 결과 **그 밖의 secret 7개**가 여전히 모든 subprocess에 전달되었습니다. Anthropic, Mistral, Google, Gemini key와 다른 CLI의 key, 그리고 secret은 아니지만 traffic을 재지정하는 `OPENAI_BASE_URL`입니다. 그런데 이 두 CLI는 **agent**이며, Grok agent는 많은 Linux 환경에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 filtering은 이름 목록이 아닌 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)을 기준으로 수행합니다. 따라서 코드가 알지 못하더라도 사용자가 `.env`에 추가한 변수까지 포함합니다. CLI에는 이들 변수가 전혀 필요하지 않습니다. 인증 정보는 `~/.codex`과 `~/.grok`에 존재하며 환경에는 절대 들어가지 않습니다. 강화된 환경에서 두 provider 각각을 통해 **실제 번역을 성공적으로 완료**하여 검증했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`의 21개 test가 provider flag의 상호 배타성, `stopReason` 계약, news regex의 선형성, CI 거부 메시지, Gemini memoization, subprocess 환경에서 모든 secret이 제거되는지를 고정합니다. 마지막 assertion은 **generic**하므로 어떤 list에도 이름이 없는 key에도 실패합니다. 반면 기존 제거 test는 자체 상수를 그대로 비춘 형태여서 자체 loop의 고장 외에는 아무것도 감지할 수 없었습니다. 전체 test suite는 **311개 test**입니다.

  - **새로운 Grok provider 2개**: `--use_grok`(xAI API, key `XAI_API_KEY`, 사용량 기반 과금)과 `--use_grok_cli`의 공식 Grok Build CLI(Grok 구독에서 차감되며 `--use_codex`과 같은 원리)입니다.
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`을 그대로 재사용하고 `base_url`만 변경합니다. 필요한 수정은 하나뿐이었으며 모두에게 이점이 있습니다. 이제 `finish_reason`은 OpenAI가 `stop`을 내보내는 지점에서 xAI가 내보내는 형식인 `end_turn`을 허용합니다. 모델은 `grok-4.6`(고품질)과 `grok-4.3`(경제형)입니다. 참고로 Grok의 경제형 모델도 이 저장소에서 가장 비쌉니다. 100만 token당 $1.25/$2.50으로, `mistral-small-latest`의 $0.15/$0.60과 비교됩니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택하는 것입니다.
    - **CLI 모드**: Codex를 기반으로 하되 실제 환경에서 요구되는 네 가지 차이점이 있습니다. prompt는 파일로 전달되고(`--prompt-file`, CLI가 stdin을 읽지 않으며 segment를 argv로 전달하면 `ps`에 노출됨), 출력은 stdout의 단일 JSON 객체이며(JSONL도 `-o` 파일도 아님), 구독에서는 `grok-4.6`과 `grok-4.5`만 제공되고, sandbox를 적용할 수 없습니다(아래 참조). subprocess 실행은 `_codex_run_process`에서 Codex와 공통화했으며, 이미 test를 거친 Codex provider의 나머지 부분은 변경하지 않았습니다.
    - **측정 결과 `exit 0`은 아무것도 증명하지 않습니다**: 인증되지 않은 상태에서도 CLI는 **stdout**에 `{"type":"error","message":"Not signed in."}`을 기록하고 반환 코드 **0**으로 종료합니다. 거부되거나 turn 한도를 초과한 경우에도 동일하게 동작합니다. 따라서 출력 계약은 반환 코드 0, 오류 payload 없음, `stopReason == end_turn`, 비어 있지 않은 text라는 네 조건을 동시에 요구합니다. preflight도 같은 논리를 따릅니다. `grok models`는 연결이 끊긴 상태에서도 0으로 종료하며, stdout에 ‘not authenticated’가 있는지를 통해서만 결론을 내릴 수 있습니다.
    - **격리: 비대칭성을 의도적으로 채택하고 문서화했습니다.** Codex가 `--sandbox read-only`에서 실행되는 것과 달리, 최근의 여러 Linux 환경에서는 서로 독립적이며 `sudo` 없이는 우회할 수 없는 두 가지 system 원인 때문에 Grok sandbox를 적용할 수 없습니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`이 `0700`일 때 container runtime socket의 deny-list가 실패합니다. resolver는 `ErrorKind::NotFound`만 처리하며 EACCES는 치명적 오류가 됩니다. 핵심 함정은 적용할 수 없는 **내장** profile이 아무런 알림 없이 **비격리 상태로 실행**된다는 점입니다. 따라서 script는 기본적으로 어떤 profile도 요청하지 않고, 절대 아무런 알림 없이 fallback하지 않으며 stderr에 경고를 출력합니다. 보호는 catch-all `*`을 포함한 CLI의 `--deny` 규칙에 의존합니다. 이는 측정 결과 _fail-closed_로 동작하는 유일한 계층입니다. 알 수 없는 prefix의 규칙이 있으면 시작이 거부됩니다. `GROK_TRANSLATE_SANDBOX=read-only`으로 이를 필수화할 수 있으며, 해당 환경에서 준수할 수 없으면 시작에 실패합니다.
    - **보호 장치**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`은 subprocess 환경에서 제거됩니다. key가 있으면 사용량 기반 과금으로 전환되고, 상속된 `GROK_SANDBOX`은 적용할 수 없는 profile을 오해의 소지가 있는 메시지와 함께 강제합니다. MCP/hooks/skills/agents switch는 비활성화되며, `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI에서의 거부, process group을 종료하는 timeout, rate limit back-off를 적용합니다. `--max-turns`은 1이 아니라 6으로 설정합니다. counter는 tool turn 이후 증가하므로 1로 설정하면 출력이 잘립니다.
    - **Quota**: Grok pool은 주 단위이며 **Chat, Imagine, Voice와 공유**되고, 이를 표시하는 명령이 없습니다. `account/rateLimits/read`으로 사용량을 수치화할 수 있는 Codex와 대조적입니다. 따라서 `regen_translations.sh`은 동시 실행 수를 2로 제한하고 이를 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`에 24개 test가 추가되었습니다. 전체 test suite는 **290개 test**입니다.
  - **수정된 버그 — 여러 문단으로 구성된 영어 인용문이 일부만 보호되었습니다(`--news` 모드)**: `_NEWS_CITATION_REGEX`은 인용문 본문으로 **연속된** `>` 줄만 허용했습니다. 인용문이 빈 `>` 줄로 구분된 여러 문단에 걸쳐 있으면 마지막 문단만 캡처되어 placeholder로 대체되고, 앞 문단들은 LLM으로 전달되어 번역된 상태로 돌아왔습니다. 이는 `--news`이 보장하려는 것과 정확히 반대되는 동작입니다. 이제 반복문은 내부의 빈 `>` 줄을 허용하고 non-greedy 방식으로 동작하여, 처음 만나는 빈 줄이 아니라 italic 줄 앞의 빈 `>`에서 멈춥니다.
    - **실제 영향 범위 측정**: 실제 198개 문서 corpus에서 419개 인용문 중 11개가 영향을 받았습니다. 회귀는 없었습니다. 새 regex는 정확히 같은 수의 인용문을 캡처하며 여러 문단으로 구성된 본문만 확장되었습니다(408개 본문은 동일하고 11개는 확장됨). 또한 `> — …` attribution 줄은 여전히 본문에 포함될 수 없습니다(lookahead 유지).
    - **End-to-end 증명**: 69KB 문서를 ja/ar로 번역했습니다. 이전에는 인용문의 첫 문단이 일본어로 `> GLM-5.3がオープンウェイト化。`이 되고 아랍어에서도 마찬가지로 번역되었지만, 이제는 `> GLM-5.3 is now open-weight.`으로 유지됩니다. 영어 인용문 줄 수는 원문과 같은 10줄로 9줄에서 복원됩니다.
    - 참고로 이 결함은 인용문이 완전한지는 확인하지 않고 존재 여부만 확인하는 downstream validator에서는 감지되지 않았습니다.
  - **기본 provider에서 측정된 비용 절감**: `_openai_extra_kwargs`은 `--eco`인 경우를 포함하여 모델 이름이 `gpt-5`로 시작하면 항상 `reasoning_effort="medium"`을 전송했습니다. 열 단어 문장을 번역하기 위해 `gpt-5.4-mini`에서 측정한 결과, `medium`은 reasoning token 45개와 출력 token 65개를 사용했고 `none`은 각각 0개와 14개를 사용했습니다. 번역에는 reasoning이 아무런 이점도 없는데 모든 파일의 모든 segment에서 비용이 발생했습니다. 이제 기본값은 `--eco`에서는 `none`이고 그 외에는 `medium`입니다. CLI에서 명시적으로 전달한 값은 계속 우선합니다. 이제 `--reasoning_effort`은 `low`/`medium`/`high` 외에도 `none`과 `xhigh`을 허용합니다. 모든 모델이 이들 값을 전부 허용하는 것은 아닙니다. 예를 들어 `minimal`은 `gpt-5.4-mini`에서 거부됩니다. 기존의 parameter 없는 retry가 이 경우를 처리합니다.
  - **SDK 업데이트 및 Gemini migration**: `google-generativeai`(지원이 2025-11-30에 종료되었고 저장소도 archive됨)을 통합 SDK **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 다음 `client.models.generate_content(model=, contents=, config=)`을 사용하며, system prompt는 segment에 연결하지 않고 `system_instruction`으로 전달합니다. `mistralai`는 **2.9.4**로 업데이트했습니다. import는 `from mistralai.client import Mistral`이 되며, 이전 것은 `ImportError`을 발생시킵니다. 이는 wheel에서 검증했습니다. `anthropic`는 **0.125.0**, `openai`은 **2.54.0**으로 업데이트했습니다. 두 HTTP stack이 venv에 공존하지 않도록 `httpx2` 전환 전의 마지막 version을 사용했습니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5의 제한도 해제했습니다.
  - **문서가 아니라 실제 test로 발견한 회귀 2건**:
    - `anthropic` ≥ 1.0은 `max_tokens`에서 10분을 넘길 것으로 예상되는 non-streaming 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 보호 장치는 0.34.2에는 없었으며 `max_tokens=32768`을 사용하는 모든 Claude 호출을 중단시켰습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정했습니다. 전체 응답만 사용하는 호출을 위해 streaming으로 전환하지 않아도 됩니다.
    - `thinking_level="minimal"`은 Gemini catalog 일부에서만 허용됩니다. `gemini-3.1-flash-lite`은 지원하지만 `gemini-3.7-flash`와 `gemini-3.1-pro-preview`은 400으로 거부합니다. 따라서 OpenAI에 이미 존재하는 fallback을 본떠 `_gemini_generate_with_fallback`, 즉 `minimal` → `low` → thinking_config 없음의 cascade를 구현했습니다. 최적화 parameter 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델 갱신**, 각각 실제 호출로 검증했습니다. OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%), Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜가 없는 canonical ID), Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(stable version이며 `3.5-flash-lite`보다 저렴함)입니다.
 Mistral은 변경 없이 유지되며, `mistral-large-latest`이 네 모델 중 여전히 가성비가 가장 좋습니다. 참고: `gemini-3.1-pro-preview`보다 최신인 Pro급 Gemini 모델은 없습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 라인업은 전부 Flash 전용입니다.
  - **Gemini 전환 전 측정한 A/B 테스트**: `README.md`를 `gemini-3.1-pro-preview`과 `gemini-3.7-flash`로 각각 일본어로 번역했습니다. 구조는 완전히 동일했으며(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존), 소요 시간은 **48초 대비 8초**였습니다. 번역이나 비라틴 문자 체계에서 이 두 모델을 비교한 공개 벤치마크가 없으므로, 이 테스트가 없었다면 전환은 단순한 추정에 근거했을 것입니다.
  - **Claude 응답 블록 필터링**: `_call_claude`은 유형을 필터링하지 않고 `block.text for block in response.content`을 수행했습니다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 중간에 삽입하는데, 이 블록은 `.text`가 아니라 `.thinking`을 노출합니다. 따라서 첫 번째 세그먼트에서 불투명한 `AttributeError` 때문에 번역이 중단될 수 있었습니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result` 블록은 제외되며(텍스트를 포함한 알 수 없는 유형을 허용할 수 있도록 부정 목록 사용), 텍스트 블록이 하나도 없는 응답은 명시적인 오류를 발생시킵니다. 호출할 때마다 `thinking={"type": "disabled"}`이 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 지원 종료일이 지난 모델을 삭제했습니다(`magistral-*` 제품군은 2026-07-31, `gemini-2.0-*`은 2026-06-01, `gemini-3-pro-preview`는 2026-03-09에 지원 종료, 그 외 `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`). 한도 수정: Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1,000,000 → **1,048,576**(실제 입력 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 제품군을 추가했습니다. 참고: `translate()`이 세그먼트 분할을 `min(16000, limite)`으로 제한하므로, 이 한도들은 여전히 참고용입니다.

  - **`--use_codex` Provider**: 사용량 기반으로 과금되는 API를 호출하는 대신, 비대화형 모드에서 공식 Codex CLI(`codex exec`)를 구동하는 다섯 번째 Provider입니다. 번역 사용량은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. 이는 OpenAI가 이 용도로 문서화한 유일한 방법입니다. 요금제별 제공 기능 표에는 “Codex SDK, `codex exec`, and scriptable workflows”가 Plus/Pro/Business/Enterprise에서 제공된다고 명시되어 있으며, `~/.codex/auth.json`의 토큰으로는 API Platform 호출을 인증할 수 없습니다. 또한 이 스크립트는 해당 토큰을 절대 읽지 않으며, 인증과 갱신은 계속 CLI가 관리합니다.
  - **npm뿐 아니라 pip로도 설치할 수 있는 Codex 바이너리**: `_resolve_codex_binary()`은 `CODEX_BIN`, 이어서 `PATH`, 마지막으로 OpenAI가 배포하는 공식 Python 패키지 **`openai-codex-cli-bin`**(`openai-codex` SDK의 의존성)에서 바이너리를 찾습니다. 따라서 Python 프로젝트에서 `--use_codex`을 사용하기 위해 더 이상 전역 npm 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가하지 않았습니다. 바이너리 크기가 약 250MB이므로 선택적 Provider를 위해 모든 사용자에게 설치를 강제하게 되기 때문입니다. 전체 과정을 검증했습니다. `codex`이 `PATH`에 없는 상태에서도 패키지에 포함된 바이너리를 찾아 6초 만에 전체 번역을 완료합니다.
  - **“구독 모드” 보장**: 하위 프로세스 환경에서 `OPENAI_API_KEY`과 `CODEX_API_KEY`을 제거합니다. 이 보호 장치가 없으면 `.env`에 존재하는 키로 인해 아무런 표시 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 이는 바로 이 Provider가 방지하려는 상황입니다.
  - **테스트로 차단한 CLI 함정**:
    - `codex exec`은 프롬프트가 인수로 전달되더라도 stdin을 **읽습니다**. stdin을 닫지 않으면 명령은 모델을 한 번도 호출하지 않은 채 타임아웃까지 대기합니다(재현 결과: 180초 후 exit 124, 0바이트). 따라서 `communicate(input=...)`은 필수입니다.
    - npm으로 설치한 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 이 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 후에도 살아남아 할당량을 계속 소모할 수 있습니다. 이 때문에 `Popen(start_new_session=True)`과 `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`을 내보내고도 종료 코드 0으로 끝날 수 있습니다. 반환 코드뿐 아니라 JSONL 출력(`--json`)도 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **Rate limit 발생 시 back-off**: CLI에는 내부 retry가 구현되어 있지 않습니다(`max_retries = 0`). 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. “quota”라는 단어는 복구 가능한 429뿐 아니라 영구적인 `insufficient_quota`에도 나타나기 때문입니다.
  - **CI 보호 장치**: `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 `--use_codex`을 거부합니다. 구독 인증은 공유 runner용이 아니며, OpenAI도 공개 저장소에서 이 workflow를 명시적으로 권장하지 않습니다.
  - **모델**: `gpt-5.6-sol`(품질)과 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 제품군은 CLI와 API Platform에서 공통으로 제공되지만, ChatGPT 계정이 모든 모델을 사용할 수 있는 것은 아닙니다. allowlist는 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 지정하면 경고가 발생합니다. Plus 요금제에서 Luna는 5시간 단위 기간마다 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개를 제공합니다. 따라서 모든 일괄 처리에는 `--eco` 모드를 권장합니다.
  - **수정된 버그 — 완전히 성공했는데도 `regen_translations.sh`이 오류로 종료됨**: `trap ... EXIT`이 `main()`의 `local` 변수인 `failed_log`을 참조했지만, trap이 실행될 때는 이 변수가 더 이상 존재하지 않았습니다. `set -u`에서 이로 인해 `failed_log: unbound variable`이 발생하여 28개 번역이 모두 올바른데도 스크립트가 종료 코드 1로 끝났습니다. 그 결과 재생성 직후이자 가장 비용이 많이 드는 단계에서 `release.sh --auto`(`set -e`)이 중단될 수 있었습니다. 변수를 전역으로 바꾸고 trap이 변수의 존재 여부를 검사하도록 했습니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 종료 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: `regen_translations.sh`의 새로운 환경 변수로, Provider의 기본값보다 특정 모델을 우선 적용합니다. 예를 들어 처리량 중심 모델인 `--eco` 대신 구독 할당량의 고급 모델로 재생성하려면 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 사용할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때 `REGEN_PROVIDER=codex`을 사용할 수 있습니다. 사용자 모르게 구독 할당량을 소모하지 않도록 자동 감지는 절대 하지 않습니다. 병렬 처리를 시작하기 전에 토큰을 순차적으로 한 번 갱신합니다. Codex refresh는 회전식 일회용이므로 동시 실행 job이 `codex login` session을 무효화할 수 있기 때문입니다. 동시 실행 수는 4로 제한합니다.
  - **관련 refactor**: 전체 호출 체인에 네 번째 boolean을 전달하는 대신 Provider 이름을 반환하는 `_resolve_provider()`을 사용하여 `_dispatch_provider_call`의 매개변수를 8개에서 6개로 줄였습니다. 최소한의 `Namespace`으로 `translate(..., use_mistral=True)`을 호출하는 테스트를 유지하기 위해 명시적 boolean은 계속 `args`보다 우선합니다.
  - **테스트**: 새로운 파일 `tests/test_codex_provider.py`에 48개 테스트를 추가하여 argv, 정제된 환경, 서문 방지 계약, 조용한 실패, timeout/killpg, back-off, preflight, Provider 결정, Gemini 추론 cascade, Claude 블록 필터링, 여러 문단으로 구성된 뉴스 인용을 다룹니다. 전체 제품군은 290개 테스트입니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 참조 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 25줄, HTML 링크 13개, 이미지 13개, URL 19개, 코드 블록은 문자 단위까지 동일, placeholder 잔여물 0개). `--news` 모드에서 69KB 분량의 뉴스 기사를 처리했을 때 `gpt-5.6-luna`과 `gpt-5.6-sol` 출력 모두 en/ja/ar에 대한 후속 애플리케이션 validator를 통과했습니다. `account/rateLimits/read`로 측정한 사용량은 `--eco` 모드에서 카운터의 반올림 임계값 미만(5시간 단위 기간의 0%)으로 유지되었습니다.

- **1.9.2** 중첩 괄호 또는 프랑스어 접두사가 있는 뉴스 출처 URL 추출 수정(2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`의 출처 URL 추출은 regex `re.search(r"\((.+?)\)", attribution)`(괄호 사이를 lazy capture)을 사용했습니다. `(relayé par [@user sur X](https://x.com/.../123))`과 같은 출처 표기에서는 괄호가 중첩되어(`(`의 바깥 괄호 + Markdown link의 `]()`), 처음 만난 `)`에서 캡처가 중단되었습니다. 그 결과 프랑스어 접두사가 포함되고 잘린 문자열인 `relayé par [@user sur X](https://x.com/.../123`(`)` 끝부분 없음)이 생성되었습니다. 이 때문에 `_validate_news_post`가 번역된 출력에서 이 문자열을 찾다가 항상 실패했습니다. 원인은 두 가지로, `)`이 잘렸고 “relayé par”가 `relayed by`/`weitergeleitet von`/…로 번역되었기 때문입니다. low → medium → high → gpt-5.5 전체 cascade가 통과할 수 없었습니다.
  - **수정**: regex를 `re.search(r"\]\(([^)]+)\)", attribution)`으로 변경했습니다. Markdown link의 `](url)`을 구체적으로 대상으로 삼아 **순수 URL만** 캡처하므로 프랑스어 접두사나 잘림이 없으며, 번역 중에는 `#URL{N}#` placeholder로 불변성이 보장됩니다. 문제가 된 다음 두 패턴을 모두 안정적으로 처리합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥 괄호가 없는 프랑스어 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 2개를 새로 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그를 그대로 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`이 포함된 변형)
  - **검증 공백**: `check-editorial-coverage.py`은 편집 구문을 검증하지만 translator로 번역할 수 있는지는 검증하지 않습니다. 향후 개선 사항(v1.9.2 범위 밖)으로, 게시 **전에** 위험한 패턴을 감지하도록 dry-run에서 출처 추출을 시뮬레이션하는 검사를 추가할 수 있습니다.

- **1.9.1** 번역 marker 안내문의 CTA label i18n 수정(2026-05-10):

  - **수정된 버그**: 번역 파일 상단의 marker 배너에 있는 CTA 링크 label `[Voir le projet sur GitHub ↗]`이 `target_lang`을 따르지 않고 모든 대상 언어에서 **프랑스어**로 남아 있었습니다. URL과 저장소 slug를 보존하기 위해 Python 측에서 조립하므로 LLM은 이 내용을 전혀 보지 못하며, 번역 단계에서도 이를 수정할 수 없었습니다. v1.9에서 `marker` 형식을 추가한 이후 발생한 조용한 회귀였습니다.
  - **수정**: 15개 언어를 각 현지화 label에 매핑하는 새로운 상수 `_VIEW_PROJECT_LABELS`을 추가했습니다. 이제 `_translation_note_invariants(target_lang)`와 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달합니다. 언어를 알 수 없을 때는 `fr`으로 fallback합니다(KeyError 방지).
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 조정했습니다(target_lang `ja` → 예상 일본어 label). 테스트 2개를 새로 추가했습니다. `test_source_link_label_localized_per_target_lang`은 라틴 문자, 표의 문자, abjad를 포괄하는 7개 언어로 매개변수화했으며, 다른 하나는 `test_source_link_label_falls_back_to_french_for_unknown_target`입니다. `test_translation_note_position.py`의 테스트는 총 40개로 늘었습니다(기존 38개).
  - **이전 버전 호환성**: 기본값이 있는 signature `target_lang="fr"`을 사용하므로, `args.target_lang`이 없는 외부 프로그래밍 호출자도 수정 없이 계속 작동합니다.
- **1.9** 무응답 실패 수정 + 종합 품질 도구 체계 + 다중 위치 번역 안내문 (2026-05-07):
  - **다중 위치 번역 안내문 + "embed card" 마커 형식**:
    - 새로운 CLI 옵션 추가(기본값은 변경되지 않음 → **호환성 유지**):
      - `--note_position {top,bottom,both}`(기본값: `bottom`): 번역된 파일의 상단, 하단 또는 양쪽 모두에 안내문을 배치합니다.
      - `--note_format {legacy,marker}`(기본값: `legacy`):
        - `legacy`은 v1.8의 동작(굵은 문단 `**…**`)을 **바이트 단위까지** 정확히 재현합니다.
        - `marker`은 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)와 함께 "GitHub 저장소 embed card" 형태로 렌더링되도록 구성된 **3개 문단의 blockquote**를 출력합니다. 여기에는 inline code 형식의 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM이 번역한 설명, 보이는 화살표가 포함된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 들어갑니다. 빌드 시 remark 플러그인에서 활용할 수 있습니다(jls42.org 블로그 → `remark-translation-banner` 플러그인 참조).
    - **LLM에 절대 전송되지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문장을 번역한 후 Python 측에서 조합됩니다. LLM은 `ai-powered-markdown-translator` slug나 `https://github.com/jls42/...`을 절대 보지 않으므로 renderer, 대소문자 또는 scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter를 닫는 `---` 블록 **뒤에** 안내문이 삽입됩니다(Astro Content Collections / gray-matter 안전성 보장). `_split_frontmatter` helper는 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 유지합니다. 닫는 fence 없이 열린 frontmatter에는 **`RuntimeError`을 발생시켜**, 잘못된 위치에 안내문이 삽입된 파일을 쓰는 대신 해당 파일이 `failed_files`에 표시되도록 합니다.
    - **Whitelist 기반 모델 sanitizer**: `_sanitize_model`은 `[A-Za-z0-9._:/-]` 이외의 모든 문자를 `_`으로 바꾸며, 결과가 비어 있으면 `unknown`을 사용합니다. Astro remark 플러그인 측 validator와 일치하도록 하며 marker 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 refactor**: `_append_translation_note`(단일 거대 함수) → 순수 helper 7개(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). Builder와 composer를 분리했습니다(builder는 구분자 없는 순수 block을 반환하고 composer는 위치에 따라 `\n\n`을 적용). production과 source helper는 동일한 3문단 assembler를 공유합니다.
    - **빈 줄을 보존하는 `_quote_lines`**: 각 줄 앞에 `> `을 붙이고 빈 줄은 `>`만 있는 줄로 변환합니다. 이를 통해 mdast가 blockquote를 줄바꿈이 포함된 단일 문단이 아니라 서로 구분된 3개 문단(제목 / 설명 / 링크)으로 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 유지한 문단 수에 따라 동작합니다(3개 = 완전한 card 형식, 2개 = 문장 + 링크, 1개 = fallback). 1문단 fallback은 Markdown 링크 `](`이 감지되면 더 이상 **`**...**`으로 감싸지 않습니다**(링크 주위의 `<strong>`은 렌더링이 불안정함).
    - **상위 호환성**: `_compose_with_notes` 측의 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")` — 이러한 속성이 없는 Namespace(기존 테스트와 외부 프로그래밍 방식 호출)도 수정 없이 계속 작동합니다.
  - **긴 번역에서 발생하는 무응답 실패 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 validation 적용: 결정론적 계층(원문의 verbatim 발췌문 재검출) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에서 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k segment에서 잠재적인 truncation 방지, FR→JA/ZH/KO/AR/HI 교차 문자 체계 변환 여유 확보)
    - Heading 인식 segmentation: segment 후반부의 H2/H3에 우선순위를 부여하여 각 segment가 완전한 의미 단위 section으로 시작하도록 함
    - 오류를 0이 아닌 exit code까지 전파: `translate_markdown_file`이 typed status `success` / `failure` / `skipped`을 반환하고, 하나 이상의 파일이 실패하면 `main()`에서 `sys.exit(1)` 처리(single-file 및 batch)
    - 모든 provider에 empty-content guard 적용, source/output sanity ratio 적용(500자 이상에서 5% 미만이면 거부), code placeholder validation(`#CODEBLOCK`/`#INLINECODE`), LLM 처리 후 normalization(구분자/링크가 heading에 붙는 문제), `BadRequestError`에서 `reasoning_effort` 없이 retry
    - `langdetect==1.0.9` dependency 추가
  - **Pre-commit 품질 도구 체계**("EurekAI 완전형", hook 14개):
    - Pre-commit: ruff(lint+format), shellcheck, prettier(md/yaml/json), detect-secrets(API key 4개 보호), Lizard(CCN ≤ 12), pre-commit-hooks v5(whitespace, EOF, large-files, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `./venv/bin/python`을 사용하는 `scripts/`의 로컬 wrapper
    - `scripts/audit_verdict.py`: unittest 11개가 포함된 pip-audit JSON parser로, jls42-astro parser의 Python port
    - 초기 ruff 위반 7건 수정: B904(raise from) ×2, B007(unused dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard에서 `translate.py`을 일시적으로 제외(CCN 21~47인 함수 4개, refactor 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 포괄적 coverage**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): push 및 pull-request마다 분석하고 `coverage.xml`을 통해 coverage 측정
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` stdlib): 무응답 실패 오류 chain의 6개 연결 단계를 다룸
    - `tests/test_orchestration.py`(+79개 테스트): `translate.py`의 orchestration 계층을 다룸(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return branch)
    - `scripts/tests/test_audit_verdict.py`: `main()`(stdin/stdout)과 `if __name__ == "__main__"` block을 subprocess로 coverage
    - **새 코드의 coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 matrix(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 여러 줄 prefix 처리, 바이트 단위 상위 호환성(golden literal), sanitizer, frontmatter split(닫히지 않은 fence에서의 raise 포함), 3문단 형식, 2문단 fallback, 1문단 + Markdown 링크 guard 및 제목과 URL이 LLM에 절대 전송되지 않는지 assert하는 핵심 safeguard `TestLLMPayloadExcludesInvariants`을 다룹니다. **테스트 190개 통과**, regression 0건.
  - 문서: badge가 포함된 `README.md`(프랑스어 + 번역 14개), `CLAUDE.md`(pre-commit workflow + 상세 CI watch), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 bump(2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token limit 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder로 영어 인용문 보호, `LANG_FLAGS` mapping(15개 언어), 대상 언어별 flag 처리
  - 복원 전 news placeholder validation(회귀 문제: LLM이 placeholder를 삭제하면 인용문 없는 출력이 조용히 생성되었음)
  - `regen_translations.sh` script를 이식 가능하게 개선(절대 경로 사용, pwd dependency 제거)
  - README/CHANGELOG의 language bar에 프랑스어 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원래 파일명을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **Inline code 보존**: 이제 번역 중 backtick(`` `...` ``)을 보호
  - System prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - Template variable `{variable}` 보호
    - 요청하지 않은 번역자 주석 금지
  - 파일 364개에서 성공적으로 테스트(jls42.org 블로그 migration)
- **1.6** 새로운 기능:
  - 번역용 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 탐색하지 않고 단일 파일 번역(`--file`)
  - 새롭고 단순한 naming pattern: `{base}-{lang}.md`
  - 모델 이름을 포함하는 기존 형식을 유지하는 `--include_model` 옵션
  - 목록에 없는 모델을 기본 token limit(128k)로 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`으로 업데이트.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`으로 업데이트.
  - **번역 prompt 최적화:**
    - 직접 번역 및 번역 안내문을 위한 prompt의 명확성과 효율성을 높였으며, metadata와 특정 formatting 요소 보존에 관한 상세 지침을 포함했습니다.
  - **코드 refactor:**
    - Mistral AI client 초기화를 위해 `MistralClient`을 `Mistral` class로 교체했습니다.
    - 가독성과 유지보수성을 높이기 위해 import를 재구성했습니다.
    - 번역 중 원래 formatting을 보존하도록 텍스트 segmentation과 code block 처리를 개선했습니다.
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 바꾸어(예: `f"{base}-{args.target_lang}-{args.model}.md"`) 번역 파일을 더 쉽게 정리하고 찾을 수 있도록 했습니다.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 코드를 정리했습니다.
    - Script의 구조와 가독성을 높이기 위한 소규모 조정을 적용했습니다.
- **1.4** 새로운 기능:
  - 번역용 Anthropic Claude API 지원
  - 명확성과 효율성을 높이기 위한 prompt 최적화
  - 코드 유지보수성을 높이기 위한 소규모 조정
- **1.3** 개선 사항 및 새로운 기능:
  - Code block 처리 개선
  - 출력 파일 관리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 모델과 언어의 순서 변경
- **1.2** Changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**gpt-5.6-sol로 프랑스어에서 한국어로 번역된 기사.**
