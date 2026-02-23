# AI-संचालित Markdown अनुवादक

🌍 [फ़्रेंच](README.md) | [अंग्रेज़ी](README-en.md) | [स्पैनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिंदी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

Markdown फ़ाइलों का अनुवादक जो **OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करता है।

यह Python स्क्रिप्ट स्रोत भाषा से लक्ष्य भाषा में Markdown फ़ाइलों का अनुवाद करती है जबकि फॉर्मैटिंग, कोड ब्लॉक्स और front matter मेटाडेटा को संरक्षित रखती है।

## मुख्य विशेषताएँ

- **मल्टी-प्रोवाइडर**: 4 APIs का समर्थन (OpenAI, Mistral, Claude, Gemini)
- **2026 मॉडल**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **किफायती मोड**: विकल्प `--eco` तेज़ और सस्ते मॉडलों के उपयोग के लिए
- **एकल फ़ाइल**: विकल्प `--file` एक ही फ़ाइल का अनुवाद करने के लिए
- **स्मार्ट सेगमेंटेशन**: लंबे टेक्स्ट का प्रबंधन मॉडल द्वारा टोकन सीमाओं के साथ
- **कोड की सुरक्षा**: कोड ब्लॉक्स और inline कोड (`` `...` ``) संरक्षित रहते हैं
- **फ़ाइल नाम**: विकल्प `--keep_filename` मूल नाम बनाए रखने के लिए
- **न्यूज़ मोड**: विकल्प `--news` अंग्रेज़ी उद्धरणों को सुरक्षित रखता है और समाचार लेखों में भाषा-आधारित झंडों को संभालता है
- **.env कॉन्फ़िगरेशन**: API कीज़ के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक अनुवाद नोट जोड़ना

## इंस्टॉलेशन

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## कॉन्फ़िगरेशन

प्रोजेक्ट की रूट में `.env` फ़ाइल बनाएं या पर्यावरण चर सेट करें:

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

तेज़ और सस्ते मॉडलों (gpt-5-mini, claude-haiku, gemini-flash) का उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प | विवरण |
|--------|-------------|
| `--file` | अनुवाद करने के लिए एकल Markdown फ़ाइल |
| `--source_dir` | स्रोत निर्देशिका जिसमें Markdown फ़ाइलें हैं |
| `--target_dir` | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका |
| `--source_lang` | स्रोत भाषा (डिफ़ॉल्ट: `fr`) |
| `--target_lang` | लक्ष्य भाषा (डिफ़ॉल्ट: `en`) |
| `--model` | उपयोग करने के लिए विशिष्ट मॉडल |
| `--eco` | किफायती मॉडल का उपयोग करें |
| `--use_mistral` | Mistral AI API का उपयोग करें |
| `--use_claude` | Claude API का उपयोग करें |
| `--use_gemini` | Gemini API का उपयोग करें |
| `--force` | पुनः-अनुवाद को मजबूर करें |
| `--keep_filename` | मूल फ़ाइल नाम बनाए रखें |
| `--news` | न्यूज़ मोड: अंग्रेज़ी उद्धरणों को सुरक्षित रखें, भाषा-आधारित झंडे संभालें |
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

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX
Email : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. देखें [लाइसेंस](LICENSE).

**यह दस्तावेज़ fr संस्करण से hi भाषा में gpt-5-mini मॉडल का उपयोग करके अनुवादित किया गया है। अनुवाद प्रक्रिया के बारे में अधिक जानकारी के लिए, https://gitlab.com/jls42/ai-powered-markdown-translator देखें**

