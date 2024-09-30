# AI-Powered Markdown 번역기 OpenAI, Mistral AI 및 Anthropic의 Claude

이 프로젝트는 OpenAI, Mistral AI 또는 Anthropic의 Claude API를 사용하여 소스 언어에서 대상 언어로 Markdown 파일을 번역하는 고급 Python 스크립트입니다. 유연하고 사용하기 쉬운 것을 목표로 설계되었으며, 번역 주석 추가, 출력 파일 관리 개선, 기존 파일 감지 및 다양한 언어 및 번역 모델 지원과 같은 추가 옵션을 제공합니다.

자세한 설명과 데모를 보려면 [jls42.org](https://jls42.org/) 또는 번역된 버전을 방문하세요: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) 및 [jls42.org 中文](https://jls42.org/traductions_zh/).

## 주요 특징

- **AI-Powered 번역**: OpenAI, Mistral AI 또는 Anthropic의 Claude를 사용하여 최신 AI 기술로 문서를 번역합니다.
- **다국어 지원**: 다양한 언어 모델을 지원하여 문서를 여러 언어로 번역합니다.
- **스마트 세그먼트**: 자동 세그먼트를 통해 긴 텍스트를 효과적으로 관리합니다.
- **번역 주석**: 사용된 프로세스에 대한 독자 정보를 제공하기 위해 자동으로 번역 주석을 추가합니다.
- **출력 파일 관리 개선**: 번역을 시작하기 전에 번역이 이미 존재하는지 확인합니다.
- **기존 파일 감지 개선**: 원본 파일의 기본 이름과 대상 언어에 해당하는 파일을 검색합니다.
- **유연하고 확장 가능**: 새로운 기능을 쉽게 추가할 수 있도록 코드가 구조화되어 있습니다.

## 전제 조건

- Python 3.6 이상.
- OpenAI, Mistral AI 또는 Anthropic의 Claude에 대한 유효한 API 키.

## 설치

1. Git 저장소를 복제합니다:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 필요한 종속성을 설치합니다:
```
pip install -r requirements.txt
```

## 구성

환경을 구성하려면 필요한 API 키에 대한 환경 변수를 설정합니다:

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
- `--model`: 사용할 GPT 번역 모델. 기본 모델은 선택한 API에 따라 다릅니다.
- `--source_lang`: 문서의 소스 언어. 특히 번역 주석 추가에 중요합니다.
- `--target_lang`: 번역할 대상 언어. 기본값은 영어입니다.
- `--force`: 파일에 이미 번역이 있는 경우에도 번역을 강제합니다.

### API 특정 옵션

- `--use_mistral`: 번역에 Mistral AI API를 사용합니다.
- `--use_claude`: 번역에 Anthropic의 Claude API를 사용합니다.
- `--add_translation_note`: 번역된 콘텐츠에 사용된 방법 및 도구를 지정하는 번역 주석을 추가합니다.

### 사용 예

- OpenAI를 사용하여 프랑스어에서 영어로 번역하고 번역 주석을 추가합니다:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AI를 사용하여 프랑스어에서 스페인어로 번역하고 번역 주석을 추가하지 않습니다:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 작성자

Julien LE SAUX
Email: contact@jls42.org

## 라이선스

이 프로젝트는 GNU GENERAL PUBLIC LICENSE 버전 3, 2007년 6월 29일에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

**Ce document a été traduit de la version fr vers la langue ko en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**

