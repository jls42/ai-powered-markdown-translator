# AI-Powered Markdown 번역기

🌍 [프랑스어](README.md) | [영어](README-en.md) | [스페인어](README-es.md) | [중국어](README-zh.md) | [독일어](README-de.md) | [일본어](README-ja.md) | [한국어](README-ko.md) | [아랍어](README-ar.md) | [힌디어](README-hi.md) | [이탈리아어](README-it.md) | [네덜란드어](README-nl.md) | [폴란드어](README-pl.md) | [포르투갈어](README-pt.md) | [루마니아어](README-ro.md) | [스웨덴어](README-sv.md)

<h4 align="center">📊 코드 품질</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="품질 게이트 상태"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="보안 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="신뢰성 등급"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="유지보수성 등급"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="커버리지"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="취약점"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="버그"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="코드 스멜"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="중복된 줄(%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="기술 부채"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="코드 줄 수"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 배지"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** 및 **Google Gemini**를 사용하는 Markdown 파일 번역기입니다.

이 Python 스크립트는 서식, 코드 블록, front matter 메타데이터를 보존하면서 Markdown 파일을 원본 언어에서 대상 언어로 번역합니다.

## 주요 기능

- **다중 공급자**: 4개 API 지원(OpenAI, Mistral, Claude, Gemini)
- **2026 모델**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **경제 모드**: 더 빠르고 비용이 적게 드는 모델을 사용하기 위한 `--eco` 옵션
- **단일 파일**: 하나의 파일만 번역하기 위한 `--file` 옵션
- **지능형 분할**: 모델별 토큰 제한이 있는 긴 텍스트 처리
- **코드 보존**: 코드 블록과 인라인 코드(`` `...` ``)가 보존됩니다
- **파일 이름**: 원래 이름을 유지하기 위한 `--keep_filename` 옵션
- **뉴스 모드**: 뉴스 기사에서 영어 인용문을 보호하고 언어별 깃발을 처리하기 위한 `--news` 옵션
- **.env 설정**: API 키를 위한 `.env` 파일 지원
- **번역 노트**: 문서 끝에 선택적으로 노트를 추가

## 설치

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 품질 도구(선택 사항이지만 권장)

이 프로젝트는 형식이 잘못되었거나 취약점이 있거나 비밀 정보가 포함된 코드를 커밋하는 것을 방지하기 위해 [`pre-commit`](https://pre-commit.com)를 사용합니다. 설치:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

활성 후크: ruff(lint+format), shellcheck(bash), prettier(markdown/yaml/json), Lizard(복잡도), detect-secrets(API 키), mypy(점진적 타이핑), Opengrep(SAST), pip-audit(CVE 의존성), unittest. 자세한 내용은 `CLAUDE.md`의 _Quality / pre-commit_ 섹션을 참조하세요.

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

더 빠르고 비용이 적게 드는 모델(gpt-5.4-mini, claude-haiku, gemini-flash)을 사용합니다:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 옵션

| 옵션                     | 설명                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 번역할 단일 Markdown 파일                                       |
| `--source_dir`           | Markdown 파일이 들어 있는 원본 디렉터리                        |
| `--target_dir`           | 번역된 파일의 출력 디렉터리                          |
| `--source_lang`          | 원본 언어(기본값: `fr`)                                             |
| `--target_lang`          | 대상 언어(기본값: `en`)                                              |
| `--model`                | 사용할 특정 모델                                             |
| `--eco`                  | 경제형 모델 사용                                         |
| `--use_mistral`          | Mistral AI API 사용                                                |
| `--use_claude`           | Claude API 사용                                                    |
| `--use_gemini`           | Gemini API 사용                                                    |
| `--force`                | 재번역 강제                                                  |
| `--keep_filename`        | 원래 파일 이름 유지                                     |
| `--news`                 | 뉴스 모드: 영어 인용문 보호, 언어별 깃발 처리 |
| `--add_translation_note` | 번역 노트 추가                                           |
| `--note_position`        | 노트 위치: `top`, `bottom`(기본값), 또는 `both`                |
| `--note_format`          | 노트 형식: `legacy`(기본값, 굵은 문단) 또는 `marker`       |
| `--include_model`        | 출력 파일에 모델 이름 포함                       |

### 번역 노트: 위치와 형식

`--add_translation_note`를 사용하면 번역기는 노트를 상단, 하단, 또는 양쪽 모두에 배치할 수 있으며, 일반 텍스트 형식(하위 호환) 또는 Markdown 플러그인에서 사용할 수 있는 `marker` 형식으로 만들 수 있습니다.

**위치** (`--note_position`) :

- `bottom`(기본값): 기존과 같이 파일 끝에 노트 삽입.
- `top`: YAML frontmatter 뒤에 노트 삽입(Astro Content Collections, gray-matter 등의 안전성).
- `both`: 상단과 하단 모두에 삽입(LLM 호출 1회, 두 위치에 재사용되는 콘텐츠).

**형식** (`--note_format`) :

- `legacy`(기본값): 굵은 문단 `**...**` — v1.8과 바이트 단위로 완전히 동일한 동작. Hugo, GitHub, GitLab 및 모든 Markdown 렌더러와 호환됩니다.
- `marker`: 보이지 않는 Markdown 링크 참조 정의 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` 뒤에 굵은 blockquote가 오는 형식. GitHub/GitLab에서 기본적으로 읽을 수 있으며, Astro 측의 remark 플러그인이 빌드 시 스타일이 적용된 배너를 생성하는 데 사용할 수 있습니다(참조: blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### 기본 모델(2026)

| 공급자 | 품질(기본값)         | 경제형 (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **장문 번역 권장**: `--use_gemini`(기본값 = `gemini-3.1-pro-preview` 품질, `--eco` = `gemini-3.1-flash-lite-preview`)는 비라틴 스크립트(PL, JA, ZH, AR, HI)에서 Markdown 구조를 더 잘 보존하는 경향이 있으며, 특히 플레이스홀더의 정확성이 중요한 `--news` 모드에서 그렇습니다. OpenAI는 여전히 하위 호환을 위한 기본값입니다.

## 이 스크립트를 사용하는 프로젝트

- **[jls42.org](https://jls42.org)** - 다국어 개인 블로그(15개 언어)

## 작성자

Julien LE SAUX  
이메일: contact@jls42.org

## 라이선스

GNU GENERAL PUBLIC LICENSE 버전 3. [LICENSE](LICENSE)를 참조하세요.

**gpt-5.4-mini로 프랑스어에서 한국어로 번역된 기사.**
