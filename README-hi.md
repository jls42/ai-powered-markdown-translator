# AI-संचालित Markdown अनुवादक

🌍 [अंग्रेज़ी](README-en.md) | [स्पेनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

Markdown फ़ाइलों के लिए अनुवादक जो **OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करता है।

यह Python स्क्रिप्ट स्रोत भाषा से लक्षित भाषा में Markdown फ़ाइलों का अनुवाद करती है, जबकि स्वरूपण, कोड ब्लॉक्स और फ्रंट मैटर मेटाडेटा को संरक्षित रखती है।

## मुख्य सुविधाएँ

- **मल्टी-प्रोवाइडर**: 4 APIs का समर्थन (OpenAI, Mistral, Claude, Gemini)
- **मॉडल 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **इकॉनॉमिक मोड**: तेज़ और सस्ता मॉडल उपयोग करने के लिए विकल्प `--eco`
- **एकल फ़ाइल**: एक फ़ाइल अनुवादने के लिए विकल्प `--file`
- **स्मार्ट सेगमेंटेशन**: मॉडल के अनुसार टोकन सीमाओं के साथ लंबे टेक्स्ट का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक्स और inline कोड (`` `...` ``) संरक्षित रहते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए विकल्प `--keep_filename`
- **.env विन्यास**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## इंस्टॉलेशन

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## विन्यास

प्रोजेक्ट की रूट में `.env` फ़ाइल बनाएं या पर्यावरण चर सेट करें :

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

### एक फ़ाइल अनुवादें

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### एक डायरेक्टरी अनुवादें

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

### इकॉर्मिक मोड

तेज़ और सस्ते मॉडल का उपयोग करता है (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| Option | Description |
|--------|-------------|
| `--file` | अनुवाद करने के लिए एकल Markdown फ़ाइल |
| `--source_dir` | Markdown फ़ाइलें शामिल स्रोत निर्देशिका |
| `--target_dir` | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका |
| `--source_lang` | स्रोत भाषा (डिफ़ॉल्ट: `fr`) |
| `--target_lang` | लक्ष्य भाषा (डिफ़ॉल्ट: `en`) |
| `--model` | उपयोग करने के लिए विशिष्ट मॉडल |
| `--eco` | इकॉनॉमिक मॉडल का उपयोग करें |
| `--use_mistral` | Mistral AI API का उपयोग करें |
| `--use_claude` | Claude API का उपयोग करें |
| `--use_gemini` | Gemini API का उपयोग करें |
| `--force` | पुनः अनुवाद को मजबूर करें |
| `--keep_filename` | मूल फ़ाइल नाम रखें |
| `--add_translation_note` | अनुवाद नोट जोड़ें |
| `--include_model` | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें |

### डिफ़ॉल्ट मॉडल (2026)

| प्रदाता | गुणवत्ता (डिफ़ॉल्ट) | इकॉनॉमिक (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - व्यक्तिगत ब्लॉग जो 15 भाषाओं में अनूदित है 

## लेखक

Julien LE SAUX  
ईमेल : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE संस्करण 3. देखें [लाइसेंस](LICENSE).

**यह दस्तावेज़ fr संस्करण से hi भाषा में gpt-5-mini मॉडल का उपयोग करके अनूदित किया गया है। अनुवाद प्रक्रिया के बारे में अधिक जानकारी के लिए, देखें https://gitlab.com/jls42/ai-powered-markdown-translator**

