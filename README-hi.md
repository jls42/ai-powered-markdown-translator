# AI-संचालित Markdown अनुवादक

🌍 [अंग्रेज़ी](README-en.md) | [स्पैनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

Markdown फ़ाइलों का अनुवादक जो **OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करता है।

यह Python स्क्रिप्ट Markdown फ़ाइलों को स्रोत भाषा से लक्ष्य भाषा में अनुवादित करती है, फॉर्मैटिंग, कोड ब्लॉक्स और फ्रंट मैटर मेटाडेटा को संरक्षित करते हुए।

## मुख्य विशेषताएँ

- **मल्टी-प्रोवाइडर**: 4 APIs का समर्थन (OpenAI, Mistral, Claude, Gemini)
- **मॉडल 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **किफायती मोड**: विकल्प `--eco` तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए
- **एकल फ़ाइल**: विकल्प `--file` एक ही फ़ाइल अनुवाद करने के लिए
- **स्मार्ट विभाजन**: लंबे टेक्स्ट्स के लिए मॉडल-विशिष्ट टोकन सीमा प्रबंधन
- **कोड का संरक्षण**: कोड ब्लॉक्स और इनलाइन कोड (`` `...` ``) संरक्षित रहते हैं
- **फ़ाइल नाम**: विकल्प `--keep_filename` मूल नाम बनाए रखने के लिए
- **.env कॉन्फ़िगरेशन**: `.env` फ़ाइल के लिए समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक अनुवाद नोट जोड़ने का विकल्प

## इंस्टॉलेशन

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## कॉन्फ़िगरेशन

प्रोजेक्ट की रूट में एक `.env` फ़ाइल बनाएं या पर्यावरण चर सेट करें:

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

### एक फ़ाइल अनुवाद करें

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### एक निर्देशिका अनुवाद करें

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

### किफायती मोड

तेज़ और सस्ते मॉडल का उपयोग करता है (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प | विवरण |
|--------|-------------|
| `--file` | अनुवाद के लिए एकल Markdown फ़ाइल |
| `--source_dir` | स्रोत निर्देशिका जिसमें Markdown फ़ाइलें हैं |
| `--target_dir` | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका |
| `--source_lang` | स्रोत भाषा (डिफ़ॉल्ट: `fr`) |
| `--target_lang` | लक्ष्य भाषा (डिफ़ॉल्ट: `en`) |
| `--model` | उपयोग करने के लिए विशिष्ट मॉडल |
| `--eco` | किफायती मॉडल का उपयोग करें |
| `--use_mistral` | Mistral AI API का उपयोग करें |
| `--use_claude` | Claude API का उपयोग करें |
| `--use_gemini` | Gemini API का उपयोग करें |
| `--force` | पुनः अनुवाद ज़बरदस्ती करें |
| `--keep_filename` | मूल फ़ाइल नाम रखें |
| `--add_translation_note` | अनुवाद नोट जोड़ें |
| `--include_model` | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें |

### डिफ़ॉल्ट मॉडल (2026)

| प्रदाता | गुणवत्ता (डिफ़ॉल्ट) | किफायती (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - व्यक्तिगत बहुभाषी ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX  
ईमेल : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE संस्करण 3. देखें [लाइसेंस](LICENSE).

**यह दस्तावेज़ fr संस्करण से hi भाषा में gpt-5-mini मॉडल का उपयोग करके अनुवादित किया गया है। अनुवाद प्रक्रिया के बारे में अधिक जानकारी के लिए, देखें https://gitlab.com/jls42/ai-powered-markdown-translator**

