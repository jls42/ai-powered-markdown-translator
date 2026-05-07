# مترجم Markdown مدعوم بالذكاء الاصطناعي

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 جودة الكود</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="حالة بوابة الجودة"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="تقييم الأمان"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="تقييم الاعتمادية"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="تقييم قابلية الصيانة"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="التغطية"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="الثغرات"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="الأخطاء"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="روائح الكود"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="نسبة الأسطر المكررة (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="الدين التقني"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="أسطر الكود"></a>
</p>

مترجم ملفات Markdown يستخدم **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini**.

هذا السكربت بلغة Python يترجم ملفات Markdown من لغة مصدر إلى لغة هدف مع الحفاظ على التنسيق، وكتل الكود، والبيانات الوصفية front matter.

## الميزات الرئيسية

- **متعدد المزودين**: دعم 4 واجهات API (OpenAI، Mistral، Claude، Gemini)
- **نماذج 2026**: GPT-5.5، Claude Sonnet 4.6، Gemini 3.1 Pro
- **الوضع الاقتصادي**: خيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- **ملف واحد**: خيار `--file` لترجمة ملف واحد
- **تقسيم ذكي**: التعامل مع النصوص الطويلة مع حدود الرموز لكل نموذج
- **الحفاظ على الكود**: تُحفظ كتل الكود وكذلك الكود المضمن `...`
- **اسم الملف**: خيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **وضع الأخبار**: خيار `--news` لحماية الاقتباسات الإنجليزية والتعامل مع الأعلام في مقالات الأخبار
- **تهيئة .env**: دعم ملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### أدوات الجودة (اختياري لكن موصى به)

يستخدم المشروع [`pre-commit`](https://pre-commit.com) لمنع الالتزام بكود سيئ التنسيق أو غير آمن أو يحتوي على سر. التثبيت:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

الـ hooks النشطة: ruff (lint+format)، shellcheck (bash)، prettier (markdown/yaml/json)، Lizard (التعقيد)، detect-secrets (مفاتيح API)، mypy (الكتابة التدريجية)، Opengrep (SAST)، pip-audit (اعتمادات CVE)، unittest. راجع قسم `CLAUDE.md` _Quality / pre-commit_ للتفاصيل.

## الإعداد

أنشئ ملف `.env` في جذر المشروع أو حدّد متغيرات البيئة:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## الاستخدام

### ترجمة ملف واحد

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ترجمة مجلد

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

### الوضع الاقتصادي

يستخدم نماذج أسرع وأقل تكلفة (gpt-5.4-mini، claude-haiku، gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### الخيارات

| الخيار                   | الوصف                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | ملف Markdown واحد للترجمة                                       |
| `--source_dir`           | المجلد المصدر الذي يحتوي على ملفات Markdown                        |
| `--target_dir`           | مجلد الإخراج للملفات المترجمة                          |
| `--source_lang`          | لغة المصدر (الافتراضي: `fr`)                                             |
| `--target_lang`          | لغة الهدف (الافتراضي: `en`)                                              |
| `--model`                | النموذج المحدد للاستخدام                                             |
| `--eco`                  | استخدام النماذج الاقتصادية                                         |
| `--use_mistral`          | استخدام واجهة Mistral AI API                                                |
| `--use_claude`           | استخدام واجهة Claude API                                                    |
| `--use_gemini`           | استخدام واجهة Gemini API                                                    |
| `--force`                | فرض إعادة الترجمة                                                  |
| `--keep_filename`        | الاحتفاظ باسم الملف الأصلي                                     |
| `--news`                 | وضع الأخبار: يحمي الاقتباسات EN، ويتعامل مع الأعلام حسب اللغة |
| `--add_translation_note` | إضافة ملاحظة ترجمة                                           |
| `--note_position`        | موضع الملاحظة: `top`، `bottom` (الافتراضي)، أو `both`                |
| `--note_format`          | صيغة الملاحظة: `legacy` (الافتراضي، فقرة بخط عريض) أو `marker`       |
| `--include_model`        | تضمين اسم النموذج في ملف الإخراج                       |

### ملاحظة الترجمة: المواضع والصيغ

مع `--add_translation_note`، يمكن للمترجم وضع الملاحظة في الأعلى أو الأسفل أو في كلا الموضعين، وجعلها إما بصيغة نص عادي (متوافق مع الإصدارات السابقة) أو بصيغة `marker` قابلة للاستهلاك بواسطة إضافة Markdown.

**الموضع** (`--note_position`) :

- `bottom` (الافتراضي) : ملاحظة في نهاية الملف، كما كان تاريخيًا.
- `top` : ملاحظة تُدرج **بعد frontmatter YAML** (أمان Astro Content Collections، gray-matter، إلخ).
- `both` : ملاحظة تُدرج في الأعلى وفي الأسفل (استدعاء LLM واحد فقط، والمحتوى يُعاد استخدامه لكلا الموضعين).

**الصيغة** (`--note_format`) :

- `legacy` (الافتراضي) : فقرة بخط عريض `**...**` — سلوك مطابق تمامًا لـ v1.8، حرفًا بحرف. متوافق مع Hugo وGitHub وGitLab وأي renderer Markdown.
- `marker` : تعريف مرجع رابط Markdown غير مرئي `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` يتبعه blockquote بخط عريض. قابل للقراءة أصليًا على GitHub/GitLab، وقابل للاستفادة عند البناء بواسطة إضافة remark على جانب Astro لإنتاج شريط منسق (cf. blog jls42.org).

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

| المزود | الجودة (الافتراضي)         | الاقتصادي (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **توصية للترجمات الطويلة** : `--use_gemini` (الافتراضي = `gemini-3.1-pro-preview` الجودة، `--eco` = `gemini-3.1-flash-lite-preview`) يميل إلى الحفاظ على بنية markdown بشكل أفضل على السكربتات غير اللاتينية (PL، JA، ZH، AR، HI)، خاصة في وضع `--news` حيث تكون دقة العناصر النائبة مهمة. يبقى OpenAI الافتراضي للتوافق مع الإصدارات السابقة.

## المشاريع التي تستخدم هذا السكربت

- **[jls42.org](https://jls42.org)** - مدونة شخصية متعددة اللغات (15 لغة)

## المؤلف

Julien LE SAUX
البريد الإلكتروني: contact@jls42.org

## الرخصة

GNU GENERAL PUBLIC LICENSE Version 3. راجع [LICENSE](LICENSE).

**مقالة مترجمة من fr إلى ar باستخدام gpt-5.4-mini.**
