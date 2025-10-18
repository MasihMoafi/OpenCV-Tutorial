"""
اولین برنامه با OpenCV
First Program with OpenCV

این فایل شامل ساده‌ترین مثال‌ها برای شروع کار با OpenCV است.

نویسنده: مسیح معافی
تاریخ: ۲۲ مهر ۱۴۰۴ (14 اکتبر 2025)
درس: بینایی کامپیوتر - دکتر محمد داورپناه جزی
"""

import cv2
import numpy as np

print("=" * 50)
print("اولین برنامه با OpenCV")
print("First Program with OpenCV")
print("=" * 50)

# ========================================
# مثال 1: نمایش نسخه OpenCV
# Example 1: Display OpenCV Version
# ========================================

print(f"\nOpenCV Version: {cv2.__version__}")
print(f"NumPy Version: {np.__version__}")


# ========================================
# مثال 2: ایجاد یک تصویر ساده
# Example 2: Create a Simple Image
# ========================================

print("\n[مثال 2] ایجاد تصویر سیاه...")

# ایجاد تصویر سیاه 300x300 پیکسل
# Create a black image 300x300 pixels
black_image = np.zeros((300, 300, 3), dtype=np.uint8)

# ذخیره تصویر
cv2.imwrite('results/black_image.png', black_image)

print("✓ تصویر سیاه ذخیره شد")


# ========================================
# مثال 3: ایجاد تصویر رنگی
# Example 3: Create a Colored Image
# ========================================

print("\n[مثال 3] ایجاد تصویر رنگی...")

# ایجاد تصویر آبی
# BGR format: Blue=255, Green=0, Red=0
blue_image = np.zeros((300, 300, 3), dtype=np.uint8)
blue_image[:, :] = (255, 0, 0)  # BGR: آبی

# ایجاد تصویر سبز
green_image = np.zeros((300, 300, 3), dtype=np.uint8)
green_image[:, :] = (0, 255, 0)  # BGR: سبز

# ایجاد تصویر قرمز
red_image = np.zeros((300, 300, 3), dtype=np.uint8)
red_image[:, :] = (0, 0, 255)  # BGR: قرمز

# ذخیره تصاویر
cv2.imwrite('results/blue_image.png', blue_image)
cv2.imwrite('results/green_image.png', green_image)
cv2.imwrite('results/red_image.png', red_image)

print("✓ تصاویر رنگی ذخیره شدند")


# ========================================
# مثال 4: رسم اشکال ساده
# Example 4: Draw Simple Shapes
# ========================================

print("\n[مثال 4] رسم اشکال...")

# ایجاد تصویر سفید
canvas = np.ones((400, 400, 3), dtype=np.uint8) * 255

# رسم مستطیل
cv2.rectangle(canvas, (50, 50), (150, 150), (0, 255, 0), 3)

# رسم دایره
cv2.circle(canvas, (300, 100), 50, (255, 0, 0), -1)  # -1 = پر شده

# رسم خط
cv2.line(canvas, (50, 250), (350, 250), (0, 0, 255), 2)

# نوشتن متن
cv2.putText(canvas, 'OpenCV', (150, 350), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imwrite('results/shapes_canvas.png', canvas)

print("✓ اشکال رسم و ذخیره شدند")


# ========================================
# مثال 5: ذخیره تصویر
# Example 5: Save Image
# ========================================

print("\n[مثال 5] ذخیره تصویر...")

# ذخیره تصویر
cv2.imwrite('results/my_first_opencv_image.png', canvas)

print("✓ تصویر ذخیره شد: results/my_first_opencv_image.png")


# ========================================
# مثال 6: خواندن و نمایش تصویر ذخیره شده
# Example 6: Read and Display Saved Image
# ========================================

print("\n[مثال 6] خواندن تصویر...")

# خواندن تصویر
loaded_image = cv2.imread('results/my_first_opencv_image.png')

if loaded_image is not None:
    print(f"✓ تصویر خوانده شد")
    print(f"  - ابعاد: {loaded_image.shape}")
    print(f"  - نوع داده: {loaded_image.dtype}")
else:
    print("✗ خطا در خواندن تصویر")


# ========================================
# خلاصه
# Summary
# ========================================

print("\n" + "=" * 50)
print("خلاصه مفاهیم آموخته شده:")
print("=" * 50)
print("1. نمایش نسخه OpenCV")
print("2. ایجاد تصویر با NumPy")
print("3. کار با رنگ‌ها (BGR format)")
print("4. رسم اشکال (مستطیل، دایره، خط، متن)")
print("5. ذخیره تصویر با cv2.imwrite()")
print("6. خواندن تصویر با cv2.imread()")
print("=" * 50)

print("\n✓ برنامه با موفقیت اجرا شد!")
print("\nبرای ادامه، فایل بعدی را اجرا کنید:")
print("  python 03_reading_images.py")
