### 변경 기록

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.11.1** 문서 수정: README가 마침내 일곱 가지 provider 경로를 모두 안내 (2026-09-03):

  - **1.11.0의 PyPI 페이지에는 “4개의 API + Codex CLI”라고 적혀 있었다.** 실제 코드에는 API 방식의 OpenAI, Mistral, Claude, Gemini, Grok와 구독 방식의 Codex (ChatGPT), Grok 등 일곱 가지가 노출되어 있으며, 사용량에 따른 과금은 없다. 두 가지 Grok 모드가 소개 문구와 _Multi-Provider_ 항목에서 빠져 있었고, 14개 번역본도 같은 오류를 반복하고 있었다. 패키지의 긴 설명은 버전별로 고정되므로, 소개 페이지를 수정하려면 번호를 새로 발행해야 했다. 이것이 이번 버전의 유일한 발행 이유다. **코드 변경은 없다.**
  - `CLAUDE.md`는 발행에서 도입한 내용에 맞춰 정렬되었다. gate 카운터(16, `--full`에서 17), 활성화된 11개 워크플로, `gh pr checks`에 표시되지 않는 두 Sonar/Codacy 카운터(hotspots, Codacy API), `# nosemgrep`를 `ruff-format`마다 이동한 내용, OIDC 교환에 필요한 GitHub 환경, 그리고 _pending publisher_가 이름을 예약하지 않는다는 사실이 포함된다.

- **1.11.0** PyPI 발행: 저장소를 복제하지 않고 `pip install ai-powered-markdown-translator`에 이어 `aipmt` 명령을 실행 (2026-09-03):

  - **단일 파일 스크립트가 설치 가능한 패키지가 되었다.** `translate.py`가 루트에서 `src/aipmt/translate.py`로 이동했으며, 콘솔 진입점 `aipmt`와 그에 해당하는 `python -m aipmt`가 추가되었다. 기여하려면 여전히 복제한 저장소가 필요하다. 테스트, 28개 번역본, 품질 도구가 저장소에 있기 때문이다. 하지만 사용만 할 때는 더 이상 필요하지 않다.

    - **import 이름은 `aipmt`이며 절대로 `translate`가 아니다.** 실제로 조용한 이름 충돌이 발생하기 때문이다. PyPI 패키지 `translate`(v3.8.1, 마지막 업로드 2026-07-06)는 같은 이름의 디렉터리를 설치한다. venv에서 재현한 결과, 디렉터리가 모듈보다 우선되어 `translate.main`가 사라지고 진입점이 `AttributeError`에서 실패한다. 그런데 `pip check`는 rc=0으로 “No broken requirements found”라고 응답한다. 사용자의 `pip install translate` 하나만으로도 진단 가능한 오류 없이 CLI가 망가질 수 있었다. 실제 wheel로 반증도 확인했다. 패키지 위에 `pip install translate`를 설치해도 `aipmt --help`는 설치 전후 모두 rc=0이며, 두 CLI가 공존한다.
    - **배포 이름은 길게, 명령은 짧게.** `ai-powered-markdown-translator`는 PyPI 검색으로 패키지를 찾을 수 있게 한다. 프로젝트를 이미 아는 사람만 알 수 있는 약어만 사용하면 검색되지 않는데, 이번 발행의 목적이 바로 검색 가능하게 만드는 것이기 때문이다. 그럴듯한 후보 두 개는 검증을 통해 제외했다. `ai-markdown-translator`는 2024년부터 같은 목적의 도구가 npm에서 사용 중이며 이 저장소보다 17개월 먼저 존재했고, `aimt`는 `aim`(v3.29.1)과 한 글자 차이뿐이다. 후자는 같은 분야의 활성 패키지이므로 지속적인 혼동을 일으키기에 최악의 구성이다. 덧붙여 방법론상의 함정도 있다. `pypi.org/project/<nom>/`는 어떤 이름이든 200을 반환한다(봇 방지 페이지). 신뢰할 수 있는 것은 JSON API뿐이다.
    - **평면 패키지보다 `src/` 레이아웃을 선택했다.** 평면 패키지는 테스트의 여섯 `sys.path.insert(..., "..")`를 유지했을 것이다. 그런데 바로 그것이 결함이다. 이 파일들은 패키지가 아니라 소스 트리를 import하게 만들어 패키징 오류를 가린다. 실제 비용은 대체 규칙 하나가 추가되는 것이다.

  - **이제 키를 한 번만 설정하면 된다.** 설치된 CLI에는 영속적인 설정이 전혀 없었다. 환경 변수와 현재 디렉터리의 `.env`만 남아 있었다. `find_dotenv`는 시스템 루트까지 올라가므로 **홈 디렉터리 아래에서 작업할 때는** `~/.env`를 찾았지만, 다른 곳에서 작업할 때는 아무것도 찾지 못했다. 이는 설계상의 선택이 아니라 명령을 실행한 위치에 따라 달라지는 적용 범위였다. 따라서 기존 두 계층 아래에 세 번째 계층인 `~/.config/aipmt/.env`가 추가되었다.

    - **우선순위를 코드로 하드코딩하지 않았다.** 우선순위는 `load_dotenv`의 기본값인 `override=False`에서 도출된다. 각 계층은 이전 계층이 비워 둔 부분만 채운다. 따라서 순서는 환경 변수 → 프로젝트의 `.env` → 사용자 설정이다. 이 순서는 구조가 아니라 동작 테스트로 확인했다. 두 호출의 순서를 바꾸면 테스트가 실패하고, 세 번째 계층을 제거해도 실패한다.
    - **TOML이 아닌 `.env` 형식**을 의도적으로 사용했다. `python-dotenv`는 이미 의존성이며, 15개 README에 문법이 이미 문서화되어 있고, 동일한 파일을 두 범위에서 사용할 수 있다. 새로운 의존성이나 문법은 없다. 위치는 `XDG_CONFIG_HOME`가 **절대 경로인 경우** 이를 따르며, 상대 경로는 사양에 따라 무시한다. 그렇지 않으면 설정 위치가 다시 현재 디렉터리에 종속되기 때문이다. Windows에서는 `APPDATA`를 사용한다.
    - **두 가지 선택지를 이유와 함께 제외했다.** 시스템 키체인(`keyring`)은 데스크톱에서는 더 안전하지만 headless 환경(서버, 컨테이너, CI)에서는 실패한다. 이는 바로 일괄 번역의 사용 사례이므로 opt-in 기능으로는 적합하지만 기본값으로는 부적합하다. `--api-key` 플래그를 사용하면 키가 셸 기록에 남고 `ps`에 노출된다.
    - **키가 없을 때 호출 스택을 더 이상 표시하지 않는다.** 사용자는 `site-packages`를 가리키는 Python 스택과 “환경 또는 .env”라고만 적힌 메시지를 받았으며, 두 번째 파일을 어디에 만들어야 하는지는 안내받지 못했다. 이제 세 위치와 정확한 경로를 모두 열거하고, 명령은 2로 종료된다. 방어 범위는 **의도적으로 좁다**. `except ValueError`는 설정 단계에만 적용된다. 전체 실행을 감싸면 번역 중 발생한 실제 버그를 안심시키는 메시지로 바꾸게 되며, 이는 이 저장소가 추적하는 장애 방식이다. 이를 금지하기 위해 `main()`의 소스를 읽는 테스트가 추가되었다.

  - **수정 — 도구가 설치된 뒤 사용자의 `.env`가 한 번 무시되었다.** 인자 없는 `load_dotenv()`는 현재 디렉터리에서 거슬러 올라가는 것이 아니라 호출 파일에서부터 거슬러 올라간다. 즉 `site-packages`에서 시작한다. 자체 `.env`를 가진 프로젝트에서 실제 콘솔 진입점을 실행해 측정한 결과, `find_dotenv()`는 `''`를 반환하여 키를 로드하지 않았지만 `find_dotenv(usecwd=True)`는 키를 찾았다. 도구가 복제한 저장소에서만 실행되던 동안에는 이 버그가 존재하지 않았다. 그러나 발행 후에는 정상적인 설정에서도 API 키가 “누락”되었다는 증상만 남긴 채 항상 발생했을 것이다.

  - **아무것도 검증하지 않게 된 상태에서도 세 개의 gate가 통과할 수 있었다.** 이 gate들은 이동 전에 의도적으로 강화했다. 잡아내야 할 변경 이후에 작성된 보호 장치는 아무것도 증명하지 못하기 때문이다. 각각 원본 저장소에서는 통과하고, 마이그레이션한 복사본에서는 실패하도록 양방향을 측정했다.

    - **Lizard는 존재하지 않는 경로를 조용히 무시한다.** rc=0, “0 file analyzed”가 된다. 복잡도 gate는 158개 함수 / 2247 nloc에서 3개 함수 / 34 nloc으로 줄어들고, 출력은 0바이트가 된다. 이제 범위는 각 항목의 존재 여부를 확인하는 배열이다.
    - **존재하지 않는 모듈에 대한 `coverage run --source=`는 실패하지 않는다.** stderr에만 경고를 내고 unittest와 `coverage xml` 모두 rc=0을 반환하며, 보고서도 1453개에서 141개 statement로 축소된 채 게시된다. 거의 분석되지 않았기 때문에 프로젝트가 정상으로 보였을 것이다. 보고서를 지키는 하한선은 두 가지다. 전체 합계와 측정된 가장 큰 파일이다.
    - **번역 최신성 검사는 호출 형식에 구조적으로 눈이 멀어 있다.** argparse 플래그를 기준으로 삼는데, 파일 이름 변경은 바로 그 플래그를 바꾸지 않는다. 재현 결과 모듈을 이동해도 15개 README가 여전히 존재하지 않는 명령을 문서화하고 있었지만 판정은 “오래된 번역 없음”이었다. 따라서 일곱 번째 섹션은 옵션이 아니라 형식을 확인한다. 또한 Lizard hook은 실제 스코프와 대조된다. 해당 키 `files:`가 더 이상 일치하지 않아도 pre-commit을 실패시키는 것이 아니라 건너뛰게 한다.

  - **`requires-python = ">=3.10"`가 더 이상 주장에 그치지 않는다.** `sonar-project.properties`는 이미 3.10-3.12를 선언했지만, 개발 환경에는 3.12만 있어 실제로 검증된 적이 없었다. 발행으로 공개되었을 내부 모순이다. 이제 테스트 워크플로가 3.10, 3.11, 3.12에서 패키지를 설치한 뒤 테스트 전체를 실행하므로 공개된 버전 범위까지 검증된다.

  - **하한선만 두고 상한선은 없다.** `requirements.txt`는 테스트된 lock으로 유지하고, `[project.dependencies]`는 공개 계약이 된다. lock의 정확한 버전을 발행하면 다른 패키지를 사용하는 모든 사용자와 충돌하기 때문이다. `<N+1` 상한선도 두지 않는다. 이는 주요 버전 지연이 발생하면 release gate를 실패시키는 `check-deps-fresh.sh`와 정면으로 모순된다. 하한선 조합으로 문제를 해결했으며, `openai==1.0.0`에 대한 반증 검사는 `ResolutionImpossible`로 종료된다. 이는 검사가 모든 것을 무조건 허용하는 것이 아니라 구분한다는 증거다. 또한 `pyproject.toml`의 버전이 CHANGELOG의 버전과 달라지는 것을 금지하는 보호 장치도 있다. PyPI는 같은 번호를 재사용할 수 없기 때문이다.

  - **새 venv에서 처음부터 끝까지 검증했다.** 약 70KB 크기의 wheel에는 `aipmt/*.py`, dist-info, 라이선스만 포함된다. `aipmt --help`는 22개 플래그와 함께 rc=0으로 종료되고, `python -m aipmt`는 “usage: aipmt”를 표시하며 “usage: \_\_main\_\_.py”를 표시하지 않는다. `pipx` 설치도 정상 작동했다. 무엇보다 **임의의 사용자 디렉터리에서 실제 fr→en 번역**을 수행했으며, 굵은 글씨, 목록, 인라인 코드, 링크와 URL은 보존되고 코드 블록은 번역되지 않았다. 마이그레이션 전 318개 테스트는 전후 식별자 목록이 바이트 단위로 완전히 동일한 상태에서 통과했다. 테스트가 무력화되지 않았음을 증명하는 것은 “OK”가 아니라 바로 이 사실이다. 여기에 3계층 설정 테스트 12개가 추가되어 총 330개가 되었다.

