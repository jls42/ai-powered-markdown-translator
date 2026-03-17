# एआई-संचालित Markdown अनुवादक

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइल अनुवादक।

यह Python स्क्रिप्ट Markdown फ़ाइलों को स्रोत भाषा से लक्ष्य भाषा में अनुवाद करती है, जबकि फ़ॉर्मेटिंग, कोड ब्लॉक्स और फ्रंट मैटर मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **Multi-Provider**: 4 APIs (OpenAI, Mistral, Claude, Gemini) का समर्थन
- **2026 मॉडल**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **किफायती मोड**: तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: एक ही फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **स्मार्ट सेगमेंटेशन**: मॉडल-विशिष्ट टोकन सीमाओं के साथ लंबे पाठ का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक्स और इनलाइन कोड (`` `...` ``) सुरक्षित रहते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **समाचार मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों की रक्षा करने और झंडों को संभालने के लिए `--news` विकल्प
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## स्थापना

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## कॉन्फ़िगरेशन

प्रोजेक्ट की रूट में `.env` फ़ाइल बनाएँ या पर्यावरण चर निर्धारित करें :

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
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### किफायती मोड

तेज़ और कम लागत वाले मॉडल (gpt-5-mini, claude-haiku, gemini-flash) का उपयोग करता है :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प | विवरण |
|--------|-------------|
| `--file` | अनुवाद करने के लिए एकल Markdown फ़ाइल |
| `--source_dir` | Markdown फ़ाइलों वाली स्रोत निर्देशिका |
| `--target_dir` | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका |
| `--source_lang` | स्रोत भाषा (डिफ़ॉल्ट: `fr`) |
| `--target_lang` | लक्ष्य भाषा (डिफ़ॉल्ट: `en`) |
| `--model` | उपयोग करने के लिए विशिष्ट मॉडल |
| `--eco` | किफायती मॉडल का उपयोग करें |
| `--use_mistral` | Mistral AI API का उपयोग करें |
| `--use_claude` | Claude API का उपयोग करें |
| `--use_gemini` | Gemini API का उपयोग करें |
| `--force` | पुनः-अनुवाद बाध्य करें |
| `--keep_filename` | मूल फ़ाइल नाम बनाए रखें |
| `--news` | समाचार मोड: EN उद्धरणों की रक्षा करता है, भाषा के अनुसार झंडों को संभालता है |
| `--add_translation_note` | अनुवाद नोट जोड़ें |
| `--include_model` | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें |

### डिफ़ॉल्ट मॉडल (2026)

| Provider | गुणवत्ता (डिफ़ॉल्ट) | किफायती (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX
Email : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. देखें [LICENSE](LICENSE).