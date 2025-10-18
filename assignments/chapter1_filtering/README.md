# فصل ۱: فیلترینگ و هموارسازی تصویر
# Chapter 1: Image Filtering and Smoothing

**دانشجو / Student:** مسیح معافی / Masih Moafi  
**تاریخ / Date:** ۲۳ مهر ۱۴۰۴ (October 15, 2025)

---

## محتوای این فصل / Chapter Contents

این فصل شامل مباحث زیر است:

1. **مقدمه‌ای بر نویز در تصاویر** - Introduction to Image Noise
2. **فیلترهای خطی** - Linear Filters
   - میانگین‌گیری محلی (Local Averaging)
   - فیلتر گاوسی (Gaussian Filter)
3. **فیلترهای غیرخطی** - Non-linear Filters
   - فیلتر میانه (Median Filter)
   - فیلتر دوطرفه (Bilateral Filter)
4. **تمرین‌های عملی** - Practical Exercises

---

## فایل‌های این فصل / Chapter Files

- `01_noise_introduction.md` - مقدمه نویز
- `02_linear_filters.ipynb` - فیلترهای خطی (نوت‌بوک تعاملی)
- `03_nonlinear_filters.ipynb` - فیلترهای غیرخطی
- `04_practical_examples.py` - مثال‌های عملی
- `sample_images/` - تصاویر نمونه برای تمرین

---

## پیش‌نیازها / Prerequisites

- نصب OpenCV (مراجعه کنید به `chapter0_opencv_tutorial`)
- آشنایی با مفاهیم پایه تصویر دیجیتال
- Python 3.7+

---

## اهداف یادگیری / Learning Objectives

پس از مطالعه این فصل، شما قادر خواهید بود:

✓ انواع نویز در تصاویر را بشناسید  
✓ فیلترهای مختلف را پیاده‌سازی کنید  
✓ تفاوت فیلترهای خطی و غیرخطی را درک کنید  
✓ فیلتر مناسب را برای هر نوع نویز انتخاب کنید  
✓ کیفیت فیلترینگ را ارزیابی کنید (SNR, PSNR)

---

## شروع کنید / Get Started

برای شروع، فایل `01_noise_introduction.md` را مطالعه کنید، سپس نوت‌بوک‌های تعاملی را اجرا کنید.

```bash
# اجرای نوت‌بوک‌ها
jupyter notebook 02_linear_filters.ipynb
```
