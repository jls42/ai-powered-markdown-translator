### 변경 이력

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.12.0** Provider `--use_opencode` : OpenCode, 오픈 소스 에이전트를 사용해 원하는 공급자로 — 로컬 모델, 계정·구독·키 없이 무료로 (2026-09-04):

  - **기존 일곱 경로와는 성격이 다른 여덟 번째 provider.** [OpenCode](https://opencode.ai)(MIT)는 모델 공급자가 아니라 사용자가 OpenCode 자체에서 구성한 공급자로 연결하는 _라우터_다. API 키, 구독(GitHub Copilot, ChatGPT, SuperGrok), 무료 모델을 **계정 없이** 제공하는 OpenCode Zen 게이트웨이, 또는 **로컬** 모델(Ollama, LM Studio, llama.cpp)을 사용할 수 있다. 이 스크립트는 Codex와 Grok을 제어하는 방식과 마찬가지로 비대화형 모드에서 `opencode run`을 제어하며, 동일한 하위 프로세스 기반(독립 프로세스 그룹, 타임아웃 시 `SIGTERM` 후 `SIGKILL`, 항상 닫힌 stdin, 정리된 환경)을 재사용한다. **두 번의 실제 번역**으로 검증했다. `opencode/mimo-v2.5-free`를 통해 이 README 전체를 영어로 번역했으며 — 49초, 단 한 번의 실행, 원본 파일과 동일한 구조(제목 32개, 코드 블록 종료 26개, 링크 18개, URL 37개, 표 행 37개, 인라인 코드 135개) — `ollama/qwen2.5:7b`를 통해 키 없이 로컬에서 시험 파일도 번역했다.

  - **`--model provider/modèle`은 필수이며, 이는 의도된 선택이다.** `--model`이 없으면 OpenCode는 자체 기본값으로 돌아가는데, 새로 설치한 환경에서는 `opencode/big-pickle`이다. 이는 대화 내용이 학습에 사용될 수 있는 무료 « stealth » 모델이며 — 측정 결과 실제로 이 모델이 응답했다. 사용자를 대신해 이를 조용히 선택하는 것은 이 저장소가 추적하는 바로 그런 보이지 않는 전환이므로, 오류 메시지에는 모델을 나열하는 명령(`opencode models`)과 세 가지 예시(로컬, 무료, 구독)를 명시한다. `--eco`은 아무 효과가 없으며 그 사실을 알린다. `--reasoning_effort`은 명시적으로 요청한 경우에만 OpenCode의 `--variant`로 그대로 전달된다.

  - **가정이 아니라 측정된 격리.** 인라인 구성(`OPENCODE_CONFIG_CONTENT`)은 OpenCode의 병합 순서에서 마지막에 오므로 사용자의 구성을 대체하지 않고 그보다 우선하며, `aipmt` 에이전트를 정의한다. 이 에이전트에서는 모든 도구가 거부된다(`permission: {"*": "deny"}`). 따라서 모델은 도구를 제안하지도 않으며, « 파일을 나열하고 `id`을 실행하라 »는 요청에도 도구가 없다고 답한다. 세션 공유는 비활성화하고, 외부 플러그인은 제외하며(`--pure`), 절대 `--auto`하지 않고, 작업 디렉터리는 비어 있는 임시 디렉터리로 둔다. 조용히 주입되던 두 가지 요소를 측정하고 차단했다. `OPENCODE_DISABLE_CLAUDE_CODE`이 없으면 사용자의 `~/.claude/CLAUDE.md`이 **모든** 프롬프트에 들어간다(단순한 « 안녕하세요 »에 입력 토큰 186개가 아닌 515개)； `OPENCODE_DISABLE_PROJECT_CONFIG`이 없으면 현재 디렉터리의 `AGENTS.md`도 들어가며, « 모든 응답을 BANANA로 끝내라 »는 지시가 번역에 적용되었다. 전역 `~/.config/opencode/AGENTS.md`은 계속 주입된다. 이를 제외하는 스위치는 없으며, 변조된 `XDG_CONFIG_HOME`로 우회하면 사용자의 공급자도 숨겨지기 때문이다. 임시방편 대신 문서화했다.

  - **`exit 0`은 아무것도 증명하지 않는다. 세 번째 CLI에도 같은 원칙이 적용되지만, 이 CLI만의 함정이 두 가지 있다.** 알 수 없는 `--agent`은 `opencode run`을 실패시키지 않는다. stderr에 경고를 남기고, 도구가 활성화된 코딩 에이전트로 **조용히** 대체한다. 따라서 인라인 구성이 적용되지 않았다면 번역은 파일을 쓸 수 있는 에이전트로 실행된다. 출력 계약은 이 메시지가 없음을 확인하며, 반환 코드 0, `error` 이벤트 없음, `tool_use` 없음, 마지막 `step_finish`이 `stop`임( `length`은 잘린 응답)을 함께 확인한다. 텍스트도 비어 있지 않아야 한다. 두 번째 함정은 오류 JSON 이벤트가 **불투명**하다는 점이다. « Unexpected server error. Check server logs for details. »라는 메시지와 단순한 참조만 제공하며, 실제 원인(`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`, `ProviderAuthError` 등)은 로그에만 존재한다. 따라서 `--print-logs --log-level ERROR`를 사용하고 stderr의 `error="…"` 필드를 읽되, 뒤따르는 Bun 트레이스는 제외한다. 이렇게 하면 알 수 없는 모델도 원인을 명시한 채 1초 만에 실패한다. `--title`은 추가 LLM 호출도 방지한다. 이것이 없으면 OpenCode가 `small_model`에 한 번 더 요청해 세션 제목을 생성한다.

  - **비밀 정보: Codex 및 Grok과 동일한 패턴 필터링, 단 하나의 명시적 예외.** `OPENCODE_API_KEY`은 보존된다. 이는 OpenCode 자체의 키( Zen 게이트웨이, Go 구독)이며, 이름으로 OpenCode에 전달되는 값이다. 즉 OpenCode의 `auth.json`에 해당하며, aipmt가 관리하거나 비용을 청구할 수 있는 키가 아니다. 공급자는 OpenCode에서 구성한다(`opencode auth login`, `opencode.json`). aipmt의 `.env`에는 절대 구성하지 않으며, 그 어떤 키도 하위 프로세스에 도달하지 않는다. 구독 CLI와 달리 CI에서 거부하지 않는다. 러너에서 API 키나 자체 호스팅 모델을 사용하는 것은 정당한 용도이기 때문이다.

  - **경로 순회 방지는 이제 원시 값이 아니라 보간된 값을 검사한다.** `provider/modèle`에는 1.10.0의 방어 로직이 거부하던 `/`이 포함되어 있었다. `--model`이 파일명 `--include_model`에 보간되므로, 거부는 올바른 동작이었다. 이제 파일명 레이블은 보간 전에 `/`, `\`, `:`을 `-`로 대체한다(`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`, 여기서 `:`는 Windows에서 허용되지 않음). 상위 방어 로직은 이 레이블을 검사한다. 따라서 `../../evil`는 대상 아래에서 단순한 이름 `doc-en-..-..-evil.md`이 되고, `..`만 계속 거부되며 `--target_lang ../x`도 거부된다. 범위 방어인 `_ensure_within_directory`는 변경 없이 두 번째 계층으로 유지된다.

  - **무료 모델과 로컬 모델에서 측정된 결과.** `opencode/mimo-v2.5-free`은 단락을 16초, 이 README를 49초에 번역했다. `opencode/big-pickle`은 200단어에 40초가 걸렸으며, 단독 요청은 각각 성공하는 상황에서 동시 요청 두 개는 5분 동안 응답이 없었다. `opencode/nemotron-3.5-lightning-free`은 3분 동안 아무 응답도 하지 않았다. 따라서 `REGEN_PROVIDER=opencode`을 사용하고 `REGEN_MODEL`를 필수로 하며 **2개 작업**을 병렬 실행한다. 로컬 환경에서는 Ollama가 컨텍스트를 4,096토큰으로 구성하는 경우가 많지만 세그먼트는 최대 16,000자이므로 `Modelfile`와 `PARAMETER num_ctx 32768`이 필요하다. 품질은 모델에 따라 달라진다. 시험 파일에서는 7B 모델이 목록 순서를 뒤집고 코드 블록 종료를 손상시킨 반면, 게이트웨이 모델은 모든 것을 보존했다.

  - **rate limit 재시도 지연은 공통화했다**(`_retry_on_rate_limit`). Codex와 Grok의 루프는 이름만 달랐고, 세 번째 복사본을 추가하면 중복 임계값을 넘게 된다. 세 CLI 오류는 동일한 `_CliCallError`에서 파생되며, 세 오류 중 하나라도 여기서 벗어나면 공유 루프가 더 이상 이를 감지하지 못하므로 이를 금지하는 테스트를 추가했다.

  - **테스트**: 새 파일 `tests/test_opencode_provider.py`(테스트 51개) — 완전한 출력 계약, 에이전트 대체, 로그에서 원인 읽기, 중복 제거된 텍스트 조각과 무시되는 합성 조각, 프로세스 그룹을 종료하는 타임아웃, 429 재시도 지연, 필수 및 검증된 모델, 비밀 정보 없는 사전 점검, 바이너리 해석, 디스패치 연결, 파일명 레이블 및 경로 순회 반례를 포함한다. `tests/test_review_hardening.py`은 새 provider에 대해서도 플래그의 상호 배타성과 비밀 정보 부재를 확장한다. 이제 게이트는 문서화된 argparse 플래그 **22개**를 요구한다. 전체 테스트는 **382개**다.

- **1.11.1** 문서 수정: README가 마침내 일곱 개의 provider 경로를 안내한다 (2026-09-03):

  - **1.11.0의 PyPI 페이지에는 « 4 APIs + Codex CLI »라고 적혀 있었다.** 코드가 제공하는 경로는 일곱 개다. API를 통한 OpenAI, Mistral, Claude, Gemini, Grok, 그리고 사용량별 과금 없이 구독으로 이용하는 Codex(ChatGPT)와 Grok이다. 두 가지 Grok 모드가 소개 문구와 _Multi-Provider_ 항목에서 누락되었고, 14개 번역도 이 오류를 반복했다. 패키지의 긴 설명은 버전별로 고정되므로, 진열 내용을 수정하려면 버전 번호가 필요했다. 이것이 이 버전의 유일한 존재 이유다. **코드 변경은 없다.**
  - `CLAUDE.md`은 게시물에서 도입한 내용과 일치하도록 조정했다. 게이트 카운터(16, `--full`에서 17), 활성 워크플로 11개, `gh pr checks`에 보이지 않는 두 Sonar/Codacy 카운터(hotspots, Codacy API), `# nosemgrep` 하나를 `ruff-format`로 옮긴 내용, OIDC 교환에 필요한 GitHub 환경, 그리고 _pending publisher_가 이름을 예약하지 않는다는 사실을 반영한다.

- **1.11.0** PyPI 게시: 먼저 `pip install ai-powered-markdown-translator`, 이어서 `aipmt` 명령을 실행하며 저장소를 복제할 필요가 없다 (2026-09-03):

  - **단일 파일 스크립트가 설치 가능한 패키지가 되었다.** `translate.py`은 루트에서 `src/aipmt/translate.py`로 이동했으며, 콘솔 진입점 `aipmt`과 그에 상응하는 `python -m aipmt`을 제공한다. 기여하려면 여전히 복제된 저장소가 필요하다. 테스트, 28개 번역, 품질 도구가 그곳에 있기 때문이다. 하지만 사용만을 위해 저장소를 복제할 필요는 없다.

    - **import 이름은 `aipmt`이며 `translate`이 아니다.** 충돌이 실제로 발생하고도 조용히 지나가기 때문이다. PyPI 패키지 `translate`(v3.8.1, 마지막 업로드 2026-07-06)는 같은 이름의 디렉터리를 설치한다. venv에서 재현한 결과 디렉터리가 모듈보다 우선하고, `translate.main`가 사라지며, 진입점은 `AttributeError`에서 실패한다. 그런데 `pip check`은 rc=0으로 « No broken requirements found »라고 응답한다. 사용자가 `pip install translate` 한 번만 실행해도 활용 가능한 진단 없이 CLI가 망가질 수 있었다. 실제 wheel로 반례를 확인했다. 패키지 위에 `pip install translate`를 설치해도 `aipmt --help`의 rc는 전후 모두 0이며, 두 CLI가 공존한다.
    - **배포 이름은 길게, 명령은 짧게.** `ai-powered-markdown-translator`은 PyPI 검색으로 패키지를 찾을 수 있게 한다. 이미 프로젝트를 아는 사람이 아니면 단독 약어는 검색하기 어렵기 때문이다. 게시의 목적은 바로 발견되는 것이었다. 그럴듯한 후보 두 개는 확인을 거쳐 제외했다. `ai-markdown-translator`는 2024년부터 npm에서 같은 목적의 도구가 사용 중이며 이 저장소보다 17개월 앞서 있었고, `aimt`는 `aim`(v3.29.1)와 한 글자 차이로, 같은 분야의 활성 패키지다. 이는 지속적인 혼동을 일으키기에 최악의 구성이다. 여기서 방법론적 함정도 확인했다. `pypi.org/project/<nom>/`는 어떤 이름이든 200을 반환한다(봇 방지 페이지). 신뢰할 수 있는 것은 JSON API뿐이다.
    - **평면 패키지 대신 `src/` 레이아웃.** 평면 패키지를 사용하면 테스트의 `sys.path.insert(..., "..")` 6개를 유지할 수 있지만, 바로 그것이 문제다. 이 파일들은 패키지가 아니라 소스 트리를 import하게 하므로 패키징 오류를 모두 가린다. 실제 비용은 대체 규칙 하나가 추가되는 것이다.

  - **이제 키를 한 번만 구성하면 된다.** 설치된 CLI에는 PERSISTENT 구성이 없었다. 환경 변수와 현재 디렉터리의 `.env`만 사용할 수 있었다. `find_dotenv`은 시스템 루트까지 거슬러 올라가므로 **홈 디렉터리에서 작업할 때**는 `~/.env`을 찾았지만, 다른 곳에서는 찾지 못했다. 이는 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라지는 적용 범위였다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`을 추가했다.

    - **우선순위는 코드에 하드코딩하지 않았다.** `load_dotenv`의 기본값인 `override=False`에서 자연스럽게 도출된다. 각 계층은 이전 계층이 비워 둔 부분만 채운다. 따라서 순서는 환경 변수 → 프로젝트의 `.env` → 사용자 구성이다. 이는 구조가 아니라 동작 테스트로 검증했다. 두 호출의 순서를 바꾸면 테스트가 실패하고, 세 번째 계층을 제거해도 실패한다.
    - **TOML이 아닌 `.env` 형식**을 의도적으로 사용한다. `python-dotenv`은 이미 의존성이며, 문법은 15개 README에 이미 문서화되어 있고, 같은 파일을 두 범위에서 모두 사용할 수 있다. 새로운 의존성이나 문법은 없다. 위치는 `XDG_CONFIG_HOME`이 **절대 경로**일 때 이를 따르며, 사양상 상대 경로는 무시한다. 그렇지 않으면 구성 위치가 다시 현재 디렉터리에 따라 달라지기 때문이다. Windows에서는 `APPDATA`을 사용한다.
    - **제외한 두 가지 선택지와 그 이유.** 시스템 키체인(`keyring`)은 데스크톱에서 더 안전하지만 headless 환경(서버, 컨테이너, CI)에서는 실패한다. 이는 바로 일괄 번역의 사용 사례이므로, opt-in에는 적합하지만 기본값으로는 부적합하다. `--api-key` 플래그를 사용하면 키가 셸 기록에 남고 `ps`에 노출된다.
    - **키가 없을 때 호출 스택을 더 이상 표시하지 않는다.** 사용자는 `site-packages`을 가리키는 Python 스택과 « 환경 또는 .env »라고만 말하는 메시지를 받았다. 이제 세 위치와 정확한 경로를 모두 나열하며, 명령은 2로 종료된다. 이 보호망은 의도적으로 **좁게** 적용된다. `except ValueError`은 구성 단계에만 적용한다. 전체 실행을 감싸면 번역 중 실제 버그가 안심시키는 메시지로 바뀌는데, 이것이 이 저장소가 추적하는 장애 방식이다. 이를 금지하기 위해 `main()`의 소스 코드를 읽는 테스트가 있다.

  - **수정 — 도구 설치 후 사용자의 `.env`이 한 번 무시되었다.** 인자 없는 `load_dotenv()`은 현재 디렉터리에서 올라가지 않고 호출자 파일에서 올라가므로, `site-packages`에서 시작한다. 자체 `.env`을 가진 프로젝트에서 실제 콘솔 진입점을 실행해 측정한 결과, `find_dotenv()`는 `''`을 반환하고 키를 로드하지 않았지만 `find_dotenv(usecwd=True)`은 키를 찾았다. 도구가 복제된 저장소에서만 실행되던 동안에는 버그가 존재하지 않았다. 그러나 게시 후에는 올바른 구성에서도 API 키가 « 누락 »되었다는 증상만 남긴 채 항상 발생했을 것이다.

  - **세 게이트는 아무것도 검증하지 않게 된 뒤에도 통과할 수 있었다.** 따라서 이동하기 전에 의도적으로 강화했다. 잡아내야 할 변경 후에 작성된 안전장치는 아무것도 증명하지 못한다. 각 게이트는 원본 저장소에서는 통과하고, 마이그레이션한 복사본에서는 실패한다. 양방향을 모두 측정했다.

    - **Lizard는 없는 경로를 아무 말 없이 무시한다.** rc=0, « 0 file analyzed »가 된다. 복잡도 게이트는 158개 함수 / 2247 nloc에서 3개 함수 / 34 nloc으로 줄어들고, 0바이트 출력을 내면서도 통과할 수 있었다. 이제 scope는 각 항목의 존재 여부를 검사하는 배열이다.
    - **없는 모듈에 대한 `coverage run --source=`도 실패하지 않는다.** stderr에만 경고를 남기고 unittest와 `coverage xml` 모두 rc=0을 반환하며, 보고서도 게시한다. 단, 1453개에서 141개 statements로 축소된 보고서다. 거의 분석되지 않았기 때문에 프로젝트가 정상으로 보일 수 있었다. 보고서를 보호하는 하한선은 두 가지다. 전체 합계와 측정된 가장 큰 파일이다.
    - **번역 최신성 탐색기는 호출 형식에 구조적으로 눈이 멀어 있다.** argparse 플래그를 기준으로 삼는데, 파일 이름을 바꿔도 바로 그 플래그는 바뀌지 않기 때문이다. 재현 결과 모듈을 옮겨도 15개 README는 여전히 존재하지 않는 명령을 문서화했고, 판정은 « 오래된 번역 없음 »이었다. 따라서 일곱 번째 절은 옵션이 아니라 호출 **형식**을 검사한다. Lizard hook은 실제 스크립트 scope와 대조한다. 해당 키 `files:`가 더 이상 일치하지 않아도 pre-commit을 실패시키는 것이 아니라 건너뛴다.

  - **`requires-python = ">=3.10"`는 더 이상 단순한 주장에 그치지 않는다.** `sonar-project.properties`은 실제로 아무도 실행하지 않았는데도 이미 3.10-3.12를 선언하고 있었다. 개발 환경에는 3.12만 있었기 때문이다. 이는 게시되면 공개적으로 드러날 내부 모순이었다. 이제 테스트 워크플로가 3.10, 3.11, 3.12에서 전체 테스트를 실행하며, 패키지를 설치하므로 공개된 버전 범위도 함께 검증한다.
- **하한선은 있고, 상한선은 없다.** `requirements.txt`은 테스트된 잠금 파일로 유지하고, `[project.dependencies]`은 공개 계약이 된다. 잠금 파일의 정확한 버전을 공개하면 다른 패키지를 사용하는 모든 사용자에게 충돌이 발생하기 때문이다. `<N+1` 상한선도 두지 않는다. 모든 메이저 버전 지연에서 릴리스 gate를 실패시키는 `check-deps-fresh.sh`과 정면으로 충돌하기 때문이다. 하한선 집합으로 문제가 해결되며, 반증 테스트 `openai==1.0.0`은 `ResolutionImpossible`로 종료되어 검사가 무엇이든 허용하는 것이 아니라 구분한다는 점을 입증한다. 또한 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지는 것을 방지하는 보호 장치가 있다. PyPI는 동일한 번호의 재사용을 허용하지 않는다.

  - **새로운 venv에서 처음부터 끝까지 검증됨**: 약 70KB 크기의 wheel에는 `aipmt/*.py`, dist-info와 라이선스만 포함된다. 22개 플래그를 사용한 `aipmt --help`의 rc=0, « usage: aipmt »를 표시하고 « usage: \_\_main\_\_.py »는 표시하지 않는 `python -m aipmt`, 정상 작동하는 `pipx` 설치, 그리고 무엇보다 **임의의 사용자 디렉터리에서 수행한 실제 fr→en 번역**이 확인되었다. 굵은 글씨, 목록, 인라인 코드, 링크와 URL은 보존되고 코드 블록은 번역되지 않았다. 마이그레이션 전의 318개 테스트는 전후 식별자 목록이 바이트 단위로 동일한 상태에서 통과했다. 테스트가 무력화되지 않았음을 입증하는 것은 « OK »가 아니라 바로 이것이다. 여기에 3계층 구성 테스트 12개가 추가되어 총 330개가 되었다.

- **1.10.0** Provider `--use_codex`(ChatGPT 구독 할당량), SDK 및 모델 업데이트, 여러 문단으로 구성된 news 인용 수정 (2026-08-29):

  - **보안 검토 — PR이 마련했지만 모든 곳에서 지키지는 못했던 두 가지 보호 장치**:

    - **Codex preflight가 전체 `.env`를 바이너리에 전달했다.** `_codex_preflight`은 **`env=` 없이** `subprocess.run`을 호출했다. 하위 프로세스는 `os.environ` 전체, 즉 `load_dotenv`가 로드한 `.env`의 전부를 상속했다. 계측된 가짜 바이너리로 측정한 결과, preflight에 **7개의 비밀값**이 도달했다. 6개 provider의 키와 `GITHUB_TOKEN` 하나였다. 반면 동일한 역할의 `_grok_preflight`은 `env=_grok_env()`을 제대로 전달하여 **0개**였다. 이 불일치는 PR 내부의 문제였다. 불과 몇 줄 아래에 이 불변 조건을 유지하기 위해 정확히 존재하는 `_strip_secret_env`가 있었기 때문이다. 공통 `_codex_env_base()`을 추출해 두 경로에서 공유했으며, 수정 후 측정 결과 양쪽 모두 비밀값은 0개였다.
    - **« `--deny` fail-closed » 속성이 사용된 형식을 포괄하지 못했다.** 주석은 알 수 없는 접두사의 규칙이 시작을 거부한다는 점을 근거로 Grok 격리를 정당화했다. 하지만 `grok 1.0.13`에서 측정한 결과 이 검증은 **괄호 형식에만** 존재했다. `--deny 'CeciNestPasUnOutil(*)'`은 « unknown tool prefix »로 시작을 거부하지만, `--deny 'CeciNestPasUnOutil'`는 조용히 허용된다. 그런데 `GROK_DENY_RULES`는 이름만 사용했으므로, xAI 측에서 도구 이름을 변경하면 측정된 유일한 격리 계층이 아무 신호 없이 제거된다. 게다가 해당 컴퓨터에서는 OS sandbox가 이미 적용되지 않는다. 이름이 지정된 8개 규칙은 `Prefix(*)`으로 통과하며, 각각 CLI에서 알려진 접두사인지 확인된다. catch-all `*`은 허용되는 유일한 리터럴 형식으로 그대로 유지된다. 검증되지 않은 형식으로 되돌아가는 것을 막는 테스트도 추가했다.
    - **그 외의 항목은 깨끗하게 검증됨**: 명령 주입 없음(어디서나 목록 형식을 사용하며, `shell=True`은 사용하지 않고, 문서 내용은 stdin 또는 `--prompt-file`를 통해 전달됨), 안전하지 않은 역직렬화 없음(`json.loads`만 사용하며 타입 보호 포함), 7개 페이로드에서 우회가 발견되지 않은 경로 탐색 수정, 그리고 CLI에서 실제로 적용되는 `--deny '*'`(`DENY_ENFORCED`이 workdir 밖 읽기에서 관찰됨).
    - 앞서 추가한 최신성 검사는 그 과정에서 자신의 원칙을 우회했다. PyPI 요청이 실패한 패키지를 조용히 건너뛰어 gate가 통과했기 때문이다. 이제 실제로 비교된 패키지 수를 집계하며, 적용 범위가 불완전하면 실패한다.

  - **의존성을 최신화하고, 지연이 재발하지 않도록 두 가지 안전망 추가**:

    - **지연은 실제로 지속되고 있었다**: `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22**. 모든 provider 호출의 TLS를 검증하는 루트 인증서 저장소가 2년이나 뒤처진 상태였다. 원인은 **`.github/dependabot.yml`가 없었다는 것**으로 확인되었다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하고, Dependabot은 CVE가 있는 의존성에 대해서만 PR을 제안한다. 따라서 `urllib3`과 `idna`은 bump했지만 두 SDK는 메이저 버전 하나만큼 뒤처진 채 남아 있었던 것이다.
    - **두 메이저 버전은 충돌 없이 공존한다.** 이전 추론에서 우려했던 것과 달리 `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**로 이전하고, `mistralai`와 `google-genai`은 `httpx<1`에 남지만 서로 다른 배포판이다. 실제 설치로 확인한 뒤, **7개의 provider 경로를 처음부터 끝까지 테스트**했다. OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI 및 Grok CLI 모두에서 각 출력의 인라인 코드와 링크가 보존되었다. « 두 HTTP 스택을 피한다 »는 선호 사항이지 차단 조건이 아니었으며, 측정으로 결론이 났다.
    - **`requirements.txt`는 실제 환경을 설명하지 않았다**: `google-auth`, `cryptography` 및 `opentelemetry` 스택은 작업 venv에 설치되어 있었지만 선언된 적이 없었다. 따라서 새로 설치하면 테스트한 환경을 재현할 수 없었다. 반대로 `tokenizers`, `huggingface-hub` 및 `PyYAML`은 해당 환경에 있었지만 어떤 코드에서도 import되거나 요구되지 않았으며, `mistralai` 1.x의 잔재였다. 파일은 직접 의존성만으로 구성한 venv의 완전한 폐쇄 집합으로 재생성되었다. `pip-audit`은 새 집합에서 알려진 취약점을 보고하지 않는다.
    - **`.github/dependabot.yml`**(신규)는 매주 버전, pip 및 github-actions 업데이트를 활성화한다. 마이너 버전과 패치는 하나의 PR로 묶는다. PR마다 패치 bump 하나만 올리면 결국 무시되고, 소음은 업데이트의 적이기 때문이다. **메이저 버전은 분리**하며, 각각 실제 호출을 통한 검증이 필요하다.
    - **`scripts/check-deps-fresh.sh`**(신규이며 gate에 연결됨)은 프로젝트 판정에 지연을 드러낸다. Dependabot은 제안할 뿐 보장하지 않으며, PR이 누적될 수도 있다. 메이저 지연은 실패, 마이너 지연은 경고로 처리한다. gate가 항상 빨간색이면 결국 무시되기 때문이다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 skip하고 **CI에서는 fail-closed**로 처리한다. 실행되지 않은 검사는 성공이 아니기 때문이다. 양쪽 방향으로 검증했다. 수정 전의 정확한 상태(`openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`)를 잡아내며, 마이너 지연에는 경고만 표시한다.

  - **이 PR 검토에서 나온 수정 사항** — 5명의 검토 에이전트가 diff를 철저히 살폈다. 아래 항목은 모두 수정 전에 **측정으로 재현**했으며, 그중 2개는 같은 버전에서 앞서 도입된 회귀였다.

    - **수정된 회귀 — `_NEWS_CITATION_REGEX`에 지수적 backtracking이 있었다.** 여러 문단 수정에서 반복문 안에 `(?:[ \t]*$|[ \t]+.*)`를 도입했다. `[ \t]+`과 `.*` 사이의 공백 공유가 모호했고, 이 모호성이 반복마다 증폭되었다. 패턴과 일치하지 않는, 완전히 합법적인 Markdown 들여쓰기인 `>   texte` 줄에서 측정한 결과 **14줄에 2,589ms**, 수정 후에는 0.04ms였으며 줄이 하나 추가될 때마다 약 9배씩 증가했다. `--news` 모드에서는 길고 형식에 맞지 않는 blockquote 하나만으로도 작업 timeout까지 번역이 멈출 수 있었고 원인을 식별할 수 없었다. 이제 반복문은 한 번에 전체 줄(`\n^>(?![ \t]*—).*`)을 소비하므로 반복마다 일치하는 방법이 하나만 남는다. 실제 231개 문서 말뭉치에서 검증한 결과 **캡처 차이는 0개**였고, 인용 423개가 동일했으며 여러 문단으로 된 본문 14개도 계속 확장되었다.
    - **두 provider 플래그를 동시에 사용해도 조용히 사용량이 과금되었다.** `--use_codex --use_mistral`은 허용되었고, `_select_provider_client`은 Mistral을 먼저 검사했으며, `_resolve_provider`은 명시적 Boolean에 우선순위를 부여했다. 두 플래그 모두 결국 Mistral로 수렴했다. 사용자는 구독 할당량을 요청했지만 사용량 기반 과금을 받았고, 경고는 전혀 없었다. 바로 이런 장애 모드를 막기 위해 `--use_codex`이 존재한다. 이제 6개의 provider 플래그는 모두 `add_mutually_exclusive_group`를 통과한다. **동작 변경**: 지금까지 조용히 허용되었던 두 provider를 함께 지정한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패한다.
    - **작업 완료 gate는 probe가 실패해도 통과했다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개는 반환 코드를 확인하지 않고 « stdout을 캡처하고 비어 있으면 결론 »을 내리는 방식을 따랐다. 예외(`FileNotFoundError` 등)가 stderr에 기록되고 stdout은 비어 있으면 검사는 « 알릴 내용 없음 »이라고 결론 내렸다. 이를 방지하기 위해 작성한 스크립트 내부에서 « `exit 0` 하나만으로는 아무것도 증명하지 못한다 »는 함정이 재현되었다. 이제 `probe()` helper가 반환 코드 0 **및** 종료 sentinel을 요구한다. 또한 probe는 기준 집합이 비어 있을 때 결론을 내리지 않는다. 빈 집합에 대한 assertion은 언제나 참이기 때문이다. 시연 결과, 위의 exclusive group 추가로 provider 플래그가 `*_group` 객체를 통과하게 되었고 기존 정규식 `parser\.add_argument\(`은 이를 더 이상 일치시키지 못했다. **21개 중 6개 플래그**가 조용히 범위 밖으로 빠졌지만 gate는 통과했다.
    - **비밀값 스캔이 6개 중 4개 provider를 놓쳤다.** `[A-Za-z0-9]` 클래스는 하이픈을 제외한다. `sk-proj-…`(현재 OpenAI 형식)과 `sk-ant-api03-…`는 두 번째 하이픈에서 실패했고, `AIza…`은 포함되지 않았다. 패턴을 확장하고 `.secrets.baseline`을 스캔에서 제외했다. 또한 `.env` 보호 장치는 `git diff --cached`를 조회했는데, 이는 index만 확인한다. **이미 커밋된** `.env`은 최악의 경우인데도 나타나지 않았다. 이제 `git ls-files`를 조회한다.
    - **Codex « token warm-up »은 실제 warm-up이 아니었다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`을 변경하지 않았다(mtime과 크기 모두 동일). 도움말에는 « Show login status »라고 표시되었다. 그런데 주석은 token을 « 한 번, 순차적으로 » 갱신하여 일회성 회전 token의 동시 갱신 위험을 무력화한다고 주장했다. 명시된 보호 기능은 존재하지 않았다. 이제 주석은 코드가 실제로 하는 일을 설명하며, 실제 대응책은 여전히 `max_jobs=4`이다. 또한 검사는 무시하던 `CODEX_BIN`를 준수한다. `codex`이 `PATH`에 없는 컴퓨터에서는 « 인증되지 않음 »으로 실패하여 오해를 부르는 진단이 발생했기 때문이다.
    - **`.env`가 하위 셸에서 source되었다.** `detect_provider`는 명령 치환으로 호출되므로 export가 상위로 전달되지 않았다. 따라서 `.env`에서 정의한 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`은 `main()`에서 수행한 조회에 보이지 않아, 올바른 구성에서도 « Grok 바이너리를 찾을 수 없음 »이라고 결론 내렸다.
    - **동시 실행 수가 명시된 상한을 50% 초과했다.** 보호 장치가 README/CHANGELOG 쌍을 시작한 뒤에 배치되어, `max_jobs=2`의 측정 피크는 **3개**였다. 주간 할당량을 Chat/Imagine/Voice와 공유하며 측정할 수 없는 Grok에서는 스크립트가 스스로 설정한 상한이 지켜지지 않은 것이다. 최종 개수는 표시되었지만 28과 비교되지 않아, 파일 하나가 없어도 감지되지 않았다.
    - **Grok 출력 계약: 이제 `stopReason`이 없으면 실패한다.** 코드가 계약에서 요구하는 `end_turn` 대신 « `end_turn` **또는 없음** »을 적용하고 있었다. 필드가 없는 payload나 CLI 업데이트로 필드 이름이 변경된 payload는 보호 장치를 조용한 no-op으로 만들었다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류하지 않는다. 소진된 것은 라운드 예산이므로 재시도해도 결과는 같고 90초 대기만 발생하기 때문이다. `quota`도 rate limit 표식에서 제외했다. 그 이유는 `_codex_is_rate_limited`의 docstring이 이미 설명하고 있었지만 Grok에는 적용되지 않았기 때문이다.
    - **Gemini cascade는 모델별로 메모이제이션된다.** 각 segment마다 `minimal`에서 다시 시작했지만 기본 모델은 이를 거부했다. 따라서 정상 경로에서도 segment마다 400 왕복이 발생하고 동일한 경고가 반복 출력되었다. 경고가 수백 번 반복되면 더 이상 읽히지 않는다. 그렇게 경고가 가면이 된다.
    - **기타**: CI 거부 메시지가 Codex용으로 하드코딩되어 `--use_grok_cli` 사용자를 `XAI_API_KEY`가 아닌 `OPENAI_API_KEY`으로 안내했다. `provider.capitalize()`은 « Grok_cli »와 « Openai »를 표시했다. 하위 프로세스 기반에 대한 주석은 두 CLI 모두에 « shim »을 일반화했지만 Grok 바이너리는 네이티브 ELF다. 올바른 근거는 « 자체 하위 프로세스를 spawn하는 agent »이다. `subprocess`의 SAST finding 12개는 `# nosec` / `# nosemgrep`으로 표시하고 근거를 추가했다. `shell=True` 없는 목록 형식으로 주입이 불가능하며 문서 내용은 argv를 통해 전달되지 않는다.
    - **이제 agent 하위 프로세스에는 어떤 비밀값도 들어가지 않는다.** 이름을 지정한 deny-list는 **과금** 불변 조건만 보호했다(Codex에는 `OPENAI_API_KEY`, Grok에는 `XAI_API_KEY` 없음). 측정 결과 다른 비밀값 **7개**가 여전히 각 하위 프로세스에 들어갔다. Anthropic, Mistral, Google 및 Gemini 키, 다른 CLI의 키, 그리고 비밀값은 아니지만 트래픽을 재지정하는 `OPENAI_BASE_URL`이었다. 이 두 CLI는 **agent**이며, Grok CLI는 많은 Linux 컴퓨터에서 적용 가능한 OS sandbox 없이 실행된다. 이제 필터링은 이름을 지정한 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)으로 수행한다. 따라서 이 코드가 알지 못하는 사용자의 `.env`에 추가된 변수도 포함된다. CLI에는 어떤 변수도 필요하지 않다. 인증은 `~/.codex`와 `~/.grok`에 저장되며 환경에는 절대 저장되지 않는다. 강화된 환경을 사용해 두 provider 각각으로 **실제 번역을 완료**하여 이를 검증했다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`(테스트 21개)이 provider 플래그의 배타성, `stopReason` 계약, news 정규식의 선형성, CI 거부 메시지, Gemini 메모이제이션 및 하위 프로세스 환경에 비밀값이 전혀 없음을 고정한다. 마지막 assertion은 **일반적**이다. 목록에 이름이 없는 키에서도 실패한다. 반면 기존 expurgation 테스트는 자체 상수의 거울에 불과해 자체 반복문이 고장 난 것 외에는 아무것도 감지할 수 없었다. 전체 테스트는 **311개**가 되었다.
- **Grok 프로바이더 2종 추가**: `--use_grok` (xAI API, 키 `XAI_API_KEY`, 사용량 기준 과금) 및 `--use_grok_cli` (공식 Grok Build CLI, Grok 구독에서 차감 — `--use_codex`과 동일한 원리).
    - **API 모드, 약 40줄**: xAI 엔드포인트는 OpenAI와 호환되므로 클라이언트와 `_call_openai`를 그대로 재사용하고, `base_url`만 변경한다. 한 가지 조정만 필요했으며 모두에게 이점이 돌아간다. `finish_reason`가 이제 `end_turn`를 허용한다. 이는 OpenAI가 `stop`을 내보내는 위치에서 xAI가 내보내는 형식이다. 모델은 `grok-4.6`(품질) 및 `grok-4.3`(경제형)이다. 참고로 Grok의 경제형 모델은 저장소에서 여전히 가장 비싸다 — 백만 토큰당 $1.25/$2.50인 반면 `mistral-small-latest`는 $0.15/$0.60이다. 이 프로바이더는 가격이 아니라 모델 다양성을 위해 선택해야 한다.
    - **CLI 모드**: Codex를 본떠 만들었지만, 실제 환경 때문에 네 가지 차이가 있다 — 프롬프트는 파일로 전달된다(`--prompt-file`, CLI가 stdin을 읽지 않으며 argv의 세그먼트는 `ps`에 노출될 수 있음), stdout에는 단일 JSON 객체가 출력된다(JSONL도 아니고 `-o` 파일도 아님), 구독에서는 `grok-4.6`과 `grok-4.5`만 제공되며, sandbox를 적용할 수 없다(아래 참조). 하위 프로세스 실행은 `_codex_run_process`에서 Codex와 공통화했으며, 이미 테스트된 기존 Codex 프로바이더의 나머지 부분은 건드리지 않았다.
    - **`exit 0`은 아무것도 증명하지 않는다. 측정 결과**: 인증되지 않은 상태에서 CLI는 **stdout**에 `{"type":"error","message":"Not signed in."}`을 기록하고 종료 코드 **0**을 반환한다. 거부나 턴 초과도 같은 방식으로 동작한다. 따라서 출력 계약에는 네 가지 조건이 동시에 필요하다: 종료 코드 0, 오류 payload 없음, `stopReason == end_turn`, 비어 있지 않은 텍스트. 사전 점검도 같은 논리를 따른다. 연결이 끊긴 상태에서도 `grok models`는 0으로 종료되며, stdout에 « not authenticated »가 있는 경우에만 그렇게 판단할 수 있다.
    - **격리: 의도적으로 비대칭이며 문서화됨.** Codex가 `--sandbox read-only`에서 실행되는 것과 달리, Grok의 sandbox는 두 가지 독립적이고 우회할 수 없는 시스템 원인으로 인해 최신 Linux 환경의 많은 시스템에서 적용할 수 없다. 이를 해결하려면 `sudo`가 필요하다. AppArmor는 Ubuntu 24.04부터 권한 없는 user namespace를 차단한다(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨). 또한 컨테이너 런타임 소켓 deny-list는 `/run/podman`가 `0700`일 때 실패한다(리졸버는 `ErrorKind::NotFound`만 복구하고, EACCES는 치명적 오류가 됨). 핵심 함정은 **통합된** 프로필을 적용할 수 없을 때 **격리되지 않은 상태로 조용히 시작한다**는 점이다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않으며, 조용히 대체하지도 않는다 — stderr로 경고한다. 보호는 CLI의 `--deny` 규칙에 의존하며, catch-all인 `*`도 포함된다. 이는 측정된 유일한 _fail-closed_ 계층이다(알 수 없는 접두사의 규칙이 시작을 거부하게 함). `GROK_TRANSLATE_SANDBOX=read-only`를 사용하면 이를 강제할 수 있으며, 시스템이 이를 준수할 수 없으면 시작이 실패한다.
    - **안전장치**: `XAI_API_KEY`, `GROK_API_KEY` 및 `GROK_SANDBOX`은 하위 프로세스 환경에서 제거된다(키가 있으면 사용량 기준 과금으로 전환되고, 상속된 `GROK_SANDBOX`는 적용할 수 없는 프로필을 강제하면서 오해의 소지가 있는 메시지를 표시함). MCP/hooks/skills/agents 스위치 비활성화, `--disable-web-search`, `--no-subagents`, `--no-plan`, 임시 workdir, CI에서의 거부, 프로세스 그룹을 종료하는 timeout, rate limit에 대한 back-off를 적용한다. `--max-turns`은 1이 아니라 6으로 설정된다. 도구 턴 후에 카운터가 증가하므로 1이면 출력이 잘린다.
    - **할당량**: Grok 풀은 주간 단위이며 **Chat, Imagine, Voice와 공유**된다. 이를 노출하는 명령은 없으며, `account/rateLimits/read`로 사용량을 산출할 수 있는 Codex와는 다르다. 따라서 `regen_translations.sh`는 동시성을 2로 제한하고 이를 명시적으로 경고한다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`(테스트 24개). 전체 테스트는 **290개**다.
  - **수정된 버그 — EN 다중 문단 인용이 (`--news` 모드에서) 부분적으로만 보호됨**: `_NEWS_CITATION_REGEX`은 인용 본문으로 `>` 줄이 **연속해서** 이어지는 경우만 허용했다. 인용이 여러 문단에 걸쳐 있을 때(빈 `>` 줄로 구분됨), 마지막 문단만 캡처되어 placeholder로 대체되고 앞부분은 LLM으로 전달되어 번역되었다 — 이는 `--news`가 보장하기 위해 존재하는 목적과 정확히 반대다. 이제 반복 패턴은 내부의 `>` 빈 줄을 허용하고 탐욕적이지 않게 동작하여, 이탤릭체 줄 앞의 `>` 빈 줄에서 멈추며 첫 번째 빈 줄에서 멈추지 않는다.
    - **측정된 범위**: 실제 198개 문서로 구성된 코퍼스에서 해당 인용은 419개 중 11개였다. 회귀는 없었다 — 새 정규식은 정확히 동일한 수의 인용을 캡처하며, 다중 문단 본문만 확장된다(본문 408개는 동일하고 11개가 확장됨). 기여 줄 `> — …`은 여전히 본문에 흡수될 수 없다(lookahead 유지).
    - **엔드투엔드 증명**: ja/ar로 번역한 69KB 문서에서, 이전에는 인용의 첫 문단이 일본어로 `> GLM-5.3がオープンウェイト化。` 렌더링되고 아랍어에서도 같은 방식으로 번역되었지만, 이제는 `> GLM-5.3 is now open-weight.`로 유지된다. 영어 인용 줄 수는 9개에서 10개로 돌아가 소스와 같아졌다.
    - 참고: 이 결함은 후속 검증기에서는 감지되지 않았다. 검증기는 인용이 존재하는지만 확인하고 완전한지 여부는 확인하지 않는다.
  - **기본 프로바이더에서 측정된 비용 절감**: `_openai_extra_kwargs`은 모델이 `gpt-5`로 시작하기만 하면 `reasoning_effort="medium"`을 전송했으며, `--eco`인 경우도 포함되었다. 10단어 문장 하나를 번역하는 `gpt-5.4-mini` 측정 결과: `medium` → reasoning 토큰 45개와 출력 토큰 65개, `none` → 0개와 14개였다. 추론은 번역에 아무런 이점이 없으며 모든 파일의 모든 세그먼트에서 비용이 발생했다. 기본값은 이제 `none`이며 `--eco`에서 적용되고, 그 외에는 `medium`로 유지된다. CLI에서 명시적으로 전달한 값이 계속 우선한다. `--reasoning_effort`은 이제 `none` 및 `xhigh`도 `low`/`medium`/`high`와 함께 허용한다(모든 모델이 모두 허용하는 것은 아니다: 예를 들어 `minimal`은 `gpt-5.4-mini`에서 거부됨 — 기존의 매개변수 없는 재시도가 이 경우를 처리함).
  - **SDK 업데이트 및 Gemini 마이그레이션**: `google-generativeai`(2025-11-30 지원 종료, 저장소 보관됨)을 통합 SDK **`google-genai`**로 교체했다 — `genai.Client(api_key=...)` 후 `client.models.generate_content(model=, contents=, config=)`을 사용하며, 시스템 프롬프트는 세그먼트에 연결하지 않고 `system_instruction`로 전달한다. `mistralai`은 **2.9.4**로 업데이트했다(import는 `from mistralai.client import Mistral`가 됨; 이전 방식은 `ImportError`을 발생시키며 wheel에서 확인됨). `anthropic`은 **0.125.0**, `openai`은 **2.54.0**으로 업데이트했다 — `httpx2`로 전환하기 전의 마지막 버전이며, venv에서 두 HTTP 스택이 공존하지 않도록 하기 위한 것이다. 그에 따라 `httpx` 0.28.1 및 `pydantic` 2.13.5도 사용할 수 있게 되었다.
  - **실제 테스트에서 발견된 두 가지 회귀, 문서에서는 발견되지 않음**:
    - `anthropic` ≥ 1.0은 `max_tokens`가 10분을 초과할 것으로 예상되는 비스트리밍 호출을 클라이언트 측에서 거부한다(`ValueError: Streaming is required...`). 이 안전장치는 0.34.2에는 없었으며 `max_tokens=32768`를 사용하는 모든 Claude 호출을 중단시켰다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 전체 응답만 사용하는 호출을 스트리밍으로 전환하지 않도록 했다.
    - `thinking_level="minimal"`은 Gemini 카탈로그의 일부 모델에서만 허용된다. `gemini-3.1-flash-lite`은 이를 지원하지만 `gemini-3.7-flash` 및 `gemini-3.1-pro-preview`은 400 오류로 거부한다. 따라서 `_gemini_generate_with_fallback`을 도입했다. `minimal` → `low` → thinking_config 없음의 연쇄 fallback이며, 기존 OpenAI fallback과 같은 방식이다 — 최적화 매개변수 하나 때문에 번역이 실패해서는 안 된다.
  - **기본 모델 갱신**, 모두 실제 호출로 검증됨: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 배치에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%); Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜가 없는 정식 ID); Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(안정 버전이며 `3.5-flash-lite`보다 저렴). Mistral은 변경하지 않았으며, `mistral-large-latest`은 네 모델 중 가격 대비 품질이 가장 우수한 모델로 유지된다. 참고로 `gemini-3.1-pro-preview`보다 최신인 Pro급 Gemini 모델은 존재하지 않는다 — 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 계열은 전부 Flash다.
  - **Gemini 전환 전 측정한 A/B 테스트**: `README.md`를 `gemini-3.1-pro-preview`으로 일본어 번역한 뒤 `gemini-3.7-flash`로 번역했다. 구조는 완전히 동일했다(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존). 처리 시간은 **8초 대 48초**였다. 번역이나 비라틴 스크립트에 대해 두 모델을 비교한 공개 벤치마크가 없었으므로, 그렇지 않았다면 전환은 단순한 추정에 근거했을 것이다.
  - **Claude 응답 블록 필터링**: `_call_claude`은 유형을 필터링하지 않고 `block.text for block in response.content`을 수행했다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 삽입하는데, 이 블록은 `.text`이 아니라 `.thinking`를 노출한다 — 첫 번째 세그먼트에서 불투명한 `AttributeError`을 만나면 번역이 실패했을 것이다. 이제 `thinking`, `redacted_thinking`, `tool_use` 및 `tool_result` 블록은 제외된다(알 수 없는 유형이 텍스트를 담고 있을 때도 허용하도록 음수 목록 사용). 텍스트 블록이 전혀 없는 응답은 명시적인 오류를 발생시킨다. `thinking={"type": "disabled"}`은 모든 호출에 전달된다.
  - **`MODEL_TOKEN_LIMITS` 동기화**: 지원 종료일이 지난 모델을 제거했다(2026-07-31에 제거된 `magistral-*` 계열, 2026-06-01의 `gemini-2.0-*`, 2026-03-09의 `gemini-3-pro-preview`, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`). 한도도 수정했다: Mistral 128K → **256K**(Large 3 / Small 4 생성), Gemini 1,000,000 → **1,048,576**(실제 입력 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 계열 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest` 및 `ministral-*` 계열을 추가했다. 참고로 이러한 한도는 여전히 참고용이며, `translate()`가 세그먼트 분할을 `min(16000, limite)`으로 제한한다.
- **Provider `--use_codex`**: 공식 Codex CLI(`codex exec`)를 비대화형 모드로 제어하는 다섯 번째 provider입니다. 사용량에 따라 과금되는 API를 호출하는 대신, 이미 결제한 ChatGPT 구독 할당량에서 번역량이 차감됩니다. OpenAI가 이 용도에 대해 문서화한 유일한 방식입니다. 요금제별 가용성 매트릭스에는 Plus/Pro/Business/Enterprise에서 « Codex SDK, `codex exec`, and scriptable workflows »를 사용할 수 있다고 명시되어 있으며, `~/.codex/auth.json`의 토큰은 Platform API 호출을 인증하지 않습니다(이 스크립트는 해당 토큰을 절대 읽지 않으며, 인증과 갱신은 CLI가 계속 관리합니다).
  - **pip로 설치 가능한 Codex 바이너리, 더 이상 npm만 필요하지 않음**: `_resolve_codex_binary()`는 먼저 `CODEX_BIN`에서, 다음으로 `PATH`에서, 마지막으로 OpenAI가 배포하는 공식 Python 패키지 **`openai-codex-cli-bin`**에서 바이너리를 찾습니다(`openai-codex` SDK의 의존성입니다). 따라서 Python 프로젝트에서 `--use_codex`를 사용하기 위해 더 이상 전역 npm 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가되지 않습니다. 바이너리 크기가 약 250MB이므로 선택적 provider를 위해 모든 사용자가 이를 설치해야 하게 되기 때문입니다. 처음부터 끝까지 검증되었습니다. `PATH`에 `codex`가 없는 상태에서도 패키지된 바이너리를 찾아 6초 만에 전체 번역이 완료됩니다.
  - **« 구독 모드 » 보장**: `OPENAI_API_KEY` 및 `CODEX_API_KEY`는 하위 프로세스 환경에서 제거됩니다. 이 보호 장치가 없으면 `.env`에 있는 키로 인해 눈에 보이는 신호 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 바로 이 provider가 방지하려는 상황입니다.
  - **테스트로 고정한 CLI 함정**:
    - `codex exec`는 프롬프트를 인수로 전달한 경우에도 **stdin을 읽습니다**. stdin을 닫지 않으면 명령이 모델을 호출하지 않은 채 시간 제한까지 대기합니다(재현 결과: 180초 후 exit 124, 0바이트). 따라서 `communicate(input=...)`는 필수입니다.
    - npm으로 설치되는 `codex`는 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 실제 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 할당량을 계속 소비합니다. 따라서 `Popen(start_new_session=True)` + `os.killpg`가 필요합니다.
    - CLI는 `turn.failed`를 출력하고도 종료 코드 0으로 끝날 수 있습니다. JSONL 출력(`--json`)을 반환 코드와 함께 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **속도 제한 시 백오프**: CLI에는 내부 재시도(`max_retries = 0`)가 구현되어 있지 않습니다. 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행됩니다. « quota »라는 단어가 복구 가능한 429 오류와 최종적인 `insufficient_quota` 모두에 나타나기 때문입니다.
  - **CI 보호**: `CI` 또는 `GITHUB_ACTIONS`가 정의되어 있으면 `--use_codex`가 거부됩니다. 구독 인증은 공유 runner를 위한 방식이 아니며, OpenAI는 공개 저장소에서 이 workflow를 사용하지 말 것을 명시적으로 권고합니다.
  - **모델**: `gpt-5.6-sol`(품질) 및 `gpt-5.6-luna`(`--eco`)입니다. `gpt-5.6-*` 제품군은 CLI와 Platform API에서 공통으로 사용되지만, ChatGPT 계정이 모든 모델에 접근할 수 있는 것은 아닙니다. allowlist는 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 지정하면 경고가 발생합니다. Plus 요금제에서 Luna는 5시간 창당 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개만 제공합니다. 따라서 `--eco`는 모든 일괄 처리에 권장되는 모드입니다.
  - **수정된 버그 — `regen_translations.sh`가 완전히 성공했는데도 오류를 반환함**: `trap ... EXIT`가 `failed_log`를 참조하고 있었는데, 이는 `main()`의 `local` 변수로서 trap이 실행될 때는 더 이상 존재하지 않았습니다. `set -u`에서는 이로 인해 `failed_log: unbound variable`가 발생하고 스크립트가 1로 종료되었습니다. 28개의 번역은 정상인데도, 가장 비용이 많이 드는 단계인 재생성 직후 `release.sh --auto`(`set -e`)가 중단될 수 있었습니다. 변수를 전역으로 옮기고 trap에서 변수의 존재 여부를 검사합니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 이제 종료 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: provider 기본값보다 우선하여 특정 모델을 강제하는 `regen_translations.sh`의 새 환경 변수입니다. 예를 들어 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`를 사용하면 볼륨 지향 모델인 `--eco` 대신 구독 할당량의 고급 모델로 재생성할 수 있습니다.
  - **`regen_translations.sh`**: 명시적인 opt-in으로 사용할 수 있는 `REGEN_PROVIDER=codex`입니다. 사용자가 모르는 사이 구독 할당량을 소비하지 않도록 자동 감지는 하지 않습니다. Codex 갱신은 순환식이며 일회성이므로, 동시 작업이 `codex login` 세션을 무효화할 수 있습니다. 따라서 병렬 처리를 시작하기 전에 토큰을 순차적으로 한 번 갱신하고 동시성은 4로 낮춥니다.
  - **관련 리팩터링**: `_dispatch_provider_call`는 provider 이름을 반환하는 `_resolve_provider()`를 통해 매개변수를 8개에서 6개로 줄였습니다. 전체 호출 경로에 네 번째 불리언 값을 전달하는 방식은 사용하지 않습니다. 명시적인 불리언 값은 `args`보다 계속 우선하여, 최소한의 `Namespace`로 `translate(..., use_mistral=True)`를 호출하는 테스트를 보존합니다.
  - **테스트**: `tests/test_codex_provider.py`라는 새 파일(48개 테스트)이 추가되었습니다. argv, 정리된 환경, 서문 금지 계약, 무음 실패, timeout/killpg, 백오프, preflight, provider 확인, Gemini 추론 cascade, Claude 블록 필터링, 여러 문단의 news 인용을 다룹니다. 전체 테스트 수는 290개입니다.
  - **실제 검증**: 프로젝트의 `README.md`를 Codex로 **14개 언어**로 번역한 결과, 기준 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 행 25개, HTML 링크 13개, 이미지 13개, URL 19개, 문자 단위로 동일한 코드 블록, placeholder 잔여물 0개). `--news` 모드에서 69KB 뉴스 기사를 처리했을 때 `gpt-5.6-luna`와 `gpt-5.6-sol` 출력 모두 en/ja/ar에 대한 후속 애플리케이션 validator를 통과했습니다. `account/rateLimits/read`로 측정한 사용량은 `--eco` 모드에서 카운터의 반올림 임계값 아래로 유지되었습니다(5시간 창의 0%).

- **1.9.2** 괄호 중첩 또는 FR 접두사가 있는 news attribution URL 추출 수정 (2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`의 attribution URL 추출은 `re.search(r"\((.+?)\)", attribution)` 정규식을 사용했습니다(괄호 사이를 lazy capture). `(relayé par [@user sur X](https://x.com/.../123))`과 같은 attribution에서는(중첩 괄호: 바깥쪽 `(` + markdown link의 `]()`) 첫 번째 `)`에서 캡처가 중단되어 문자열이 잘리고 FR 접두사가 포함되었습니다: `relayé par [@user sur X](https://x.com/.../123`(마지막 `)` 없음). 그 결과 `_validate_news_post`가 번역된 출력에서 이 문자열을 찾다가 항상 실패했습니다. 두 가지 원인이 있었습니다. `)`가 잘렸고, "relayé par"가 `relayed by`/`weitergeleitet von`/...로 번역되었습니다. low → medium → high → gpt-5.5 전체 cascade를 통과할 수 없었습니다.
  - **수정**: 정규식이 `re.search(r"\]\(([^)]+)\)", attribution)`으로 변경되었습니다. markdown link의 `](url)`를 구체적으로 대상으로 하여 **순수 URL만** 캡처합니다(FR 접두사와 잘림 없음). 번역 중에는 `#URL{N}#` placeholder를 통해 invariant가 보존됩니다. 다음 두 가지 문제 패턴에 모두 대응합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥 괄호가 없는 FR 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 2개를 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B에서 재현한 정확한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`을 포함한 변형)
  - **보완이 필요한 범위**: `check-editorial-coverage.py`는 편집 문법은 검증하지만 translator를 통한 번역 가능성은 검증하지 않습니다. 가능한 개선 사항( v1.9.2 범위 밖)은 게시 전에 위험한 패턴을 감지하도록 dry-run에서 attribution 추출을 시뮬레이션하는 검사입니다.

- **1.9.1** 번역 marker 노트의 CTA label i18n 수정 (2026-05-10):

  - **수정된 버그**: 번역된 파일 상단 marker 배너의 CTA 링크 label인 `[Voir le projet sur GitHub ↗]`가 대상 언어에 맞지 않고 모든 언어에서 **프랑스어로** 남아 있었습니다. `target_lang`를 따르지 않았습니다. URL과 저장소 slug를 보존하기 위해 Python 측에서 조립되므로 LLM은 이를 전혀 보지 못하며, 번역 단계에서도 수정할 수 없었습니다. v1.9에서 `marker` 형식을 추가한 이후 발생한 조용한 회귀였습니다.
  - **수정**: 15개 언어를 현지화된 label에 매핑하는 새 상수 `_VIEW_PROJECT_LABELS`를 추가했습니다. `_translation_note_invariants(target_lang)` 및 `_assemble_translation_note_paragraphs(phrase, target_lang)`가 이제 대상 언어를 전달합니다. 알 수 없는 언어에서는 안전을 위해 KeyError가 발생하지 않도록 `fr`로 대체합니다.
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`를 수정했습니다(target_lang `ja` → 예상되는 일본어 label). 새 테스트 2개를 추가했습니다: `test_source_link_label_localized_per_target_lang`(라틴 문자, 표의 문자, 아브자드를 포함하는 7개 언어에 대해 매개변수화) 및 `test_source_link_label_falls_back_to_french_for_unknown_target`. 전체적으로 `test_translation_note_position.py`에 40개 테스트가 있습니다(기존 38개).
  - **Backward-compat**: 기본값이 있는 `target_lang="fr"` 시그니처를 사용하므로, `args.target_lang` 없이 호출하는 외부 프로그래밍 호출자도 수정 없이 계속 작동합니다.
- **1.9** 무음 실패 수정 + 종합 품질 도구 + 다중 위치 번역 노트 (2026-05-07):
  - **다중 위치 번역 노트 + "embed card" 형식 마커**:
    - 새로운 CLI 옵션(추가 옵션, 기본값 변경 없음 → **호환성 유지**):
      - `--note_position {top,bottom,both}` (기본값: `bottom`): 번역된 파일의 상단, 하단 또는 양쪽에 노트를 배치합니다.
      - `--note_format {legacy,marker}` (기본값: `legacy`):
        - `legacy`은 v1.8 동작(굵은 단락 `**…**`)을 **바이트 단위로 동일하게** 재현합니다.
        - `marker`는 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)를 출력한 뒤, **GitHub 저장소 임베드 카드**와 같은 렌더링을 위한 구조화된 **3개 단락 blockquote**를 출력합니다. 프로젝트 제목은 인라인 코드(`**\`ai-powered-markdown-translator\`\*\*`), 설명은 LLM이 번역하며, 화살표가 표시된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 포함됩니다. remark 플러그인으로 빌드 시 활용할 수 있습니다(jls42.org 블로그 → `remark-translation-banner` 플러그인 참고).
    - **LLM에 절대 전송하지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문장을 번역한 후 Python 측에서 조합합니다. LLM은 slug `ai-powered-markdown-translator` 또는 `https://github.com/jls42/...`를 절대 보지 않으므로, 어떤 renderer/이상 문자/스킴도 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter의 **닫는 `---` 블록** 뒤에 노트를 삽입합니다(Astro Content Collections / gray-matter 안전성). Helper `_split_frontmatter`는 파일 시작 부분의 `---\n…\n---\n`를 감지하고 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter가 있으면 **`RuntimeError`를 발생**시키며, 파일은 잘못된 위치에 노트를 삽입한 채 기록되지 않고 `failed_files`로 전달됩니다.
    - **허용 목록 기반 모델 sanitizer**: `_sanitize_model`은 `[A-Za-z0-9._:/-]`에 속하지 않는 모든 문자를 `_`로 대체하며, 비어 있으면 `unknown`으로 대체합니다. remark Astro 플러그인 측 validator와 일치하며, 마커 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 리팩터링**: `_append_translation_note`(단일 모놀리식 함수)에서 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`)로 분리했습니다. Builder와 composer를 분리했으며(builder는 구분자 없는 순수 블록을 반환하고, composer는 위치에 따라 `\n\n`을 적용), production과 source helper는 동일한 3단락 조립기를 공유합니다.
    - **`_quote_lines`의 빈 줄 보존**: 각 줄 앞에 `> `을 붙이고, 빈 줄은 `>`만 남도록 변환합니다. 이를 통해 mdast가 blockquote 안에서 줄바꿈이 포함된 하나의 단락이 아니라 제목 / 설명 / 링크라는 서로 다른 3개 단락을 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 단락 수에 따라 동작합니다(3개 = 완전한 카드 형식, 2개 = 문장 + 링크, 1개 = 대체 형식). Markdown 링크 `](`가 감지되면 1단락 대체 형식은 더 이상 `**...**`로 감싸지 않습니다. 링크 주위의 `<strong>` 렌더링이 불안정하기 때문입니다.
    - **하위 호환성**: `_compose_with_notes` 측의 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")` — 이러한 속성이 없는 Namespace(기존 테스트, 외부 프로그래밍 호출)도 수정 없이 계속 작동합니다.
  - **긴 번역에서 발생하는 무음 실패 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 추가: 결정론적 계층(소스에서 추출한 내용의 verbatim 재발견) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` 허용 목록: 허용 목록 밖의 모든 상태(truncation, content_filter 등)에서 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k 세그먼트에서 발생하는 잠재적 truncation과 FR→JA/ZH/KO/AR/HI 스크립트 간 여유 부족 방지)
    - heading-aware 세그먼트화: 세그먼트 후반부에서 H2/H3에 우선순위를 부여(각 세그먼트가 완전한 의미 단위의 섹션으로 시작)
    - 오류를 non-zero exit code까지 전파: `translate_markdown_file`는 `success` / `failure` / `skipped`의 타입 상태를 반환하며, 하나 이상의 파일이 실패하면 `main()` `sys.exit(1)`(단일 파일 및 배치 모두)
    - 모든 provider에 빈 콘텐츠 guard, 소스/출력 sanity ratio(≥ 500자, < 5% = 거부), 코드 placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 후 정규화(heading에 붙은 구분자/링크 수정), `reasoning_effort` 없이 `BadRequestError` 재시도
    - 의존성 `langdetect==1.0.9` 추가
  - **pre-commit 품질 도구**("완전한 EurekAI 유형", 14개 hook):
    - Pre-commit: ruff(린트+포맷), shellcheck, prettier(md/yaml/json), detect-secrets(보호된 API 키 4개), Lizard(CCN ≤ 12), pre-commit-hooks v5(공백, EOF, 대용량 파일, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `scripts/`의 로컬 wrapper가 `./venv/bin/python`을 사용
    - `scripts/audit_verdict.py`: 11개의 unittest로 구성된 pip-audit JSON parser, jls42-astro parser를 Python으로 이식
    - 초기 ruff 위반 7건 수정: B904(raise from) ×2, B007(사용하지 않는 dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard는 일시적으로 `translate.py`를 제외(CCN 21-47인 함수 4개, 리팩터링 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 철저한 커버리지**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): 모든 push 및 pull-request에서 분석, `coverage.xml`를 통한 coverage
    - README 상단에 SonarCloud 배지 11개(Quality Gate, Security/Reliability/Maintainability 등급, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` stdlib): 무음 실패 오류 체인의 여섯 연결 고리를 모두 커버
    - `tests/test_orchestration.py`(+ 테스트 79개): `translate.py`의 orchestration 계층(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return 분기) 커버
    - `scripts/tests/test_audit_verdict.py`: `main()`(stdin/stdout) 및 subprocess를 통한 `if __name__ == "__main__"` 블록 커버
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`가 위치 × 형식 매트릭스(E2E `marker+top|bottom|both` 및 `legacy+top|bottom|both` 포함), 다중 줄 접두사 처리, byte-for-byte 하위 호환성(golden literal), sanitizer, frontmatter 분할(닫는 fence가 없을 때의 raise 포함), 3단락 형식, 2단락 fallback, 1단락 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않음을 검증하는 중요한 안전장치 `TestLLMPayloadExcludesInvariants`를 커버합니다. **테스트 190개 통과**, 회귀 0건.
  - 문서: 배지가 포함된 `README.md`(프랑스어 + 14개 번역), `CLAUDE.md`(pre-commit workflow + 상세한 watch CI), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 업데이트 (2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k), `gemini-3.1-pro-preview`(1M)의 토큰 제한 추가
  - 초기 `--news` 모드: EN 인용 보호용 placeholder `#NEWSQUOTE\d+#`, 매핑 `LANG_FLAGS`(15개 언어), 대상 언어별 플래그 처리
  - 복원 전 news placeholder 검증 추가(회귀: LLM이 placeholder를 삭제하면 인용 없는 출력이 무음으로 생성됨)
  - `regen_translations.sh` 스크립트를 이식 가능하게 변경(절대 경로, pwd 의존성 없음)
  - README/CHANGELOG language bar에 Français 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원본 파일명을 유지하는 `--keep_filename` 옵션
  - API 키를 자동으로 불러오는 `.env` 파일 지원
  - **인라인 코드 보존**: 백틱(`` `...` ``)을 이제 번역 중 보호
  - 시스템 prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - 템플릿 변수 `{variable}` 보호
    - 요청하지 않은 번역자 노트 금지
  - 364개 파일에서 성공적으로 테스트(jls42.org 블로그 마이그레이션)
- **1.6** 새로운 기능:
  - 번역을 위한 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 순회하지 않는 단일 파일 번역(`--file`)
  - 단순화된 새로운 명명 패턴: `{base}-{lang}.md`
  - 모델명을 포함한 이전 형식을 유지하는 `--include_model` 옵션
  - 기본 토큰 제한(128k)이 적용되는 목록 외 모델 지원
  - README 14개 언어로 번역
- **1.5** 개선 사항:
  - **API 키 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`로 업데이트.
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`로 업데이트.
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`로 업데이트.
  - **번역 prompt 최적화:**
    - 직접 번역 및 번역 노트용 prompt를 더 명확하고 효율적으로 개선했으며, 메타데이터와 특정 서식 요소 보존에 대한 자세한 지침을 포함했습니다.
  - **코드 리팩터링:**
    - Mistral AI client 초기화를 위해 `MistralClient`을 `Mistral` 클래스로 교체.
    - 가독성과 유지보수성을 높이도록 import 재구성.
    - 번역 중 원본 서식을 보존하도록 텍스트 세그먼트화와 코드 블록 처리 개선.
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 반대로 변경(예: `f"{base}-{args.target_lang}-{args.model}.md"`)하여 번역의 정리와 검색을 쉽게 개선.
  - **기타 개선 사항:**
    - 불필요한 빈 줄을 제거하여 코드 정리.
    - 스크립트의 구조와 가독성을 개선하기 위한 소규모 조정.
- **1.4** 새로운 기능:
  - 번역을 위한 Anthropic Claude API 지원
  - 명확성과 효율성 향상을 위한 prompt 최적화
  - 코드 유지보수성 향상을 위한 소규모 조정
- **1.3** 개선 사항 및 새로운 기능:
  - 코드 블록 처리 개선
  - 출력 파일 처리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 모델과 언어 순서 반전
- **1.2** changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**gpt-5.6-luna로 프랑스어에서 한국어로 번역된 기사.**
