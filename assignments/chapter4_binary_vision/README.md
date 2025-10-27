# فصل ۴: بینایی دودویی و آستانه‌گذاری
# Chapter 4: Binary Vision and Thresholding

**دانشجو / Student:** مسیح معافی / Masih Moafi  
**تاریخ / Date:** ۲۸ مهر ۱۴۰۴ (October 19, 2025)

---

## محتوای این فصل / Chapter Contents

این فصل شامل مباحث زیر است:

1. **آستانه‌گذاری سراسری و تطبیقی** - Global and Adaptive Thresholding
   - آستانه‌گذاری ساده (Simple Thresholding)
   - روش اتسو (Otsu's Method)
   - آستانه‌گذاری تطبیقی (Adaptive Thresholding)
2. **عملیات مورفولوژیکی** - Morphological Operations
   - فرسایش و اتساع (Erosion and Dilation)
   - باز و بسته کردن (Opening and Closing)
   - گرادیان، Top-hat و Black-hat
3. **تحلیل مؤلفه‌های متصل** - Connected Components Analysis
   - برچسب‌گذاری مؤلفه‌ها (Component Labeling)
   - استخراج ویژگی‌ها (Feature Extraction)
   - شمارش اشیاء (Object Counting)

---

## فایل‌های این فصل / Chapter Files

- `01_thresholding.ipynb` - آستانه‌گذاری سراسری و تطبیقی
- `02_morphological_operations.ipynb` - عملیات مورفولوژیکی
- `03_connected_components.ipynb` - تحلیل مؤلفه‌های متصل

---

## پیش‌نیازها / Prerequisites

- تکمیل فصل ۰ (مقدمات OpenCV)
- تکمیل فصل ۱ (فیلترینگ) - توصیه می‌شود
- تکمیل فصل ۳ (هیستوگرام‌ها) - توصیه می‌شود
- آشنایی با NumPy و Matplotlib
- Python 3.7+

**نصب کتابخانه‌های مورد نیاز:**
```bash
pip install opencv-python numpy matplotlib jupyter
```

یا با uv (سریع‌تر):
```bash
uv pip install opencv-python numpy matplotlib jupyter
```

---

## اهداف یادگیری / Learning Objectives

پس از مطالعه این فصل، شما قادر خواهید بود:

✓ تصاویر خاکستری را به تصاویر دودویی تبدیل کنید  
✓ از روش‌های مختلف آستانه‌گذاری استفاده کنید  
✓ آستانه بهینه را با روش اتسو محاسبه کنید  
✓ آستانه‌گذاری تطبیقی را برای تصاویر با نور نامتجانس اعمال کنید  
✓ عملیات مورفولوژیکی را برای پردازش تصاویر دودویی پیاده‌سازی کنید  
✓ نویز را با عملیات باز و بسته کردن حذف کنید  
✓ مؤلفه‌های متصل را شناسایی و برچسب‌گذاری کنید  
✓ ویژگی‌های اشیاء (مساحت، مرکز جرم، کادر محیطی) را استخراج کنید  
✓ اشیاء را در تصاویر بشمارید

---

## شروع کنید / Get Started

### ⚡ شروع سریع / Quick Start

**گام 1:** اطمینان از نصب کتابخانه‌ها
```bash
pip install opencv-python numpy matplotlib jupyter
```

**گام 2:** باز کردن اولین نوت‌بوک
```bash
jupyter notebook 01_thresholding.ipynb
```

**گام 3:** اجرای سلول‌ها به ترتیب (Shift + Enter)

### 📚 ترتیب مطالعه پیشنهادی / Recommended Study Order

1. ابتدا `01_thresholding.ipynb` را مطالعه کنید
2. سپس `02_morphological_operations.ipynb` را بررسی کنید
3. در نهایت `03_connected_components.ipynb` را اجرا کنید

---

## مفاهیم کلیدی / Key Concepts

### آستانه‌گذاری / Thresholding
تبدیل تصویر خاکستری به تصویر دودویی با استفاده از یک مقدار آستانه. پیکسل‌هایی که مقدارشان بالاتر از آستانه است، سفید (255) و بقیه سیاه (0) می‌شوند.

### عملیات مورفولوژیکی / Morphological Operations
عملیاتی که بر اساس شکل اشیاء در تصویر عمل می‌کنند. برای حذف نویز، پر کردن شکاف‌ها و استخراج مرزها استفاده می‌شوند.

### مؤلفه‌های متصل / Connected Components
مجموعه پیکسل‌های سفید که به هم متصل هستند و یک شیء را تشکیل می‌دهند.

---

## کاربردهای عملی / Practical Applications

- **تشخیص متن (OCR):** جداسازی متن از پس‌زمینه
- **تحلیل تصاویر پزشکی:** شناسایی سلول‌ها و بافت‌ها
- **بینایی ماشین:** تشخیص اشیاء در خط تولید
- **پردازش اسناد:** اسکن و بهبود کیفیت اسناد
- **شمارش اشیاء:** شمارش خودکار اقلام در تصاویر

---

## منابع مورد استفاده / References

1. **کتاب درس / Textbook:**
   - A Practical Introduction to Computer Vision with OpenCV
   - Dawson-Howe K., John Wiley & Sons Ltd.
   - Chapter 4: Binary Vision

2. **مستندات OpenCV / OpenCV Documentation:**
   - https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
   - https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
   - https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html

3. **منابع آنلاین / Online Resources:**
   - PyImageSearch - Thresholding Techniques
   - LearnOpenCV - Morphological Operations

---

## نکات مهم / Important Notes

⚠️ **نکته 1:** آستانه‌گذاری تطبیقی برای تصاویر با نور نامتجانس مناسب‌تر است  
⚠️ **نکته 2:** اندازه عنصر ساختاری (kernel) در عملیات مورفولوژیکی بسیار مهم است  
⚠️ **نکته 3:** ترتیب اعمال عملیات مورفولوژیکی روی نتیجه نهایی تأثیرگذار است  
⚠️ **نکته 4:** قبل از تحلیل مؤلفه‌های متصل، تصویر باید دودویی باشد

---

## ✅ وضعیت تکمیل / Completion Status

- [x] ساختار فصل ایجاد شد
- [x] README نوشته شد
- [ ] نوت‌بوک آستانه‌گذاری
- [ ] نوت‌بوک عملیات مورفولوژیکی
- [ ] نوت‌بوک مؤلفه‌های متصل
- [ ] تست و بررسی نهایی

---

**آخرین به‌روزرسانی / Last Updated:** ۲۸ مهر ۱۴۰۴ (October 19, 2025)
