# OpenAI, Mistral AI 및 Anthropic의 Claude를 사용한 AI 기반 Markdown 번역기

이 프로젝트는 OpenAI, Mistral AI 또는 Anthropic의 Claude API를 사용하여 Markdown 파일을 원본 언어에서 대상 언어로 번역하는 고급 Python 스크립트입니다. 유연하고 사용하기 쉽게 설계되었으며, 번역 노트 추가, 향상된 출력 파일 관리, 기존 파일 감지, 여러 언어 및 번역 모델 지원과 같은 추가 옵션을 제공합니다.

데모 및 자세한 설명은 [jls42.org](https://jls42.org/) 또는 번역된 버전: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) 및 [jls42.org 中文](https://jls42.org/traductions_zh/)을 방문하세요.

## 주요 특징

- **AI 기반 번역**: OpenAI, Mistral AI 또는 Anthropic의 Claude를 사용하여 문서 번역에 최신 AI 기술을 활용합니다.
- **다국어 지원**: 다양한 언어 모델을 지원하여 문서를 여러 언어로 번역합니다.
- **지능형 분할**: 자동화된 분할을 통해 긴 텍스트를 효율적으로 관리합니다.
- **번역 노트**: 사용된 프로세스에 대해 독자에게 알리기 위해 자동으로 번역 노트를 추가합니다.
- **향상된 출력 파일 관리**: 번역을 시작하기 전에 번역이 이미 존재하는지 확인합니다.
- **향상된 기존 파일 감지**: 원본 파일의 기본 이름과 대상 언어에 해당하는 파일을 검색합니다.
- **유연하고 확장 가능**: 새로운 기능을 쉽게 추가할 수 있도록 코드가 구조화되어 있습니다.

## 전제 조건

- Python 3.6 이상.
- OpenAI, Mistral AI 또는 Anthropic의 Claude에 대한 유효한 API 키.

## 설치

1. Git 저장소 복제:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 필요한 종속성 설치:
```
pip install -r requirements.txt
```

## 구성

필요한 API 키에 대한 환경 변수를 설정하여 환경을 구성하세요:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Anthropic의 Claude**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## 사용법

스크립트는 번역 프로세스를 사용자 정의하기 위한 여러 옵션을 제공합니다:

### 일반 옵션

- `--source_dir`: 번역할 Markdown 파일이 포함된 디렉토리.
- `--target_dir`: 번역된 파일의 출력 디렉토리.
- `--model`: 사용할 GPT 번역 모델. 기본 모델은 선택된 API에 따라 다릅니다.
- `--source_lang`: 문서의 원본 언어. 특히 번역 노트 추가에 중요합니다.
- `--target_lang`: 번역 대상 언어. 기본값은 영어입니다.
- `--force`: 파일에 대한 번역이 이미 존재하더라도 번역을 강제합니다.

### API 특정 옵션

- `--use_mistral`: 번역에 Mistral AI API 사용.
- `--use_claude`: 번역에 Anthropic의 Claude API 사용.
- `--add_translation_note`: 번역된 내용에 사용된 방법과 도구를 명시하는 번역 노트 추가.

### 사용 예시

- OpenAI를 사용하여 프랑스어에서 영어로 번역하고 번역 노트 추가:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AI를 사용하여 프랑스어에서 스페인어로 번역, 번역 노트 없음:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 저자

Julien LE SAUX  
이메일: contact@jls42.org

## 라이선스

이 프로젝트는 GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 하에 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

**이 문서는 claude-3-5-sonnet-20240620 모델을 사용하여 fr 버전에서 ko 언어로 번역되었습니다. 번역 과정에 대한 자세한 정보는 https://gitlab.com/jls42/ai-powered-markdown-translator 를 참조하십시오.**

