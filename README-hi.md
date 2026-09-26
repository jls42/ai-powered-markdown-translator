# AI-पावर्ड Markdown अनुवादक

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 कोड गुणवत्ता</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="क्वालिटी गेट स्थिति"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="सुरक्षा रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="विश्वसनीयता रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="रख-रखाव रेटिंग"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="कवरेज"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="कमजोरियां"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="बग्स"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="कोड स्मेल्स"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="डुप्लिकेट की गई लाइनें (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="तकनीकी ऋण"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="कोड की लाइनें"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy बैज"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

संरचना को सुरक्षित रखते हुए Markdown फ़ाइलों का एक भाषा से दूसरी भाषा में अनुवाद करता है: कोड ब्लॉक, इनलाइन कोड, URL, एंकर, तालिकाएं और front matter। किसी मॉडल को कॉल करने के दस तरीके — पाँच API, बिना उपयोग-आधारित बिलिंग वाले तीन सब्सक्रिप्शन, दो राउटर — और प्रत्येक मॉडल वास्तव में क्या सुरक्षित रखता है, इसका एक प्रकाशित माप।

## संक्षेप में

- **दस प्रोवाइडर पथ**: OpenAI, Mistral, Claude, Gemini और Grok API; बिना उपयोग-आधारित बिलिंग वाले ChatGPT (Codex), Grok और Google (Antigravity) सब्सक्रिप्शन; OpenCode (ओपन सोर्स, मुफ़्त या स्थानीय) और OpenRouter (400 से अधिक मॉडल) राउटर।
- **खोए हुए टोकन के कारण कुछ भी गलत नहीं**: कॉल से पहले कोड ब्लॉक, इनलाइन कोड, URL, एंकर और उद्धरणों को टोकन से बदल दिया जाता है और वापसी पर सत्यापित किया जाता है। यदि कोई एक भी गायब है, तो फ़ाइल नहीं लिखी जाती है।
- **लंबे दस्तावेज़**: मॉडल की विंडो के अनुसार विभाजन।
- **`--news` मोड**: निगरानी लेखों के लिए, अंग्रेजी उद्धरण सुरक्षित और भाषा के अनुसार झंडे प्रबंधित।
- **`--eco` मोड**: तेज़ और सस्ते मॉडल।
- वैकल्पिक **अनुवाद नोट**, ऊपर, नीचे या दोनों जगह।

