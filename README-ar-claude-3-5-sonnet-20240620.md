# مترجم Markdown مدعوم بالذكاء الاصطناعي باستخدام OpenAI وMistral AI وClaude من Anthropic

هذا المشروع عبارة عن نص برمجي Python متقدم يستخدم واجهات برمجة التطبيقات (APIs) الخاصة بـ OpenAI أو Mistral AI أو Claude من Anthropic لترجمة ملفات Markdown من لغة المصدر إلى لغة الهدف. تم تصميمه ليكون مرنًا وسهل الاستخدام، ويقدم خيارات إضافية مثل إضافة ملاحظة الترجمة، وإدارة محسنة لملفات الإخراج، واكتشاف الملفات الموجودة، ودعم العديد من اللغات ونماذج الترجمة.

للعرض التوضيحي والشروحات التفصيلية، قم بزيارة [jls42.org](https://jls42.org/) أو في النسخة المترجمة: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) و [jls42.org 中文](https://jls42.org/traductions_zh/).

## الميزات الرئيسية

- **الترجمة المدعومة بالذكاء الاصطناعي**: استخدم أحدث تقنيات الذكاء الاصطناعي لترجمة مستنداتك باستخدام OpenAI أو Mistral AI أو Claude من Anthropic.
- **دعم متعدد اللغات**: ترجم مستنداتك إلى عدة لغات مع دعم لنماذج لغوية مختلفة.
- **التقسيم الذكي**: إدارة فعالة للنصوص الطويلة من خلال التقسيم التلقائي.
- **ملاحظة الترجمة**: أضف تلقائيًا ملاحظة ترجمة لإعلام القراء بالعملية المستخدمة.
- **إدارة محسنة لملفات الإخراج**: تحقق مما إذا كانت الترجمة موجودة بالفعل قبل بدء الترجمة.
- **اكتشاف محسن للملفات الموجودة**: ابحث عن الملفات المطابقة لاسم الملف الأصلي واللغة الهدف.
- **مرن وقابل للتوسع**: تم هيكلة الكود للسماح بسهولة إضافة ميزات جديدة.

## المتطلبات الأساسية

- Python 3.6 أو إصدار أحدث.
- مفتاح API صالح لـ OpenAI أو Mistral AI أو Claude من Anthropic.

## التثبيت

1. استنسخ مستودع Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. قم بتثبيت التبعيات اللازمة:
```
pip install -r requirements.txt
```

## الإعداد

قم بإعداد بيئتك عن طريق تعيين متغيرات البيئة لمفاتيح API اللازمة:

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

يوفر النص البرمجي عدة خيارات لتخصيص عملية الترجمة:

### الخيارات العامة

- `--source_dir`: الدليل الذي يحتوي على ملفات Markdown المراد ترجمتها.
- `--target_dir`: دليل الإخراج للملفات المترجمة.
- `--model`: نموذج ترجمة GPT المراد استخدامه. النموذج الافتراضي يعتمد على API المحدد.
- `--source_lang`: اللغة المصدر للمستندات. مهمة خاصة لإضافة ملاحظات الترجمة.
- `--target_lang`: اللغة الهدف للترجمة. الافتراضي هو الإنجليزية.
- `--force`: فرض الترجمة حتى لو كانت هناك ترجمة موجودة بالفعل للملف.

### خيارات API محددة

- `--use_mistral`: استخدام API Mistral AI للترجمة.
- `--use_claude`: استخدام API Claude من Anthropic للترجمة.
- `--add_translation_note`: إضافة ملاحظة ترجمة إلى المحتوى المترجم، محددة الطريقة والأدوات المستخدمة.

### أمثلة الاستخدام

- الترجمة من الفرنسية إلى الإنجليزية باستخدام OpenAI، مع إضافة ملاحظة ترجمة:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- الترجمة من الفرنسية إلى الإسبانية باستخدام Mistral AI، بدون ملاحظة ترجمة:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## المؤلف

Julien LE SAUX  
البريد الإلكتروني: contact@jls42.org

## الترخيص

هذا المشروع مرخص بموجب GNU GENERAL PUBLIC LICENSE الإصدار 3، 29 يونيو 2007. انظر ملف [LICENSE](LICENSE) لمزيد من التفاصيل.

**هذا المستند تمت ترجمته من الإصدار fr إلى اللغة ar باستخدام النموذج claude-3-5-sonnet-20240620. لمزيد من المعلومات حول عملية الترجمة، راجع https://gitlab.com/jls42/ai-powered-markdown-translator**

