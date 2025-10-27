# فصل ۶: تشخیص لبه و کانتور
# Chapter 6: Edge Detection and Contours

**دانشجو / Student:** مسیح معافی / Masih Moafi  
**تاریخ / Date:** ۱۴۰۳/۰۷/۲۸ (October 19, 2025)

---

## درباره این فصل / About This Chapter

این فصل به یکی از مهم‌ترین موضوعات بینایی ماشین می‌پردازد: تشخیص لبه‌ها و کانتورها. لبه‌ها نشان‌دهنده تغییرات ناگهانی در شدت روشنایی تصویر هستند و اطلاعات مهمی درباره ساختار و شکل اشیاء ارائه می‌دهند.

This chapter covers one of the most important topics in computer vision: edge detection and contours. Edges represent sudden changes in image intensity and provide crucial information about object structure and shape.

---

## محتوای این فصل / Chapter Contents

### ۱. عملگرهای گرادیان / Gradient Operators
- عملگر سوبل (Sobel) برای محاسبه گرادیان در جهت x و y
- عملگر شار (Scharr) برای دقت بهتر
- عملگر لاپلاسین (Laplacian) برای مشتق مرتبه دوم
- لاپلاسین گاوسی (LoG) برای تشخیص لبه مقاوم به نویز
- تحلیل قدرت و جهت لبه‌ها

### 2. Gradient Operators
- Sobel operator for x and y gradient calculation
- Scharr operator for improved accuracy
- Laplacian operator for second derivative
- Laplacian of Gaussian (LoG) for noise-robust edge detection
- Edge strength and direction analysis

### ۲. تشخیص لبه کنی / Canny Edge Detection
- الگوریتم کنی و مراحل آن
- تأثیر آستانه‌های مختلف
- مراحل میانی: محو گاوسی، محاسبه گرادیان، سرکوب غیرماکزیمم، هیسترزیس
- تنظیم پارامترها
- مقایسه با روش‌های دیگر

### 3. Canny Edge Detection
- Canny algorithm and its steps
- Effect of different threshold values
- Intermediate steps: Gaussian blur, gradient calculation, non-maximum suppression, hysteresis
- Parameter tuning
- Comparison with other methods

### ۳. تشخیص و تحلیل کانتور / Contour Detection and Analysis
- یافتن کانتورها با cv2.findContours()
- حالت‌های مختلف بازیابی کانتور
- رسم کانتورها
- محاسبه ویژگی‌های کانتور: مساحت، محیط، مرکز جرم، مستطیل محیطی
- تقریب کانتور با cv2.approxPolyDP()
- محاسبه پوسته محدب (Convex Hull)
- تطبیق و تشخیص شکل
- تحلیل سلسله‌مراتب کانتورهای تو در تو

### 4. Contour Detection and Analysis
- Finding contours with cv2.findContours()
- Different retrieval modes
- Drawing contours
- Calculating contour properties: area, perimeter, centroid, bounding box
- Contour approximation with cv2.approxPolyDP()
- Convex hull calculation
- Shape matching and recognition
- Hierarchy analysis for nested contours

### ۴. تبدیل هاف / Hough Transform
- تشخیص خط با cv2.HoughLines()
- تبدیل هاف احتمالاتی با cv2.HoughLinesP()
- تشخیص دایره با cv2.HoughCircles()
- تنظیم پارامترها و تأثیر آن‌ها
- کاربردهای عملی: تشخیص خط خطوط جاده، شمارش سکه

### 5. Hough Transform
- Line detection with cv2.HoughLines()
- Probabilistic Hough line transform with cv2.HoughLinesP()
- Circle detection with cv2.HoughCircles()
- Parameter tuning and effects
- Practical applications: lane detection, coin counting

---

## فایل‌های این فصل / Chapter Files

### 📓 01_gradient_operators.ipynb
عملگرهای گرادیان شامل سوبل، شار، و لاپلاسین. این نوت‌بوک نحوه محاسبه گرادیان‌های تصویر و استفاده از آن‌ها برای تشخیص لبه را نشان می‌دهد.

Gradient operators including Sobel, Scharr, and Laplacian. This notebook demonstrates how to calculate image gradients and use them for edge detection.

### 📓 02_canny_edge_detection.ipynb
الگوریتم تشخیص لبه کنی که یکی از محبوب‌ترین و دقیق‌ترین روش‌های تشخیص لبه است. شامل تنظیم پارامترها و مقایسه با روش‌های دیگر.

Canny edge detection algorithm, one of the most popular and accurate edge detection methods. Includes parameter tuning and comparison with other methods.

### 📓 03_contours.ipynb
یافتن و تحلیل کانتورها در تصاویر باینری. شامل محاسبه ویژگی‌های کانتور، تقریب شکل، و کاربردهای عملی.

Finding and analyzing contours in binary images. Includes contour property calculation, shape approximation, and practical applications.

### 📓 04_hough_transform.ipynb
تبدیل هاف برای تشخیص اشکال هندسی مانند خطوط و دایره‌ها. شامل کاربردهای عملی مانند تشخیص خطوط جاده.

Hough transform for detecting geometric shapes like lines and circles. Includes practical applications like lane detection.

---

## پیش‌نیازها / Prerequisites

