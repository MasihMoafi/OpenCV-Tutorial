# فصل ۵: تبدیلات هندسی
# Chapter 5: Geometric Transformations

**دانشجو / Student:** مسیح معافی / Masih Moafi  
**تاریخ / Date:** ۲۸ مهر ۱۴۰۴ (October 19, 2025)

---

## محتوای این فصل / Chapter Contents

این فصل شامل مباحث زیر است:

1. **تبدیلات آفین** - Affine Transformations
   - انتقال (Translation)
   - چرخش (Rotation)
   - مقیاس‌بندی (Scaling)
   - برش (Shearing)
   - ترکیب تبدیلات (Combining Transformations)
2. **تبدیلات پرسپکتیو** - Perspective Transformations
   - محاسبه ماتریس تبدیل (Computing Transformation Matrix)
   - اصلاح پرسپکتیو (Perspective Correction)
   - اسکن اسناد (Document Scanning)
   - نمای پرنده (Bird's Eye View)
3. **ثبت تصویر** - Image Registration
   - تراز کردن تصاویر (Image Alignment)
   - تطبیق الگو (Template Matching)
   - همبستگی فاز (Phase Correlation)
   - دوخت تصاویر (Image Stitching)

---

## فایل‌های این فصل / Chapter Files

- `01_affine_transformations.ipynb` - تبدیلات آفین (انتقال، چرخش، مقیاس‌بندی، برش)
- `02_perspective_transform.ipynb` - تبدیلات پرسپکتیو و اصلاح دیدگاه
- `03_image_registration.ipynb` - تراز کردن و دوخت تصاویر

---

## پیش‌نیازها / Prerequisites

- تکمیل فصل ۰ (مقدمات OpenCV)
- آشنایی با NumPy و Matplotlib
- درک مفاهیم پایه جبر خطی (ماتریس‌ها و تبدیلات)
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

✓ تصاویر را با استفاده از تبدیلات آفین جابجا، چرخش و مقیاس‌بندی کنید  
✓ ماتریس‌های تبدیل را برای عملیات مختلف محاسبه کنید  
✓ چندین تبدیل را با هم ترکیب کنید  
✓ تبدیلات پرسپکتیو را برای اصلاح دیدگاه اعمال کنید  
✓ اسناد را به صورت خودکار اسکن و اصلاح کنید  
✓ نمای پرنده (bird's eye view) از تصاویر ایجاد کنید  
✓ تصاویر را با استفاده از روش‌های مختلف تراز کنید  
✓ تطبیق الگو را برای یافتن اشیاء در تصاویر پیاده‌سازی کنید  
✓ چندین تصویر را برای ایجاد پانوراما به هم بدوزید

---

## شروع کنید / Get Started

### ⚡ شروع سریع / Quick Start

**گام 1:** اطمینان از نصب کتابخانه‌ها
```bash
pip install opencv-python numpy matplotlib jupyter
```

**گام 2:** باز کردن اولین نوت‌بوک
```bash
jupyter notebook 01_affine_transformations.ipynb
```

**گام 3:** اجرای سلول‌ها به ترتیب (Shift + Enter)

### 📚 ترتیب مطالعه پیشنهادی / Recommended Study Order

1. ابتدا `01_affine_transformations.ipynb` را مطالعه کنید
2. سپس `02_perspective_transform.ipynb` را بررسی کنید
3. در نهایت `03_image_registration.ipynb` را اجرا کنید

---

## مفاهیم کلیدی / Key Concepts

### تبدیلات آفین / Affine Transformations
تبدیلاتی که خطوط موازی را حفظ می‌کنند. شامل انتقال، چرخش، مقیاس‌بندی و برش می‌شوند. با ماتریس 2×3 نمایش داده می‌شوند.

### تبدیلات پرسپکتیو / Perspective Transformations
تبدیلات کلی‌تر که می‌توانند خطوط موازی را به خطوط همگرا تبدیل کنند. برای اصلاح دیدگاه دوربین استفاده می‌شوند. با ماتریس 3×3 نمایش داده می‌شوند.

### ثبت تصویر / Image Registration
فرآیند تراز کردن دو یا چند تصویر از یک صحنه. برای دوخت تصاویر، ردیابی حرکت و تحلیل تغییرات استفاده می‌شود.

---

## کاربردهای عملی / Practical Applications

- **افزایش داده (Data Augmentation):** تولید داده‌های آموزشی بیشتر برای یادگیری ماشین
- **اسکن اسناد:** اصلاح خودکار تصاویر اسناد گرفته شده با موبایل
- **واقعیت افزوده (AR):** قرار دادن اشیاء مجازی در دنیای واقعی
- **پانوراما:** ایجاد تصاویر پانورامای گسترده از چندین عکس
- **تحلیل تصاویر پزشکی:** تراز کردن تصاویر از روش‌های مختلف تصویربرداری
- **ردیابی حرکت:** دنبال کردن اشیاء در ویدیو
- **نقشه‌برداری:** تصحیح هندسی تصاویر هوایی و ماهواره‌ای

---

## منابع مورد استفاده / References

1. **کتاب درس / Textbook:**
   - A Practical Introduction to Computer Vision with OpenCV
   - Dawson-Howe K., John Wiley & Sons Ltd.
   - Chapter 5: Geometric Transformations

2. **مستندات OpenCV / OpenCV Documentation:**
   - https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html
   - https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html
   - https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

3. **منابع آنلاین / Online Resources:**
   - PyImageSearch - Image Transformations
   - LearnOpenCV - Geometric Transformations

---

## نکات مهم / Important Notes

⚠️ **نکته 1:** تبدیلات آفین خطوط موازی را حفظ می‌کنند، اما تبدیلات پرسپکتیو این کار را نمی‌کنند  
⚠️ **نکته 2:** ترتیب اعمال تبدیلات مهم است - چرخش و سپس انتقال با انتقال و سپس چرخش متفاوت است  
⚠️ **نکته 3:** برای تبدیلات پرسپکتیو، حداقل 4 نقطه مطابق نیاز است  
⚠️ **نکته 4:** روش‌های درون‌یابی (interpolation) بر کیفیت تصویر نهایی تأثیر می‌گذارند  
⚠️ **نکته 5:** هنگام ترکیب تبدیلات، ضرب ماتریس‌ها از راست به چپ انجام می‌شود

---

## ✅ وضعیت تکمیل / Completion Status

- [x] ساختار فصل ایجاد شد
- [x] README نوشته شد
- [ ] نوت‌بوک تبدیلات آفین
- [ ] نوت‌بوک تبدیلات پرسپکتیو
- [ ] نوت‌بوک ثبت تصویر
- [ ] تست و بررسی نهایی

---

**آخرین به‌روزرسانی / Last Updated:** ۲۸ مهر ۱۴۰۴ (October 19, 2025)
