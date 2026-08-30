# مترجم Markdown مدعوم بالذكاء الاصطناعي

🌍 [الفرنسية](README.md) | [الإنجليزية](README-en.md) | [الإسبانية](README-es.md) | [الصينية](README-zh.md) | [الألمانية](README-de.md) | [اليابانية](README-ja.md) | [الكورية](README-ko.md) | [العربية](README-ar.md) | [الهندية](README-hi.md) | [الإيطالية](README-it.md) | [الهولندية](README-nl.md) | [البولندية](README-pl.md) | [البرتغالية](README-pt.md) | [الرومانية](README-ro.md) | [السويدية](README-sv.md)

<h4 align="center">📊 جودة الشيفرة</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="حالة بوابة الجودة"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="تصنيف الأمان"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="تصنيف الموثوقية"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="تصنيف قابلية الصيانة"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="تغطية الاختبارات"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="الثغرات الأمنية"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="الأخطاء البرمجية"></a>
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

مترجم لملفات Markdown يستخدم **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini**.

يترجم سكربت Python هذا ملفات Markdown من لغة مصدر إلى لغة مستهدفة مع الحفاظ على التنسيق وكتل الشيفرة وبيانات front matter الوصفية.

## الميزات الرئيسية

- **مزودون متعددون**: دعم 4 واجهات API ‏(OpenAI وMistral وClaude وGemini)، بالإضافة إلى CLI الخاص بـCodex ضمن اشتراك ChatGPT
- **نماذج 2026**: GPT-5.6 Terra وClaude Sonnet 5 وGemini 3.7 Flash
- **الوضع الاقتصادي**: الخيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- **ملف واحد**: الخيار `--file` لترجمة ملف واحد فقط
- **تقسيم ذكي**: معالجة النصوص الطويلة وفق حدود tokens لكل نموذج
- **الحفاظ على الشيفرة**: يُحافظ على كتل الشيفرة وكذلك الشيفرة المضمنة (`` `...` ``)
- **اسم الملف**: الخيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **وضع الأخبار**: الخيار `--news` لحماية الاقتباسات الإنجليزية ومعالجة الأعلام في المقالات الإخبارية
- **إعدادات .env**: دعم الملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### أدوات الجودة (اختيارية لكن موصى بها)

