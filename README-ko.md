# AI 기반 Markdown 번역기

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기입니다.

이 Python 스크립트는 서식, 코드 블록 및 front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **멀티 제공업체**: 4개 API 지원(OpenAI, Mistral, Claude, Gemini)
- **2026 모델**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 하나의 파일만 번역하기 위한 `--file` 옵션
- **지능형 분할**: 모델별 토큰 제한을 고려한 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드(`` `...` ``)가 보존됩니다
- **파일 이름**: 원래 이름을 유지하기 위한 `--keep_filename` 옵션
- **뉴스 모드**: 뉴스 기사에서 영어 인용문을 보호하고 언어별 국기를 처리하기 위한 `--news` 옵션
- **.env 설정**: API 키를 위한 `.env` 파일 지원
- **번역 노트**: 문서 끝에 선택적으로 노트를 추가

## 설치

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 설정

프로젝트 루트에 `.env` 파일을 만들거나 환경 변수를 정의하세요:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## 사용법

### 단일 파일 번역

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 디렉터리 번역

```bash
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 경제 모드

더 빠르고 저렴한 모델(gpt-5-mini, claude-haiku, gemini-flash)을 사용합니다:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| Option | Description |
|--------|-------------|
| `--file` | 번역할 단일 Markdown 파일 |
| `--source_dir` | Markdown 파일이 들어 있는 소스 디렉터리 |
| `--target_dir` | 번역된 파일의 출력 디렉터리 |
| `--source_lang` | 소스 언어(기본값: `fr`) |
| `--target_lang` | 대상 언어(기본값: `en`) |
| `--model` | 사용할 특정 모델 |
| `--eco` | 경제 모델 사용 |
| `--use_mistral` | Mistral AI API 사용 |
| `--use_claude` | Claude API 사용 |
| `--use_gemini` | Gemini API 사용 |
| `--force` | 재번역 강제 실행 |
| `--keep_filename` | 원래 파일 이름 유지 |
| `--news` | 뉴스 모드: EN 인용문 보호, 언어별 국기 처리 |
| `--add_translation_note` | 번역 노트 추가 |
| `--include_model` | 출력 파일에 모델 이름 포함 |

### 기본 모델(2026)

| Provider | 품질(기본) | 경제적(`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) 참조.