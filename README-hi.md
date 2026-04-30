# एआई-संचालित Markdown अनुवादक

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइल अनुवादक।

यह Python स्क्रिप्ट स्रोत भाषा से लक्ष्य भाषा में Markdown फ़ाइलों का अनुवाद करती है, साथ ही फ़ॉर्मेटिंग, कोड ब्लॉक और front matter मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **Multi-Provider**: 4 APIs (OpenAI, Mistral, Claude, Gemini) का समर्थन
- **2026 मॉडल**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **किफायती मोड**: तेज़ और कम-लागत वाले मॉडल उपयोग करने के लिए विकल्प `--eco`
- **एकल फ़ाइल**: एक ही फ़ाइल का अनुवाद करने के लिए विकल्प `--file`
- **स्मार्ट सेगमेंटेशन**: मॉडल-विशिष्ट टोकन सीमाओं के साथ लंबे पाठ का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और inline code (`` `...` ``) सुरक्षित रखे जाते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए विकल्प `--keep_filename`
- **News मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों की सुरक्षा और झंडों के प्रबंधन के लिए विकल्प `--news`
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## स्थापना

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### गुणवत्ता टूलिंग (वैकल्पिक लेकिन अनुशंसित)

प्रोजेक्ट [`pre-commit`](https://pre-commit.com) का उपयोग करता है ताकि गलत-फ़ॉर्मेट किए गए, असुरक्षित या सीक्रेट वाले कोड को कमिट होने से रोका जा सके। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (जटिलता), detect-secrets (API कुंजियाँ), mypy (क्रमिक टाइपिंग), Opengrep (SAST), pip-audit (CVE deps), unittest। विवरण के लिए `CLAUDE.md` अनुभाग _Quality / pre-commit_ देखें।

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

### एकल फ़ाइल का अनुवाद करें

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### एक directory का अनुवाद करें

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

तेज़ और कम-लागत वाले मॉडल (gpt-5.4-mini, claude-haiku, gemini-flash) का उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद के लिए एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलों वाला स्रोत directory                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट directory                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्ष्य भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                             |
| `--eco`                  | किफायती मॉडल उपयोग करें                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करें                                                |
| `--use_claude`           | Claude API का उपयोग करें                                                    |
| `--use_gemini`           | Gemini API का उपयोग करें                                                    |
| `--force`                | पुनः-अनुवाद को बाध्य करें                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखें                                     |
| `--news`                 | समाचार मोड: EN उद्धरणों की सुरक्षा करता है, भाषा के अनुसार झंडों का प्रबंधन करता है |
| `--add_translation_note` | अनुवाद नोट जोड़ें                                           |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें                       |

### डिफ़ॉल्ट मॉडल (2026)

| प्रदाता | गुणवत्ता (डिफ़ॉल्ट)         | किफायती (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **लंबे-रूप अनुवादों के लिए अनुशंसा** : `--use_gemini` (डिफ़ॉल्ट = `gemini-3.1-pro-preview` गुणवत्ता, `--eco` = `gemini-3-flash-preview`) गैर-लैटिन स्क्रिप्टों (PL, JA, ZH, AR, HI) पर markdown संरचना को बेहतर ढंग से संरक्षित करने की प्रवृत्ति रखता है, विशेषकर `--news` मोड में जहाँ placeholders की निष्ठा महत्वपूर्ण होती है। पीछे की संगतता के लिए OpenAI अभी भी डिफ़ॉल्ट है।

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX
Email : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. देखें [LICENSE](LICENSE).

**इस दस्तावेज़ का अनुवाद फ्र संस्करण से hi भाषा में gpt-5.4-mini मॉडल का उपयोग करके किया गया है। अनुवाद प्रक्रिया के बारे में अधिक जानकारी के लिए, https://gitlab.com/jls42/ai-powered-markdown-translator देखें**

