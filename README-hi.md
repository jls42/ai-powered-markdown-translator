# AI-संचालित Markdown अनुवादक

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 कोड की गुणवत्ता</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="गुणवत्ता गेट स्थिति"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="सुरक्षा रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="विश्वसनीयता रेटिंग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="रखरखाव-क्षमता रेटिंग"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="कवरेज"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="कमज़ोरियाँ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="बग"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="कोड संबंधी समस्याएँ"></a>
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

यह Python स्क्रिप्ट स्रोत भाषा से लक्ष्य भाषा में Markdown फ़ाइलों का अनुवाद करती है और फ़ॉर्मेटिंग, कोड ब्लॉक तथा front matter मेटाडेटा को सुरक्षित रखती है।

## मुख्य विशेषताएँ

- **Multi-Provider**: 4 APIs (OpenAI, Mistral, Claude, Gemini) और ChatGPT सदस्यता पर Codex CLI का समर्थन
- **2026 मॉडल**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **किफ़ायती मोड**: तेज़ और कम लागत वाले मॉडल इस्तेमाल करने के लिए विकल्प `--eco`
- **एकल फ़ाइल**: केवल एक फ़ाइल का अनुवाद करने के लिए विकल्प `--file`
- **स्मार्ट विभाजन**: प्रत्येक मॉडल की token सीमाओं के साथ लंबे पाठों का प्रबंधन
- **कोड संरक्षण**: कोड ब्लॉक और inline कोड (`` `...` ``) सुरक्षित रखे जाते हैं
- **फ़ाइल नाम**: मूल नाम बनाए रखने के लिए विकल्प `--keep_filename`
- **News मोड**: समाचार लेखों में अंग्रेज़ी उद्धरणों को सुरक्षित रखने और झंडों को संभालने के लिए विकल्प `--news`
- **.env कॉन्फ़िगरेशन**: API कुंजियों के लिए `.env` फ़ाइल का समर्थन
- **अनुवाद नोट**: दस्तावेज़ के अंत में वैकल्पिक नोट जोड़ना

## इंस्टॉलेशन

### टूल का उपयोग करने के लिए

```bash
pip install ai-powered-markdown-translator
```

इसके बाद `aipmt` कमांड हर जगह उपलब्ध होगी। यदि Python की scripts निर्देशिका आपके `PATH` में नहीं है, तो `python -m aipmt` ठीक यही काम करती है। Python 3.10 या नया संस्करण आवश्यक है।

अपने अन्य पैकेजों से अलग इंस्टॉलेशन के लिए:

```bash
pipx install ai-powered-markdown-translator
```

### परियोजना में योगदान देने के लिए

