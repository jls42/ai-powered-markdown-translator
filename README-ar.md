# مترجم Markdown مدعوم بالذكاء الاصطناعي

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

مترجم ملفات Markdown يستخدم **OpenAI** و**Mistral AI** و**Claude (Anthropic)** و**Google Gemini**.

يترجم هذا السكربت بلغة Python ملفات Markdown من لغة مصدر إلى لغة هدف مع الحفاظ على التنسيق وكتل الكود وبيانات front matter الوصفية.

## الميزات الرئيسية

- متعدد المزوّدين: دعم 4 واجهات برمجة تطبيقات (OpenAI, Mistral, Claude, Gemini)
- نماذج 2026: GPT-5، Claude Sonnet 4.5، Gemini 3 Pro
- الوضع الاقتصادي: خيار `--eco` لاستخدام نماذج أسرع وأقل تكلفة
- ملف واحد: خيار `--file` لترجمة ملف واحد
- تقسيم ذكي: إدارة النصوص الطويلة مع حدود التوكنات لكل نموذج
- الحفاظ على الكود: لا تُترجم كتل الكود
- ملاحظة ترجمة: إضافة اختيارية لملاحظة في نهاية المستند

## التثبيت

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## التهيئة

قم بتعيين متغير البيئة لواجهة البرمجة التي ترغب في استخدامها:

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
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

يستخدم نماذج أسرع وأقل تكلفة (gpt-5-mini وclaude-haiku وgemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### الخيارات

| الخيار | الوصف |
|--------|-------|
| `--file` | ملف Markdown واحد للترجمة |
| `--source_dir` | الدليل المصدري الذي يحتوي على ملفات Markdown |
| `--target_dir` | دليل الإخراج للملفات المترجمة |
| `--source_lang` | اللغة المصدر (الافتراضي: `fr`) |
| `--target_lang` | اللغة الهدف (الافتراضي: `en`) |
| `--model` | النموذج المحدد للاستخدام |
| `--eco` | استخدام النماذج الاقتصادية |
| `--use_mistral` | استخدام واجهة برمجة Mistral AI |
| `--use_claude` | استخدام واجهة برمجة Claude |
| `--use_gemini` | استخدام واجهة برمجة Gemini |
| `--force` | فرض إعادة الترجمة |
| `--add_translation_note` | إضافة ملاحظة ترجمة |

### النماذج الافتراضية (2026)

| المزوّد | الجودة (افتراضي) | اقتصادي (`--eco`) |
|---------|-------------------|-------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## المؤلف

Julien LE SAUX
البريد الإلكتروني: contact@jls42.org

## الترخيص

رخصة GNU GENERAL PUBLIC LICENSE الإصدار 3. راجع [LICENSE](LICENSE).