- **1.10.0** `--use_codex` provider (ChatGPT 구독 할당량), SDK와 모델 업데이트, 여러 문단으로 구성된 news 인용 수정 (2026-08-29):

  - **보안 검토 — PR이 추가했지만 모든 곳에서 유지하지 못한 두 가지 보호 장치:**

    - **Codex preflight가 전체 `.env`를 바이너리에 전달했다.** `_codex_preflight`는 **`env=` 없이** `subprocess.run`를 호출했다. 하위 프로세스는 전체 `os.environ`를 상속했으며, 따라서 `load_dotenv`가 로드한 `.env`의 모든 내용이 전달되었다. 계측된 가짜 바이너리로 측정한 결과 preflight에 **7개의 비밀**이 도달했다. 6개 provider의 키와 `GITHUB_TOKEN` 하나였다. 반면 대응 경로인 `_grok_preflight`는 `env=_grok_env()`를 올바르게 전달하여 **0개**였다. 이 불일치는 PR 내부에 존재했다. 몇 줄 떨어진 곳에 있는 `_strip_secret_env`는 바로 이 불변 조건을 유지하기 위해 존재한다. `_codex_env_base()`를 추출해 두 경로가 공유하도록 했으며, 수정 후 측정 결과 양쪽 모두 비밀은 0개였다.
    - **“`--deny` fail-closed” 속성이 사용된 형식을 포괄하지 못했다.** 주석은 알 수 없는 접두사의 규칙이 시작을 거부하기 때문에 Grok 격리가 완전하다고 설명했다. 그러나 `grok 1.0.13`에서 측정한 결과 이 검증은 **괄호 형식에만** 존재했다. `--deny 'CeciNestPasUnOutil(*)'`는 시작을 거부하지만(“unknown tool prefix”), `--deny 'CeciNestPasUnOutil'`는 조용히 허용된다. 그런데 `GROK_DENY_RULES`는 이름만 사용했다. 따라서 xAI 측에서 도구 이름을 바꾸면 유일하게 측정된 격리 계층이 아무 신호 없이 제거된다. 게다가 해당 환경에서는 OS sandbox도 이미 적용되지 않는다. 이름이 지정된 8개 규칙은 `Prefix(*)`로 통과하며, 각각 CLI에서 알려진 접두사인지 확인된다. catch-all `*`는 허용되는 유일한 리터럴 형식으로 그대로 남겨 두었다. 검증되지 않은 형식으로 되돌아가지 않도록 테스트가 방지한다.
    - **그 밖의 항목은 깨끗하게 검증되었다.** 명령 주입은 없었다(어디서나 목록 형식이며 `shell=True`는 사용하지 않고, 문서 내용은 stdin 또는 `--prompt-file`로 전달), 안전하지 않은 역직렬화도 없었다(`json.loads`만 사용하며 형식 검사 포함). 경로 순회 수정은 7개 페이로드에서 우회가 발견되지 않았고, `--deny '*'`도 CLI에 실제로 적용되었다(`DENY_ENFORCED`가 workdir 외부 읽기에서 관찰됨).
    - 앞서 추가한 최신성 검사도 자체 원칙을 우회하고 있었다. PyPI 요청이 실패한 패키지를 조용히 건너뛰어 gate가 통과했다. 이제 실제로 비교한 패키지 수를 세고, 적용 범위가 불완전하면 실패한다.

  - **의존성을 최신화하고 지연 재발을 막는 두 가지 방어 장치를 추가했다:**

    - **지연은 실제로 오래 지속되었다.** `openai`는 2.54에서 **3.6.0**으로, `anthropic`는 0.125에서 **1.2.0**으로, `certifi`는 2024.8.30에서 **2026.7.22**로 업데이트되었다. 이는 모든 provider 호출의 TLS를 검증하는 루트 인증서 저장소가 2년 동안 뒤처져 있었다는 뜻이다. 원인은 **`.github/dependabot.yml`가 없었다는 것**이다. 이 파일이 없으면 GitHub는 _security updates_만 활성화하고, Dependabot은 CVE의 영향을 받는 의존성에 대해서만 PR을 제안한다. 따라서 `urllib3`와 `idna`는 업데이트하면서도 두 SDK가 주요 버전 뒤처진 상태로 남아 있었던 것이다.
    - **두 주요 버전은 충돌 없이 공존한다.** 이전의 추론과 달리, `openai` 3.x와 `anthropic` 1.x는 **`httpx2`**로 이동하고, `mistralai`와 `google-genai`는 `httpx<1`에 남지만 서로 다른 배포판이다. 실제 설치로 확인한 뒤 **7개 provider 경로를 처음부터 끝까지 테스트**했다. OpenAI, Claude, Mistral, Gemini, Grok API, Codex CLI, Grok CLI가 모두 포함되며, 각 출력에서 인라인 코드와 링크도 보존되었다. “HTTP 스택 두 개를 피한다”는 선호 사항이었을 뿐 차단 조건은 아니며, 측정 결과가 결론을 내렸다.
    - **`requirements.txt`는 실제 환경을 설명하지 못했다.** `google-auth`, `cryptography`, `opentelemetry` 스택은 작업 venv에 설치되어 있었지만 선언된 적이 없었다. 따라서 새로 설치하면 실제 테스트 환경을 재현할 수 없었다. 반대로 `tokenizers`, `huggingface-hub`, `PyYAML`는 import되지도, 다른 어떤 항목에서 요구되지도 않았으며 `mistralai` 1.x의 잔재였다. 파일은 직접 의존성만으로 구축한 venv의 완전한 폐쇄 목록으로 재생성되었다. `pip-audit`는 새 구성에서 알려진 취약점을 보고하지 않는다.
    - **`.github/dependabot.yml`**(신규)은 주간 버전 업데이트, pip, github-actions 업데이트를 활성화한다. 마이너 버전과 수정 버전은 하나의 PR로 묶는다. PR마다 patch bump 하나만 올리면 결국 무시되고, 소음은 업데이트의 적이다. **주요 버전은 분리**하며, 각각 실제 호출을 통한 검증이 필요하다.
    - **`scripts/check-deps-fresh.sh`**(신규, gate에 연결됨)은 프로젝트 판정에서 지연을 드러낸다. Dependabot은 제안할 뿐 보장하지 않으며, PR이 누적될 수도 있다. 주요 버전 지연은 실패, 마이너 버전 지연은 경고로 처리한다. gate가 항상 빨간색이면 결국 무시되기 때문이다. PyPI에 연결할 수 없으면 로컬에서는 명시적으로 건너뛰고 **CI에서는 fail-closed**로 처리한다. 실행되지 않은 검사는 성공이 아니기 때문이다. 양방향으로 검증했다. 정확히 수정 전 상태(`openai 2.54.0→3.6.0`, `certifi 2024.8.30→2026.7.22`)를 잡아내며, 마이너 버전 지연에는 경고만 표시한다.

  - **이번 PR 검토에서 도출된 수정 사항** — 5명의 검토 에이전트가 diff를 철저히 검토했으며, 아래 항목은 모두 수정 전에 **측정으로 재현**되었다. 그중 두 개는 바로 이 버전에서 앞서 도입된 회귀였다.
