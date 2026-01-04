### 변경 로그

🌍 [영어](CHANGELOG-en.md) | [스페인어](CHANGELOG-es.md) | [중국어](CHANGELOG-zh.md) | [독일어](CHANGELOG-de.md) | [일본어](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [아랍어](CHANGELOG-ar.md) | [힌디어](CHANGELOG-hi.md) | [이탈리아어](CHANGELOG-it.md) | [네덜란드어](CHANGELOG-nl.md) | [폴란드어](CHANGELOG-pl.md) | [포르투갈어](CHANGELOG-pt.md) | [루마니아어](CHANGELOG-ro.md) | [스웨덴어](CHANGELOG-sv.md)

- **1.7** 새로운 기능 :
    - 파일 이름을 번역 시 원본으로 유지하는 옵션 `--keep_filename`
    - API 키를 자동으로 로드하기 위한 파일 `.env` 지원
    - **인라인 코드 보존** : 백틱(`` `...` ``)이 이제 번역 중에 보호됩니다
    - 시스템 프롬프트 개선 :
        - YAML 프론트매터의 따옴표 처리 개선
        - 템플릿 변수 `{variable}` 보호
        - 요청되지 않은 번역자 메모 금지
    - 364개 파일에서 성공적으로 테스트됨 (블로그 jls42.org 마이그레이션)
- **1.6** 새로운 기능 :
    - 번역을 위한 Google Gemini API 지원 (`--use_gemini`)
    - 2026 기본 모델 업데이트 :
        - OpenAI : `gpt-5` (고품질), `gpt-5-mini` (저비용)
        - Claude : `claude-sonnet-4-5` (고품질), `claude-haiku-4-5` (저비용)
        - Gemini : `gemini-3-pro-preview` (고품질), `gemini-3-flash-preview` (저비용)
    - 더 빠르고 비용 효율적인 모델을 사용하기 위한 절약 모드 (`--eco`)
    - 디렉토리를 탐색하지 않고 단일 파일을 번역하는 기능 (`--file`)
    - 새로운 단순화된 명명 패턴 : `{base}-{lang}.md`
    - 모델 이름이 포함된 이전 형식을 유지하기 위한 옵션 `--include_model`
    - 기본 토큰 제한(128k)으로 나열되지 않은 모델 지원
    - README가 14개 언어로 번역됨
- **1.5** 개선 사항 :
    - **API 키 및 기본 모델 업데이트 :**
        - **OpenAI :** `DEFAULT_MODEL_OPENAI` 에서 `"gpt-4o"` 로 업데이트.
        - **Mistral AI :** `DEFAULT_MODEL_MISTRAL` 에서 `"mistral-large-latest"` 로 업데이트.
        - **Anthropic의 Claude :** `DEFAULT_ANTHROPIC_API_KEY` 추가 및 `DEFAULT_MODEL_CLAUDE` 에서 `"claude-3-5-sonnet-20240620"` 로 업데이트.
    - **번역 프롬프트 최적화 :**
        - 직접 번역 및 번역 메모용 프롬프트가 명확성과 효율성을 위해 강화되었으며, 메타데이터 및 특정 서식 요소 보존에 대한 자세한 지침을 포함합니다.
    - **코드 리팩터링 :**
        - Mistral AI 클라이언트 초기화를 위해 `MistralClient`를 `Mistral` 클래스로 교체함.
        - 가독성 및 유지 관리를 위한 임포트 재구성.
        - 번역 시 원래 서식을 보존하기 위한 텍스트 분할 및 코드 블록 관리 개선.
    - **출력 파일 관리 :**
        - 출력 파일 이름에서 모델과 언어의 순서를 뒤바꿈(예: `f"{base}-{args.target_lang}-{args.model}.md"`)으로 번역물의 정리 및 검색을 용이하게 함.
    - **기타 개선 사항 :**
        - 불필요한 빈 줄 제거로 코드 정리.
        - 구조 및 가독성 향상을 위한 사소한 조정.
- **1.4** 새로운 기능 :
    - Anthropic의 Claude API 지원
    - 명확성과 효율성을 높이기 위한 프롬프트 최적화
    - 코드 유지 관리를 위한 사소한 조정
- **1.3** 개선 사항 및 신규 기능 :
    - 코드 블록 처리 개선
    - 출력 파일 관리 개선
    - 기존 파일 감지 향상
    - 번역 강제 옵션 `--force`
    - 출력 파일 이름에서 모델과 언어의 순서 뒤바꿈
- **1.2** 변경 로그 수정
- **1.1** Mistral IA API 지원 추가
- **1.0** 초기 버전 - OpenAI API 지원

**이 문서는 gpt-5-mini 모델을 사용하여 fr 버전에서 ko 언어로 번역되었습니다. 번역 과정에 대한 자세한 정보는 https://gitlab.com/jls42/ai-powered-markdown-translator 를 참조하십시오.**

