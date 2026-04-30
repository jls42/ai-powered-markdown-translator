# एआई-संचालित Markdown अनुवादक

🌍 [फ़्रançais](README.md) | [अंग्रेज़ी](README-en.md) | [स्पैनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइलों का अनुवादक।

यह Python स्क्रिप्ट स्रोत भाषा से लक्ष्य भाषा में Markdown फ़ाइलों का अनुवाद करती है, जबकि फ़ॉर्मैटिंग, कोड ब्लॉक और front matter मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **Multi-Provider**: 4 APIs (OpenAI, Mistral, Claude, Gemini) का समर्थन
- **2026 मॉडल**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **आर्थिक मोड**: तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: एक ही फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **स्मार्ट सेगमेंटेशन**: मॉडल-विशिष्ट टोकन सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और inline code (`` `...` ``) सुरक्षित रहते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **समाचार मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों की सुरक्षा और झंडों को संभालने के लिए `--news` विकल्प
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## स्थापना

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### गुणवत्ता उपकरण (वैकल्पिक लेकिन अनुशंसित)

प्रोजेक्ट खराब फ़ॉर्मैट किए गए, असुरक्षित या सीक्रेट वाली कोड कमिट करने से रोकने के लिए [`pre-commit`](https://pre-commit.com) का उपयोग करता है। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (CVE deps), unittest. विवरण के लिए `CLAUDE.md` अनुभाग _Quality / pre-commit_ देखें।

## कॉन्फ़िगरेशन

प्रोजेक्ट की रूट में एक `.env` फ़ाइल बनाएँ या पर्यावरण चर (environment variables) परिभाषित करें:

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

### एक निर्देशिका का अनुवाद

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

### आर्थिक मोड

तेज़ और कम लागत वाले मॉडल (gpt-5.4-mini, claude-haiku, gemini-flash) का उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद करने के लिए एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलें युक्त स्रोत निर्देशिका                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्ष्य भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                             |
| `--eco`                  | आर्थिक मॉडल का उपयोग करें                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करें                                                |
| `--use_claude`           | Claude API का उपयोग करें                                                    |
| `--use_gemini`           | Gemini API का उपयोग करें                                                    |
| `--force`                | पुनः-अनुवाद को बाध्य करें                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखें                                     |
| `--news`                 | समाचार मोड: EN उद्धरणों की रक्षा करता है, भाषा के अनुसार झंडों को संभालता है |
| `--add_translation_note` | एक अनुवाद नोट जोड़ें                                           |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें                       |

### डिफ़ॉल्ट मॉडल (2026)

| Provider | गुणवत्ता (डिफ़ॉल्ट)         | आर्थिक (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **लंबी-रूप अनुवादों के लिए अनुशंसा** : `--use_gemini` (डिफ़ॉल्ट = `gemini-3.1-pro-preview` गुणवत्ता, `--eco` = `gemini-3-flash-preview`) गैर-लैटिन स्क्रिप्ट्स (PL, JA, ZH, AR, HI) पर markdown संरचना को बेहतर बनाए रखने की प्रवृत्ति रखता है, विशेषकर `--news` मोड में जहाँ placeholders की शुद्धता महत्वपूर्ण होती है। OpenAI पिछड़ी संगतता के लिए डिफ़ॉल्ट बना रहता है।

## इस स्क्रिप्ट का उपयोग करने वाले प्रोजेक्ट

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX  
Email : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. देखें [LICENSE](LICENSE).

**यह दस्तावेज़ fr संस्करण से hi भाषा में gpt-5.4-mini मॉडल का उपयोग करके अनुवादित किया गया है। अनुवाद प्रक्रिया के बारे में अधिक जानकारी के लिए, https://github.com/jls42/ai-powered-markdown-translator देखें**
