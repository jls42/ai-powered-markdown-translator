# ترجمة ماركداون المدعومة بالذكاء الاصطناعي باستخدام OpenAI و Mistral AI و Claude من Anthropic

هذا المشروع هو سكريبت Python متقدم يستخدم واجهات برمجة التطبيقات OpenAI و Mistral AI و Claude من Anthropic لترجمة ملفات ماركداون من لغة مصدر إلى لغة هدف. وهو مصمم ليكون مرنًا وسهل الاستخدام، ويوفر خيارات إضافية مثل إضافة ملاحظة ترجمة، وإدارة محسنة لملفات الإخراج، والكشف عن الملفات الموجودة، ودعم اللغات ونماذج الترجمة المتعددة.

لعرض توضيحي وشرح مفصل، يرجى زيارة [jls42.org](https://jls42.org/) أو النسخة المترجمة: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) و [jls42.org 中文](https://jls42.org/traductions_zh/).

## الميزات الرئيسية

- **ترجمة مدعومة بالذكاء الاصطناعي**: استخدم أحدث تقنيات الذكاء الاصطناعي لترجمة وثائقك باستخدام OpenAI و Mistral AI و Claude من Anthropic.
- **دعم متعدد اللغات**: ترجم وثائقك إلى عدة لغات مع دعم نماذج اللغة المختلفة.
- **تقسيم ذكي**: أدر النصوص الطويلة بكفاءة بفضل التقسيم الآلي.
- **ملاحظة الترجمة**: أضف تلقائيًا ملاحظة ترجمة لإعلام القراء على العملية المستخدمة.
- **إدارة محسنة لملفات الإخراج**: تحقق مما إذا كانت ترجمة موجودة بالفعل قبل بدء الترجمة.
- **الكشف عن الملفات الموجودة محسنًا**: ابحث عن ملفات تتطابق مع اسم أساس الملف الأصلي واللغة الهدف.
- **مرن وقابل للتوسيع**: الكود منظم لتسهيل إضافة ميزات جديدة.

## المتطلبات الأساسية

- Python 3.6 أو إصدار أحدث.
- مفتاح API صالح لـ OpenAI أو Mistral AI أو Claude من Anthropic.

## التثبيت

1. استنسخ المستودع Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. ثبت التبعيات اللازمة:
```
pip install -r requirements.txt
```

## التكوين

قم بتكوين بيئتك عن طريق تعريف متغيرات البيئة للمفاتيح API المطلوبة:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Claude من Anthropic**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## الاستخدام

يوفر السكريبت عدة خيارات لتخصيص عملية الترجمة:

### خيارات عامة

- `--source_dir`: الدليل الذي يحتوي على ملفات ماركداون المراد ترجمتها.
- `--target_dir`: الدليل الخارجي لملفات الترجمة.
- `--model`: نموذج الترجمة GPT المراد استخدامه. النموذج الافتراضي يعتمد على API المختارة.
- `--source_lang`: لغة مصدر الوثائق. مهمة بشكل خاص لإضافة ملاحظات الترجمة.
- `--target_lang`: اللغة الهدف للترجمة. الافتراضية هي الإنجليزية.
- `--force`: فرض الترجمة حتى إذا كانت ترجمة موجودة بالفعل للملف.

### خيارات محددة لـ API

- `--use_mistral`: استخدام API Mistral AI للترجمة.
- `--use_claude`: استخدام API Claude من Anthropic للترجمة.
- `--add_translation_note`: إضافة ملاحظة ترجمة إلى المحتوى المترجم، وتحديد الطريقة والأدوات المستخدمة.

### أمثلة على الاستخدام

- ترجمة من الفرنسية إلى الإنجليزية باستخدام OpenAI، مع إضافة ملاحظة ترجمة:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- ترجمة من الفرنسية إلى الإسبانية باستخدام Mistral AI، بدون ملاحظة ترجمة:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## المؤلف

Julien LE SAUX
البريد الإلكتروني: contact@jls42.org

## الرخصة

هذا المشروع تحت رخصة GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. انظر الملف [LICENSE](LICENSE) لمزيد من التفاصيل.

**'Ce document a été traduit de la version fr vers la langue ar en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator'.**