## इंस्टॉलेशन

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 या नया। रिपॉजिटरी से इंस्टॉल करने के लिए, [योगदान दें](#योगदान-करें) देखें।

## कॉन्फ़िगरेशन

कुंजियाँ तीन स्थानों से पढ़ी जाती हैं, सर्वोच्च प्राथमिकता से न्यूनतम तक; प्रत्येक केवल उसी को भरता है जो पिछला खाली छोड़ देता है।

|     | कहाँ                                          | किसलिए                                |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | एनवायरनमेंट वेरिएबल्स                         | CI, कंटेनर, तदर्थ अपवाद               |
| 2   | वर्तमान (या पैरेंट) डायरेक्टरी का `.env` | किसी प्रोजेक्ट के लिए विशिष्ट कुंजी   |
| 3   | `~/.config/aipmt/.env`                                 | एक बार इंस्टॉल किया, हर जगह मान्य    |

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

`GOOGLE_API_KEY` के स्थान पर `GEMINI_API_KEY` स्वीकार किया जाता है। उपयोगकर्ता फ़ाइल Windows पर `XDG_CONFIG_HOME` (केवल निरपेक्ष पथ) और `%APPDATA%` का अनुसरण करती है। बिना किसी कुंजी के, कमांड तीनों स्थानों को सूचीबद्ध करता है।

**किसी प्रोजेक्ट का `.env` न तो कॉल को पुनर्निर्देशित कर सकता है और न ही निष्पादित प्रोग्राम चुन सकता है।** यह केवल कुंजियाँ प्रदान करता है, कभी कोई गंतव्य या बाइनरी नहीं: `_BASE_URL`, `_API_BASE`, `_ENDPOINT` या `_BIN` (`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, प्रॉक्सी (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), प्रमाणपत्र स्टोर (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) और `XDG_CONFIG_HOME` / `APPDATA` में किसी भी चर को एक चेतावनी के साथ अनदेखा कर दिया जाता है। एक क्लोन की गई रिपॉजिटरी को आपकी कुंजी को हाईजैक करने या पहले अनुवाद पर आपको अपना स्वयं का प्रोग्राम चलाने के लिए मजबूर करने में सक्षम नहीं होना चाहिए। यह फ़ाइल बिना इंटरपोलेशन के भी पढ़ी जाती है: `NOM=${OPENAI_API_KEY}` वहाँ कुंजी को कॉपी नहीं करता है। इन चरों को एनवायरनमेंट में या `~/.config/aipmt/.env` में सेट करें।

वैकल्पिक चर: `XAI_BASE_URL` (डिफ़ॉल्ट `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (प्रति कॉल सेकंड, डिफ़ॉल्ट 900), `CODEX_BIN`, `CODEX_TIMEOUT` (डिफ़ॉल्ट 600), `GROK_BIN`, `GROK_HOME` (डिफ़ॉल्ट `~/.grok`), `GROK_TIMEOUT` (डिफ़ॉल्ट 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (डिफ़ॉल्ट 900), `OPENCODE_BIN`, `OPENCODE_TIMEOUT` (डिफ़ॉल्ट 600), `OPENROUTER_BASE_URL` (`https://` आवश्यक), `OPENROUTER_TIMEOUT` (डिफ़ॉल्ट 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (डिफ़ॉल्ट 30)। प्रत्येक का विवरण उसके प्रोवाइडर वाले अनुभाग में दिया गया है।

## शुरुआत करना

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

स्पेनिश में अनुवादित `document.md` `--target_dir` में `document-es.md` देता है; `--include_model` के साथ, `document-es-gpt-5.6-terra.md`। एक्सटेंशन हमेशा `.md` बन जाता है — `article.mdx` से `article-en.md` मिलता है — सिवाय `--keep_filename` के, जो मूल नाम को बनाए रखता है। पहले से मौजूद अनुवाद को `--force` के बिना छोड़ दिया जाता है।

एग्जिट कोड: `0` यदि सब कुछ सफल रहा या छोड़ दिया गया, `1` यदि कोई फ़ाइल विफल रही (मानक त्रुटि पर सूची), `2` यदि कॉन्फ़िगरेशन में कोई समस्या है। विफल फ़ाइल कभी नहीं लिखी जाती है, भले ही लेखन स्वयं विफल हो जाए: सामग्री पहले अलग से लिखी जाती है और फिर उसका नाम बदला जाता है। बस पुनः चलाना पर्याप्त है।

## कौन सा मॉडल चुनें

दो वास्तविक दस्तावेज़ों पर मापा गया, जिन्हें प्रत्येक मॉडल द्वारा उन्हीं चौदह भाषाओं में अनुवादित किया गया। **यह संख्या चौदह में से उन भाषाओं की संख्या है जहाँ अनुवाद लिखा गया है और स्रोत से कुछ भी भिन्न नहीं है।**

| मॉडल                 | इस तक कैसे पहुँचें                | सघन निगरानी लेख         | यह README    | क्या भिन्न है, और कितनी भाषाओं पर                                                                                                     |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google सब्सक्रिप्शन (Antigravity) | ✅ 14/14                | ✅ 14/14     | कुछ भी नहीं, दोनों में से किसी भी दस्तावेज़ पर                                                                                        |
| **Gemini 3.7 Flash** | Google API कुंजी                  | ✅ 14/14                | ⚠️ 13/14     | 14 में से 1 भाषा: एक अतिरिक्त बोल्ड शब्द (ja)                                                                                         |
| **Gemini 3.7 Flash** | Google सब्सक्रिप्शन (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 14 में से 1 भाषा: एक कम बोल्ड शब्द (ko)                                                                                               |
| **GPT-5.6 Sol**      | ChatGPT सब्सक्रिप्शन, या OpenAI कुंजी | ✅ 14/14            | ⚠️ 12/14     | 14 में से 2 भाषाएँ: एक कम बोल्ड शब्द (ar, ja)                                                                                         |
| **GLM-5.2**          | OpenRouter कुंजी                  | ✅ 14/14                | ⚠️ 11/14     | 14 में से 3 भाषाएँ: एक कम बोल्ड शब्द (hi, ja, ko)                                                                                     |
| Claude Sonnet 5      | Anthropic API कुंजी               | ⚠️ 11/14                | ⚠️ 12/14     | लेख पर 3 भाषाएँ: एक अतिरिक्त कोड ब्लॉक दिखा (es, de, hi); इस README पर 2: बिना मार्कअप वाला एक लिंक (sv), एक बोल्ड शब्द (zh)           |
| Qwen 3.7 Flash       | OpenRouter कुंजी                  | ❌ 8/14                 | ⚠️ 10/14     | लेख पर 1 भाषा अस्वीकृत, 5 अन्य में अंतर; इस README पर, लगभग चालीस शब्द `code` में बदल दिए गए (ar)                              |
| Grok 4.6             | Grok सब्सक्रिप्शन                 | ❌ 8/14                 | रेट नहीं किया गया | इनलाइन कोड और URL वापस न मिलने के कारण 14 में से 5 भाषाएँ अस्वीकृत; डच में हर चीज़ में विचलन                                          |
| GPT-OSS 20B          | स्थानीय मॉडल (Ollama)             | ❌ 7/14                 | पुनः नहीं मापा गया | 14 में से 4 भाषाएँ अस्वीकृत: मॉडल ने इनमें फ़्रेंच अंश छोड़ दिए थे, सुरक्षा जांच ने उन्हें रोक दिया                                     |
| MiMo v2.5 (मुफ़्त)   | OpenCode Zen, बिना खाते के        | ❌ 11/14                | पुनः नहीं मापा गया | 1 भाषा अस्वीकृत; पोलिश में एक पूरा अनुभाग खो गया                                                                                      |
| Mistral Large        | Mistral API कुंजी                 | ❌ 5/14                 | ❌ 1/14      | **एक पूरा अनुभाग गायब हो जाता है**: लेख पर 1 भाषा (hi), इस README पर 3 (ar, hi, ko) — और लेख पर 3 भाषाएँ अस्वीकृत                     |
| DeepSeek V4 Flash    | OpenRouter कुंजी                  | ❌ 3/14                 | पुनः नहीं मापा गया | 14 में से 10 भाषाएँ अस्वीकृत; 37 मिनट प्रति भाषा                                                                                      |

|     | प्रतीक का अर्थ                                                                                                                                                                                        |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | चौदह भाषाओं का अनुवाद किया गया, और स्रोत से कुछ भी भिन्न नहीं है                                                                                                                                      |
| ⚠️  | चौदह भाषाओं का अनुवाद किया गया; जो भिन्न है वह **मार्कअप** है — एक बोल्ड शब्द, एक `code`, कोष्ठक खोने वाला एक लिंक। कोई पाठ, कोई URL, कोई कोड ब्लॉक, कोई अनुभाग गायब नहीं है                 |
| ❌  | कम से कम एक भाषा का अनुवाद नहीं किया जा सका — फ़ाइल अस्वीकृत है, लिखी नहीं गई — **या** लिखी गई फ़ाइल में सामग्री गायब है                                                                              |

मुख्य बातें:

- **अस्वीकृत अनुवाद कोई दूषित अनुवाद नहीं होता।** जब वापसी पर कोई टोकन
  गायब होता है, तो फ़ाइल नहीं लिखी जाती है और भाषा को अस्वीकृत माना जाता है।
  लेख पर Grok के साथ यही होता है: पाँच गैर-लैटिन लिपियों में,
  पहले ही खंड में चार इनलाइन कोड और तीन URL खो गए।
- **यह सुरक्षा जाल शीर्षकों, तालिकाओं, front matter या टेक्स्ट को कवर नहीं करता है।**
  एक मॉडल जो किसी अनुभाग को हटा देता है, वह ऐसी फ़ाइल लौटाता है जिसे टूल बिना
  किसी रोकटोक के लिख देता है — Mistral के मामले में ऐसा ही है। ये तत्व
  टोकन द्वारा प्रतिस्थापन योग्य नहीं हैं, और वर्तमान सुरक्षा जाँचें इन्हें नियंत्रित नहीं करती हैं;
  `scripts/compare_structure.py` किसी खोए हुए अनुभाग का पता लगाता है, लेकिन बाद में।
- **इस README पर Grok की कोई रेटिंग नहीं है**: इसका CLI सत्र बारह भाषाओं
  के बाद समाप्त हो गया, जिनमें से ग्यारह बिना किसी अंतर के थीं। एक बाधित अभियान को रेट नहीं किया जाता है।
- **दस्तावेज़ का घनत्व भाषा से अधिक मायने रखता है।** Grok सामान्य README पर
  सही काम करता है और लिंक से भरे लेख पर विफल हो जाता है, जिसमें डच भाषा भी शामिल है।

तिथियाँ और दस्तावेज़: "यह README" कॉलम को 9 सितंबर 2026 को इस फ़ाइल के एक स्थिर संशोधन (785 लाइनें, 285 इनलाइन कोड, 89 तालिका लाइनें) पर मापा गया था, जिसमें तब से बदलाव किए गए हैं — सिवाय दो Antigravity पंक्तियों के, जिन्हें 26 सितंबर को 1.14.0 के साथ प्रकाशित छोटे संशोधन (600 लाइनें, 257 इनलाइन कोड, 85 तालिका लाइनें) पर मापा गया था। "सघन निगरानी लेख" कॉलम 589 लाइनों के एक लेख पर 4 और 5 सितंबर के अभियान से आता है, सिवाय Grok पंक्ति के, जिसे 9 सितंबर को उसी निगरानी के दूसरे संस्करण पर दोबारा मापा गया था, और दो Antigravity पंक्तियों के, जिन्हें 26 सितंबर को उसी लेख पर मापा गया था।
पूर्ण तालिकाएं, अवधि और प्रोटोकॉल [विस्तृत माप](#विस्तृत-माप) में हैं।

## सभी विकल्प

| विकल्प                   | विवरण                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | अनुवाद के लिए एकल Markdown फ़ाइल (`--source_dir` का विकल्प)                                                   |
| `--source_dir`           | Markdown फ़ाइलों वाली स्रोत डायरेक्टरी (डिफ़ॉल्ट: `content/posts`)                                             |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट डायरेक्टरी (डिफ़ॉल्ट: `traductions_en`)                                          |
| `--source_lang`           | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                                                         |
| `--target_lang`           | लक्षित भाषा (डिफ़ॉल्ट: `en`)                                                                        |
| `--model`           | उपयोग करने के लिए विशिष्ट मॉडल                                                                                |
| `--eco`           | किफ़ायती मॉडलों का उपयोग करें                                                                                 |
| `--use_mistral`           | Mistral AI API का उपयोग करें                                                                                  |
| `--use_claude`           | Claude API का उपयोग करें                                                                                      |
| `--use_gemini`           | Gemini API का उपयोग करें                                                                                      |
| `--use_grok`           | xAI (Grok) API का उपयोग करें — `XAI_API_KEY` की आवश्यकता है                                                   |
| `--use_codex`           | ChatGPT सब्सक्रिप्शन कोटा पर Codex CLI का उपयोग करें                                                          |
| `--use_grok_cli`           | Grok सब्सक्रिप्शन कोटा पर Grok CLI का उपयोग करें                                                              |
| `--use_antigravity`           | Google AI Pro या Ultra सब्सक्रिप्शन कोटा पर Antigravity CLI (`agy`) का उपयोग करें                     |
| `--use_opencode`           | OpenCode में कॉन्फ़िगर किए गए प्रदाता के लिए OpenCode (ओपन सोर्स) का उपयोग करें; `--model provider/modèle` की आवश्यकता है |
| `--use_openrouter`           | OpenRouter का उपयोग करें — `OPENROUTER_API_KEY` और `--model fournisseur/modèle` की आवश्यकता है                                    |
| `--force`           | पुन: अनुवाद के लिए बाध्य करें                                                                                 |
| `--keep_filename`           | मूल फ़ाइल नाम बनाए रखें                                                                                        |
| `--news`           | समाचार मोड: EN उद्धरणों को सुरक्षित रखता है, भाषा के अनुसार झंडों को प्रबंधित करता है                         |
| `--add_translation_note`           | एक अनुवाद नोट जोड़ें                                                                                          |
| `--note_position`           | नोट की स्थिति: `top`, `bottom` (डिफ़ॉल्ट), या `both`                                   |
| `--note_format`           | नोट का प्रारूप: `legacy` (डिफ़ॉल्ट, बोल्ड पैराग्राफ) या `marker`                                  |
| `--include_model`          | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें                                                                       |
| `--reasoning_effort`          | GPT-5.x रीज़निंग प्रयास: `none`/`low`/`medium`/`high`/`xhigh`     |

नौ `--use_*` फ़्लैग परस्पर अनन्य हैं: किन्हीं दो को संयोजित करना अस्वीकृत है।

## प्रोवाइडर

### API द्वारा: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` प्रत्येक प्रदाता के किफायती स्तर पर स्विच करता है।

| प्रदाता     | गुणवत्ता (डिफ़ॉल्ट)                                      | किफायती (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (`--model` के ज़रिए `terra` और `luna` भी) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` अनिवार्य                 | वही — `--eco` का कोई प्रभाव नहीं |
| OpenRouter  | `--model fournisseur/modèle` अनिवार्य              | वही — `--eco` का कोई प्रभाव नहीं |

### ChatGPT सब्सक्रिप्शन पर: `--use_codex`

यह आधिकारिक Codex CLI को नियंत्रित करता है: अनुवाद ChatGPT सब्सक्रिप्शन के कोटा से काटा जाता है, बिना किसी API कुंजी या उपयोग-आधारित बिलिंग के।

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- बाइनरी को `CODEX_BIN`, फिर `PATH`, और उसके बाद `openai-codex-cli-bin` पैकेज में खोजा जाता है। `~/.codex/auth.json` को कभी नहीं पढ़ा जाता है।
- `OPENAI_API_KEY` और `CODEX_API_KEY` को सब-प्रोसेस के परिवेश से हटा दिया जाता है: किसी कुंजी के मौजूद होने पर भी वह कभी API पर स्विच नहीं करता।
- प्रत्येक सेगमेंट की लागत 5-घंटे की विंडो में से कम से कम एक "मैसेज" होती है — यदि इसका सत्यापन विफल हो जाता है और इसे पुनः आज़माया जाता है, तो दो मैसेज। OpenAI एक अनुमान के तौर पर Plus प्लान पर `gpt-5.6-luna` (`--eco`) के लिए 250-2,000 मैसेज/5 घंटे और `gpt-5.6-sol` के लिए 10-100 मैसेज की घोषणा करता है।
- `--model gpt-5.6-terra` और `--model gpt-5.6-luna` भी सब्सक्रिप्शन के ज़रिए चलते हैं। एक ऐसा मॉडल जिस पर खाते का अधिकार नहीं है, वह 400 "model is not supported when using Codex with a ChatGPT account" लौटाता है।
- API की तुलना में धीमा, और दस्तावेज़ के साथ यह अंतर बढ़ता जाता है: इस README पर, `gpt-5.6-sol` के साथ प्रति भाषा माध्यिका 6 मिनट 46 सेकंड, जबकि `gemini-3.7-flash` के लिए 36 सेकंड।
- CI में अस्वीकृत (`CI` या `GITHUB_ACTIONS` निर्धारित होने पर): सब्सक्रिप्शन एक व्यक्तिगत सत्र फ़ाइल द्वारा प्रमाणित होता है, जिसका किसी साझा रनर पर कोई काम नहीं है।
- वेरिएबल्स: `CODEX_BIN`, `CODEX_TIMEOUT` (प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 600)।

### Grok सब्सक्रिप्शन पर: `--use_grok_cli`

SuperGrok या X Premium+ सब्सक्रिप्शन पर, आधिकारिक Grok Build CLI के साथ यही सिद्धांत लागू होता है।

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex की तुलना में कमज़ोर कन्फ़ाइनमेंट।** Grok का OS सैंडबॉक्स कई हालिया Linux मशीनों (AppArmor, कंटेनर रनटाइम सॉकेट्स) पर लागू नहीं होता है, और जो प्रोफ़ाइल लागू नहीं हो पाती है वह चुपचाप बिना कन्फ़ाइनमेंट के शुरू हो जाती है। इसलिए स्क्रिप्ट डिफ़ॉल्ट रूप से किसी प्रोफ़ाइल का अनुरोध नहीं करती है, इसकी घोषणा करती है, और CLI के `--deny` नियमों पर निर्भर करती है, जिसमें कैच-ऑल `*` शामिल है — एकमात्र ऐसी परत जो बिना बताए सुरक्षा हटाने के बजाय शुरू होने से मना कर देती है। `GROK_TRANSLATE_SANDBOX=read-only` के लिए OS सैंडबॉक्स आवश्यक है, और यदि मशीन इसे पूरा करने में असमर्थ है तो स्टार्टअप विफल हो जाता है।
- कोटा साप्ताहिक होता है, जो Chat, Imagine और Voice के साथ साझा किया जाता है, और कोई भी कमांड इसे पढ़ने की अनुमति नहीं देता: कोई बैच बिना किसी संकेत के बातचीत के उपयोग को प्रभावित कर सकता है।
- वेरिएबल्स: `GROK_BIN`, `GROK_HOME` (CLI डायरेक्टरी, डिफ़ॉल्ट `~/.grok`), `GROK_TIMEOUT` (डिफ़ॉल्ट 900), `GROK_TRANSLATE_SANDBOX`।

### Google सब्सक्रिप्शन पर: `--use_antigravity`

Antigravity के आधिकारिक CLI, `agy` के साथ भी यही सिद्धांत है: जो लोग Google AI Pro या Ultra के लिए भुगतान करते हैं, उनके लिए अनुवाद टोकन के आधार पर बिल किए जाने के बजाय सब्सक्रिप्शन कोटे से काटा जाता है। इस कोटे तक पहुँचने का यह एकमात्र तरीका है: Gemini CLI 18 जून 2026 से इन खातों को सेवा नहीं देता है ([घोषणा](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)), और Antigravity SDK केवल एक API कुंजी या Google Cloud प्रोजेक्ट स्वीकार करता है।

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **कोई भी सशुल्क मार्ग खुला नहीं रहता।** agy को आपके परिवेश से केवल वेरिएबल्स की एक बंद सूची प्राप्त होती है — `PATH`, भाषा और समय क्षेत्र, टर्मिनल, पहचान, प्रॉक्सी और प्रमाणपत्र, सत्र बस — और कोई कुंजी नहीं: इसके कई वेरिएबल्स बिना कुछ प्रदर्शित किए कॉल को बदल देते हैं (मापा गया: एक दस्तावेज़ को तीसरे पक्ष के गेटवे पर भेजता है, दूसरा बिल किए गए Google Cloud प्रोजेक्ट पर), और एक अस्वीकृति सूची हर समीक्षा में कुछ न कुछ छोड़ देती थी। किसी भी सेगमेंट से पहले, `agy -p /config`, जिसमें कोई कोटा खर्च नहीं होता, को सशुल्क AI क्रेडिट अक्षम दिखाना चाहिए, बिना किसी API कुंजी या Google Cloud प्रोजेक्ट के — किसी सेटिंग का न होना अस्वीकृति माना जाता है —, अन्यथा कुछ भी अनुवादित नहीं होता है; इसके बाद प्रत्येक कॉल के लॉग को सब्सक्रिप्शन की पुष्टि करनी चाहिए (`authMethod=consumer`), अन्यथा प्रतिक्रिया अस्वीकार कर दी जाती है।
- **कन्फ़ाइनमेंट।** प्रत्येक कॉल बिना किसी टूल वाले अनुवाद एजेंट के साथ एक निजी और डिस्पोजेबल व्यक्तिगत डायरेक्टरी में चलती है: आपकी सेटिंग्स, नियम, प्लगइन्स, MCP सर्वर और agy हुक इसमें प्रवेश नहीं करते हैं, आपके इतिहास में कुछ भी नहीं जुड़ता है, और लॉगिन कीचेन में रहता है, जिसे aipmt कभी नहीं पढ़ता है। एजेंट न मिलने पर agy चुपचाप अपने कोडिंग एजेंट और उसके टूल्स पर वापस लौट जाता है: लॉग की एक पूरी पंक्ति को सही एजेंट की पुष्टि करनी चाहिए — इस संदेश को उद्धृत करने वाला दस्तावेज़ इसे प्रतिस्थापित नहीं करता —, अन्यथा अस्वीकृति।
- **प्लेटफ़ॉर्म**: Linux, एक ऐसे सत्र में जिसमें कीचेन हो (D-Bus सत्र बस, Secret Service); macOS स्वीकार किया जाता है, बिना उस पर मापे गए। Windows पर अस्वीकृत, जहाँ agy उन वेरिएबल्स को नहीं पढ़ता जो प्रत्येक कॉल को अलग करते हैं, और बिना सत्र बस वाले Linux पर — SSH सत्र, कंटेनर, सर्वर: agy वहाँ अपने टोकन को `~/.gemini` की एक फ़ाइल में संग्रहीत करता है, जिसे अलगाव छिपा देता है। कनेक्शन कोड के लिए एक मिनट प्रतीक्षा करने के बजाय, किसी भी शुरुआत से पहले ही कारण सहित अस्वीकृति आ जाती है।
- **मॉडल**: `agy models` के मॉडल। Gemini अपने नाम में प्रयास दर्शाते हैं (`gemini-3.8-flash-medium`…): बिना प्रत्यय वाला नाम कॉल से पहले ही अस्वीकार कर दिया जाता है, और `--reasoning_effort` का कोई प्रभाव नहीं होता है। डिफ़ॉल्ट रूप से `gemini-3.8-flash-medium`, और `--eco` में `gemini-3.7-flash-low`; इन्हें निर्धारित करने वाले अभियानों का वर्णन [विस्तृत माप](#विस्तृत-माप) में किया गया है। Claude और GPT-OSS का अपना कोटा होता है, जो काफी छोटा है: मापे गए प्रति कॉल 5-घंटे की विंडो का लगभग 1%, जबकि Flash में 0.05%।
- **कोटा**: प्रति समूह, एक 5-घंटे की विंडो और एक साप्ताहिक विंडो, टोकन लागत के अनुपात में। लेखक के खाते पर मापा गया: `gemini-3.8-flash-medium` में प्रति मिलियन स्रोत वर्णों पर 5-घंटे की विंडो के लगभग 16 अंक, `gemini-3.7-flash-medium` में 14 और कम प्रयास पर 7 से 8 — इसलिए 40,000 वर्णों वाले README की लागत आधे अंक से थोड़ी अधिक होती है। साप्ताहिक सीमा, जहाँ तक बात है, स्तर पर निर्भर करती है। पुनः प्रयास agy द्वारा पुनः प्रयास योग्य घोषित किए जाने के अनुसार होता है; ऐसा न होने पर, समाप्त हो चुकी विंडो को कभी भी पुनः प्रयास नहीं किया जाता: यह `/usage` द्वारा प्रदर्शित रीसेट तक प्रत्येक फ़ाइल को विफल कर देती है।
- **API से धीमा**: माप के सघन लेख पर, `gemini-3.8-flash-medium` में प्रति भाषा माध्यिका 3 मिनट 59 सेकंड और `gemini-3.7-flash-medium` में 3 मिनट 14 सेकंड, जबकि API के माध्यम से Gemini 3.7 Flash के लिए 1 मिनट 18 सेकंड।
- **रुकावट**: Ctrl-C, या बंद किया गया टर्मिनल, आपके कोटे पर agy को अपना काम पूरा करने देने के बजाय कमांड के साथ ही रोक देता है; यही बात Codex, Grok CLI और OpenCode पर भी लागू होती है। `nohup` के तहत अनुवाद जारी रहता है।
- CI में अस्वीकृत (`CI` या `GITHUB_ACTIONS` निर्धारित होने पर): लॉगिन एक व्यक्तिगत कीचेन में रहता है। रनर पर, `GOOGLE_API_KEY` के साथ `--use_gemini` का उपयोग करें।
- वेरिएबल्स: `AGY_BIN` (अन्यथा `PATH`, फिर `~/.local/bin/agy`), `AGY_TIMEOUT` (शुरुआती समय सहित प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 900)।

**उपयोग की शर्तें: यह आपका खाता है जो दांव पर है।** [Antigravity की शर्तें](https://antigravity.google/terms) (धारा 6) और इसके [FAQ](https://antigravity.google/docs/faq/) खाता निलंबन के जोखिम के तहत, Antigravity लॉगिन का उपयोग करके किसी तीसरे पक्ष के सॉफ़्टवेयर द्वारा सेवा तक पहुँचने पर रोक लगाते हैं — जिनमें Claude Code, OpenClaw और OpenCode का उल्लेख है। aipmt टोकन को न तो पढ़ता है और न ही दोबारा उपयोग करता है: यह आधिकारिक बाइनरी को उस [हेडलेस मोड](https://antigravity.google/docs/cli/headless/) में लॉन्च करता है जिसे Google स्क्रिप्ट और CI के लिए प्रलेखित करता है। Google के एक सदस्य ने अपने स्वयं के काम के लिए किसी स्थानीय स्क्रिप्ट से `agy -p` लॉन्च करने को "मानक" माना था ([आधिकारिक फ़ोरम, 25 सितंबर 2026, गैर-बाध्यकारी उत्तर](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)); कोई भी दस्तावेज़ इस जैसे वितरित टूल के मामले पर स्पष्ट निर्णय नहीं देता है।

**केवल सार्वजनिक दस्तावेज़।** उन्हीं शर्तों की धारा 5 के अनुसार, आदान-प्रदान — प्रॉम्प्ट, प्रतिक्रियाएँ, मेटाडेटा — का उपयोग Google के उत्पादों और मशीन लर्निंग को बेहतर बनाने के लिए किया जा सकता है और इंसानों द्वारा उनकी समीक्षा की जा सकती है, जिसमें सशुल्क सब्सक्रिप्शन भी शामिल है। इससे बाहर निकलने के लिए `enableTelemetry` सेटिंग का उपयोग होता है, जिसका प्रभाव अप्रलेखित है, जिसे aipmt सेट नहीं करता है; आपकी agy सेटिंग्स इसके अलगाव में साथ नहीं जाती हैं। इसमें से कोई भी गोपनीय सामग्री न गुजारें।

### अपनी पसंद के प्रदाता की ओर: `--use_opencode`

[OpenCode](https://opencode.ai) एक ओपन-सोर्स (MIT) कोड एजेंट है जो अपने भीतर कॉन्फ़िगर किए गए प्रदाताओं की ओर रूट करता है: API कुंजी, सब्सक्रिप्शन, OpenCode Zen गेटवे (बिना खाते के मुफ़्त मॉडल) या स्थानीय मॉडल। यहाँ दो तरीकों का शुरू से अंत तक परीक्षण और मापन किया गया: Zen और Ollama।

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` अनिवार्य है: इसके बिना, OpenCode एक मुफ़्त मॉडल पर वापस चला जाएगा जिसके आदान-प्रदान का उपयोग प्रशिक्षण के लिए किया जा सकता है, और यह निर्णय आपकी जगह नहीं लिया जाता।

प्रत्येक कॉल पर कन्फ़ाइनमेंट:

- एक इनलाइन कॉन्फ़िगरेशन, जो आपके कॉन्फ़िगरेशन से अधिक प्राथमिकता रखता है, एक `aipmt` एजेंट को परिभाषित करता है जिसके सभी टूल्स को अस्वीकार कर दिया जाता है (`permission: { "*": "deny" }`), सत्र साझाकरण अक्षम होता है, `--pure`, कभी `--auto` नहीं;
- डिस्पोजेबल और खाली कार्य डायरेक्टरी, `OPENCODE_DISABLE_PROJECT_CONFIG` और `OPENCODE_DISABLE_CLAUDE_CODE` सेट किए गए — इनके बिना, OpenCode वर्तमान डायरेक्टरी के `AGENTS.md` और `~/.claude/CLAUDE.md` को प्रॉम्प्ट में इंजेक्ट कर देता है। ग्लोबल `~/.config/opencode/AGENTS.md` इंजेक्टेड ही रहता है, OpenCode इसे हटाने की अनुमति नहीं देता;
- आउटपुट अनुबंध: रिटर्न कोड 0, कोई `error` इवेंट नहीं, कोई टूल कॉल नहीं, अंतिम चरण `stop` में, गैर-रिक्त टेक्स्ट, और एजेंट `aipmt` वास्तव में लोड हुआ हो — एक अज्ञात `--agent` OpenCode को विफल नहीं करता, यह चुपचाप कोडिंग एजेंट पर वापस लौट जाता है;
- `aipmt` की कोई भी कुंजी पास नहीं की जाती है, सिवाय `OPENCODE_API_KEY` के, जो स्वयं OpenCode की कुंजी है। प्रदाताओं को OpenCode में कॉन्फ़िगर किया जाता है, `aipmt` के `.env` में नहीं।

ध्यान देने योग्य बातें:

- Zen के मुफ़्त मॉडल परिवर्तनशील हैं, जिनकी सीमाएं अप्रलेखित हैं, और उनके आदान-प्रदान का उपयोग प्रशिक्षण के लिए किया जा सकता है: केवल सार्वजनिक दस्तावेज़ीकरण के लिए, निजी सामग्री के लिए नहीं।
- एक स्थानीय मॉडल को कम से कम 16k संदर्भ टोकन प्रदान करने चाहिए, क्योंकि सेगमेंट 16,000 वर्णों तक के होते हैं। Ollama अक्सर इसे 4,096 पर कॉन्फ़िगर करता है: `PARAMETER num_ctx 32768` वाले `Modelfile` का उपयोग करें।
- `--eco` का कोई प्रभाव नहीं है; `--reasoning_effort` को OpenCode के `--variant` के रूप में ज्यों का त्यों पास किया जाता है।
- OpenCode प्रत्येक सत्र को `~/.local/share/opencode/` में लॉग करता है।
- वेरिएबल्स: `OPENCODE_BIN` (अन्यथा `PATH`, फिर `~/.opencode/bin/opencode`), `OPENCODE_TIMEOUT` (प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 600)। `OPENCODE_CONFIG` OpenCode को ज्यों का त्यों पास किया जाता है।

`~/.config/opencode/opencode.json` में Ollama के माध्यम से एक स्थानीय मॉडल का उदाहरण:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` उस रीज़निंग को बंद कर देता है जिसे Ollama इन मॉडलों पर डिफ़ॉल्ट रूप से सक्रिय करता है, और जिसे कोई Modelfile अक्षम नहीं कर सकता। छह शब्दों के एक वाक्य पर मापा गया: इस विकल्प के बिना 919 थिंकिंग टोकन और 68 सेकंड, जबकि इसके साथ 9 टोकन।

### 400 से अधिक मॉडलों के लिए: `--use_openrouter`

OpenRouter एक उपयोग-आधारित बिलिंग वाला राउटर है, जो एकल क्रेडिट पर काम करता है, और तीसरे पक्षों द्वारा होस्ट किए गए मॉडलों के सामने रहता है — जिसमें वे खुले चीनी मॉडल भी शामिल हैं जिन्हें यहाँ कोई अन्य प्रदाता प्रदर्शित नहीं करता।

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` अनिवार्य है। किसी भी बिलिंग से पहले निष्पादित एक प्रीफ़्लाइट, रूटिंग की दो विशेषताओं को संभालता है:

- **एक ही मॉडल को अलग-अलग सीमाओं वाले दर्जनों होस्टों द्वारा परोसा जाता है** — `z-ai/glm-5.3-flash` पर, 23 होस्ट जिनमें से एक 2,048 आउटपुट टोकन तक सीमित है। प्रीफ़्लाइट `/api/v1/models/{modèle}/endpoints` को पढ़ता है, 8,000 आउटपुट टोकन से कम या ख़राब स्थिति वाले होस्टों को हटा देता है, और बाकी को `allow_fallbacks: false` के साथ पिन करता है।
- **रीज़निंग का बिल आउटपुट दर पर लिया जाता है** — `z-ai/glm-5.2` की एक "OK" प्रतिक्रिया पर 2 के मुकाबले 107 टोकन। इसे डिफ़ॉल्ट रूप से बंद रखा जाता है; जो मॉडल इसे अनिवार्य करते हैं उन्हें सबसे कम स्वीकार्य प्रयास सौंपा जाता है, क्योंकि कैटलॉग का डिफ़ॉल्ट अनुवाद समाप्त होने से पहले ही आउटपुट को समाप्त कर सकता है। `--reasoning_effort` को प्राथमिकता बनी रहती है।

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- कॉन्टेक्स्ट विंडो कैटलॉग से आती है। किसी भी कॉल से पहले 16,400 टोकन से कम वाले मॉडल को अस्वीकार कर दिया जाता है: प्रॉम्प्ट और सेगमेंट के लिए 8,400, और आउटपुट के लिए कम से कम 8,000।
- कैटलॉग से अनुपस्थित कोई स्लग, अगम्य कैटलॉग, या सीमा को बनाए रखने वाले होस्ट का अभाव कमांड को रोक देता है।
- खाली आउटपुट के साथ `finish_reason=length` रीज़निंग द्वारा खपत किया गया बजट है, न कि कोई काट-छाँट: संदेश इसमें अंतर करता है।
- `--eco` का कोई प्रभाव नहीं है।
- वेरिएबल्स: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (डिफ़ॉल्ट `https://openrouter.ai/api/v1`, `https://` आवश्यक), `OPENROUTER_TIMEOUT` (डिफ़ॉल्ट 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (डिफ़ॉल्ट 30)।

### अनुवाद संबंधी टिप्पणी

`--add_translation_note` एक टिप्पणी जोड़ता है, `bottom` में (डिफ़ॉल्ट), `top` में (फ़्रंट मैटर के बाद) या `both` में (`--note_position`), `legacy` प्रारूप (बोल्ड पैराग्राफ़, डिफ़ॉल्ट) या `marker` (`--note_format`) में। `marker` प्रारूप एक अदृश्य Markdown संदर्भ परिभाषा है, `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`, जिसके बाद एक बोल्ड उद्धरण होता है: यह GitHub पर पठनीय है और किसी remark प्लगइन द्वारा बिल्ड के समय उपयोग योग्य है।

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## विस्तृत माप

सभी माप वास्तव में `aipmt` के साथ चौदह भाषाओं में निष्पादित किए गए अनुवाद हैं: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi। **लिखित** उन फ़ाइलों की गणना करता है जिन्हें गार्ड्स ने पास होने दिया; **बिना अंतर के** वे हैं जहाँ `scripts/compare_structure.py` को कुछ भी नहीं मिलता — अनुभागों, उप-शीर्षकों, लिंकों, विशिष्ट URL, कोड ब्लॉक, इनलाइन कोड, तालिका पंक्तियों, ब्लॉककोट और बोल्ड शब्दों की समान संख्या।

"बिना अंतर के" का अर्थ है "कुछ भी पता नहीं चला", न कि "समान": तुलनित्र उनकी सामग्री को पढ़े बिना केवल तत्वों की गणना करता है। यह न तो किसी हटाए गए स्तर 4 के शीर्षक की रिपोर्ट करता है, न ही किसी बदले गए इनलाइन कोड के टेक्स्ट की, न ही बदले गए किसी फ़्लैग की, और न ही किसी अतिरिक्त कोष्ठक के साथ रेंडर किए गए आंतरिक लिंक की, `[texte]((#ancre))`, जो अब कहीं नहीं ले जाता — और यह भाषा का आकलन नहीं करता।

### सघन निगरानी लेख, मोड `--news`

[jls42.org की AI निगरानी](https://jls42.org/fr/news) का एक संस्करण:
589 पंक्तियाँ, 140 लिंक, 21 अनुभाग, 3 सुरक्षित अंग्रेज़ी उद्धरण। 4 और
5 सितंबर 2026 का अभियान।

| मॉडल                                            | एक्सेस              | लिखित   | बिना अंतर    | माध्यिका/भाषा  |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google सदस्यता     | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google सदस्यता     | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT सदस्यता    | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | स्थानीय            | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok सदस्यता       | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok को 9 सितंबर को उसी निगरानी के एक अन्य संस्करण (356 पंक्तियाँ) पर
फिर से मापा गया था: 14 में से 9 भाषाएँ लिखी गईं, 8 बिना किसी अंतर के। यही
आँकड़ा शीर्ष तालिका में दिखाई देता है। तीन बाधित अभियानों को शामिल नहीं
किया गया है: क्रेडिट समाप्त होने के कारण `qwen3.5-27b` (9 भाषाएँ) और `kimi-k2.6` (4),
तथा `z-ai/glm-5.3-flash` जिसकी दो विफलताएँ एक रीज़निंग सेटिंग के कारण थीं जिसे
प्रदाता तब से ठीक कर रहा है। OpenRouter पंक्तियों को `--use_openrouter` से पहले,
राउटर की डिफ़ॉल्ट सेटिंग्स पर मापा गया था; `z-ai/glm-5.2`, जिसे प्रदान किए गए
प्रदाता के साथ पुनः मापा गया, वही 14/14 का परिणाम देता है। वर्तमान कंपैरेटर
के साथ 10 सितंबर को आँकड़ों की पुनर्गणना की गई: `qwen3.8-flash` और
`qwen3.7-flash` प्रत्येक पहले प्रकाशन की तुलना में एक अतिरिक्त भाषा प्राप्त
करते हैं, बाकी अपरिवर्तित हैं।

`--use_antigravity` पंक्तियों को 26 सितंबर को उसी लेख पर मापा गया था, समानांतर में
चार अनुवाद: सुबह `gemini-3.7-flash-medium`, दोपहर में `gemini-3.8-flash-medium`। अंग्रेज़ी में,
प्रत्येक ने बिना कोई फ़्लैग बनाए, उद्धरणों के नीचे फ़्रेंच अनुवाद की तीन पंक्तियों को
स्वयं हटा दिया, और अंग्रेज़ी उद्धरण अक्षुण्ण हैं: फ़ॉलबैक क्लीनअप को कुछ भी
करने की आवश्यकता नहीं पड़ी। `--eco` (`gemini-3.7-flash-low`) में, केवल
चार भाषाओं पर (en, ja, ar, hi): 4 में से 4 लिखी गईं, सभी बिना किसी अंतर के,
1 min 52 s की माध्यिका। उसी दिन निगरानी के एक नए संस्करण, 25 सितंबर वाले
संस्करण (438 पंक्तियाँ, 2 अंग्रेज़ी उद्धरण) पर प्रति-परीक्षण किया गया, जिसका
अनुवाद ब्लॉग के बाहर `gemini-3.7-flash-medium` द्वारा किया गया: 14 में से 14 लिखी गईं,
सभी बिना अंतर के, 87 से 128 s प्रति भाषा।

### इस प्रोजेक्ट की README, मानक Markdown

9 सितंबर 2026 को फ़्रीज़ किया गया रिविज़न: 785 पंक्तियाँ, 285 इनलाइन कोड, 40
ब्लॉक क्लोज़र, 89 तालिका पंक्तियाँ। समानांतर में चार अनुवाद।

| मॉडल                                            | लिखित   | बिना अंतर  | माध्यिका/भाषा  | क्या भिन्न है                                                            |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | कुछ नहीं                                                                 |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | एक बोल्ड शब्द (ja)                                                       |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | एक बोल्ड शब्द (ko)                                                       |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | एक लिंक (sv), एक बोल्ड शब्द (zh)                                         |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | एक बोल्ड शब्द (ar, ja)                                                   |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | एक बोल्ड शब्द (hi, ja, ko)                                               |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | अरबी में 40 इनलाइन कोड जोड़े गए; बोल्ड (hi, ja, ko)                      |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | एक अनुभाग खो गया (ar, hi, ko); कोड ब्लॉक जोड़े गए (ja, ko, ro, zh)       |

दो बाधित अभियानों को दर्ज नहीं किया गया है: Grok, बारह भाषाओं (ग्यारह बिना अंतर के)
के बाद CLI सत्र समाप्त हो गया, और `qwen3.8-flash`, दो के बाद इसके होस्ट से HTTP 429।
`opencode/mimo-v2.5-free` और `ollama/gpt-oss-20b-32k` को इस रिविज़न पर फिर से नहीं मापा गया;
4 और 5 सितंबर वाले रिविज़न पर, जो 277 पंक्तियाँ छोटा था, उन्होंने प्रत्येक ने 14 में से 9 अनुवाद
लिखे, जिनमें क्रमशः 7 और 1 बिना अंतर के थे।

`--use_antigravity` पंक्तियों को फ़्रीज़ किए गए रिविज़न पर नहीं मापा गया था, बल्कि
26 सितंबर को 1.14.0 के साथ प्रकाशित रिविज़न पर मापा गया था: 600 पंक्तियाँ, 257 इनलाइन कोड,
30 ब्लॉक क्लोज़र, 85 तालिका पंक्तियाँ। 185 पंक्तियाँ छोटा होने के कारण, इसकी अन्य पंक्तियों से
सीधे तौर पर तुलना नहीं की जा सकती; दोनों Antigravity पंक्तियाँ आपस में तुलना योग्य हैं। आंतरिक
लिंकों पर, जिन्हें कंपैरेटर नियंत्रित नहीं करता है, `gemini-3.8-flash-medium` ने उन्हें चौदह भाषाओं में
अक्षुण्ण रखा, जबकि `gemini-3.7-flash-medium` ने उन्हें इतालवी में तोड़ दिया।

### जाने-माने प्रोजेक्ट्स की चार README

FastAPI, Ollama, tldr-pages और Vue.js, GitHub से यथावत लिए गए — पिछले दो की
तुलना में आसान दस्तावेज़। यह अभियान कठिनाई का सामना करने वाले मॉडलों पर लक्षित
था; Gemini यहाँ तुलना के बिंदु के रूप में कार्य करता है।

| मॉडल                         | दायरा                      | लिखित   | बिना अंतर    |
| ---------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`           | 4 प्रोजेक्ट्स × 14 भाषाएँ  | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free`    | 4 प्रोजेक्ट्स × 14 भाषाएँ  | 55/56   | ❌ 47/56     |
| `grok-4.6` (सदस्यता)    | 4 प्रोजेक्ट्स × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`     | 4 प्रोजेक्ट्स × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### ये माप क्या नहीं हैं

- **कोई संपूर्ण रैंकिंग नहीं**: केवल OpenRouter ही चार सौ से अधिक मॉडल प्रस्तुत
  करता है, जिनमें से लगभग पंद्रह को मापा गया था।
- **सांकेतिक अवधियाँ**: अभियानों के आधार पर समानांतर में तीन से छह अनुवाद,
  और प्रदाता का थ्रूपुट दिन भर में बदलता रहता है।
- **दिनांकित अवलोकन**: एक ही नाम के तहत मॉडल बदलते रहते हैं, और आपके
  दस्तावेज़ हमारे दस्तावेज़ों जैसे नहीं हैं।

अपने दस्तावेज़ों पर, फ़ाइल की फ़्रीज़ की गई प्रति पर माप दोहराने के लिए:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## योगदान करें

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

दोनों पंक्तियाँ आवश्यक हैं: `pip install -e .` के बिना, `python -m aipmt`
`No module named aipmt` का उत्तर देता है।

गुणवत्ता टूलिंग, वैकल्पिक लेकिन अनुशंसित:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

रिपॉजिटरी के 28 अनुवाद (README और CHANGELOG, चौदह भाषाएँ)
`./regen_translations.sh --force` के साथ पुनर्जीवित होते हैं — डिफ़ॉल्ट रूप से ChatGPT
सदस्यता पर Codex और `gpt-5.6-sol`, समानांतर में चार। `REGEN_PROVIDER` और
`REGEN_MODEL` पथ बदलते हैं: `antigravity` एक सदस्यता पर रहता है, Google वाली,
और बिना किसी छूट के पास हो जाता है; बिल की जाने वाली API (`openai`, `gemini`,
`grok`, `openrouter`) `REGEN_ALLOW_PAID_API=1` के बिना अस्वीकार कर दी जाती है;
`REGEN_JOB_TIMEOUT` प्रत्येक जॉब को कैप करता है (600 s, Codex और
Antigravity पर 1,800 s)। टूलिंग का विवरण `CLAUDE.md` में है।

## इस स्क्रिप्ट का उपयोग करने वाले प्रोजेक्ट्स

- **[jls42.org](https://jls42.org)** — 15 भाषाओं में प्रकाशित व्यक्तिगत ब्लॉग। इसकी
  [दैनिक AI निगरानी](https://jls42.org/fr/news) का अनुवाद प्रतिदिन इस टूल द्वारा किया जाता है,
  और यह उपरोक्त मापों के लिए संदर्भ दस्तावेज़ के रूप में कार्य करता है।

## लेखक

Julien LE SAUX
ईमेल: contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3। [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) देखें।

## चेतावनी

यह प्रोग्राम GPL v3 की धारा 15 और 16 की शर्तों के तहत **बिना किसी वारंटी के**
वितरित किया जाता है: "जैसा है" के आधार पर प्रदान किया गया, किसी विशेष उद्देश्य के
लिए व्यापारिकता या उपयुक्तता की वारंटी के बिना, और इसके लेखक को इसके उपयोग से
होने वाले किसी भी नुकसान के लिए उत्तरदायी नहीं ठहराया जा सकता है। लाइसेंस का
मूल पाठ इस सारांश से अधिक मान्य है।

- **प्रकाशित करने से पहले दोबारा पढ़ें।** सुरक्षा केवल कोड ब्लॉक, इनलाइन कोड,
  URL, एंकर और `--news` मोड के उद्धरणों को कवर करती है — न तो शीर्षकों को,
  न तालिकाओं को, न फ्रंट मैटर को, और न ही आपके वाक्यों के अर्थ को।
- **आपके दस्तावेज़ चुने गए प्रदाता के पास जाते हैं**, उसकी उपयोग की शर्तों और डेटा
  नीति के तहत। कुछ मुफ़्त मॉडल आपके संवादों का उपयोग प्रशिक्षण के लिए कर सकते हैं,
  और Antigravity की शर्तें Google को उनका पुन: उपयोग करने और इंसानों द्वारा उनकी
  समीक्षा कराने की अनुमति देती हैं, जिसमें सशुल्क सदस्यता भी शामिल है; एक स्थानीय मॉडल
  ही एकमात्र ऐसा तरीका है जिससे कोई भी डेटा आपकी मशीन से बाहर नहीं जाता है।
- **API कॉल का शुल्क आपसे लिया जाता है।** यह प्रोग्राम खर्च की कोई सीमा तय नहीं
  करता है: एक लंबा दस्तावेज़, विफलता के बाद पुनः प्रयास, या ऐसा मॉडल जो बहुत अधिक
  रीज़निंग करता है, अधिक लागत लाते हैं।
- **प्रकाशित माप दिनांकित अवलोकन हैं**, कोई गारंटी नहीं।

उल्लिखित उत्पादों और कंपनियों के नाम उनके संबंधित स्वामियों के हैं। यह प्रोजेक्ट इनमें
से किसी से भी संबद्ध नहीं है।

**gemini-3.8-flash-medium के साथ फ़्रेंच से हिंदी में अनुवादित लेख।**
