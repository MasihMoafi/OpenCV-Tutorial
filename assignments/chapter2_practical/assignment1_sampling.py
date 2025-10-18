# Assignment 1: Sampling Effects
# Masih Moafi - Computer Vision Course
# Dr. Mohammad Davarpanah Jazi

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('how-many-horses.webp', 0)

if img is None:
    print("Image not found, creating test image")
    # Make a test pattern
    img = np.zeros((200, 200), dtype=np.uint8)
    for i in range(0, 200, 20):
        cv2.line(img, (i, 0), (i, 200), 255, 2)
        cv2.line(img, (0, i), (200, i), 255, 2)

# Different resolutions
original = img.copy()
res_128 = cv2.resize(img, (128, 96))
res_64 = cv2.resize(img, (64, 48)) 
res_32 = cv2.resize(img, (32, 24))

# Display results
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0,0].imshow(original, cmap='gray')
axes[0,0].set_title('Original')
axes[0,1].imshow(res_128, cmap='gray')
axes[0,1].set_title('128x96')
axes[1,0].imshow(res_64, cmap='gray')
axes[1,0].set_title('64x48')
axes[1,1].imshow(res_32, cmap='gray')
axes[1,1].set_title('32x24 - details lost!')

for ax in axes.flat:
    ax.axis('off')

plt.tight_layout()
plt.savefig('sampling_results.png')
plt.show()

print("Done")