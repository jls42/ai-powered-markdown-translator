# AI 기반 Markdown 번역기

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기.

이 Python 스크립트는 서식, 코드 블록 및 프런트 매터 메타데이터를 유지하면서 소스 언어의 Markdown 파일을 대상 언어로 번역합니다.

## 주요 특징

- **멀티 프로바이더**: 4개 API 지원 (OpenAI, Mistral, Claude, Gemini)
- **2026년 모델**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 하나의 파일만 번역하기 위한 `--file` 옵션
- **지능형 분할**: 모델별 토큰 한도를 고려한 장문 텍스트 처리
- **코드 보존**: 코드 블록은 번역되지 않습니다
- **번역 노트**: 문서 끝에 노트를 선택적으로 추가

## 설치

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 설정

사용하려는 API에 대한 환경 변수를 설정하세요:

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## 사용법

### 단일 파일 번역

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 디렉터리 번역

```bash
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 경제 모드

더 빠르고 비용이 적은 모델을 사용합니다 (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션 | 설명 |
|--------|-------------|
| `--file` | 번역할 단일 Markdown 파일 |
| `--source_dir` | Markdown 파일이 들어 있는 소스 디렉터리 |
| `--target_dir` | 번역된 파일의 출력 디렉터리 |
| `--source_lang` | 소스 언어 (기본값: `fr`) |
| `--target_lang` | 대상 언어 (기본값: `en`) |
| `--model` | 사용할 특정 모델 |
| `--eco` | 경제형 모델 사용 |
| `--use_mistral` | Mistral AI API 사용 |
| `--use_claude` | Claude API 사용 |
| `--use_gemini` | Gemini API 사용 |
| `--force` | 재번역 강제 |
| `--add_translation_note` | 번역 노트 추가 |

### 기본 모델 (2026)

| 프로바이더 | 품질(기본) | 경제형 (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 작성자

Julien LE SAUX
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE 버전 3. [LICENSE](LICENSE)를 참조하세요.