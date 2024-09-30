# OpenAI, Mistral AI 및 Claude d'Anthropic가 포함된 AI 기반 마크다운 번역기

이 프로젝트는 OpenAI, Mistral AI 또는 Claude d'Anthropic API를 사용하여 원본 언어에서 대상 언어로 마크다운 파일을 번역하는 고급 Python 스크립트입니다. 사용하기 쉽고 유연하도록 설계되었으며 번역 노트 추가, 출력 파일 관리, 기존 파일 감지와 같은 추가 옵션을 제공하며 여러 언어 및 번역 모델을 지원합니다.

데모와 자세한 설명은 [jls42.org](https://jls42.org/) 또는 번역된 버전에서 확인하세요: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) 및 [jls42.org 中文](https://jls42.org/traductions_zh/).

## 주요 기능

- **AI 기반 번역**: OpenAI, Mistral AI 또는 Claude d'Anthropic와 함께 최신 AI 기술을 사용하여 문서를 번역합니다.
- **다국어 지원**: 여러 언어로 문서를 번역하며 다양한 언어 모델을 지원합니다.
- **지능형 세분화**: 자동화된 세분화를 통해 긴 텍스트를 효율적으로 관리합니다.
- **번역 노트**: 번역 과정을 독자에게 알리는 번역 노트를 자동으로 추가합니다.
- **개선된 출력 파일 관리**: 번역을 시작하기 전에 번역이 이미 존재하는지 확인합니다.
- **개선된 기존 파일 감지**: 원본 파일 이름의 기본 이름과 대상 언어에 해당하는 파일을 검색합니다.
- **유연하고 확장 가능**: 코드는 새로운 기능 추가를 용이하게 하도록 구조화되어 있습니다.

## 필수 조건

- Python 3.6 이상 버전.
- 유효한 OpenAI, Mistral AI 또는 Claude d'Anthropic API 키.

## 설치

1. Git 저장소를 클론하세요:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 필요한 종속성을 설치하세요:
```
pip install -r requirements.txt
```

## 구성

필요한 API 키를 환경 변수로 설정하여 환경을 구성하세요:

- **OpenAI** :
    ```
    export OPENAI_API_KEY='votre-clé-api-openai'
    ```
- **Mistral AI** :
    ```
    export MISTRAL_API_KEY='votre-clé-api-mistral'
    ```
- **Claude d'Anthropic** :
    ```
    export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
    ```

## 사용법

스크립트는 번역 과정을 사용자 정의할 수 있는 여러 옵션을 제공합니다:

### 일반 옵션

- `--source_dir` : 번역할 마크다운 파일이 포함된 디렉토리.
- `--target_dir` : 번역된 파일의 출력 디렉토리.
- `--model` : 사용할 GPT 번역 모델. 기본 모델은 선택한 API에 따라 다릅니다.
- `--source_lang` : 문서의 원본 언어. 특히 번역 노트를 추가할 때 중요합니다.
- `--target_lang` : 번역 대상 언어. 기본값은 영어입니다.
- `--force` : 파일에 대한 번역이 이미 존재하더라도 번역을 강제로 수행합니다.

### API 특정 옵션

- `--use_mistral` : 번역에 Mistral AI API를 사용합니다.
- `--use_claude` : 번역에 Claude d'Anthropic API를 사용합니다.
- `--add_translation_note` : 사용된 방법과 도구를 명시하는 번역 노트를 번역 내용에 추가합니다.

### 사용 예시

- OpenAI를 사용하여 프랑스어를 영어로 번역하고 번역 노트를 추가합니다:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AI를 사용하여 프랑스어를 스페인어로 번역하고 번역 노트를 추가하지 않습니다:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 작성자

Julien LE SAUX  
Email : contact@jls42.org

## 라이선스

이 프로젝트는 GNU 일반 공중 사용 허가서 버전 3, 2007년 6월 29일의 조건에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

**이 문서는 gpt-4o 모델을 사용하여 fr 버전에서 ko 언어로 번역되었습니다. 번역 프로세스에 대한 자세한 내용은 https://gitlab.com/jls42/ai-powered-markdown-translator를 참조하십시오.**

