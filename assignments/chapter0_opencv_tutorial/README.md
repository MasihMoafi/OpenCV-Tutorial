# تکلیف فصل صفرم - آموزش OpenCV
## یادگیری محیط برنامه‌نویسی OpenCV

**دانشجو:** مسیح معافی  
**استاد:** دکتر محمد داورپناه جزی  
**درس:** بینایی کامپیوتر  
**ترم:** اول 1404-1405

---

## 📋 شرح تکلیف

یادگیری محیط برنامه‌نویسی OpenCV با توجه به بیان مثال‌های مرتبط با هر یک از موضوعات درس بر مبنای امکانات این محیط و همچنین لزوم انجام تعدادی از تکالیف درس به‌صورت پیاده‌سازی در این محیط.

این کار به‌عنوان یک کار اضافی برای درس در نظر گرفته می‌شود.

### 🎓 دوره‌های رایگان OpenCV

OpenCV دوره‌های رایگان متعددی در وب‌سایت رسمی خود ارائه می‌دهد:
- **لینک:** https://courses.opencv.org/courses/
- **محتوا:** دوره‌های ساختاریافته از مبتدی تا پیشرفته
- **زبان:** انگلیسی
- **هزینه:** رایگان

### 📦 روش‌های نصب

بسته به سیستم‌عامل و مدیر بسته، روش‌های مختلفی برای نصب OpenCV وجود دارد:

**با pip (توصیه می‌شود):**
```bash
pip install opencv-python
```

**با uv (سریع‌تر):**
```bash
uv pip install opencv-python
```

**با Anaconda:**
```bash
conda install -c conda-forge opencv
```

جزئیات بیشتر در `01_installation_guide.md`

---

## 📚 محتویات

### 🎓 دفترچه‌های آموزشی اصلی (Main Tutorials)
**برای یادگیری OpenCV، این دو فایل را به ترتیب مطالعه کنید:**

1. **`01_basic_opencv.ipynb`** - مفاهیم پایه OpenCV
   - نصب و راه‌اندازی
   - خواندن و نمایش تصاویر
   - عملیات پایه روی تصاویر
   - رسم اشکال و متن

2. **`02_filters.ipynb`** - فیلترها و پردازش تصویر
   - فیلترهای خطی (Linear Filters)
   - فیلترهای غیرخطی (Non-linear Filters)
   - تشخیص لبه (Edge Detection)
   - هموارسازی (Smoothing)

### 📖 مستندات و راهنماها
- `01_installation_guide.md` - راهنمای نصب کامل
- `02_first_program.py` - کد نمونه Python
- `resources.md` - منابع یادگیری و دوره‌های رایگان
- `CHAPTER0_SUMMARY.md` - خلاصه فصل
- `presentation/` - فایل‌های کمکی و پشتیبان
- `results/` - تصاویر خروجی

---

## 🎯 اهداف یادگیری

پس از مطالعه این مطالب، دانشجو قادر خواهد بود:

1. نصب و راه‌اندازی OpenCV در Python
2. خواندن، نمایش و ذخیره تصاویر
3. تبدیل بین فضاهای رنگی مختلف
4. اعمال فیلترها و عملیات پردازش تصویر
5. پیاده‌سازی الگوریتم‌های ساده بینایی کامپیوتر

---

## 🚀 نحوه استفاده

### ⚡ شروع سریع

**گام 1:** نصب OpenCV
```bash
pip install opencv-python numpy matplotlib jupyter
```

**گام 2:** باز کردن دفترچه‌های آموزشی
```bash
jupyter notebook 01_basic_opencv.ipynb
```

**گام 3:** اجرای سلول‌ها به ترتیب (Shift + Enter)

### روش‌های دیگر

**اجرای کد Python:**
```bash
python 02_first_program.py
```

**مشاهده نتایج:**
- پوشه `results/` - تصاویر خروجی
- پوشه `presentation/` - فایل‌های کمکی

---

## 📖 منابع مورد استفاده

1. **OpenCV Official Documentation**
   - https://docs.opencv.org/4.x/

2. **OpenCV Python Tutorials**
   - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

3. **کتاب درس:**
   - A Practical Introduction to Computer Vision with OpenCV
   - Dawson-Howe K., John Wiley & Sons Ltd.

4. **منابع آنلاین:**
   - Real Python OpenCV Tutorial
   - PyImageSearch Blog
   - LearnOpenCV.com

---

## ✅ وضعیت تکمیل

- [x] نصب و راه‌اندازی
- [x] مفاهیم پایه
- [x] پردازش تصویر
- [x] مثال‌های کاربردی
- [x] مستندسازی

---

**تاریخ تکمیل:** ۲۲ مهر ۱۴۰۴ (14 اکتبر 2025)
