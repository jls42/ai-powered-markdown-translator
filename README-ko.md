# AI 기반 Markdown 번역기

🌍 [프랑스어](README.md) | [영어](README-en.md) | [스페인어](README-es.md) | [중국어](README-zh.md) | [독일어](README-de.md) | [일본어](README-ja.md) | [한국어](README-ko.md) | [아랍어](README-ar.md) | [힌디어](README-hi.md) | [이탈리아어](README-it.md) | [네덜란드어](README-nl.md) | [폴란드어](README-pl.md) | [포르투갈어](README-pt.md) | [루마니아어](README-ro.md) | [스웨덴어](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기입니다.

이 Python 스크립트는 원본 언어에서 대상 언어로 Markdown 파일을 번역하면서 형식, 코드 블록 및 front matter 메타데이터를 보존합니다.

## 주요 기능

- **다중 제공자**: 4개의 API 지원 (OpenAI, Mistral, Claude, Gemini)
- **2026 모델**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **경제 모드**: 옵션 `--eco` 으로 더 빠르고 저렴한 모델 사용
- **단일 파일**: 옵션 `--file` 으로 단일 파일 번역
- **스마트 분할**: 모델별 토큰 한계를 고려한 긴 텍스트 처리
- **코드 보존**: 코드 블록 및 인라인 코드 (`` `...` ``) 보존
- **파일명**: 옵션 `--keep_filename` 으로 원본 이름 유지
- **뉴스 모드**: 옵션 `--news` 로 영어 인용문 보호 및 기사 내 언어별 국기 처리
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 메모**: 문서 끝에 선택적으로 번역 메모 추가

## 설치

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 구성

프로젝트 루트에 `.env` 파일을 생성하거나 환경 변수를 설정하세요:

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

더 빠르고 저렴한 모델 사용 (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션 | 설명 |
|--------|-------------|
| `--file` | 번역할 단일 Markdown 파일 |
| `--source_dir` | Markdown 파일이 들어있는 소스 디렉터리 |
| `--target_dir` | 번역된 파일을 위한 출력 디렉터리 |
| `--source_lang` | 원본 언어 (기본: `fr`) |
| `--target_lang` | 대상 언어 (기본: `en`) |
| `--model` | 사용할 특정 모델 |
| `--eco` | 경제 모델 사용 |
| `--use_mistral` | Mistral AI API 사용 |
| `--use_claude` | Claude API 사용 |
| `--use_gemini` | Gemini API 사용 |
| `--force` | 재번역 강제 |
| `--keep_filename` | 원본 파일명 유지 |
| `--news` | 뉴스 모드: 영어 인용문 보호, 언어별 국기 처리 |
| `--add_translation_note` | 번역 메모 추가 |
| `--include_model` | 출력 파일에 모델 이름 포함 |

### 기본 모델 (2026)

| 제공자 | 품질 (기본) | 경제형 (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그 (15개 언어)

## 저자

Julien LE SAUX  
이메일 : contact@jls42.org

## 라이선스

GNU 일반 공중 사용 허가서 버전 3. [라이선스](LICENSE)를 참조하세요.

**이 문서는 gpt-5-mini 모델을 사용하여 프랑스어(fr) 버전에서 한국어(ko)로 번역되었습니다. 번역 과정에 대한 자세한 내용은 https://gitlab.com/jls42/ai-powered-markdown-translator를 참조하세요.**

