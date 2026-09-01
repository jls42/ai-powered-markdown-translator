# AI-संचालित Markdown अनुवादक

🌍 [फ़्रेंच](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [अंग्रेज़ी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [स्पैनिश](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [चीनी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [जर्मन](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [जापानी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [कोरियाई](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [अरबी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [इतालवी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [डच](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [पोलिश](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [पुर्तगाली](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [रोमानियाई](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [स्वीडिश](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 कोड गुणवत्ता</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="गुणवत्ता गेट स्थिति"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="सुरक्षा रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="विश्वसनीयता रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="रखरखाव क्षमता रेटिंग"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="कवरेज"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="कमज़ोरियाँ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="बग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="कोड स्मेल"></a>
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

**OpenAI**, **Mistral AI**, **Claude (Anthropic)** और **Google Gemini** का उपयोग करने वाला Markdown फ़ाइल अनुवादक।

यह Python स्क्रिप्ट Markdown फ़ाइलों का स्रोत भाषा से लक्ष्य भाषा में अनुवाद करती है और फ़ॉर्मैटिंग, कोड ब्लॉक तथा front matter मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **Multi-Provider**: 4 APIs (OpenAI, Mistral, Claude, Gemini) और ChatGPT सदस्यता वाले Codex CLI का समर्थन
- **मॉडल 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **किफ़ायती मोड**: तेज़ और कम महंगे मॉडल इस्तेमाल करने के लिए `--eco` विकल्प
- **एकल फ़ाइल**: केवल एक फ़ाइल का अनुवाद करने के लिए `--file` विकल्प
- **स्मार्ट विभाजन**: प्रत्येक मॉडल की token सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और inline code (`` `...` ``) सुरक्षित रखे जाते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए `--keep_filename` विकल्प
- **News मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों को सुरक्षित रखने और झंडों का प्रबंधन करने के लिए `--news` विकल्प
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद टिप्पणी**: दस्तावेज़ के अंत में वैकल्पिक टिप्पणी जोड़ना

## स्थापना

### टूल का उपयोग करने के लिए

```bash
pip install ai-powered-markdown-translator
```

इसके बाद `aipmt` कमांड हर जगह उपलब्ध होगी। यदि Python scripts निर्देशिका आपके `PATH` में नहीं है, तो `python -m aipmt` बिल्कुल यही काम करता है। Python 3.10 या उससे नया आवश्यक है।

अपने अन्य पैकेजों से अलग एक पृथक स्थापना के लिए:

```bash
pipx install ai-powered-markdown-translator
```

### परियोजना में योगदान देने के लिए

विकास के लिए क्लोन की गई repository आवश्यक रहती है: परीक्षण, 28 अनुवाद और सभी गुणवत्ता उपकरण वहीं मौजूद हैं।

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` पूरी तरह **pinned lock** है, जो परीक्षण किए गए environment का सटीक प्रतिबिंब है। `pyproject.toml` में प्रकाशित सीमाएँ जानबूझकर अधिक व्यापक हैं: वे आपके अन्य पैकेजों पर कोई बाध्यता नहीं डालतीं।

### गुणवत्ता उपकरण (वैकल्पिक, लेकिन अनुशंसित)

परियोजना [`pre-commit`](https://pre-commit.com) का उपयोग करती है, ताकि गलत फ़ॉर्मैट वाले, कमज़ोरियों वाले या किसी secret वाले कोड को commit करने से रोका जा सके। स्थापना:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय Hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (जटिलता), detect-secrets (API कुंजियाँ), mypy (क्रमिक typing), Opengrep (SAST), pip-audit (CVE deps), unittest। विवरण के लिए `CLAUDE.md` के _Quality / pre-commit_ अनुभाग को देखें।

## कॉन्फ़िगरेशन

कुंजियाँ **तीन स्थानों** पर खोजी जाती हैं, सबसे अधिक प्राथमिकता से सबसे कम प्राथमिकता तक।
प्रत्येक स्थान केवल वही भरता है जिसे पिछला स्थान खाली छोड़ देता है।

|     | कहाँ                                            | किस लिए                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | पर्यावरण चर                     | CI, containers, अस्थायी अपवाद |
| 2   | वर्तमान निर्देशिका (या किसी parent) की `.env` | किसी project की अपनी कुंजी            |
| 3   | `~/.config/aipmt/.env`                        | **एक बार स्थापित, हर जगह मान्य**   |

`pip install` के बाद सबसे सरल तरीका तीसरा है:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

जब variable किसी absolute path को दर्शाता है, तो यह फ़ाइल `XDG_CONFIG_HOME` का पालन करती है
(अन्यथा specification के अनुसार इसे अनदेखा किया जाता है), और Windows पर `%APPDATA%` का पालन करती है।

दूसरा तरीका तब उपयोगी रहता है जब किसी repository की अपनी कुंजी हो: उसके root में मौजूद `.env` उपयोगकर्ता कॉन्फ़िगरेशन पर प्राथमिकता पाता है, उसे बदले बिना। और environment में पहले से परिभाषित variable दोनों पर प्राथमिकता पाता है:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

यदि कोई कुंजी नहीं मिलती, तो command call trace प्रदर्शित नहीं करती: वह तीनों स्थानों को उनके सटीक path के साथ सूचीबद्ध करती है।

`GEMINI_API_KEY` को `GOOGLE_API_KEY` के विकल्प के रूप में स्वीकार किया जाता है (AI
Studio convention)। वैकल्पिक variables: `XAI_BASE_URL` (xAI endpoint, default
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (प्रति Anthropic call seconds, default
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
और `GROK_TRANSLATE_SANDBOX` (Grok CLI अनुभाग देखें)। `regen_translations.sh` की ओर से:
`REGEN_PROVIDER`, `REGEN_MODEL` और `REGEN_JOB_TIMEOUT` (प्रति job सीमा, default 600 s)।

## उपयोग

### एकल फ़ाइल का अनुवाद

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### किसी directory का अनुवाद

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### अपनी ChatGPT सदस्यता पर अनुवाद (`--use_codex`)

यह provider किसी API key का उपयोग नहीं करता: यह आधिकारिक Codex CLI को non-interactive mode में चलाता है, इसलिए अनुवाद पहले से भुगतान की गई ChatGPT सदस्यता (Plus, Pro, Business…) के quota से घटता है। इस उपयोग के लिए OpenAI द्वारा documented यही एकमात्र तरीका है — `~/.codex/auth.json` के tokens Platform API calls को authenticate नहीं करते और यह script उन्हें कभी पढ़ती भी नहीं है।

**पूर्वापेक्षाएँ:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binary को इस क्रम में खोजा जाता है: `CODEX_BIN` variable, `PATH`,
फिर Python package `openai-codex-cli-bin`। बाद वाला जानबूझकर `requirements.txt` में शामिल नहीं है:
इसका आकार लगभग 250 Mo है, जिसे एक वैकल्पिक provider के लिए सभी users पर थोपना उचित नहीं होगा।

**जानने योग्य बातें:**

- **कोई API key उपयोग नहीं की जाती।** `OPENAI_API_KEY` और `CODEX_API_KEY` को
  subprocess environment से हटा दिया जाता है, जिससे यह सुनिश्चित होता है कि
  `.env` में मौजूद key कभी भी अनुवाद को usage-based billing में न बदले।
- **एक segment = plan की 5 घंटे की window का एक « local message »**।
  गुणवत्ता वाले model (`gpt-5.6-sol`, 10-100 messages/5 h) के बजाय
  `--eco` (model `gpt-5.6-luna`, Plus पर 250-2 000 messages/5 h) का उपयोग करें।
- **API call से धीमा**: पूरे README के लिए लगभग 45 s, सीधे call में कुछ seconds की तुलना में।
- **CI में अस्वीकृत** (`CI` या `GITHUB_ACTIONS` परिभाषित होने पर): subscription authentication shared runner के लिए नहीं है, और OpenAI public repositories पर इस workflow की अनुशंसा नहीं करता। इस path पर API key का उपयोग करें।
- Environment variables: `CODEX_BIN` (binary का स्पष्ट path) और
  `CODEX_TIMEOUT` (प्रति segment seconds, default `600`)।

### अपनी Grok सदस्यता पर अनुवाद (`--use_grok_cli`)

`--use_codex` के समान सिद्धांत, आधिकारिक **Grok Build** CLI के साथ: अनुवाद token के आधार पर bill होने के बजाय Grok सदस्यता (SuperGrok / X Premium+) के quota से घटता है।

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Sandbox — उपयोग से पहले पढ़ें।** यह provider संरचनात्मक रूप से **`--use_codex` से अधिक कमज़ोर** है, और यह जानबूझकर ऐसा है:

- Codex `--sandbox read-only` में चलता है, जो system द्वारा लागू की गई सीमा है।
- हाल के कई Linux systems पर Grok का sandbox लागू नहीं हो सकता: Ubuntu 24.04 से AppArmor अप्रतिष्ठित user namespaces को रोकता है, और यदि `/run/podman` `0700` में हो, तो container runtime sockets की deny-list विफल हो जाती है। जबकि ऐसा **integrated** profile, जो लागू नहीं हो सकता, **चुपचाप बिना confinement के** शुरू हो जाता है।
- इसलिए script default रूप से कोई profile नहीं माँगती और **कभी चुपचाप fallback नहीं करती**: वह warning प्रदर्शित करती है। Confinement CLI के `--deny` नियमों (जिसमें catch-all `*` शामिल है) पर निर्भर करता है, जो एकमात्र मापी गई _fail-closed_ layer है — अज्ञात rule सुरक्षा हटाने के बजाय startup को अस्वीकार कर देता है।
- OS sandbox को **अनिवार्य** करने के लिए: `GROK_TRANSLATE_SANDBOX=read-only`। यदि machine इसे लागू नहीं कर सकती, तो startup विफल होगा; यही अपेक्षित व्यवहार है।

**Quota**: Grok pool **साप्ताहिक और साझा** है, Chat, Imagine और Voice के साथ, और इसे पढ़ने के लिए कोई command उपलब्ध नहीं है। इसलिए batch processing आपके conversational usage को बिना किसी संकेत के कम कर सकती है — इसी कारण concurrency 2 तक सीमित है और `regen_translations.sh` में warning दी जाती है।

अन्य variables: `GROK_BIN` (binary path), `GROK_TIMEOUT` (default 900 s)।

28 अनुवादों को फिर से बनाने के लिए:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### किफ़ायती मोड

तेज़ और कम महंगे मॉडल का उपयोग करता है (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प                   | विवरण                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | अनुवाद करने के लिए एकल Markdown फ़ाइल                                       |
| `--source_dir`           | Markdown फ़ाइलों वाली स्रोत directory                        |
| `--target_dir`           | अनुवादित फ़ाइलों के लिए output directory                          |
| `--source_lang`          | स्रोत भाषा (default: `fr`)                                             |
| `--target_lang`          | लक्ष्य भाषा (default: `en`)                                              |
| `--model`                | उपयोग करने के लिए विशिष्ट model                                             |
| `--eco`                  | किफ़ायती models का उपयोग करना                                         |
| `--use_mistral`          | Mistral AI API का उपयोग करना                                                |
| `--use_claude`           | Claude API का उपयोग करना                                                    |
| `--use_gemini`           | Gemini API का उपयोग करना                                                    |
| `--use_codex`            | ChatGPT सदस्यता quota पर Codex CLI का उपयोग करना               |
| `--use_grok`             | xAI (Grok) API का उपयोग करना — `XAI_API_KEY` आवश्यक                      |
| `--use_grok_cli`         | Grok सदस्यता quota पर Grok CLI का उपयोग करना                   |
| `--force`                | पुनः अनुवाद को बाध्य करना                                                  |
| `--keep_filename`        | मूल फ़ाइल नाम बनाए रखना                                     |
| `--news`                 | समाचार मोड: EN उद्धरण सुरक्षित करता है, भाषा के अनुसार झंडों का प्रबंधन करता है |
| `--add_translation_note` | अनुवाद टिप्पणी जोड़ना                                           |
| `--note_position`        | टिप्पणी की स्थिति: `top`, `bottom` (default), या `both`                |
| `--note_format`          | टिप्पणी का प्रारूप: `legacy` (default, bold paragraph) या `marker`       |
| `--include_model`        | output फ़ाइल में model का नाम शामिल करना                       |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`    |

> **छह provider flags परस्पर बहिष्कृत हैं।** पहले दो को एक साथ इस्तेमाल करना चुपचाप स्वीकार किया जाता था और पहले जाँचे गए विकल्प पर resolve होता था: subscription quota पर माँगा गया अनुवाद (`--use_codex`, `--use_grok_cli`) इस प्रकार बिना किसी warning के usage-based billing में जा सकता था।
> `argparse` अब इस संयोजन को अस्वीकार करता है।

### अनुवाद टिप्पणी: स्थितियाँ और प्रारूप

`--add_translation_note` के साथ translator टिप्पणी को ऊपर, नीचे या दोनों स्थानों पर रख सकता है और उसे या तो साधारण text format (backward-compatible) में या Markdown plugin द्वारा उपयोग किए जा सकने वाले `marker` format में प्रस्तुत कर सकता है।

**स्थिति** (`--note_position`):

- `bottom` (default): फ़ाइल के अंत में टिप्पणी, जैसा कि ऐतिहासिक रूप से होता आया है।
- `top`: **YAML frontmatter के बाद** टिप्पणी सम्मिलित की जाती है (Astro Content Collections, gray-matter आदि के लिए सुरक्षित)।
- `both`: ऊपर और नीचे दोनों जगह टिप्पणी सम्मिलित की जाती है (एक ही LLM call, दोनों स्थानों के लिए पुनः उपयोग किया गया content)।

**प्रारूप** (`--note_format`):

- `legacy` (default): bold paragraph `**...**` — v1.8 के समान व्यवहार, byte-for-byte। Hugo, GitHub, GitLab और किसी भी Markdown renderer के साथ संगत।
- `marker`: अदृश्य Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), जिसके बाद bold blockquote आता है। GitHub/GitLab पर मूल रूप से पठनीय और Astro में remark plugin द्वारा build के समय उपयोग योग्य, ताकि stylized banner बनाया जा सके (jls42.org blog देखें)।

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### डिफ़ॉल्ट मॉडल (2026)

| Provider | गुणवत्ता (default)       | किफ़ायती (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **लंबे अनुवादों के लिए अनुशंसा**: `--use_gemini` (default = `gemini-3.7-flash`) गैर-लैटिन scripts (PL, JA, ZH, AR, HI) पर Markdown संरचना को विश्वसनीय रूप से सुरक्षित रखता है, जिसमें `--news` mode भी शामिल है, जहाँ placeholders की निष्ठा महत्वपूर्ण है। जापानी में अनुवाद किए गए इस README पर मापा गया: लगभग 6x कम latency में `gemini-3.1-pro-preview` के समान संरचना (21 lists, 18 code blocks, 13 HTML links, 13 images, सभी URLs सुरक्षित)। Backward compatibility के लिए OpenAI अभी भी default है।

## इस script का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत blog (15 भाषाएँ)

## लेखक

Julien LE SAUX
Email: contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3। [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) देखें।

**gpt-5.6-luna के साथ fr से hi में अनुवादित लेख।**
