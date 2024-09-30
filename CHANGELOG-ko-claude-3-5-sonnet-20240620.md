### 변경 로그

- **1.0** 초기 버전 - OpenAI API 지원
- **1.1** Mistral AI API 지원 추가
- **1.2** 변경 로그 수정
- **1.3** 개선 및 새로운 기능:
    - 코드 블록 처리 개선
    - 출력 파일 처리 개선
    - 기존 파일 감지 개선
    - 번역을 강제하는 `--force` 옵션
    - 출력 파일 이름에서 모델과 언어 순서 반전
- **1.4** 새로운 기능:
    - 번역을 위한 Anthropic의 Claude API 지원
    - 명확성과 효율성을 높이기 위한 프롬프트 최적화
    - 코드 유지보수 개선을 위한 minor 조정
- **1.5** 개선 사항:
    - **API 키 및 기본 모델 업데이트:**
        - **OpenAI:** `DEFAULT_MODEL_OPENAI`를 `"gpt-4o"`로 업데이트.
        - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`을 `"mistral-large-latest"`로 업데이트.
        - **Claude d'Anthropic:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`를 `"claude-3-5-sonnet-20240620"`으로 업데이트.
    - **번역 프롬프트 최적화:**
        - 직접 번역 및 번역 노트를 위한 프롬프트가 메타데이터 및 특정 포맷팅 요소 보존에 대한 상세 지침을 포함하여 더 나은 명확성과 효율성을 위해 보강되었습니다.
    - **코드 리팩토링:**
        - Mistral AI 클라이언트 초기화를 위해 `MistralClient`를 `Mistral` 클래스로 대체.
        - 가독성과 유지보수를 위한 import 재구성.
        - 번역 시 원본 포맷팅을 보존하기 위한 텍스트 세그먼테이션 및 코드 블록 처리 개선.
    - **출력 파일 관리:**
        - 출력 파일 이름에서 모델과 언어 순서 반전 (예: `f"{base}-{args.target_lang}-{args.model}.md"`), 번역본의 조직과 검색을 용이하게 함.
    - **기타 개선 사항:**
        - 불필요한 빈 줄 제거로 코드 정리.
        - 스크립트의 구조와 가독성을 개선하기 위한 minor 조정.

**이 문서는 claude-3-5-sonnet-20240620 모델을 사용하여 fr 버전에서 ko 언어로 번역되었습니다. 번역 과정에 대한 자세한 정보는 https://gitlab.com/jls42/ai-powered-markdown-translator 를 참조하십시오.**

