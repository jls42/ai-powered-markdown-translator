# مترجم Markdown مدعوم بالذكاء الاصطناعي

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 جودة الشيفرة</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="حالة بوابة الجودة"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="تصنيف الأمان"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="تصنيف الموثوقية"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="تصنيف قابلية الصيانة"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="التغطية"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="الثغرات"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="الأخطاء"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="روائح الشيفرة"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="الأسطر المكررة (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="الدين التقني"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="أسطر الشيفرة"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="شارة Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

مترجم لملفات Markdown يستخدم **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini** و**Grok (xAI)** — عبر API، أو باستخدام حصة اشتراك ChatGPT (Codex) أو Grok دون فوترة حسب الاستخدام، أو عبر **OpenCode**، الوكيل مفتوح المصدر، إلى المزوّد الذي تختاره: نموذج محلي (Ollama)، أو مجاني، أو باشتراك (GitHub Copilot…) أو باستخدام مفتاح.

يترجم هذا البرنامج النصي المكتوب بلغة Python ملفات Markdown من لغة مصدر إلى لغة هدف، مع الحفاظ على التنسيق وكتل الشيفرة وبيانات front matter الوصفية.

## الميزات الرئيسية

- **متعدد المزوّدين**: 5 واجهات API (OpenAI وMistral وClaude وGemini وGrok) + واجهتا CLI باشتراك، دون فوترة حسب الاستخدام — Codex (ChatGPT) وGrok — + OpenCode (مفتوح المصدر، MIT) إلى أي مزوّد مُعدّ في OpenCode، بما في ذلك نموذج محلي
- **نماذج 2026**: GPT-5.6 Terra وClaude Sonnet 5 وGemini 3.7 Flash
- **الوضع الاقتصادي**: خيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- **ملف واحد**: خيار `--file` لترجمة ملف واحد
- **التقسيم الذكي**: إدارة النصوص الطويلة مع حدود الرموز لكل نموذج
- **الحفاظ على الشيفرة**: يتم الحفاظ على كتل الشيفرة وكذلك الشيفرة المضمّنة (`` `...` ``)
- **اسم الملف**: خيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **وضع الأخبار**: خيار `--news` لحماية الاقتباسات الإنجليزية ومعالجة الأعلام في مقالات الأخبار
- **إعدادات .env**: دعم الملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

### لاستخدام الأداة

```bash
pip install ai-powered-markdown-translator
```

يصبح الأمر `aipmt` متاحًا بعد ذلك في كل مكان. إذا لم يكن مجلد نصوص
Python البرمجية موجودًا في `PATH`، فإن `python -m aipmt` ينفذ الشيء نفسه تمامًا.
يتطلب Python 3.10 أو إصدارًا أحدث.

للتثبيت بمعزل عن بقية حزمك:

```bash
pipx install ai-powered-markdown-translator
```

### للمساهمة في المشروع

يبقى المستودع المستنسخ ضروريًا للتطوير: ففيه توجد الاختبارات،
والترجمات الـ28، وجميع أدوات الجودة.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

إن `requirements.txt` هو **ملف قفل مثبت بالكامل**، وهو انعكاس مطابق تمامًا
للبيئة التي خضعت للاختبار. أما الحدود المنشورة في `pyproject.toml` فهي
أوسع عمدًا: ولا تفرض أي شيء على حزمك الأخرى.

### أدوات الجودة (اختيارية لكن موصى بها)

