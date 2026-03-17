# مترجم Markdown المدعوم بالذكاء الاصطناعي

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

مترجم ملفات Markdown باستخدام **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini**.

يقوم هذا البرنامج النصي بلغة Python بترجمة ملفات Markdown من لغة مصدر إلى لغة هدف مع الحفاظ على التنسيق وكتل الشيفرة والبيانات الوصفية في front matter.

## الميزات الرئيسية

- **متعدد المزودين**: دعم 4 واجهات API (OpenAI وMistral وClaude وGemini)
- **نماذج 2026**: GPT-5.4 وClaude Sonnet 4.5 وGemini 3.1 Pro
- **الوضع الاقتصادي**: خيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- **ملف واحد**: خيار `--file` لترجمة ملف واحد
- **تجزئة ذكية**: التعامل مع النصوص الطويلة مع حدود الرموز لكل نموذج
- **الحفاظ على الشيفرة**: تُحفظ كتل الشيفرة وكذلك الشيفرة المضمنة (`` `...` ``)
- **اسم الملف**: خيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **وضع الأخبار**: خيار `--news` لحماية الاقتباسات الإنجليزية والتعامل مع الأعلام في المقالات الإخبارية
- **إعدادات .env**: دعم ملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## الإعداد

أنشئ ملف `.env` في جذر المشروع أو عرّف متغيرات البيئة:

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

### ترجمة دليل

```bash
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### الوضع الاقتصادي

يستخدم نماذج أسرع وأقل تكلفة (gpt-5-mini، claude-haiku، gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### الخيارات

| الخيار | الوصف |
|--------|-------------|
| `--file` | ملف Markdown واحد للترجمة |
| `--source_dir` | دليل المصدر الذي يحتوي على ملفات Markdown |
| `--target_dir` | دليل الإخراج للملفات المترجمة |
| `--source_lang` | لغة المصدر (الافتراضي: `fr`) |
| `--target_lang` | لغة الهدف (الافتراضي: `en`) |
| `--model` | النموذج المحدد المراد استخدامه |
| `--eco` | استخدام النماذج الاقتصادية |
| `--use_mistral` | استخدام واجهة Mistral AI API |
| `--use_claude` | استخدام واجهة Claude API |
| `--use_gemini` | استخدام واجهة Gemini API |
| `--force` | فرض إعادة الترجمة |
| `--keep_filename` | الاحتفاظ باسم الملف الأصلي |
| `--news` | وضع الأخبار: يحمي الاقتباسات الإنجليزية، ويتعامل مع الأعلام حسب اللغة |
| `--add_translation_note` | إضافة ملاحظة ترجمة |
| `--include_model` | تضمين اسم النموذج في ملف الإخراج |

### النماذج الافتراضية (2026)

| Provider | الجودة (افتراضي) | الاقتصادي (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## المشاريع التي تستخدم هذا البرنامج النصي

- **[jls42.org](https://jls42.org)** - مدونة شخصية متعددة اللغات (15 لغة)

## المؤلف

Julien LE SAUX
البريد الإلكتروني: contact@jls42.org

## الرخصة

GNU GENERAL PUBLIC LICENSE Version 3. راجع [LICENSE](LICENSE).