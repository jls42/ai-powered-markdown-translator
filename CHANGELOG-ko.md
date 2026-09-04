### 변경 이력

🌍 [프랑스어](CHANGELOG.md) | [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.12.0** Provider `--use_opencode`: 오픈 소스 에이전트 OpenCode를 사용자가 선택한 제공자로 연결 — 로컬 모델, 계정 없이 무료로 사용할 수 있는 모델, 구독 또는 키(2026-09-04):

  - **앞선 일곱 경로와는 성격이 다른 여덟 번째 provider 경로입니다.** [OpenCode](https://opencode.ai)(MIT)는 모델 제공자가 아니라 사용자가 OpenCode 자체에 구성해 둔 대상으로 연결하는 _라우터_입니다. 대상은 API 키, 구독(GitHub Copilot, ChatGPT, SuperGrok), **계정 없이** 무료 모델을 제공하는 OpenCode Zen 게이트웨이 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp)일 수 있습니다. 스크립트는 Codex 및 Grok과 마찬가지로 `opencode run`을 비대화형 모드로 제어하며, 동일한 하위 프로세스 기반 구조를 재사용합니다. 즉, 독립된 프로세스 그룹, timeout 시 `SIGTERM` 후 `SIGKILL`, 항상 닫힌 stdin, 정리된 환경을 사용합니다. **두 차례의 실제 번역**으로 검증했습니다. `opencode/mimo-v2.5-free`를 통해 이 README 전체를 영어로 번역한 작업은 49초가 걸렸고 단 한 번의 패스로 완료되었으며, 원본 파일과 구조가 같았습니다(제목 32개, 코드 닫기 26개, 링크 18개, URL 37개, 표 행 37개, inline code 135개). 또한 `ollama/qwen2.5:7b`를 통해 테스트 파일을 키 없이 로컬에서 번역했습니다.

  - **`--model provider/modèle`은 필수이며, 이는 의도적인 선택입니다.** `--model`이 없으면 OpenCode는 자체 기본값으로 돌아가며, 새로 설치한 환경에서 그 기본값은 대화 내용이 훈련에 사용될 수 있는 무료 « stealth » 모델 `opencode/big-pickle`입니다. 실제로 측정했을 때 응답한 모델도 이것이었습니다. 사용자 대신 이를 조용히 선택하는 것은 이 저장소가 추적하는 바로 그 보이지 않는 전환에 해당합니다. 따라서 오류 메시지는 모델을 나열하는 명령(`opencode models`)과 세 가지 예시(로컬, 무료, 구독)를 알려 줍니다. `--eco`은 아무 효과가 없으며, 그 사실도 명시합니다. `--reasoning_effort`은 명시적으로 요청한 경우에만 OpenCode의 `--variant`로 그대로 전달됩니다.

  - **격리는 가정한 것이 아니라 측정한 것입니다.** inline 구성(`OPENCODE_CONFIG_CONTENT`, OpenCode 병합 순서에서 마지막이므로 사용자의 구성을 대체하지 않으면서 우선 적용됨)은 모든 도구가 거부된(`permission: {"*": "deny"}`) `aipmt` 에이전트를 정의합니다. 레지스트리는 더 이상 모델에 도구를 제안하지도 않으며, 모델에 « 파일을 나열하고 `id`을 실행하라 »고 지시하면 도구가 없다고 응답합니다. 세션 공유는 비활성화하고 외부 plugins는 제외하며(`--pure`), `--auto`은 절대 사용하지 않고, 비어 있는 일회용 작업 디렉터리를 사용합니다. 두 가지 은밀한 주입을 측정해 차단했습니다. `OPENCODE_DISABLE_CLAUDE_CODE`가 없으면 사용자의 `~/.claude/CLAUDE.md`이 **모든** prompt에 들어갑니다(단순한 « 안녕하세요 »의 입력이 186 tokens가 아니라 515 tokens). `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 디렉터리의 `AGENTS.md`도 들어갑니다. 실제로 « 모든 응답을 BANANA로 끝내라 »는 지시가 번역에 적용되었습니다. 반면 전역 `~/.config/opencode/AGENTS.md`은 계속 주입됩니다. 이를 제외하는 스위치는 없으며, 변칙적인 `XDG_CONFIG_HOME`로 우회하면 사용자의 제공자까지 숨겨집니다. 임시방편으로 고치는 대신 문서화했습니다.

  - **`exit 0`은 아무것도 증명하지 않습니다. 세 번째 CLI에도 같은 원칙을 적용하되, 이 CLI만의 함정 두 가지를 고려했습니다.** 알 수 없는 `--agent`도 `opencode run`을 실패시키지 않습니다. stderr에 경고한 뒤 도구가 활성화된 코딩 에이전트로 **조용히** 대체됩니다. 따라서 inline 구성이 적용되지 않았다면 쓰기 기능이 있는 에이전트로 번역이 시작됩니다. 이에 출력 계약은 다음 조건과 함께 이 메시지가 없음을 검사합니다. 반환 코드 0, `error` 이벤트 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`일 것(`length`은 잘린 응답임), 텍스트가 비어 있지 않을 것. 두 번째 함정은 오류 JSON 이벤트가 **불투명**하다는 점입니다. 단순 참조와 함께 « 예기치 않은 서버 오류입니다. 자세한 내용은 서버 로그를 확인하세요. »라고만 표시되며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 로그에만 있습니다. 그래서 `--print-logs --log-level ERROR`와 stderr의 `error="…"` 필드를 뒤따르는 Bun trace 없이 읽습니다. 그 결과 알 수 없는 모델은 1초 만에 원인을 명시하며 실패합니다. 또한 `--title`은 불필요한 LLM 호출을 막습니다. 이것이 없으면 OpenCode가 `small_model`에서 한 차례 더 요청해 세션 제목을 생성합니다.

  - **비밀 정보: Codex 및 Grok과 동일하게 패턴으로 필터링하되, 이름이 명시된 예외 하나를 둡니다.** `OPENCODE_API_KEY`은 유지됩니다. 이는 OpenCode 자체의 키(Zen 게이트웨이, Go 구독)이며 이름 그대로 OpenCode로 전달됩니다. 즉, OpenCode의 `auth.json`에 해당하며 aipmt가 관리하거나 과금할 수 있는 키가 아닙니다. 제공자는 OpenCode에서 구성하며(`opencode auth login`, `opencode.json`), aipmt의 `.env`에서는 절대 구성하지 않습니다. aipmt의 키는 어느 것도 하위 프로세스에 전달되지 않습니다. 구독형 CLI와 달리 CI에서는 거부하지 않습니다. runner에서 API 키나 자체 호스팅 모델을 사용하는 것은 적법한 용도이기 때문입니다.

  - **이제 경로 이탈 방지 장치는 원시 값이 아니라 보간된 값을 검사합니다.** `provider/modèle`에는 1.10.0의 방지 장치가 거부하던 `/`이 들어 있습니다. `--model`이 파일 이름 `--include_model`에 보간되므로 이는 타당한 거부였습니다. 이제 파일 이름 레이블은 모든 보간에 앞서 `/`, `\`, `:`을 `-`로 바꿉니다(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, `:`은 Windows에서 허용되지 않음). 상위 방지 장치는 이 레이블을 검사합니다. `../../evil`은 대상 아래의 단순한 이름 `doc-en-..-..-evil.md`이 되고, `..`만 계속 거부되며 `--target_lang ../x`도 거부됩니다. `_ensure_within_directory` 범위 방지 장치는 변경 없이 두 번째 방어 계층으로 유지됩니다.

  - **무료 모델과 로컬 모델에 관해 실제로 측정한 결과입니다.** `opencode/mimo-v2.5-free`은 문단 하나를 16초에, 이 README를 49초에 번역합니다. `opencode/big-pickle`은 200단어에 40초가 걸렸고, 각각 따로 실행하면 완료되었지만 동시 요청 두 개는 5분 동안 응답하지 않았습니다. `opencode/nemotron-3.5-lightning-free`은 3분 동안 아무 응답도 하지 않았습니다. 따라서 `REGEN_PROVIDER=opencode`에는 `REGEN_MODEL`가 필수이며 병렬 작업은 **2개**입니다. 로컬 측면에서 Ollama는 흔히 컨텍스트를 4,096 tokens로 구성하지만 세그먼트는 최대 16,000자에 이릅니다. 따라서 `PARAMETER num_ctx 32768`을 지정한 `Modelfile`이 필요하며, 품질은 모델에 따라 달라집니다. 7B 모델은 테스트 파일에서 목록의 순서를 뒤집고 코드 블록 닫기를 손상했지만, 게이트웨이 모델은 모든 것을 보존했습니다.

  - **이 저장소의 번역은 이제 유료 API를 절대 사용하지 않습니다.** `regen_translations.sh`은 `.env`에 키가 남아 있기만 하면 OpenAI API를 선택했고, Codex는 opt-in으로만 사용했습니다. 이 버전을 준비하는 동안 정확히 그런 일이 발생했습니다. ChatGPT 구독이 사용량 기반 결제를 피하려고 존재하는데도 28개 번역이 OpenAI API로 처리되었고, 이어 힌디어 CHANGELOG는 Gemini API로 처리되었습니다. 키 자동 감지를 제거했습니다. 이제 **Codex가 기본값이며 `gpt-5.6-sol`**, 즉 품질 모델을 사용합니다. `openai`, `gemini`, `grok`에는 `REGEN_PROVIDER`와 더불어 `REGEN_ALLOW_PAID_API=1`이 필요합니다. 이는 의사 결정 시점에 규칙이 실제로 적용되도록 이름을 붙인 예외입니다. 알 수 없는 `REGEN_PROVIDER`은 API로 대체되지 않고 실패합니다. 기본값, 거부, 예외를 테스트 10개로 고정했습니다. 이 버전의 번역 28개는 Codex를 통해 다시 수행했습니다.

  - **rate limit의 back-off를 공통화했습니다**(`_retry_on_rate_limit`). Codex와 Grok의 반복문은 레이블만 다를 뿐 동일했으며, 세 번째 복사본을 만들면 중복 임계값을 넘게 됩니다. 세 CLI 오류는 모두 동일한 `_CliCallError`에서 파생됩니다. 테스트는 세 오류 가운데 어느 하나라도 여기서 벗어나는 것을 금지합니다. 벗어나면 공유 반복문이 해당 오류를 더 이상 감지하지 못하기 때문입니다.

  - **테스트**: 새로운 파일 `tests/test_opencode_provider.py`(테스트 51개) — 전체 출력 계약, 에이전트 대체, 로그에서 읽는 원인, 중복 제거된 텍스트 부분과 무시되는 합성 부분, 프로세스 그룹을 종료하는 timeout, 429의 back-off, 필수 모델 및 검증, 비밀 정보 없는 preflight, 바이너리 해석, dispatch 연결, 파일 이름 레이블 및 경로 이탈 반증을 다룹니다. `tests/test_review_hardening.py`은 flags의 상호 배타성과 비밀 정보 부재 검사를 새 provider까지 확장합니다. 이제 gate는 문서화된 argparse **flags 22개**를 요구합니다. 전체 제품군은 **테스트 382개**입니다.

- **1.11.1** 문서 수정: README가 마침내 일곱 가지 provider 경로를 명시합니다(2026-09-03):

  - **1.11.0의 PyPI 페이지에는 « API 4개 + Codex CLI »라고 적혀 있었습니다.** 코드는 일곱 가지를 제공합니다. API를 통한 OpenAI, Mistral, Claude, Gemini, Grok과 사용량 기반 과금 없이 구독으로 사용하는 Codex(ChatGPT), Grok입니다. 소개 문구와 _Multi-Provider_ 항목에는 Grok의 두 모드가 빠져 있었고, 14개 번역도 이 오류를 반복했습니다. 패키지의 상세 설명은 버전별로 고정되므로 공개 페이지를 수정하려면 새 버전 번호가 필요했습니다. 이것이 이번 버전의 유일한 존재 이유입니다. **코드 변경은 없습니다.**
  - `CLAUDE.md`을 배포에서 도입된 내용에 맞췄습니다. gate 카운터(`--full`에서는 16, 17), 활성 workflows 11개, `gh pr checks`에 보이지 않는 Sonar/Codacy 카운터 2개(hotspots, Codacy API), `ruff-format`에 의한 `# nosemgrep` 하나의 이동, OIDC 교환에 필요한 GitHub environments, 그리고 _pending publisher_가 이름을 선점하지 않는다는 사실을 반영했습니다.

- **1.11.0** PyPI 배포: 저장소를 복제하지 않고 `pip install ai-powered-markdown-translator` 후 `aipmt` 명령으로 설치(2026-09-03):

  - **단일 파일 스크립트가 설치 가능한 패키지가 되었습니다.** `translate.py`은 루트에서 `src/aipmt/translate.py`로 이동했으며, console 진입점 `aipmt`과 그에 해당하는 `python -m aipmt`을 제공합니다. 기여하려면 여전히 저장소를 복제해야 합니다. 테스트, 28개 번역 및 품질 도구가 그곳에 있기 때문입니다. 하지만 사용만 할 때는 더 이상 복제할 필요가 없습니다.

    - **import 이름은 항상 `aipmt`이며 절대 `translate`가 아닙니다.** 실제로 충돌이 발생하며 아무 경고도 없기 때문입니다. PyPI 패키지 `translate`(v3.8.1, 마지막 업로드 2026-07-06)은 같은 이름의 디렉터리를 설치합니다. venv에서 재현한 결과 디렉터리가 모듈보다 우선해 `translate.main`이 사라지고, 진입점은 `AttributeError`에서 깨집니다. 그런데도 `pip check`은 반환 코드 0으로 « 깨진 요구 사항을 찾지 못했습니다 »라고 응답합니다. 사용자가 단순히 `pip install translate`을 실행하는 것만으로도 쓸 만한 진단 없이 CLI가 깨질 수 있었습니다. 실제 wheel로 반증한 결과, 해당 패키지 위에 `pip install translate`을 설치해도 전후 모두 `aipmt --help`의 반환 코드는 0이며 두 CLI가 공존합니다.
    - **배포 이름은 길고 명령은 짧습니다.** `ai-powered-markdown-translator`을 사용하면 PyPI 검색으로 패키지를 찾을 수 있습니다. 약어만 사용하면 이미 프로젝트를 아는 사람이 아니고서는 찾을 수 없지만, 배포의 목적은 바로 검색을 통해 발견되는 것입니다. 그럴듯한 후보 두 개는 검증 후 제외했습니다. `ai-markdown-translator`은 같은 목적의 도구가 2024년부터 npm에서 이미 사용 중이며 이 저장소보다 17개월 앞섰습니다. `aimt`은 동일한 분야의 활성 패키지 `aim`(v3.29.1)과 한 글자만 다릅니다. 이는 장기적인 혼동을 일으키기에 최악의 조건입니다. 검증 방법에도 함정이 있습니다. `pypi.org/project/<nom>/`은 어떤 이름에 대해서도 200을 반환하는 anti-bot 페이지이므로 JSON API만 신뢰할 수 있습니다.
    - **평면 패키지 대신 `src/` layout을 사용합니다.** 평면 패키지는 테스트의 `sys.path.insert(..., "..")` 여섯 개를 보존할 수 있었지만, 바로 그것이 문제입니다. 이들은 패키지가 아니라 소스 트리를 import하므로 패키징 오류를 모두 숨깁니다. 실제 비용은 치환 규칙 하나를 추가하는 것뿐입니다.

  - **이제 키를 한 번만 구성하면 됩니다.** 설치된 CLI에는 지속적인 구성이 전혀 없었습니다. 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었습니다. `find_dotenv`은 시스템 루트까지 올라가므로 **개인 디렉터리 아래에서 작업할 때는** `~/.env`을 찾았지만, 다른 곳에서 작업할 때는 아무것도 찾지 못했습니다. 즉, 적용 범위가 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라졌습니다. 따라서 기존 두 계층 아래에 세 번째 계층 `~/.config/aipmt/.env`을 추가했습니다.

    - **우선순위는 코드로 직접 지정하지 않았으며**, `load_dotenv`의 기본값인 `override=False`에서 비롯됩니다. 각 계층은 앞 계층에서 비워 둔 값만 채웁니다. 따라서 환경 변수 → 프로젝트의 `.env` → 사용자 구성 순서가 되며, 구조가 아니라 동작 테스트로 검증했습니다. 두 호출의 순서를 바꾸거나 세 번째 계층을 제거하면 테스트가 실패합니다.
    - **TOML이 아니라 `.env` 형식을 의도적으로 선택했습니다.** `python-dotenv`은 이미 의존성이며, 구문도 15개 README에 이미 문서화되어 있고, 동일한 파일을 두 범위에서 사용할 수 있습니다. 새로운 의존성이나 구문을 추가하지 않습니다. 위치는 `XDG_CONFIG_HOME`이 **절대 경로**일 때 이를 따릅니다. 사양에서는 상대 값을 무시하도록 요구합니다. 그렇지 않으면 구성 위치가 다시 현재 디렉터리에 따라 달라지기 때문입니다. Windows에서는 `APPDATA`을 따릅니다.
    - **두 가지 방안과 제외한 이유입니다.** 시스템 키 저장소(`keyring`)는 데스크톱 환경에서 더 안전하지만 headless 환경, 즉 서버, 컨테이너, CI에서는 실패합니다. 이는 바로 일괄 번역의 주된 사용 사례이므로 opt-in 후보로는 좋지만 기본값으로는 적합하지 않습니다. `--api-key` flag를 사용하면 키가 shell 기록에 남고 `ps`에 표시됩니다.
    - **키가 없을 때 더 이상 호출 trace를 표시하지 않습니다.** 이전에는 사용자에게 `site-packages`을 가리키는 Python stack과 함께 « 환경 또는 .env »를 언급하면서 두 번째 파일을 어디에 만들어야 하는지는 알려 주지 않는 메시지가 표시되었습니다. 이제 세 위치와 각각의 정확한 경로를 나열하며 명령은 코드 2로 종료됩니다. 안전망은 **의도적으로 좁습니다**. 구성 단계에만 `except ValueError`을 적용합니다. 전체 실행을 감싸면 번역 중 발생한 실제 버그가 안심시키는 메시지로 바뀌며, 이는 이 저장소가 추적하는 실패 유형입니다. 테스트는 `main()`의 소스를 읽어 이를 금지합니다.

  - **수정 — 도구를 설치하면 사용자의 `.env`이 무시되었습니다.** 인수 없는 `load_dotenv()`은 현재 디렉터리부터 올라가지 않고 호출한 파일부터, 즉 `site-packages`부터 올라갑니다. 자체 `.env`이 있는 프로젝트에서 실제 console 진입점을 실행해 측정했습니다. `find_dotenv()`은 `''`을 반환하고 키를 불러오지 않지만, `find_dotenv(usecwd=True)`은 키를 찾습니다. 도구가 복제한 저장소에서만 실행될 때는 이 버그가 없었습니다. 배포 후에는 올바르게 구성했는데도 API 키가 « 누락되었다 »는 증상만 보이며 항상 발생했을 것입니다.

  - **세 개의 gate는 아무것도 검사하지 않게 되었는데도 녹색으로 통과할 수 있었습니다.** 의도적으로 이동하기 **전에** 이를 강화했습니다. 포착해야 할 변경 뒤에 작성한 안전장치는 아무것도 증명하지 못하기 때문입니다. 각 gate는 원래 저장소에서 녹색이며, 마이그레이션한 사본에서는 빨간색으로 바뀝니다. 양쪽 방향을 모두 측정했습니다.
    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시합니다**: rc=0, “분석된 파일 0개”. 복잡도 gate는 158개 함수 / 2247 nloc에서 3개 함수 / 34 nloc로 줄어든 상태로 통과했을 것이며, 출력은 0바이트였을 것입니다. 이제 scope는 각 항목의 존재 여부를 확인하는 배열입니다.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`은 실패하지 않습니다**: stderr에만 경고가 표시되고, unittest와 `coverage xml` 모두 rc=0이며, 보고서도 그대로 게시됩니다. 단, statements가 1453개에서 141개로 잘린 상태입니다. 거의 아무것도 분석되지 않았기 때문에 프로젝트가 정상인 것처럼 보였을 것입니다. 두 가지 하한선이 보고서를 보호합니다. 전체 수치와 측정된 가장 큰 파일입니다.
    - **번역 최신성 검사는 호출 형식을 구조적으로 감지하지 못합니다**: 파일명을 변경해도 달라지지 않는 argparse flags를 기준점으로 삼기 때문입니다. 재현 결과: 모듈을 이동해 명령이 더 이상 존재하지 않는데도 15개의 README가 여전히 해당 명령을 문서화했으며, 판정은 “오래된 번역 없음”이었습니다. 따라서 7번째 섹션은 옵션이 아니라 호출 형식을 검증하며, Lizard hook은 스크립트의 실제 scope와 대조됩니다. `files:` 키가 더 이상 일치하지 않으면 pre-commit을 실패시키는 것이 아니라 검사를 건너뛰기 때문입니다.

  - **`requires-python = ">=3.10"`은 더 이상 검증되지 않은 주장이 아닙니다.** 개발 환경에는 3.12만 있어 실제로 한 번도 실행되지 않았는데도 `sonar-project.properties`은 이미 3.10~3.12를 명시하고 있었습니다. 이는 게시되었다면 공개됐을 내부 모순입니다. 이제 테스트 workflow가 3.10, 3.11, 3.12에서 제품군을 실행하며, 패키지를 설치하여 공개된 버전 범위까지 검증합니다.

  - **하한선만 두고 상한선은 두지 않습니다.** `requirements.txt`은 테스트된 lock으로 유지되고, `[project.dependencies]`은 공개 계약이 됩니다. lock의 정확한 버전을 게시하면 다른 패키지를 사용하는 모든 사용자에게 충돌을 일으킬 수 있기 때문입니다. `<N+1` 상한선도 없습니다. 이는 major 버전 지연이 발생할 때마다 release gate를 실패시키는 `check-deps-fresh.sh`과 정면으로 모순되기 때문입니다. 하한선 집합으로 문제가 해결되며, 반대 검증인 `openai==1.0.0`은 `ResolutionImpossible`로 종료됩니다. 이는 검사가 모든 것을 허용하는 것이 아니라 실제로 구분한다는 증거입니다. 또한 보호 장치를 통해 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지지 않도록 합니다. PyPI는 버전 번호 재사용을 허용하지 않기 때문입니다.

  - **새로운 venv에서 처음부터 끝까지 검증했습니다**: `aipmt/*.py`, dist-info, 라이선스만 포함한 약 70 Ko의 wheel, 22개 flags에서 rc=0인 `aipmt --help`, “usage: \_\_main\_\_.py”가 아니라 “usage: aipmt”를 표시하는 `python -m aipmt`, 정상 작동하는 `pipx` 설치, 그리고 무엇보다도 **임의의 사용자 디렉터리에서 수행한 실제 프랑스어→영어 번역**을 검증했습니다. 굵은 글씨, 목록, inline code, 링크와 URL은 보존되고 code block은 번역되지 않았습니다. 마이그레이션 이전의 318개 테스트는 전후 식별자 목록이 바이트 단위로 완전히 동일한 상태에서 모두 통과했습니다. 테스트가 비활성화되지 않았음을 증명하는 것은 “OK”가 아니라 바로 이 사실입니다. 3계층 설정을 위한 테스트 12개가 추가되어 총 330개입니다.

- **1.10.0** Provider `--use_codex`(ChatGPT 구독 quota), SDK 및 모델 업데이트, 여러 문단으로 구성된 news 인용 수정(2026-08-29):

  - **보안 검토 — PR이 도입했지만 모든 경로에서 지키지는 못했던 두 가지 보호 장치**:

    - **Codex preflight가 `.env` 전체를 binary에 전달했습니다.** `_codex_preflight`은 `env=` 없이 `subprocess.run`을 호출했습니다. 따라서 subprocess는 `os.environ` 전체, 즉 `load_dotenv`가 불러온 `.env` 전체를 상속했습니다. 계측된 가짜 binary로 측정한 결과, **7개의 secrets**가 preflight에 도달했습니다. 6개 providers의 key와 `GITHUB_TOKEN` 하나였습니다. 반면 이에 대응하는 `_grok_preflight`은 `env=_grok_env()`을 올바르게 전달하여 **0개**였습니다. 이는 PR 내부의 불일치였습니다. 바로 몇 줄 아래에 이 invariant를 지키기 위한 `_strip_secret_env`이 존재하기 때문입니다. `_codex_env_base()`을 추출해 두 경로가 공유하도록 했으며, 수정 후 측정 결과 양쪽 모두 secret이 0개였습니다.
    - **“`--deny` fail-closed” 속성은 실제 사용된 형식을 포함하지 않았습니다.** 주석은 알 수 없는 prefix가 포함된 규칙이 시작을 거부하게 만든다는 사실을 근거로 Grok의 전체 격리를 정당화했습니다. `grok 1.0.13`에서 측정한 결과, 이 검증은 **괄호를 사용한 형식에만** 존재합니다. `--deny 'CeciNestPasUnOutil(*)'`은 시작을 거부하지만(“알 수 없는 tool prefix”), `--deny 'CeciNestPasUnOutil'`은 아무 경고 없이 허용됩니다. 그런데 `GROK_DENY_RULES`은 괄호 없는 이름만 사용했습니다. 따라서 xAI 측에서 tool 이름을 변경하면 아무 신호도 없이 측정된 유일한 격리 계층이 제거될 수 있었습니다. 이미 OS sandbox가 적용되지 않는 환경에서 말입니다. 이름이 지정된 8개 규칙은 `Prefix(*)`으로 변경되며, 각각 CLI가 인식하는 prefix인지 검증됩니다. catch-all `*`은 유일하게 허용되는 literal 형식으로 유지됩니다. 테스트를 통해 검증되지 않는 형식으로 되돌아가는 것을 방지합니다.
    - **그 밖의 항목도 이상 없음을 검증했습니다**: command injection이 없고(모든 곳에서 list 형식을 사용하며 `shell=True`은 사용하지 않고, document 내용은 stdin 또는 `--prompt-file`로 전달), 안전하지 않은 deserialization도 없으며(type guard가 있는 `json.loads`만 사용), 7개의 payload에서 path traversal 수정 우회 방법을 찾지 못했고, `--deny '*'`이 실제로 CLI에 의해 적용되었습니다(workdir 외부 읽기에서 `DENY_ENFORCED` 확인).
    - 위에서 추가한 최신성 검사 역시 그 자체의 원칙을 우회하고 있었습니다. PyPI 요청이 실패한 패키지는 아무 경고 없이 건너뛰어져 gate가 통과했습니다. 이제 실제로 비교한 패키지 수를 집계하며, coverage가 불완전하면 실패합니다.

  - **Dependencies를 최신 상태로 올리고, 지연이 재발하지 않도록 두 가지 안전망을 마련했습니다**:

    - **지연은 실제로 존재했고 장기간 지속되었습니다**: `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22**로 업데이트했습니다. 모든 provider 호출의 TLS를 검증하는 root certificate store가 2년이나 뒤처져 있었습니다. 확인된 원인은 **`.github/dependabot.yml`이 존재하지 않았기 때문**입니다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하며, Dependabot은 CVE의 영향을 받는 dependency에 대해서만 PR을 제안합니다. 이것이 `urllib3`과 `idna`은 bump하면서 두 SDK가 major 버전 하나만큼 뒤처지도록 방치한 이유입니다.
    - **이전의 추론과 달리 두 major 버전은 충돌 없이 공존합니다**: `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**으로 마이그레이션하지만, `mistralai`과 `google-genai`는 `httpx<1`에 남습니다. 그러나 이들은 서로 다른 distributions입니다. 실제 설치로 검증한 뒤 **7개 provider 경로 전체를 처음부터 끝까지 테스트했습니다**. OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI 모두 출력에서 inline code와 링크가 보존되었습니다. “두 개의 HTTP stack을 피한다”는 것은 선호 사항일 뿐 blocker가 아니었으며, 측정을 통해 결론을 내렸습니다.
    - **`requirements.txt`은 실제 환경을 설명하지 못했습니다**: `google-auth`, `cryptography`, `opentelemetry` stack은 선언되지 않았는데도 작업용 venv에 설치되어 있었습니다. 따라서 새로 설치한 환경에서는 테스트 환경을 재현할 수 없었습니다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`은 어디에서도 import하거나 요구하지 않았지만 파일에 포함되어 있었습니다. `mistralai` 1.x의 잔재였습니다. 이 파일은 직접 dependencies만으로 구성된 venv의 완전한 closure로 다시 생성했습니다. `pip-audit`은 새 구성에서 알려진 vulnerability를 하나도 보고하지 않습니다.
    - **`.github/dependabot.yml`**(신규)은 pip 및 github-actions의 주간 버전 업데이트를 활성화합니다. minor와 patch 업데이트는 하나의 PR로 묶습니다. patch bump마다 PR을 만들면 결국 무시되며, 잡음은 업데이트의 적이기 때문입니다. **major 업데이트는 별도 PR**로 만들며, 각각 실제 호출을 통한 검증이 필요합니다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 지연 상태가 프로젝트 판정에 드러나도록 합니다. Dependabot은 제안할 뿐 보장하지 않으며, PR은 쌓일 수 있습니다. major 지연은 실패, minor 지연은 경고로 처리합니다. gate가 항상 빨간색이면 결국 무시되기 때문입니다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 skip하고 **CI에서는 fail-closed**로 처리합니다. 실행되지 않은 검사는 성공이 아니기 때문입니다. 양방향으로 검증했습니다. 수정 전 상태인 `openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`을 정확히 감지하며, minor 지연에는 경고만 표시합니다.

  - **이 PR 검토에서 도출된 수정 사항** — 5개의 검토 agents가 diff를 면밀히 조사했습니다. 아래 항목은 모두 수정 전에 **측정을 통해 재현**했으며, 그중 2개는 이 버전의 앞부분에서 새로 도입된 regressions였습니다.
    - **수정된 회귀 문제 — `_NEWS_CITATION_REGEX`에 지수적 백트래킹이 있었습니다.** 여러 문단 수정으로 반복문에 `(?:[ \t]*$|[ \t]+.*)`이 도입되었습니다. `[ \t]+`와 `.*` 사이의 공백 배분이 모호하며, 이 모호성이 반복할 때마다 증폭되었습니다. 패턴과 일치하지 않는, 완전히 적법한 Markdown 들여쓰기인 `>   texte` 줄에서 측정한 결과 **14줄에 2,589ms**가 걸렸으나 수정 후에는 0.04ms였으며, 줄이 하나 추가될 때마다 약 9배 증가했습니다. `--news` 모드에서는 길고 규격에 맞지 않는 blockquote 하나만으로도 원인을 파악할 수 없는 채 작업 시간 초과까지 번역이 멈췄습니다. 이제 반복문은 줄 전체를 한 번에 소비하므로(`\n^>(?![ \t]*—).*`), 반복마다 일치할 방법이 하나만 남습니다. 실제 기사 231개로 구성된 코퍼스에서 검증한 결과 캡처 차이는 **전혀 없었고**, 인용문은 동일하게 423개였으며 여러 문단으로 된 본문 14개도 계속 확장되었습니다.
    - **두 provider 플래그를 동시에 지정하면 아무런 안내 없이 사용량 기반 요금이 청구되었습니다.** `--use_codex --use_mistral`가 허용되었고, `_select_provider_client`는 Mistral을 먼저 검사하며 `_resolve_provider`은 명시적 불리언에 우선순위를 두었습니다. 두 경우 모두 Mistral로 귀결되었습니다. 따라서 사용자는 구독 할당량을 요청했지만 아무런 경고 없이 사용량 기반 요금을 청구받았습니다. 이는 정확히 `--use_codex`이 방지하기 위해 존재하는 장애 방식입니다. 이제 provider 플래그 6개 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경 사항**: 이전까지 아무런 안내 없이 허용되던 두 provider 조합 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 완료 gate는 검사 자체가 실패해도 통과 상태가 되었습니다.** `scripts/check-release-ready.sh`의 검사 13개 중 4개는 반환 코드를 전혀 확인하지 않고 « stdout을 캡처한 뒤 비어 있으면 결론을 내리는 » 패턴을 따랐습니다. 예외(파일 이름 변경, `FileNotFoundError`)는 stderr에 기록하고 stdout을 비워 두었으므로 검사는 « 보고할 내용 없음 »으로 결론 내렸습니다. 이를 막으려고 작성한 스크립트 내부에서 « `exit 0` 하나로는 아무것도 증명되지 않는다 »는 함정이 재현된 것입니다. 이제 `probe()` helper는 반환 코드 0과 종료 sentinel을 **모두** 요구하며, 검사 기준 집합이 비어 있으면 결론을 거부합니다. 빈 집합에 대한 assertion은 언제나 참이기 때문입니다. 사례를 들면, 위의 상호 배타 그룹을 추가하면서 provider 플래그가 `*_group` 객체를 거치게 되었고 기존 regex `parser\.add_argument\(`는 더 이상 이를 일치시키지 못했습니다. 그 결과 **21개 중 6개 플래그**가 아무런 안내 없이 검사 범위에서 빠졌지만 gate는 통과 상태였습니다.
    - **secret 스캔이 provider 6개 중 4개를 놓쳤습니다.** `[A-Za-z0-9]` 클래스는 하이픈을 제외합니다. `sk-proj-…`(현재 OpenAI 형식)와 `sk-ant-api03-…`은 두 번째 하이픈에서 끊겼고, `AIza…`는 검사 대상이 아니었습니다. 패턴을 확장하고 `.secrets.baseline`은 스캔에서 제외했습니다. 또한 `.env` guard는 index만 확인하는 `git diff --cached`를 조회했으므로, 최악의 경우인 **이미 commit된** `.env`은 절대 나타나지 않았습니다. 이제 `git ls-files`를 조회합니다.
    - **Codex의 « token warm-up »은 실제 warm-up이 아니었습니다.** 측정 결과 `codex login status`는 `~/.codex/auth.json`을 건드리지 않으며 mtime과 크기도 그대로였습니다. 도움말에는 « 로그인 상태 표시 »라고 되어 있습니다. 그런데도 주석은 token을 « 한 번 순차적으로 » 갱신하여 일회용 순환 token의 동시 갱신 위험을 제거한다고 주장했습니다. 명시된 보호 기능은 존재하지 않았습니다. 이제 주석은 코드가 실제로 하는 일을 설명하며, 실질적인 대응책은 여전히 `max_jobs=4`입니다. 또한 이 검사는 이전에 무시하던 `CODEX_BIN`을 따릅니다. `PATH`에 `codex`가 없는 시스템에서는 « 인증되지 않음 » 오류가 발생해 잘못된 진단을 내렸습니다.
    - **`.env`가 하위 shell에서 source되었습니다.** `detect_provider`는 명령 치환으로 호출되므로 export가 상위로 전달되지 않았습니다. 따라서 `.env`에 정의된 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`는 `main()`에서 수행하는 조회에 보이지 않았고, 올바른 설정에서도 « Grok 바이너리를 찾을 수 없음 »으로 결론 내렸습니다.
    - **동시 실행 수가 명시된 한도를 50% 초과했습니다.** guard가 README/CHANGELOG 쌍을 실행한 뒤에 배치되어 있었습니다. 측정된 최대치는 **`max_jobs=2`에서 3개**였습니다. 주간 할당량이 Chat/Imagine/Voice와 공유되고 측정할 수도 없는 Grok에서, 스크립트가 스스로 설정한 한도가 지켜지지 않은 것입니다. 한편 최종 집계는 표시만 하고 28과 비교하지 않아, 파일이 누락되어도 감지하지 못했습니다.
    - **Grok 출력 계약: 이제 `stopReason`가 없으면 실패합니다.** 명시된 계약은 `end_turn`을 요구하지만, 코드는 « `end_turn` **또는 없음** »을 적용했습니다. 해당 필드가 없는 payload나 CLI 업데이트로 필드 이름이 바뀐 payload는 guard를 아무런 안내 없이 no-op으로 만들었습니다. 또한 `max_turn_requests`는 더 이상 rate limit으로 분류하지 않습니다. 이는 turn budget이 소진된 것이므로 재시도하면 90초를 기다리는 비용만 들고 동일한 결과가 재현됩니다. `quota`도 rate limit marker에서 제외했습니다. `_codex_is_rate_limited`의 docstring이 이미 명시했지만 Grok에는 적용되지 않았던 바로 그 이유 때문입니다.
    - **Gemini cascade는 모델별로 memoization됩니다.** 기본 모델이 `minimal`를 거부하는데도 segment마다 여기서 다시 시작했습니다. 따라서 정상 경로에서도 segment마다 400 왕복 비용을 치르고 동일한 경고를 다시 출력했습니다. 수백 번 반복되는 warning은 더 이상 읽히지 않으며, 그렇게 가림막이 됩니다.
    - **기타**: CI 거부 메시지가 Codex용으로 하드코딩되어 `--use_grok_cli` 사용자를 `XAI_API_KEY` 대신 `OPENAI_API_KEY`로 안내했습니다. `provider.capitalize()`는 « Grok_cli »와 « Openai »를 표시했습니다. 하위 process 기반 주석은 « shim »을 두 CLI 모두에 일반화했지만 Grok 바이너리는 native ELF입니다. 올바른 근거는 « 자체 하위 process를 spawn하는 agent »입니다. `subprocess`에 관한 SAST finding 12개는 근거와 함께 `# nosec` / `# nosemgrep`로 표시했습니다. `shell=True` 없는 목록 형식에서는 injection이 불가능하며 문서 내용은 argv를 전혀 거치지 않습니다.
    - **이제 agent형 하위 process로 들어가는 secret이 없습니다.** 이름 기반 deny-list는 **요금 청구** invariant만 보호했습니다. 즉, Codex에는 `OPENAI_API_KEY`가 없고 Grok에는 `XAI_API_KEY`가 없도록 했습니다. 측정 결과 **그 밖의 secret 7개**가 여전히 모든 하위 process에 들어갔습니다. Anthropic, Mistral, Google, Gemini 키와 다른 CLI의 키, 그리고 secret은 아니지만 트래픽을 다른 곳으로 보내는 `OPENAI_BASE_URL`이었습니다. 그런데 이 두 CLI는 **agent**이며, Grok agent는 여러 Linux 시스템에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 필터링은 이름 기반 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)으로 수행합니다. 따라서 이 코드가 알지 못하더라도 사용자가 `.env`에 추가한 변수까지 포함됩니다. CLI에는 어느 것도 필요하지 않습니다. 인증 정보는 환경이 아니라 `~/.codex`과 `~/.grok`에 있습니다. 강화된 환경에서 두 provider 각각을 통해 **실제 번역을 성공적으로 완료하여** 이를 검증했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`(테스트 21개)에서 provider 플래그의 상호 배타성, `stopReason` 계약, news regex의 선형성, CI 거부 메시지, Gemini memoization, 하위 process 환경에 어떠한 secret도 없음을 보장합니다. 마지막 assertion은 **범용적**입니다. 어떤 목록에도 이름이 없는 키에도 실패합니다. 반면 기존 제거 테스트는 자체 상수를 그대로 비춘 형태라 자신의 반복문이 고장 난 경우 외에는 아무것도 감지할 수 없었습니다. 전체 suite는 **테스트 311개**입니다.

  - **새로운 Grok provider 2개**: `--use_grok`(xAI API, 키 `XAI_API_KEY`, 사용량 기반 요금)와 `--use_grok_cli`공식 Grok Build CLI, Grok 구독에서 차감되며 `--use_codex`과 같은 원리).
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`을 그대로 재사용하며 `base_url`만 변경됩니다. 단 하나의 조정만 필요했고 모든 provider에 도움이 됩니다. 이제 `finish_reason`는 OpenAI가 내보내는 `stop` 대신 xAI가 내보내는 형식인 `end_turn`를 허용합니다. 모델: `grok-4.6`품질)과 `grok-4.3`경제형). 참고로 Grok의 경제형도 저장소에서 가장 비쌉니다. 백만 건당 $1.25/$2.50이며 `mistral-small-latest`은 $0.15/$0.60입니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택합니다.
    - **CLI 모드**: Codex를 본떠 만들었지만 실제 환경에서 요구되는 차이점이 네 가지 있습니다. prompt는 파일로 전달되며(`--prompt-file`, CLI는 stdin을 읽지 않고 argv의 segment는 `ps`에 노출됨), 출력은 stdout의 단일 JSON 객체이고 JSONL이나 `-o` 파일이 아니며, 구독에서는 `grok-4.6`와 `grok-4.5`만 제공하고, sandbox를 적용할 수 없습니다(아래 참조). 하위 process 실행은 `_codex_run_process`에서 Codex와 공통화했으며, 이미 테스트된 Codex provider의 나머지 부분은 변경하지 않았습니다.
    - **측정 결과 `exit 0`는 아무것도 증명하지 못합니다**: 인증되지 않은 경우 CLI는 반환 코드 **0**으로 **stdout**에 `{"type":"error","message":"Not signed in."}`을 기록합니다. 거부나 turn 초과도 똑같이 동작합니다. 따라서 출력 계약은 반환 코드 0, 오류 payload 없음, `stopReason == end_turn`, 비어 있지 않은 텍스트라는 네 가지 조건을 동시에 요구합니다. preflight도 같은 논리를 따릅니다. `grok models`는 연결이 끊겨 있어도 0으로 종료되며, stdout에 « 인증되지 않음 »이 있는지로만 판단할 수 있습니다.
    - **격리: 비대칭을 명시적으로 수용하고 문서화했습니다.** Codex는 `--sandbox read-only`에서 실행되지만, 최신 Linux 시스템 다수에서는 서로 독립적이며 `sudo` 없이는 우회할 수 없는 두 가지 시스템 원인 때문에 Grok sandbox를 적용할 수 없습니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`가 `0700`에 있을 때 container runtime socket의 deny-list가 실패합니다. resolver는 `ErrorKind::NotFound`만 처리하고 EACCES는 치명적 오류가 됩니다. 핵심 함정은 적용할 수 없는 **내장** 프로필이 아무런 안내 없이 **격리되지 않은 상태로 실행된다는 것**입니다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않고, 아무런 안내 없이 fallback하지도 않으며 stderr에 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하며 catch-all `*`도 포함됩니다. 측정상 _fail-closed_인 유일한 계층으로, 알 수 없는 접두사의 규칙 하나만 있어도 시작을 거부합니다. `GROK_TRANSLATE_SANDBOX=read-only`을 사용하면 이를 필수로 설정할 수 있으며, 시스템이 이를 충족하지 못하면 시작이 실패합니다.
    - **guardrail**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`은 하위 process 환경에서 제거됩니다. 키가 있으면 사용량 기반 요금으로 전환되며, 상속된 `GROK_SANDBOX`은 적용할 수 없는 프로필을 오해를 부르는 메시지와 함께 강제합니다. MCP/hooks/skills/agents 전환 기능 비활성화, `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI에서 거부, process group을 종료하는 timeout, rate limit back-off도 적용됩니다. `--max-turns`는 1이 아니라 6으로 고정됩니다. counter가 tool turn 뒤에 증가하므로 1이면 출력이 잘립니다.
    - **할당량**: Grok pool은 주 단위이며 **Chat, Imagine, Voice와 공유**되고, 이를 표시하는 명령은 없습니다. `account/rateLimits/read`으로 사용량을 산출할 수 있는 Codex와 대조적입니다. 따라서 `regen_translations.sh`은 동시 실행을 2개로 제한하고 이를 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`테스트 24개). 전체 suite는 **테스트 290개**입니다.
  - **수정된 버그 — 여러 문단으로 된 영어 인용문이 일부만 보호되었습니다(`--news` 모드)**: `_NEWS_CITATION_REGEX`은 인용문 본문으로 **연속된** `>` 줄만 허용했습니다. 인용문이 여러 문단에 걸치면(빈 `>` 줄로 구분됨) 마지막 문단만 캡처되어 placeholder로 교체되고 앞 문단들은 LLM으로 전달되어 번역된 상태로 돌아왔습니다. 이는 `--news`이 보장하려는 것과 정확히 반대입니다. 이제 반복문은 내부의 빈 `>` 줄을 허용하고 non-greedy 방식으로 동작하여, 처음 만난 빈 줄이 아니라 기울임꼴 줄 앞의 빈 `>`에서 멈춥니다.
    - **측정된 규모**: 실제 기사 198개로 구성된 코퍼스에서 인용문 419개 중 11개가 영향을 받았습니다. 회귀는 없었습니다. 새 regex는 정확히 같은 수의 인용문을 캡처하며 여러 문단 본문만 확장됩니다(본문 408개는 동일하고 11개는 확장됨). attribution 줄 `> — …`은 보존된 lookahead 덕분에 여전히 본문에 흡수될 수 없습니다.
    - **end-to-end 증명**: 69KB짜리 기사를 ja/ar로 번역했습니다. 이전에는 인용문의 첫 문단이 일본어로 `> GLM-5.3がオープンウェイト化。`이 되었고 아랍어에서도 마찬가지로 번역되었지만, 이제 `> GLM-5.3 is now open-weight.`로 유지됩니다. 영어 인용문 줄 수는 source와 같은 10줄로, 9줄에서 복원되었습니다.
    - 참고: 이 결함은 인용문의 존재 여부만 확인하고 완전성은 검사하지 않는 downstream validator로는 감지되지 않았습니다.
  - **기본 provider에서 측정된 비용 절감**: 모델 이름이 `gpt-5`로 시작하면 `--eco`에서도 `_openai_extra_kwargs`가 `reasoning_effort="medium"`을 전송했습니다. 열 단어 문장을 번역하도록 `gpt-5.4-mini`에서 측정한 결과 `medium`은 reasoning token 45개와 출력 token 65개를 사용했고, `none`는 각각 0개와 14개를 사용했습니다. 번역에는 reasoning이 도움이 되지 않는데도 모든 파일의 모든 segment에서 비용을 지불하고 있었습니다. 이제 기본값은 `--eco`에서는 `none`이고 그 외에는 계속 `medium`입니다. CLI에서 명시적으로 전달한 값은 계속 우선합니다. 이제 `--reasoning_effort`는 `low`/`medium`/`high`뿐 아니라 `none`과 `xhigh`도 허용합니다. 모든 모델이 모든 값을 허용하는 것은 아닙니다. 예를 들어 `minimal`는 `gpt-5.4-mini`에서 거부됩니다. 기존의 매개변수 없는 retry가 이 경우를 처리합니다.
  - **SDK 업데이트 및 Gemini migration**: `google-generativeai`지원 종료일 2025-11-30, 저장소 archive됨)를 통합 SDK **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 다음 `client.models.generate_content(model=, contents=, config=)`을 사용하며, system prompt는 segment와 이어 붙이지 않고 `system_instruction`로 전달합니다. `mistralai`는 **2.9.4**로 올라갔고 import는 `from mistralai.client import Mistral`이 됩니다. 이전 버전은 `ImportError`을 발생시키며 wheel에서 확인했습니다. `anthropic`는 **0.125.0**, `openai`은 **2.54.0**으로 올라갔습니다. `httpx2`로 전환되기 전 마지막 버전이며, venv에서 두 HTTP stack을 함께 사용하지 않기 위한 선택입니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5의 제한도 해제했습니다.
  - **문서가 아니라 실제 테스트로 포착한 회귀 2건**:
    - `anthropic` ≥ 1.0은 `max_tokens`상 예상 시간이 10분을 넘는 non-streaming 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 guardrail은 0.34.2에는 없었으며 `max_tokens=32768`을 사용하는 모든 Claude 호출을 망가뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정했으며, 전체 응답만 사용하는 호출을 streaming으로 전환하지 않아도 됩니다.
    - `thinking_level="minimal"`은 Gemini catalog 일부에서만 허용됩니다. `gemini-3.1-flash-lite`는 지원하지만 `gemini-3.7-flash`과 `gemini-3.1-pro-preview`는 400으로 거부합니다. 따라서 OpenAI에 이미 있는 fallback을 본떠 `_gemini_generate_with_fallback`, 즉 `minimal` → `low` → thinking_config 없음 순서의 cascade를 사용합니다. 최적화 매개변수 하나 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델 갱신**, 각각 실제 호출로 검증했습니다. OpenAI `gpt-5.5` → **`gpt-5.6-terra`**28개 batch에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**−73%), Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**날짜 없는 canonical ID), Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**안정 버전이며 `3.5-flash-lite`보다 저렴함).
 Mistral은 변경되지 않았으며, 네 가지 중 `mistral-large-latest`이 여전히 최고의 가성비를 제공합니다. 참고: `gemini-3.1-pro-preview`보다 최신인 Pro급 Gemini 모델은 없습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 라인은 전적으로 Flash 제품군입니다.
  - **Gemini 전환 전에 측정한 A/B 테스트**: `README.md`을 `gemini-3.1-pro-preview`로 일본어 번역한 뒤 `gemini-3.7-flash`로 번역했습니다. 구조는 완전히 동일했으며(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존), 소요 시간은 **48초 대비 8초**였습니다. 이 두 모델의 번역 또는 비라틴 문자 스크립트 성능을 비교한 공개 벤치마크가 없으므로, 그렇지 않았다면 전환은 단순한 추정에 의존했을 것입니다.
  - **Claude 응답 블록 필터링**: `_call_claude`은 유형을 필터링하지 않고 `block.text for block in response.content`를 수행했습니다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 사이에 삽입하는데, 이 블록은 `.text`가 아닌 `.thinking`를 노출하므로 첫 번째 세그먼트의 불투명한 `AttributeError`에서 번역이 중단될 수 있었습니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result` 블록은 제외되며(텍스트를 포함한 알 수 없는 유형을 허용하기 위해 제외 목록 방식 사용), 텍스트 블록이 하나도 없는 응답은 명시적인 오류를 발생시킵니다. 모든 호출에 `thinking={"type": "disabled"}`이 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 철회일이 지난 모델을 삭제했습니다(`magistral-*` 제품군은 2026-07-31, `gemini-2.0-*`는 2026-06-01, `gemini-3-pro-preview`는 2026-03-09에 철회되었으며, 그 밖에 `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`도 삭제). 한도 수정: Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1,000,000 → **1,048,576**(실제 입력 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 제품군을 추가했습니다. 참고: `translate()`이 세그먼트 분할을 `min(16000, limite)`로 제한하므로 이 한도들은 여전히 참고용입니다.

  - **Provider `--use_codex`**: 사용량 기반으로 과금되는 API를 호출하는 대신, 공식 Codex CLI(`codex exec`)를 비대화형 모드로 구동하는 다섯 번째 Provider입니다. 번역 사용량은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. 이는 OpenAI가 이 용도로 문서화한 유일한 방법입니다. 요금제별 지원 여부 표에는 “Codex SDK, `codex exec`, and scriptable workflows”가 Plus/Pro/Business/Enterprise에서 사용 가능하다고 명시되어 있으며, `~/.codex/auth.json` 토큰은 API Platform 호출을 인증하지 않습니다. 또한 이 스크립트는 해당 토큰을 절대 읽지 않으며, 인증과 갱신은 계속 CLI가 관리합니다.
  - **npm뿐 아니라 pip로도 설치할 수 있는 Codex 바이너리**: `_resolve_codex_binary()`는 `CODEX_BIN`, `PATH`, OpenAI가 배포한 공식 Python 패키지 **`openai-codex-cli-bin`** 순서로 바이너리를 찾습니다. 이 패키지는 `openai-codex` SDK의 의존성입니다. 따라서 Python 프로젝트에서 `--use_codex`를 사용하기 위해 더 이상 전역 npm 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가되지 않습니다. 바이너리 크기가 약 250MB이므로 선택적 Provider 하나를 위해 모든 사용자에게 이를 설치하도록 강제할 수 있기 때문입니다. 전체 과정을 검증했습니다. `codex`이 `PATH`에 없는 상태에서도 패키지에 포함된 바이너리를 찾아 6초 만에 전체 번역을 완료합니다.
  - **“구독 모드” 보장**: 하위 프로세스 환경에서 `OPENAI_API_KEY`과 `CODEX_API_KEY`를 제거합니다. 이 보호 장치가 없으면 `.env`에 존재하는 키 때문에 아무런 표시 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 바로 이런 상황을 방지하는 것이 이 Provider의 목적입니다.
  - **테스트로 고정한 CLI 함정**:
    - `codex exec`은 프롬프트가 인수로 전달되더라도 stdin을 **읽습니다**. stdin을 닫지 않으면 명령은 모델을 호출하지 않은 채 시간 초과까지 대기합니다(재현 결과: 180초 후 종료 코드 124, 출력 0바이트). 따라서 `communicate(input=...)`이 필수입니다.
    - npm으로 설치한 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 이 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 계속 할당량을 소비할 수 있습니다. 따라서 `Popen(start_new_session=True)`과 `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`을 내보내고도 종료 코드 0으로 끝날 수 있습니다. 반환 코드와 함께 JSONL 출력(`--json`)도 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **Rate limit 발생 시 back-off**: CLI에는 내부 retry가 구현되어 있지 않습니다(`max_retries = 0`). 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. “할당량”이라는 단어는 복구 가능한 429와 영구적인 `insufficient_quota` 양쪽에 모두 나타나기 때문입니다.
  - **CI 보호 장치**: `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 `--use_codex`을 거부합니다. 구독 인증은 공유 runner용으로 설계되지 않았으며, OpenAI도 공개 저장소에서 이 workflow를 사용하지 말 것을 명시적으로 권고합니다.
  - **모델**: `gpt-5.6-sol`(품질)과 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 제품군은 CLI와 API Platform에서 공통으로 제공되지만, ChatGPT 계정으로 모든 모델을 사용할 수 있는 것은 아닙니다. allowlist는 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 사용하면 경고가 표시됩니다. Plus 요금제에서 Luna는 5시간 단위 기간마다 250~2,000개 메시지를 제공하는 반면 Sol은 10~100개를 제공합니다. 따라서 모든 일괄 처리에는 `--eco` 모드를 권장합니다.
  - **수정된 버그 — 전체 작업에 성공하고도 `regen_translations.sh`이 오류로 종료됨**: `trap ... EXIT`은 `main()`의 `local` 변수인 `failed_log`을 참조했지만, trap이 실행될 때는 이 변수가 더 이상 존재하지 않았습니다. `set -u` 환경에서는 이로 인해 `failed_log: unbound variable`가 발생했고, 번역 28개가 모두 올바른데도 스크립트가 종료 코드 1로 끝났습니다. 그 결과 가장 비용이 큰 단계인 재생성 직후에 `release.sh --auto`(`set -e`)이 중단될 수 있었습니다. 변수를 전역으로 바꾸고 trap에서 변수의 존재 여부를 검사하도록 했습니다. 유용한 부수 효과로, 지금까지 이 오류에 가려졌던 실제 번역 실패가 최종 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: `regen_translations.sh`의 새로운 환경 변수로, Provider 기본값보다 특정 모델을 우선 사용하도록 강제합니다. 예를 들어 대량 처리용 `--eco` 모델 대신 구독 할당량의 최상급 모델로 재생성하려면 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 사용할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때 `REGEN_PROVIDER=codex`을 사용할 수 있습니다. 사용자 모르게 구독 할당량을 소비하지 않도록 자동 감지는 절대 하지 않습니다. 병렬 처리를 시작하기 전에 토큰을 순차적으로 한 번 갱신합니다. Codex 갱신 토큰은 회전식이며 일회용이므로 동시 작업이 `codex login` 세션을 무효화할 수 있기 때문입니다. 동시 실행 수도 4로 줄였습니다.
  - **관련 refactor**: 전체 호출 체인에 네 번째 boolean을 전달하는 대신 Provider 이름을 반환하는 `_resolve_provider()`을 사용하여 `_dispatch_provider_call`의 매개변수를 8개에서 6개로 줄였습니다. 최소한의 `Namespace`로 `translate(..., use_mistral=True)`을 호출하는 테스트를 보존하기 위해 명시적 boolean은 계속 `args`보다 우선합니다.
  - **테스트**: 새 파일 `tests/test_codex_provider.py`에 48개 테스트를 추가하여 argv, 정리된 환경, 머리말 금지 계약, silent failure, timeout/killpg, back-off, preflight, Provider 선택, Gemini 추론 cascade, Claude 블록 필터링, 여러 문단으로 된 뉴스 인용을 검증합니다. 전체 제품군은 290개 테스트입니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 참조 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 행 25개, HTML 링크 13개, 이미지 13개, URL 19개, 문자 단위까지 동일한 코드 블록, 남은 placeholder 0개). 69KB 뉴스 기사에 `--news` 모드를 적용했을 때 `gpt-5.6-luna`과 `gpt-5.6-sol` 출력 모두 en/ja/ar에서 후속 애플리케이션 validator를 통과했습니다. `account/rateLimits/read`로 측정한 사용량은 `--eco` 모드에서 계수기의 반올림 임계값 미만(5시간 단위 기간의 0%)으로 유지되었습니다.

- **1.9.2** 중첩 괄호 또는 프랑스어 접두사가 있는 뉴스 출처 URL 추출 수정(2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`의 출처 URL 추출에는 정규식 `re.search(r"\((.+?)\)", attribution)`을 사용했습니다(괄호 사이를 lazy capture). `(relayé par [@user sur X](https://x.com/.../123))` 같은 출처 표기에서는 괄호가 중첩되어 있으므로(`(` 바깥 괄호 + Markdown 링크의 `]()`), 처음 만난 `)`에서 capture가 중단되어 문자열이 잘리고 프랑스어 접두사까지 포함되었습니다. 결과는 `relayé par [@user sur X](https://x.com/.../123`이며, 마지막 `)`가 누락되었습니다. 그 결과 `_validate_news_post`이 번역된 출력에서 이 문자열을 찾으려 할 때 항상 실패했습니다. 이유는 두 가지로, `)`이 잘렸고 “전달자”가 `relayed by`/`weitergeleitet von`/…로 번역되었기 때문입니다. low → medium → high → gpt-5.5 전체 cascade가 통과할 수 없었습니다.
  - **수정**: 정규식을 `re.search(r"\]\(([^)]+)\)", attribution)`으로 변경했습니다. Markdown 링크의 `](url)`만 구체적으로 대상으로 삼아 프랑스어 접두사나 잘림 없이 **순수 URL만** capture하며, 이 불변성은 번역 중 `#URL{N}#` placeholder로 보존됩니다. 문제가 된 다음 두 패턴을 모두 안정적으로 처리합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥 괄호가 없는 프랑스어 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 2개를 새로 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그를 정확히 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`을 사용한 변형)
  - **검증 공백**: `check-editorial-coverage.py`은 편집 문법을 검증하지만 translator가 번역할 수 있는지는 검증하지 않습니다. 향후 개선 사항(v1.9.2 범위 밖)으로, dry-run에서 출처 추출을 시뮬레이션하여 게시 **전에** 위험한 패턴을 감지하는 검사를 추가할 수 있습니다.

- **1.9.1** 번역 marker 안내문의 CTA label i18n 수정(2026-05-10):

  - **수정된 버그**: 번역 파일 상단 marker 배너의 CTA 링크에 있는 `[Voir le projet sur GitHub ↗]` label이 `target_lang`를 따르지 않고 모든 대상 언어에서 **프랑스어**로 남아 있었습니다. URL과 저장소 slug를 보존하기 위해 Python 측에서 조립되므로 LLM에는 절대 노출되지 않으며, 따라서 번역 단계에서도 이를 수정할 수 없었습니다. v1.9에서 `marker` 형식을 추가한 뒤부터 발생한 silent regression입니다.
  - **수정**: 15개 언어를 각각 현지화된 label에 매핑하는 새 상수 `_VIEW_PROJECT_LABELS`을 추가했습니다. 이제 `_translation_note_invariants(target_lang)`와 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달합니다. 알 수 없는 언어에는 `fr` fallback을 적용합니다(안전성 확보 및 KeyError 방지).
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 조정했습니다(target_lang `ja` → 예상 일본어 label). 테스트 2개를 새로 추가했습니다. `test_source_link_label_localized_per_target_lang`은 라틴 문자, 표의 문자, abjad 문자를 포괄하는 7개 언어를 매개변수화하여 검증하며, 다른 하나는 `test_source_link_label_falls_back_to_french_for_unknown_target`입니다. `test_translation_note_position.py`의 테스트는 총 40개로 늘었습니다(기존 38개).
  - **하위 호환성**: 기본값이 있는 시그니처 `target_lang="fr"`을 사용하므로 `args.target_lang` 없이 호출하는 외부 프로그래밍 호출자도 수정 없이 계속 작동합니다.
- **1.9** 무음 실패 수정 + 완전한 품질 도구 체계 + 다중 위치 번역 주석 (2026-05-07):
  - **다중 위치 번역 주석 + "embed card" 마커 형식**:
    - 새로운 CLI 옵션 추가(기본값은 그대로 유지 → **호환성 유지**):
      - `--note_position {top,bottom,both}`(기본값: `bottom`): 번역된 파일의 위쪽, 아래쪽 또는 양쪽에 주석을 배치합니다.
      - `--note_format {legacy,marker}`(기본값: `legacy`):
        - `legacy`는 v1.8 동작(굵은 단락 `**…**`)을 **바이트 단위로 정확히** 재현합니다.
        - `marker`는 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)를 출력한 뒤, "GitHub repo embed card" 형태로 렌더링되도록 구성된 **3개 단락의 blockquote**를 출력합니다. 여기에는 inline code로 된 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM으로 번역된 설명, 표시되는 화살표가 포함된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 들어갑니다. 빌드 시 remark plugin에서 활용할 수 있습니다(jls42.org 블로그의 `remark-translation-banner` plugin 참조).
    - **LLM에 절대 전송되지 않는 불변 요소**: repo 제목과 GitHub URL은 설명 문장을 번역한 후 Python 측에서 조합됩니다. LLM은 `ai-powered-markdown-translator` slug나 `https://github.com/jls42/...`를 전혀 보지 않으므로 renderer, 대소문자 또는 scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter의 닫는 `---` 블록 **뒤에** 주석이 삽입됩니다(Astro Content Collections / gray-matter 안전성). `_split_frontmatter` helper는 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter에는 **`RuntimeError`를 발생시키며**, 잘못된 위치에 주석이 포함된 파일을 쓰는 대신 해당 파일이 `failed_files`에 표시됩니다.
    - **Whitelist 기반 모델 sanitizer**: `_sanitize_model`는 `[A-Za-z0-9._:/-]`에 포함되지 않는 모든 문자를 `_`로 바꾸며, 결과가 비어 있으면 `unknown`를 사용합니다. Astro remark plugin 측 validator와 일치하며 마커 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 refactor**: `_append_translation_note`(하나의 거대한 함수) → 순수 helper 7개(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). Builder와 composer를 분리했습니다(builder는 구분자가 없는 순수 블록을 반환하고, composer는 위치에 따라 `\n\n`를 적용). 실제 코드와 소스 helper가 동일한 3개 단락 assembler를 공유합니다.
    - **빈 줄을 보존하는 `_quote_lines`**: 각 줄 앞에 `> `를 붙이고 빈 줄은 `>` 하나로 변환합니다. 이를 통해 mdast가 blockquote를 줄바꿈이 포함된 단일 단락이 아니라 서로 구분된 3개 단락(제목 / 설명 / 링크)으로 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 단락 수에 따라 달라집니다(3개 = 완전한 card 형식, 2개 = 문장 + 링크, 1개 = fallback). Markdown 링크 `](`가 감지되면 1개 단락 fallback은 더 이상 **`**...**`로 감싸지 않습니다**(링크 주위의 `<strong>` 렌더링이 불안정하기 때문).
    - **상위 호환성**: `_compose_with_notes` 측에서 `getattr(args, "note_position", "bottom")`와 `getattr(args, "note_format", "legacy")`를 사용하므로 해당 속성이 없는 Namespace(기존 테스트와 외부 프로그래밍 방식 호출)도 변경 없이 계속 작동합니다.
  - **긴 번역의 무음 실패 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 추가: 결정론적 계층(원문 발췌가 그대로 발견되는지 확인) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k segment에서 잠재적인 truncation 방지, FR→JA/ZH/KO/AR/HI 교차 script 여유 확보)
    - Heading 인식 segmentation: segment 후반부의 H2/H3에 우선순위 부여(각 segment가 의미적으로 완전한 section으로 시작)
    - 0이 아닌 exit code까지 오류 전파: `translate_markdown_file`가 형식화된 상태 `success` / `failure` / `skipped`을 반환하고, 파일 하나라도 실패하면 `main()`가 `sys.exit(1)` 처리(single-file 및 batch)
    - 모든 provider에 empty-content guard 적용, source/output sanity ratio 검사(500자 이상에서 5% 미만이면 거부), code placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 후 정규화(heading에 붙은 구분자/링크), `reasoning_effort` 없이 `BadRequestError` retry
    - `langdetect==1.0.9` dependency 추가
  - **Pre-commit 품질 도구 체계**("완전한 EurekAI 유형", hook 14개):
    - Pre-commit: ruff(lint+format), shellcheck, prettier(md/yaml/json), detect-secrets(API key 4개 보호), Lizard(CCN ≤ 12), pre-commit-hooks v5(whitespace, EOF, large-files, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `./venv/bin/python`을 사용하는 로컬 wrapper를 `scripts/`에 배치
    - `scripts/audit_verdict.py`: unittest 11개가 포함된 pip-audit JSON parser이며, jls42-astro parser를 Python으로 이식한 버전
    - 초기 ruff 위반 7개 수정: B904(raise from) ×2, B007(unused dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard에서 `translate.py`를 일시적으로 제외(CCN 21~47인 함수 4개, refactor 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 포괄적인 coverage**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): 모든 push와 pull-request에서 분석하고 `coverage.xml`를 통해 coverage 측정
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` stdlib): 무음 실패 오류 체인의 여섯 연결 단계를 다룹니다.
    - `tests/test_orchestration.py`(+79개 테스트): `translate.py`의 orchestration 계층(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return branch)을 다룹니다.
    - `scripts/tests/test_audit_verdict.py`: subprocess를 통해 `main()`(stdin/stdout)과 `if __name__ == "__main__"` 블록의 coverage 확보
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`는 위치 × 형식 행렬(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 여러 줄 prefix 추가, 바이트 단위 상위 호환성(golden literal), sanitizer, frontmatter 분할(닫히지 않은 fence에서의 raise 포함), 3개 단락 형식, 2개 단락 fallback, 1개 단락 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않는지 assert하는 중요한 안전장치 `TestLLMPayloadExcludesInvariants`을 다룹니다. **190개 테스트 통과**, regression 0건.
  - 문서화: badge가 포함된 `README.md`(FR + 번역 14개), `CLAUDE.md`(pre-commit workflow + 상세한 CI 모니터링), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 버전 상향(2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token 제한 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder를 통한 영어 인용 보호, `LANG_FLAGS` mapping(15개 언어), 대상 언어별 flag 관리
  - 복원 전 news placeholder 검증(regression: LLM이 placeholder를 삭제하면 인용이 없는 출력이 아무 오류 없이 생성되던 문제)
  - `regen_translations.sh` script의 이식성 확보(절대 경로 사용, pwd dependency 없음)
  - README/CHANGELOG의 language bar에 프랑스어 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원래 파일 이름을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **Inline code 보존**: 이제 번역 중 backtick(`` `...` ``)이 보호됩니다.
  - System prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - Template 변수 `{variable}` 보호
    - 요청하지 않은 번역자 주석 금지
  - 364개 파일에서 성공적으로 테스트(jls42.org 블로그 migration)
- **1.6** 새로운 기능:
  - 번역용 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 순회하지 않고 단일 파일 번역(`--file`)
  - 새롭게 단순화된 이름 지정 pattern: `{base}-{lang}.md`
  - 모델 이름이 포함된 이전 형식을 유지하는 `--include_model` 옵션
  - 목록에 없는 모델을 기본 token 제한(128k)과 함께 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트했습니다.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`로 업데이트했습니다.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY`을 추가하고 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`로 업데이트했습니다.
  - **번역 prompt 최적화:**
    - 직접 번역과 번역 주석용 prompt의 명확성과 효율성을 높였으며, metadata와 특정 formatting 요소의 보존에 관한 상세한 지침을 포함했습니다.
  - **코드 refactor:**
    - Mistral AI client 초기화에 사용하던 `MistralClient`를 `Mistral` class로 교체했습니다.
    - 가독성과 유지보수성을 높이도록 import를 재구성했습니다.
    - 번역 시 원래 formatting을 보존하도록 텍스트 segmentation과 code block 처리를 개선했습니다.
  - **출력 파일 관리:**
    - 출력 파일 이름에서 모델과 언어의 순서를 바꾸어(예: `f"{base}-{args.target_lang}-{args.model}.md"`) 번역을 더 쉽게 정리하고 찾을 수 있도록 했습니다.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 코드를 정리했습니다.
    - script 구조와 가독성을 개선하기 위한 소규모 조정을 적용했습니다.
- **1.4** 새로운 기능:
  - 번역용 Anthropic Claude API 지원
  - 명확성과 효율성을 높이도록 prompt 최적화
  - 코드 유지보수성 향상을 위한 소규모 조정
- **1.3** 개선 사항 및 새로운 기능:
  - Code block 처리 개선
  - 출력 파일 관리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일 이름에서 모델과 언어의 순서 변경
- **1.2** Changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 최초 버전 - OpenAI API 지원

**gpt-5.6-sol로 프랑스어에서 한국어로 번역된 기사.**
