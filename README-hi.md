# एआई-संचालित मार्कडाउन अनुवादक

🌍 [फ़्रेंच](README.md) | [अंग्रेज़ी](README-en.md) | [स्पैनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

<h4 align="center">📊 कोड गुणवत्ता</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करके मार्कडाउन फ़ाइलों का अनुवादक।

यह Python स्क्रिप्ट स्रोत भाषा से लक्ष्य भाषा में Markdown फ़ाइलों का अनुवाद करती है, जबकि फ़ॉर्मेटिंग, कोड ब्लॉक्स और front matter मेटाडेटा को संरक्षित रखती है।

## मुख्य विशेषताएँ

- **कई प्रदाता**: 4 APIs (OpenAI, Mistral, Claude, Gemini) का समर्थन
- **2026 मॉडल**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **किफायती मोड**: `--eco` विकल्प, तेज़ और कम लागत वाले मॉडलों का उपयोग करने के लिए
- **एकल फ़ाइल**: एक ही फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **बुद्धिमान विभाजन**: मॉडल टोकन सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक्स और inline code (`` `...` ``) दोनों संरक्षित रहते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **न्यूज़ मोड**: अंग्रेज़ी उद्धरणों की सुरक्षा और समाचार लेखों में झंडों को संभालने के लिए `--news` विकल्प
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## स्थापना

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### गुणवत्ता टूलिंग (वैकल्पिक लेकिन अनुशंसित)

प्रोजेक्ट खराब फ़ॉर्मेटेड, असुरक्षित या गोपनीयता-उल्लंघन करने वाले कोड को कमिट होने से रोकने के लिए [`pre-commit`](https://pre-commit.com) का उपयोग करता है। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय हुक: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (CVE deps), unittest। विवरण के लिए `CLAUDE.md` अनुभाग _Quality / pre-commit_ देखें।

## कॉन्फ़िगरेशन

प्रोजेक्ट की root में एक `.env` फ़ाइल बनाएं या environment variables परिभाषित करें:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## उपयोग

### एकल फ़ाइल का अनुवाद

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### किसी निर्देशिका का अनुवाद

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

### किफायती मोड

तेज़ और कम लागत वाले मॉडल (gpt-5.4-mini, claude-haiku, gemini-flash) का उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद करने के लिए एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलों वाली स्रोत निर्देशिका                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्ष्य भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                             |
| `--eco`                  | किफायती मॉडल उपयोग करें                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करें                                                |
| `--use_claude`           | Claude API का उपयोग करें                                                    |
| `--use_gemini`           | Gemini API का उपयोग करें                                                    |
| `--force`                | पुनः-अनुवाद को बाध्य करें                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखें                                     |
| `--news`                 | समाचार मोड: EN उद्धरणों की सुरक्षा करता है, भाषा के अनुसार झंडों को संभालता है |
| `--add_translation_note` | अनुवाद नोट जोड़ें                                           |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें                       |

### डिफ़ॉल्ट मॉडल (2026)

| प्रदाता | गुणवत्ता (डिफ़ॉल्ट)         | किफायती (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **लंबे-फॉर्म अनुवादों के लिए सिफारिश** : `--use_gemini` (डिफ़ॉल्ट = `gemini-3.1-pro-preview` गुणवत्ता, `--eco` = `gemini-3.1-flash-lite-preview`) गैर-लैटिन स्क्रिप्ट्स (PL, JA, ZH, AR, HI) पर markdown संरचना को बेहतर बनाए रखने की प्रवृत्ति रखता है, विशेष रूप से `--news` मोड में जहाँ placeholders की निष्ठा महत्वपूर्ण होती है। पिछड़े संगतता के लिए OpenAI अभी भी डिफ़ॉल्ट है।

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX
Email : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. देखें [LICENSE](LICENSE).

**यह दस्तावेज़ fr संस्करण से hi भाषा में gpt-5.4-mini मॉडल का उपयोग करके अनुवादित किया गया है। अनुवाद प्रक्रिया के बारे में अधिक जानकारी के लिए, https://github.com/jls42/ai-powered-markdown-translator देखें**
