### 변경 이력

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.11.0** PyPI에 게시: 저장소를 복제하지 않고 `pip install ai-powered-markdown-translator` 다음 `aipmt` 명령 사용 (2026-09-03):

  - **단일 파일 스크립트가 설치 가능한 패키지가 됨.** `translate.py`가 루트에서 `src/aipmt/translate.py`로 이동하고, 콘솔 진입점 `aipmt` 및 이에 해당하는 `python -m aipmt`가 추가됨. 복제한 저장소는 기여를 위해서는 여전히 필요함 — 테스트, 28개 번역, 품질 도구가 그 안에 있음 — 하지만 사용을 위해서는 더 이상 필요하지 않음.

    - **가져오기 이름은 `aipmt`이며 절대로 `translate`이 아님.** 충돌이 실제로 발생하며 조용히 일어나기 때문임. PyPI 패키지 `translate` (v3.8.1, 마지막 업로드 2026-07-06)는 같은 이름의 디렉터리를 설치함. venv에서 재현하면 디렉터리가 모듈보다 우선하고 `translate.main`가 사라지며, 진입점은 `AttributeError`에서 실패함 — 그런데 `pip check`는 rc=0으로 « No broken requirements found »를 반환함. 사용자가 간단히 `pip install translate`만 실행해도 진단 가능한 정보 없이 CLI가 망가질 수 있었음. 실제 wheel로 반증 테스트: 패키지 위에 `pip install translate`를 실행하고, 전후 모두 `aipmt --help` rc=0, 두 CLI가 함께 존재함.
    - **배포 이름은 길게, 명령은 짧게.** `ai-powered-markdown-translator`는 PyPI 검색으로 패키지를 찾을 수 있게 함. 이미 프로젝트를 알고 있는 사람만 찾을 수 있는 약어만 사용하면 검색되지 않는데, 이번 게시의 목적은 바로 발견되는 것이기 때문임. 그럴듯한 후보 두 개는 검증을 통해 제외됨: `ai-markdown-translator`은 2024년부터 npm에서 이 저장소와 같은 목적의 도구가 사용 중이며 이 저장소보다 17개월 앞섬. 또한 `aimt`은 `aim`(v3.29.1)과 한 글자 차이인데, 같은 분야의 활성 패키지라서 장기적인 혼동에 최악의 구성임. 덧붙여 방법론상의 함정: `pypi.org/project/<nom>/`는 봇 방지 페이지 때문에 어떤 이름이든 200을 반환하므로 JSON API만 신뢰해야 함.
    - **평면 패키지보다 `src/` 레이아웃.** 평면 패키지는 테스트의 여섯 `sys.path.insert(..., "..")`를 그대로 유지했겠지만, 그것이 바로 결함임. 이 항목들은 패키지가 아니라 소스 트리를 가져오게 하므로 패키징 오류를 모두 가려 버림. 실제 비용은 치환 규칙 하나가 추가되는 것임.

  - **이제 키를 한 번만 설정하면 됨.** 설치된 CLI에는 영속적인 설정이 없었음. 환경 변수와 현재 디렉터리의 `.env`만 남아 있었음. `find_dotenv`는 시스템 루트까지 거슬러 올라가므로 **홈 디렉터리 아래에서 작업할 때는** `~/.env`를 찾았지만, 다른 곳에서 작업하면 아무것도 찾지 못했음 — 명령을 실행한 위치에 따라 적용 범위가 달라졌으며, 이는 설계상의 선택이 아니었음. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`가 추가됨.

    - **우선순위는 하드코딩되지 않음.** `load_dotenv`의 기본값인 `override=False`에서 파생됨. 각 계층은 이전 계층이 비워 둔 부분만 채움. 따라서 순서는 환경 변수 → 프로젝트의 `.env` → 사용자 설정임. 이는 구조가 아니라 동작 테스트로 검증됨 — 두 호출의 순서를 뒤집어도 실패하고, 세 번째 계층을 제거해도 실패함.
    - **TOML이 아닌 `.env` 형식**, 의도적인 선택임. `python-dotenv`는 이미 의존성이며, 문법은 15개 README에 이미 문서화되어 있고, 같은 파일을 두 범위에서 사용함. 새로운 의존성이나 문법은 없음. 위치는 `XDG_CONFIG_HOME`가 **절대 경로**일 때 이를 따름 — 사양상 상대 경로 값은 무시해야 하며, 그렇지 않으면 설정 위치가 다시 현재 디렉터리에 따라 달라짐 — Windows에서는 `APPDATA` 아래를 사용함.
    - **두 가지 선택지를 이유와 함께 제외함.** 시스템 키체인(`keyring`)은 데스크톱에서는 더 안전하지만 headless 환경 — 서버, 컨테이너, CI — 에서는 실패함. 이는 바로 일괄 번역의 사용 사례이므로 opt-in 후보로는 좋지만 기본값으로는 부적절함. `--api-key` 플래그는 키를 셸 기록에 남기고 `ps`에 노출함.
    - **키가 없을 때 호출 스택을 더 이상 표시하지 않음.** 사용자는 `site-packages`를 가리키는 Python 스택과, 두 번째 위치를 어디에 만들어야 하는지 말하지 않는 « 환경 또는 .env »라는 메시지를 받았음. 이제 세 위치와 정확한 경로를 나열하고 명령은 2로 종료함. 이 안전망은 **의도적으로 좁음**: 설정 단계에만 `except ValueError`를 적용함. 전체 실행을 감싸면 번역 중 발생한 실제 버그를 안심시키는 메시지로 바꾸게 되는데, 이는 이 저장소가 추적하는 장애 방식임. 이를 금지하기 위해 한 테스트가 `main()`의 소스 코드를 읽음.

  - **수정 — 도구가 설치된 뒤 사용자 `.env`가 무시되던 문제.** 인수 없이 실행한 `load_dotenv()`는 현재 디렉터리에서 거슬러 올라가지 않고 호출자 파일에서부터 거슬러 올라감. 즉 `site-packages`에서 시작함. 자체 `.env`를 가진 프로젝트에서 실제 콘솔 진입점을 실행해 측정한 결과, `find_dotenv()`는 `''`를 반환하고 키를 불러오지 못했지만 `find_dotenv(usecwd=True)`는 키를 찾았음. 도구가 복제된 저장소에서만 실행될 때는 존재하지 않던 버그였음. 게시 후에는 이 문제가 체계적으로 발생하며, 올바른 설정에서도 API 키가 « 누락됨 »으로 표시되는 것이 유일한 증상이 되었을 것임.

  - **아무것도 검증하지 않게 된 상태에서도 세 개의 게이트가 통과될 수 있었음.** 의도적으로 이동 **전에** 강화함. 잡아내야 할 변경 후에 작성된 안전장치는 아무것도 증명하지 못함. 원본 저장소에서는 각각 녹색이고, 마이그레이션된 복사본에서는 빨간색으로 바뀜 — 양쪽 방향을 모두 측정함.

    - **Lizard는 존재하지 않는 경로를 아무 말 없이 무시함**: rc=0, « 0 file analyzed ». 복잡도 게이트는 158개 함수 / 2247 nloc에서 3개 함수 / 34 nloc로 바뀌고, 0바이트 출력을 내며 통과했을 것임. 이제 범위는 각 항목의 존재 여부를 확인하는 배열임.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`는 실패하지 않음**: unittest와 `coverage xml` 모두 stderr에만 경고를 내고 rc=0을 반환하며, 보고서도 계속 게시함 — 측정된 statements가 1453개에서 141개로 잘려도 마찬가지임. 거의 분석되지 않았기 때문에 프로젝트가 정상인 것처럼 보였을 것임. 두 개의 하한선이 보고서를 보호함: 전체 합계와 측정된 가장 큰 파일.
    - **번역 최신성 검사는 호출 형태에 구조적으로 눈이 멂**: argparse 플래그를 기준으로 삼는데, 파일 이름 변경으로는 바로 그 플래그가 바뀌지 않음. 재현 결과 모듈은 이동했지만 15개 README는 여전히 존재하지 않는 명령을 문서화하고 있었으며 판정은 « 오래된 번역 없음 »이었음. 따라서 일곱 번째 섹션은 옵션이 아니라 **형태**를 확인하고, Lizard hook은 실제 스크립트 범위와 대조됨 — 해당 키 `files:`가 더 이상 일치하지 않으면 pre-commit을 실패시키는 것이 아니라 **건너뜀**.

  - **`requires-python = ">=3.10"`는 더 이상 주장에 그치지 않음.** `sonar-project.properties`는 이미 3.10-3.12를 명시했지만 개발 환경에는 3.12만 있어 실제로 검증된 적이 없었음 — 게시되었다면 공개적인 내부 모순이 되었을 것임. 이제 테스트 workflow가 3.10, 3.11, 3.12에서 전체 테스트를 실행하고, 공개 범위가 포함된 패키지를 설치함.

  - **하한선만 설정하고 상한선은 없음.** `requirements.txt`는 테스트된 lock으로 유지되고, `[project.dependencies]`는 공개 계약이 됨. lock의 정확한 버전을 게시하면 다른 패키지를 사용하는 모든 사용자와 충돌하기 때문임. `<N+1` 상한선도 없음 — 모든 메이저 버전 지연에서 release gate를 실패시키는 `check-deps-fresh.sh`와 정면으로 모순되기 때문임. 하한선 집합으로 해결하고, `openai==1.0.0` 반증 테스트가 `ResolutionImpossible`을 반환하여 검사가 무엇이든 허용하는 것이 아니라 구분한다는 점을 입증함. 또한 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지지 않도록 하는 보호 장치가 있음. PyPI는 같은 번호의 재사용을 허용하지 않음.

  - **새 venv에서 처음부터 끝까지 검증함**: 약 70KB의 wheel에는 `aipmt/*.py`, dist-info, 라이선스만 포함됨. `aipmt --help`는 22개 플래그와 함께 rc=0, `python -m aipmt`는 « usage: aipmt »를 표시하며 « usage: \_\_main\_\_.py »가 아님. `pipx` 설치도 작동함. 무엇보다 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행했으며, 굵은 글씨, 목록, 인라인 코드, 링크와 URL은 보존되고 코드 블록은 번역되지 않음. 마이그레이션 전 318개 테스트는 전후 바이트 단위로 동일한 식별자 목록과 함께 통과함 — 테스트가 무력화되지 않았음을 증명하는 것은 « OK »가 아니라 이것임. 여기에 3계층 설정 테스트 12개가 추가되어 총 330개임.