### دانش لازم / Required Knowledge
- ✅ **فصل ۰**: مبانی OpenCV، خواندن و نمایش تصویر، فضاهای رنگی
- ✅ **فصل ۱**: فیلترهای خطی و غیرخطی، محو گاوسی، فیلتر میانه
- ✅ **فصل ۳**: هیستوگرام و یکنواخت‌سازی (برای پیش‌پردازش)
- ✅ **فصل ۴**: آستانه‌گذاری و عملیات مورفولوژیکی (برای کار با کانتورها)

### Required Knowledge
- ✅ **Chapter 0**: OpenCV basics, reading and displaying images, color spaces
- ✅ **Chapter 1**: Linear and nonlinear filters, Gaussian blur, median filter
- ✅ **Chapter 3**: Histograms and equalization (for preprocessing)
- ✅ **Chapter 4**: Thresholding and morphological operations (for working with contours)

### نصب کتابخانه‌ها / Library Installation
```bash
pip install opencv-python numpy matplotlib jupyter
```

---

## اهداف یادگیری / Learning Objectives

پس از مطالعه این فصل، شما قادر خواهید بود:

After completing this chapter, you will be able to:

- [ ] محاسبه گرادیان تصویر با استفاده از عملگرهای سوبل و شار / Calculate image gradients using Sobel and Scharr operators
- [ ] استفاده از عملگر لاپلاسین برای تشخیص لبه / Use Laplacian operator for edge detection
- [ ] پیاده‌سازی الگوریتم تشخیص لبه کنی / Implement Canny edge detection algorithm
- [ ] تنظیم پارامترهای کنی برای نتایج بهینه / Tune Canny parameters for optimal results
- [ ] یافتن و رسم کانتورها در تصاویر / Find and draw contours in images
- [ ] محاسبه ویژگی‌های کانتور مانند مساحت و محیط / Calculate contour properties like area and perimeter
- [ ] تقریب شکل کانتورها / Approximate contour shapes
- [ ] استفاده از تبدیل هاف برای تشخیص خطوط و دایره‌ها / Use Hough transform to detect lines and circles
- [ ] پیاده‌سازی کاربردهای عملی مانند تشخیص خطوط جاده / Implement practical applications like lane detection
- [ ] مقایسه روش‌های مختلف تشخیص لبه / Compare different edge detection methods

---

## مفاهیم کلیدی / Key Concepts

### لبه چیست؟ / What is an Edge?
لبه نقطه‌ای در تصویر است که در آن تغییر ناگهانی در شدت روشنایی رخ می‌دهد. لبه‌ها معمولاً مرز بین اشیاء یا تغییر در بافت را نشان می‌دهند.

An edge is a point in an image where there is a sudden change in intensity. Edges typically represent boundaries between objects or changes in texture.

### گرادیان تصویر / Image Gradient
گرادیان نشان‌دهنده نرخ تغییر شدت روشنایی در تصویر است. بردار گرادیان دارای دو مؤلفه است: قدرت (magnitude) و جهت (direction).

The gradient represents the rate of change of intensity in an image. The gradient vector has two components: magnitude and direction.

### کانتور / Contour
کانتور یک منحنی است که تمام نقاط پیوسته با شدت روشنایی یکسان را به هم متصل می‌کند. کانتورها برای تشخیص شکل و تحلیل اشیاء مفید هستند.

A contour is a curve joining all continuous points with the same intensity. Contours are useful for shape detection and object analysis.

---

## شروع کنید / Get Started

### راه‌اندازی سریع / Quick Start
```bash
# نصب وابستگی‌ها / Install dependencies
pip install opencv-python numpy matplotlib jupyter

# اجرای Jupyter Notebook / Run Jupyter Notebook
jupyter notebook

# باز کردن اولین نوت‌بوک / Open the first notebook
# 01_gradient_operators.ipynb
```

### ساختار یادگیری پیشنهادی / Recommended Learning Path
1. ابتدا نوت‌بوک عملگرهای گرادیان را مطالعه کنید
2. سپس به الگوریتم کنی بپردازید
3. کانتورها را یاد بگیرید
4. در نهایت تبدیل هاف را بررسی کنید

1. Start with the gradient operators notebook
2. Then study the Canny algorithm
3. Learn about contours
4. Finally explore the Hough transform

---

## منابع اضافی / Additional Resources

### کتاب‌ها / Books
- Dawson-Howe K., "A Practical Introduction to Computer Vision with OpenCV" - Chapter 6

### مستندات / Documentation
- [OpenCV Edge Detection Tutorial](https://docs.opencv.org/master/da/d22/tutorial_py_canny.html)
- [OpenCV Contours Tutorial](https://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html)
- [OpenCV Hough Transform Tutorial](https://docs.opencv.org/master/d9/db0/tutorial_hough_lines.html)

---

## نکات مهم / Important Notes

⚠️ **نکته ۱**: قبل از تشخیص لبه، معمولاً نیاز به پیش‌پردازش تصویر (مانند محو گاوسی) برای کاهش نویز است.

⚠️ **Note 1**: Before edge detection, preprocessing (like Gaussian blur) is usually needed to reduce noise.

⚠️ **نکته ۲**: انتخاب آستانه‌های مناسب در الگوریتم کنی بسیار مهم است و بستگی به تصویر دارد.

⚠️ **Note 2**: Choosing appropriate thresholds in Canny algorithm is crucial and depends on the image.

⚠️ **نکته ۳**: برای یافتن کانتور، تصویر باید باینری (سیاه و سفید) باشد.

⚠️ **Note 3**: For contour detection, the image must be binary (black and white).

---

**موفق باشید! / Good luck with your learning!** 🚀
