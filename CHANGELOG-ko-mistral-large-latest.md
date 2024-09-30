### Changelog

- **1.0** 초기 버전 - OpenAI API 지원
- **1.1** Mistral AI API 지원 추가
- **1.2** 변경 로그 수정
- **1.3** 개선 및 새로운 기능:
    - 코드 블록 관리 개선
    - 출력 파일 관리 개선
    - 기존 파일 감지 개선
    - `--force` 옵션을 통한 강제 번역
    - 출력 파일 이름에서 모델과 언어 순서 변경
- **1.4** 새로운 기능:
    - Anthropic의 Claude API 번역 지원
    - 프롬프트 최적화를 통한 명확성 및 효율성 향상
    - 코드 유지보수를 위한 소소한 조정
- **1.5** 개선 사항:
    - **기본 API 키 및 모델 업데이트:**
        - **OpenAI:** `DEFAULT_MODEL_OPENAI`를 `"gpt-4o"`로 업데이트.
        - **Mistral AI:** `DEFAULT_MODEL_MISTRAL`을 `"mistral-large-latest"`로 업데이트.
        - **Anthropic의 Claude:** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE`를 `"claude-3-5-sonnet-20240620"`로 업데이트.
    - **번역 프롬프트 최적화:**
        - 직접 번역 및 번역 참고 사항을 위한 프롬프트가 명확성 및 효율성을 높이기 위해 강화되었으며, 메타데이터 및 특정 포맷팅 요소 보존에 대한 자세한 지침이 포함되었습니다.
    - **코드 리팩토링:**
        - `MistralClient`를 `Mistral` 클래스로 교체하여 Mistral AI 클라이언트 초기화.
        - 가독성 및 유지보수를 위한 임포트 재정리.
        - 번역 시 원래 포맷팅을 보존하기 위한 텍스트 세분화 및 코드 블록 관리 개선.
    - **출력 파일 관리:**
        - 출력 파일 이름에서 모델과 언어 순서 변경(예: `f"{base}-{args.target_lang}-{args.model}.md"`), 이를 통해 번역 정리 및 검색이 용이해짐.
    - **기타 개선 사항:**
        - 불필요한 빈 줄 제거를 통한 코드 정리.
        - 스크립트의 구조와 가독성을 향상시키기 위한 소소한 조정.

**Ce document a été traduit de la version fr vers la langue ko en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator.**