- **1.10.0** Provider `--use_codex` (ChatGPT 구독 할당량), SDK 및 모델 업데이트, 여러 문단으로 구성된 news 인용 수정 (2026-08-29):

  - **보안 검토 — PR이 마련했지만 모든 곳에서 유지하지 못한 두 가지 안전장치**:

    - **Codex preflight가 전체 `.env`를 바이너리에 전달함.** `_codex_preflight`는 **`env=` 없이** `subprocess.run`를 호출함. 하위 프로세스가 전체 `os.environ`를 상속하므로, `load_dotenv`가 불러온 `.env`의 전체 내용이 전달됨. 계측된 가짜 바이너리로 측정한 결과, preflight에는 6개 provider의 키와 `GITHUB_TOKEN` 하나를 합친 **7개의 비밀**이 도달했음. 반면 대응하는 `_grok_preflight`에는 **0개**였고, 이쪽은 제대로 `env=_grok_env()`를 전달했음. 이 불일치는 PR 내부의 문제였음. 불과 몇 줄 떨어진 곳에 바로 이 불변 조건을 유지하기 위한 `_strip_secret_env`가 이미 존재함. `_codex_env_base()`를 추출해 두 경로가 공유하도록 했고, 수정 후 측정 결과 양쪽 모두 비밀은 0개였음.
    - **« `--deny` fail-closed » 속성이 사용된 형태를 포괄하지 않음.** 주석은 알 수 없는 접두사의 규칙이 시작을 거부한다는 점을 근거로 Grok 격리를 정당화했음. 그러나 `grok 1.0.13`에서 측정한 결과, 이 검증은 **괄호 형태에만** 존재함: `--deny 'CeciNestPasUnOutil(*)'`는 « unknown tool prefix »와 함께 시작을 거부하지만 `--deny 'CeciNestPasUnOutil'`는 조용히 허용됨. 그런데 `GROK_DENY_RULES`는 이름만 사용했음. 따라서 xAI 측에서 도구 이름을 바꾸면, 이미 OS sandbox가 적용되지 않는 환경에서 측정된 유일한 격리 계층이 아무 신호 없이 제거될 수 있었음. 이름이 지정된 8개 규칙은 `Prefix(*)`에 통과하며 각각 CLI에서 알려진 접두사인지 확인됨. catch-all인 `*`는 유일하게 허용되는 리터럴 형태로 유지됨. 테스트 하나가 검증되지 않은 형태로 되돌아가는 것을 방지함.
    - **그 밖의 항목은 깨끗하게 검증됨**: 명령 주입 없음 (모든 곳에서 목록 형태를 사용하고, `shell=True`는 절대 사용하지 않으며, 문서 내용은 stdin 또는 `--prompt-file`로 전달), 안전하지 않은 역직렬화 없음 (`json.loads`만 사용하고 형식 검사 포함), 7개 페이로드에서 우회가 발견되지 않은 경로 순회 수정, 그리고 `--deny '*'`가 CLI에 실제로 적용됨 (`DENY_ENFORCED`를 벗어난 디렉터리 읽기에서 확인).
    - 위에서 추가한 최신성 검사 자체도 원칙을 우회하고 있었음. PyPI 요청이 실패한 패키지를 조용히 건너뛰어 게이트가 녹색이 되었음. 이제 실제로 비교한 패키지 수를 세고, 적용 범위가 불완전하면 실패함.

  - **의존성을 최신화하고 지연 재발을 막는 두 가지 안전망 추가**:

    - **지연은 실제로 장기간 지속되었음**: `openai` 2.54 → **3.6.0**, `anthropic` 0.125 → **1.2.0**, `certifi` 2024.8.30 → **2026.7.22** — 모든 provider 호출에서 TLS를 검증하는 루트 인증서 저장소가 2년 동안 뒤처져 있었음. 원인은 **`.github/dependabot.yml`가 존재하지 않았기 때문**으로 확인됨. 이 파일이 없으면 GitHub는 _security updates_만 활성화하고 Dependabot은 CVE의 영향을 받는 의존성에 대해서만 PR을 제안함. 따라서 `urllib3`와 `idna`는 업데이트했지만 두 SDK가 메이저 버전 뒤처진 채 남아 있었음.
    - **두 메이저 버전은 충돌 없이 공존함.** 이전의 추론과 달리 `openai` 3.x 및 `anthropic` 1.x는 **`httpx2`**로 마이그레이션하고, `mistralai` 및 `google-genai`는 `httpx<1`에 남지만 서로 다른 배포판임. 실제 설치로 확인한 뒤 **7개의 provider 경로를 처음부터 끝까지 테스트**함 — OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI — 각 출력에서 인라인 코드와 링크도 보존됨. « 두 HTTP 스택을 피하자 »는 선호 사항일 뿐 차단 조건이 아니었으며, 측정으로 결론을 냄.
    - **`requirements.txt`는 실제 환경을 설명하지 않았음**: `google-auth`, `cryptography`, `opentelemetry` 스택은 작업 venv에 설치되어 있었지만 선언된 적이 없었음. 따라서 새로 설치해도 테스트한 환경을 재현할 수 없었음. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`는 파일에 있었지만 아무것도 import하거나 요구하지 않았으며, `mistralai` 1.x의 잔재였음. 파일은 직접 의존성만으로 구축한 venv의 완전한 폐쇄 상태를 반영하도록 재생성함. `pip-audit`는 새 구성에서 알려진 취약점을 보고하지 않음.
    - **`.github/dependabot.yml`** (신규)는 버전, pip 및 github-actions의 주간 업데이트를 활성화함. 마이너 버전과 패치는 하나의 PR로 묶음 — PR마다 패치 하나만 올리면 결국 무시되고, 소음은 업데이트의 적임. **메이저 버전은 분리**하며, 각각 실제 호출을 통한 검증이 필요함.
    - **`scripts/check-deps-fresh.sh`** (신규, 게이트에 연결됨)는 프로젝트 판정에 지연을 명확히 표시함. Dependabot은 제안할 뿐 보장하지 않으며 PR이 쌓일 수 있음. 메이저 지연 → 실패, 마이너 지연 → 경고. 게이트가 항상 빨간색이면 결국 무시되기 때문임. PyPI에 연결할 수 없음 → 로컬에서는 명시적 skip, **CI에서는 fail-closed**. 실행되지 않은 검사는 성공이 아님. 양방향으로 검증함. 수정 전의 정확한 상태인 `openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`를 잡아내고, 마이너 지연에는 경고만 표시함.

  - **이 PR 검토에서 나온 수정 사항** — 다섯 명의 검토 에이전트가 diff를 철저히 확인함. 아래 항목은 모두 수정 전에 **측정으로 재현**되었으며, 그중 두 개는 바로 이 버전의 앞부분에서 도입된 회귀였음.
- **회귀 버그 수정 — `_NEWS_CITATION_REGEX`에 지수적 백트래킹이 있었습니다.** 다중 단락 수정으로 반복문 안에 `(?:[ \t]*$|[ \t]+.*)`이 도입되었습니다. `[ \t]+`와 `.*` 사이의 공백 공유가 모호했고, 이 모호성이 반복될 때마다 증폭되었습니다. 패턴과 일치하지 않는, 완전히 합법적인 Markdown 들여쓰기인 `>   texte` 행에서 측정한 결과, **14행에 2,589ms**가 걸렸지만 수정 후에는 0.04ms로 줄었고, 행이 하나 추가될 때마다 약 9배씩 증가했습니다. `--news` 모드에서는 길고 형식에 맞지 않는 blockquote 하나만으로도 원인을 식별할 수 없는 상태에서 작업 timeout까지 번역이 멈출 수 있었습니다. 이제 반복문은 한 번에 전체 행(`\n^>(?![ \t]*—).*`)을 소비하므로 반복마다 일치할 방법이 하나뿐입니다. 실제 231개 문서 코퍼스에서 검증한 결과, **캡처 차이는 0건**이었고 인용문 423개가 동일했으며 다중 단락 본문 14개도 계속 확장되었습니다.
    - **두 개의 provider 플래그를 동시에 지정해도 조용히 사용량 과금이 발생했습니다.** `--use_codex --use_mistral`가 허용되었고, `_select_provider_client`은 Mistral을 먼저 검사했으며, `_resolve_provider`은 명시적인 불리언 값에 우선순위를 부여했지만 둘 다 Mistral로 수렴했습니다. 따라서 사용자는 구독 할당량을 요청했다고 생각했지만 아무 경고 없이 사용량 과금을 받았습니다. 이는 바로 `--use_codex`가 방지하기 위해 존재하는 장애 방식입니다. 이제 6개의 provider 플래그는 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경**: 지금까지 조용히 허용되던 두 provider를 함께 지정한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **프로브가 실패해도 작업 종료 게이트가 통과했습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 4개가 반환 코드를 전혀 확인하지 않고 “stdout을 캡처하고 비어 있으면 결론을 내리는” 패턴을 따랐습니다. 예외(파일 이름 변경, `FileNotFoundError`)가 stderr에 기록되고 stdout은 비어 있으면 검사는 “보고할 내용 없음”이라고 결론 내렸습니다. 이를 막기 위해 작성된 스크립트 내부에서도 “`exit 0` 하나만으로는 아무것도 증명할 수 없다”는 함정이 재현되었습니다. 이제 `probe()` 헬퍼가 반환 코드 0 **및** 종료 센티널을 요구하며, 프로브는 빈 기준 집합을 근거로 결론을 내리지 않습니다. 빈 집합에 대한 assertion은 항상 참이기 때문입니다. 시연 사례로, 위의 배타적 그룹을 추가하자 provider 플래그가 `*_group` 객체를 통과하게 되었고 기존 정규식 `parser\.add_argument\(`은 더 이상 일치하지 않았습니다. **21개 중 6개 플래그**가 조용히 검사 범위에서 빠졌지만 게이트는 통과했습니다.
    - **secret 스캔이 6개 provider 중 4개를 놓쳤습니다.** `[A-Za-z0-9]` 클래스는 하이픈을 제외합니다. 현재 OpenAI 형식인 `sk-proj-…`와 `sk-ant-api03-…`은 두 번째 하이픈에서 실패했고, `AIza…`는 지원 대상에 포함되지 않았습니다. 패턴을 확장하고 `.secrets.baseline`는 스캔에서 제외했습니다. 또한 `.env` 가드는 `git diff --cached`을 조회했는데, 이는 인덱스만 확인하므로 **이미 커밋된** 최악의 경우인 `.env`은 나타나지 않았습니다. 이제 `git ls-files`를 조회합니다.
    - **Codex의 “토큰 웜업”은 실제 웜업이 아니었습니다.** 측정 결과 `codex login status`은 `~/.codex/auth.json`에 접근하지 않았고(mtime과 크기도 변하지 않음), 도움말에는 “Show login status”라고 적혀 있었습니다. 그런데 주석은 토큰을 “한 번, 순차적으로” 새로 고쳐 단일 사용 토큰에서 동시 refresh 위험을 무력화한다고 주장했습니다. 명시된 보호 기능은 존재하지 않았습니다. 이제 주석은 코드가 실제로 하는 일을 설명하며, 진정한 대응책은 여전히 `max_jobs=4`입니다. 또한 검사는 무시하고 있던 `CODEX_BIN`를 준수합니다. `codex`가 없는 컴퓨터에서 `PATH`에 있으면 “인증되지 않음”으로 실패하던 오진도 해결되었습니다.
    - **`.env`가 하위 셸에서 source 처리되었습니다.** `detect_provider`는 명령 치환으로 호출되므로 export가 상위 환경으로 올라오지 않았습니다. 따라서 `.env`에서 정의된 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`은 `main()`에서 수행되는 읽기에는 보이지 않았고, 올바른 구성에서도 “Grok 바이너리를 찾을 수 없음”으로 결론 내렸습니다.
    - **동시성이 명시된 한도를 50% 초과했습니다.** 가드가 README/CHANGELOG 쌍을 시작한 뒤에 배치되어 측정된 피크는 **`max_jobs=2` 3개**였습니다. 주간 할당량을 Chat/Imagine/Voice와 공유하며 측정할 수 없는 Grok에서는 스크립트가 스스로 정한 한도를 지키지 못한 것입니다. 최종 개수는 표시되었지만 28과 비교되지 않아 파일 하나가 없어도 알아차릴 수 없었습니다.
    - **Grok 출력 계약: 이제 `stopReason`가 없으면 실패합니다.** 코드는 계약에서 `end_turn`을 요구하는 곳에 “`end_turn` **또는 없음**”을 적용했습니다. 필드가 없는 payload나 CLI 업데이트로 필드 이름이 변경된 payload는 가드를 조용한 no-op으로 만들었습니다. 또한 `max_turn_requests`는 더 이상 rate limit으로 분류되지 않습니다. 소진된 것은 턴 예산이므로 재시도해도 결과는 같고 90초 대기만 발생합니다. `quota`도 rate limit 표식에서 제외했습니다. 이는 `_codex_is_rate_limited`의 docstring이 이미 설명하고 있었지만 Grok에는 적용되지 않던 이유입니다.
    - **Gemini cascade가 모델별로 메모이제이션됩니다.** 각 세그먼트마다 `minimal`에서 다시 시작했지만 기본 모델은 이를 거부했습니다. 그 결과 정상 경로에서도 세그먼트마다 400 왕복이 발생하고 같은 경고가 반복 출력되었습니다. 경고가 수백 번 반복되면 더 이상 읽히지 않으며, 그렇게 경고는 가면이 됩니다.
    - **기타**: CI의 거부 메시지가 Codex에 하드코딩되어 `--use_grok_cli` 사용자를 `XAI_API_KEY` 대신 `OPENAI_API_KEY`로 안내했습니다. `provider.capitalize()`는 “Grok_cli”와 “Openai”를 표시했습니다. 하위 프로세스 기반의 주석은 두 CLI 모두를 “shim”으로 일반화했지만 Grok 바이너리는 네이티브 ELF입니다. 올바른 근거는 “자체 하위 프로세스를 spawn하는 agent”입니다. `subprocess`의 SAST finding 12개는 정당한 사유와 함께 `# nosec` / `# nosemgrep`로 표시했습니다. `shell=True`이 없는 목록 형식에서는 주입이 불가능하고 문서 내용도 argv를 통해 전달되지 않습니다.
    - **이제 agent 하위 프로세스에 secret이 들어가지 않습니다.** 이름을 열거한 deny-list는 **과금** 불변식만 보호했습니다(Codex는 `OPENAI_API_KEY` 없이, Grok은 `XAI_API_KEY` 없이). 측정 결과 그 밖의 secret 7개는 각 하위 프로세스에 여전히 들어갔습니다. Anthropic, Mistral, Google, Gemini 키, 다른 CLI의 키, 그리고 secret은 아니지만 트래픽을 재지정하는 `OPENAI_BASE_URL`입니다. 두 CLI는 **agent**이며 Grok CLI는 많은 Linux 컴퓨터에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 필터링은 이름 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)을 사용하므로, 이 코드가 알지 못한 채 사용자가 `.env`에 추가한 변수도 포함합니다. CLI에는 이 변수들이 필요하지 않습니다. 인증은 항상 `~/.codex`과 `~/.grok`에 있으며 환경에는 없습니다. 환경을 강화한 상태에서 두 provider 각각을 통한 **실제 번역 성공**으로 검증했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`(테스트 21개)이 provider 플래그의 배타성, `stopReason` 계약, news 정규식의 선형성, CI 거부 메시지, Gemini 메모이제이션, 하위 프로세스 환경에 secret이 없는 상태를 고정합니다. 마지막 assertion은 **일반적**이므로 어떤 목록에도 이름이 없는 키가 있어도 실패합니다. 기존 expurgation 테스트는 자체 상수의 거울에 불과해 자체 루프의 고장 외에는 아무것도 감지할 수 없었습니다. 전체 테스트는 **311개**입니다.

  - **새로운 Grok provider 2개**: `--use_grok`(xAI API, `XAI_API_KEY` 키, 사용량 과금) 및 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독에서 차감 — `--use_codex`와 같은 원리).
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`을 그대로 재사용하고 `base_url`만 변경합니다. 필요한 적응은 하나뿐이었으며 모두에게 이점이 있습니다. `finish_reason`가 이제 `end_turn`도 허용합니다. OpenAI가 `stop`을 출력하는 곳에서 xAI가 출력하는 형식입니다. 모델은 `grok-4.6`(품질)과 `grok-4.3`(절약형)입니다. 참고로 Grok의 절약형 모델은 저장소에서 여전히 가장 비쌉니다. 백만 토큰당 $1.25/$2.50인 반면 `mistral-small-latest`은 $0.15/$0.60입니다. 따라서 이 provider는 가격이 아니라 모델 다양성을 위해 선택합니다.
    - **CLI 모드**: Codex를 기반으로 하되 실제 환경 때문에 네 가지 차이가 있습니다. prompt는 파일로 전달되고(`--prompt-file`, CLI가 stdin을 읽지 않으며 argv에 세그먼트를 넣으면 `ps`에 노출됨), 출력은 stdout의 단일 JSON 객체입니다(JSONL도 파일 `-o`도 아님). 구독은 `grok-4.6`과 `grok-4.5`만 노출하며 sandbox는 적용할 수 없습니다(아래 참조). 하위 프로세스 실행은 `_codex_run_process`에서 Codex와 공통으로 추출했으며, 이미 테스트된 나머지 Codex provider는 건드리지 않았습니다.
    - **측정 결과 `exit 0`만으로는 아무것도 증명할 수 없습니다**: 인증되지 않은 상태에서 CLI는 **stdout**에 `{"type":"error","message":"Not signed in."}`을 쓰고 반환 코드 **0**을 냅니다. 거부나 턴 초과도 동일하게 동작합니다. 따라서 출력 계약에는 네 가지 조건이 동시에 필요합니다. 반환 코드 0, 오류 payload 없음, `stopReason == end_turn`, 그리고 비어 있지 않은 텍스트입니다. 사전 검사도 같은 논리를 따릅니다. 연결이 끊긴 상태에서도 `grok models`는 0으로 종료하므로 stdout에 “not authenticated”가 있어야만 결론을 내릴 수 있습니다.
    - **격리: 비대칭을 의도적으로 수용하고 문서화했습니다.** Codex가 `--sandbox read-only`에서 실행되는 반면, 최근 Linux 컴퓨터 상당수에서는 두 가지 독립적이고 우회할 수 없는 시스템 원인 때문에 Grok sandbox를 적용할 수 없습니다. `sudo` 없이는 해결할 수 없습니다. Ubuntu 24.04부터 AppArmor가 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), `/run/podman`가 `0700`일 때 컨테이너 runtime socket deny-list가 실패합니다(resolver는 `ErrorKind::NotFound`만 보완하고 EACCES는 치명적이 됨). 핵심 함정은 적용할 수 없는 **통합** 프로필이 조용히 **비격리 상태로 시작한다**는 것입니다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않으며 조용히 비격리 상태로 되돌아가지 않습니다. stderr로 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하며 catch-all `*`도 포함합니다. 이는 측정된 유일한 _fail-closed_ 계층입니다(알 수 없는 접두사의 규칙이 있으면 시작이 거부됨). `GROK_TRANSLATE_SANDBOX=read-only`를 사용하면 이를 강제할 수 있으며, 컴퓨터가 이를 준수할 수 없으면 시작이 실패합니다.
    - **안전장치**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`는 하위 프로세스 환경에서 제거됩니다(키가 있으면 사용량 과금으로 전환되고, 상속된 `GROK_SANDBOX`는 적용할 수 없는 프로필을 강제하여 오해를 부르는 메시지를 표시함). MCP/hooks/skills/agents 스위치를 비활성화하고, `--disable-web-search`, `--no-subagents`, `--no-plan`, 임시 workdir, CI에서의 거부, 프로세스 그룹을 종료하는 timeout, rate limit에 대한 back-off를 적용합니다. `--max-turns`은 1이 아니라 6으로 설정합니다. 도구 실행 라운드 뒤에 카운터가 증가하므로 1이면 출력이 잘립니다.
    - **할당량**: Grok pool은 주간 단위이며 **Chat, Imagine, Voice와 공유**되고, 이를 노출하는 명령은 없습니다. `account/rateLimits/read`로 소비량을 계산할 수 있는 Codex와는 다릅니다. 따라서 `regen_translations.sh`는 동시성을 2로 제한하고 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`(테스트 24개). 전체 테스트는 **290개**입니다.
  - **버그 수정 — EN 다중 단락 인용문이 일부만 보호되었습니다(`--news` 모드)**: `_NEWS_CITATION_REGEX`는 인용문 본문으로 `>` 행이 **연속해서** 이어지는 경우만 허용했습니다. 인용문이 여러 단락에 걸쳐 있고 단락 사이에 `>` 빈 줄이 있으면 마지막 단락만 캡처되어 placeholder로 교체되었고, 앞부분은 LLM으로 전달되어 번역되어 돌아왔습니다. 이는 `--news`가 보장하기 위해 존재하는 목적과 정반대입니다. 이제 반복문은 내부의 `>` 빈 줄을 허용하고 탐욕적이지 않게 동작하여, 처음 만나는 빈 줄이 아니라 기울임꼴 행 앞의 `>` 빈 줄에서 멈춥니다.
    - 실제 198개 문서 코퍼스에서 측정한 **영향 범위**는 419개 중 11개 인용문이었습니다. 회귀는 없었습니다. 새 정규식은 정확히 같은 수의 인용문을 캡처하며 다중 단락 본문만 확장됩니다(동일한 본문 408개, 확장된 본문 11개). attribution 행 `> — …`은 lookahead를 유지하므로 여전히 본문에 흡수되지 않습니다.
    - ja/ar로 번역한 69KB 문서의 **end-to-end 증명**: 이전에는 인용문의 첫 단락이 일본어에서 `> GLM-5.3がオープンウェイト化。`로 렌더링되고 아랍어에서도 같은 방식으로 번역되었지만, 이제는 `> GLM-5.3 is now open-weight.`로 유지됩니다. 영어 인용문 행 수는 9에서 10으로 돌아가 원본과 같아졌습니다.
    - 참고로 이 결함은 후속 validator에서 감지되지 않았습니다. validator는 인용문이 존재하는지만 확인하고 완전한지 여부는 확인하지 않기 때문입니다.
  - **기본 provider에서 측정된 비용 절감**: 모델이 `gpt-5`로 시작하기만 하면 `_openai_extra_kwargs`가 `reasoning_effort="medium"`를 전송했으며, `--eco`인 경우도 포함되었습니다. 10단어 문장을 번역할 때 `gpt-5.4-mini`에서 측정한 결과, `medium`는 reasoning token 45개와 출력 토큰 65개를 사용했지만 `none`는 각각 0개와 14개를 사용했습니다. 추론은 번역에 아무런 이점이 없으며 모든 파일의 모든 세그먼트에서 비용이 발생했습니다. 기본값은 `--eco`에서 `none`가 되고, 그 외에는 계속 `medium`입니다. CLI에서 명시적으로 전달한 값은 여전히 우선합니다. `--reasoning_effort`는 이제 `low`/`medium`/`high` 외에도 `none`와 `xhigh`을 허용합니다(모든 모델이 모두 허용하는 것은 아닙니다. 예를 들어 `minimal`은 `gpt-5.4-mini`에서 거부되며, 기존의 매개변수 없는 retry가 이를 처리합니다).
  - **SDK 업데이트 및 Gemini 마이그레이션**: `google-generativeai`(지원 종료일 2025-11-30, 저장소 보관됨)을 통합 SDK **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 다음에 `client.models.generate_content(model=, contents=, config=)`를 사용하고, 시스템 prompt는 세그먼트에 이어 붙이는 대신 `system_instruction`로 전달합니다. `mistralai`은 **2.9.4**로 업데이트했습니다(import가 `from mistralai.client import Mistral`로 변경되며 기존 import는 `ImportError`를 발생시킴. wheel에서 확인). `anthropic`은 **0.125.0**, `openai`은 **2.54.0**으로 업데이트했습니다. 이는 `httpx2`로 전환하기 전 마지막 버전이며 venv에 두 HTTP 스택이 공존하지 않도록 하기 위한 것입니다. 그에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5도 사용할 수 있게 되었습니다.
  - **문서가 아니라 실제 테스트에서 발견한 두 가지 회귀**:
    - `anthropic` ≥ 1.0은 `max_tokens`가 10분 이상을 예상하게 만드는 비스트리밍 호출을 클라이언트 측에서 거부합니다(`ValueError: Streaming is required...`). 이 안전장치는 0.34.2에는 없었으며 `max_tokens=32768`를 사용하는 모든 Claude 호출을 망가뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 완전한 응답만 사용하는 호출을 streaming으로 전환하지 않도록 했습니다.
    - `thinking_level="minimal"`는 Gemini 모델 카탈로그의 일부에서만 허용됩니다. `gemini-3.1-flash-lite`는 이를 지원하지만 `gemini-3.7-flash`와 `gemini-3.1-pro-preview`는 400으로 거부합니다. 따라서 `_gemini_generate_with_fallback`를 적용했습니다. `minimal` → `low` → thinking_config 없음의 cascade이며, 기존 OpenAI fallback과 같은 방식입니다. 최적화 매개변수 하나 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델 갱신**, 모두 실제 호출로 검증: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 배치에서 −60%) 및 `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%); Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신) 및 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜가 없는 정식 ID); Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 및 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(안정 버전이며 `3.5-flash-lite`보다 저렴).
Mistral은 변경되지 않았으며, 네 모델 중 `mistral-large-latest`이 여전히 최고의 가성비를 보입니다. 참고로 `gemini-3.1-pro-preview`보다 최신인 Pro급 Gemini 모델은 존재하지 않습니다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시되지 않았으며, 3.5/3.6/3.7 라인은 전적으로 Flash입니다.
  - **Gemini로 전환하기 전 측정한 A/B 테스트**: `README.md`을 `gemini-3.1-pro-preview`로 일본어 번역한 뒤 `gemini-3.7-flash`로 번역했습니다. 구조는 완전히 동일했으며(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존), **48초가 아니라 8초**가 걸렸습니다. 번역이나 비라틴 스크립트에 대해 이 두 모델을 비교한 공개 벤치마크는 없었으므로, 그렇지 않았다면 전환은 단순한 추정에만 근거했을 것입니다.
  - **Claude 응답 블록 필터링**: `_call_claude`은 유형을 필터링하지 않고 `block.text for block in response.content`을 수행했습니다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 삽입하는데, 이 블록은 `.thinking`이 아니라 `.text`을 노출합니다. 따라서 첫 번째 세그먼트에서 불투명한 `AttributeError`을 만나면 번역이 중단됩니다. 이제 `thinking`, `redacted_thinking`, `tool_use`, `tool_result`는 제외됩니다(알 수 없는 유형이 텍스트를 담고 있어도 허용할 수 있도록 음의 목록 사용). 텍스트 블록이 전혀 없는 응답은 명시적인 오류를 발생시킵니다. `thinking={"type": "disabled"}`은 모든 호출에 전달됩니다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 사용 중단일이 지난 모델을 제거했습니다(2026-07-31에 단종된 `magistral-*` 제품군, 2026-06-01에 단종된 `gemini-2.0-*`, 2026-03-09에 단종된 `gemini-3-pro-preview`, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`). 한도도 수정했습니다. Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1 000 000 → **1 048 576**(실제 입력 한도), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1,05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest`, `ministral-*` 제품군을 추가했습니다. 참고로 이 한도는 여전히 참고용이며, `translate()`은 세그먼트 분할을 `min(16000, limite)`로 제한합니다.

  - **Provider `--use_codex`**: 공식 Codex CLI(`codex exec`)를 비대화형 모드로 실행하는 다섯 번째 provider이며, 사용량에 따라 과금되는 API를 호출하지 않습니다. 번역 비용은 이미 결제한 ChatGPT 구독의 할당량에서 차감됩니다. OpenAI가 이 용도에 대해 문서화한 유일한 방법입니다. 요금제별 제공 기능 표에는 « Codex SDK, `codex exec`, and scriptable workflows »가 Plus/Pro/Business/Enterprise에서 제공되는 것으로 나와 있습니다. 한편 `~/.codex/auth.json`의 토큰은 Platform API 호출을 인증하지 않으며, 이 스크립트는 해당 토큰을 절대 읽지 않습니다. 인증과 갱신은 계속 CLI가 관리합니다.
  - **npm뿐 아니라 pip로도 설치 가능한 Codex 바이너리**: `_resolve_codex_binary()`은 먼저 `CODEX_BIN`에서 바이너리를 찾고, 그다음 `PATH`에서 찾은 뒤, OpenAI가 배포하는 공식 Python 패키지 **`openai-codex-cli-bin`**를 확인합니다(이는 `openai-codex` SDK의 의존성입니다). 따라서 Python 프로젝트에서 `--use_codex`를 사용하기 위해 더 이상 전역 npm 설치가 필요하지 않습니다. 이 패키지는 `requirements.txt`에 추가하지 않습니다. 바이너리 크기가 약 250MB이므로 선택적 provider를 위해 모든 사용자에게 설치를 강제하게 되기 때문입니다. 처음부터 끝까지 검증했습니다. `codex`이 `PATH`에 없을 때 패키징된 바이너리를 찾아 전체 번역이 6초 만에 완료됩니다.
  - **« 구독 모드 » 보장**: `OPENAI_API_KEY`과 `CODEX_API_KEY`를 하위 프로세스의 환경에서 제거합니다. 이 보호 장치가 없으면 `.env`에 있는 키로 인해 눈에 보이는 신호 없이 Codex가 사용량 기반 과금으로 전환될 수 있습니다. 이는 이 provider가 존재하는 이유와 정확히 반대되는 동작입니다.
  - **CLI 함정을 테스트로 차단**:
    - `codex exec`은 프롬프트를 인수로 전달한 경우에도 stdin을 **읽습니다**. stdin을 닫지 않으면 모델을 호출하지 않은 채 명령이 시간 초과까지 대기합니다(재현 결과: 180초 후 종료 코드 124, 0바이트). 따라서 `communicate(input=...)`가 필수입니다.
    - npm으로 설치되는 `codex`은 실제 Rust 바이너리를 `spawn`하는 Node shim입니다. 실제 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `SIGKILL`이 `subprocess.run(timeout=)`을 수행한 뒤에도 살아남아 할당량을 계속 소비할 수 있습니다. 그래서 `Popen(start_new_session=True)` + `os.killpg`가 필요합니다.
    - CLI는 `turn.failed`를 출력하면서도 종료 코드 0을 반환할 수 있습니다. 따라서 반환 코드뿐 아니라 JSONL 출력(`--json`)도 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킵니다.
  - **Rate limit 백오프**: CLI는 내부 재시도(`max_retries = 0`)를 구현하지 않습니다. 분류는 부분 문자열이 아니라 JSON payload 구조(`status: 429` / `error.type`)를 기준으로 수행합니다. « quota »라는 단어가 복구 가능한 429 오류와 복구 불가능한 `insufficient_quota` 모두에 나타날 수 있기 때문입니다.
  - **CI 보호**: `--use_codex`은 `CI` 또는 `GITHUB_ACTIONS`이 정의되어 있으면 거부됩니다. 구독 인증은 공유 runner용으로 설계되지 않았으며, OpenAI도 공개 저장소에서 이 작업 흐름을 명시적으로 권장하지 않습니다.
  - **모델**: `gpt-5.6-sol`(품질) 및 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 제품군은 CLI와 Platform API에서 공통으로 사용되지만, ChatGPT 계정이 모든 모델을 사용할 수 있는 것은 아닙니다. 허용 목록은 로컬 검증 없이 서버 측에서 적용되며, 비정상적인 모델을 사용하면 경고가 발생합니다. Plus 요금제에서 Luna는 5시간 창당 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개만 제공합니다. 따라서 `--eco`은 모든 일괄 처리에 권장되는 모드입니다.
  - **수정된 버그 — `regen_translations.sh`가 전체 성공 후에도 오류를 발생시킴**: `trap ... EXIT`가 더 이상 존재하지 않는 `failed_log`을 참조하고 있었습니다. 이는 `main()`의 `local` 변수로, trap이 실행될 때는 이미 사라진 상태였습니다. `set -u`에서는 이로 인해 `failed_log: unbound variable`이 발생하고 스크립트가 종료 코드 1로 끝났습니다. 28개의 번역은 올바른 상태였지만, 가장 비용이 큰 단계인 재생성 직후 `release.sh --auto`(`set -e`)이 중단되었을 것입니다. 해당 변수를 전역으로 만들고 trap에서 존재 여부를 검사하도록 했습니다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 이제 종료 요약에 다시 표시됩니다.
  - **`REGEN_MODEL`**: provider의 기본값보다 우선하여 특정 모델을 강제하는 `regen_translations.sh`의 새 환경 변수입니다. 예를 들어 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`를 사용하면 처리량 중심 모델인 `--eco` 대신 구독 할당량의 고급 모델로 재생성할 수 있습니다.
  - **`regen_translations.sh`**: 명시적으로 opt-in할 때만 사용할 수 있는 `REGEN_PROVIDER=codex`입니다(사용자 모르게 구독 할당량을 소비하지 않도록 자동 감지하지 않음). Codex 갱신은 순차적으로 한 번 수행한 뒤 병렬 처리를 시작합니다. 갱신 토큰은 회전식 일회용이므로 동시 작업이 `codex login` 세션을 무효화할 수 있기 때문입니다. 동시성은 4로 낮췄습니다.
  - **관련 리팩터링**: `_dispatch_provider_call`은 provider 이름을 반환하는 `_resolve_provider()`을 통해 매개변수를 8개에서 6개로 줄였습니다. 전체 호출 체인에 네 번째 불리언을 전달하는 대신 provider 이름을 사용합니다. `args`보다 명시적 불리언을 계속 우선하여, 최소한의 `Namespace`로 `translate(..., use_mistral=True)`을 호출하는 테스트를 보존합니다.
  - **테스트**: 새로운 `tests/test_codex_provider.py` 파일(테스트 48개)이 argv, 정리된 환경, 서문 방지 계약, 무음 실패, timeout/killpg, 백오프, preflight, provider 확인, Gemini 추론 cascade, Claude 블록 필터링, 다중 단락 news 인용을 다룹니다. 전체 테스트 모음은 290개로 늘었습니다.
  - **실제 검증**: 프로젝트의 `README.md`을 Codex로 **14개 언어**로 번역한 결과, 참조 번역과 구조가 완전히 동일했습니다(코드 블록 14개, 제목 24개, 표 행 25개, HTML 링크 13개, 이미지 13개, URL 19개, 문자 단위로 동일한 코드 블록, placeholder 잔여물 0개). 69KB 분량의 뉴스 기사에서 `--news` 모드로 생성한 `gpt-5.6-luna` 및 `gpt-5.6-sol` 출력은 모두 en/ja/ar에서 후속 애플리케이션 검증을 통과했습니다. `account/rateLimits/read`을 통해 측정한 사용량은 `--eco` 모드에서 카운터 반올림 임계값 미만으로 유지되었습니다(5시간 창의 0%).