- **수정된 회귀 — `_NEWS_CITATION_REGEX`에 지수적 백트래킹이 있었습니다.** 다중 문단 수정으로 반복문에 `(?:[ \t]*$|[ \t]+.*)`이 도입되었습니다. `[ \t]+`와 `.*` 사이의 공백 공유가 모호했고, 이 모호성이 반복될 때마다 증폭되었습니다. 패턴과 일치하지 않는 `>   texte` 줄 — 완전히 합법적인 Markdown 들여쓰기 — 에서 측정한 결과, **14줄에 2,589ms**가 걸렸지만 수정 후에는 0.04ms였으며, 줄을 하나 추가할 때마다 약 9배 증가했습니다. `--news` 모드에서는 길고 형식에 맞지 않는 blockquote 하나만으로도 작업 제한 시간이 초과될 때까지 번역이 멈췄고, 원인을 식별할 수 없었습니다. 이제 반복문은 줄 전체를 한 번에 소비하므로(`\n^>(?![ \t]*—).*`), 반복마다 일치하는 방법이 하나만 남습니다. 실제 231개 문서 코퍼스에서 확인한 결과, **캡처 차이는 0건**이었고 인용문 423개가 동일했으며, 다중 문단 본문 14개도 계속 확장되었습니다.
    - **두 provider 플래그를 동시에 지정해도 조용히 사용량 과금이 발생했습니다.** `--use_codex --use_mistral`는 허용되었고, `_select_provider_client`는 먼저 Mistral을 검사했으며, `_resolve_provider`은 명시적 불리언 값에 우선순위를 부여했지만 둘 다 Mistral로 수렴했습니다. 사용자는 구독 할당량을 요청했지만 사용량 과금이 발생했고, 경고는 전혀 없었습니다. 이는 바로 `--use_codex`이 방지하기 위해 존재하는 장애 방식입니다. 이제 여섯 provider 플래그는 모두 `add_mutually_exclusive_group`을 거칩니다. **동작 변경**: 지금까지 조용히 허용되던 두 provider를 함께 지정한 명령줄은 이제 `argument --use_mistral: not allowed with argument --use_codex`에서 실패합니다.
    - **검사가 실패했을 때도 작업 종료 게이트가 통과되었습니다.** `scripts/check-release-ready.sh`의 13개 검사 중 네 개가 반환 코드를 확인하지 않고 “stdout을 캡처한 뒤 비어 있으면 결론 내리는” 패턴을 따랐습니다. 예외(파일 이름 변경, `FileNotFoundError`)가 stderr에 기록되고 stdout은 비어 있으면 검사는 “보고할 내용 없음”으로 결론 내렸습니다. 이를 막기 위해 작성된 스크립트 안에서 “`exit 0` 하나만으로는 아무것도 증명하지 못한다”는 함정이 재현된 셈입니다. 이제 `probe()` 헬퍼가 0인 반환 코드와 종료 센티넬을 모두 요구하며, 검사는 기준 집합이 비어 있을 때 결론을 내리지 않습니다. 빈 집합에 대한 단언은 언제나 참이기 때문입니다. 시연 사례로, 위의 배타적 그룹을 추가하자 provider 플래그가 `*_group` 객체를 통과하게 되었고, 기존 정규식 `parser\.add_argument\(`은 더 이상 일치하지 않았습니다. **21개 중 6개 플래그**가 조용히 검사 범위에서 빠졌고 게이트는 통과했습니다.
    - **시크릿 스캔이 6개 provider 중 4개를 놓쳤습니다.** `[A-Za-z0-9]` 클래스는 하이픈을 제외합니다. 현재 OpenAI 형식인 `sk-proj-…`과 `sk-ant-api03-…`은 두 번째 하이픈에서 실패했고, `AIza…`는 검사 대상에 포함되지 않았습니다. 패턴을 확장하고 `.secrets.baseline`은 스캔에서 제외했습니다. 또한 `.env` 가드는 인덱스만 확인하는 `git diff --cached`를 조회하고 있었습니다. **이미 커밋된** 최악의 경우인 `.env`은 여기에 나타나지 않았습니다. 이제 `git ls-files`를 조회합니다.
    - **Codex의 “토큰 워밍업”은 실제 워밍업이 아니었습니다.** 측정 결과 `codex login status`는 `~/.codex/auth.json`에 접근하지 않았고(mtime과 크기도 변하지 않음), 도움말에는 “로그인 상태 표시”라고 적혀 있었습니다. 그러나 주석은 순환 토큰의 동시 refresh 위험을 무력화하기 위해 토큰을 “한 번, 순차적으로” 갱신한다고 주장했습니다. 명시된 보호 기능은 존재하지 않았으며, 이제 주석은 코드가 실제로 하는 일을 설명합니다. 진정한 대응책은 여전히 `max_jobs=4`입니다. 또한 검사는 지금까지 무시하던 `CODEX_BIN`를 준수합니다. `codex`가 `PATH`에 없는 환경에서는 “인증되지 않음”으로 실패했는데, 이는 오해를 부르는 진단이었습니다.
    - **`.env`이 서브셸에서 source 처리되었습니다.** `detect_provider`는 명령 치환으로 호출되므로 export가 상위 셸로 전달되지 않았습니다. 따라서 `GROK_BIN`, `GROK_HOME` 또는 `REGEN_MODEL`가 `.env`에서 정의되어도 `main()`에서 수행하는 읽기에는 보이지 않았고, 올바른 구성에서도 “Grok 바이너리를 찾을 수 없음”으로 결론 내렸습니다.
    - **동시성이 공지된 상한을 50% 초과했습니다.** 가드가 README/CHANGELOG 쌍을 시작한 뒤에 배치되어, 측정된 최고치는 **`max_jobs=2` 3개**였습니다. 주간 할당량을 Chat/Imagine/Voice와 공유하며 측정할 수 없는 Grok에서는 스크립트가 스스로 정한 상한을 지키지 못한 것입니다. 최종 개수는 표시되었지만 28과 비교되지 않아 파일 하나가 없어도 알아차릴 수 없었습니다.
    - **Grok 출력 계약: 이제 `stopReason`이 없으면 실패합니다.** 코드가 계약에서 요구하는 `end_turn` 대신 “`end_turn` **또는 없음**”을 적용하고 있었습니다. 필드가 없는 payload나 CLI 업데이트로 필드 이름이 바뀐 payload는 가드를 조용한 no-op으로 만들었습니다. 또한 `max_turn_requests`은 더 이상 rate limit으로 분류되지 않습니다. 소진된 것은 turn 예산이므로 재시도해도 결과가 같고 90초 대기만 발생합니다. `quota`은 이미 `_codex_is_rate_limited`의 docstring이 설명하고 있었지만 Grok에는 적용되지 않던 이유로 rate limit 마커에서 제외됩니다.
    - **Gemini cascade를 모델별로 메모이제이션했습니다.** 매 segment마다 `minimal`부터 다시 시작했지만 기본 모델은 이를 거부했습니다. 그 결과 정상 경로에서도 segment마다 400 왕복이 발생하고 같은 경고가 반복 출력되었습니다. 경고가 수백 번 반복되면 더 이상 읽히지 않으며, 그렇게 경고는 가면이 됩니다.
    - **기타**: CI의 거부 메시지가 Codex용으로 하드코딩되어 `--use_grok_cli` 사용자에게 `XAI_API_KEY` 대신 `OPENAI_API_KEY`을 안내했습니다. `provider.capitalize()`는 “Grok_cli”와 “Openai”를 표시했습니다. 하위 프로세스 기반의 주석은 두 CLI 모두를 “shim”으로 일반화했지만 Grok 바이너리는 네이티브 ELF입니다. 올바른 근거는 “자체 하위 프로세스를 spawn하는 agent”입니다. `subprocess`에 대한 SAST finding 12개는 `# nosec` / `# nosemgrep`로 사유와 함께 표시했습니다. `shell=True`이 없는 목록 형식에서는 injection이 불가능하고 문서 내용이 argv를 통해 전달되지 않기 때문입니다.
    - **이제 어떤 secret도 agent 하위 프로세스로 들어가지 않습니다.** 이름을 열거한 deny-list는 **과금** 불변식만 보호했습니다(Codex는 `OPENAI_API_KEY` 없이, Grok은 `XAI_API_KEY` 없이). 측정 결과 다른 **7개 secret**은 여전히 각 하위 프로세스로 들어가고 있었습니다. Anthropic, Mistral, Google, Gemini 키와 다른 CLI의 키, 그리고 secret은 아니지만 트래픽을 재지정하는 `OPENAI_BASE_URL`입니다. 이 두 CLI는 **agent**이며, Grok agent는 많은 Linux 시스템에서 적용 가능한 OS sandbox 없이 실행됩니다. 이제 필터링은 이름 목록이 아니라 **이름 패턴**(`API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIALS`)을 사용하므로, 코드가 알지 못하는 사용자의 `.env`에 추가된 변수도 포함합니다. CLI에는 이 변수들이 필요하지 않습니다. 인증은 `~/.codex`과 `~/.grok`에 존재하며 환경에는 절대 존재하지 않습니다. 환경을 강화한 상태에서 두 provider 각각을 통한 **실제 번역 성공**으로 이를 확인했습니다.
    - **테스트**: 새 파일 `tests/test_review_hardening.py`(테스트 21개)을 추가하여 provider 플래그의 배타성, `stopReason` 계약, news 정규식의 선형성, CI 거부 메시지, Gemini 메모이제이션, 하위 프로세스 환경에 secret이 없는지를 고정했습니다. 마지막 단언은 **일반적**이므로 어떤 목록에도 이름이 없는 키가 있으면 실패합니다. 기존 expurgation 테스트는 자신의 상수를 그대로 반영한 거울에 불과해 자체 루프의 고장 외에는 아무것도 감지할 수 없었습니다. 전체 테스트는 **311개**입니다.

  - **새로운 Grok provider 두 개**: `--use_grok`(xAI API, 키 `XAI_API_KEY`, 사용량 과금)와 `--use_grok_cli`(공식 Grok Build CLI, Grok 구독에서 차감 — `--use_codex`과 같은 원리).
    - **API 모드, 약 40줄**: xAI endpoint가 OpenAI와 호환되므로 client와 `_call_openai`을 그대로 재사용하고 `base_url`만 변경합니다. 필요한 조정은 하나뿐이었으며 모두에게 이점이 있습니다. `finish_reason`이 이제 OpenAI가 출력하는 `stop` 대신 xAI가 출력하는 형식인 `end_turn`도 허용합니다. 모델은 `grok-4.6`(품질)과 `grok-4.3`(경제형)입니다. 참고로 Grok의 경제형은 저장소에서 여전히 가장 비쌉니다. 백만 토큰당 $1.25/$2.50인 반면 `mistral-small-latest`은 $0.15/$0.60입니다. 이 provider는 가격이 아니라 모델 다양성을 위해 선택합니다.
    - **CLI 모드**: Codex를 기반으로 하되 실제 환경에서 요구된 네 가지 차이가 있습니다. prompt는 파일로 전달되고(`--prompt-file`, CLI가 stdin을 읽지 않으며 argv에 segment를 넣으면 `ps`에서 보임), 출력은 stdout의 단일 JSON 객체입니다(JSONL도 아니고 `-o` 파일도 아님). 구독에서는 `grok-4.6`와 `grok-4.5`만 노출되며 sandbox는 적용할 수 없습니다(아래 참조). 하위 프로세스 실행은 `_codex_run_process`에서 Codex와 공통화했으며, 이미 테스트된 Codex provider의 나머지는 건드리지 않았습니다.
    - **측정 결과 `exit 0`만으로는 아무것도 증명하지 못합니다**: 인증되지 않은 상태에서 CLI는 **stdout**에 `{"type":"error","message":"Not signed in."}`을 기록하고 반환 코드는 **0**입니다. 거부나 turn 초과도 같은 방식으로 동작합니다. 따라서 출력 계약은 네 조건을 동시에 요구합니다. 반환 코드 0, error payload 없음, `stopReason == end_turn`, 비어 있지 않은 텍스트입니다. 사전 점검도 같은 논리를 따릅니다. 연결이 끊겨도 `grok models`은 0으로 종료하므로 stdout에 “not authenticated”가 있어야만 결론을 내릴 수 있습니다.
    - **격리: 비대칭을 인정하고 문서화했습니다.** Codex가 `--sandbox read-only`에서 실행되는 반면, 최근 Linux 시스템 다수에서는 두 가지 독립적인 시스템 원인 때문에 Grok sandbox를 적용할 수 없습니다. `sudo` 없이는 우회할 수 없습니다. AppArmor는 Ubuntu 24.04부터 권한 없는 user namespace를 차단하며(`bwrap: setting up uid map: Permission denied`, Grok 외부에서도 재현됨), container runtime socket deny-list는 `/run/podman`가 `0700`일 때 실패합니다(resolver가 `ErrorKind::NotFound`만 복구하고 EACCES는 치명적이 됨). 핵심 함정은 **통합된** 프로필이 적용되지 못하면 **조용히 비격리 상태로 시작한다**는 것입니다. 따라서 스크립트는 기본적으로 어떤 프로필도 요청하지 않고 조용히 fallback하지 않습니다. stderr로 경고합니다. 보호는 CLI의 `--deny` 규칙에 의존하며 catch-all인 `*`도 포함합니다. 이는 측정된 유일한 _fail-closed_ 계층으로, 알 수 없는 prefix의 규칙이 시작을 거부하게 합니다. `GROK_TRANSLATE_SANDBOX=read-only`을 사용하면 이를 강제할 수 있으며, 시스템이 준수할 수 없으면 시작이 실패합니다.
    - **안전장치**: `XAI_API_KEY`, `GROK_API_KEY`, `GROK_SANDBOX`은 하위 프로세스 환경에서 제거됩니다(키가 있으면 사용량 과금으로 전환되고, 상속된 `GROK_SANDBOX`은 적용할 수 없는 프로필을 강제하여 오해를 부르는 메시지를 출력함). MCP/hooks/skills/agents 스위치 비활성화, `--disable-web-search`, `--no-subagents`, `--no-plan`, 일회용 workdir, CI 거부, 프로세스 그룹을 종료하는 timeout, rate limit에 대한 back-off를 적용합니다. `--max-turns`는 1이 아니라 6으로 설정합니다. 도구 작업 후에 카운터가 증가하므로 1이면 출력이 잘립니다.
    - **할당량**: Grok pool은 주간 단위이며 **Chat, Imagine, Voice와 공유**되고 이를 노출하는 명령은 없습니다. `account/rateLimits/read`으로 소비량을 산정할 수 있는 Codex와 다릅니다. 따라서 `regen_translations.sh`은 동시성을 2로 제한하고 명시적으로 경고합니다.
    - **테스트**: 새 파일 `tests/test_grok_provider.py`(테스트 24개)을 추가했습니다. 전체 테스트는 **290개**입니다.
  - **수정된 버그 — EN 다중 문단 인용문이 일부만 보호되었습니다(`--news` 모드)**: `_NEWS_CITATION_REGEX`은 인용문 본문으로 `>` 줄이 **연속해서** 이어지는 경우만 허용했습니다. 인용문이 여러 문단에 걸치면(빈 `>` 줄로 구분됨) 마지막 문단만 캡처되어 placeholder로 대체되고 앞부분은 LLM으로 전달되어 번역되어 돌아왔습니다. 이는 `--news`이 보장하려는 것과 정확히 반대입니다. 이제 반복문은 내부의 빈 `>` 줄을 허용하고 non-greedy가 되어, 처음 만나는 빈 줄이 아니라 기울임꼴 줄 앞의 `>` 빈 줄에서 멈춥니다.
    - **실제 측정 규모**: 실제 198개 문서 코퍼스에서 해당 인용문은 11개(총 419개 중)였습니다. 회귀는 없었습니다. 새 정규식은 정확히 같은 수의 인용문을 캡처하고 다중 문단 본문만 확장합니다(동일한 본문 408개, 확장된 본문 11개). 귀속 줄 `> — …`은 lookahead를 유지하므로 여전히 본문에 흡수되지 않습니다.
    - **end-to-end 증명**: 69KB 문서를 ja/ar로 번역한 결과, 이전에는 일본어에서 `> GLM-5.3がオープンウェイト化。`로 렌더링되고 아랍어에서도 같은 방식으로 번역되던 인용문의 첫 문단이 이제 `> GLM-5.3 is now open-weight.`로 유지됩니다. 영어 인용 줄 수는 9줄에서 10줄로 돌아가 원문과 같아졌습니다.
    - 참고로 이 결함은 후속 validator가 인용문이 존재하는지만 확인하고 완전한지 검사하지 않았기 때문에 발견되지 않았습니다.
  - **기본 provider에서 측정된 비용 절감**: `_openai_extra_kwargs`는 모델명이 `gpt-5`로 시작하기만 하면 `reasoning_effort="medium"`을 전송했으며, `--eco`인 경우도 포함되었습니다. 10단어 문장 하나를 번역하도록 `gpt-5.4-mini`에서 측정한 결과, `medium`는 reasoning token 45개와 출력 token 65개를 사용했고 `none`는 0개와 14개를 사용했습니다. reasoning은 번역에 아무런 이점이 없으며 각 파일의 각 segment마다 비용이 발생했습니다. 기본값은 `--eco`에서 `none`이 되고 그 외에는 `medium`로 유지됩니다. CLI에서 명시적으로 전달한 값이 여전히 우선합니다. `--reasoning_effort`는 이제 `low`/`medium`/`high` 외에도 `none`과 `xhigh`을 허용합니다. 다만 모든 모델이 모두 허용하는 것은 아닙니다. 예를 들어 `minimal`는 `gpt-5.4-mini`에서 거부되며, 기존의 매개변수 없는 retry가 이 경우를 처리합니다.
  - **SDK 업데이트 및 Gemini 마이그레이션**: `google-generativeai`(2025-11-30 지원 종료, 저장소 보관됨)을 통합 SDK **`google-genai`**로 교체했습니다. `genai.Client(api_key=...)` 다음 `client.models.generate_content(model=, contents=, config=)`을 사용하고, 시스템 prompt는 segment에 이어 붙이는 대신 `system_instruction`로 전달합니다. `mistralai`는 **2.9.4**로 올렸습니다(import는 `from mistralai.client import Mistral`이 되며 기존 방식은 `ImportError`를 발생시킴. wheel에서 확인). `anthropic`는 **0.125.0**, `openai`은 **2.54.0**으로 올렸습니다. 두 버전은 `httpx2`로 전환하기 전 마지막 버전이며, venv에 두 HTTP 스택이 함께 존재하지 않도록 하기 위한 것입니다. 이에 따라 `httpx` 0.28.1과 `pydantic` 2.13.5도 사용할 수 있게 되었습니다.
  - **문서가 아니라 실제 테스트로 발견한 두 회귀**:
    - `anthropic` ≥ 1.0은 `max_tokens`이 10분을 초과할 것으로 예상되는 비스트리밍 호출(`ValueError: Streaming is required...`)을 client 측에서 거부합니다. 이 안전장치는 0.34.2에는 없었고 `max_tokens=32768`을 사용하는 모든 Claude 호출을 망가뜨렸습니다. 명시적인 `timeout`(`CLAUDE_TIMEOUT`, 기본값 900초)으로 수정하여, 완전한 응답만 사용하는 호출을 streaming으로 전환하지 않도록 했습니다.
    - `thinking_level="minimal"`은 Gemini 카탈로그 일부에서만 허용됩니다. `gemini-3.1-flash-lite`은 지원하지만 `gemini-3.7-flash`과 `gemini-3.1-pro-preview`은 400으로 거부합니다. 따라서 `_gemini_generate_with_fallback`을 적용했습니다. 이는 `minimal` → `low` → thinking_config 없음 순서의 cascade이며, 기존 OpenAI fallback과 같은 방식입니다. 최적화 매개변수 하나 때문에 번역이 실패해서는 안 됩니다.
  - **기본 모델 갱신**, 모두 실제 호출로 검증: OpenAI `gpt-5.5` → **`gpt-5.6-terra`**(28개 batch에서 −60%), `gpt-5.4-mini` → **`gpt-5.6-luna`**(−73%); Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**(더 저렴하고 최신), `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**(날짜가 없는 canonical ID); Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**, `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**(안정 버전이며 `3.5-flash-lite`보다 저렴).
