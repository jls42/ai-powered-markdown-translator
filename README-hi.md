# AI-संचालित Markdown अनुवादक

🌍 [फ़्रेंच](README.md) | [अंग्रेज़ी](README-en.md) | [स्पेनी](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

<h4 align="center">📊 कोड की गुणवत्ता</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="गुणवत्ता गेट की स्थिति"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="सुरक्षा रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="विश्वसनीयता रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="रखरखाव-योग्यता रेटिंग"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="कवरेज"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="कमज़ोरियाँ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="बग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="कोड संबंधी समस्याएँ"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="दोहराई गई पंक्तियाँ (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="तकनीकी ऋण"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="कोड की पंक्तियाँ"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy बैज"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइल अनुवादक।

यह Python स्क्रिप्ट स्वरूपण, कोड ब्लॉक और front matter मेटाडेटा को सुरक्षित रखते हुए Markdown फ़ाइलों को स्रोत भाषा से लक्ष्य भाषा में अनुवादित करती है।

## प्रमुख विशेषताएँ

- **बहु-प्रदाता**: 4 APIs (OpenAI, Mistral, Claude, Gemini) और ChatGPT सदस्यता पर Codex CLI का समर्थन
- **2026 मॉडल**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **किफ़ायती मोड**: अधिक तेज़ और कम लागत वाले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: केवल एक फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **बुद्धिमान विभाजन**: प्रत्येक मॉडल की token सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और inline code (`` `...` ``) सुरक्षित रखे जाते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **समाचार मोड**: समाचार लेखों में अंग्रेज़ी उद्धरण सुरक्षित रखने और ध्वजों को संभालने के लिए `--news` विकल्प
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद टिप्पणी**: दस्तावेज़ के अंत में वैकल्पिक टिप्पणी जोड़ना

## स्थापना

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### गुणवत्ता उपकरण (वैकल्पिक, लेकिन अनुशंसित)

यह परियोजना गलत ढंग से स्वरूपित, असुरक्षित या किसी गोपनीय जानकारी वाले कोड को commit होने से रोकने के लिए [`pre-commit`](https://pre-commit.com) का उपयोग करती है। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (जटिलता), detect-secrets (API कुंजियाँ), mypy (क्रमिक typing), Opengrep (SAST), pip-audit (निर्भरता CVE), unittest। विवरण के लिए `CLAUDE.md` का _Quality / pre-commit_ अनुभाग देखें।

## कॉन्फ़िगरेशन

परियोजना के मूल में `.env` फ़ाइल बनाएँ या environment variables परिभाषित करें:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` को `GOOGLE_API_KEY` के विकल्प के रूप में स्वीकार किया जाता है (AI
Studio परंपरा)। वैकल्पिक variables: `XAI_BASE_URL` (xAI endpoint, डिफ़ॉल्ट
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (प्रत्येक Anthropic कॉल के लिए सेकंड, डिफ़ॉल्ट
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
और `GROK_TRANSLATE_SANDBOX` (Grok CLI अनुभाग देखें)।

## उपयोग

### एक फ़ाइल का अनुवाद करना

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### किसी डायरेक्टरी का अनुवाद करना

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### अपनी ChatGPT सदस्यता पर अनुवाद करना (`--use_codex`)

यह provider किसी API कुंजी का उपयोग नहीं करता: यह आधिकारिक Codex CLI को
गैर-संवादात्मक मोड में संचालित करता है, इसलिए अनुवाद का उपयोग पहले से भुगतान की गई
ChatGPT सदस्यता (Plus, Pro, Business…) के quota में गिना जाता है। इस उपयोग के लिए
OpenAI द्वारा दस्तावेज़ित यह एकमात्र तरीका है—`~/.codex/auth.json` के tokens
API Platform कॉल को प्रमाणित नहीं करते और यह स्क्रिप्ट उन्हें कभी पढ़ती भी नहीं है।

**पूर्वापेक्षाएँ:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

बाइनरी को इस क्रम में खोजा जाता है: `CODEX_BIN` variable, `PATH`,
फिर Python package `openai-codex-cli-bin`। अंतिम वाला जानबूझकर
`requirements.txt` में नहीं है: इसका आकार लगभग 250 MB है, जिसे किसी वैकल्पिक
provider के लिए सभी उपयोगकर्ताओं पर थोपना पड़ता।

**ध्यान देने योग्य बातें:**

- **किसी API कुंजी का उपयोग नहीं किया जाता।** `OPENAI_API_KEY` और `CODEX_API_KEY` को
  subprocess के environment से हटा दिया जाता है, जिससे यह सुनिश्चित होता है कि
  `.env` में मौजूद कोई कुंजी अनुवाद को कभी भी उपयोग-आधारित बिलिंग पर
  स्विच नहीं करेगी।
- **एक segment = एक “स्थानीय संदेश”**, योजना की 5 घंटे की विंडो में।
  गुणवत्ता मॉडल (`gpt-5.6-sol`, Plus पर 10-100 संदेश/5 घंटे) के बजाय
  `--eco` (मॉडल `gpt-5.6-luna`, Plus पर 250-2 000 संदेश/5 घंटे) का उपयोग करें।
- **API कॉल से धीमा**: पूर्ण README के लिए लगभग 45 सेकंड लगते हैं, जबकि
  सीधे कॉल में कुछ सेकंड लगते हैं।
- **CI में अस्वीकृत** (`CI` या `GITHUB_ACTIONS` परिभाषित होने पर): सदस्यता-आधारित
  प्रमाणीकरण किसी साझा runner के लिए अभिप्रेत नहीं है और OpenAI सार्वजनिक
  repositories पर इस workflow की अनुशंसा नहीं करता। इस स्थिति में API कुंजी का उपयोग करें।
- Environment variables: `CODEX_BIN` (बाइनरी का स्पष्ट path) और
  `CODEX_TIMEOUT` (प्रति segment सेकंड, डिफ़ॉल्ट `600`)।

### अपनी Grok सदस्यता पर अनुवाद करना (`--use_grok_cli`)

`--use_codex` के समान सिद्धांत, आधिकारिक **Grok Build** CLI के साथ: अनुवाद की
गणना प्रति token बिलिंग के बजाय Grok सदस्यता (SuperGrok / X Premium+) में
की जाती है।

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**पृथक्करण—उपयोग से पहले पढ़ें।** यह provider संरचनात्मक रूप से `--use_codex` से
**कमज़ोर** है और यह जानबूझकर है:

- Codex `--sandbox read-only` में चलता है, जो system द्वारा लागू की गई सीमा है।
- Grok का sandbox कई आधुनिक Linux मशीनों पर **लागू नहीं हो सकता**:
  Ubuntu 24.04 से AppArmor गैर-विशेषाधिकार प्राप्त user namespaces को अवरुद्ध करता है
  और यदि `/run/podman`, `0700` में हो तो container runtime sockets की
  deny-list विफल हो जाती है। जो **अंतर्निर्मित** profile लागू नहीं हो सकती, वह
  **चुपचाप बिना पृथक्करण के** शुरू हो जाती है।
- इसलिए स्क्रिप्ट डिफ़ॉल्ट रूप से कोई profile नहीं माँगती और **कभी चुपचाप
  fallback नहीं करती**: यह चेतावनी दिखाती है। पृथक्करण CLI के `--deny`
  नियमों (जिनमें catch-all `*` शामिल है) पर आधारित है, जो एकमात्र मापी गई
  _fail-closed_ परत है—कोई अज्ञात नियम सुरक्षा को बिना बताए हटाने के बजाय
  शुरुआत को अस्वीकार कर देता है।
- OS sandbox को **अनिवार्य करने** के लिए: `GROK_TRANSLATE_SANDBOX=read-only`।
  यदि मशीन इसका पालन नहीं कर सकती तो शुरुआत विफल हो जाएगी, जो अपेक्षित
  व्यवहार है।

**Quota**: Grok pool **साप्ताहिक और साझा** है, जिसका उपयोग Chat, Imagine और
Voice भी करते हैं, और इसे पढ़ने के लिए कोई command उपलब्ध नहीं है। इसलिए batch
processing आपके संवादात्मक उपयोग को बिना किसी सूचना के कम कर सकती है—इसी कारण
concurrency को 2 तक सीमित किया गया है और `regen_translations.sh` में चेतावनी दी गई है।

अन्य variables: `GROK_BIN` (बाइनरी का path), `GROK_TIMEOUT` (डिफ़ॉल्ट 900 सेकंड)।

28 अनुवादों को पुनः उत्पन्न करने के लिए:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### किफ़ायती मोड

अधिक तेज़ और कम लागत वाले मॉडल (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite) का उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद करने के लिए एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलों वाली स्रोत डायरेक्टरी                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए आउटपुट डायरेक्टरी                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्ष्य भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट मॉडल                                             |
| `--eco`                  | किफ़ायती मॉडल का उपयोग करना                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करना                                                |
| `--use_claude`           | Claude API का उपयोग करना                                                    |
| `--use_gemini`           | Gemini API का उपयोग करना                                                    |
| `--use_codex`            | ChatGPT सदस्यता quota पर Codex CLI का उपयोग करना               |
| `--use_grok`             | xAI API (Grok) का उपयोग करना—`XAI_API_KEY` आवश्यक है                      |
| `--use_grok_cli`         | Grok सदस्यता quota पर Grok CLI का उपयोग करना                   |
| `--force`                | पुनः अनुवाद बाध्य करना                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखना                                     |
| `--news`                 | समाचार मोड: अंग्रेज़ी उद्धरणों को सुरक्षित रखता है, भाषा के अनुसार ध्वज संभालता है |
| `--add_translation_note` | अनुवाद टिप्पणी जोड़ना                                           |
| `--note_position`        | टिप्पणी का स्थान: `top`, `bottom` (डिफ़ॉल्ट), या `both`                |
| `--note_format`          | टिप्पणी का प्रारूप: `legacy` (डिफ़ॉल्ट, मोटा अनुच्छेद) या `marker`       |
| `--include_model`        | आउटपुट फ़ाइल में मॉडल का नाम शामिल करना                       |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`     |

### अनुवाद टिप्पणी: स्थान और प्रारूप

`--add_translation_note` के साथ, अनुवादक टिप्पणी को ऊपर, नीचे या दोनों स्थानों पर रख सकता है और इसे साधारण पाठ प्रारूप (पश्च-संगत) या Markdown plugin द्वारा उपयोग योग्य `marker` प्रारूप में प्रस्तुत कर सकता है।

**स्थान** (`--note_position`):

- `bottom` (डिफ़ॉल्ट): पहले की तरह फ़ाइल के अंत में टिप्पणी।
- `top`: टिप्पणी **YAML frontmatter के बाद** जोड़ी जाती है (Astro Content Collections, gray-matter आदि के लिए सुरक्षित)।
- `both`: टिप्पणी ऊपर और नीचे दोनों जगह जोड़ी जाती है (केवल एक LLM कॉल, दोनों स्थानों के लिए सामग्री का पुनः उपयोग)।

**प्रारूप** (`--note_format`):

- `legacy` (डिफ़ॉल्ट): मोटा अनुच्छेद `**...**`—v1.8 के बिल्कुल समान व्यवहार, byte-for-byte। Hugo, GitHub, GitLab और प्रत्येक Markdown renderer के साथ संगत।
- `marker`: अदृश्य Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), जिसके बाद मोटे अक्षरों में blockquote होता है। GitHub/GitLab पर मूल रूप से पठनीय और Astro की ओर remark plugin द्वारा build के समय शैलीबद्ध banner बनाने के लिए उपयोग योग्य (देखें: jls42.org ब्लॉग)।

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

| Provider | गुणवत्ता (डिफ़ॉल्ट)       | किफ़ायती (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **दीर्घ-प्रारूप अनुवादों के लिए अनुशंसा**: `--use_gemini` (डिफ़ॉल्ट = `gemini-3.7-flash`) गैर-Latin लिपियों (PL, JA, ZH, AR, HI) में Markdown संरचना को सटीकता से सुरक्षित रखता है, जिसमें `--news` मोड भी शामिल है जहाँ placeholders की विश्वसनीयता महत्त्वपूर्ण होती है। जापानी में अनुवादित इस README पर मापा गया: लगभग 6 गुना कम विलंबता में `gemini-3.1-pro-preview` के समान संरचना (21 सूचियाँ, 18 कोड ब्लॉक, 13 HTML लिंक, 13 चित्र, सभी URLs सुरक्षित)। पश्च-संगतता के लिए OpenAI डिफ़ॉल्ट बना हुआ है।

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी निजी ब्लॉग (15 भाषाएँ)

## लेखक

Julien LE SAUX
ईमेल: contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE संस्करण 3। [LICENSE](LICENSE) देखें।

**gpt-5.6-sol के साथ fr से hi में अनुवादित लेख।**