- **1.9.2** 중첩 괄호 또는 FR 접두사가 있는 news attribution URL 추출 수정 (2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`에서 attribution URL을 추출할 때 `re.search(r"\((.+?)\)", attribution)` 정규식(괄호 사이를 lazy capture)을 사용했습니다. `(relayé par [@user sur X](https://x.com/.../123))`와 같은 attribution(중첩 괄호: 바깥쪽 `(` + Markdown 링크의 `]()`)에서는 캡처가 처음 만나는 `)`에서 중단되어 문자열이 잘리고 FR 접두사까지 포함했습니다: `relayé par [@user sur X](https://x.com/.../123`(마지막 `)` 누락). 그 결과 `_validate_news_post`이 번역된 출력에서 이 문자열을 찾으려다 항상 실패했습니다(두 가지 원인: 잘린 `)`과 « relayé par »가 `relayed by`/`weitergeleitet von`/…로 번역됨). low → medium → high → gpt-5.5 전체 cascade를 통과할 수 없었습니다.
  - **수정**: 정규식을 `re.search(r"\]\(([^)]+)\)", attribution)`로 변경했습니다. 이는 Markdown 링크의 `](url)`을 구체적으로 대상으로 하며, **순수 URL만** 캡처합니다(FR 접두사와 잘림 제외). 번역 중에는 `#URL{N}#` placeholder가 불변성을 보존합니다. 다음 두 문제 패턴 모두에 견고합니다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥쪽 괄호가 없는 FR 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 2개를 추가했습니다.
    - `test_extract_attribution_url_with_nested_parens`(Genspark CEO E2B 버그의 정확한 재현 사례)
    - `test_extract_attribution_url_with_french_prefix`(`via`를 포함한 변형)
  - **커버리지 공백**: `check-editorial-coverage.py`는 편집 구문은 검증하지만 translator를 통한 번역 가능성은 검증하지 않습니다. 가능한 개선 사항으로는(이번 v1.9.2 범위 외) 게시 전에 위험 패턴을 감지하도록 dry-run에서 attribution 추출을 시뮬레이션하는 검사를 추가하는 방법이 있습니다.

- **1.9.1** 번역 marker 노트의 CTA 레이블 i18n 수정 (2026-05-10):

  - **수정된 버그**: 번역된 파일 상단 marker 배너의 CTA 링크 레이블 `[Voir le projet sur GitHub ↗]`이 모든 대상 언어에서 **프랑스어로 남아** `target_lang`를 따르지 않았습니다. URL과 저장소 slug를 보존하기 위해 Python 측에서 조립되므로 LLM에는 절대 보이지 않았고, 번역 단계에서도 수정할 수 없었습니다. v1.9에서 `marker` 형식이 추가된 이후 발생한 무음 회귀였습니다.
  - **수정**: 15개 언어를 현지화된 레이블에 매핑하는 새 상수 `_VIEW_PROJECT_LABELS`를 추가했습니다. 이제 `_translation_note_invariants(target_lang)`과 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달합니다. 언어를 알 수 없는 경우에는 안전을 위해 KeyError 대신 `fr`로 대체합니다.
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 수정했습니다(target_lang `ja` → 예상 일본어 레이블). 새 테스트 2개도 추가했습니다: `test_source_link_label_localized_per_target_lang`(라틴 문자, 표의 문자, 아브자드를 포함하는 7개 언어에 매개변수화) 및 `test_source_link_label_falls_back_to_french_for_unknown_target`. 전체 테스트는 `test_translation_note_position.py`에서 38개에서 40개로 늘었습니다.
  - **Backward-compat**: 기본값이 있는 `target_lang="fr"` 시그니처를 사용하므로 `args.target_lang` 없이 호출하는 외부 프로그래밍 호출자도 수정 없이 계속 작동합니다.
- **1.9** 자동 실패 수정 + 완전한 품질 도구 + 다중 위치 번역 노트 (2026-05-07) :
  - **다중 위치 번역 노트 + "embed card" 형식 marker** :
    - 새로운 CLI 옵션 (추가 기능, 기본값은 변경되지 않음 → **비호환 변경 없음**) :
      - `--note_position {top,bottom,both}` (기본값: `bottom`): 번역된 파일의 위쪽, 아래쪽 또는 양쪽에 노트를 배치합니다.
      - `--note_format {legacy,marker}` (기본값: `legacy`) :
        - `legacy`는 v1.8 동작(굵은 단락 `**…**`)을 **byte-for-byte**로 엄격하게 재현합니다.
        - `marker`는 보이지 않는 Markdown 링크 reference definition(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에, "GitHub repo embed card"와 같은 렌더링을 위한 구조화된 **3개 단락 blockquote**를 출력합니다. 프로젝트 제목은 inline code(`**\`ai-powered-markdown-translator\`\*\*`)로 표시되고, LLM이 번역한 설명과 화살표가 표시되는 CTA 링크(`[Voir le projet sur GitHub ↗](URL)`)가 포함됩니다. remark 플러그인으로 빌드 시 활용할 수 있습니다(jls42.org 블로그 → `remark-translation-banner` 플러그인 참조).
    - **LLM에 절대 전송하지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문장 번역 후 Python 측에서 조립됩니다. LLM은 slug `ai-powered-markdown-translator` 또는 `https://github.com/jls42/...`을 절대 보지 않으므로 renderer/case/scheme이 변경되지 않습니다.
    - **Frontmatter 인식 삽입**: `top` 또는 `both` 모드에서는 노트를 YAML frontmatter의 **닫는 `---` 블록 뒤**에 삽입합니다. Helper `_split_frontmatter`은 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter가 있으면 **`RuntimeError`를 발생**시키며, 해당 파일은 잘못된 위치에 노트를 포함해 기록되지 않고 `failed_files`으로 이동합니다.
    - **모델 sanitizer whitelist**: `_sanitize_model`은 `[A-Za-z0-9._:/-]`에 속하지 않는 모든 문자를 `_`로 대체하며, 비어 있으면 `unknown`로 대체합니다. remark Astro 플러그인 측 validator와 일치하며, marker 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 리팩터링**: `_append_translation_note` (단일 거대 함수) → 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`). Builder와 composer를 분리했습니다(builder는 구분자 없는 순수 블록을 반환하고, composer는 위치에 따라 `\n\n`을 적용). 생성 코드와 source helper는 동일한 3개 단락 조립기를 공유합니다.
    - **`_quote_lines` blank-preserving**: 각 줄 앞에 `> `을 붙이고, 빈 줄은 `>`만 남도록 변환합니다. 이를 통해 mdast가 blockquote 안에서 줄바꿈이 있는 하나의 단락이 아니라 3개의 서로 다른 단락(제목 / 설명 / 링크)을 인식할 수 있습니다.
    - **적응형 `_build_translation_note_block`**: LLM이 보존한 단락 수에 따라 동작합니다(3개 = 완전한 card 형식, 2개 = 문장 + 링크, 1개 = fallback). 1개 단락 fallback에서는 Markdown 링크 `](`이 감지될 때 더 이상 `**...**`으로 감싸지 않습니다. 링크 주위의 `<strong>` 렌더링이 불안정하기 때문입니다.
    - **하위 호환성**: `_compose_with_notes` 측의 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")` — 이러한 속성이 없는 Namespace(기존 테스트, 외부 프로그래밍 호출)도 수정 없이 계속 작동합니다.
  - **긴 번역에서의 자동 실패 수정** :
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 번역 후 언어 검증 추가: 결정론적 계층(소스에서 추출한 내용의 verbatim 재발견) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에서 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768` (16k 세그먼트에서 발생하는 잠재적 truncation과 FR→JA/ZH/KO/AR/HI 교차 스크립트의 여유 부족 방지)
    - Heading 인식 세분화: 세그먼트 후반부에서 H2/H3에 우선순위를 부여(각 세그먼트가 완전한 의미론적 섹션으로 시작)
    - 오류를 종료 코드가 0이 아닐 때까지 전파: `translate_markdown_file`은 `success` / `failure` / `skipped`의 타입 상태를 반환하며, 하나 이상의 파일이 실패하면 `main()` `sys.exit(1)` (단일 파일 및 batch)
    - 모든 provider에 empty-content guard, 소스/출력 sanity ratio(≥ 500자, < 5%이면 거부), 코드 placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 후 정규화(heading에 붙은 구분자/링크), `BadRequestError`을 사용하지 않는 `reasoning_effort` retry
    - `langdetect==1.0.9` 의존성 추가
  - **pre-commit 품질 도구** ("완전한 EurekAI 유형", 14개 hook) :
    - Pre-commit: ruff(린트+포맷), shellcheck, prettier(md/yaml/json), detect-secrets(보호된 API key 4개), Lizard(CCN ≤ 12), pre-commit-hooks v5(공백, EOF, 대용량 파일, shebang 등)
    - Pre-push: mypy(점진적 lax 모드), Opengrep SAST(translate.py + scripts/), pip-audit(초기 reporting 모드), unittest discover(tests/ + scripts/tests/)
    - `scripts/`의 로컬 wrapper는 `./venv/bin/python`를 사용합니다.
    - `scripts/audit_verdict.py`: 11개의 unittest로 pip-audit JSON parser를 테스트하며, jls42-astro parser를 Python으로 이식한 버전입니다.
    - 초기 ruff 위반 7개 수정: B904(raise from) ×2, B007(미사용 dirs), C408(dict literal), C419(list-comp), SIM105(contextlib.suppress), SIM110(any())
    - Lizard는 일시적으로 `translate.py`을 제외합니다(CCN 21-47인 함수 4개, 리팩터링 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 철저한 커버리지** :
    - GitHub Actions workflow `SonarCloud`(sonarcloud.yml + sonar-project.properties): 모든 push 및 pull-request에서 분석, `coverage.xml`를 통한 coverage
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py` (`unittest` stdlib): 자동 실패 오류 체인의 6개 연결 고리를 모두 테스트
    - `tests/test_orchestration.py` (+79개 테스트): `translate.py`의 orchestration 계층을 테스트(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallback, o1-series prompt 형식, `_validate_translation_output`의 early-return 분기)
    - `scripts/tests/test_audit_verdict.py`: `main()`(stdin/stdout) 및 subprocess를 통한 `if __name__ == "__main__"` 블록을 테스트
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`은 위치 × 형식 매트릭스(E2E `marker+top|bottom|both` 및 `legacy+top|bottom|both` 포함), 다중 줄 접두사 추가, byte-for-byte 하위 호환(golden literal), sanitizer, frontmatter 분할(닫히지 않은 fence에서의 raise 포함), 3개 단락 형식, 2개 단락 fallback, 1개 단락 + Markdown 링크 guard, 그리고 제목과 URL이 LLM에 절대 전송되지 않음을 단언하는 중요한 안전장치 `TestLLMPayloadExcludesInvariants`을 테스트합니다. **테스트 190개 통과**, 회귀 0건.
  - 문서화: badge가 포함된 `README.md`(프랑스어 + 14개 번역), `CLAUDE.md`(pre-commit workflow + 상세 CI watch), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026 모델 업데이트 (2026-03-17, tag `v1.8`) :
  - 기본 모델 업데이트(2026년 3월) :
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token limit 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder를 사용한 영어 인용 보호, `LANG_FLAGS` 매핑(15개 언어), 대상 언어별 flag 처리
  - 복원 전 news placeholder 검증(placeholder를 삭제한 LLM이 인용 없는 출력을 자동으로 생성하던 회귀 수정)
  - `regen_translations.sh` 스크립트를 이식 가능하게 변경(절대 경로, pwd 의존성 없음)
  - README/CHANGELOG language bar에 프랑스어 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능 :
  - 번역 시 원본 파일명을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오기 위한 `.env` 파일 지원
  - **inline code 보존**: backtick(`` `...` ``)을 이제 번역 중 보호
  - 시스템 prompt 개선 :
    - YAML frontmatter에서 따옴표 처리 개선
    - template 변수 `{variable}` 보호
    - 요청하지 않은 번역자 노트 금지
  - 364개 파일에서 성공적으로 테스트(blog jls42.org 마이그레이션)
- **1.6** 새로운 기능 :
  - 번역을 위한 Google Gemini API 지원(`--use_gemini`)
  - 2026년 기본 모델 업데이트 :
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 순회하지 않는 단일 파일 번역(`--file`)
  - 새로운 간소화된 명명 패턴: `{base}-{lang}.md`
  - 모델명을 포함한 기존 형식을 유지하는 `--include_model` 옵션
  - 기본 token limit(128k)을 적용한 목록에 없는 모델 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항 :
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`으로 업데이트
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`으로 업데이트
  - **번역 prompt 최적화:**
    - 직접 번역 및 번역 노트용 prompt를 더 명확하고 효율적으로 개선했으며, 메타데이터와 특정 서식 요소의 보존을 위한 상세 지침을 포함했습니다.
  - **코드 리팩터링:**
    - Mistral AI client 초기화를 위해 `MistralClient`를 `Mistral` 클래스로 교체
    - 가독성과 유지보수를 위한 import 재구성
    - 번역 중 원본 서식을 보존하도록 텍스트 세분화와 code block 처리 개선
  - **출력 파일 관리:**
    - 출력 파일명에서 모델과 언어의 순서를 뒤집음(예: `f"{base}-{args.target_lang}-{args.model}.md"`)으로써 번역의 정리와 검색을 용이하게 함
  - **기타 개선:**
    - 불필요한 빈 줄을 제거하여 코드 정리
    - script의 구조와 가독성을 개선하기 위한 사소한 조정
- **1.4** 새로운 기능 :
  - 번역을 위한 Anthropic Claude API 지원
  - 명확성과 효율성 향상을 위한 prompt 최적화
  - 코드 유지보수성을 개선하기 위한 사소한 조정
- **1.3** 개선 사항 및 새로운 기능 :
  - code block 처리 개선
  - 출력 파일 처리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 모델과 언어의 순서를 뒤집음
- **1.2** changelog 수정
- **1.1** Mistral IA API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**gpt-5.6-luna로 프랑스어에서 한국어로 번역된 기사.**
