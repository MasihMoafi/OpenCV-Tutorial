# Assignment 3: Color Space Conversions
# Masih Moafi - Computer Vision Course
# Dr. Mohammad Davarpanah Jazi

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load color image
img_bgr = cv2.imread('how-many-horses.webp', cv2.IMREAD_COLOR)

if img_bgr is None:
    print("Creating synthetic color image for testing")
    img_bgr = np.zeros((200, 300, 3), dtype=np.uint8)
    # Add some colored rectangles
    img_bgr[50:100, 50:100] = [255, 0, 0]    # Blue in BGR
    img_bgr[50:100, 150:200] = [0, 255, 0]   # Green
    img_bgr[100:150, 50:100] = [0, 0, 255]   # Red
    img_bgr[100:150, 150:200] = [255, 255, 0] # Cyan

print(f"Image shape: {img_bgr.shape}")

# Convert to different color spaces as per slides

# 1. RGB (slide 19) - need to convert BGR to RGB for display
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 2. Grayscale conversion (slide 19)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 3. CMY (slides 23-24) - simple inversion
img_cmy = 255 - img_bgr

# 4. YUV (slides 25-26)
img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

# 5. HLS (slides 27-30)
img_hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)

# Display all conversions
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(img_rgb)
plt.title('Original RGB')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(img_cmy, cv2.COLOR_BGR2RGB))
plt.title('CMY (Inverted)')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(img_yuv)
plt.title('YUV')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(img_hls)
plt.title('HLS')
plt.axis('off')

# Show HLS channels separately (slide 28-30)
h, l, s = cv2.split(img_hls)
plt.subplot(2, 3, 6)
plt.imshow(h, cmap='hsv')
plt.title('HLS - Hue Channel')
plt.axis('off')

plt.suptitle('Color Space Conversions')
plt.tight_layout()
plt.savefig('colorspace_results.png')
plt.show()

# Also show RGB channels separately (slides 16-22)
b, g, r = cv2.split(img_bgr)

plt.figure(figsize=(12, 4))
plt.subplot(1, 4, 1)
plt.imshow(img_rgb)
plt.title('Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(r, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(g, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(b, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.savefig('rgb_channels.png')
plt.show()

print("Done with color spaces")