يستخدم المشروع [`pre-commit`](https://pre-commit.com) لمنع إيداع شيفرة سيئة التنسيق أو
قابلة للاستغلال أو تحتوي على سر. التثبيت:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

الأدوات النشطة: ruff (فحص وتنسيق)، shellcheck (bash)، prettier (markdown/yaml/json)،
Lizard (التعقيد)، detect-secrets (مفاتيح API)، mypy (التحقق التدريجي من الأنواع)،
Opengrep (SAST)، pip-audit (ثغرات تبعيات CVE)، unittest. راجع قسم
`CLAUDE.md` _Quality / pre-commit_ للاطلاع على التفاصيل.

## الإعداد

يُبحث عن المفاتيح في **ثلاثة أماكن**، من الأعلى أولوية إلى الأقل.
ولا يملأ كل مكان منها إلا ما تركه المكان السابق فارغًا.

|     | أين                                            | لماذا                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | متغيرات البيئة                                 | CI، الحاويات، التجاوز المؤقت |
| 2   | `.env` للمجلد الحالي (أو أحد المجلدات الأب) | مفتاح خاص بمشروع واحد            |
| 3   | `~/.config/aipmt/.env`                        | **يُثبت مرة واحدة ويصلح في كل مكان**   |

بعد `pip install`، يكون الخيار الثالث هو الأبسط:

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

يتبع هذا الملف `XDG_CONFIG_HOME` عندما يشير المتغير إلى مسار مطلق
(وإلا فسيُتجاهل، كما تنص المواصفة)، ويتبع `%APPDATA%`
في Windows.

يبقى الخيار الثاني مفيدًا عندما يمتلك مستودع ما مفتاحه الخاص: إذ يتغلب
`.env` الموجود في جذره على إعدادات المستخدم من دون تعديلها. كما أن
المتغير المحدد مسبقًا في البيئة يتغلب على كليهما:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

إذا لم يُعثر على أي مفتاح، فلا يعرض الأمر أثر الاستدعاء: بل
يسرد المواقع الثلاثة مع مسار كل منها كاملًا.

يُقبل `GEMINI_API_KEY` بديلًا عن `GOOGLE_API_KEY` (وفق اصطلاح AI
Studio). المتغيرات الاختيارية: `XAI_BASE_URL` (نقطة نهاية xAI، الافتراضية
`https://api.x.ai/v1`)، و`CLAUDE_TIMEOUT` (الثواني لكل استدعاء Anthropic، الافتراضي
900)، و`CODEX_BIN` / `CODEX_TIMEOUT`، و`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`،
و`GROK_TRANSLATE_SANDBOX` (راجع قسم Grok CLI)، و`OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (راجع قسم OpenCode). أما في جانب
`regen_translations.sh` فهي: `REGEN_PROVIDER` و`REGEN_MODEL` و
`REGEN_JOB_TIMEOUT` (الحد الأقصى لكل مهمة، الافتراضي 600 ثانية).

## الاستخدام

### ترجمة ملف واحد

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ترجمة مجلد

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### الترجمة باستخدام اشتراك ChatGPT الخاص بك (`--use_codex`)

لا يستهلك هذا المزوّد أي مفتاح API: فهو يتحكم في CLI Codex الرسمي في وضع
غير تفاعلي، ولذلك تُخصم الترجمة من حصة اشتراك ChatGPT (Plus وPro وBusiness…)
المدفوعة مسبقًا. وهذه هي الطريقة الوحيدة الموثقة من OpenAI لهذا الاستخدام —
فإن رموز `~/.codex/auth.json` لا تُصادق على استدعاءات API Platform، كما أن هذا
البرنامج النصي لا يقرأها مطلقًا.

**المتطلبات المسبقة:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

يُبحث عن الملف التنفيذي بالترتيب التالي: المتغير `CODEX_BIN`، ثم `PATH`،
ثم حزمة Python `openai-codex-cli-bin`. ولا توجد هذه الأخيرة عمدًا في `requirements.txt`:
فحجمها نحو 250 ميغابايت، ما كان سيفرضها على جميع المستخدمين من أجل مزوّد اختياري.

**ما ينبغي معرفته:**

- **لا يُستخدم أي مفتاح API.** تتم إزالة `OPENAI_API_KEY` و`CODEX_API_KEY`
  من بيئة العملية الفرعية، ما يضمن أن وجود مفتاح في `.env` لن يحوّل
  الترجمة أبدًا إلى فوترة حسب الاستخدام.
- **كل مقطع = «رسالة محلية» واحدة** من نافذة الخمس ساعات الخاصة بالخطة.
  استخدم `--eco` (النموذج `gpt-5.6-luna`، من 250 إلى 2,000 رسالة/5 ساعات
  في Plus) بدلًا من نموذج الجودة (`gpt-5.6-sol`، من 10 إلى 100 رسالة/5 ساعات).
- **أبطأ** من استدعاء API: احسب نحو 45 ثانية لملف README كامل، مقابل
  بضع ثوانٍ مباشرة.
- **مرفوض في CI** (عند تعريف `CI` أو `GITHUB_ACTIONS`): فالمصادقة
  بالاشتراك غير مخصصة لعامل تشغيل مشترك، كما أن OpenAI لا توصي بهذا المسار
  في المستودعات العامة. استخدم مفتاح API في هذا المسار.
- متغيرات البيئة: `CODEX_BIN` (مسار صريح للملف التنفيذي) و`CODEX_TIMEOUT`
  (الثواني لكل مقطع، الافتراضي `600`).

### الترجمة باستخدام اشتراك Grok الخاص بك (`--use_grok_cli`)

المبدأ نفسه المتبع في `--use_codex`، مع CLI الرسمي **Grok Build**:
تُخصم الترجمة من اشتراك Grok (SuperGrok / X Premium+) بدلًا من
فوترة الرموز.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**العزل — اقرأ هذا قبل الاستخدام.** هذا المزوّد **أضعف بنيويًا**
من `--use_codex`، وهذا أمر مقصود:

- يعمل Codex في `--sandbox read-only`، وهو حد تفرضه المنظومة.
- لا يمكن تطبيق بيئة Grok المعزولة **على كثير من أجهزة Linux الحديثة**:
  إذ يحظر AppArmor مساحات أسماء المستخدمين غير المميّزة منذ Ubuntu 24.04،
  كما تفشل قائمة منع مقابس وقت تشغيل الحاويات إذا كان
  `/run/podman` هو `0700`. والحساب **المضمّن** الذي لا يمكن
  تطبيقه يبدأ **من دون عزل، بصمت**.
- لذلك لا يطلب البرنامج النصي أي حساب افتراضيًا، ولا يعود أبدًا
  **بصمت**: بل يعرض تحذيرًا. ويعتمد العزل على قواعد `--deny`
  الخاصة بـ CLI (ومنها قاعدة الالتقاط الشاملة `*`)، وهي طبقة
  القياس الوحيدة _fail-closed_ — إذ تؤدي القاعدة غير المعروفة إلى رفض بدء التشغيل
  بدل إزالة الحماية دون إبلاغ.
- **لفرض** عزل نظام التشغيل: `GROK_TRANSLATE_SANDBOX=read-only`. سيفشل بدء التشغيل إذا لم يتمكن
  الجهاز من الالتزام به، وهذا هو السلوك المطلوب.

**الحصة**: مجموعة Grok **أسبوعية ومشتركة** مع Chat وImagine وVoice،
ولا يوجد أي أمر يتيح قراءتها. لذلك قد تستهلك المعالجة الدفعية استخدامك
للمحادثة من دون أي إشارة — ومن هنا جاء تحديد التزامن بـ2 والتحذير في `regen_translations.sh`.

متغيرات أخرى: `GROK_BIN` (مسار الملف التنفيذي)، و`GROK_TIMEOUT` (الافتراضي 900 ثانية).

لإعادة إنشاء الترجمات الـ28:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### الترجمة باستخدام OpenCode إلى المزوّد الذي تختاره (`--use_opencode`)

إن [OpenCode](https://opencode.ai) هو وكيل شيفرة **مفتوح المصدر (MIT)** يعمل في
الطرفية. وهو ليس مزوّد نماذج، بل **موجّه** إلى النماذج التي أعددتها
داخل OpenCode نفسه: مفتاح API، أو اشتراك (GitHub Copilot وChatGPT وSuperGrok)،
أو بوابة OpenCode Zen — التي تقدم نماذج مجانية **من دون حساب** — أو نموذج
**محلي** (Ollama وLM Studio وllama.cpp). يتحكم هذا المزوّد في `opencode run`
في وضع غير تفاعلي ويقصر الاستدعاء على جولة واحدة ذهابًا وإيابًا، من دون أي أداة.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

إن `--model` **إلزامي**، بالتنسيق `provider/modèle`. فـ OpenCode ليس
مزوّدًا، ولا يُختار أي افتراضي نيابةً عنك: إذ سيكون البديل الخاص به نموذجًا
مجانيًا قد تُستخدم محادثاته في التدريب.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**العزل — ما يفعله البرنامج النصي في كل استدعاء:**

- يحدد إعدادًا مضمنًا (`OPENCODE_CONFIG_CONTENT`)، له الأولوية على إعدادك، وكيلًا
  `aipmt` تكون **جميع أدواته مرفوضة** (`permission: { "*": "deny" }`): فلا يستطيع
  النموذج القراءة أو الكتابة أو تشغيل أمر — وقد أظهرت القياسات أنه لا يحاول
  ذلك حتى. وتُعطّل مشاركة الجلسة، بينما يستبعد `--pure` المكونات
  الإضافية الخارجية، ولا يُستخدم `--auto` مطلقًا.
- يجري الاستدعاء داخل **مجلد مؤقت وفارغ**، مع مفتاحي التبديل
  `OPENCODE_DISABLE_PROJECT_CONFIG` و`OPENCODE_DISABLE_CLAUDE_CODE`: فمن دونهما يحقن OpenCode في كل مطالبة
  `AGENTS.md` الخاص بالمجلد الحالي و`~/.claude/CLAUDE.md` الخاص بك — وقد أظهرت
  القياسات أن تعليمة «اختم كل إجابة بـ BANANA» الموضوعة في
  `AGENTS.md` كانت تُطبّق على الترجمة. أما القواعد العامة لـ`~/.config/opencode/AGENTS.md`
  فتبقى مطبقة: إذ لا يسمح OpenCode بتجاوزها.
- يتطلب عقد الإخراج كل ما يلي في آن واحد: رمز عودة 0، وعدم وجود حدث
  `error`، وعدم استدعاء أي أداة، وأن تكون الخطوة الأخيرة منتهية
  بـ`stop`، ونصًا غير فارغ، وأن يكون الوكيل محمّلًا بالفعل — فـ
  `--agent` غير المعروف لا يؤدي إلى فشل OpenCode، بل **يعود بصمت**
  إلى وكيل البرمجة ذي الأدوات النشطة. كما أن `exit 0` لا يثبت شيئًا هنا.
- **لا يُمرر أي مفتاح aipmt** إلى العملية الفرعية (بنفس التصفية المستخدمة
  مع Codex وGrok)، باستثناء مسمّى واحد: `OPENCODE_API_KEY`، وهو مفتاح OpenCode
  نفسه (Zen، Go). تُعدّ المزوّدات داخل OpenCode (`opencode auth login` و`opencode.json`)،
  لا داخل `.env` الخاص بـ aipmt.

**ما ينبغي معرفته:**

- نماذج Zen المجانية هي نماذج «خفيّة» أو نماذج مساهمين، ومتغيرة،
  وحدودها غير موثقة، وقد تُستخدم محادثاتها في التدريب: وهي مثالية للتوثيق
  العام، لكن ينبغي تجنبها للمحتوى الخاص. وفق القياس: يترجم `opencode/mimo-v2.5-free`
  ملف README هذا في مرور واحد؛ أما `opencode/big-pickle` فأبطأ، وقد بقي طلبان
  متزامنان فيه من دون استجابة.
- يجب أن يوفر النموذج المحلي سياقًا لا يقل عن 16 ألفًا — إذ تصل المقاطع
  إلى 16,000 محرف — بينما يضبط Ollama غالبًا 4,096 افتراضيًا. مع Ollama:
  استخدم `Modelfile` مع `PARAMETER num_ctx 32768`، ثم `ollama create`. وتعتمد الجودة
  على النموذج: فقد عكس نموذج 7B قائمة وأتلف إغلاق كتلة شيفرة في ملف اختبار،
  بينما حافظ نموذج من البوابة على كل شيء.
- لا تأثير لـ`--eco` (فالنموذج هو نموذج `--model`)؛ أما
  `--reasoning_effort` فيُمرر كما هو باعتباره `--variant` في OpenCode، ولا ينبغي
  طلبه إلا إذا كان النموذج يعرفه.
- يسجل OpenCode الجلسات في قاعدة بياناته (`~/.local/share/opencode/`)، كما يفعل مع
  كل جلسة OpenCode.
- متغيرات البيئة: `OPENCODE_BIN` (مسار صريح للملف التنفيذي، وإلا
  `PATH` ثم `~/.opencode/bin/opencode`) و`OPENCODE_TIMEOUT`
  (الثواني لكل مقطع، الافتراضي `600`). ويُحترم `OPENCODE_CONFIG`
  إذا قمت بتصديره.

### الوضع الاقتصادي

يستخدم نماذج أسرع وأقل تكلفة (gpt-5.6-luna وclaude-haiku-4-5 وgemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### الخيارات

| الخيار | الوصف |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file` | ملف Markdown واحد لترجمته |
| `--source_dir` | الدليل المصدر الذي يحتوي على ملفات Markdown |
| `--target_dir` | دليل الإخراج للملفات المترجمة |
| `--source_lang` | اللغة المصدر (الافتراضية: `fr`) |
| `--target_lang` | اللغة الهدف (الافتراضية: `en`) |
| `--model` | النموذج المحدد المطلوب استخدامه |
| `--eco` | استخدام النماذج الاقتصادية |
| `--use_mistral` | استخدام واجهة برمجة تطبيقات Mistral AI |
| `--use_claude` | استخدام واجهة برمجة تطبيقات Claude |
| `--use_gemini` | استخدام واجهة برمجة تطبيقات Gemini |
| `--use_codex` | استخدام CLI الخاص بـ Codex ضمن حصة اشتراك ChatGPT |
| `--use_grok` | استخدام واجهة برمجة تطبيقات xAI (Grok) — يتطلب `XAI_API_KEY` |
| `--use_grok_cli` | استخدام CLI الخاص بـ Grok ضمن حصة اشتراك Grok |
| `--use_opencode` | استخدام OpenCode (مفتوح المصدر) مع المزوّد المهيأ في OpenCode؛ يتطلب `--model provider/modèle` |
| `--force` | فرض إعادة الترجمة |
| `--keep_filename` | الاحتفاظ باسم الملف الأصلي |
| `--news` | وضع الأخبار: حماية الاقتباسات باللغة الإنجليزية وإدارة الأعلام حسب اللغة |
| `--add_translation_note` | إضافة ملاحظة ترجمة |
| `--note_position` | موضع الملاحظة: `top` أو `bottom` (الافتراضي) أو `both` |
| `--note_format` | تنسيق الملاحظة: `legacy` (الافتراضي، فقرة عريضة) أو `marker` |
| `--include_model` | تضمين اسم النموذج في ملف الإخراج |
| `--reasoning_effort` | جهد الاستدلال في GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **أعلام المزوّد السبعة متنافية فيما بينها.** كان الجمع بين علمين مقبولًا سابقًا بصمت، وكان يُحسم لصالح أول علم يتم اختباره:  
> ولذلك كان من الممكن أن تنتقل ترجمة مطلوبة باستخدام حصة الاشتراك (`--use_codex`، `--use_grok_cli`) إلى الفوترة حسب الاستخدام من دون أي تحذير.  
> يرفض `argparse` الآن هذا الجمع.

### ملاحظة الترجمة: المواضع والتنسيقات

باستخدام `--add_translation_note`، يمكن للمترجم وضع الملاحظة في الأعلى أو الأسفل أو في الموضعين معًا، كما يمكنه تنسيقها إما كنص عادي (للتوافق مع الإصدارات السابقة) أو بتنسيق `marker` القابل للاستخدام بواسطة إضافة Markdown.

**الموضع** (`--note_position`):

- `bottom` (الافتراضي): الملاحظة في نهاية الملف، كما كان يحدث تاريخيًا.
- `top`: إدراج الملاحظة **بعد الواجهة الأمامية YAML** (لضمان التوافق مع Astro Content Collections وgray-matter وغيرهما).
- `both`: إدراج الملاحظة في الأعلى والأسفل معًا (استدعاء واحد لـ LLM، وإعادة استخدام المحتوى في الموضعين).

**التنسيق** (`--note_format`):

- `legacy` (الافتراضي): فقرة عريضة `**...**` — سلوك مطابق تمامًا للإصدار v1.8، بايتًا ببايت. متوافق مع Hugo وGitHub وGitLab وأي مُصيّر Markdown.
- `marker`: تعريف مرجع رابط Markdown غير مرئي (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)، يتبعه اقتباس جماعي عريض. قابل للقراءة أصليًا على GitHub/GitLab، ويمكن لإضافة remark على جانب Astro استخدامه أثناء البناء لإنتاج شريط إشعار منسّق (راجع مدونة jls42.org).

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

### النماذج الافتراضية (2026)

| المزوّد | الجودة (الافتراضية) | الاقتصادي (`--eco`) |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |
| OpenCode | `--model provider/modèle` إلزامي | مماثل — `--eco` بلا تأثير |

> **توصية للترجمات الطويلة**: يحافظ `--use_gemini` (الافتراضي = `gemini-3.7-flash`) بأمانة على بنية Markdown في النصوص غير اللاتينية (PL وJA وZH وAR وHI)، بما في ذلك وضع `--news` حيث تكون دقة العناصر النائبة مهمة. وقد قيس ذلك على ملف README هذا المترجم إلى اليابانية: بنية مطابقة لـ `gemini-3.1-pro-preview` (21 قائمة، و18 كتلة تعليمات برمجية، و13 رابط HTML، و13 صورة، مع الحفاظ على جميع عناوين URL) وبزمن استجابة أقل بنحو 6 مرات. يظل OpenAI هو الخيار الافتراضي للتوافق مع الإصدارات السابقة.

## مشاريع تستخدم هذا البرنامج النصي

- **[jls42.org](https://jls42.org)** - مدونة شخصية متعددة اللغات (15 لغة)

## المؤلف

Julien LE SAUX  
البريد الإلكتروني: contact@jls42.org

## الترخيص

GNU GENERAL PUBLIC LICENSE الإصدار 3. راجع [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**مقالة مترجمة من الفرنسية إلى العربية باستخدام gpt-5.6-luna.**
