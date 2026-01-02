# एआई-संचालित मार्कडाउन अनुवादक

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइल अनुवादक।

यह Python स्क्रिप्ट स्रोत भाषा से लक्ष्य भाषा में Markdown फ़ाइलों का अनुवाद करती है, साथ ही फ़ॉर्मेटिंग, कोड ब्लॉक्स और फ्रंट मैटर मेटाडेटा को संरक्षित रखती है।

## मुख्य विशेषताएँ

- **मल्टी-प्रोवाइडर**: 4 API का समर्थन (OpenAI, Mistral, Claude, Gemini)
- **2026 मॉडल**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **आर्थिक मोड**: तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: केवल एक फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **स्मार्ट विभाजन**: प्रति मॉडल टोकन सीमाओं के साथ लंबे पाठ का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक्स का अनुवाद नहीं किया जाता
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## स्थापना

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## कॉन्फ़िगरेशन

जिस API का आप उपयोग करना चाहते हैं, उसके लिए पर्यावरण चर सेट करें :

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## उपयोग

### एकल फ़ाइल का अनुवाद

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### एक निर्देशिका का अनुवाद

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

### आर्थिक मोड

तेज़ और कम लागत वाले मॉडल उपयोग करता है (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प | विवरण |
|--------|-------------|
| `--file` | अनुवाद के लिए एकल Markdown फ़ाइल |
| `--source_dir` | Markdown फ़ाइलें युक्त स्रोत निर्देशिका |
| `--target_dir` | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका |
| `--source_lang` | स्रोत भाषा (डिफ़ॉल्ट: `fr`) |
| `--target_lang` | लक्ष्य भाषा (डिफ़ॉल्ट: `en`) |
| `--model` | उपयोग करने के लिए विशिष्ट मॉडल |
| `--eco` | आर्थिक मॉडल का उपयोग करें |
| `--use_mistral` | Mistral AI API का उपयोग करें |
| `--use_claude` | Claude API का उपयोग करें |
| `--use_gemini` | Gemini API का उपयोग करें |
| `--force` | पुनः अनुवाद को बाध्य करें |
| `--add_translation_note` | अनुवाद नोट जोड़ें |

### डिफ़ॉल्ट मॉडल (2026)

| प्रोवाइडर | गुणवत्ता (डिफ़ॉल्ट) | आर्थिक (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## लेखक

Julien LE SAUX
ईमेल : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE संस्करण 3. [LICENSE](LICENSE) देखें.