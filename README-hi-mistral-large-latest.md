# AI-Powered Markdown Translator with OpenAI, Mistral AI and Claude d'Anthropic

यह प्रोजेक्ट एक उन्नत पायथन स्क्रिप्ट है जो OpenAI, Mistral AI या Claude d'Anthropic के API का उपयोग करके स्रोत भाषा से लक्ष्य भाषा में मार्कडाउन फाइलों का अनुवाद करता है। यह लचीला और आसानी से उपयोग किया जा सकने वाला डिजाइन किया गया है, जिसमें अतिरिक्त विकल्प शामिल हैं जैसे अनुवाद नोट जोड़ना, आउटपुट फाइलों का बेहतर प्रबंधन, मौजूदा फाइलों का पता लगाना, और कई भाषाओं और अनुवाद मॉडल्स का समर्थन।

एक डेमो और विस्तृत व्याख्याओं के लिए, [jls42.org](https://jls42.org/) पर जाएं या अनुवादित संस्करण में: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) और [jls42.org 中文](https://jls42.org/traductions_zh/).

## मुख्य विशेषताएँ

- **AI-Powered अनुवाद**: OpenAI, Mistral AI या Claude d'Anthropic के साथ आपके दस्तावेजों के लिए नवीनतम AI तकनीकों का उपयोग करें।
- **मल्टीलिंग्वल सपोर्ट**: विभिन्न भाषा मॉडल्स के साथ अपने दस्तावेजों का कई भाषाओं में अनुवाद करें।
- **इंटेलिजेंट सेगमेंटेशन**: स्वचालित सेगमेंटेशन के माध्यम से लंबे टेक्स्ट का प्रबंधन करें।
- **अनुवाद नोट**: प्रक्रिया के बारे में पाठकों को सूचित करने के लिए अनुवादित सामग्री में स्वचालित रूप से एक अनुवाद नोट जोड़ें।
- **बेहतर आउटपुट फाइल प्रबंधन**: अनुवाद शुरू करने से पहले देखें कि कोई अनुवाद पहले से मौजूद है या नहीं।
- **बेहतर मौजूदा फाइल डिटेक्शन**: मूल फाइल के बेस नाम और लक्ष्य भाषा के अनुसार मेल खाती फाइलों की खोज करें।
- **लचीला और एक्सटेंसिबल**: कोड नयी सुविधाओं को जोड़ने की सुविधा के लिए संरचित है।

## प्रारंभिक आवश्यकताएँ

- पायथन 3.6 या उससे नई संस्करण।
- OpenAI, Mistral AI या Claude d'Anthropic के लिए एक वैध API कुंजी।

## इंस्टॉलेशन

1. गिट डिपॉजिटरी को क्लोन करें:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. आवश्यक निर्भरताएँ इंस्टॉल करें:
```
pip install -r requirements.txt
```

## कॉन्फ़िगरेशन

अपने वातावरण को आवश्यक API कुंजियों के लिए एन्वायरमेंट वेरिएबल्स सेट करके कॉन्फ़िगर करें:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='आपकी-ओपनएआई-एपीआई-कुंजी'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='आपकी-मिस्ट्रल-एपीआई-कुंजी'
    ```
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='आपकी-एंथ्रोपिक-एपीआई-कुंजी'
    ```

## उपयोग

स्क्रिप्ट अनुवाद प्रक्रिया को अनुकूलित करने के लिए कई विकल्प प्रदान करता है:

### सामान्य विकल्प

- `--source_dir` : अनुवाद करने के लिए मार्कडाउन फाइलों वाला डायरेक्टरी।
- `--target_dir` : अनुवादित फाइलों के लिए आउटपुट डायरेक्टरी।
- `--model` : उपयोग करने के लिए गपट अनुवाद मॉडल। डिफ़ॉल्ट मॉडल चयनित API पर निर्भर करता है।
- `--source_lang` : दस्तावेजों की स्रोत भाषा। विशेष रूप से अनुवाद नोट्स जोड़ने के लिए महत्वपूर्ण।
- `--target_lang` : अनुवाद के लिए लक्ष्य भाषा। डिफ़ॉल्ट में अंग्रेजी है।
- `--force` : अनुवाद पहले से मौजूद होने पर भी अनुवाद करें।

### API विशिष्ट विकल्प

- `--use_mistral` : अनुवाद के लिए Mistral AI API का उपयोग करें।
- `--use_claude` : अनुवाद के लिए Claude d'Anthropic API का उपयोग करें।
- `--add_translation_note` : अनुवादित सामग्री में एक अनुवाद नोट जोड़ें, जिसमें प्रयुक्त विधि और उपकरण दिखाए गए हैं।

### उपयोग के उदाहरण

- ओपनएआई के साथ फ्रेंच से अंग्रेजी में अनुवाद करें, एक अनुवाद नोट जोड़ें:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AI के साथ फ्रेंच से स्पेनिश में अनुवाद करें, बिना अनुवाद नोट के:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## लेखक

Julien LE SAUX
ईमेल : contact@jls42.org

## लाइसेंस

यह प्रोजेक्ट GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 के तहत लाइसेंस प्राप्त है। अधिक विवरण के लिए फ़ाइल [LICENSE](LICENSE) देखें।

**Ce document a été traduit de la version fr vers la langue hi en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**

