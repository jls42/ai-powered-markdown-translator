# एआई-संचालित Markdown अनुवादक

🌍 [फ़्रेंच](README.md) | [अंग्रेज़ी](README-en.md) | [स्पेनिश](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

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

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइल अनुवादक।

यह Python स्क्रिप्ट स्रोत भाषा से लक्षित भाषा में Markdown फ़ाइलों का अनुवाद करती है, जबकि फ़ॉर्मेटिंग, कोड ब्लॉक्स और front matter मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **बहु-प्रदाता**: 4 APIs (OpenAI, Mistral, Claude, Gemini) का समर्थन
- **2026 मॉडल**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **किफायती मोड**: तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: एक ही फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **स्मार्ट सेगमेंटेशन**: मॉडल-विशिष्ट token सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक्स और इनलाइन कोड (`` `...` ``) सुरक्षित रहते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **समाचार मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों की रक्षा करने और ध्वजों को संभालने के लिए `--news` विकल्प
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

प्रोजेक्ट खराब फ़ॉर्मेटेड, असुरक्षित या गुप्त-युक्त कोड को commit करने से रोकने के लिए [`pre-commit`](https://pre-commit.com) का उपयोग करता है। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (CVE deps), unittest. विवरण के लिए `CLAUDE.md` अनुभाग _Quality / pre-commit_ देखें।

## कॉन्फ़िगरेशन

प्रोजेक्ट की root में एक `.env` फ़ाइल बनाएं या environment variables परिभाषित करें:

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

### एक directory का अनुवाद करें

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
| `--source_dir`           | Markdown फ़ाइलों वाला source directory                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए output directory                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्षित भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                             |
| `--eco`                  | किफायती मॉडल उपयोग करें                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करें                                                |
| `--use_claude`           | Claude API का उपयोग करें                                                    |
| `--use_gemini`          | Gemini API का उपयोग करें                                                    |
| `--force`                | पुनः-अनुवाद बाध्य करें                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखें                                     |
| `--news`                 | समाचार मोड: EN उद्धरणों की रक्षा करता है, भाषा के अनुसार झंडों को संभालता है |
| `--add_translation_note` | अनुवाद नोट जोड़ें                                           |
| `--note_position`        | नोट की स्थिति: `top`, `bottom` (डिफ़ॉल्ट), या `both`                |
| `--note_format`          | नोट का फ़ॉर्मेट: `legacy` (डिफ़ॉल्ट, बोल्ड पैराग्राफ) या `marker`       |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल नाम शामिल करें                       |

### अनुवाद नोट: स्थितियाँ और फ़ॉर्मेट

`--add_translation_note` के साथ, translator नोट को ऊपर, नीचे, या दोनों जगह रख सकता है, और इसे या तो साधारण पाठ फ़ॉर्मेट (backward-compatible) या Markdown प्लगइन द्वारा consumable `marker` फ़ॉर्मेट में प्रस्तुत कर सकता है।

**स्थिति** (`--note_position`) :

- `bottom` (डिफ़ॉल्ट) : नोट फ़ाइल के अंत में, जैसा कि ऐतिहासिक रूप से होता आया है।
- `top` : नोट YAML frontmatter के बाद सम्मिलित किया जाता है (Astro Content Collections, gray-matter आदि के लिए सुरक्षा)।
- `both` : नोट ऊपर और नीचे दोनों जगह सम्मिलित किया जाता है (एक ही LLM कॉल, दोनों स्थानों के लिए पुन: उपयोग किया गया content)।

**फ़ॉर्मेट** (`--note_format`) :

- `legacy` (डिफ़ॉल्ट) : बोल्ड पैराग्राफ `**...**` — v1.8 के साथ byte-for-byte बिल्कुल समान व्यवहार। Hugo, GitHub, GitLab, और किसी भी Markdown renderer के साथ संगत।
- `marker` : अदृश्य Markdown link reference definition `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` जिसके बाद एक bold blockquote आता है। GitHub/GitLab पर मूल रूप से पठनीय, और Astro-side remark plugin द्वारा build के समय उपयोग करके एक stylized banner उत्पन्न करने योग्य (cf. blog jls42.org)।

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

> **लंबे-रूप अनुवादों के लिए सिफ़ारिश** : `--use_gemini` (डिफ़ॉल्ट = `gemini-3.1-pro-preview` गुणवत्ता, `--eco` = `gemini-3.1-flash-lite-preview`) गैर-लैटिन स्क्रिप्ट्स (PL, JA, ZH, AR, HI) पर markdown संरचना को बेहतर ढंग से संरक्षित करने की प्रवृत्ति रखता है, विशेषकर `--news` मोड में जहाँ placeholders की निष्ठा महत्वपूर्ण होती है। पिछड़े अनुकूलता के लिए OpenAI डिफ़ॉल्ट बना रहता है।

## इस स्क्रिप्ट का उपयोग करने वाले प्रोजेक्ट

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX
Email : contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) देखें।

**फ्र से hi में अनुवादित लेख gpt-5.4-mini के साथ।**
