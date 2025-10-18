# Assignment 2: Quantization
# Masih Moafi - Computer Vision Course  
# Dr. Mohammad Davarpanah Jazi

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create gradient image to show quantization effects clearly
img = np.zeros((150, 300), dtype=np.uint8)
for i in range(300):
    img[:, i] = int(255 * i / 299)

print(f"Original image range: {img.min()} to {img.max()}")

# Apply different bit depths as shown in slides
img_8bit = img.copy()  # 256 levels (2^8)
img_6bit = (img >> 2) << 2  # 64 levels (2^6)
img_4bit = (img >> 4) << 4  # 16 levels (2^4)  
img_2bit = (img >> 6) << 6  # 4 levels (2^2)

print(f"6-bit range: {img_6bit.min()} to {img_6bit.max()}")
print(f"4-bit range: {img_4bit.min()} to {img_4bit.max()}")
print(f"2-bit range: {img_2bit.min()} to {img_2bit.max()}")

# Show the banding effect
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img_8bit, cmap='gray')
plt.title('8-bit (256 levels)')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(img_6bit, cmap='gray')
plt.title('6-bit (64 levels)')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(img_4bit, cmap='gray')
plt.title('4-bit (16 levels)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(img_2bit, cmap='gray')
plt.title('2-bit (4 levels) - severe banding!')
plt.axis('off')

plt.suptitle('Quantization Effects - Bit Depth Reduction')
plt.tight_layout()
plt.savefig('quantization_results.png')
plt.show()

# Also test on real image
real_img = cv2.imread('how-many-horses.webp', 0)
if real_img is not None:
    real_4bit = (real_img >> 4) << 4
    
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(real_img, cmap='gray')
    plt.title('Original 8-bit')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(real_4bit, cmap='gray')
    plt.title('Reduced to 4-bit')
    plt.axis('off')
    
    plt.savefig('real_quantization.png')
    plt.show()

print("Finished")