### 변경 이력

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.11.0** PyPI에 게시: 저장소를 복제하지 않고 `pip install ai-powered-markdown-translator` 다음 `aipmt` 명령을 사용 (2026-08-31):

  - **단일 파일 스크립트가 설치 가능한 패키지가 됨.** `translate.py`가 루트에서 `src/aipmt/translate.py`로 이동하고, 콘솔 진입점 `aipmt` 및 이에 대응하는 `python -m aipmt`가 추가되었습니다. 기여하려면 여전히 복제된 저장소가 필요합니다. 테스트, 28개 번역 및 품질 도구가 그 안에 있기 때문입니다. 하지만 사용하기 위해서는 더 이상 필요하지 않습니다.

    - **가져오기 이름은 `aipmt`이며, 절대 `translate`이 아닙니다.** 실제로 조용한 충돌이 발생하기 때문입니다. PyPI 패키지 `translate`(v3.8.1, 마지막 업로드 2026-07-06)은 같은 이름의 디렉터리를 설치합니다. 가상 환경에서 재현하면 디렉터리가 모듈보다 우선하여 `translate.main`가 사라지고, 진입점이 `AttributeError`에서 중단됩니다. 그런데 `pip check`은 rc=0으로 “No broken requirements found”라고 응답합니다. 사용자 환경에서 간단히 `pip install translate`만 실행해도 진단 가능한 정보 없이 CLI가 망가질 수 있었습니다. 실제 wheel로 반증도 확인했습니다. 패키지 위에 `pip install translate`을 실행하고, 전후로 `aipmt --help`가 rc=0을 반환하며 두 CLI가 공존합니다.
    - **배포 이름은 길게, 명령은 짧게.** `ai-powered-markdown-translator`는 PyPI 검색으로 패키지를 찾을 수 있게 합니다. 아는 사람만 찾을 수 있는 단독 약어는 프로젝트를 모르는 사용자를 찾지 못하게 하므로, 이번 게시의 목적과 맞지 않습니다. 그럴듯한 후보 두 개는 검증을 통해 제외했습니다. `ai-markdown-translator`은 2024년부터 npm에서 같은 목적의 도구가 사용 중이며 이 저장소보다 17개월 앞섰고, `aimt`은 `aim`(v3.29.1)과 한 글자 차이일 뿐이며 같은 분야의 활성 패키지입니다. 지속적인 혼동을 일으키기에 최악의 구성입니다. 참고로 방법론상의 함정도 있습니다. `pypi.org/project/<nom>/`는 봇 방지 페이지 때문에 어떤 이름이든 200을 반환하며, JSON API만 신뢰할 수 있습니다.
    - **평면 패키지보다 `src/` 레이아웃을 사용.** 평면 패키지는 테스트의 여섯 `sys.path.insert(..., "..")`을 그대로 유지했을 것이며, 바로 그것이 문제입니다. 해당 항목들은 패키지가 아니라 소스 트리를 가져오게 하므로 패키징 오류를 숨길 수 있습니다. 실제 비용은 대체 규칙 하나가 추가되는 것입니다.

  - **수정 — 도구 설치 후 사용자의 `.env`가 무시됨.** 인수 없이 실행한 `load_dotenv()`는 현재 디렉터리가 아니라 호출자 파일에서, 즉 `site-packages`에서 거슬러 올라갑니다. 자체 `.env`를 가진 프로젝트에서 실제 콘솔 진입점을 실행해 측정한 결과, `find_dotenv()`은 `''`을 반환하고 키를 불러오지 못했지만 `find_dotenv(usecwd=True)`은 키를 찾았습니다. 도구가 복제된 저장소에서만 실행될 때는 존재하지 않던 버그였으며, 게시 후에는 올바른 구성에서도 API 키가 “누락”되었다는 증상만 남긴 채 항상 발생했을 것입니다.

  - **아무것도 검증하지 않게 된 상태에서도 세 개의 게이트가 통과될 수 있었음.** 의도적으로 이동 전에 강화했습니다. 잡아내야 할 변경 이후에 작성된 안전장치는 아무것도 증명하지 못하기 때문입니다. 각 게이트는 원본 저장소에서는 통과하고, 이동한 복사본에서는 실패합니다. 두 방향 모두 측정했습니다.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시함**: rc=0, “0 file analyzed”. 복잡도 게이트는 158개 함수 / 2247 nloc에서 3개 함수 / 34 nloc으로 바뀌고, 출력은 0바이트가 되었을 것입니다. 이제 범위는 각 항목의 존재 여부를 확인하는 배열입니다.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`가 실패하지 않음**: stderr에만 경고를 출력하고 unittest와 `coverage xml` 모두 rc=0을 반환하며, 보고서도 계속 게시됩니다. 측정된 문 수가 1453에서 141로 줄었지만 말입니다. 거의 분석되지 않았기 때문에 프로젝트가 정상으로 보였을 것입니다. 이제 두 개의 하한이 보고서를 보호합니다. 전체 합계와 측정된 가장 큰 파일입니다.
    - **번역 최신성 검사가 호출 형식에 구조적으로 눈이 멂**: 파일 이름 변경으로는 바뀌지 않는 argparse 플래그를 기준으로 삼기 때문입니다. 재현 결과, 모듈을 이동해도 15개의 README가 여전히 존재하지 않는 명령을 문서화하는데 판정은 “오래된 번역 없음”이었습니다. 따라서 일곱 번째 섹션은 옵션이 아니라 형식을 확인하며, Lizard 훅은 실제 스크립트 범위와 대조됩니다. 해당 훅의 `files:` 키가 더 이상 일치하지 않을 때 pre-commit을 실패시키는 것이 아니라 건너뛰게 합니다.

  - **`requires-python = ">=3.10"`는 더 이상 단순한 주장에 그치지 않음.** `sonar-project.properties`는 실제로 실행된 적이 없는데도 이미 3.10-3.12를 명시하고 있었습니다. 개발 환경에는 3.12만 있었기 때문이며, 이는 게시 시 공개적으로 드러났을 내부 모순입니다. 이제 테스트 워크플로가 3.10, 3.11, 3.12에서 전체 테스트를 실행하고, 패키지를 설치하여 공개된 버전 범위도 검증합니다.

  - **하한만 설정하고 상한은 없음.** `requirements.txt`는 테스트된 잠금 버전으로 유지하고, `[project.dependencies]`는 공개 계약이 됩니다. 잠금 파일의 정확한 버전을 게시하면 다른 패키지를 사용하는 모든 사용자에게 충돌이 발생하기 때문입니다. `<N+1` 상한도 두지 않습니다. 이는 주요 버전 지연이 발생하면 릴리스 게이트를 실패시키는 `check-deps-fresh.sh`와 정면으로 충돌하기 때문입니다. 하한 집합으로 문제를 해결했으며, 반증 테스트인 `openai==1.0.0`은 `ResolutionImpossible`로 종료되어 검사가 모든 것을 허용하지 않고 구분한다는 사실을 입증합니다. 또한 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지지 않도록 방지하는 검사가 있습니다. PyPI는 동일한 번호를 재사용할 수 없기 때문입니다.

  - **새 가상 환경에서 처음부터 끝까지 검증**: `aipmt/*.py`만 포함하고 dist-info와 라이선스만 포함하는 69,768바이트 wheel, 22개 플래그와 함께 rc=0을 반환하는 `aipmt --help`, “usage: \_\_main\_\_.py”가 아니라 “usage: aipmt”를 표시하는 `python -m aipmt`, 정상 작동하는 `pipx` 설치, 그리고 무엇보다 **임의의 사용자 디렉터리에서 실제로 fr→en 번역**을 수행했습니다. 굵게 표시된 텍스트, 목록, 인라인 코드, 링크와 URL은 보존되고 코드 블록은 번역되지 않았습니다. 마이그레이션 전후로 식별자 목록이 바이트 단위까지 동일한 318개 테스트가 통과했습니다. 테스트가 무력화되지 않았음을 증명하는 것은 “OK”가 아니라 바로 이 사실입니다.

- **1.10.0** `--use_codex` provider(ChatGPT 구독 할당량), SDK 및 모델 업데이트, 여러 문단으로 구성된 뉴스 인용 수정 (2026-08-29):

  - **보안 검토 — PR에서 제시했지만 모든 곳에서 지키지 못한 두 가지 안전장치**:

    - **Codex 사전 점검이 전체 `.env`를 바이너리에 전달함.** `_codex_preflight`가 **`env=` 없이** `subprocess.run`을 호출하여 하위 프로세스가 전체 `os.environ`를 상속했고, 그 결과 `load_dotenv`가 불러온 `.env` 전체가 전달되었습니다. 계측된 가짜 바이너리로 측정한 결과, 사전 점검에 도달한 비밀은 **7개**였습니다. 6개 provider의 키와 `GITHUB_TOKEN` 하나였으며, 올바르게 `env=_grok_env()`를 전달하는 대응 경로 `_grok_preflight`에서는 **0개**였습니다. 이 불일치는 PR 내부에 존재했습니다. 몇 줄 떨어진 곳에 있는 `_strip_secret_env`는 정확히 이 불변 조건을 유지하기 위해 존재합니다. 이제 `_codex_env_base()`를 추출하여 두 경로가 공유하며, 수정 후 측정 결과 양쪽 모두 비밀은 0개였습니다.
    - **“`--deny` fail-closed” 속성이 사용된 형식을 포함하지 않음.** 주석은 알 수 없는 접두사의 규칙이 시작을 거부한다는 점을 근거로 Grok 격리를 정당화했습니다. 그러나 `grok 1.0.13`에서 측정한 결과, 이 검증은 **괄호 형식에만** 존재했습니다. `--deny 'CeciNestPasUnOutil(*)'`은 시작을 거부(“unknown tool prefix”)하지만 `--deny 'CeciNestPasUnOutil'`은 조용히 허용됩니다. 그런데 `GROK_DENY_RULES`는 이름만 사용했으므로, xAI 측에서 도구 이름을 변경하면 측정된 유일한 격리 계층이 아무 신호 없이 제거됩니다. 게다가 OS 샌드박스가 이미 적용되지 않는 환경일 수 있습니다. 이름이 지정된 8개 규칙은 `Prefix(*)`으로 통과하며 각각 CLI에서 알려진 접두사인지 확인됩니다. catch-all `*`는 유일하게 허용되는 리터럴 형식으로 유지됩니다. 검증되지 않은 형식으로 되돌아가지 못하도록 테스트를 추가했습니다.
    - **그 밖의 항목은 깨끗하게 검증됨**: 명령 주입 없음(어디에서도 목록 형식만 사용하며 `shell=True`는 사용하지 않음, 문서 내용은 stdin 또는 `--prompt-file`으로 전달), 안전하지 않은 역직렬화 없음(`json.loads`만 사용하며 타입 검사 포함), 7개 페이로드에서 우회가 발견되지 않은 경로 순회 수정, 그리고 CLI가 실제로 `--deny '*'`를 적용함(`DENY_ENFORCED`가 workdir 외부 읽기에서 관찰됨).
    - 앞서 추가한 최신성 검사도 그 원칙 자체를 우회하고 있었습니다. PyPI 요청이 실패한 패키지를 조용히 건너뛰어 게이트가 통과했기 때문입니다. 이제 실제로 비교한 패키지 수를 세고, 검사 범위가 불완전하면 실패합니다.

  - **의존성을 최신화하고, 지연이 재발하지 않도록 두 가지 안전망 추가**:

    - **지연은 실제로 존재했고 지속적이었음**: `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22** — 모든 provider 호출의 TLS를 검증하는 루트 인증서 저장소가 2년이나 뒤처져 있었습니다. 원인은 **`.github/dependabot.yml`가 없었다는 것**으로 확인되었습니다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하고, Dependabot은 CVE가 지정된 의존성에 대해서만 PR을 제안합니다. 따라서 `urllib3`와 `idna`는 업데이트했지만 두 SDK가 주요 버전에서 뒤처진 채 남아 있었던 것입니다.
    - **두 주요 버전은 충돌 없이 공존함**: 이전 추론과 달리 `openai` 3.x와 `anthropic` 1.x는 `mistralai`와 `google-genai`이 `httpx<1`에 유지되는 동안 **`httpx2`**로 이전하지만, 서로 다른 배포판입니다. 실제 설치로 확인한 뒤, **7개 provider 경로를 처음부터 끝까지 테스트**했습니다. OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI 및 Grok CLI 모두에서 각 출력의 인라인 코드와 링크가 보존되었습니다. “두 HTTP 스택을 피하자”는 선호 사항일 뿐 차단 요인이 아니었으며, 측정 결과가 이를 결정했습니다.
    - **`requirements.txt`가 실제 환경을 설명하지 못했음**: `google-auth`, `cryptography` 및 `opentelemetry` 스택은 작업 가상 환경에 설치되어 있었지만 선언된 적이 없으므로, 새로 설치해도 테스트된 환경을 재현하지 못했습니다. 반대로 `tokenizers`, `huggingface-hub` 및 `PyYAML`은 어디에서도 가져오거나 요구하지 않았는데, `mistralai` 1.x의 잔재로 포함되어 있었습니다. 이제 파일은 직접 의존성만으로 구축한 가상 환경의 완전한 폐쇄 집합으로 다시 생성됩니다. `pip-audit`은 새 집합에서 알려진 취약점을 보고하지 않습니다.
    - **`.github/dependabot.yml`**(신규)은 매주 버전 업데이트, pip 및 github-actions 업데이트를 활성화합니다. 마이너 버전과 패치는 하나의 PR로 묶습니다. PR마다 패치 하나만 올리면 결국 무시되며, 소음은 업데이트의 적이기 때문입니다. **주요 버전은 분리**하고, 각각 실제 호출을 통한 검증을 요구합니다.
    - **`scripts/check-deps-fresh.sh`**(신규, 게이트에 연결됨)은 프로젝트 판정에서 지연을 드러냅니다. Dependabot은 제안할 뿐 보장하지 않으며, PR이 누적될 수도 있습니다. 주요 버전 지연 → 실패, 마이너 버전 → 경고입니다. 게이트가 항상 빨간색이면 결국 무시되기 때문입니다. PyPI에 연결할 수 없음 → 로컬에서는 명시적 건너뛰기, **CI에서는 fail-closed**입니다. 실행되지 않은 검사는 성공이 아니기 때문입니다. 양방향으로 검증했습니다. 수정 전의 정확한 상태(`openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`)를 잡아내며, 마이너 버전에는 경고만 표시합니다.

  - **이 PR 검토에서 도출된 수정 사항** — 5명의 검토 에이전트가 diff를 면밀히 점검했으며, 아래 항목은 모두 수정 전에 **측정을 통해 재현**되었습니다. 그중 두 가지는 바로 이 버전의 앞부분에서 도입된 회귀였습니다.
- **수정된 회귀 — `_NEWS_CITATION_REGEX`에 지수적 백트래킹이 있었습니다.** 다중 문단 수정으로 반복문 안에 `(?:[ \t]*$|[ \t]+.*)`가 도입되었습니다. `[ \t]+`와 `.*` 사이의 공백 공유가 모호했고, 이 모호성이 반복마다 증폭되었습니다. 패턴과 일치하지 않는, 완전히 합법적인 Markdown 들여쓰기인 `>   texte` 줄에서 측정한 결과 **14줄에 2,589ms**가 걸렸지만 수정 후에는 0.04ms였고, 줄이 하나 추가될 때마다 약 9배씩 증가했습니다. `--news` 모드에서는 길고 형식에 맞지 않는 blockquote 하나만으로도 원인을 식별할 수 없는 상태에서 작업이 timeout될 때까지 번역이 멈출 수 있었습니다. 이제 반복문은 한 번에 전체 줄을 소비하므로(`\n^>(?![ \t]*—).*`), 반복마다 일치 방식이 하나만 남습니다. 실제 231개 문서 코퍼스로 확인한 결과 **캡처 차이 0건**, 동일한 인용문 423개, 다중 문단 본문 14개도 모두 계속 확장됩니다.
    - **두 provider 플래그를 동시에 지정하면 조용히 사용량 과금이 발생했습니다.** `--use_codex --use_mistral`가 허용되었고, `_select_provider_client`는 먼저 Mistral을 검사했으며, `_resolve_provider`는 명시적 불리언에 우선순위를 부여했습니다. 둘 다 Mistral로 수렴했습니다. 따라서 사용자는 구독 할당량을 요청했지만 사용량 과금이 발생했고, 아무 경고도 없었습니다. 이는 정확히 `--use_codex`가 방지하기 위해 존재하는 실패 방식입니다. 이제 6개의 provider 플래그는 모두 `add_mutually_exclusive_group`를 거칩니다. **동작 변경**: 지금까지 조용히 허용되던 두 provider를 조합한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **작업 종료 gate는 probe가 실패해도 성공으로 통과했습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개가 반환 코드를 확인하지 않고 “stdout을 캡처하고 비어 있으면 결론 내리는” 패턴을 따랐습니다. 예외(파일 이름 변경, `FileNotFoundError`)가 stderr에 기록되고 stdout은 비어 있으면, 검사는 “보고할 내용 없음”이라고 결론 내렸습니다. 이를 방지하기 위해 작성한 스크립트 안에서 “`exit 0` 하나만으로는 아무것도 증명할 수 없다”는 함정이 재현되었습니다. 이제 `probe()` helper가 0인 반환 코드 **및** 종료 sentinel을 요구하며, probe는 비어 있는 기준 집합을 근거로 결론 내리지 않습니다. 빈 집합에 대한 assertion은 항상 참이기 때문입니다. 위의 배타적 그룹을 추가하면서 provider 플래그가 `*_group` 객체를 통과하게 되었고, 기존 정규식 `parser\.add_argument\(`는 더 이상 일치하지 않았습니다. 그 결과 **21개 중 6개 플래그**가 조용히 범위에서 빠졌지만 gate는 성공 상태였습니다.
    - **secret scan이 6개 provider 중 4개를 놓쳤습니다.** `[A-Za-z0-9]` 클래스는 하이픈을 제외합니다. `sk-proj-…`(현재 OpenAI 형식)와 `sk-ant-api03-…`는 두 번째 하이픈에서 실패했고, `AIza…`는 지원되지 않았습니다. 패턴을 확장하고 `.secrets.baseline`를 scan에서 제외했습니다. 또한 `.env` guard는 `git diff --cached`를 조회했는데, 이는 index만 보기 때문에 **이미 커밋된** 최악의 경우인 `.env`가 나타나지 않았습니다. 이제 `git ls-files`를 조회합니다.
    - **Codex의 “token 워밍업”은 실제 워밍업이 아니었습니다.** 측정 결과 `codex login status`는 `~/.codex/auth.json`를 건드리지 않았고(mtime과 크기 모두 변경 없음), 도움말에는 “로그인 상태 표시”라고 나왔습니다. 그런데 주석은 token을 “한 번, 순차적으로” 새로 고쳐 일회성 rotating token에서 동시 refresh 위험을 무력화한다고 설명하고 있었습니다. 명시된 보호 기능은 존재하지 않았습니다. 이제 주석은 코드의 실제 동작을 설명하며, 진정한 대응책은 여전히 `max_jobs=4`입니다. 또한 검사는 무시하던 `CODEX_BIN`를 준수합니다. `codex`가 `PATH`에 없는 환경에서는 “인증되지 않음”으로 실패했는데, 이는 오해를 부르는 진단이었습니다.
    - **`.env`가 하위 셸에서 source 처리되었습니다.** `detect_provider`가 명령 치환으로 호출되어 export가 상위 환경으로 전달되지 않았습니다. 따라서 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`가 `.env`에서 정의되어도 `main()`에서 수행되는 조회에는 보이지 않았고, 올바른 구성에서도 “Grok 바이너리를 찾을 수 없음”으로 결론 내렸습니다.
    - **동시 실행 수가 명시된 한도를 50% 초과했습니다.** guard가 README/CHANGELOG 쌍을 시작한 뒤에 배치되어, 측정된 최고치는 **`max_jobs=2` 3개**였습니다. 주간 quota를 Chat/Imagine/Voice와 공유하고 측정할 수 없는 Grok에서는 스크립트가 설정한 한도가 지켜지지 않았습니다. 최종 개수는 표시되었지만 28과 비교되지 않았으므로, 파일 하나가 없어도 알아차릴 수 없었습니다.
    - **Grok 출력 계약: `stopReason`가 없으면 이제 실패합니다.** 코드에는 명시된 계약이 `end_turn`를 요구하는 곳에 “`end_turn` **또는 없음**”이 적용되어 있었습니다. 필드가 없는 payload나 CLI 업데이트로 필드 이름이 변경된 payload는 guard를 조용한 no-op으로 만들었습니다. 또한 `max_turn_requests`는 더 이상 rate limit으로 분류되지 않습니다. 소진된 것은 turn budget이므로 재시도해도 90초를 기다린 뒤 같은 결과가 나옵니다. `quota`도 rate limit marker에서 제외됩니다. 이는 `_codex_is_rate_limited`의 docstring이 이미 설명하고 있었지만 Grok에는 적용되지 않았던 이유입니다.
    - **Gemini cascade가 모델별로 메모이제이션됩니다.** 각 segment마다 `minimal`에서 다시 시작했지만 기본 모델은 이를 거부했습니다. 그 결과 정상 경로에서도 segment마다 400 왕복이 발생했고 같은 경고가 반복 출력되었습니다. 수백 번 반복되는 warning은 더 이상 읽히지 않으며, 그렇게 경고가 가면이 됩니다.
    - **기타**: CI 거부 메시지가 Codex용으로 하드코딩되어 `--use_grok_cli` 사용자를 `XAI_API_KEY` 대신 `OPENAI_API_KEY`로 안내했습니다. `provider.capitalize()`는 “Grok_cli”와 “Openai”를 표시했습니다. 하위 프로세스 기반의 주석은 두 CLI 모두를 “shim”으로 일반화했지만 Grok 바이너리는 네이티브 ELF입니다. 올바른 근거는 “자체 하위 프로세스를 생성하는 agent”입니다. `subprocess`의 SAST finding 12개는 사유와 함께 `# nosec` / `# nosemgrep`로 표시되었습니다. `shell=True`가 없는 목록 형식은 injection을 불가능하게 하며 문서 내용은 argv를 통해 전달되지 않습니다.
    - **이제 어떤 secret도 agent 하위 프로세스로 들어가지 않습니다.** 이름을 열거한 deny-list는 **과금** 불변식만 보호했습니다(Codex에는 `OPENAI_API_KEY`가 없고 Grok에는 `XAI_API_KEY`가 없음). 측정 결과 Anthropic, Mistral, Google, Gemini 키와 다른 CLI의 키, 그리고 secret은 아니지만 트래픽을 전환하는 `OPENAI_BASE_URL`까지 **추가로 7개의 secret**이 각 하위 프로세스에 들어가고 있었습니다. 두 CLI는 **agent**이며, Grok agent는 많은 Linux 환경에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 필터링은 이름 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)을 사용하므로, 이 코드가 알지 못하는 사용자의 `.env`에 추가된 변수도 포함합니다. CLI에는 어느 것도 필요하지 않습니다. 인증은 `~/.codex`와 `~/.grok`에 저장되며 환경에는 절대 두지 않습니다. 강화된 환경에서 두 provider 각각을 통해 **실제 번역을 성공적으로 완료**하여 확인했습니다.
    - **테스트**: provider 플래그의 배타성, `stopReason` 계약, news 정규식의 선형성, CI 거부 메시지, Gemini 메모이제이션, 하위 프로세스 환경에 secret이 없는지를 고정하는 새 파일 `tests/test_review_hardening.py`(테스트 21개)을 추가했습니다. 마지막 assertion은 **일반적**이므로 어떤 목록에도 이름이 없는 키가 있으면 실패합니다. 반면 기존 정제 테스트는 자체 상수의 복사본이어서 자체 반복문의 고장 외에는 아무것도 감지할 수 없었습니다. 전체 테스트 수는 **311개**입니다.

  - **새로운 Grok provider 2개**: `--use_grok`(xAI API, `XAI_API_KEY` 키, 사용량 과금)와 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독에서 차감 — `--use_codex`와 같은 원리).
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`를 그대로 재사용하고, `base_url`만 변경합니다. 한 가지 조정만 필요했으며 모두에게 이점이 있습니다. `finish_reason`가 이제 `end_turn`도 허용합니다. 이는 xAI가 생성하는 형식이고 OpenAI는 `stop`를 생성합니다. 모델은 `grok-4.6`(품질)와 `grok-4.3`(경제형)입니다. 참고로 Grok의 경제형은 저장소에서 가장 비쌉니다. 백만 토큰당 $1.25/$2.50이며 `mistral-small-latest`는 $0.15/$0.60입니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택합니다.
    - **CLI 모드**: Codex를 본떴지만 실제 환경에서 요구된 네 가지 차이가 있습니다. prompt는 파일로 전달되고(`--prompt-file`, CLI가 stdin을 읽지 않으며 argv의 segment는 `ps`에 노출됨), 출력은 stdout의 단일 JSON 객체입니다(JSONL도 아니고 `-o` 파일도 아님). 구독은 `grok-4.6`와 `grok-4.5`만 노출하며 sandbox는 적용할 수 없습니다(아래 참조). 하위 프로세스 실행은 `_codex_run_process`에서 Codex와 공통화했으며, 이미 테스트된 Codex provider의 나머지는 건드리지 않았습니다.
    - **측정 결과 `exit 0`는 아무것도 증명하지 않습니다**: 인증되지 않은 상태에서 CLI는 **stdout**에 `{"type":"error","message":"Not signed in."}`를 반환 코드 **0**과 함께 씁니다. 거부나 turn 초과도 동일하게 동작합니다. 따라서 출력 계약에는 네 가지 조건이 동시에 필요합니다. 반환 코드 0, error payload 없음, `stopReason == end_turn`, 그리고 비어 있지 않은 텍스트입니다. preflight도 같은 논리를 따릅니다. 연결이 끊겨도 `grok models`는 0으로 종료하므로 stdout에 “not authenticated”가 있어야만 결론을 내릴 수 있습니다.
    - **격리: 비대칭을 인정하고 문서화했습니다.** Codex가 `--sandbox read-only`에서 실행되는 반면, 최근 Linux 환경의 많은 시스템에서는 두 가지 독립적이고 우회할 수 없는 시스템 원인 때문에 Grok sandbox를 적용할 수 없습니다. `sudo` 없이는 해결할 수 없습니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), container runtime socket deny-list는 `/run/podman`가 `0700`에 있을 때 실패합니다(resolver는 `ErrorKind::NotFound`만 복구하고 EACCES는 치명적이 됨). 핵심 함정은 적용할 수 없는 **통합** profile이 **조용히 비격리 상태로 시작한다**는 점입니다. 따라서 스크립트는 기본적으로 profile을 요청하지 않으며 절대 조용히 fallback하지 않습니다. stderr로 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하며 catch-all인 `*`도 포함합니다. 이는 측정된 유일한 _fail-closed_ 계층입니다(알 수 없는 접두사의 규칙은 시작을 거부함). `GROK_TRANSLATE_SANDBOX=read-only`를 사용하면 이를 강제할 수 있으며, 시스템이 준수할 수 없으면 시작이 실패합니다.
    - **안전장치**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`는 하위 프로세스 환경에서 제거됩니다(키 하나가 사용량 과금으로 전환시키며, 상속된 `GROK_SANDBOX`는 적용할 수 없는 profile을 강제해 오해를 부르는 메시지를 발생시킴). MCP/hooks/skills/agents 스위치는 비활성화되고, `--disable-web-search`, `--no-subagents`, `--no-plan`, 임시 workdir, CI 거부, process group을 종료하는 timeout, rate limit에 대한 back-off가 적용됩니다. `--max-turns`는 1이 아니라 6으로 설정됩니다. 도구 turn 이후에 counter가 증가하므로 1이면 출력이 잘립니다.
    - **Quota**: Grok pool은 주간 단위이며 **Chat, Imagine, Voice와 공유**되고 이를 노출하는 명령은 없습니다. `account/rateLimits/read`로 사용량을 계산할 수 있는 Codex와 다릅니다. 따라서 `regen_translations.sh`는 동시 실행을 2개로 제한하고 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`(테스트 24개)을 추가했습니다. 전체 테스트 수는 **290개**입니다.
  - **수정된 버그 — EN 다중 문단 인용문은 `--news` 모드에서 일부만 보호되었습니다**: `_NEWS_CITATION_REGEX`는 인용문 본문으로 `>` 줄이 **연속해서** 이어지는 경우만 허용했습니다. 인용문이 여러 문단에 걸쳐 있고 그 사이에 `>` 빈 줄이 있으면 마지막 문단만 캡처되어 placeholder로 대체되었습니다. 앞선 문단은 LLM으로 넘어가 번역되어 돌아왔습니다. 이는 `--news`가 보장하기 위해 존재하는 것과 정반대입니다. 이제 반복문은 내부의 `>` 빈 줄을 허용하고 non-greedy가 되어, 처음 만나는 빈 줄이 아니라 이탤릭체 줄 앞의 `>` 빈 줄에서 멈춥니다.
    - **측정된 범위**: 실제 198개 문서 코퍼스에서 419개 중 11개 인용문이 영향을 받았습니다. 회귀는 없었습니다. 새 정규식은 정확히 동일한 수의 인용문을 캡처하며, 다중 문단 본문만 확장됩니다(동일한 본문 408개, 확장된 본문 11개). attribution 줄 `> — …`는 lookahead가 유지되어 여전히 본문에 흡수되지 않습니다.
    - **end-to-end 증명**: ja/ar로 번역한 69KB 문서에서 이전에는 인용문의 첫 문단이 일본어에서는 `> GLM-5.3がオープンウェイト化。`로 렌더링되고 아랍어에서도 같은 방식으로 번역되었습니다. 이제는 `> GLM-5.3 is now open-weight.`로 유지됩니다. 영어 인용문 줄 수는 9개에서 10개로 돌아가 원문과 같아졌습니다.
    - 참고: 이 결함은 이후 validator에서 감지되지 않았습니다. validator는 인용문이 존재하는지만 확인하고 완전한지 여부는 확인하지 않습니다.
  - **기본 provider에서 측정된 비용 절감**: `_openai_extra_kwargs`는 모델명이 `gpt-5`로 시작하기만 하면 `reasoning_effort="medium"`를 전송했으며, `--eco`인 경우에도 마찬가지였습니다. 10단어 문장 하나를 번역하기 위해 `gpt-5.4-mini`에서 측정한 결과, `medium`는 reasoning token 45개와 출력 토큰 65개를 사용했고, `none`는 각각 0개와 14개를 사용했습니다. reasoning은 번역에 아무런 이점이 없으며 모든 파일의 모든 segment마다 비용이 발생했습니다. 이제 기본값은 `--eco`에서 `none`가 되고, 그 외에는 `medium`으로 유지됩니다. CLI에서 명시적으로 전달한 값은 여전히 우선합니다. `--reasoning_effort`는 이제 `none`와 `xhigh`도 `low`/`medium`/`high`와 함께 허용합니다. 모든 모델이 모두 허용하는 것은 아닙니다. 예를 들어 `minimal`는 `gpt-5.4-mini`가 거부하지만, 기존의 매개변수 없는 retry가 이 경우를 처리합니다.
  - **SDK 업데이트 및 Gemini 마이그레이션**: 지원이 2025-11-30에 종료되고 저장소가 보관된 `google-generativeai`를 통합 SDK **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 다음 `client.models.generate_content(model=, contents=, config=)`을 사용하며, system prompt는 segment에 이어 붙이지 않고 `system_instruction`로 전달합니다. `mistralai`는 **2.9.4**로 업데이트되었습니다(import는 `from mistralai.client import Mistral`가 되며, 이전 방식은 `ImportError`를 발생시킴; wheel에서 확인). `anthropic`는 **0.125.0**, `openai`는 **2.54.0**으로 업데이트했습니다. 두 HTTP stack이 venv에 공존하지 않도록 `httpx2`로 전환하기 전 마지막 버전입니다. 그 결과 `httpx` 0.28.1과 `pydantic` 2.13.5도 사용할 수 있게 되었습니다.
  - **문서가 아니라 실제 테스트에서 두 회귀를 발견했습니다**:
    - `anthropic` ≥ 1.0은 `max_tokens`가 10분 이상을 예상하게 하는 비스트리밍 호출을 client 측에서 거부합니다(`ValueError: Streaming is required...`). 이 안전장치는 0.34.2에는 없었고 `max_tokens=32768`를 사용하는 모든 Claude 호출을 깨뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 완전한 응답만 사용하는 호출이 streaming으로 전환되지 않도록 했습니다.
    - `thinking_level="minimal"`는 Gemini catalog의 일부에서만 허용됩니다. `gemini-3.1-flash-lite`는 이를 지원하지만 `gemini-3.7-flash`와 `gemini-3.1-pro-preview`는 400으로 거부합니다. 따라서 `_gemini_generate_with_fallback`가 필요합니다. 이는 `minimal` → `low` → thinking_config 없음의 cascade이며, 기존 OpenAI fallback과 같은 방식입니다. 최적화 매개변수 하나 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델을 갱신하고 각각 실제 호출로 검증했습니다**: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%), `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%); Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신), `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜 없는 canonical ID); Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**, `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(안정 버전이며 `3.5-flash-lite`보다 저렴).
Mistral은 변경되지 않았으며, 네 모델 중에서는 `mistral-large-latest`이 여전히 가성비가 가장 좋습니다. 참고로 `gemini-3.1-pro-preview`보다 최신인 Pro 제품군의 Gemini 모델은 존재하지 않습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 실제로 출시되지 않았으며, 3.5/3.6/3.7 라인은 전적으로 Flash입니다.
  - **Gemini로 전환하기 전 측정한 A/B 테스트**: `README.md`을 `gemini-3.1-pro-preview`로 일본어 번역한 뒤 `gemini-3.7-flash`으로 번역했습니다. 구조는 완전히 동일했습니다(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존). 처리 시간은 **48초 대비 8초**였습니다. 이 두 모델을 번역이나 비라틴 스크립트에 대해 비교한 공개 벤치마크는 없으므로, 그렇지 않았다면 전환은 단순한 추정에 의존했을 것입니다.
  - **Claude 응답 블록 필터링**: `_call_claude`는 블록 유형을 필터링하지 않고 `block.text for block in response.content`을 수행했습니다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 삽입하는데, 이 블록은 `.text`이 아니라 `.thinking`를 노출합니다. 따라서 첫 번째 세그먼트에서 번역이 불투명한 `AttributeError`에 걸려 중단되었을 것입니다. 이제 `thinking`, `redacted_thinking`, `tool_use` 및 `tool_result` 블록은 제외됩니다(알 수 없지만 텍스트를 담은 유형에는 계속 관대하도록 음수 목록 사용). 텍스트 블록이 전혀 없는 응답은 명시적인 오류를 발생시킵니다. `thinking={"type": "disabled"}`는 모든 호출에 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 폐기일이 지난 모델을 제거했습니다(2026-07-31에 폐기된 `magistral-*` 제품군, 2026-06-01의 `gemini-2.0-*`, 2026-03-09의 `gemini-3-pro-preview`, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`). 한도도 수정했습니다. Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1 000 000 → **1 048 576**(실제 입력 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1,05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest` 및 `ministral-*` 제품군을 추가했습니다. 참고로 이러한 한도는 여전히 참고용이며, `translate()`가 세그먼트 크기를 `min(16000, limite)`로 제한합니다.

  - **Provider `--use_codex`**: 공식 Codex CLI(`codex exec`)를 비대화형 모드로 구동하는 다섯 번째 provider이며, 사용량에 따라 과금되는 API를 호출하지 않습니다. 번역 비용은 이미 결제한 ChatGPT 구독 할당량에서 차감됩니다. 이 용도에 대해 OpenAI가 문서화한 유일한 방법입니다. 요금제별 제공 여부 표에는 Plus/Pro/Business/Enterprise에서 « Codex SDK, `codex exec`, and scriptable workflows »를 사용할 수 있다고 명시되어 있지만, `~/.codex/auth.json`의 토큰은 Platform API 호출을 인증하지 않습니다(또한 이 스크립트는 해당 토큰을 절대 읽지 않으며, 인증과 갱신은 CLI가 계속 관리합니다).
  - **Codex 바이너리를 이제 npm뿐 아니라 pip로도 설치 가능**: `_resolve_codex_binary()`는 먼저 `CODEX_BIN`에서 바이너리를 찾고, 그다음 `PATH`, 마지막으로 OpenAI가 게시한 공식 Python 패키지 **`openai-codex-cli-bin`**(SDK `openai-codex`의 종속성)를 찾습니다. 따라서 Python 프로젝트에서 `--use_codex`을 사용하기 위해 더 이상 전역 npm 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가하지 않습니다. 바이너리 용량이 약 250MB이므로 선택적 provider를 위해 모든 사용자에게 설치를 강제하게 되기 때문입니다. 처음부터 끝까지 검증했습니다. `codex`가 `PATH`에 없을 때 패키지된 바이너리를 찾아 전체 번역이 6초 만에 완료되었습니다.
  - **« 구독 모드 » 보장**: `OPENAI_API_KEY` 및 `CODEX_API_KEY`를 하위 프로세스 환경에서 제거합니다. 이 보호 장치가 없으면 `.env`에 있는 키로 인해 아무런 가시적 신호 없이 Codex가 사용량 기반 과금으로 전환될 수 있으며, 이는 바로 이 provider가 방지하려는 상황입니다.
  - **CLI의 함정을 테스트로 잠금**:
    - `codex exec`는 프롬프트가 인수로 전달된 경우에도 stdin을 **읽습니다**. stdin을 닫지 않으면 모델을 호출하지 않은 채 명령이 시간 초과까지 대기합니다(재현 결과: 180초 후 종료 코드 124, 0바이트). 따라서 `communicate(input=...)`가 필수입니다.
    - npm으로 설치된 `codex`는 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 실제 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 살아남아 할당량을 계속 소비할 수 있습니다. 그래서 `Popen(start_new_session=True)` + `os.killpg`을 사용합니다.
    - CLI는 `turn.failed`를 출력했더라도 종료 코드 0으로 끝날 수 있습니다. JSONL 출력(`--json`)을 반환 코드와 함께 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **속도 제한 시 백오프**: CLI는 내부 재시도(`max_retries = 0`)를 구현하지 않습니다. 분류는 하위 문자열이 아니라 JSON 페이로드 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. « quota »라는 단어는 복구 가능한 429 오류와 복구 불가능한 `insufficient_quota` 모두에 나타날 수 있기 때문입니다.
  - **CI 보호**: `CI` 또는 `GITHUB_ACTIONS`가 정의되어 있으면 `--use_codex`를 거부합니다. 구독 인증은 공유 runner를 대상으로 설계되지 않았으며, OpenAI는 공개 저장소에서 이 워크플로를 사용하지 말 것을 명시적으로 권고합니다.
  - **모델**: `gpt-5.6-sol`(품질) 및 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 제품군은 CLI와 Platform API에서 공통으로 사용되지만, ChatGPT 계정이 모든 모델에 접근할 수 있는 것은 아닙니다. 허용 목록은 로컬 검증 없이 서버 측에서 적용되며, 비정상적인 모델을 지정하면 경고가 발생합니다. Plus 요금제에서 Luna는 5시간 창당 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개만 제공합니다. 따라서 `--eco`가 모든 일괄 처리에 권장되는 모드입니다.
  - **수정된 버그 — 완전히 성공했는데도 `regen_translations.sh`가 오류로 종료됨**: `trap ... EXIT`가 더 이상 존재하지 않는 `failed_log`를 참조하고 있었습니다. 이는 `main()`의 `local` 변수로, trap이 실행될 때는 존재하지 않습니다. `set -u`에서는 이로 인해 `failed_log: unbound variable`가 발생하고 스크립트가 1로 종료되었습니다. 28개의 번역이 올바른 상태였지만, 재생성 직후 가장 비용이 많이 드는 단계에서 `release.sh --auto`(`set -e`)가 중단되었을 것입니다. 변수를 전역으로 옮기고 trap에서 변수의 존재 여부를 검사합니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 이제 종료 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: provider의 기본값보다 우선하여 특정 모델을 강제하는 `regen_translations.sh`의 새로운 환경 변수입니다. 예를 들어 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`를 사용하면 처리량 중심 모델인 `--eco` 대신 구독 할당량의 상위 모델로 재생성할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때 사용할 수 있는 `REGEN_PROVIDER=codex`입니다(사용자 모르게 구독 할당량을 소비하지 않도록 자동 감지하지 않음). Codex 갱신은 회전식이며 일회용이므로 동시 작업이 `codex login` 세션을 무효화할 수 있습니다. 따라서 병렬 처리를 시작하기 전에 토큰을 순차적으로 한 번 갱신하고 동시성은 4로 낮춥니다.
  - **관련 리팩터링**: `_dispatch_provider_call`는 provider 이름을 반환하는 `_resolve_provider()`를 통해 매개변수를 8개에서 6개로 줄였습니다. 전체 호출 체인에 네 번째 불리언을 전달하는 대신 provider 이름을 사용합니다. `args`보다 명시적인 불리언을 계속 우선하므로, 최소한의 `Namespace`으로 `translate(..., use_mistral=True)`을 호출하는 테스트를 보존합니다.
  - **테스트**: argv, 정리된 환경, 서문 방지 계약, 무음 실패, timeout/killpg, 백오프, 사전 점검, provider 확인, Gemini 추론 cascade, Claude 블록 필터링 및 다중 문단 news 인용을 다루는 새 파일 `tests/test_codex_provider.py`(테스트 48개)을 추가했습니다. 전체 테스트는 290개로 늘었습니다.
  - **실제 검증**: 프로젝트의 `README.md`를 Codex로 **14개 언어**로 번역한 결과, 기준 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 행 25개, HTML 링크 13개, 이미지 13개, URL 19개, 문자 단위로 동일한 코드 블록, placeholder 잔여물 0개). `--news` 모드에서 69KB 뉴스 기사의 경우 `gpt-5.6-luna` 및 `gpt-5.6-sol` 출력이 모두 en/ja/ar에 대한 후속 애플리케이션 검증을 통과했습니다. `account/rateLimits/read`로 측정한 사용량은 `--eco` 모드에서 카운터 반올림 임계값(5시간 창의 0%) 이하로 유지되었습니다.

- **1.9.2** 중첩 괄호 또는 FR 접두사가 있는 news attribution URL 추출 수정 (2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`의 attribution URL 추출은 `re.search(r"\((.+?)\)", attribution)` 정규식을 사용했습니다(괄호 사이를 느슨하게 캡처). `(relayé par [@user sur X](https://x.com/.../123))`과 같은 attribution(중첩 괄호: 바깥쪽 `(` + markdown link의 `]()`)에서는 캡처가 처음 만나는 `)`에서 멈췄습니다 → 문자열이 잘리고 FR 접두사도 포함되었습니다: `relayé par [@user sur X](https://x.com/.../123`(마지막 `)` 없음). 그 결과 `_validate_news_post`가 번역된 출력에서 이 문자열을 찾다가 항상 실패했습니다(두 가지 원인: `)`가 잘렸고 « relayé par »가 `relayed by`/`weitergeleitet von`/…로 번역됨). low → medium → high → gpt-5.5 전체 cascade를 통과할 수 없었습니다.
  - **수정**: 정규식을 `re.search(r"\]\(([^)]+)\)", attribution)`로 변경했습니다. 이는 markdown link의 `](url)`를 정확히 대상으로 하며 **순수 URL만** 캡처합니다(FR 접두사와 잘림 없음). 번역 중에는 `#URL{N}#` placeholder를 통해 불변성이 유지됩니다. 문제가 되는 두 패턴에 모두 강건합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥 괄호가 없는 FR 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 2개를 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그를 정확히 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via` 변형)
  - **누락된 커버리지**: `check-editorial-coverage.py`는 편집 문법은 검증하지만 translator가 번역할 수 있는지는 검증하지 않습니다. 가능한 개선 사항(v1.9.2 범위 외)은 게시 전에 위험한 패턴을 감지하도록 dry-run에서 attribution 추출을 시뮬레이션하는 검사입니다.

- **1.9.1** 번역 marker 노트의 CTA 라벨 i18n 수정 (2026-05-10):

  - **수정된 버그**: 번역된 파일 상단 marker 배너의 CTA 링크 라벨 `[Voir le projet sur GitHub ↗]`가 모든 대상 언어에서 `target_lang`를 따르지 않고 **프랑스어로 남아 있었습니다**. 저장소의 URL과 slug를 보존하기 위해 Python 측에서 조립되므로 LLM은 이를 전혀 보지 못했고, 번역 단계에서도 수정할 수 없었습니다. v1.9에서 `marker` 형식을 추가한 이후 발생한 무음 회귀였습니다.
  - **수정**: 15개 언어를 현지화된 라벨에 매핑하는 새 상수 `_VIEW_PROJECT_LABELS`를 추가했습니다. 이제 `_translation_note_invariants(target_lang)` 및 `_assemble_translation_note_paragraphs(phrase, target_lang)`가 대상 언어를 전달합니다. 언어를 알 수 없는 경우에는 KeyError를 방지하기 위해 `fr`로 대체합니다.
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`를 수정했습니다(target_lang `ja` → 일본어 라벨 예상). 새 테스트 2개: `test_source_link_label_localized_per_target_lang`(라틴 문자, 표의 문자, 아브자드를 포괄하는 7개 언어 매개변수화) 및 `test_source_link_label_falls_back_to_french_for_unknown_target`. 총 `test_translation_note_position.py` 테스트는 38개에서 40개로 늘었습니다.
  - **Backward-compat**: 기본값이 있는 `target_lang="fr"` 시그니처를 사용하므로, `args.target_lang` 없이 호출하는 외부 프로그래밍 호출자도 수정 없이 계속 작동합니다.
- **1.9** 무음 실패 수정 + 종합 품질 도구 + 다중 위치 번역 노트 (2026-05-07):
  - **다중 위치 번역 노트 + "embed card" 형식 마커**:
    - 새로운 CLI 옵션(추가 옵션, 기본값 변경 없음 → **비호환 변경 없음**):
      - `--note_position {top,bottom,both}` (기본값: `bottom`): 번역된 파일의 상단, 하단 또는 양쪽 위치에 노트를 배치합니다.
      - `--note_format {legacy,marker}` (기본값: `legacy`):
        - `legacy`은 v1.8 동작(굵은 문단 `**…**`)을 **byte-for-byte**로 엄격하게 재현합니다.
        - `marker`는 보이지 않는 Markdown 링크 참조 정의(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에, "GitHub repo embed card"와 같은 렌더링을 위한 구조화된 **3문단 blockquote**를 출력합니다. 구성은 인라인 코드로 표시된 프로젝트 제목(`**\`ai-powered-markdown-translator\`\*\*`), LLM이 번역한 설명, 화살표가 표시된 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)입니다. remark 플러그인이 빌드 단계에서 활용할 수 있습니다(jls42.org 블로그 → `remark-translation-banner` 플러그인 참조).
    - **LLM에 절대 전송하지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문장 번역 후 Python 측에서 조립합니다. LLM은 slug `ai-powered-markdown-translator`나 `https://github.com/jls42/...`을 절대 보지 않으므로 renderer, 이스케이프, scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 YAML frontmatter의 **닫는 `---` 블록 뒤에** 노트를 삽입합니다(Astro Content Collections / gray-matter 안전성). Helper `_split_frontmatter`은 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter가 있으면 **`RuntimeError`을 발생**시키며, 해당 파일은 잘못된 위치에 노트를 삽입해 기록되는 대신 `failed_files`으로 이동합니다.
    - **모델 sanitizer 화이트리스트**: `_sanitize_model`는 `[A-Za-z0-9._:/-]` 범위를 벗어난 모든 문자를 `_`으로 바꾸며, 비어 있으면 `unknown`을 대체값으로 사용합니다. remark Astro 플러그인 측 validator와 동일한 규칙을 적용하여 공백, 따옴표, 괄호, 쉼표 등 marker 형식을 손상시킬 수 있는 문자를 무력화합니다.
    - **내부 리팩터링**: `_append_translation_note`(단일 모놀리식 함수)을 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`)로 분리했습니다. Builder와 composer를 분리했으며(builder는 구분자 없는 순수 블록을 반환하고 composer는 위치에 따라 `\n\n`을 적용), 생성 로직과 소스 helper는 동일한 3문단 조립기를 공유합니다.
    - **`_quote_lines` 공백 보존**: 각 줄 앞에 `> `을 붙이고, 빈 줄은 `>`만 있는 줄로 변환합니다. 이를 통해 mdast가 blockquote 안에서 줄바꿈이 있는 하나의 문단이 아니라 제목 / 설명 / 링크라는 3개의 서로 다른 문단을 인식할 수 있습니다.
    - **`_build_translation_note_block` 적응형 처리**: LLM이 보존한 문단 수에 따라 동작합니다(3개 = 완전한 카드 형식, 2개 = 문장 + 링크, 1개 = 대체 형식). Markdown 링크 `](`가 감지되면 1문단 대체 형식은 더 이상 `**...**`으로 감싸지 않습니다(`<strong>` 주변의 링크 렌더링이 취약하기 때문).
    - **하위 호환성**: `_compose_with_notes` 측의 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")` — 이러한 속성이 없는 Namespace(기존 테스트, 외부의 프로그래밍 방식 호출)도 수정 없이 계속 작동합니다.
  - **긴 번역에서의 무음 실패 수정**:
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 추가: 결정론적 계층(소스 발췌문이 verbatim으로 다시 나타나는지 확인) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` 화이트리스트: 화이트리스트에 없는 모든 상태(truncation, content_filter 등)에서 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768`(16k 세그먼트의 잠재적 truncation 방지, FR→JA/ZH/KO/AR/HI 교차 스크립트에 대한 여유 확보)
    - heading-aware 세분화: 세그먼트의 후반부에서는 H2/H3를 우선하여 각 세그먼트가 완전한 의미 단위의 섹션으로 시작하도록 처리
    - 오류를 0이 아닌 exit code까지 전파: `translate_markdown_file`은 `success` / `failure` / `skipped`의 타입이 지정된 상태를 반환하고, 하나 이상의 파일이 실패하면 `main()`은 `sys.exit(1)`합니다(single-file 및 batch 모두).
    - 모든 provider에 empty-content guard, 소스/출력 비율 검사(≥ 500자, < 5%이면 거부), 코드 placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 후 정규화(heading에 붙은 구분자/링크 수정), `BadRequestError`에서 `reasoning_effort` 없이 재시도
    - `langdetect==1.0.9` 의존성 추가
  - **pre-commit 품질 도구**("완전한 EurekAI 유형", 14개 hook):
    - Pre-commit: ruff(린트 + 포맷), shellcheck, prettier(md/yaml/json), detect-secrets(보호되는 API key 4개), Lizard(CCN ≤ 12), pre-commit-hooks v5(공백, EOF, 대용량 파일, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `scripts/`의 로컬 wrapper가 `./venv/bin/python`을 사용합니다.
    - `scripts/audit_verdict.py`: 11개의 unittest로 pip-audit JSON parser를 테스트하며, jls42-astro parser를 Python으로 이식했습니다.
    - 초기 ruff 위반 7건 수정: B904(raise from) ×2, B007(미사용 dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard는 일시적으로 `translate.py`을 제외합니다(CCN 21-47인 함수 4개, 리팩터링 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 전체 커버리지**:
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): 모든 push와 pull-request에서 분석, `coverage.xml`를 통한 coverage
    - README 상단에 SonarCloud 배지 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py`(`unittest` stdlib): 무음 실패 오류 체인의 6개 연결 고리를 모두 다룹니다.
    - `tests/test_orchestration.py`(+ 테스트 79개): `translate.py`의 orchestration 계층을 다룹니다(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return 분기)
    - `scripts/tests/test_audit_verdict.py`: `main()`(stdin/stdout)과 subprocess를 통한 `if __name__ == "__main__"` 블록을 다룹니다.
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 매트릭스(E2E `marker+top|bottom|both` 및 `legacy+top|bottom|both` 포함), 다중 줄 접두사 처리, byte-for-byte 하위 호환성(golden literal), sanitizer, frontmatter 분할(닫히지 않은 fence에서의 raise 포함), 3문단 형식, 2문단 대체 형식, 1문단 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않는지 단언하는 중요한 안전장치 `TestLLMPayloadExcludesInvariants`을 다룹니다. **테스트 190개 통과**, 회귀 0건.
  - 문서화: 배지가 포함된 `README.md`(프랑스어 + 14개 번역), `CLAUDE.md`(pre-commit workflow + 상세한 CI 감시), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026년 모델 업데이트 (2026-03-17, tag `v1.8`):
  - 기본 모델 업데이트(2026년 3월):
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token 제한 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder를 사용한 EN 인용 보호, `LANG_FLAGS` 매핑(15개 언어), 대상 언어별 플래그 처리
  - 복원 전 news placeholder 검증(회귀: placeholder를 삭제한 LLM이 인용 없는 출력을 조용히 생성)
  - `regen_translations.sh` 스크립트를 이식 가능하게 변경(절대 경로, pwd 의존성 없음)
  - README/CHANGELOG language bar에 Français 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능:
  - 번역 시 원본 파일명을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **인라인 코드 보존**: 이제 backtick(`` `...` ``)을 번역 중 보호
  - 시스템 prompt 개선:
    - YAML frontmatter의 따옴표 처리 개선
    - template 변수 `{variable}` 보호
    - 요청하지 않은 번역자 노트 금지
  - 364개 파일에서 성공적으로 테스트(jls42.org 블로그 마이그레이션)
- **1.6** 새로운 기능:
  - 번역을 위한 Google Gemini API 지원 추가(`--use_gemini`)
  - 2026년 기본 모델 업데이트:
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 순회하지 않는 단일 파일 번역(`--file`)
  - 단순화된 새로운 명명 패턴: `{base}-{lang}.md`
  - 모델명을 포함한 기존 형식을 유지하는 `--include_model` 옵션
  - 기본 token 제한(128k)을 적용한 목록에 없는 모델 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항:
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`으로 업데이트
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`으로 업데이트
  - **번역 prompt 최적화:**
    - 직접 번역과 번역 노트용 prompt를 더 명확하고 효율적으로 개선했으며, 메타데이터와 특정 서식 요소의 보존에 관한 자세한 지침을 포함했습니다.
  - **코드 리팩터링:**
    - Mistral AI client 초기화를 위해 `MistralClient`을 `Mistral` 클래스로 대체
    - 가독성과 유지보수성 향상을 위한 import 재구성
    - 번역 중 원본 서식을 보존하도록 텍스트 세분화 및 코드 블록 처리 개선
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 반전(예: `f"{base}-{args.target_lang}-{args.model}.md"`)하여 번역본을 더 쉽게 정리하고 검색할 수 있도록 개선
  - **기타 개선:**
    - 불필요한 빈 줄을 제거하여 코드 정리
    - 스크립트 구조와 가독성 향상을 위한 사소한 조정
- **1.4** 새로운 기능:
  - 번역을 위한 Anthropic Claude API 지원
  - 명확성과 효율성 향상을 위한 prompt 최적화
  - 코드 유지보수성 향상을 위한 사소한 조정
- **1.3** 개선 사항 및 새로운 기능:
  - 코드 블록 처리 개선
  - 출력 파일 관리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 모델과 언어의 순서 반전
- **1.2** changelog 수정
- **1.1** Mistral AI API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**gpt-5.6-luna로 프랑스어에서 한국어로 번역된 기사.**