يستخدم المشروع [`pre-commit`](https://pre-commit.com) لمنع إجراء commit لشيفرة سيئة التنسيق أو تحتوي على ثغرات أو أسرار. للتثبيت:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

الـhooks النشطة: ruff ‏(lint+format)، وshellcheck ‏(bash)، وprettier ‏(markdown/yaml/json)، وLizard ‏(التعقيد)، وdetect-secrets ‏(مفاتيح API)، وmypy ‏(التحقق التدريجي من الأنواع)، وOpengrep ‏(SAST)، وpip-audit ‏(ثغرات CVE في التبعيات)، وunittest. راجع قسم _Quality / pre-commit_ في `CLAUDE.md` للتفاصيل.

## الإعداد

أنشئ ملف `.env` في جذر المشروع أو عرّف متغيرات البيئة:

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

يُقبل `GEMINI_API_KEY` بديلاً عن `GOOGLE_API_KEY` ‏(اصطلاح AI
Studio). المتغيرات الاختيارية: `XAI_BASE_URL` ‏(نقطة نهاية xAI، القيمة الافتراضية
`https://api.x.ai/v1`)، و`CLAUDE_TIMEOUT` ‏(عدد الثواني لكل استدعاء Anthropic، القيمة الافتراضية
900)، و`CODEX_BIN` / `CODEX_TIMEOUT`، و`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`،
و`GROK_TRANSLATE_SANDBOX` ‏(راجع قسم Grok CLI).

## الاستخدام

### ترجمة ملف واحد

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ترجمة مجلد

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

### الترجمة باستخدام اشتراك ChatGPT ‏(`--use_codex`)

لا يستهلك هذا المزود أي مفتاح API: فهو يشغّل CLI الرسمي لـCodex في الوضع
غير التفاعلي، ولذلك تُحتسب الترجمة من حصة اشتراك
ChatGPT ‏(Plus وPro وBusiness وغيرها) المدفوع مسبقًا. هذه هي الطريقة الوحيدة التي توثقها
OpenAI لهذا الاستخدام — إذ لا تُستخدم tokens الخاصة بـ`~/.codex/auth.json` للمصادقة على
استدعاءات API Platform، كما أن هذا السكربت لا يقرأها أصلًا.

**المتطلبات الأساسية:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

يُبحث عن الملف التنفيذي بهذا الترتيب: المتغير `CODEX_BIN`، ثم `PATH`،
ثم حزمة Python المسماة `openai-codex-cli-bin`. لم تُضمّن الأخيرة عمدًا
في `requirements.txt`: إذ يبلغ حجمها نحو 250 ميغابايت، ما كان سيفرضها على جميع
المستخدمين من أجل مزود اختياري.

**معلومات مهمة:**

- **لا يُستخدم أي مفتاح API.** تُزال `OPENAI_API_KEY` و`CODEX_API_KEY`
  من بيئة العملية الفرعية، ما يضمن أن وجود مفتاح
  في `.env` لن يحوّل الترجمة أبدًا إلى نظام الفوترة حسب
  الاستخدام.
- **كل مقطع يساوي «رسالة محلية» واحدة** ضمن نافذة الخمس ساعات للخطة.
  استخدم `--eco` ‏(النموذج `gpt-5.6-luna`، من 250 إلى 2 000 رسالة/5 ساعات ضمن Plus)
  بدلًا من نموذج الجودة (`gpt-5.6-sol`، من 10 إلى 100 رسالة/5 ساعات).
- **أبطأ** من استدعاء API: يستغرق ملف README كامل نحو 45 ثانية، مقابل
  بضع ثوانٍ عند الاتصال المباشر.
- **مرفوض في CI** ‏(عند تعريف `CI` أو `GITHUB_ACTIONS`): فالمصادقة عبر
  الاشتراك غير مخصصة لـrunner مشترك، كما لا توصي OpenAI بسير العمل هذا
  في المستودعات العامة. استخدم مفتاح API في هذه الحالة.
- متغيرات البيئة: `CODEX_BIN` ‏(المسار الصريح للملف التنفيذي) و
  `CODEX_TIMEOUT` ‏(عدد الثواني لكل مقطع، القيمة الافتراضية `600`).

### الترجمة باستخدام اشتراك Grok ‏(`--use_grok_cli`)

المبدأ نفسه المستخدم في `--use_codex`، ولكن مع CLI الرسمي **Grok Build**: تُحتسب
الترجمة من اشتراك Grok ‏(SuperGrok / X Premium+) بدلًا
من الفوترة حسب token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**العزل — يجب قراءته قبل الاستخدام.** هذا المزود **أضعف
بنيويًا** من `--use_codex`، وهذا مقبول عن قصد:

- يعمل Codex في `--sandbox read-only`، وهو حد يفرضه النظام.
- لا يمكن تطبيق sandbox الخاص بـGrok على كثير من أجهزة Linux
  الحديثة: إذ يحظر AppArmor مساحات أسماء المستخدمين غير المميزة منذ Ubuntu
  24.04، وتفشل قائمة حظر sockets الخاصة ببيئة تشغيل الحاويات إذا كان
  `/run/podman` مضبوطًا على `0700`. لكن ملف تعريف **مدمجًا** يتعذر
  تطبيقه يبدأ العمل **دون عزل وبصمت**.
- لذلك لا يطلب السكربت أي ملف تعريف افتراضيًا، و**لا يتراجع أبدًا
  بصمت**: بل يعرض تحذيرًا. يعتمد العزل على قواعد
  `--deny` الخاصة بـCLI ‏(ومنها قاعدة catch-all ‏`*`)، وهي الطبقة الوحيدة التي ثبت أنها
  _fail-closed_ — إذ تؤدي أي قاعدة مجهولة إلى رفض بدء التشغيل بدلًا من
  إزالة الحماية دون تنبيه.
- **لفرض** sandbox الخاص بنظام التشغيل: `GROK_TRANSLATE_SANDBOX=read-only`. سيفشل
  بدء التشغيل إذا تعذر على الجهاز الالتزام به، وهذا هو
  السلوك المقصود.

**الحصة**: حصة Grok **أسبوعية ومشتركة** بين Chat وImagine و
Voice، ولا يتيح أي أمر الاطلاع عليها. لذلك قد تستهلك المعالجة المجمعة
جزءًا من استخدامك للمحادثات دون أي تنبيه — ولهذا
يقتصر التزامن على 2 ويظهر تحذير في `regen_translations.sh`.

متغيرات أخرى: `GROK_BIN` ‏(مسار الملف التنفيذي)، و`GROK_TIMEOUT` ‏(القيمة الافتراضية 900 ثانية).

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
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### الخيارات

| الخيار                   | الوصف                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | ملف Markdown واحد لترجمته                                       |
| `--source_dir`           | مجلد المصدر الذي يحتوي على ملفات Markdown                        |
| `--target_dir`           | مجلد إخراج الملفات المترجمة                          |
| `--source_lang`          | لغة المصدر (القيمة الافتراضية: `fr`)                                             |
| `--target_lang`          | اللغة المستهدفة (القيمة الافتراضية: `en`)                                              |
| `--model`                | نموذج محدد لاستخدامه                                             |
| `--eco`                  | استخدام النماذج الاقتصادية                                         |
| `--use_mistral`          | استخدام API الخاص بـMistral AI                                                |
| `--use_claude`           | استخدام API الخاص بـClaude                                                    |
| `--use_gemini`           | استخدام API الخاص بـGemini                                                    |
| `--use_codex`            | استخدام CLI الخاص بـCodex من حصة اشتراك ChatGPT               |
| `--use_grok`             | استخدام API الخاص بـxAI ‏(Grok) — يتطلب `XAI_API_KEY`                      |
| `--use_grok_cli`         | استخدام CLI الخاص بـGrok من حصة اشتراك Grok                   |
| `--force`                | فرض إعادة الترجمة                                                  |
| `--keep_filename`        | الاحتفاظ باسم الملف الأصلي                                     |
| `--news`                 | وضع الأخبار: يحمي الاقتباسات الإنجليزية ويعالج الأعلام حسب اللغة |
| `--add_translation_note` | إضافة ملاحظة ترجمة                                           |
| `--note_position`        | موضع الملاحظة: `top` أو `bottom` ‏(الافتراضي) أو `both`                |
| `--note_format`          | تنسيق الملاحظة: `legacy` ‏(الافتراضي، فقرة عريضة) أو `marker`       |
| `--include_model`        | تضمين اسم النموذج في ملف الإخراج                       |
| `--reasoning_effort`     | جهد استدلال GPT-5.x: ‏`none`/`low`/`medium`/`high`/`xhigh`     |

### ملاحظة الترجمة: المواضع والتنسيقات

باستخدام `--add_translation_note`، يستطيع المترجم وضع الملاحظة في الأعلى أو الأسفل أو في الموضعين، وعرضها إما بتنسيق نصي بسيط متوافق مع الإصدارات السابقة، وإما بتنسيق `marker` يمكن أن يستهلكه plugin خاص بـMarkdown.

**الموضع** (`--note_position`):

- `bottom` ‏(الافتراضي): الملاحظة في نهاية الملف، كما جرت العادة.
- `top`: تُدرج الملاحظة **بعد frontmatter الخاص بـYAML** ‏(لضمان التوافق مع Astro Content Collections وgray-matter وغيرها).
- `both`: تُدرج الملاحظة في الأعلى والأسفل معًا (استدعاء LLM واحد، ويُعاد استخدام المحتوى في الموضعين).

**التنسيق** (`--note_format`):

- `legacy` ‏(الافتراضي): فقرة عريضة `**...**` — سلوك مطابق تمامًا للإصدار v1.8 على مستوى byte-for-byte. متوافق مع Hugo وGitHub وGitLab وأي renderer خاص بـMarkdown.
- `marker`: تعريف link reference غير مرئي في Markdown ‏(`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`)، يتبعه blockquote عريض. قابل للقراءة مباشرة على GitHub/GitLab، ويمكن أن يستخدمه plugin من نوع remark أثناء build في Astro لإنتاج لافتة منسقة (راجع مدونة jls42.org).

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

### النماذج الافتراضية (2026)

| المزود | الجودة (الافتراضي)       | الاقتصادي (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **توصية للترجمات الطويلة**: يحافظ `--use_gemini` ‏(الافتراضي = `gemini-3.7-flash`) بأمانة على بنية markdown في النصوص غير اللاتينية (PL وJA وZH وAR وHI)، بما في ذلك وضع `--news` الذي تكون فيه دقة placeholders مهمة. وقد أظهر القياس على نسخة README هذه المترجمة إلى اليابانية بنية مطابقة لـ`gemini-3.1-pro-preview` ‏(21 قائمة، و18 كتلة شيفرة، و13 رابط HTML، و13 صورة، مع الحفاظ على جميع URLs) بزمن استجابة أقل بنحو 6 أضعاف. يظل OpenAI الخيار الافتراضي حفاظًا على التوافق مع الإصدارات السابقة.

## مشاريع تستخدم هذا السكربت

- **[jls42.org](https://jls42.org)** - مدونة شخصية متعددة اللغات (15 لغة)

## المؤلف

Julien LE SAUX
البريد الإلكتروني: contact@jls42.org

## الترخيص

GNU GENERAL PUBLIC LICENSE Version 3. راجع [LICENSE](LICENSE).

**مقال مترجم من الفرنسية إلى العربية باستخدام gpt-5.6-sol.**
