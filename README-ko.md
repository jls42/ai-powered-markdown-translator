# AI 기반 Markdown 번역기

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기입니다.

이 Python 스크립트는 소스 언어에서 대상 언어로 Markdown 파일을 번역하면서 서식, 코드 블록, front matter 메타데이터를 보존합니다.

## 주요 기능

- **Multi-Provider**: 4개 API 지원(OpenAI, Mistral, Claude, Gemini)
- **2026 모델**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **경제 모드**: 더 빠르고 저렴한 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 단일 파일을 번역하기 위한 `--file` 옵션
- **지능형 분할**: 모델별 토큰 제한을 고려한 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드(`` `...` ``)가 보존됩니다
- **파일 이름**: 원래 이름을 유지하기 위한 `--keep_filename` 옵션
- **뉴스 모드**: 뉴스 기사에서 영어 인용문을 보호하고 국기를 처리하기 위한 `--news` 옵션
- **.env 구성**: API 키를 위한 `.env` 파일 지원
- **번역 메모**: 문서 끝에 선택적으로 메모 추가

## 설치

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 품질 도구(선택 사항이지만 권장)

이 프로젝트는 잘못된 형식이거나, 취약하거나, 비밀을 포함한 코드를 커밋하는 것을 방지하기 위해 [`pre-commit`](https://pre-commit.com)를 사용합니다. 설치:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성 훅: ruff(lint+format), shellcheck(bash), prettier(markdown/yaml/json), Lizard(복잡도), detect-secrets(API 키), mypy(점진적 타이핑), Opengrep(SAST), pip-audit(CVE deps), unittest. 자세한 내용은 `CLAUDE.md` 섹션 _Quality / pre-commit_을 참조하세요.

## 구성

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
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 경제 모드

더 빠르고 저렴한 모델(gpt-5.4-mini, claude-haiku, gemini-flash)을 사용합니다:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션                   | 설명                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 번역할 단일 Markdown 파일                                       |
| `--source_dir`           | Markdown 파일이 들어 있는 소스 디렉터리                        |
| `--target_dir`           | 번역된 파일의 출력 디렉터리                          |
| `--source_lang`          | 소스 언어(기본값: `fr`)                                             |
| `--target_lang`          | 대상 언어(기본값: `en`)                                              |
| `--model`                | 사용할 특정 모델                                             |
| `--eco`                  | 경제 모델 사용                                         |
| `--use_mistral`          | Mistral AI API 사용                                                |
| `--use_claude`           | Claude API 사용                                                    |
| `--use_gemini`           | Gemini API 사용                                                    |
| `--force`                | 재번역 강제                                                  |
| `--keep_filename`        | 원본 파일 이름 유지                                     |
| `--news`                 | 뉴스 모드: EN 인용문 보호, 언어별 국기 처리 |
| `--add_translation_note` | 번역 메모 추가                                           |
| `--include_model`        | 출력 파일에 모델 이름 포함                       |

### 기본 모델(2026)

| Provider | 품질(기본값)         | 경제적 (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **장문 번역 권장 사항**: `--use_gemini`(기본값 = `gemini-3.1-pro-preview` 품질, `--eco` = `gemini-3-flash-preview`)은 비라틴 문자 스크립트(PL, JA, ZH, AR, HI)에서 Markdown 구조를 더 잘 보존하는 경향이 있으며, 특히 플레이스홀더 충실도가 중요한 `--news` 모드에서 그렇습니다. OpenAI는 하위 호환성을 위해 기본값으로 유지됩니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX
Email : contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE)를 참조하세요.

**이 문서는 gpt-5.4-mini 모델을 사용하여 fr 버전에서 ko 언어로 번역되었습니다. 번역 과정에 대한 자세한 정보는 https://gitlab.com/jls42/ai-powered-markdown-translator 를 참조하세요.**

