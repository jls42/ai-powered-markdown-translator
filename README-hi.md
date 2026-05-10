# Markdown का एआई-संचालित अनुवादक

🌍 [फ़्रेंच](README.md) | [अंग्रेज़ी](README-en.md) | [स्पेनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

<h4 align="center">📊 कोड की गुणवत्ता</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="गुणवत्ता गेट स्थिति"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="सुरक्षा रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="विश्वसनीयता रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="रखरखाव योग्यता रेटिंग"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="कवरेज"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="कमजोरियाँ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="बग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="कोड की गंध"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="डुप्लिकेट पंक्तियाँ (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="तकनीकी ऋण"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="कोड की पंक्तियाँ"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy बैज"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइलों का अनुवादक।

यह Python स्क्रिप्ट स्रोत भाषा से लक्षित भाषा में Markdown फ़ाइलों का अनुवाद करती है, जबकि फ़ॉर्मेटिंग, कोड ब्लॉक और front matter मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **बहु-प्रदाता**: 4 APIs (OpenAI, Mistral, Claude, Gemini) का समर्थन
- **2026 मॉडल**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **किफायती मोड**: तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: एक फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **बुद्धिमान विभाजन**: मॉडल-आधारित टोकन सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और इनलाइन कोड (`` `...` ``) सुरक्षित रखे जाते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **न्यूज़ मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों की सुरक्षा और भाषा-आधारित झंडों को संभालने के लिए `--news` विकल्प
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

यह प्रोजेक्ट खराब फ़ॉर्मेट किए गए, असुरक्षित या सीक्रेट वाले कोड को कमिट होने से रोकने के लिए [`pre-commit`](https://pre-commit.com) का उपयोग करता है। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (जटिलता), detect-secrets (API कुंजियाँ), mypy (क्रमिक टाइपिंग), Opengrep (SAST), pip-audit (CVE deps), unittest. विवरण के लिए `CLAUDE.md` अनुभाग _Quality / pre-commit_ देखें।

## कॉन्फ़िगरेशन

प्रोजेक्ट की मूल निर्देशिका में एक `.env` फ़ाइल बनाएँ या पर्यावरण चर निर्धारित करें:

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

### एक निर्देशिका का अनुवाद करें

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

तेज़ और कम लागत वाले मॉडल (gpt-5.4-mini, claude-haiku, gemini-flash) का उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद के लिए एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलों वाली स्रोत निर्देशिका                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट निर्देशिका                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्षित भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                             |
| `--eco`                  | किफायती मॉडल का उपयोग करें                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करें                                                |
| `--use_claude`           | Claude API का उपयोग करें                                                    |
| `--use_gemini`          | Gemini API का उपयोग करें                                                    |
| `--force`                | पुनः-अनुवाद को बाध्य करें                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखें                                     |
| `--news`                 | न्यूज़ मोड: EN उद्धरणों की सुरक्षा करता है, भाषा-आधारित झंडों को संभालता है |
| `--add_translation_note` | एक अनुवाद नोट जोड़ें                                           |
| `--note_position`        | नोट की स्थिति: `top`, `bottom` (डिफ़ॉल्ट), या `both`                |
| `--note_format`          | नोट का प्रारूप: `legacy` (डिफ़ॉल्ट, मोटा पैराग्राफ) या `marker`       |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल का नाम शामिल करें                       |

### अनुवाद नोट: स्थान और प्रारूप

`--add_translation_note` के साथ, translator नोट को ऊपर, नीचे, या दोनों जगह रख सकता है, और उसे या तो सादा-पाठ प्रारूप (पिछड़ी संगत) में या Markdown प्लगइन द्वारा उपभोग्य `marker` प्रारूप में प्रस्तुत कर सकता है।

**स्थिति** (`--note_position`) :

- `bottom` (डिफ़ॉल्ट) : नोट फ़ाइल के अंत में, जैसा कि पारंपरिक रूप से होता आया है।
- `top` : नोट **YAML frontmatter के बाद** डाला जाता है (Astro Content Collections, gray-matter आदि के लिए सुरक्षा)।
- `both` : नोट ऊपर और नीचे दोनों जगह डाला जाता है (एक ही LLM कॉल, दोनों स्थानों के लिए पुनः उपयोग होने वाली सामग्री)।

**प्रारूप** (`--note_format`) :

- `legacy` (डिफ़ॉल्ट) : मोटा `**...**` पैराग्राफ — v1.8 के समान, byte-for-byte. Hugo, GitHub, GitLab, और किसी भी Markdown renderer के साथ संगत।
- `marker` : Markdown अदृश्य लिंक संदर्भ परिभाषा (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) जिसके बाद एक मोटा blockquote आता है। GitHub/GitLab पर मूल रूप से पठनीय, और Astro साइड remark प्लगइन द्वारा build के समय एक स्टाइलिश बैनर बनाने के लिए उपयोगी (cf. blog jls42.org)।

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### डिफ़ॉल्ट मॉडल (2026)

| प्रदाता | गुणवत्ता (डिफ़ॉल्ट)         | किफायती (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **दीर्घ-रूप अनुवादों के लिए अनुशंसा** : `--use_gemini` (डिफ़ॉल्ट = `gemini-3.1-pro-preview` गुणवत्ता, `--eco` = `gemini-3.1-flash-lite-preview`) गैर-लैटिन लिपियों (PL, JA, ZH, AR, HI) पर Markdown संरचना को बेहतर बनाए रखने की प्रवृत्ति रखता है, विशेष रूप से `--news` मोड में जहाँ placeholders की निष्ठा महत्वपूर्ण होती है। पिछड़ी संगतता के लिए OpenAI अभी भी डिफ़ॉल्ट है।

## इस स्क्रिप्ट का उपयोग करने वाले प्रोजेक्ट

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX  
ईमेल : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE संस्करण 3. देखें [LICENSE](LICENSE).

**जीपीटी-5.4-मिनी के साथ फ्र से हिंदी में अनूदित लेख।**
