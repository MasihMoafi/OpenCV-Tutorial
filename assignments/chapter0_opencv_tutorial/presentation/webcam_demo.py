#!/usr/bin/env python3
"""
نمایش ویدیو از وب‌کم - OpenCV Demo
Webcam Video Display - OpenCV Demo

برای خروج از برنامه:
- کلید 'q' را فشار دهید
- یا کلید 'ESC' را فشار دهید
"""

import cv2
import sys

def main():
    print("Starting webcam...")
    print("Press 'q' or 'ESC' to exit")
    print("شروع وب‌کم...")
    print("برای خروج 'q' یا 'ESC' را فشار دهید")
    
    # باز کردن وب‌کم (0 برای وب‌کم پیش‌فرض)
    cap = cv2.VideoCapture(0)
    
    # بررسی اینکه وب‌کم باز شده است
    if not cap.isOpened():
        print("Error: Cannot open webcam")
        print("خطا: وب‌کم باز نمی‌شود")
        return
    
    try:
        while True:
            # خواندن فریم
            ret, frame = cap.read()
            
            # اگر فریم خوانده نشد
            if not ret:
                print("Error: Cannot read frame")
                break
            
            # اضافه کردن متن راهنما روی فریم
            cv2.putText(frame, "Press 'q' or 'ESC' to exit", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.7, (0, 255, 0), 2)
            
            # نمایش فریم
            cv2.imshow('Webcam - Press q or ESC to exit', frame)
            
            # بررسی کلیدهای فشرده شده
            key = cv2.waitKey(1) & 0xFF
            
            # اگر کلید 'q' یا 'ESC' فشرده شد، خروج
            if key == ord('q') or key == 27:  # 27 = ESC
                print("Exiting...")
                break
                
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    
    finally:
        # آزاد کردن منابع
        cap.release()
        cv2.destroyAllWindows()
        
        # اطمینان از بسته شدن پنجره‌ها
        for i in range(5):
            cv2.waitKey(1)
        
        print("Webcam closed successfully")
        print("وب‌کم با موفقیت بسته شد")

if __name__ == "__main__":
    main()
