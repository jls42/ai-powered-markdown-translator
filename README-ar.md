# مترجم Markdown مدعوم بالذكاء الاصطناعي

🌍 [الفرنسية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [الإنجليزية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [الإسبانية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [الصينية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [الألمانية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [اليابانية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [الكورية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [الهندية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [الإيطالية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [الهولندية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [البولندية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [البرتغالية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [الرومانية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [السويدية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 جودة الكود</h4>

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="روائح الكود"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="الأسطر المكررة (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="الدين التقني"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="أسطر الكود"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="شارة Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

مترجم لملفات Markdown يستخدم **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini**.

يترجم نص Python هذا ملفات Markdown من لغة مصدر إلى لغة هدف، مع الحفاظ على التنسيق وكتل الكود وبيانات front matter الوصفية.

## الميزات الرئيسية

- **متعدد المزوّدين**: دعم 4 واجهات API (OpenAI وMistral وClaude وGemini) بالإضافة إلى CLI Codex ضمن اشتراك ChatGPT
- **نماذج 2026**: GPT-5.6 Terra وClaude Sonnet 5 وGemini 3.7 Flash
- **الوضع الاقتصادي**: خيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- **ملف واحد**: خيار `--file` لترجمة ملف واحد
- **التقسيم الذكي**: إدارة النصوص الطويلة مع حدود الرموز المميزة حسب النموذج
- **الحفاظ على الكود**: يتم الحفاظ على كتل الكود والكود المضمّن (`` `...` ``)
- **اسم الملف**: خيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **وضع الأخبار**: خيار `--news` لحماية الاقتباسات الإنجليزية والتعامل مع الأعلام في المقالات الإخبارية
- **إعدادات .env**: دعم الملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

### لاستخدام الأداة

```bash
pip install ai-powered-markdown-translator
```

يصبح الأمر `aipmt` متاحًا في كل مكان. إذا لم يكن مجلد
البرامج النصية لـ Python موجودًا في `PATH`، فإن `python -m aipmt` ينفّذ
الشيء نفسه تمامًا. يلزم Python 3.10 أو إصدار أحدث.

لتثبيت معزول عن بقية حزمك:

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

إن `requirements.txt` هو **ملف قفل مثبت بالكامل**، ويمثل انعكاسًا دقيقًا
للبيئة المختبرة. أما الحدود المنشورة في `pyproject.toml` فأوسع عمدًا:
ولا تفرض أي شيء على حزمك الأخرى.

### أدوات الجودة (اختيارية لكن موصى بها)

يستخدم المشروع [`pre-commit`](https://pre-commit.com) لمنع تنفيذ commit لكود سيئ التنسيق أو
يحتوي على ثغرات أو سرّ. التثبيت:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

الخطافات النشطة: ruff (الفحص والتنسيق)، shellcheck (bash)، prettier (markdown/yaml/json)، Lizard (التعقيد)، detect-secrets (مفاتيح API)، mypy (التحقق التدريجي من الأنواع)، Opengrep (SAST)، pip-audit (تبعيات CVE)، unittest. راجع قسم _Quality / pre-commit_ في `CLAUDE.md` للاطلاع على التفاصيل.

## الإعداد

أنشئ ملف `.env` **في المجلد الذي تشغّل منه الأمر** (يُبحث عنه هناك،
ثم في المجلدات الأصلية)، أو عرّف متغيرات البيئة:

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

يُقبل `GEMINI_API_KEY` كبديل لـ `GOOGLE_API_KEY` (اصطلاح AI
Studio). المتغيرات الاختيارية: `XAI_BASE_URL` (نقطة نهاية xAI، القيمة
الافتراضية `https://api.x.ai/v1`)، و`CLAUDE_TIMEOUT` (بالثواني لكل استدعاء Anthropic، القيمة الافتراضية
900)، و`CODEX_BIN` / `CODEX_TIMEOUT`، و`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`،
و`GROK_TRANSLATE_SANDBOX` (راجع قسم Grok CLI). أما في جانب
`regen_translations.sh`، فهناك `REGEN_PROVIDER` و`REGEN_MODEL` و
`REGEN_JOB_TIMEOUT` (حد أقصى لكل مهمة، القيمة الافتراضية 600 ثانية).

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
```

### الترجمة باستخدام اشتراك ChatGPT (`--use_codex`)

لا يستهلك هذا المزوّد أي مفتاح API؛ إذ يتحكم في CLI Codex الرسمي في وضع
غير تفاعلي، ولذلك تُحتسب الترجمة من حصة اشتراك ChatGPT (Plus وPro وBusiness…)
المدفوعة مسبقًا. وهذه هي الطريقة الوحيدة الموثقة من OpenAI لهذا الاستخدام — إذ إن
رموز `~/.codex/auth.json` لا تصادق على استدعاءات Platform API، ولا يقرأها هذا البرنامج
على أي حال.

**المتطلبات المسبقة:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

يُبحث عن الملف التنفيذي بالترتيب التالي: المتغير `CODEX_BIN`، ثم `PATH`،
ثم حزمة Python `openai-codex-cli-bin`. ولا توجد هذه الأخيرة عمدًا ضمن `requirements.txt`،
إذ يبلغ حجمها نحو 250 ميجابايت، ما كان سيفرضها على جميع المستخدمين من أجل مزوّد اختياري.

**ما ينبغي معرفته:**

- **لا يُستخدم أي مفتاح API.** تتم إزالة `OPENAI_API_KEY` و`CODEX_API_KEY` من
  بيئة العملية الفرعية، ما يضمن أن وجود مفتاح في `.env` لن يؤدي أبدًا إلى
  تحويل الترجمة إلى فوترة حسب الاستخدام.
- **كل مقطع = «رسالة محلية» واحدة** من نافذة الخمس ساعات للخطة.
  استخدم `--eco` (النموذج `gpt-5.6-luna`، من 250 إلى 2,000 رسالة/5 ساعات في Plus)
  بدلًا من نموذج الجودة (`gpt-5.6-sol`، من 10 إلى 100 رسالة/5 ساعات).
- **أبطأ** من استدعاء API: توقّع نحو 45 ثانية لملف README كامل، مقابل
  بضع ثوانٍ مباشرة.
- **مرفوض في CI** (عند تعريف `CI` أو `GITHUB_ACTIONS`): مصادقة الاشتراك
  غير مخصصة لـ runner مشترك، كما أن OpenAI لا توصي بهذا المسار في المستودعات العامة.
  استخدم مفتاح API لهذا المسار.
- متغيرات البيئة: `CODEX_BIN` (المسار الصريح للملف التنفيذي) و
  `CODEX_TIMEOUT` (الثواني لكل مقطع، القيمة الافتراضية `600`).

### الترجمة باستخدام اشتراك Grok (`--use_grok_cli`)

المبدأ نفسه المتبع في `--use_codex`، مع CLI الرسمي **Grok Build**:
تُحتسب الترجمة من اشتراك Grok (SuperGrok / X Premium+) بدلًا من فوترة الرموز المميزة.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**العزل — يُرجى القراءة قبل الاستخدام.** هذا المزوّد **أضعف بنيويًا
من `--use_codex`**، وهذا أمر مقصود:

- يعمل Codex في `--sandbox read-only`، وهو حد تفرضه المنظومة.
- لا يمكن تطبيق sandbox الخاص بـ Grok على كثير من أجهزة Linux الحديثة:
  إذ يحظر AppArmor مساحات أسماء المستخدمين غير المميّزة منذ Ubuntu 24.04،
  كما تفشل قائمة منع مقابس تشغيل الحاويات إذا كان `/run/podman` مضبوطًا على `0700`.
  وعندما يتعذر تطبيق ملف تعريف **مدمج**، يبدأ التشغيل **دون عزل، بصمت**.
- لذلك لا يطلب البرنامج أي ملف تعريف افتراضيًا، ولا ينتقل أبدًا إلى بديل
  بصمت، بل يعرض تحذيرًا. ويعتمد العزل على قواعد `--deny` في CLI
  (ومنها قاعدة catch-all `*`)، وهي طبقة القياس الوحيدة التي تعمل بمبدأ
  _fail-closed_ — فالقاعـدة غير المعروفة تؤدي إلى رفض التشغيل بدل إزالة الحماية دون إبلاغ.
- **لفرض** عزل نظام التشغيل: `GROK_TRANSLATE_SANDBOX=read-only`. سيفشل التشغيل إذا تعذر على الجهاز
  احترامه، وهذا هو السلوك المطلوب.

**الحصة**: إن مخزون Grok **أسبوعي ومشترك** مع Chat وImagine وVoice، ولا يوجد
أي أمر يسمح بقراءته. لذلك قد تستهلك معالجة دفعية جزءًا من استخدامك للمحادثة
دون أي إشارة إلى ذلك — ومن هنا جاء الحد الأقصى للتزامن البالغ 2 والتحذير في
`regen_translations.sh`.

المتغيرات الأخرى: `GROK_BIN` (مسار الملف التنفيذي)، و`GROK_TIMEOUT` (القيمة الافتراضية 900 ثانية).

لإعادة إنشاء الترجمات الـ28:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### الوضع الاقتصادي

يستخدم نماذج أسرع وأقل تكلفة (gpt-5.6-luna وclaude-haiku-4-5 وgemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### الخيارات

| الخيار | الوصف |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file` | ملف Markdown واحد لترجمته |
| `--source_dir` | مجلد المصدر الذي يحتوي على ملفات Markdown |
| `--target_dir` | مجلد الإخراج للملفات المترجمة |
| `--source_lang` | لغة المصدر (الافتراضية: `fr`) |
| `--target_lang` | اللغة الهدف (الافتراضية: `en`) |
| `--model` | النموذج المحدد المطلوب استخدامه |
| `--eco` | استخدام النماذج الاقتصادية |
| `--use_mistral` | استخدام Mistral AI API |
| `--use_claude` | استخدام Claude API |
| `--use_gemini` | استخدام Gemini API |
| `--use_codex` | استخدام CLI Codex ضمن حصة اشتراك ChatGPT |
| `--use_grok` | استخدام xAI API (Grok) — يتطلب `XAI_API_KEY` |
| `--use_grok_cli` | استخدام CLI Grok ضمن حصة اشتراك Grok |
| `--force` | فرض إعادة الترجمة |
| `--keep_filename` | الاحتفاظ باسم الملف الأصلي |
| `--news` | وضع الأخبار: يحمي الاقتباسات EN ويتعامل مع الأعلام حسب اللغة |
| `--add_translation_note` | إضافة ملاحظة ترجمة |
| `--note_position` | موضع الملاحظة: `top` أو `bottom` (الافتراضي)، أو `both` |
| `--note_format` | تنسيق الملاحظة: `legacy` (الافتراضي، فقرة عريضة) أو `marker` |
| `--include_model` | تضمين اسم النموذج في ملف الإخراج |
| `--reasoning_effort` | جهد الاستدلال GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **أعلام المزوّدين الستة متنافية.** كان جمع اثنين منها مقبولًا سابقًا بصمت، وكان
> يؤدي إلى اختيار أول مزوّد تم اختباره: لذلك كان من الممكن أن تنتقل ترجمة مطلوبة
> من حصة اشتراك (`--use_codex`، `--use_grok_cli`) إلى الفوترة حسب الاستخدام دون أي تحذير.
> أما `argparse` فيرفض الآن هذا الجمع.

### ملاحظة الترجمة: المواضع والتنسيقات

مع `--add_translation_note`، يستطيع المترجم وضع الملاحظة في الأعلى أو الأسفل أو في الموضعين،
وعرضها إما بتنسيق نص عادي (للتوافق مع الإصدارات السابقة) أو بتنسيق `marker`
يمكن لإضافة Markdown استهلاكه.

**الموضع** (`--note_position`):

- `bottom` (الافتراضي): الملاحظة في نهاية الملف، كما كان تاريخيًا.
- `top`: تُدرج الملاحظة **بعد frontmatter الخاص بـ YAML** (لأمان Astro Content Collections وgray-matter وغيرهما).
- `both`: تُدرج الملاحظة في الأعلى والأسفل (استدعاء LLM واحد، ويُعاد استخدام المحتوى في الموضعين).

**التنسيق** (`--note_format`):

- `legacy` (الافتراضي): فقرة عريضة `**...**` — سلوك مطابق تمامًا للإصدار v1.8، بايتًا ببايت. متوافق مع Hugo وGitHub وGitLab وأي عارض Markdown.
- `marker`: تعريف Markdown غير مرئي لمرجع رابط (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)، يتبعه اقتباس كتلي عريض. يمكن قراءته أصليًا على GitHub/GitLab، كما يمكن لإضافة remark في Astro استغلاله أثناء البناء لإنتاج شريط منسق (راجع مدونة jls42.org).

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

| المزوّد | الجودة (الافتراضي) | الاقتصادي (`--eco`) |
| -------- | ---------------------- | ----------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |

> **التوصية للترجمات المطوّلة**: يحافظ `--use_gemini` (الافتراضي = `gemini-3.7-flash`) بأمانة على بنية Markdown في النصوص البرمجية غير اللاتينية (PL وJA وZH وAR وHI)، بما في ذلك الوضع `--news` حيث تكون أمانة العناصر النائبة مهمة. وقد قيس ذلك على ملف README هذا المترجم إلى اليابانية: بنية مطابقة لـ `gemini-3.1-pro-preview` (21 قائمة، و18 كتلة كود، و13 رابط HTML، و13 صورة، مع الحفاظ على جميع عناوين URL) بزمن استجابة أقل بنحو 6 مرات. يظل OpenAI هو الافتراضي للحفاظ على التوافق مع الإصدارات السابقة.

## مشاريع تستخدم هذا البرنامج النصي

- **[jls42.org](https://jls42.org)** - مدونة شخصية متعددة اللغات (15 لغة)

## المؤلف

Julien LE SAUX  
البريد الإلكتروني: contact@jls42.org

## الترخيص

GNU GENERAL PUBLIC LICENSE الإصدار 3. راجع [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**مقالة مترجمة من الفرنسية إلى العربية باستخدام gpt-5.6-luna.**
