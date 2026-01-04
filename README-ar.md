# مترجم Markdown مدعوم بالذكاء الاصطناعي

🌍 [الإنجليزية](README-en.md) | [الإسبانية](README-es.md) | [الصينية](README-zh.md) | [الألمانية](README-de.md) | [اليابانية](README-ja.md) | [الكورية](README-ko.md) | [العربية](README-ar.md) | [الهندية](README-hi.md) | [الإيطالية](README-it.md) | [الهولندية](README-nl.md) | [البولندية](README-pl.md) | [البرتغالية](README-pt.md) | [الرومانية](README-ro.md) | [السويدية](README-sv.md)

مترجم لملفات Markdown يستخدم **OpenAI**، **Mistral AI**، **Claude (Anthropic)** و **Google Gemini**.

يقوم هذا السكربت بلغة بايثون بترجمة ملفات Markdown من لغة المصدر إلى لغة الهدف مع الحفاظ على التنسيق، وكتل الشيفرة وبيانات front matter.

## الميزات الرئيسية

- **متعدد المزودين**: دعم 4 واجهات برمجة تطبيقات (OpenAI، Mistral، Claude، Gemini)
- **نماذج 2026**: GPT-5، Claude Sonnet 4.5، Gemini 3 Pro
- **الوضع الاقتصادي**: خيار `--eco` لاستخدام نماذج أسرع وأرخص
- **ملف واحد**: خيار `--file` لترجمة ملف واحد
- **التجزئة الذكية**: معالجة النصوص الطويلة مع حدود التوكن لكل نموذج
- **الحفاظ على الشيفرة**: كتل الشيفرة وكود inline (`` `...` ``) محفوظان
- **اسم الملف**: خيار `--keep_filename` للاحتفاظ بالاسم الأصلي
- **تكوين .env**: دعم الملف `.env` لمفاتيح API
- **ملاحظة الترجمة**: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## الإعداد

أنشئ ملف `.env` في جذر المشروع أو قم بتعيين متغيرات البيئة :

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
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### الوضع الاقتصادي

يستخدم نماذج أسرع وأرخص (gpt-5-mini، claude-haiku، gemini-flash) :

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
| `--model` | نموذج محدد للاستخدام |
| `--eco` | استخدام النماذج الاقتصادية |
| `--use_mistral` | استخدام واجهة برمجة تطبيقات Mistral AI |
| `--use_claude` | استخدام واجهة برمجة تطبيقات Claude |
| `--use_gemini` | استخدام واجهة برمجة تطبيقات Gemini |
| `--force` | إجبار إعادة الترجمة |
| `--keep_filename` | الاحتفاظ باسم الملف الأصلي |
| `--add_translation_note` | إضافة ملاحظة ترجمة |
| `--include_model` | تضمين اسم النموذج في ملف الإخراج |

### النماذج الافتراضية (2026)

| المزود | الجودة (الافتراضي) | اقتصادي (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## المشاريع التي تستخدم هذا السكربت

- **[jls42.org](https://jls42.org)** - مدونة شخصية مترجمة إلى 15 لغة (364 ملفًا، 22 مقالة + 4 مشاريع)

## المؤلف

Julien LE SAUX  
البريد الإلكتروني: contact@jls42.org

## الرخصة

رخصة جنو العمومية الإصدار 3. راجع [الرخصة](LICENSE).

**تمت ترجمة هذا المستند من النسخة fr إلى اللغة ar باستخدام نموذج gpt-5-mini. لمزيد من المعلومات حول عملية الترجمة، راجع https://gitlab.com/jls42/ai-powered-markdown-translator**