विकास के लिए cloned repository आवश्यक रहती है: परीक्षण, 28 अनुवाद और सभी गुणवत्ता-संबंधी टूल वहीं मौजूद हैं।

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` पूरी तरह **pinned lock** फ़ाइल है, जो परीक्षण किए गए environment का सटीक प्रतिबिंब है। `pyproject.toml` में प्रकाशित सीमाएँ जानबूझकर अधिक व्यापक हैं: वे आपके अन्य पैकेजों पर कोई बाध्यता नहीं डालतीं।

### गुणवत्ता-संबंधी टूल (वैकल्पिक लेकिन अनुशंसित)

परियोजना [`pre-commit`](https://pre-commit.com) का उपयोग करती है, ताकि खराब फ़ॉर्मेट वाला, असुरक्षित या secret युक्त कोड commit न हो। इंस्टॉलेशन:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

सक्रिय hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (जटिलता), detect-secrets (API कुंजियाँ), mypy (क्रमिक typing), Opengrep (SAST), pip-audit (CVE deps), unittest। विवरण के लिए `CLAUDE.md` के _Quality / pre-commit_ अनुभाग को देखें।

## कॉन्फ़िगरेशन

`.env` नामक फ़ाइल **उस निर्देशिका में बनाएँ जहाँ से आप कमांड चलाते हैं** (इसे पहले वहीं, फिर parent directories में खोजा जाता है), या environment variables परिभाषित करें:

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

`GEMINI_API_KEY` को `GOOGLE_API_KEY` के विकल्प के रूप में स्वीकार किया जाता है (AI Studio convention)। वैकल्पिक variables: `XAI_BASE_URL` (xAI endpoint, डिफ़ॉल्ट `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (प्रत्येक Anthropic call के लिए सेकंड, डिफ़ॉल्ट 900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`, और `GROK_TRANSLATE_SANDBOX` (Grok CLI अनुभाग देखें)। `regen_translations.sh` के लिए: `REGEN_PROVIDER`, `REGEN_MODEL` और `REGEN_JOB_TIMEOUT` (प्रति job सीमा, डिफ़ॉल्ट 600 s)।

## उपयोग

### एकल फ़ाइल का अनुवाद

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### किसी निर्देशिका का अनुवाद

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

### अपनी ChatGPT सदस्यता पर अनुवाद करना (`--use_codex`)

यह provider किसी API कुंजी का उपयोग नहीं करता: यह आधिकारिक Codex CLI को non-interactive मोड में नियंत्रित करता है। इसलिए अनुवाद पहले से भुगतान की गई ChatGPT सदस्यता (Plus, Pro, Business…) के quota से घटता है। इस उपयोग के लिए OpenAI द्वारा दस्तावेज़ीकृत यही एकमात्र तरीका है — `~/.codex/auth.json` के tokens Platform API calls को authenticate नहीं करते और यह स्क्रिप्ट उन्हें कभी पढ़ती भी नहीं है।

**पूर्वापेक्षाएँ:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binary को इस क्रम में खोजा जाता है: `CODEX_BIN` variable, `PATH`, फिर Python package `openai-codex-cli-bin`। अंतिम package जानबूझकर `requirements.txt` में शामिल नहीं है: इसका आकार लगभग 250 Mo है, जिसे वैकल्पिक provider के लिए सभी उपयोगकर्ताओं पर लागू करना उचित नहीं होगा।

**जानकारी के लिए:**

- **किसी API कुंजी का उपयोग नहीं किया जाता।** `OPENAI_API_KEY` और `CODEX_API_KEY` को subprocess के environment से हटा दिया जाता है, जिससे यह सुनिश्चित होता है कि `.env` में मौजूद कोई कुंजी अनुवाद को usage-based billing में न बदल सके।
- **एक segment = plan की 5 घंटे की window का एक “स्थानीय संदेश”।** गुणवत्ता वाले मॉडल (`gpt-5.6-sol`, 10-100 messages/5 h) के बजाय `--eco` (मॉडल `gpt-5.6-luna`, Plus पर 250-2,000 messages/5 h) का उपयोग करें।
- **API call से धीमा**: सीधे कुछ सेकंड की तुलना में पूरे README के लिए लगभग 45 s मानें।
- **CI में अस्वीकार** (`CI` या `GITHUB_ACTIONS` परिभाषित होने पर): सदस्यता-आधारित authentication साझा runner के लिए नहीं है और OpenAI public repositories पर इस workflow की सलाह नहीं देता। इस path पर API कुंजी का उपयोग करें।
- Environment variables: `CODEX_BIN` (binary का स्पष्ट path) और `CODEX_TIMEOUT` (प्रति segment सेकंड, डिफ़ॉल्ट `600`)।

### अपनी Grok सदस्यता पर अनुवाद करना (`--use_grok_cli`)

`--use_codex` के समान सिद्धांत, आधिकारिक **Grok Build** CLI के साथ: अनुवाद token के आधार पर बिल होने के बजाय Grok सदस्यता (SuperGrok / X Premium+) के quota से घटता है।

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Sandboxing — उपयोग से पहले पढ़ें।** यह provider संरचनात्मक रूप से `--use_codex` से **कमज़ोर** है, और यह जानबूझकर ऐसा है:

- Codex `--sandbox read-only` में चलता है, जो system द्वारा थोपी गई सीमा है।
- कई नए Linux systems पर Grok का sandbox लागू नहीं हो सकता: Ubuntu 24.04 के बाद AppArmor unprivileged user namespaces को block करता है, और container runtime sockets की deny-list तब विफल हो जाती है जब `/run/podman` `0700` में हो। जबकि ऐसा **integrated** profile, जिसे लागू नहीं किया जा सकता, चुपचाप **बिना confinement** के शुरू हो जाता है।
- इसलिए स्क्रिप्ट डिफ़ॉल्ट रूप से कोई profile नहीं माँगती और कभी भी चुपचाप fallback नहीं करती: यह warning दिखाती है। Confinement CLI के `--deny` rules (जिसमें catch-all `*` भी शामिल है) पर निर्भर करता है; यही मापी गई _fail-closed_ layer है — अज्ञात rule सुरक्षा हटाने के बजाय startup को अस्वीकार कर देता है।
- OS sandbox को **अनिवार्य** करने के लिए: `GROK_TRANSLATE_SANDBOX=read-only`। यदि machine इसे लागू नहीं कर सकती, तो startup विफल होगा, जो अपेक्षित व्यवहार है।

**Quota**: Grok pool **साप्ताहिक और साझा** है तथा Chat, Imagine और Voice के साथ साझा किया जाता है; इसे पढ़ने के लिए कोई command उपलब्ध नहीं है। इसलिए batch processing आपके conversational usage को बिना किसी सूचना के कम कर सकती है — इसी कारण `regen_translations.sh` में concurrency 2 तक सीमित है और warning दी जाती है।

अन्य variables: `GROK_BIN` (binary path), `GROK_TIMEOUT` (डिफ़ॉल्ट 900 s)।

28 अनुवादों को पुनः उत्पन्न करने के लिए:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### किफ़ायती मोड

तेज़ और कम लागत वाले मॉडल इस्तेमाल करें (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### विकल्प

| विकल्प | विवरण |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file` | अनुवाद के लिए एकल Markdown फ़ाइल |
| `--source_dir` | Markdown फ़ाइलों वाली स्रोत निर्देशिका |
| `--target_dir` | अनुवादित फ़ाइलों के लिए output directory |
| `--source_lang` | स्रोत भाषा (डिफ़ॉल्ट: `fr`) |
| `--target_lang` | लक्ष्य भाषा (डिफ़ॉल्ट: `en`) |
| `--model` | उपयोग करने के लिए विशिष्ट मॉडल |
| `--eco` | किफ़ायती मॉडल इस्तेमाल करें |
| `--use_mistral` | Mistral AI API का उपयोग करें |
| `--use_claude` | Claude API का उपयोग करें |
| `--use_gemini` | Gemini API का उपयोग करें |
| `--use_codex` | ChatGPT सदस्यता quota पर Codex CLI का उपयोग करें |
| `--use_grok` | xAI API (Grok) का उपयोग करें — `XAI_API_KEY` आवश्यक |
| `--use_grok_cli` | Grok सदस्यता quota पर Grok CLI का उपयोग करें |
| `--force` | पुनः अनुवाद को बाध्य करें |
| `--keep_filename` | मूल फ़ाइल नाम बनाए रखें |
| `--news` | समाचार मोड: EN उद्धरण सुरक्षित रखता है, भाषा के अनुसार झंडे संभालता है |
| `--add_translation_note` | अनुवाद नोट जोड़ें |
| `--note_position` | नोट की स्थिति: `top`, `bottom` (डिफ़ॉल्ट), या `both` |
| `--note_format` | नोट का प्रारूप: `legacy` (डिफ़ॉल्ट, bold paragraph) या `marker` |
| `--include_model` | output फ़ाइल में मॉडल का नाम शामिल करें |
| `--reasoning_effort` | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh` |

> **Provider के छह flags परस्पर अनन्य हैं।** पहले दो flags को पहले चुपचाप स्वीकार कर लिया जाता था और परीक्षण किए गए पहले provider पर resolve किया जाता था: सदस्यता quota पर माँगा गया अनुवाद (`--use_codex`, `--use_grok_cli`) इस प्रकार बिना किसी warning के usage-based billing में जा सकता था। `argparse` अब इस संयोजन को अस्वीकार करता है।

### अनुवाद नोट: स्थितियाँ और प्रारूप

`--add_translation_note` के साथ translator नोट को ऊपर, नीचे या दोनों स्थानों पर रख सकता है और उसे साधारण text format (backward-compatible) या Markdown plugin द्वारा उपयोग किए जा सकने वाले `marker` format में प्रस्तुत कर सकता है।

**स्थिति** (`--note_position`):

- `bottom` (डिफ़ॉल्ट): फ़ाइल के अंत में नोट, जैसा कि पहले होता था।
- `top`: **YAML frontmatter के बाद** नोट डाला जाता है (Astro Content Collections, gray-matter आदि की सुरक्षा के लिए)।
- `both`: नोट ऊपर और नीचे दोनों जगह डाला जाता है (एक LLM call, दोनों स्थानों के लिए पुनः उपयोग किया गया content)।

**प्रारूप** (`--note_format`):

- `legacy` (डिफ़ॉल्ट): bold paragraph `**...**` — v1.8 जैसा बिल्कुल समान व्यवहार, byte-for-byte। Hugo, GitHub, GitLab और किसी भी Markdown renderer के साथ संगत।
- `marker`: अदृश्य Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), जिसके बाद bold blockquote आता है। GitHub/GitLab पर native रूप से पठनीय और Astro में remark plugin द्वारा build के समय stylized banner बनाने के लिए उपयोगी (jls42.org blog देखें)।

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

| Provider | गुणवत्ता (डिफ़ॉल्ट) | किफ़ायती (`--eco`) |
| -------- | ---------------------- | ----------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |

> **लंबे अनुवादों के लिए अनुशंसा**: `--use_gemini` (डिफ़ॉल्ट = `gemini-3.7-flash`) non-Latin scripts (PL, JA, ZH, AR, HI) पर Markdown संरचना को विश्वसनीय रूप से सुरक्षित रखता है, जिसमें `--news` मोड भी शामिल है, जहाँ placeholders की fidelity महत्वपूर्ण होती है। जापानी में अनुवाद किए गए इस README पर मापा गया: `gemini-3.1-pro-preview` के समान संरचना (21 सूचियाँ, 18 code blocks, 13 HTML links, 13 images, सभी URLs सुरक्षित) और लगभग 6 गुना कम latency। Backward compatibility के लिए OpenAI अभी भी default है।

## इस स्क्रिप्ट का उपयोग करने वाली परियोजनाएँ

- **[jls42.org](https://jls42.org)** - बहुभाषी व्यक्तिगत blog (15 भाषाएँ)

## लेखक

Julien LE SAUX  
Email: contact@jls42.org

## लाइसेंस

GNU GENERAL PUBLIC LICENSE Version 3। [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) देखें।

**लेख का फ्रेंच से हिंदी में gpt-5.6-luna द्वारा अनुवाद किया गया।**
