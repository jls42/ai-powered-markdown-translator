# AI-संचालित Markdown अनुवादक

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

संरचना को सुरक्षित रखते हुए Markdown फ़ाइलों का एक भाषा से दूसरी भाषा में अनुवाद करता है: कोड ब्लॉक, इनलाइन कोड, URL, एंकर, तालिकाएँ और front matter। किसी मॉडल को कॉल करने के ग्यारह तरीके — पाँच API, चार बिना उपयोग-आधारित बिलिंग वाले सब्सक्रिप्शन, दो राउटर — और प्रत्येक मॉडल वास्तव में क्या सुरक्षित रखता है, इसका एक प्रकाशित माप।

## संक्षेप में

- **ग्यारह प्रोवाइडर पाथ**: OpenAI, Mistral, Claude, Gemini और Grok API; बिना उपयोग-आधारित बिलिंग वाले ChatGPT (Codex), Grok, Google (Antigravity) और Claude (Claude Code) सब्सक्रिप्शन; OpenCode (ओपन सोर्स, मुफ़्त या स्थानीय) और OpenRouter (400 से अधिक मॉडल) राउटर।
- **खोए हुए टोकन के कारण कुछ भी गलत नहीं**: कॉल से पहले कोड ब्लॉक, इनलाइन कोड, URL, एंकर और उद्धरणों को टोकन से बदल दिया जाता है और वापसी पर सत्यापित किया जाता है। यदि कोई एक भी अनुपस्थित हो, तो फ़ाइल नहीं लिखी जाती है।
- **लंबे दस्तावेज़**: मॉडल की विंडो के अनुसार विखंडन (segmentation)।
- **`--news` मोड**: तकनीकी निगरानी लेखों के लिए, सुरक्षित अंग्रेजी उद्धरण और प्रति भाषा प्रबंधित फ़्लैग।
- **`--eco` मोड**: तेज़ और कम खर्चीले मॉडल।
- **वैकल्पिक अनुवाद नोट**: ऊपर, नीचे या दोनों जगह।

