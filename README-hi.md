# AI-Powered Markdown अनुवादक

🌍 [फ़्रांसीसी](README.md) | [अंग्रेज़ी](README-en.md) | [स्पेनी](README-es.md) | [चीनी](README-zh.md) | [जर्मन](README-de.md) | [जापानी](README-ja.md) | [कोरियाई](README-ko.md) | [अरबी](README-ar.md) | [हिन्दी](README-hi.md) | [इतालवी](README-it.md) | [डच](README-nl.md) | [पोलिश](README-pl.md) | [पुर्तगाली](README-pt.md) | [रोमानियाई](README-ro.md) | [स्वीडिश](README-sv.md)

<h4 align="center">📊 कोड गुणवत्ता</h4>

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="कोड की खामियाँ"></a>
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

यह Python स्क्रिप्ट स्वरूपण, कोड ब्लॉक और front matter मेटाडेटा को सुरक्षित रखते हुए Markdown फ़ाइलों का स्रोत भाषा से लक्ष्य भाषा में अनुवाद करती है।

## प्रमुख विशेषताएँ

- **Multi-Provider**: 4 APIs (OpenAI, Mistral, Claude, Gemini) तथा ChatGPT सदस्यता पर Codex CLI का समर्थन
- **2026 मॉडल**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **किफ़ायती मोड**: अधिक तेज़ और कम खर्चीले मॉडल उपयोग करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: केवल एक फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **बुद्धिमान विभाजन**: प्रत्येक मॉडल की token सीमाओं के साथ लंबे पाठ का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और inline कोड (`` `...` ``), दोनों सुरक्षित रखे जाते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **समाचार मोड**: अंग्रेज़ी उद्धरणों को सुरक्षित रखने और समाचार लेखों में ध्वजों को संभालने के लिए `--news` विकल्प
- **.env विन्यास**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद टिप्पणी**: दस्तावेज़ के अंत में वैकल्पिक टिप्पणी जोड़ना

## स्थापना

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### गुणवत्ता उपकरण (वैकल्पिक, लेकिन अनुशंसित)