Mistral은 변경되지 않았으며, 네 모델 중 `mistral-large-latest`이 여전히 가성비가 가장 좋다. 참고로 `gemini-3.1-pro-preview`보다 최신인 Pro 등급의 Gemini 모델은 존재하지 않는다. 2026년 5월에 발표된 Gemini 3.5 Pro는 출시된 적이 없으며, 3.5/3.6/3.7 라인은 Flash 전용이다.
  - **Gemini로 전환하기 전 측정한 A/B 테스트**: `README.md`을 `gemini-3.1-pro-preview`로 일본어로 번역한 뒤 `gemini-3.7-flash`으로 번역했다. 구조는 완전히 동일했다(목록 21개, 코드 블록 18개, HTML 링크 13개, 이미지 13개, 모든 URL 보존). 소요 시간은 **48초가 아닌 8초**였다. 이 두 모델을 번역이나 비라틴 스크립트에 비교한 공개 벤치마크가 없었으므로, 테스트하지 않았다면 전환은 단순한 추정에 근거했을 것이다.
  - **Claude 응답 블록 필터링**: `_call_claude`은 유형을 필터링하지 않고 `block.text for block in response.content`을 수행했다. 적응형 추론 모델(Sonnet 5 이상)은 `thinking` 블록을 삽입하는데, 이 블록은 `.text`이 아니라 `.thinking`를 노출한다. 그 결과 첫 번째 세그먼트에서 번역이 불투명한 `AttributeError`에 걸려 중단될 수 있었다. 이제 `thinking`, `redacted_thinking`, `tool_use` 및 `tool_result`은 제외된다(알 수 없는 유형이 텍스트를 포함하더라도 허용하기 위한 음의 목록). 텍스트 블록이 전혀 없는 응답은 명시적인 오류를 발생시킨다. `thinking={"type": "disabled"}`은 모든 호출에 전달된다.
  - **`MODEL_TOKEN_LIMITS` 재동기화**: 철회일이 지난 모델을 제거했다(`magistral-*` 제품군은 2026-07-31, `gemini-2.0-*`는 2026-06-01, `gemini-3-pro-preview`는 2026-03-09에 철회되었으며, `claude-3-5-sonnet-20240620`, `claude-3-7-sonnet-20250219`, `claude-opus-4-1-20250805`, `claude-sonnet-4-20250514`도 제거). 제한값도 수정했다. Mistral 128K → **256K**(Large 3 / Small 4 세대), Gemini 1 000 000 → **1 048 576**(실제 입력 제한), `claude-opus-4-5` 200K → **1M**, `gpt-5.6-*` 제품군 400K → **1.05M**. Claude 5(`claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`), `claude-opus-4-8`, Gemini 3.5/3.6/3.7, `mistral-medium-latest` 및 `ministral-*` 제품군을 추가했다. 참고로 이 제한값은 여전히 참고용이며, `translate()`이 세그먼트 분할을 `min(16000, limite)`로 제한한다.

  - **Provider `--use_codex`**: 공식 Codex CLI(`codex exec`)를 비대화형 모드로 실행하는 다섯 번째 provider다. 사용량에 따라 과금되는 API를 호출하는 대신, 이미 결제한 ChatGPT 구독의 할당량에서 번역 사용량이 차감된다. 이 사용 방식에 대해 OpenAI가 문서화한 유일한 경로다. 요금제별 가용성 표에는 Plus/Pro/Business/Enterprise에서 « Codex SDK, `codex exec`, and scriptable workflows »를 사용할 수 있다고 명시되어 있다. 반면 `~/.codex/auth.json`의 토큰은 Platform API 호출을 인증하지 않으며, 이 스크립트도 해당 토큰을 절대 읽지 않는다. 인증과 갱신은 계속 CLI가 관리한다.
  - **npm뿐 아니라 pip로도 설치 가능한 Codex 바이너리**: `_resolve_codex_binary()`는 먼저 `CODEX_BIN`에서 바이너리를 찾고, 그다음 `PATH`을 찾은 뒤, OpenAI가 배포한 공식 Python 패키지 **`openai-codex-cli-bin`**을 찾는다(이는 `openai-codex` SDK의 의존성이다). 따라서 이제 Python 프로젝트에서 `--use_codex`을 사용하기 위해 전역 npm 설치를 할 필요가 없다. 이 패키지는 `requirements.txt`에 추가하지 않는다. 바이너리 크기가 약 250MB이므로 선택적 provider를 위해 모든 사용자에게 설치를 강제하게 되기 때문이다. 전체 흐름을 검증했다. `PATH`에 `codex`가 없는 상태에서 해석기가 패키지 바이너리를 찾아 완전한 번역을 6초 만에 완료했다.
  - **« 구독 모드 » 보장**: `OPENAI_API_KEY` 및 `CODEX_API_KEY`는 하위 프로세스 환경에서 제거된다. 이 보호 장치가 없으면 `.env`에 키가 존재할 때 아무런 가시적 신호 없이 Codex가 사용량 기반 과금으로 전환될 수 있다. 바로 이 provider가 방지하려는 상황이다.
  - **CLI의 함정을 테스트로 고정**:
    - `codex exec`는 프롬프트를 인수로 전달한 경우에도 **반드시** stdin을 읽는다. stdin을 닫지 않으면 모델을 호출하지 않은 채 명령이 타임아웃까지 대기한다(재현 결과: 180초 후 종료 코드 124, 0바이트). 따라서 `communicate(input=...)`은 필수다.
    - npm으로 설치되는 `codex`는 실제 Rust 바이너리를 `spawn`하는 Node shim이다. Rust 바이너리는 Python 프로세스의 **손자 프로세스**이므로 `subprocess.run(timeout=)`의 `SIGKILL` 이후에도 계속 실행되어 할당량을 소비할 수 있다. 그래서 `Popen(start_new_session=True)` + `os.killpg`이 필요하다.
    - CLI는 `turn.failed`를 출력하면서도 종료 코드 0을 반환할 수 있다. 따라서 JSONL 출력(`--json`)을 반환 코드와 함께 검사하며, 종료 코드가 0인데 `-o` 파일이 없으면 빈 세그먼트를 생성하는 대신 명시적인 오류를 발생시킨다.
  - **속도 제한 시 백오프**: CLI에는 내부 재시도 기능이 없다(`max_retries = 0`). 분류는 문자열 일부가 아니라 JSON 페이로드 구조(`status: 429` / `error.type`)를 기준으로 한다. « quota »라는 단어가 복구 가능한 429 오류와 복구 불가능한 `insufficient_quota` 모두에 나타날 수 있기 때문이다.
  - **CI 보호 장치**: `--use_codex`는 `CI` 또는 `GITHUB_ACTIONS`가 정의되어 있으면 거부된다. 공유 runner에서는 구독 인증을 사용할 수 없으며, OpenAI도 공개 저장소에서 이 워크플로를 사용하지 말라고 명시적으로 권고한다.
  - **모델**: `gpt-5.6-sol`(품질) 및 `gpt-5.6-luna`(`--eco`). `gpt-5.6-*` 제품군은 CLI와 Platform API에서 공통으로 사용되지만, ChatGPT 계정이 모든 모델에 접근할 수 있는 것은 아니다. 허용 목록은 로컬 검증 없이 서버 측에서 적용되며, 일반적이지 않은 모델을 사용하면 경고가 발생한다. Plus 요금제에서 Luna는 5시간 창당 250~2,000개의 메시지를 제공하는 반면 Sol은 10~100개를 제공한다. 따라서 일괄 처리에는 `--eco`이 권장 모드다.
  - **수정된 버그 — 완전히 성공했는데도 `regen_translations.sh`가 오류로 종료됨**: `trap ... EXIT`는 더 이상 존재하지 않는 `main()`의 `local` 변수인 `failed_log`을 참조하고 있었다. `set -u`에서 이로 인해 `failed_log: unbound variable`가 발생해 28개의 번역이 올바른데도 스크립트가 종료 코드 1로 끝났다. 그 결과 재생성 직후 가장 비용이 큰 단계에서 `release.sh --auto`(`set -e`)이 중단될 수 있었다. 변수를 전역으로 만들고 trap에서 변수의 존재 여부를 확인하도록 수정했다. 유용한 부수 효과로, 이전에는 이 오류에 가려졌던 실제 번역 실패가 종료 요약에 다시 표시된다.
  - **`REGEN_MODEL`**: provider의 기본값을 덮어쓰고 특정 모델을 강제하는 `regen_translations.sh`의 새 환경 변수다. 예를 들어 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`을 사용하면 물량 처리에 맞춰진 `--eco` 대신 구독 할당량에서 고급 모델로 재생성할 수 있다.
  - **`regen_translations.sh`**: 명시적인 opt-in으로 `REGEN_PROVIDER=codex`을 사용할 수 있다(사용자 모르게 구독 할당량을 소비하지 않도록 자동 감지는 하지 않음). Codex 갱신 토큰은 순환형이며 일회용이므로 병렬 작업이 `codex login` 세션을 무효화할 수 있다. 따라서 병렬 처리를 시작하기 전에 토큰을 순차적으로 한 번 갱신하고 동시성은 4로 낮춘다.
  - **관련 리팩터링**: `_dispatch_provider_call`의 매개변수 수를 8개에서 6개로 줄였다. 네 번째 불리언을 전체 호출 체인에 전달하는 대신 provider 이름을 반환하는 `_resolve_provider()`을 사용한다. 명시적인 불리언은 `args`보다 계속 우선하므로, 최소한의 `Namespace`로 `translate(..., use_mistral=True)`을 호출하는 테스트도 유지된다.
  - **테스트**: 새 파일 `tests/test_codex_provider.py`(테스트 48개)이 argv, 정리된 환경, 서문 방지 계약, 조용한 실패, timeout/killpg, 백오프, 사전 검사, provider 해석, Gemini 추론 cascade, Claude 블록 필터링 및 다중 단락 news 인용을 다룬다. 전체 테스트 수는 290개로 늘었다.
  - **실제 검증**: 프로젝트의 `README.md`를 Codex로 **14개 언어**로 번역한 결과, 기준 번역과 구조가 완전히 동일했다(코드 블록 14개, 제목 24개, 표 행 25개, HTML 링크 13개, 이미지 13개, URL 19개, 코드 블록은 문자 단위로 동일하며 placeholder 잔여물 0개). `--news` 모드에서 69KB 분량의 뉴스 기사를 처리했을 때 `gpt-5.6-luna`와 `gpt-5.6-sol` 출력 모두 en/ja/ar의 후속 애플리케이션 검증을 통과했다. `account/rateLimits/read`를 통해 사용량을 측정한 결과, `--eco` 모드에서 5시간 창 카운터의 반올림 기준인 0% 미만으로 유지되었다.

- **1.9.2** 중첩 괄호 또는 FR 접두사가 있는 news attribution URL 추출 수정 (2026-05-11):

  - **수정된 버그**: `_protect_news_quotes`의 attribution URL 추출은 `re.search(r"\((.+?)\)", attribution)` 정규식(괄호 사이를 lazy capture)으로 이루어졌다. `(relayé par [@user sur X](https://x.com/.../123))`와 같은 attribution(중첩 괄호: 바깥쪽 `(` + markdown link의 `]()`)에서는 첫 번째 `)`에서 캡처가 중단되어 문자열이 잘렸다. FR 접두사까지 포함된 결과는 `relayé par [@user sur X](https://x.com/.../123`이 되었으며, 마지막 `)`가 빠졌다. 그 결과 `_validate_news_post`가 번역 출력에서 이 문자열을 찾으려 했지만 항상 실패했다. 이유는 두 가지였다. `)`가 잘렸고, "relayé par"가 `relayed by`/`weitergeleitet von`/ 등으로 번역되었기 때문이다. low → medium → high → gpt-5.5 전체 cascade를 통과할 수 없었다.
  - **수정**: 정규식을 `re.search(r"\]\(([^)]+)\)", attribution)`로 변경했다. 이제 markdown link의 `](url)`만 구체적으로 대상으로 삼아 **순수 URL만** 캡처하며(FR 접두사와 잘림을 제외), 번역 중에는 `#URL{N}#` placeholder를 통해 불변성을 유지한다. 다음 두 가지 문제 패턴에도 견고하다.
    - `(relayé par [@account sur X](url))` — 중첩 괄호
    - `via [@source](url)` 또는 `selon [@author](url)` — 바깥 괄호가 없는 FR 접두사
  - **테스트**: `test_silent_failure.py`의 `TestNewsCitationExtraction` 클래스에 2개를 추가했다.
    - `test_extract_attribution_url_with_nested_parens` (Genspark CEO E2B 버그를 정확히 재현한 사례)
    - `test_extract_attribution_url_with_french_prefix` (`via`이 포함된 변형)
  - **커버리지 공백**: `check-editorial-coverage.py`은 편집 문법은 검증하지만 translator가 번역할 수 있는지는 검증하지 않는다. 가능한 개선안(v1.9.2 범위 외)은 게시 전에 위험한 패턴을 감지하도록 dry-run에서 attribution 추출을 시뮬레이션하는 검사다.

- **1.9.1** 번역 marker 노트의 CTA 레이블 i18n 수정 (2026-05-10):

  - **수정된 버그**: 번역된 파일 상단 marker 배너의 CTA 링크 레이블 `[Voir le projet sur GitHub ↗]`이 모든 대상 언어에서 `target_lang`을 따르지 않고 **프랑스어로 남아 있었다**. URL과 저장소 slug를 보존하기 위해 Python 쪽에서 조립되므로 LLM은 이를 보지 못하며, 번역 단계에서 수정할 수 없었다. v1.9에서 `marker` 형식을 추가한 이후 발생한 조용한 회귀였다.
  - **수정**: 15개 언어를 현지화된 레이블에 매핑하는 새 상수 `_VIEW_PROJECT_LABELS`를 추가했다. 이제 `_translation_note_invariants(target_lang)`와 `_assemble_translation_note_paragraphs(phrase, target_lang)`이 대상 언어를 전달한다. 알 수 없는 언어에서는 안전을 위해 KeyError가 발생하지 않도록 `fr`로 대체한다.
  - **테스트**: `test_source_emits_three_paragraphs_repo_title_description_link`을 수정했다(target_lang `ja` → 일본어 레이블을 예상). 새 테스트 2개도 추가했다. `test_source_link_label_localized_per_target_lang`(라틴, 표의문자, 아브자드 문자를 포함하는 7개 언어에 대해 매개변수화)와 `test_source_link_label_falls_back_to_french_for_unknown_target`이다. 전체 테스트 수는 `test_translation_note_position.py`에서 38개가 아닌 40개가 되었다.
  - **Backward-compat**: 기본값이 있는 `target_lang="fr"` 시그니처를 사용하므로, `args.target_lang` 없이 호출하는 외부 프로그래밍 호출자도 수정 없이 계속 작동한다.
- **1.9** 무음 실패 수정 + 완전한 품질 도구 + 다중 위치 번역 노트 (2026-05-07) :
  - **다중 위치 번역 노트 + "embed card" 형식 marker** :
    - 새로운 CLI 옵션 (추가 옵션, 기본값은 변경되지 않음 → **하위 호환**) :
      - `--note_position {top,bottom,both}` (기본값: `bottom`): 번역된 파일의 위쪽, 아래쪽 또는 양쪽에 노트를 배치합니다.
      - `--note_format {legacy,marker}` (기본값: `legacy`) :
        - `legacy`는 v1.8의 동작(굵은 단락 `**…**`)을 **byte-for-byte** 그대로 재현합니다.
        - `marker`은 보이지 않는 Markdown 링크 reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) 뒤에, "GitHub repo embed card"와 같은 렌더링을 위한 구조화된 **3개 단락 blockquote**를 출력합니다. 프로젝트 제목은 inline code (`**\`ai-powered-markdown-translator\`\*\*`), 설명은 LLM이 번역한 내용, CTA 링크는 표시되는 화살표와 함께 (`[Voir le projet sur GitHub ↗](URL)`)로 구성됩니다. remark 플러그인으로 빌드 시 활용할 수 있습니다 (jls42.org 블로그 → `remark-translation-banner` 플러그인).
    - **LLM에 절대 전송되지 않는 불변 요소**: 저장소 제목과 GitHub URL은 설명 문장 번역 후 Python 측에서 조립됩니다. LLM은 slug `ai-powered-markdown-translator`이나 `https://github.com/jls42/...`을 절대 보지 않으므로 renderer/case/scheme이 변경되지 않습니다.
    - **Frontmatter-aware 삽입**: `top` 또는 `both` 모드에서는 노트가 YAML frontmatter의 **닫는 `---` 블록 뒤에** 삽입됩니다 (Astro Content Collections / gray-matter 안전성). Helper `_split_frontmatter`는 파일 시작 부분의 `---\n…\n---\n`을 감지하고 무결성을 보존합니다. 닫는 fence 없이 열린 frontmatter에서는 **`RuntimeError`를 발생**시키며 (잘못된 위치에 노트를 넣은 채 작성하지 않고 파일은 `failed_files`으로 이동합니다).
    - **모델 sanitizer whitelist**: `_sanitize_model`은 `[A-Za-z0-9._:/-]`에 속하지 않는 모든 문자를 `_`으로 대체하며, 비어 있으면 `unknown`을 fallback으로 사용합니다. remark Astro 플러그인 측 validator와 일치하며 marker 형식을 깨뜨릴 수 있는 문자(공백, 따옴표, 괄호, 쉼표 등)를 무력화합니다.
    - **내부 리팩터링**: `_append_translation_note`(단일 거대 함수)을 7개의 순수 helper(`_translation_note_invariants`, `_build_translation_note_phrase`, `_assemble_translation_note_paragraphs`, `_build_translation_note_source`, `_sanitize_model`, `_quote_lines`, `_split_frontmatter`, `_build_translation_note_block`, `_compose_with_notes`)로 분리했습니다. Builder와 composer를 분리했으며 (builder는 구분자 없는 순수 블록을 반환하고 composer는 위치에 따라 `\n\n`을 적용), 운영 코드와 source helper는 동일한 3단락 조립기를 공유합니다.
    - **`_quote_lines` blank-preserving**: 각 줄 앞에 `> `를 붙이고, 빈 줄은 `>` 하나로 변환합니다. 이를 통해 mdast가 blockquote 안에서 줄바꿈이 있는 하나의 단락이 아니라 3개의 서로 다른 단락(제목 / 설명 / 링크)을 인식할 수 있습니다.
    - **`_build_translation_note_block` 적응형 처리**: LLM이 보존한 단락 수에 따라 동작합니다(3개 = 완전한 card 형식, 2개 = 문장 + 링크, 1개 = fallback). 1단락 fallback에서는 Markdown 링크 `](`가 감지될 때 더 이상 `**...**`로 감싸지 않습니다. 링크 주변의 `<strong>` 렌더링이 불안정하기 때문입니다.
    - **하위 호환성**: `_compose_with_notes` 측의 `getattr(args, "note_position", "bottom")` 및 `getattr(args, "note_format", "legacy")` — 이러한 속성이 없는 Namespace(기존 테스트, 외부의 프로그래밍 방식 호출)도 수정 없이 계속 작동합니다.
  - **긴 번역에서의 무음 실패 수정** :
    - 모든 provider(OpenAI, Mistral, Claude, Gemini)에 대한 번역 후 언어 검증: 결정론적 계층(소스에서 추출한 내용의 verbatim 재발견) + 확률론적 계층(`langdetect`)
    - `finish_reason` / `stop_reason` whitelist: whitelist에 없는 모든 상태(truncation, content_filter 등)에서 `RuntimeError` 발생
    - Claude의 `max_tokens`: `4096` → `32768` (16k 세그먼트의 잠재적 truncation과 FR→JA/ZH/KO/AR/HI 교차 스크립트 여유 부족 방지)
    - Heading-aware segmentation: 세그먼트 후반부에서 H2/H3에 우선순위를 부여(각 세그먼트가 완전한 의미 단위의 section으로 시작)
    - 오류를 non-zero exit code까지 전파: `translate_markdown_file`은 유형화된 상태 `success` / `failure` / `skipped`을 반환하고, 하나 이상의 파일이 실패하면 `main()` `sys.exit(1)` (단일 파일 및 batch)
    - 모든 provider에 empty-content guard, 소스/출력 sanity ratio(≥ 500자, < 5% = 거부), 코드 placeholder 검증(`#CODEBLOCK`/`#INLINECODE`), LLM 후 정규화(heading에 붙은 구분자/링크), `BadRequestError` retry를 `reasoning_effort` 없이 수행
    - `langdetect==1.0.9` 의존성 추가
  - **pre-commit 품질 도구** ("완전한 EurekAI 유형", 14개 hook) :
    - Pre-commit: ruff (lint+format), shellcheck, prettier (md/yaml/json), detect-secrets (보호된 API key 4개), Lizard (CCN ≤ 12), pre-commit-hooks v5 (whitespace, EOF, large-files, shebangs 등)
    - Pre-push: mypy (점진적 lax 모드), Opengrep SAST (translate.py + scripts/), pip-audit (초기 reporting 모드), unittest discover (tests/ + scripts/tests/)
    - `scripts/`의 로컬 wrapper는 `./venv/bin/python`을 사용합니다.
    - `scripts/audit_verdict.py`: 11개의 unittest로 pip-audit JSON parser를 테스트하며, jls42-astro parser를 Python으로 이식한 버전입니다.
    - 초기 ruff 위반 7건 수정: B904 (raise from) ×2, B007 (unused dirs), C408 (dict literal), C419 (list-comp), SIM105 (contextlib.suppress), SIM110 (any())
    - Lizard는 일시적으로 `translate.py`을 제외합니다(CCN 21-47인 함수 4개, 리팩터링 예정) — scripts/에는 엄격한 gate 적용
  - **SonarCloud + 철저한 커버리지** :
    - GitHub Actions workflow `SonarCloud` (sonarcloud.yml + sonar-project.properties): 모든 push와 pull-request에서 분석, `coverage.xml`을 통한 coverage
    - README 상단에 SonarCloud badge 11개 추가(Quality Gate, Security/Reliability/Maintainability ratings, Coverage, Vulnerabilities, Bugs, Code Smells, Duplicated Lines, Technical Debt, Lines of Code)
    - `tests/test_silent_failure.py` (`unittest` stdlib): silent-failure 오류 체인의 6개 연결 고리를 모두 테스트
    - `tests/test_orchestration.py` (+79 tests): `translate.py`의 orchestration 계층(`_resolve_*_filename`, `_existing_translation_exists`, `_record_translation_status`, `_write_output_file`, `translate_directory`, `_validate_input_paths`, `_init_*_client`, `_select_provider_client`, `_normalize_collapsed_markdown`, `_cleanup_source_flag`, `_validate_news_flags_*`, `_openai_create_with_fallback` TypeError + BadRequestError fallbacks, o1-series prompt format, `_validate_translation_output`의 early-return branch)을 테스트
    - `scripts/tests/test_audit_verdict.py`: `main()`(stdin/stdout)와 subprocess를 통한 `if __name__ == "__main__"` 블록을 테스트
    - **새 코드의 Coverage**: 75.5% → 약 98%(translate.py 98%, scripts/audit_verdict.py 97%)
  - **테스트**: `tests/test_translation_note_position.py`는 position × format 매트릭스(`marker+top|bottom|both` 및 `legacy+top|bottom|both` E2E 포함), 다중 줄 prefix 처리, byte-for-byte 하위 호환(golden literal), sanitizer, frontmatter 분리(닫히지 않은 fence에서의 raise 포함), 3단락 형식, 2단락 fallback, Markdown 링크가 있는 1단락 guard, 그리고 제목+URL이 LLM에 절대 전송되지 않음을 검증하는 핵심 안전장치 `TestLLMPayloadExcludesInvariants`을 테스트합니다. **테스트 190개 통과**, regression 0건.
  - 문서: badge가 포함된 `README.md`(FR + 14개 번역), `CLAUDE.md`(pre-commit workflow + 상세한 CI watch), 번역 28개 재생성
- **1.8** `--news` 모드 + 2026 모델 업데이트 (2026-03-17, tag `v1.8`) :
  - 기본 모델 업데이트(2026년 3월) :
    - OpenAI 품질: `gpt-5` → `gpt-5.4`
    - OpenAI 경제형: `gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 품질: `gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.4-nano`(400k) 및 `gemini-3.1-pro-preview`(1M)의 token limit 추가
  - 초기 `--news` 모드: `#NEWSQUOTE\d+#` placeholder를 사용한 EN 인용 보호, `LANG_FLAGS` 매핑(15개 언어), 대상 언어별 flag 처리
  - 복원 전 news placeholder 검증(회귀 수정: placeholder를 삭제한 LLM이 인용 없는 출력을 조용히 생성하던 문제)
  - `regen_translations.sh` script를 portable하게 변경(절대 경로, pwd 의존성 제거)
  - README/CHANGELOG language bar에 Français 링크 추가, 번역 28개 재생성
- **1.7** 새로운 기능 :
  - 번역 시 원본 파일명을 유지하는 `--keep_filename` 옵션
  - API key를 자동으로 불러오는 `.env` 파일 지원
  - **inline code 보존**: backtick(`` `...` ``)을 이제 번역 중 보호
  - 시스템 prompt 개선 :
    - YAML frontmatter의 따옴표 처리 개선
    - template 변수 `{variable}` 보호
    - 요청하지 않은 번역자 노트 금지
  - 364개 파일(jls42.org blog migration)에서 성공적으로 테스트
- **1.6** 새로운 기능 :
  - 번역을 위한 Google Gemini API 지원 추가(`--use_gemini`)
  - 2026년 기본 모델 업데이트 :
    - OpenAI: `gpt-5`(품질), `gpt-5-mini`(경제형)
    - Claude: `claude-sonnet-4-5`(품질), `claude-haiku-4-5`(경제형)
    - Gemini: `gemini-3-pro-preview`(품질), `gemini-3-flash-preview`(경제형)
  - 더 빠르고 저렴한 모델을 사용하는 경제형 모드(`--eco`)
  - 디렉터리를 순회하지 않는 단일 파일 번역(`--file`)
  - 단순화된 새로운 이름 지정 pattern: `{base}-{lang}.md`
  - 모델명을 포함한 기존 형식을 유지하는 `--include_model` 옵션
  - 기본 token limit(128k)이 적용된 목록에 없는 모델 지원
  - README를 14개 언어로 번역
- **1.5** 개선 사항 :
  - **API key 및 기본 모델 업데이트:**
    - **OpenAI:** `DEFAULT_MODEL_OPENAI`에서 `"gpt-4o"`으로 업데이트
    - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`에서 `"mistral-large-latest"`으로 업데이트
    - **Anthropic Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`에서 `"claude-3-5-sonnet-20240620"`으로 업데이트
  - **번역 prompt 최적화:**
    - 직접 번역과 번역 노트를 위한 prompt를 더 명확하고 효율적으로 개선했으며, metadata와 특정 formatting 요소의 보존에 관한 상세한 지침을 포함했습니다.
  - **코드 리팩터링:**
    - Mistral AI client 초기화를 위해 `MistralClient`을 `Mistral` 클래스로 교체
    - 가독성과 유지 관리성을 높이기 위한 import 재구성
    - 번역 중 원본 formatting을 보존하도록 텍스트 segmentation과 code block 처리 개선
  - **출력 파일 관리:**
    - 출력 파일명에서 model과 language의 순서를 반대로 변경(예: `f"{base}-{args.target_lang}-{args.model}.md"`)하여 번역을 더 쉽게 정리하고 검색할 수 있도록 개선
  - **기타 개선 사항:**
    - 불필요한 빈 줄 제거로 코드 정리
    - script 구조와 가독성을 개선하기 위한 사소한 조정
- **1.4** 새로운 기능 :
  - 번역을 위한 Anthropic Claude API 지원
  - 명확성과 효율성을 높이기 위한 prompt 최적화
  - 코드 유지 관리성을 개선하기 위한 사소한 조정
- **1.3** 개선 사항 및 새로운 기능 :
  - code block 처리 개선
  - 출력 파일 처리 개선
  - 기존 파일 감지 개선
  - 번역을 강제하는 `--force` 옵션
  - 출력 파일명에서 model과 language 순서 반전
- **1.2** changelog 수정
- **1.1** Mistral IA API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**gpt-5.6-luna로 프랑스어에서 한국어로 번역된 기사.**