## संस्थापन

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 या नया। रिपॉजिटरी से इंस्टॉल करने के लिए, [योगदान दें](#योगदान-देना) देखें।

## कॉन्फ़िगरेशन

कुंजियाँ उच्चतम से निम्नतम प्राथमिकता के क्रम में तीन स्थानों से पढ़ी जाती हैं; प्रत्येक केवल वही भरता है जिसे पिछला खाली छोड़ देता है।

|     | कहाँ                                          | किस लिए                               |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | पर्यावरण चर (Environment variables)          | CI, कंटेनर, एकमुश्त अपवाद              |
| 2   | वर्तमान निर्देशिका (या पैरेंट) की `.env` | किसी प्रोजेक्ट के लिए विशिष्ट कुंजी   |
| 3   | `~/.config/aipmt/.env`                                 | एक बार इंस्टॉल किया गया, हर जगह मान्य |

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

`GOOGLE_API_KEY` के स्थान पर `GEMINI_API_KEY` स्वीकार किया जाता है। उपयोगकर्ता फ़ाइल `XDG_CONFIG_HOME` (केवल पूर्ण पथ) और Windows पर `%APPDATA%` का अनुसरण करती है। बिना किसी कुंजी के, कमांड तीनों स्थानों को सूचीबद्ध करता है।

**किसी प्रोजेक्ट का `.env` न तो कॉल को रीडायरेक्ट कर सकता है और न ही निष्पादित प्रोग्राम चुन सकता है।** यह कुंजियाँ प्रदान करता है, कभी भी कोई गंतव्य या बाइनरी नहीं: `_BASE_URL`, `_API_BASE`, `_ENDPOINT` या `_BIN` (`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME` में कोई भी चर, प्रॉक्सी (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), प्रमाणपत्र स्टोर (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) और `XDG_CONFIG_HOME` / `APPDATA` को चेतावनी के साथ अनदेखा कर दिया जाता है। एक क्लोन किया गया रिपॉजिटरी आपकी कुंजी को चुराने या पहले अनुवाद पर आपको अपना स्वयं का प्रोग्राम चलाने के लिए मजबूर करने में सक्षम नहीं होना चाहिए। यह फ़ाइल बिना प्रक्षेप (interpolation) के भी पढ़ी जाती है: `NOM=${OPENAI_API_KEY}` वहाँ कुंजी को कॉपी नहीं करता है। इन चरों को पर्यावरण में या `~/.config/aipmt/.env` में रखें।

वैकल्पिक चर: `XAI_BASE_URL` (डिफ़ॉल्ट `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (प्रति कॉल सेकंड, डिफ़ॉल्ट 900), `CODEX_BIN`, `CODEX_TIMEOUT` (डिफ़ॉल्ट 600), `GROK_BIN`, `GROK_HOME` (डिफ़ॉल्ट `~/.grok`), `GROK_TIMEOUT` (डिफ़ॉल्ट 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (डिफ़ॉल्ट 900), `OPENCODE_BIN`, `OPENCODE_TIMEOUT` (डिफ़ॉल्ट 600), `OPENROUTER_BASE_URL` (`https://` आवश्यक), `OPENROUTER_TIMEOUT` (डिफ़ॉल्ट 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (डिफ़ॉल्ट 30)। प्रत्येक का विवरण उसके प्रोवाइडर अनुभाग में दिया गया है।

## शुरुआत करना

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

स्पैनिश में अनुवादित `document.md`, `--target_dir` में `document-es.md` देता है; `--include_model` के साथ, `document-es-gpt-6.1-terra.md`। एक्सटेंशन हमेशा `.md` बन जाता है — `article.mdx` से `article-en.md` मिलता है — सिवाय `--keep_filename` के, जो मूल नाम को बनाए रखता है। पहले से मौजूद अनुवाद को बिना `--force` के छोड़ दिया जाता है।

एग्जिट कोड: `0` यदि सब कुछ सफल रहा या छोड़ दिया गया, `1` यदि कोई फ़ाइल विफल रही (मानक त्रुटि आउटपुट पर सूची), `2` यदि कॉन्फ़िगरेशन में कोई समस्या है। विफल फ़ाइल कभी नहीं लिखी जाती है, भले ही लिखना स्वयं विफल हो जाए: सामग्री को पास में लिखा जाता है और फिर नाम बदल दिया जाता है। पुन: चलाना ही पर्याप्त है।

## कौन सा मॉडल चुनें

दो वास्तविक दस्तावेज़ों पर मापा गया, जिनका प्रत्येक मॉडल द्वारा उन्हीं चौदह भाषाओं में अनुवाद किया गया। **यह संख्या चौदह में से उन भाषाओं की संख्या है जहाँ अनुवाद लिखा गया है और स्रोत से कुछ भी भिन्न नहीं है।**

| मॉडल                  | इस तक कैसे पहुँचें                | सघन निगरानी लेख         | यह README    | क्या भिन्न है, और कितनी भाषाओं पर                                                                                                                                  |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google सब्सक्रिप्शन (Antigravity) | ✅ 14/14                | ✅ 14/14     | कुछ नहीं, दोनों में से किसी भी दस्तावेज़ पर                                                                                                                        |
| **Claude Sonnet 5.5** | Anthropic API कुंजी               | ✅ 14/14                | ✅ 14/14     | कुछ नहीं, दोनों में से किसी भी दस्तावेज़ पर                                                                                                                        |
| **Gemini 3.7 Flash**  | Google API कुंजी                  | ✅ 14/14                | ⚠️ 13/14     | 14 में से 1 भाषा: एक अतिरिक्त बोल्ड शब्द (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google सब्सक्रिप्शन (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 14 में से 1 भाषा: एक कम बोल्ड शब्द (ko)                                                                                                                            |
| **GPT-5.6 Sol**       | ChatGPT सब्सक्रिप्शन, या OpenAI कुंजी | ✅ 14/14             | ⚠️ 12/14     | 14 में से 2 भाषाएँ: एक कम बोल्ड शब्द (ar, ja)                                                                                                                       |
| **GLM-5.2**           | OpenRouter कुंजी                  | ✅ 14/14                | ⚠️ 11/14     | 14 में से 3 भाषाएँ: एक कम बोल्ड शब्द (hi, ja, ko)                                                                                                                  |
| Claude Sonnet 5       | Claude सब्सक्रिप्शन (Claude Code) | ⚠️ 13/14                | ⚠️ 13/14     | लेख पर 14 में से 1 भाषा: एक अतिरिक्त बोल्ड शब्द (zh); इस README पर 1: तालिका की एक पंक्ति पिछली पंक्ति से चिपक गई, प्रदर्शन में छिप गई (ar)                         |
| Claude Haiku 4.5      | Claude सब्सक्रिप्शन (Claude Code) | ⚠️ 11/14                | ✅ 14/14     | लेख पर 14 में से 3 भाषाएँ: एक अनुभाग शीर्षक स्तर 1 पर चला गया (en, pl, ro); इस README पर, तुलनित्र के लिए कुछ नहीं, लेकिन आंतरिक लिंक अंग्रेजी में दोगुने हो गए   |
| Claude Sonnet 5       | Anthropic API कुंजी               | ⚠️ 11/14                | ⚠️ 12/14     | लेख पर 14 में से 3 भाषाएँ: एक अप्रत्याशित कोड ब्लॉक दिखाई दिया (es, de, hi); इस README पर 2: बिना मार्कअप वाला एक लिंक (sv), एक बोल्ड शब्द (zh)                   |
| Claude Haiku 4.5      | Anthropic API कुंजी               | ⚠️ 7/14                 | ✅ 14/14     | लेख पर 14 में से 7 भाषाएँ: एक अनुभाग शीर्षक स्तर 1 पर चला गया — जापानी में, फ्रेंच में ही रह गया; इस README पर कुछ नहीं                                            |
| Claude Haiku 5.5      | Anthropic API कुंजी               | ⚠️ 11/14                | ❌ 12/14     | लेख पर 14 में से 3 भाषाएँ: एक अनुभाग शीर्षक का स्तर बदला या दोहराया गया (ja, ko, zh); इस README पर, 2 भाषाएँ अस्वीकृत, इनलाइन कोड खो गए (ar, hi)                  |
| Qwen 3.7 Flash        | OpenRouter कुंजी                  | ❌ 8/14                 | ⚠️ 10/14     | लेख पर 1 भाषा अस्वीकृत, 5 अन्य विचलित; इस README पर, लगभग चालीस शब्द `code` में बदल दिए गए (ar)                                                            |
| Grok 4.6              | Grok सब्सक्रिप्शन                 | ❌ 8/14                 | मूल्यांकित नहीं | 14 में से 5 भाषाएँ अस्वीकृत, क्योंकि इनलाइन कोड और URL रेंडर नहीं हुए; डच भाषा में सब कुछ अलग हो गया                                                               |
| GPT-OSS 20B           | स्थानीय मॉडल (Ollama)             | ❌ 7/14                 | पुनर्मापन नहीं | 14 में से 4 भाषाएँ अस्वीकृत: मॉडल ने उसमें फ्रेंच अंश छोड़ दिए, गार्ड ने उन्हें रोक दिया                                                                           |
| MiMo v2.5 (मुफ़्त)    | OpenCode Zen, बिना खाते के        | ❌ 11/14                | पुनर्मापन नहीं | 1 भाषा अस्वीकृत; पोलिश में एक अनुभाग खो गया                                                                                                                        |
| Mistral Large         | Mistral API कुंजी                 | ❌ 5/14                 | ❌ 1/14      | **एक पूरा अनुभाग गायब हो गया**: लेख पर 14 में से 1 भाषा (hi), इस README पर 3 (ar, hi, ko) — और लेख पर 3 भाषाएँ अस्वीकृत                                           |
| DeepSeek V4 Flash     | OpenRouter कुंजी                  | ❌ 3/14                 | पुनर्मापन नहीं | 14 में से 10 भाषाएँ अस्वीकृत; 37 मिनट प्रति भाषा                                                                                                                   |
| Claude Opus 5.5       | Claude सब्सक्रिप्शन (Claude Code) | ❌ 0/14                 | ✅ 14/14     | एक संक्षिप्त जीव विज्ञान समाचार के कारण, Opus के सुरक्षा उपायों (guardrails) द्वारा सभी 14 भाषाओं में लेख अस्वीकृत; इस README पर कुछ नहीं                         |

|     | प्रतीक क्या दर्शाता है                                                                                                                                                                                |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | चौदह भाषाओं का अनुवाद किया गया, और स्रोत से कुछ भी भिन्न नहीं है                                                                                                                                      |
| ⚠️  | चौदह भाषाओं का अनुवाद किया गया; जो भिन्न है वह **मार्कअप** है — एक बोल्ड शब्द, एक `code`, कोष्ठक खो देने वाला एक लिंक। कोई टेक्स्ट, कोई URL, कोई कोड ब्लॉक, कोई अनुभाग गायब नहीं है          |
| ❌  | कम से कम एक भाषा का अनुवाद नहीं किया जा सका — फ़ाइल अस्वीकृत है, लिखी नहीं गई — **या** लिखी गई फ़ाइल में से सामग्री गायब है                                                                          |

मुख्य निष्कर्ष:

- **अस्वीकृत अनुवाद कोई विकृत अनुवाद नहीं होता।** जब वापसी पर कोई टोकन गायब
  होता है, तो फ़ाइल नहीं लिखी जाती है और भाषा को अस्वीकृत माना जाता है। लेख पर
  Grok के साथ यही होता है: पाँच गैर-लैटिन लिपियों में पहले ही सेगमेंट से चार
  इनलाइन कोड और तीन URL गायब हो गए।
- **एक मॉडल केवल एक वाक्य के कारण पूरे दस्तावेज़ को अस्वीकार कर सकता है।**
  Opus 5.5 इस README का बिना किसी विचलन के अनुवाद करता है, लेकिन किसी भी निगरानी
  लेख का नहीं: इसके सुरक्षा उपाय (guardrails) एक संक्षिप्त जीव विज्ञान समाचार
  पर प्रतिक्रिया को रोक देते हैं। फ़ाइल नहीं लिखी जाती है, और aipmt इसका कारण
  बताता है।
- **यह सुरक्षा जाल शीर्षकों, तालिकाओं, front matter या टेक्स्ट को कवर नहीं
  करता है।** जो मॉडल किसी अनुभाग को हटा देता है, वह ऐसी फ़ाइल लौटाता है जिसे
  टूल बिना किसी आपत्ति के लिख देता है — Mistral का यही मामला है। इन तत्वों को
  टोकन से नहीं बदला जा सकता है, और वर्तमान गार्ड इनकी जाँच नहीं करते हैं;
  `scripts/compare_structure.py` खोए हुए अनुभाग का पता लगाता है, लेकिन घटना के बाद।
- **इस README पर Grok का कोई मूल्यांकन नहीं है**: बारह भाषाओं के बाद इसका CLI
  सत्र समाप्त हो गया, जिनमें से ग्यारह बिना किसी विचलन के थीं। एक बाधित
  अभियान का मूल्यांकन नहीं किया जाता है।
- **दस्तावेज़ का घनत्व भाषा से अधिक मायने रखता है।** Grok साधारण README पर सही
  काम करता है और लिंक से भरे लेख पर लड़खड़ा जाता है, जिसमें डच भी शामिल है।

तिथियाँ और दस्तावेज़: "यह README" कॉलम को 9 सितंबर 2026 को इस फ़ाइल के एक स्थिर
रिवीज़न (785 पंक्तियाँ, 285 इनलाइन कोड, 89 तालिका पंक्तियाँ) पर मापा गया था,
जिसे बाद में संशोधित किया गया है — सिवाय Antigravity और Claude Code पंक्तियों
के, जिन्हें 26 सितंबर को 1.14.0 के साथ प्रकाशित छोटे रिवीज़न (600 पंक्तियाँ,
257 इनलाइन कोड, 85 तालिका पंक्तियाँ) पर मापा गया था, और API के माध्यम से Claude
Sonnet 5.5, Haiku 5.5 और Haiku 4.5 पंक्तियों को, जिन्हें उसी रिवीज़न पर 18
अक्टूबर को मापा गया था। "सघन निगरानी लेख" कॉलम 589 पंक्तियों के एक लेख पर 4
और 5 सितंबर के अभियान से आता है, सिवाय Grok पंक्ति के, जिसे 9 सितंबर को उसी
निगरानी के दूसरे संस्करण पर पुनर्मापा गया था, Antigravity और Claude Code
पंक्तियों को, जिन्हें उसी लेख पर 26 सितंबर को मापा गया था, और इन तीन Claude
पंक्तियों को 18 अक्टूबर को। पूर्ण तालिकाएँ, अवधियाँ और प्रोटोकॉल [विस्तृत माप](#विस्तृत-माप) में हैं।

## सभी विकल्प

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | अनुवाद के लिए एकल Markdown फ़ाइल (`--source_dir` का विकल्प)                                             |
| `--source_dir`           | Markdown फ़ाइलें रखने वाली स्रोत निर्देशिका (डिफ़ॉल्ट: `content/posts`)                                   |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका (डिफ़ॉल्ट: `traductions_en`)                                    |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                                                                  |
| `--target_lang`          | लक्ष्य भाषा (डिफ़ॉल्ट: `en`)                                                                                   |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                                                                  |
| `--eco`                  | किफ़ायती मॉडलों का उपयोग करें                                                                              |
| `--use_mistral`          | Mistral AI API का उपयोग करें                                                                                     |
| `--use_claude`           | Claude API का उपयोग करें                                                                                         |
| `--use_gemini`           | Gemini API का उपयोग करें                                                                                         |
| `--use_grok`             | xAI (Grok) API का उपयोग करें — `XAI_API_KEY` आवश्यक है                                                           |
| `--use_codex`            | ChatGPT सदस्यता कोटे पर Codex CLI का उपयोग करें                                                    |
| `--use_grok_cli`         | Grok सदस्यता कोटे पर Grok CLI का उपयोग करें                                                        |
| `--use_antigravity`      | Google AI Pro या Ultra सदस्यता कोटे पर Antigravity CLI (`agy`) का उपयोग करें                       |
| `--use_claude_code`      | Claude Pro या Max सदस्यता कोटे पर Claude Code CLI (`claude -p`) का उपयोग करें                      |
| `--use_opencode`         | OpenCode में कॉन्फ़िगर किए गए प्रदाता के लिए OpenCode (ओपन सोर्स) का उपयोग करें; `--model provider/modèle` आवश्यक है |
| `--use_openrouter`       | OpenRouter का उपयोग करें — `OPENROUTER_API_KEY` और `--model fournisseur/modèle` आवश्यक हैं                          |
| `--force`                | पुनः अनुवाद के लिए बाध्य करें                                                                                       |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखें                                                                          |
| `--news`                 | समाचार मोड: EN उद्धरणों की सुरक्षा करता है, भाषा-वार फ़्लैग्स संभालता है                                      |
| `--add_translation_note` | अनुवाद नोट जोड़ें                                                                                |
| `--note_position`        | नोट की स्थिति: `top`, `bottom` (डिफ़ॉल्ट), या `both`                                                     |
| `--note_format`          | नोट का प्रारूप: `legacy` (डिफ़ॉल्ट, बोल्ड पैराग्राफ) या `marker`                                            |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें                                                            |
| `--reasoning_effort`     | GPT-5.x रीज़निंग प्रयास: `none`/`low`/`medium`/`high`/`xhigh`                                         |

नौ `--use_*` फ़्लैग परस्पर अपवर्जित हैं: किन्हीं दो को एक साथ उपयोग करने की अनुमति नहीं है।

## Providers

### API द्वारा: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` प्रत्येक प्रदाता के किफ़ायती स्तर पर स्विच करता है।

| Provider    | गुणवत्ता (डिफ़ॉल्ट)                                                     | किफ़ायती (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (`--model` के माध्यम से `gpt-5.6-sol`, `terra` और `luna` भी) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | वही — `--eco` का कोई प्रभाव नहीं |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, प्रयास `low`                                               | वही — `--eco` का कोई प्रभाव नहीं |
| OpenCode    | `--model provider/modèle` अनिवार्य                                | वही — `--eco` का कोई प्रभाव नहीं |
| OpenRouter  | `--model fournisseur/modèle` अनिवार्य                             | वही — `--eco` का कोई प्रभाव नहीं |

डिफ़ॉल्ट सेटिंग्स अपनाने से पहले मापी गई प्रत्येक प्रदाता की नवीनतम पीढ़ी का अनुसरण करती हैं: OpenAI में GPT-6, Google में Gemini 4 Hydrogen, और 1.19.0 से xAI में Grok 4.7। पिछले मॉडलों को `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…) के माध्यम से स्वीकार किया जाता है, साथ ही Google के हाई-एंड मॉडल Gemini 4 Argon और Carbon को भी। aipmt स्वयं GPT और Grok के रीज़निंग प्रयास को नियंत्रित करता है, जो `--eco` में बंद रहता है, और `--reasoning_effort` इसे बाध्य करता है; Gemini को हमेशा वह न्यूनतम स्तर प्राप्त होता है जिसे वह स्वीकार करता है।
Gemini API की अस्थायी खराबी (503, 429, टाइमआउट) पर कॉल को 10, 20 और फिर 40 सेकंड के बाद तीन बार तक पुनः आज़माया जाता है। अनुत्तरित रहने वाले प्रयास को 5 मिनट बाद छोड़ दिया जाता है, और फिर उसी तरह पुनः प्रयास किया जाता है: अनिश्चित काल तक अटके रहने के बजाय, एक अनुत्तरदायी सर्वर अधिकतम लगभग बीस मिनट में सेगमेंट को विफल कर देता है।

### ChatGPT सदस्यता पर: `--use_codex`

आधिकारिक Codex CLI को संचालित करता है: बिना किसी API कुंजी या उपयोग-आधारित बिलिंग के, अनुवाद को ChatGPT सदस्यता के कोटे से काटा जाता है।

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- बाइनरी को `CODEX_BIN`, फिर `PATH`, और फिर `openai-codex-cli-bin` पैकेज में खोजा जाता है। `~/.codex/auth.json` को कभी नहीं पढ़ा जाता है।
- `OPENAI_API_KEY` और `CODEX_API_KEY` को सबप्रोसेस के एनवायरनमेंट से हटा दिया जाता है: किसी कुंजी की उपस्थिति कभी भी API पर स्विच नहीं कराती है।
- प्रत्येक सेगमेंट में 5 घंटे की विंडो का कम से कम एक "संदेश" खर्च होता है — यदि इसका सत्यापन विफल हो जाता है और पुनः प्रयास किया जाता है, तो दो संदेश। Plus प्लान पर OpenAI के अनुमान के अनुसार, `gpt-5.6-luna` (`--eco`) के लिए 250-2,000 संदेश/5 घंटे और `gpt-5.6-sol` के लिए 10-100 संदेश होते हैं।
- 1.16.3 तक डिफ़ॉल्ट रहा `--model gpt-5.6-sol`, `--model gpt-5.6-terra` और `--model gpt-5.6-luna` भी सदस्यता के माध्यम से काम करते हैं।
- सर्वर से 429 त्रुटि मिलने पर फ़ाइल नष्ट नहीं होती: Codex स्वयं पुनः कनेक्ट होता है, aipmt उस राउंड के समाप्त होने की प्रतीक्षा करता है, और यदि 429 त्रुटि बनी रहती है, तो सेगमेंट 30 और फिर 60 सेकंड के बाद पुनः प्रारंभ होता है। जिस मॉडल का खाता अधिकृत नहीं है, वह 400 "model is not supported when using Codex with a ChatGPT account" लौटाता है।
- API की तुलना में धीमा है, और दस्तावेज़ के आकार के साथ यह अंतर बढ़ता जाता है: इस README पर, `gpt-5.6-sol` के साथ प्रति भाषा औसत 6 मिनट 46 सेकंड, जबकि `gemini-3.7-flash` के लिए 36 सेकंड।
- CI में अस्वीकृत (`CI` या `GITHUB_ACTIONS` परिभाषित होने पर): सदस्यता एक व्यक्तिगत सत्र फ़ाइल द्वारा प्रमाणित होती है, जिसे किसी साझा रनर पर नहीं होना चाहिए।
- वेरिएबल: `CODEX_BIN`, `CODEX_TIMEOUT` (प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 600)।

### Grok सदस्यता पर: `--use_grok_cli`

SuperGrok या X Premium+ सदस्यता पर, आधिकारिक Grok Build CLI के साथ भी यही सिद्धांत लागू होता है।

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Codex की तुलना में कमज़ोर सैंडबॉक्सिंग।** कई आधुनिक Linux सिस्टमों (AppArmor, कंटेनर रनटाइम सॉकेट्स) पर Grok का OS सैंडबॉक्स लागू नहीं होता है, और जो प्रोफ़ाइल लागू नहीं हो सकती वह बिना किसी चेतावनी के अनकंफाइंड रूप से शुरू हो जाती है। इसलिए स्क्रिप्ट डिफ़ॉल्ट रूप से किसी प्रोफ़ाइल का अनुरोध नहीं करती है, इसकी घोषणा करती है, और CLI के `--deny` नियमों पर निर्भर करती है, जिसमें कैच-ऑल `*` शामिल है — यह एकमात्र ऐसा स्तर है जो बिना बताए सुरक्षा हटाने के बजाय शुरू होने से मना कर देता है। `GROK_TRANSLATE_SANDBOX=read-only` के लिए OS सैंडबॉक्स आवश्यक है, और यदि मशीन इसे पूरा नहीं कर सकती है तो स्टार्टअप विफल हो जाता है।
- कोटा साप्ताहिक है, जो Chat, Imagine और Voice के साथ साझा किया जाता है, और इसे पढ़ने के लिए कोई कमांड उपलब्ध नहीं है: कोई बैच बिना किसी संकेत के संवादात्मक उपयोग को प्रभावित कर सकता है।
- वेरिएबल: `GROK_BIN`, `GROK_HOME` (CLI निर्देशिका, डिफ़ॉल्ट `~/.grok`), `GROK_TIMEOUT` (डिफ़ॉल्ट 900), `GROK_TRANSLATE_SANDBOX`।

### Google सदस्यता पर: `--use_antigravity`

Antigravity के आधिकारिक CLI, `agy` के साथ भी यही सिद्धांत लागू होता है: Google AI Pro या Ultra के लिए भुगतान करने वालों के लिए, प्रति-टोकन शुल्क लेने के बजाय अनुवाद को सदस्यता कोटे से काटा जाता है। इस कोटे तक पहुँचने का यह एकमात्र तरीका है: Gemini CLI 18 जून 2026 से इन खातों को सेवा नहीं देता है ([घोषणा](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)), और Antigravity SDK केवल API कुंजी या Google Cloud प्रोजेक्ट स्वीकार करता है।

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **कोई भी सशुल्क मार्ग खुला नहीं रहता है।** agy आपके एनवायरनमेंट से केवल वेरिएबल्स की एक बंद सूची ही प्राप्त करता है — `PATH`, भाषा और समय क्षेत्र, टर्मिनल, पहचान, प्रॉक्सी और प्रमाणपत्र, सत्र बस — और कोई कुंजी नहीं: इसके कई वेरिएबल्स बिना कुछ प्रदर्शित किए कॉल को स्विच कर देते हैं (परीक्षण में पाया गया: एक वेरिएबल दस्तावेज़ को किसी तीसरे पक्ष के गेटवे पर भेजता है, दूसरा किसी बिल योग्य Google Cloud प्रोजेक्ट पर), और एक अस्वीकृति सूची हर समीक्षा में कुछ न कुछ छोड़ देती थी। किसी भी सेगमेंट से पहले, `agy -p /config`, जिसमें कोई कोटा खर्च नहीं होता, को सशुल्क AI क्रेडिट अक्षम दिखाना चाहिए, जिसमें कोई API कुंजी या Google Cloud प्रोजेक्ट न हो — किसी सेटिंग की अनुपस्थिति का अर्थ अस्वीकृति है —, अन्यथा कुछ भी अनुवादित नहीं किया जाता है; इसके बाद प्रत्येक कॉल के लॉग को सदस्यता की पुष्टि (`authMethod=consumer`) करनी चाहिए, अन्यथा प्रतिक्रिया अस्वीकार कर दी जाती है।
- **सैंडबॉक्सिंग।** प्रत्येक कॉल बिना किसी टूल वाले अनुवाद एजेंट के साथ, एक निजी और डिस्पोजेबल होम डायरेक्टरी में चलती है: आपकी agy सेटिंग्स, नियम, प्लगइन्स, MCP सर्वर और हुक इसमें प्रवेश नहीं करते हैं, आपके इतिहास में कुछ भी नहीं जुड़ता है, और लॉगिन कीचेन में रहता है, जिसे aipmt कभी नहीं पढ़ता है। यदि एजेंट नहीं मिलता है, तो agy चुपचाप अपने कोडिंग एजेंट और उसके टूल्स पर वापस चला जाता है: लॉग की एक पूरी पंक्ति द्वारा सही एजेंट की पुष्टि की जानी चाहिए — इस संदेश को उद्धृत करने वाला कोई दस्तावेज़ इसका स्थान नहीं ले सकता —, अन्यथा अस्वीकार कर दिया जाता है।
- **प्लेटफ़ॉर्म**: Linux, ऐसे सत्र में जिसके पास एक कीचेन हो (D-Bus सत्र बस, Secret Service); macOS समर्थित है, हालांकि उस पर इसका परीक्षण नहीं किया गया है। Windows पर अस्वीकृत है, जहाँ agy प्रत्येक कॉल को अलग करने वाले वेरिएबल्स को नहीं पढ़ता है, और बिना सत्र बस वाले Linux पर — SSH सत्र, कंटेनर, सर्वर: जहाँ agy अपने टोकन को `~/.gemini` की एक फ़ाइल में संग्रहीत करता है, जिसे आइसोलेशन छिपा देता है। लॉगिन कोड के लिए एक मिनट तक प्रतीक्षा करने के बजाय, लॉन्च होने से पहले ही कारण सहित अस्वीकृति आ जाती है।
- **मॉडल**: `agy models` वाले मॉडल। Gemini अपने नाम में ही प्रयास को दर्शाते हैं (`gemini-3.8-flash-medium`…): बिना प्रत्यय वाला नाम कॉल से पहले ही अस्वीकार कर दिया जाता है, और `--reasoning_effort` का कोई प्रभाव नहीं पड़ता। जब से agy ने Gemini 3.7 Flash की सेवा बंद की है, तब से डिफ़ॉल्ट रूप से `gemini-3.8-flash-medium`, और `--eco` में `gemini-3.8-flash-low` है; जिस परीक्षण अभियान ने डिफ़ॉल्ट निर्धारित किया था, उसका वर्णन [विस्तृत माप](#विस्तृत-माप) में किया गया है। Gemini 4 Hydrogen (`gemini-4-hydrogen-low`…) 3.8 Flash के कोटे को साझा करता है और इसका अधिक उपयोग करता है: मध्यम प्रयास पर इस README के लिए 5 घंटे की विंडो का 0.95 अंक, जबकि 3.8 Flash के लिए 0.32 अंक। Claude और GPT-OSS का अपना कोटा है, जो काफी छोटा है: मापे गए प्रति कॉल पर 5 घंटे की विंडो का लगभग 1%, जबकि Flash में यह 0.05% है। Gemini 4 Argon का अपना साप्ताहिक कोटा है: यह README उसका 1.35% लेता है।
- **कोटा**: प्रति समूह, टोकन लागत के अनुपात में 5 घंटे और एक साप्ताहिक विंडो। लेखक के खाते पर मापा गया: `gemini-3.8-flash-medium` में प्रति दस लाख स्रोत वर्णों पर 5 घंटे की विंडो के लगभग 16 अंक, `gemini-3.7-flash-medium` में 14 अंक और कम प्रयास पर 7 से 8 अंक — इसलिए 40,000 वर्णों वाले README की लागत आधे अंक से थोड़ी अधिक होती है। साप्ताहिक सीमा स्तर पर निर्भर करती है। पुनः प्रयास agy द्वारा पुनः प्रयास योग्य घोषित किए जाने के अनुसार होता है; अन्यथा, समाप्त हो चुकी विंडो को कभी भी पुनः प्रयास नहीं किया जाता है: यह `/usage` द्वारा दिखाए गए रीसेट होने तक प्रत्येक फ़ाइल को विफल कर देता है।
- **API की तुलना में धीमा**: परीक्षणों के विस्तृत लेख पर, `gemini-3.8-flash-medium` में प्रति भाषा औसत 3 मिनट 59 सेकंड और `gemini-3.7-flash-medium` में 3 मिनट 14 सेकंड, जबकि API के माध्यम से Gemini 3.7 Flash के लिए 1 मिनट 18 सेकंड।
- **रुकावट**: Ctrl-C, या बंद टर्मिनल, आपके कोटे पर राउंड पूरा करने देने के बजाय कमांड के साथ ही agy को रोक देता है; यही बात Codex, Grok CLI और OpenCode पर भी लागू होती है। `nohup` के तहत, अनुवाद जारी रहता है।
- CI में अस्वीकृत (`CI` या `GITHUB_ACTIONS` परिभाषित होने पर): लॉगिन क्रेडेंशियल व्यक्तिगत कीचेन में रहता है। रनर पर, `GOOGLE_API_KEY` के साथ `--use_gemini` का उपयोग करें।
- वेरिएबल: `AGY_BIN` (अन्यथा `PATH`, फिर `~/.local/bin/agy`), `AGY_TIMEOUT` (स्टार्टअप सहित प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 900)।

**उपयोग की शर्तें: यह आपका अपना खाता है जो दांव पर है।** [Antigravity की शर्तें](https://antigravity.google/terms) (अनुभाग 6) और इसके [FAQ](https://antigravity.google/docs/faq/), खाता निलंबन के जोखिम के तहत, Antigravity लॉगिन का उपयोग करके किसी तीसरे पक्ष के सॉफ़्टवेयर के माध्यम से सेवा तक पहुँचने पर रोक लगाते हैं — जिनमें Claude Code, OpenClaw और OpenCode का विशेष रूप से उल्लेख है। aipmt न तो टोकन को पढ़ता है और न ही उसका पुनः उपयोग करता है: यह आधिकारिक बाइनरी को उस [headless मोड](https://antigravity.google/docs/cli/headless/) में चलाता है जिसे Google स्क्रिप्ट और CI के लिए प्रलेखित करता है। Google के एक सदस्य ने अपने स्वयं के कार्य के लिए स्थानीय स्क्रिप्ट से `agy -p` चलाने को "मानक" माना है ([आधिकारिक फ़ोरम, 25 सितंबर 2026, गैर-बाध्यकारी उत्तर](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)); कोई भी दस्तावेज़ इस तरह के वितरित टूल के मामले पर स्पष्ट निर्णय नहीं देता है।

**केवल सार्वजनिक दस्तावेज़।** उन्हीं शर्तों के अनुभाग 5 के अनुसार, सशुल्क सदस्यता सहित, संचार — प्रॉम्प्ट, प्रतिक्रियाएं, मेटाडेटा — का उपयोग Google के उत्पादों और मशीन लर्निंग को बेहतर बनाने के लिए किया जा सकता है और मनुष्यों द्वारा उनकी समीक्षा की जा सकती है। इससे ऑप्ट-आउट करना अप्रलेखित प्रभाव वाली सेटिंग `enableTelemetry` के माध्यम से होता है, जिसे aipmt सेट नहीं करता है; आपकी agy सेटिंग्स इसके आइसोलेशन में लागू नहीं होती हैं। इसके माध्यम से कुछ भी गोपनीय न भेजें।

### Claude सदस्यता पर: `--use_claude_code`

वही सिद्धांत `claude` के साथ भी लागू होता है, जो `-p` मोड में Claude Code का आधिकारिक CLI है: जो कोई भी Claude Pro या Max का भुगतान करता है, उसके लिए अनुवाद टोकन के अनुसार बिल किए जाने के बजाय सदस्यता कोटा से घटाया जाता है। इसे `--use_claude` के साथ भ्रमित न करें, जो Anthropic का API है और उपयोग के आधार पर बिल किया जाता है।

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **कोई भी सशुल्क मार्ग खुला नहीं रहता है, और प्रत्येक कॉल इसे प्रमाणित करता है।** Claude
  Code आपके परिवेश से केवल चरों की एक बंद सूची प्राप्त करता है — न कोई
  API कुंजी, न टोकन, न क्लाउड प्रदाता, और न ही उस Claude Code सत्र का कोई मार्कर
  जहाँ से aipmt लॉन्च किया गया हो। पहले सेगमेंट से पहले, `claude auth status` को
  Console कुंजी के बिना सदस्यता कनेक्शन दिखाना चाहिए, और `/usage`, जिसमें कोई
  कोटा खर्च नहीं होता, इसे प्रमाणित करना चाहिए; प्रत्येक कॉल बदले में अपने
  आरंभीकरण इवेंट में इसे प्रमाणित करता है, अन्यथा प्रतिक्रिया अस्वीकार कर दी जाती है।
- **« extra usage » को अक्षम करें** (claude.ai, सेटिंग्स → उपयोग) ताकि
  शून्य यूरो का नियम बना रहे: सक्रिय होने पर, यह समाप्त हो चुकी विंडो की जगह ले लेता है और
  बिना कोई त्रुटि दिखाए बिलिंग शुरू कर देता है। aipmt किसी कॉल के कोटा विवरण द्वारा
  संकेत मिलते ही अनुवाद रोक देता है, लेकिन वह कॉल पहले ही गिना जा चुका होता है।
- **आपके Claude Code सत्रों के साथ साझा कोटा।** प्रत्येक कॉल 5 घंटे और
  साप्ताहिक विंडो के उपयोग की रिपोर्ट करता है; 80% (`AIPMT_CLAUDE_MAX_UTILIZATION`) से अधिक होने पर,
  कोई अन्य सेगमेंट लॉन्च नहीं किया जाता है, ताकि
  आपके काम में आने वाला कोटा समाप्त न हो।
- **कन्फ़ाइनमेंट (Confinement)।** प्रत्येक कॉल बिना किसी टूल के, एक निजी और
  डिस्पोजेबल डायरेक्टरी में, बिना किसी कस्टमाइज़ेशन मोड में चलता है: न तो आपके `CLAUDE.md`, न ही आपके प्लगइन्स,
  हुक्स, MCP सर्वर या सेटिंग्स लोड होते हैं, और सत्र का
  कुछ भी सहेजा नहीं जाता है। अटैचमेंट्स काट दिए जाते हैं: आपके दस्तावेज़ में एक `@chemin`
  टेक्स्ट ही बना रहता है और कोई फ़ाइल नहीं खोलता (परीक्षित)।
- **मॉडल**: डिफ़ॉल्ट रूप से `sonnet`, प्रयास `low` पर, और `--eco` में भी:
  `--eco` इस पथ पर कुछ भी नहीं बदलता है। समान दस्तावेज़ों पर मापे जाने पर, `haiku`
  दोगुना धीमा है — यह बिना रोके विचार करता रहता है — और
  इसकी लागत मुश्किल से ही कम है, और `opus` जीव विज्ञान से संबंधित सामग्री को अस्वीकार कर देता है (अगला
  बिंदु)। दोनों `--model` के माध्यम से सुलभ रहते हैं; ये उपनाम अपने
  परिवार के नवीनतम मॉडल का अनुसरण करते हैं। `fable` और `[1m]` वेरिएंट अस्वीकार कर दिए जाते हैं,
  क्योंकि वे सशुल्क क्रेडिट में चले जाते हैं। `--reasoning_effort` प्रयास को नियंत्रित करता है,
  जिससे अनुवाद को कोई लाभ नहीं होता: मापा गया रीज़निंग लगभग नगण्य है।
- **Opus कुछ जीव विज्ञान सामग्री को अस्वीकार करता है।** इसके सुरक्षा उपाय
  Sonnet की तुलना में अधिक सख्त हैं, और Anthropic का त्रुटि संदेश चेतावनी देता है कि वे
  « can sometimes flag biology-research-adjacent work »। मापा गया परिणाम: 279 जनरेटेड अणुओं पर
  एक संक्षिप्त निगरानी नोट के कारण लेख को चौदह
  भाषाओं में अस्वीकार कर दिया गया। कुछ भी नहीं लिखा गया: aipmt कटी हुई प्रतिक्रिया को अस्वीकार करता है,
  सुरक्षा उपायों का नाम बताता है और `--model sonnet` की सलाह देता है।
- CI में (`CI` या `GITHUB_ACTIONS` परिभाषित होने पर) और Windows के तहत (परीक्षण नहीं किया गया) अस्वीकृत।
- चर: `AIPMT_CLAUDE_BIN` (अन्यथा `PATH`, फिर `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (डिफ़ॉल्ट 0.8), `CLAUDE_CONFIG_DIR` (Claude Code
  खाता, कभी किसी प्रोजेक्ट `.env` से नहीं लिया गया); कार्य डायरेक्टरीज़
  `XDG_CACHE_HOME/aipmt/claude-code` के अंतर्गत (डिफ़ॉल्ट `~/.cache`)।

**उपयोग की शर्तें: यह आपका खाता है जो इसमें शामिल है।**
[Claude Code का कानूनी पृष्ठ](https://code.claude.com/docs/en/legal-and-compliance)
« an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription » को नहीं रोकता है: aipmt यही करता है, जो
आधिकारिक बाइनरी लॉन्च करता है और कभी टोकन नहीं पढ़ता। लेकिन Anthropic « does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users », तीसरे पक्ष के टूल के लिए API कुंजी को प्राथमिकता देता है,
« including open-source projects », और सशुल्क क्रेडिट पर उनके उपयोग की
गणना करने का अधिकार सुरक्षित रखता है
([Claude सहायता](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account))।
कोई भी पाठ ऐसे वितरित टूल के मामले पर स्पष्ट निर्णय नहीं देता है जो बाइनरी लॉन्च करता हो।

**डेटा**: Free, Pro और Max खातों पर, मॉडल प्रशिक्षण
Claude Code पर भी लागू होता है जब गोपनीयता सेटिंग इसकी अनुमति देती है
([डेटा पृष्ठ](https://code.claude.com/docs/en/data-usage))। aipmt कोई भी
स्थानीय ट्रांसक्रिप्शन नहीं रखता (`--no-session-persistence`)। इसके माध्यम से
कुछ भी गोपनीय न भेजें।

### अपनी पसंद के प्रदाता की ओर: `--use_opencode`

[OpenCode](https://opencode.ai) एक ओपन सोर्स कोड एजेंट (MIT) है जो
अपने भीतर कॉन्फ़िगर किए गए प्रदाताओं को रूट करता है: API कुंजी, सदस्यता,
OpenCode Zen गेटवे (मुफ़्त मॉडल, बिना खाते के) या स्थानीय मॉडल। यहाँ दो
मार्गों का शुरू से अंत तक परीक्षण किया गया है, Zen और Ollama।

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

`--model` अनिवार्य है: इसके बिना, OpenCode एक मुफ़्त मॉडल पर वापस चला जाएगा
जिसके संवादों का उपयोग प्रशिक्षण के लिए किया जा सकता है, और यह निर्णय आपकी
जगह खुद नहीं लिया जाता।

प्रत्येक कॉल पर कन्फ़ाइनमेंट:

- एक इनलाइन कॉन्फ़िगरेशन, जो आपके कॉन्फ़िगरेशन से अधिक प्राथमिकता रखता है, एक `aipmt` एजेंट को परिभाषित करता है
  जिसके सभी टूल अस्वीकार कर दिए जाते हैं (`permission: { "*": "deny" }`), सत्र साझाकरण
  अक्षम, `--pure`, कभी `--auto` नहीं;
- डिस्पोजेबल और खाली कार्य डायरेक्टरी, `OPENCODE_DISABLE_PROJECT_CONFIG` और
  `OPENCODE_DISABLE_CLAUDE_CODE` मौजूद हैं — इनके बिना, OpenCode वर्तमान डायरेक्टरी के
  `AGENTS.md` और `~/.claude/CLAUDE.md` को प्रॉम्प्ट में इंजेक्ट कर देता है।
  ग्लोबल `~/.config/opencode/AGENTS.md` इंजेक्टेड रहता है, OpenCode इसे
  हटाने की अनुमति नहीं देता;
- आउटपुट अनुबंध: रिटर्न कोड 0, कोई `error` इवेंट नहीं, कोई टूल
  कॉल नहीं, अंतिम चरण `stop` में, गैर-रिक्त टेक्स्ट, और `aipmt` एजेंट
  वास्तव में लोड हुआ हो — एक अज्ञात `--agent` OpenCode को विफल नहीं करता, यह
  चुपचाप कोडिंग एजेंट पर वापस चला जाता है;
- कोई भी `aipmt` कुंजी पास नहीं की जाती, सिवाय `OPENCODE_API_KEY` के, जो
  स्वयं OpenCode की कुंजी है। प्रदाताओं को OpenCode में कॉन्फ़िगर किया जाता है,
  `aipmt` के `.env` में नहीं।

ध्यान देने योग्य बातें:

- Zen के मुफ़्त मॉडल परिवर्तनशील हैं, जिनकी सीमाएं अनिर्दिष्ट हैं, और
  उनके संवादों का उपयोग प्रशिक्षण के लिए किया जा सकता है: केवल सार्वजनिक दस्तावेज़ीकरण के लिए,
  निजी सामग्री के लिए नहीं।
- एक स्थानीय मॉडल को कम से कम 16 k टोकन का संदर्भ प्रदान करना चाहिए, क्योंकि सेगमेंट
  16,000 वर्णों तक के होते हैं। Ollama अक्सर 4,096 कॉन्फ़िगर करता है: `PARAMETER num_ctx 32768` के साथ
  एक `Modelfile` का उपयोग करें।
- `--eco` का कोई प्रभाव नहीं है; `--reasoning_effort` को OpenCode के
  `--variant` के रूप में ज्यों का त्यों पास किया जाता है।
- OpenCode प्रत्येक सत्र को `~/.local/share/opencode/` में लॉग करता है।
- चर: `OPENCODE_BIN` (अन्यथा `PATH`, फिर `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (प्रति सेगमेंट सेकंड, डिफ़ॉल्ट 600)। `OPENCODE_CONFIG`
  OpenCode को ज्यों का त्यों पास किया जाता है।

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

`reasoningEffort: "none"` उस रीज़निंग को बंद कर देता है जिसे Ollama इन
मॉडलों पर डिफ़ॉल्ट रूप से सक्रिय करता है, और जिसे कोई Modelfile अक्षम नहीं कर सकता। छह शब्दों के एक वाक्य पर
मापा गया परिणाम: इस विकल्प के बिना 919 रीज़निंग टोकन और 68 सेकंड, इसके साथ 9 टोकन।

### 400 से अधिक मॉडलों की ओर: `--use_openrouter`

OpenRouter तीसरे पक्ष द्वारा होस्ट किए गए मॉडलों के लिए एक सिंगल क्रेडिट पर
उपयोग-आधारित बिलिंग वाला राउटर है — जिसमें खुले चीनी मॉडल भी शामिल हैं जिन्हें
कोई अन्य प्रदाता यहाँ उपलब्ध नहीं कराता है।

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` अनिवार्य है। किसी भी बिलिंग से पहले निष्पादित एक प्रीफ़्लाइट, रूटिंग की
दो विशिष्टताओं को संभालता है:

- **एक ही मॉडल को अलग-अलग सीमाओं वाले दर्जनों होस्टों द्वारा परोसा जाता है** — `z-ai/glm-5.3-flash` पर,
  23 होस्ट जिनमें से एक 2,048 आउटपुट टोकन तक सीमित है। प्रीफ़्लाइट `/api/v1/models/{modèle}/endpoints` को पढ़ता है,
  8,000 आउटपुट टोकन से कम या ख़राब स्थिति वाले होस्टों को हटा देता है, और
  दूसरों को `allow_fallbacks: false` के साथ पिन करता है।
- **रीज़निंग का बिल आउटपुट दर पर लिया जाता है** — `z-ai/glm-5.2` की « OK » प्रतिक्रिया पर
  2 के मुकाबले 107 टोकन। इसे डिफ़ॉल्ट रूप से बंद किया गया है; जो मॉडल इसे अनिवार्य करते हैं,
  वे सबसे कम स्वीकार्य प्रयास प्राप्त करते हैं, क्योंकि कैटलॉग का डिफ़ॉल्ट
  अनुवाद समाप्त होने से पहले ही आउटपुट को संतृप्त कर सकता है।
  `--reasoning_effort` हमेशा प्राथमिकता पर रहता है।

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- कॉन्टेक्स्ट विंडो कैटलॉग से आती है। 16,400 टोकन से कम वाले मॉडल को
  किसी भी कॉल से पहले अस्वीकार कर दिया जाता है: प्रॉम्प्ट और सेगमेंट के लिए 8,400, न्यूनतम
  8,000 आउटपुट।
- कैटलॉग में अनुपलब्ध स्लग, अगम्य कैटलॉग या सीमा को पूरा करने वाले
  होस्ट की अनुपस्थिति कमांड को रोक देती है।
- खाली आउटपुट के साथ `finish_reason=length` रीज़निंग द्वारा खपत किया गया बजट है,
  कोई ट्रंकेशन नहीं: संदेश इसमें अंतर करता है।
- `--eco` का कोई प्रभाव नहीं है।
- चर: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (डिफ़ॉल्ट `https://openrouter.ai/api/v1`, `https://`
  आवश्यक), `OPENROUTER_TIMEOUT` (डिफ़ॉल्ट 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (डिफ़ॉल्ट 30)।

### अनुवाद नोट

`--add_translation_note` एक नोट जोड़ता है, `bottom` में (डिफ़ॉल्ट), `top` में (फ्रंट मैटर के बाद)
या `both` में (`--note_position`), प्रारूप `legacy` (बोल्ड पैराग्राफ, डिफ़ॉल्ट)
या `marker` (`--note_format`) में। `marker` प्रारूप एक अदृश्य Markdown
संदर्भ परिभाषा है,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
जिसके बाद एक बोल्ड कोटेशन आता है: GitHub पर पठनीय, remark प्लगइन द्वारा बिल्ड के समय उपयोग योग्य।

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## विस्तृत माप

सभी माप चौदह भाषाओं: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi में `aipmt` के साथ
वास्तव में निष्पादित अनुवाद हैं।
**लिखित** उन फ़ाइलों की गणना करता है जिन्हें सुरक्षा गार्डों ने पास होने दिया; **बिना अंतर के** वे हैं
जहाँ `scripts/compare_structure.py` कुछ भी नहीं पाता — समान संख्या में अनुभाग,
उपशीर्षक, लिंक, अद्वितीय URL, कोड ब्लॉक, इनलाइन कोड,
तालिका पंक्तियाँ, ब्लॉककोट और बोल्ड शब्द।

« बिना अंतर के » का अर्थ है « कुछ भी पता नहीं चला », न कि « पूरी तरह समान »: तुलनित्र
तत्वों की सामग्री को पढ़े बिना उनकी गणना करता है। यह न तो हटाए गए लेवल 4 के शीर्षक की रिपोर्ट करता है,
न ही बदले गए इनलाइन कोड टेक्स्ट की, न ही बदले गए फ़्लैग की, न ही एक अतिरिक्त कोष्ठक के साथ दिए गए आंतरिक लिंक की,
`[texte]((#ancre))`, जो अब कहीं नहीं ले जाता — और यह भाषा का आकलन नहीं करता है।

### सघन निगरानी लेख, मोड `--news`

[jls42.org का AI निगरानी](https://jls42.org/fr/news) संस्करण:
589 पंक्तियाँ, 140 लिंक, 21 अनुभाग, 3 सुरक्षित अंग्रेज़ी उद्धरण। 4 और 5 सितंबर 2026 का अभियान।

| मॉडल | एक्सेस | लिखित | बिना अंतर के | माध्यिका/भाषा |
| --- | --- | --- | --- | --- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1 मिनट 18 सेकंड |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google सदस्यता | 14/14 | ✅ **14/14** | 3 मिनट 59 सेकंड |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google सदस्यता | 14/14 | ✅ **14/14** | 3 मिनट 14 सेकंड |
| `claude-sonnet-5-5` | Anthropic API | 14/14 | ✅ **14/14** | 3 मिनट 37 सेकंड |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT सदस्यता | 14/14 | ✅ **14/14** | 11 मिनट 28 सेकंड |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5 मिनट 37 सेकंड |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26 मिनट 23 सेकंड |
| `sonnet` (`--use_claude_code`) | Claude सदस्यता | 14/14 | ⚠️ 13/14 | 6 मिनट 49 सेकंड |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6 मिनट 31 सेकंड |
| `haiku` (`--use_claude_code`) | Claude सदस्यता | 14/14 | ⚠️ 11/14 | 15 मिनट 54 सेकंड |
| `claude-haiku-5-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 2 मिनट 54 सेकंड |
| `claude-haiku-4-5` | Anthropic API | 14/14 | ⚠️ 7/14 | 6 मिनट 00 सेकंड |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9 मिनट 27 सेकंड |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10 मिनट 09 सेकंड |
| `ollama/gpt-oss-20b-32k` | स्थानीय | 10/14 | ❌ 7/14 | 12 मिनट 39 सेकंड |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5 मिनट 32 सेकंड |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37 मिनट 27 सेकंड |
| `grok-4.6` (`--use_grok_cli`) | Grok सदस्यता | 1/14 | ❌ 1/14 | 23 मिनट 11 सेकंड |
| `opus` (`--use_claude_code`) | Claude सदस्यता | 0/14 | ❌ 0/14 | — |

Grok को 9 सितंबर को उसी निगरानी के दूसरे संस्करण (356 पंक्तियाँ) पर पुनः मापा गया:
14 में से 9 भाषाएँ लिखी गईं, 8 बिना किसी अंतर के। यही आंकड़ा शीर्ष तालिका में दिखाई देता है।
तीन बाधित अभियानों को नोट नहीं किया गया है: क्रेडिट की कमी के कारण `qwen3.5-27b` (9 भाषाएँ) और
`kimi-k2.6` (4), तथा `z-ai/glm-5.3-flash` जिसकी दोनों विफलताएं एक रीज़निंग सेटिंग के कारण थीं
जिसे प्रदाता तब से ठीक कर रहा है। OpenRouter पंक्तियों को `--use_openrouter` से पहले, राउटर की
डिफ़ॉल्ट सेटिंग्स पर मापा गया था; `z-ai/glm-5.2`,
जिसे दिए गए प्रदाता के साथ पुनः मापा गया, वही 14/14 देता है। आंकड़ों की गणना
वर्तमान तुलनित्र के साथ 10 सितंबर को फिर से की गई थी: `qwen3.8-flash` और
`qwen3.7-flash` प्रत्येक पहले प्रकाशन की तुलना में एक भाषा प्राप्त करते हैं, अन्य अपरिवर्तित हैं।

`--use_antigravity` पंक्तियों को 26 सितंबर को उसी लेख पर मापा गया था,
चार समानांतर अनुवाद: सुबह `gemini-3.7-flash-medium`, दोपहर में `gemini-3.8-flash-medium`।
अंग्रेज़ी में, प्रत्येक ने उद्धरणों के नीचे फ्रेंच अनुवाद की तीन पंक्तियों को स्वयं हटा दिया,
बिना कोई फ़्लैग बनाए, और अंग्रेज़ी उद्धरण बरकरार हैं: फ़ॉलबैक सफ़ाई को
कुछ भी करने की आवश्यकता नहीं पड़ी। `--eco` (`gemini-3.7-flash-low`) में, केवल चार भाषाओं
(en, ja, ar, hi) पर: 4 में से 4 लिखी गईं, सभी बिना किसी अंतर के, 1 मिनट 52 सेकंड की
माध्यिका। उसी दिन 25 सितंबर वाले निगरानी के एक नवीनतम संस्करण (438 पंक्तियाँ, 2 अंग्रेज़ी उद्धरण) पर
पुनः परीक्षण किया गया, जिसका अनुवाद ब्लॉग के बाहर `gemini-3.7-flash-medium` द्वारा किया गया:
14 में से 14 लिखी गईं, सभी बिना किसी अंतर के, प्रति भाषा 87 से 128 सेकंड।

`--use_claude_code` पंक्तियों को 26 सितंबर को उसी लेख पर मापा गया था,
चार समानांतर अनुवाद, प्रयास `low` पर। `sonnet` के साथ,
चौदह भाषाओं में अंग्रेज़ी उद्धरण बरकरार हैं और, अंग्रेज़ी में, मॉडल ने
बिना कोई फ़्लैग बनाए स्वयं फ्रेंच अनुवाद की पंक्तियों को हटा दिया। `opus` ने
कोई भी भाषा नहीं लिखी: प्रत्येक में, इसके सुरक्षा उपायों ने एक बाइंडिंग साइट के लिए जनरेट किए गए
279 अणुओं के एक संक्षिप्त नोट के कारण अंतिम सेगमेंट पर प्रतिक्रिया रोक दी।
अकेले भेजे जाने पर, इस संक्षिप्त नोट को « bio » श्रेणी के तहत अस्वीकार कर दिया जाता है;
`sonnet` ने इसका हर जगह अनुवाद किया। `haiku` चौदह भाषाएँ लिखता है;
तीन (en, pl, ro) में, एक अनुभाग का शीर्षक लेवल 2 से लेवल 1 पर चला जाता है।
यह बिना रोके विचार करता है — इसके आउटपुट टोकन का 61% —, इसलिए `sonnet` की तुलना में दोगुने से अधिक समय लगता है।

`claude-sonnet-5-5`, `claude-haiku-5-5` और `claude-haiku-4-5` पंक्तियों को
18 अक्टूबर को Anthropic API द्वारा उसी लेख पर मापा गया था, प्रति मॉडल चार
समानांतर अनुवाद। Sonnet 5.5 अपने रीज़निंग को बंद करने से इनकार करता है:
aipmt इसे सबसे कम स्वीकार्य सेटिंग भेजता है, और इसकी प्रतिक्रियाओं में
कोई रीज़निंग नहीं होती है। यह बिना किसी अंतर के और किसी सेगमेंट को दोबारा चलाए बिना
चौदह भाषाएँ लिखता है; अंग्रेज़ी में, इसने बिना कोई फ़्लैग बनाए स्वयं फ्रेंच अनुवाद की
पंक्तियों को हटा दिया, और अंग्रेज़ी उद्धरण हर जगह बरकरार हैं। Haiku 5.5 को इसके अनुकूली रीज़निंग
के साथ मापा जाता है: रीज़निंग बंद होने पर, इसने पूरे पैराग्राफ फ्रेंच में छोड़ दिए,
जिन्हें गार्ड अस्वीकार कर देता है — 14 में से 3 भाषाएँ लिखी गईं। दोनों Haiku एक ही संक्षिप्त नोट पर
अटक जाते हैं: Haiku 5.5 जापानी, कोरियाई और चीनी में इसके शीर्षक का स्तर बदल देता है या इसे दोगुना कर देता है,
Haikiku 4.5 इसे सात भाषाओं में स्तर 1 पर ले जाता है, और जापानी में इसे फ्रेंच में छोड़ देता है।
Haiku 4.5 की लागत चौदह भाषाओं में दोनों दस्तावेज़ों के लिए $3.67, Haiku 5.5 की $0.57,
Sonnet 5.5 की $9.21 आती है।

### इस प्रोजेक्ट का README, मानक Markdown

9 सितंबर 2026 को फ़्रीज़ किया गया रिविज़न: 785 पंक्तियाँ, 285 इनलाइन कोड, 40
ब्लॉक क्लोज़र, 89 टेबल पंक्तियाँ। समानांतर में चार अनुवाद।

| मॉडल                                          | लिखित | बिना अंतर | माध्यिका/भाषा | क्या भिन्न है                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | कुछ नहीं                                                                 |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | कुछ नहीं                                                                 |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | तुलनकर्ता के लिए कुछ नहीं; आंतरिक लिंक दोगुने हो गए (en)                |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | कुछ नहीं                                                                 |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | कुछ नहीं                                                                 |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | एक शब्द बोल्ड में (ja)                                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | एक शब्द बोल्ड में (ko)                                                   |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | टेबल की एक पंक्ति पिछली पंक्ति से जुड़ गई (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | एक लिंक (sv), एक शब्द बोल्ड में (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | एक शब्द बोल्ड में (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | एक शब्द बोल्ड में (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | अरबी में 40 इनलाइन कोड जोड़े गए; बोल्ड (hi, ja, ko)                      |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 भाषाएँ अस्वीकृत (ar, hi): वापसी पर कुछ इनलाइन कोड खो गए               |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | एक अनुभाग खो गया (ar, hi, ko); कोड ब्लॉक जोड़े गए (ja, ko, ro, zh)       |

दो बाधित अभियानों को नोट नहीं किया गया है: Grok, बारह भाषाओं के बाद CLI सत्र समाप्त
हो गया (ग्यारह बिना अंतर के), और `qwen3.8-flash`, दो के बाद इसके होस्ट से
HTTP 429। `opencode/mimo-v2.5-free` और `ollama/gpt-oss-20b-32k` को इस रिविज़न पर फिर से
नहीं मापा गया; 4 और 5 सितंबर वाले रिविज़न पर, जो 277 पंक्तियाँ छोटा था, वे
प्रत्येक 14 में से 9 अनुवाद लिखते थे, जिनमें क्रमशः 7 और 1 बिना अंतर के थे।

`--use_antigravity` और `--use_claude_code` पंक्तियों को फ़्रीज़ किए गए रिविज़न पर
नहीं मापा गया था, बल्कि 26 सितंबर को 1.14.0 के साथ प्रकाशित रिविज़न पर — और
पंक्तियाँ `claude-sonnet-5-5`, `claude-haiku-5-5` और `claude-haiku-4-5` को 18
अक्टूबर को उसी रिविज़न पर: 600 पंक्तियाँ, 257 इनलाइन कोड, 30 ब्लॉक क्लोज़र, 85
टेबल पंक्तियाँ। 185 पंक्तियाँ
छोटी होने के कारण, इसकी अन्य पंक्तियों से सीधे तौर पर तुलना नहीं की जा सकती;
हालाँकि इन पंक्तियों की आपस में तुलना की जा सकती है। आंतरिक लिंक पर, जिन्हें
तुलनकर्ता जाँचना नहीं करता, `gemini-3.8-flash-medium` ने उन्हें चौदह भाषाओं में
अक्षुण्ण रखा, `gemini-3.7-flash-medium` ने उन्हें इतालवी में तोड़ दिया;
`sonnet` और `opus` ने उन्हें हर जगह अक्षुण्ण रखा, `haiku` ने उन्हें
अंग्रेज़ी में दोगुना कर दिया; `claude-sonnet-5-5` और `claude-haiku-4-5` ने उन्हें
चौदह भाषाओं में अक्षुण्ण रखा, `claude-haiku-5-5` ने अपने द्वारा लिखी गई बारह भाषाओं में।

### प्रसिद्ध प्रोजेक्ट्स के चार README

FastAPI, Ollama, tldr-pages और Vue.js, जिन्हें GitHub से जैसा है वैसा ही लिया गया — पिछले
दो की तुलना में आसान दस्तावेज़। इस अभियान का उद्देश्य कठिनाई का सामना करने वाले
मॉडलों का परीक्षण करना था; Gemini यहाँ तुलना के बिंदु के रूप में कार्य करता है।

| मॉडल                    | दायरा                      | लिखित | बिना अंतर   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 प्रोजेक्ट × 14 भाषाएँ     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 प्रोजेक्ट × 14 भाषाएँ     | 55/56   | ❌ 47/56     |
| `grok-4.6` (सदस्यता)   | 4 प्रोजेक्ट × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 प्रोजेक्ट × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### ये माप क्या नहीं हैं

- **कोई संपूर्ण रैंकिंग नहीं**: अकेले OpenRouter चार सौ से अधिक मॉडल
  पेश करता है, जिनमें से लगभग पंद्रह का ही परीक्षण किया गया था।
- **सांकेतिक अवधियाँ**: अभियानों के आधार पर समानांतर में तीन से छह अनुवाद,
  और प्रदाता का थ्रूपुट दिन भर में बदलता रहता है।
- **समय-विशिष्ट अवलोकन**: एक ही नाम के तहत मॉडल बदलते रहते हैं, और आपके
  दस्तावेज़ हमारे दस्तावेज़ों जैसे नहीं हैं।

अपने दस्तावेज़ों पर, फ़ाइल की किसी फ़्रीज़ की गई प्रति पर माप दोहराने के लिए:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## योगदान देना

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

दोनों पंक्तियाँ आवश्यक हैं: `pip install -e .` के बिना, `python -m aipmt`
उत्तर देता है `No module named aipmt`।

गुणवत्ता टूलिंग, वैकल्पिक लेकिन अनुशंसित:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

रिपॉजिटरी के 28 अनुवाद (README और CHANGELOG, चौदह भाषाएँ)
`./regen_translations.sh --force` के साथ फिर से जनरेट होते हैं — डिफ़ॉल्ट रूप से ChatGPT सदस्यता पर Codex और `gpt-6.1-sol`,
समानांतर में चार। `REGEN_PROVIDER` और `REGEN_MODEL` पथ बदलते हैं: `antigravity` एक सदस्यता पर रहता है, जो
Google की है, और बिना किसी छूट के पास हो जाता है; एक बिल योग्य API (`openai`, `gemini`,
`grok`, `openrouter`) को `REGEN_ALLOW_PAID_API=1` के बिना अस्वीकार कर दिया जाता है;
`REGEN_JOB_TIMEOUT` प्रत्येक कार्य को सीमित करता है (Codex और Antigravity पर 600 s, 1 800 s)।
टूलिंग का विवरण `CLAUDE.md` में है।

## इस स्क्रिप्ट का उपयोग करने वाले प्रोजेक्ट्स

- **[jls42.org](https://jls42.org)** — 15 भाषाओं में प्रकाशित व्यक्तिगत ब्लॉग। इसकी
  [दैनिक AI निगरानी](https://jls42.org/fr/news) का अनुवाद इस टूल द्वारा प्रतिदिन
  किया जाता है, और यह उपरोक्त मापों के लिए संदर्भ दस्तावेज़ के रूप में कार्य करता है।

## लेखक

Julien LE SAUX
ईमेल: contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE संस्करण 3। देखें [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)।

## चेतावनी

यह प्रोग्राम GPL v3 की धारा 15 और 16 की शर्तों के तहत **बिना किसी वारंटी के**
वितरित किया जाता है: "जैसा है" प्रदान किया जाता है, व्यापारिकता या किसी विशेष
उद्देश्य के लिए उपयुक्तता की किसी भी वारंटी के बिना, और इसके लेखक को इसके
उपयोग से होने वाले किसी भी नुकसान के लिए उत्तरदायी नहीं ठहराया जा सकता है। लाइसेंस का
मूल पाठ इस सारांश पर प्रभावी होता है।

- **प्रकाशित करने से पहले पुनः पढ़ें।** सुरक्षा उपाय कोड ब्लॉक,
  इनलाइन कोड, URL, एंकर और `--news` मोड के उद्धरणों को कवर करते हैं — न कि
  शीर्षकों, टेबल, फ़्रंट मैटर या आपके वाक्यों के अर्थ को।
- **आपके दस्तावेज़ चुने गए प्रदाता के पास जाते हैं**, उसकी उपयोग की शर्तों
  और डेटा नीति के तहत। कुछ मुफ़्त मॉडल आपके संवादों का उपयोग प्रशिक्षण के लिए
  पुनः कर सकते हैं, और Antigravity की शर्तें Google को उनका पुनः उपयोग करने और मनुष्यों द्वारा
  उनकी समीक्षा कराने की अनुमति देती हैं, जिसमें सशुल्क सदस्यता भी शामिल है; एक स्थानीय मॉडल ही
  एकमात्र ऐसा तरीका है जिससे कोई भी डेटा आपकी मशीन से बाहर नहीं जाता है।
- **API कॉल के लिए आपसे शुल्क लिया जाता है।** यह प्रोग्राम खर्च की
  कोई सीमा तय नहीं करता: लंबा दस्तावेज़, विफलता के बाद पुनः प्रयास या अत्यधिक विचार
  करने वाले मॉडल की लागत अधिक होती है।
- **प्रकाशित माप समय-विशिष्ट अवलोकन हैं**, कोई गारंटी नहीं।

उल्लिखित उत्पादों और कंपनियों के नाम उनके संबंधित स्वामियों के हैं।
यह प्रोजेक्ट इनमें से किसी से भी संबद्ध नहीं है।

**gemini-3.8-flash-medium के साथ fr से hi में अनुवादित लेख।**
