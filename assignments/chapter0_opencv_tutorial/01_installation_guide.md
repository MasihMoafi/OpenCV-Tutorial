# راهنمای نصب OpenCV

## مقدمه

OpenCV (Open Source Computer Vision Library) یک کتابخانه متن‌باز برای پردازش تصویر و بینایی کامپیوتر است که توسط Intel توسعه یافته و در حال حاضر توسط جامعه بزرگی از توسعه‌دهندگان پشتیبانی می‌شود.

---

## پیش‌نیازها

قبل از نصب OpenCV، نیاز به موارد زیر دارید:

1. **Python 3.7 یا بالاتر**
2. **pip** (مدیر بسته Python)
3. **NumPy** (به‌صورت خودکار نصب می‌شود)

---

## روش‌های نصب

OpenCV را می‌توان با روش‌های مختلفی نصب کرد. بسته به سیستم‌عامل و مدیر بسته‌ای که استفاده می‌کنید، یکی از روش‌های زیر را انتخاب کنید:

### روش اول: نصب با pip (توصیه می‌شود)

ساده‌ترین و رایج‌ترین روش:

```bash
pip install opencv-python
```

برای نسخه کامل با ماژول‌های اضافی:

```bash
pip install opencv-contrib-python
```

### روش دوم: نصب با uv (سریع‌تر)

uv یک مدیر بسته سریع برای Python است:

```bash
# نصب uv (اگر ندارید)
curl -LsSf https://astral.sh/uv/install.sh | sh

# نصب OpenCV
uv pip install opencv-python
```

### روش سوم: نصب با Anaconda/Conda

برای کاربران Anaconda:

ابتدا anaconda را از سایت anaconda.org دانلود و نصب کنید. 

```bash
conda install -c conda-forge opencv
```

یا:

```bash
conda install opencv
```

### روش چهارم: نصب در محیط مجازی (Virtual Environment)

برای جلوگیری از تداخل با بسته‌های دیگر، استفاده از محیط مجازی توصیه می‌شود:

```bash
# ایجاد محیط مجازی
python -m venv opencv_env

# فعال‌سازی محیط مجازی
# در Windows:
opencv_env\Scripts\activate
# در Linux/Mac:
source opencv_env/bin/activate

# نصب OpenCV
pip install opencv-python numpy matplotlib
```

---

## تست نصب

برای اطمینان از نصب صحیح، کد زیر را اجرا کنید:

```python
import cv2
import numpy as np

print(f"OpenCV version: {cv2.__version__}")
print(f"NumPy version: {np.__version__}")

# تست ساده
img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.imshow('Test', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("✓ OpenCV installed successfully!")
```

اگر خطایی دریافت نکردید، نصب موفقیت‌آمیز بوده است.

---

## نصب کتابخانه‌های کمکی

برای کار راحت‌تر با OpenCV، نصب کتابخانه‌های زیر توصیه می‌شود:

```bash
pip install numpy matplotlib pillow jupyter
```

**توضیح:**
- `numpy`: محاسبات عددی و کار با آرایه‌ها
- `matplotlib`: نمایش تصاویر و نمودارها
- `pillow`: کار با فرمت‌های مختلف تصویر
- `jupyter`: محیط تعاملی برای کدنویسی

---

## مشکلات رایج و راه‌حل

### مشکل 1: خطای "No module named 'cv2'"

**راه‌حل:**
```bash
pip uninstall opencv-python
pip install opencv-python
```

### مشکل 2: تصویر نمایش داده نمی‌شود

**راه‌حل:**
- مطمئن شوید `cv2.waitKey()` را فراخوانی کرده‌اید
- در محیط‌های بدون GUI از `matplotlib` استفاده کنید

### مشکل 3: خطای import در Jupyter Notebook

**راه‌حل:**
```bash
# نصب در همان محیط Jupyter
!pip install opencv-python
```

---

## بررسی قابلیت‌های نصب شده

برای دیدن ماژول‌های موجود:

```python
import cv2
print(cv2.getBuildInformation())
```

---

## دوره‌های رایگان OpenCV

OpenCV دوره‌های رایگان و ساختاریافته‌ای ارائه می‌دهد:

- **لینک:** https://courses.opencv.org/courses/
- **محتوا:** 
  - Introduction to Computer Vision
  - Deep Learning with PyTorch
  - Object Detection
  - Image Processing
- **مزایا:** ساختاریافته، با ویدیو، با تمرین
- **هزینه:** رایگان

## منابع بیشتر

- **مستندات رسمی:** https://docs.opencv.org/
- **دوره‌های رایگان:** https://courses.opencv.org/courses/
- **راهنمای نصب:** https://pypi.org/project/opencv-python/
- **GitHub:** https://github.com/opencv/opencv-python

---

## نکات مهم

1. **نسخه‌ها:**
   - `opencv-python`: نسخه اصلی (توصیه می‌شود)
   - `opencv-contrib-python`: شامل ماژول‌های اضافی
   - `opencv-python-headless`: بدون GUI (برای سرورها)

2. **سازگاری:**
   - OpenCV 4.x با Python 3.7+ سازگار است
   - برای پروژه‌های قدیمی‌تر، OpenCV 3.x را نصب کنید

3. **حجم:**
   - نسخه اصلی: ~90 MB
   - نسخه contrib: ~200 MB

---

**نصب موفقیت‌آمیز بود؟ به بخش بعدی بروید: `02_first_program.py`**
