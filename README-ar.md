# مترجم Markdown المدعوم بالذكاء الاصطناعي

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

مترجم ملفات Markdown يستخدم **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini**.

يقوم هذا السكربت بلغة Python بترجمة ملفات Markdown من لغة مصدر إلى لغة هدف مع الحفاظ على التنسيق، وكتل التعليمات البرمجية، وبيانات front matter الوصفية.

## الميزات الرئيسية

- **متعدد المزودين**: دعم 4 واجهات برمجة تطبيقات (OpenAI، Mistral، Claude، Gemini)
- **نماذج 2026**: GPT-5.5، Claude Sonnet 4.6، Gemini 3.1 Pro
- **الوضع الاقتصادي**: خيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- **ملف واحد**: خيار `--file` لترجمة ملف واحد
- **التقسيم الذكي**: إدارة النصوص الطويلة مع حدود tokens لكل نموذج
- **الحفاظ على الكود**: تُحفظ كتل التعليمات البرمجية وكذلك الكود المضمن (`` `...` ``)
- **اسم الملف**: خيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **وضع الأخبار**: خيار `--news` لحماية الاقتباسات الإنجليزية وإدارة الأعلام في مقالات الأخبار
- **إعدادات .env**: دعم ملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### أدوات الجودة (اختياري ولكن موصى به)

يستخدم المشروع [`pre-commit`](https://pre-commit.com) لمنع committer من إدخال كود سيئ التنسيق أو معرض للخطر أو يحتوي على سر. التثبيت:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

الـ hooks النشطة: ruff (lint+format)، shellcheck (bash)، prettier (markdown/yaml/json)، Lizard (التعقيد)، detect-secrets (مفاتيح API)، mypy (typing تدريجي)، Opengrep (SAST)، pip-audit (CVE deps)، unittest. راجع قسم `CLAUDE.md` _Quality / pre-commit_ للتفاصيل.

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
| `--source_dir`           | مجلد المصدر الذي يحتوي على ملفات Markdown                        |
| `--target_dir`           | مجلد الإخراج للملفات المترجمة                          |
| `--source_lang`          | لغة المصدر (الافتراضي: `fr`)                                             |
| `--target_lang`          | لغة الهدف (الافتراضي: `en`)                                              |
| `--model`                | نموذج محدد للاستخدام                                             |
| `--eco`                  | استخدام النماذج الاقتصادية                                         |
| `--use_mistral`          | استخدام واجهة برمجة تطبيقات Mistral AI                                                |
| `--use_claude`           | استخدام واجهة برمجة تطبيقات Claude                                                    |
| `--use_gemini`           | استخدام واجهة برمجة تطبيقات Gemini                                                    |
| `--force`                | فرض إعادة الترجمة                                                  |
| `--keep_filename`        | الاحتفاظ باسم الملف الأصلي                                     |
| `--news`                 | وضع الأخبار: يحمي الاقتباسات EN، ويدير الأعلام حسب اللغة |
| `--add_translation_note` | إضافة ملاحظة ترجمة                                           |
| `--include_model`        | تضمين اسم النموذج في ملف الإخراج                       |

### النماذج الافتراضية (2026)

| Provider | الجودة (الافتراضي)         | اقتصادي (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **توصية للترجمات الطويلة**: `--use_gemini` (الافتراضي = `gemini-3.1-pro-preview` جودة، و`--eco` = `gemini-3-flash-preview`) يميل إلى الحفاظ على بنية Markdown بشكل أفضل في السكربتات غير اللاتينية (PL، JA، ZH، AR، HI)، خاصة في وضع `--news` حيث تهم دقة الـ placeholders. يبقى OpenAI هو الافتراضي من أجل التوافق العكسي.

## المشاريع التي تستخدم هذا السكربت

- **[jls42.org](https://jls42.org)** - مدونة شخصية متعددة اللغات (15 لغة)

## المؤلف

Julien LE SAUX  
البريد الإلكتروني: contact@jls42.org

## الترخيص

GNU GENERAL PUBLIC LICENSE Version 3. راجع [LICENSE](LICENSE).

**تمت ترجمة هذا المستند من الإصدار fr إلى اللغة ar باستخدام النموذج gpt-5.4-mini. لمزيد من المعلومات حول عملية الترجمة، راجع https://gitlab.com/jls42/ai-powered-markdown-translator**

