### 변경 내역

- **1.0** 초기 버전 - OpenAI API 지원
- **1.1** Mistral IA API 지원 추가
- **1.2** 변경 내역 수정
- **1.3** 개선 사항 및 새로운 기능:
    - 코드 블록 관리 개선
    - 출력 파일 관리 개선
    - 기존 파일 탐지 기능 개선
    - 번역 강제를 위한 `--force` 옵션
    - 출력 파일 이름에서 모델과 언어의 위치 반전
- **1.4** 새로운 사항:
    - 번역을 위한 Anthropic의 Claude API 지원
    - 명확성 및 효율성을 높이기 위한 프롬프트 최적화
    - 코드 유지보수를 위한 소규모 조정
- **1.5** 개선 사항:
    - **기본 API 키 및 모델 업데이트:** 
        - **OpenAI:** `DEFAULT_MODEL_OPENAI`를 `"gpt-4o"`로 업데이트.
        - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`을 `"mistral-large-latest"`로 업데이트.
        - **Anthropic의 Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`를 `"claude-3-5-sonnet-20240620"`로 업데이트.
    - **번역 프롬프트 최적화:**
        - 직접 번역 및 번역 노트를 위한 프롬프트가 명확성과 효율성 향상을 위해 개선되었으며, 메타데이터 및 특정 형식 요소의 보존에 대한 상세한 지침이 포함됨.
    - **코드 리팩토링:**
        - `MistralClient`를 Mistral AI 클라이언트 초기화를 위한 `Mistral` 클래스로 교체.
        - 가독성과 유지보수를 위해 임포트 정리.
        - 원본 형식을 유지하면서 번역할 수 있도록 텍스트 분할 및 코드 블록 관리 개선.
    - **출력 파일 관리:**
        - 출력 파일 이름에서 모델과 언어의 위치 반전 (예: `f"{base}-{args.target_lang}-{args.model}.md"`), 번역 관리 및 검색 용이.
    - **다양한 개선 사항:**
        - 불필요한 빈 줄 제거.
        - 스크립트의 구조와 가독성 향상을 위한 소규모 조정.

**이 문서는 버전 fr에서 ko 언어로 gpt-4o 모델을 사용하여 번역되었습니다. 번역 프로세스에 대한 자세한 내용은 https://gitlab.com/jls42/ai-powered-markdown-translator을 참조하십시오.**