यह परियोजना गलत स्वरूपित, असुरक्षित या किसी secret वाले कोड को commit होने से रोकने के लिए [`pre-commit`](https://pre-commit.com) का उपयोग करती है। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (जटिलता), detect-secrets (API कुंजियाँ), mypy (क्रमिक typing), Opengrep (SAST), pip-audit (निर्भरता CVE), unittest। विवरण के लिए `CLAUDE.md` का _Quality / pre-commit_ अनुभाग देखें।

## विन्यास

परियोजना के मूल में `.env` फ़ाइल बनाएँ या environment variables निर्धारित करें:

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

`GOOGLE_API_KEY` के विकल्प के रूप में `GEMINI_API_KEY` स्वीकार किया जाता है (AI
Studio परंपरा)। वैकल्पिक variables: `XAI_BASE_URL` (xAI endpoint, डिफ़ॉल्ट
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (प्रत्येक Anthropic कॉल के लिए सेकंड, डिफ़ॉल्ट
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
और `GROK_TRANSLATE_SANDBOX` (Grok CLI अनुभाग देखें)। `regen_translations.sh` की ओर:
`REGEN_PROVIDER`, `REGEN_MODEL` और
`REGEN_JOB_TIMEOUT` (प्रत्येक job की अधिकतम सीमा, डिफ़ॉल्ट 600 सेकंड)।

## उपयोग

### एकल फ़ाइल का अनुवाद

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### किसी directory का अनुवाद

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
non-interactive मोड में नियंत्रित करता है, इसलिए अनुवाद का उपयोग पहले से भुगतान
की गई ChatGPT सदस्यता (Plus, Pro, Business…) के quota में गिना जाता है। इस
उपयोग के लिए OpenAI द्वारा प्रलेखित यही एकमात्र तरीका है—`~/.codex/auth.json` के
tokens API Platform कॉल को प्रमाणित नहीं करते और यह स्क्रिप्ट उन्हें कभी पढ़ती
भी नहीं है।

**पूर्वापेक्षाएँ:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

binary को इस क्रम में खोजा जाता है: `CODEX_BIN` variable, `PATH`,
फिर Python package `openai-codex-cli-bin`। अंतिम वाला जानबूझकर `requirements.txt` में
नहीं है: उसका आकार लगभग 250 MB है, जो किसी वैकल्पिक provider के लिए सभी
उपयोगकर्ताओं पर थोपा जाता।

**ध्यान देने योग्य बातें:**

- **किसी API कुंजी का उपयोग नहीं किया जाता।** `OPENAI_API_KEY` और `CODEX_API_KEY`
  को subprocess के environment से हटा दिया जाता है, जिससे यह सुनिश्चित होता है
  कि `.env` में मौजूद कोई कुंजी अनुवाद को कभी भी उपयोग-आधारित billing
  पर नहीं ले जाएगी।
- **एक segment = plan की 5 घंटे वाली window का एक « local message »।**
  quality मॉडल (`gpt-5.6-sol`, Plus पर 10-100 messages/5 h) के बजाय
  `--eco` (मॉडल `gpt-5.6-luna`, Plus पर 250-2 000 messages/5 h) का
  उपयोग करें।
- **API कॉल से धीमा**: पूर्ण README के लिए लगभग 45 सेकंड लगते हैं, जबकि सीधे
  कॉल में कुछ सेकंड लगते हैं।
- **CI में अस्वीकृत** (`CI` या `GITHUB_ACTIONS` निर्धारित होने पर):
  सदस्यता-आधारित authentication साझा runner के लिए नहीं बनाई गई है और OpenAI
  सार्वजनिक repositories पर इस workflow की अनुशंसा नहीं करता। इस स्थिति में
  API कुंजी का उपयोग करें।
- Environment variables: `CODEX_BIN` (binary का स्पष्ट path) और
  `CODEX_TIMEOUT` (प्रत्येक segment के सेकंड, डिफ़ॉल्ट `600`)।

### अपनी Grok सदस्यता पर अनुवाद करना (`--use_grok_cli`)

आधिकारिक **Grok Build** CLI के साथ `--use_codex` जैसा ही सिद्धांत: अनुवाद का
उपयोग token के अनुसार bill होने के बजाय Grok सदस्यता (SuperGrok / X Premium+)
के quota में गिना जाता है।

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**परिरोधन—उपयोग से पहले पढ़ें।** यह provider संरचनात्मक रूप से `--use_codex`
से **कमज़ोर** है, और यह जानबूझकर है:

- Codex `--sandbox read-only` में चलता है, जो system द्वारा लागू की गई सीमा है।
- कई हालिया Linux मशीनों पर Grok sandbox **लागू नहीं हो सकता**: Ubuntu 24.04
  से AppArmor unprivileged user namespaces को block करता है, और यदि
  `/run/podman`, `0700` में हो तो container runtime sockets की
  deny-list विफल हो जाती है। वहीं, लागू न हो सकने वाला **अंतर्निहित** profile
  **बिना किसी सूचना के, असंयमित रूप में** शुरू हो जाता है।
- इसलिए स्क्रिप्ट डिफ़ॉल्ट रूप से कोई profile नहीं माँगती और **कभी भी चुपचाप
  fallback नहीं करती**: वह चेतावनी दिखाती है। परिरोधन CLI के `--deny`
  नियमों (जिसमें catch-all `*` शामिल है) पर निर्भर करता है, जो मापी
  गई एकमात्र _fail-closed_ परत है—कोई अज्ञात नियम सुरक्षा को बिना बताए हटाने
  के बजाय startup को अस्वीकार कर देता है।
- OS sandbox को **अनिवार्य** करने के लिए: `GROK_TRANSLATE_SANDBOX=read-only`। यदि मशीन इसका पालन
  नहीं कर सकती, तो startup विफल हो जाएगा, जो अपेक्षित व्यवहार है।

**Quota**: Grok pool **साप्ताहिक और साझा** है तथा Chat, Imagine और Voice के साथ
उपयोग होता है; इसे पढ़ने के लिए कोई command उपलब्ध नहीं है। इसलिए batch
processing आपके conversational उपयोग को बिना किसी सूचना के कम कर सकती
है—इसी कारण concurrency 2 तक सीमित है और `regen_translations.sh` में चेतावनी दी गई है।

अन्य variables: `GROK_BIN` (binary का path), `GROK_TIMEOUT` (डिफ़ॉल्ट 900 सेकंड)।

28 अनुवादों को पुनः उत्पन्न करने के लिए:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### किफ़ायती मोड

अधिक तेज़ और कम खर्चीले मॉडल (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite) उपयोग करता है:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद की जाने वाली एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलों वाली स्रोत directory                        |
| `--target_dir`           | अनुवादित फ़ाइलों की output directory                          |
| `--source_lang`          | स्रोत भाषा (डिफ़ॉल्ट: `fr`)                                             |
| `--target_lang`          | लक्ष्य भाषा (डिफ़ॉल्ट: `en`)                                              |
| `--model`                | उपयोग किया जाने वाला विशिष्ट मॉडल                                             |
| `--eco`                  | किफ़ायती मॉडलों का उपयोग                                         |
| `--use_mistral`          | Mistral AI API का उपयोग                                                |
| `--use_claude`           | Claude API का उपयोग                                                    |
| `--use_gemini`           | Gemini API का उपयोग                                                    |
| `--use_codex`            | ChatGPT सदस्यता quota पर Codex CLI का उपयोग               |
| `--use_grok`             | xAI (Grok) API का उपयोग—`XAI_API_KEY` आवश्यक                      |
| `--use_grok_cli`         | Grok सदस्यता quota पर Grok CLI का उपयोग                   |
| `--force`                | पुनः अनुवाद को बाध्य करना                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखना                                     |
| `--news`                 | समाचार मोड: अंग्रेज़ी उद्धरण सुरक्षित रखता है, भाषा के अनुसार ध्वज संभालता है |
| `--add_translation_note` | अनुवाद टिप्पणी जोड़ना                                           |
| `--note_position`        | टिप्पणी का स्थान: `top`, `bottom` (डिफ़ॉल्ट), या `both`                |
| `--note_format`          | टिप्पणी का प्रारूप: `legacy` (डिफ़ॉल्ट, bold paragraph) या `marker`       |
| `--include_model`        | output फ़ाइल में मॉडल का नाम शामिल करना                       |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`    |

> **provider के सभी छह flags परस्पर अनन्य हैं।** पहले दो को मिलाना बिना सूचना
> के स्वीकार कर लिया जाता था और पहले जाँचे गए विकल्प को चुनता था: सदस्यता quota
> (`--use_codex`, `--use_grok_cli`) पर माँगा गया अनुवाद इस प्रकार बिना किसी
> चेतावनी के उपयोग-आधारित billing में जा सकता था।
> अब `argparse` इस संयोजन को अस्वीकार करता है।

### अनुवाद टिप्पणी: स्थान और प्रारूप

`--add_translation_note` के साथ translator टिप्पणी को ऊपर, नीचे या दोनों स्थानों पर रख सकता है और इसे सामान्य text format (पश्चगामी-संगत) या Markdown plugin द्वारा उपयोग किए जा सकने वाले `marker` format में प्रस्तुत कर सकता है।

**स्थान** (`--note_position`):

- `bottom` (डिफ़ॉल्ट): पहले की तरह फ़ाइल के अंत में टिप्पणी।
- `top`: टिप्पणी **YAML frontmatter के बाद** जोड़ी जाती है (Astro Content Collections, gray-matter आदि के लिए सुरक्षित)।
- `both`: टिप्पणी ऊपर और नीचे दोनों जगह जोड़ी जाती है (केवल एक LLM कॉल, दोनों स्थानों पर उसी content का पुनः उपयोग)।

**प्रारूप** (`--note_format`):

- `legacy` (डिफ़ॉल्ट): bold paragraph `**...**`—v1.8 के बिल्कुल समान, byte-for-byte व्यवहार। Hugo, GitHub, GitLab और प्रत्येक Markdown renderer के साथ संगत।
- `marker`: अदृश्य Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), जिसके बाद bold blockquote आता है। GitHub/GitLab पर मूल रूप से पठनीय और Astro में remark plugin द्वारा build के समय शैलीबद्ध banner बनाने के लिए उपयोग योग्य (jls42.org blog देखें)।

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

> **लंबे प्रारूप के अनुवादों के लिए अनुशंसा**: `--use_gemini` (डिफ़ॉल्ट =
> `gemini-3.7-flash`) गैर-Latin लिपियों (PL, JA, ZH, AR, HI) में markdown संरचना
> को विश्वसनीय रूप से सुरक्षित रखता है, जिसमें `--news` मोड भी शामिल है,
> जहाँ placeholders की शुद्धता महत्वपूर्ण होती है। जापानी में अनूदित इस README
> पर किए गए मापन में: `gemini-3.1-pro-preview` के समान संरचना (21 सूचियाँ, 18 कोड ब्लॉक,
> 13 HTML links, 13 images, सभी URLs सुरक्षित) और लगभग 6 गुना कम latency।
> पश्चगामी संगतता के लिए OpenAI डिफ़ॉल्ट बना हुआ है।

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी निजी blog (15 भाषाएँ)

## लेखक

Julien LE SAUX
ईमेल: contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) देखें।

**लेख का fr से hi में अनुवाद gpt-5.6-sol के साथ किया गया।**
