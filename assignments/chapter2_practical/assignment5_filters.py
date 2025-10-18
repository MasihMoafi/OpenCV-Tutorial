# Assignment 5: Smoothing Filters
# Masih Moafi - Computer Vision Course
# Dr. Mohammad Davarpanah Jazi

import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_snr(original, processed):
    signal = np.sum(original.astype(float) ** 2)
    noise = np.sum((original.astype(float) - processed.astype(float)) ** 2)
    if noise == 0:
        return float('inf')
    return 10 * np.log10(signal / noise)

# Load image
img = cv2.imread('how-many-horses.webp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Creating test image with clear features")
    img = np.zeros((200, 200), dtype=np.uint8)
    cv2.rectangle(img, (50, 50), (150, 150), 200, -1)
    cv2.circle(img, (100, 100), 30, 100, -1)
    cv2.line(img, (0, 100), (200, 100), 255, 3)

# Add Gaussian noise to test filters
np.random.seed(42)  # For reproducible results
noise = np.random.normal(0, 20, img.shape).astype(np.int16)
noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

print(f"Original SNR: {calculate_snr(img, noisy_img):.2f} dB")

# Apply different smoothing filters (slides 51-53)

# 1. Local Average Filter (slide 51-52)
avg_3x3 = cv2.blur(noisy_img, (3, 3))
avg_5x5 = cv2.blur(noisy_img, (5, 5))

# 2. Gaussian Smoothing (slide 52)
gauss_small = cv2.GaussianBlur(noisy_img, (5, 5), 1.0)
gauss_large = cv2.GaussianBlur(noisy_img, (5, 5), 2.0)

# 3. Median Filter (good for salt & pepper)
median_3 = cv2.medianBlur(noisy_img, 3)
median_5 = cv2.medianBlur(noisy_img, 5)

# Calculate SNR improvements
snr_avg3 = calculate_snr(img, avg_3x3)
snr_avg5 = calculate_snr(img, avg_5x5)
snr_gauss1 = calculate_snr(img, gauss_small)
snr_gauss2 = calculate_snr(img, gauss_large)
snr_med3 = calculate_snr(img, median_3)
snr_med5 = calculate_snr(img, median_5)

print(f"Average 3x3 SNR: {snr_avg3:.2f} dB")
print(f"Average 5x5 SNR: {snr_avg5:.2f} dB")
print(f"Gaussian σ=1.0 SNR: {snr_gauss1:.2f} dB")
print(f"Gaussian σ=2.0 SNR: {snr_gauss2:.2f} dB")
print(f"Median 3x3 SNR: {snr_med3:.2f} dB")
print(f"Median 5x5 SNR: {snr_med5:.2f} dB")

# Display results
plt.figure(figsize=(15, 12))

plt.subplot(3, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(noisy_img, cmap='gray')
plt.title('Noisy (σ=20)')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(avg_3x3, cmap='gray')
plt.title(f'Average 3×3\nSNR={snr_avg3:.1f}dB')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(avg_5x5, cmap='gray')
plt.title(f'Average 5×5\nSNR={snr_avg5:.1f}dB')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(gauss_small, cmap='gray')
plt.title(f'Gaussian σ=1.0\nSNR={snr_gauss1:.1f}dB')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.imshow(gauss_large, cmap='gray')
plt.title(f'Gaussian σ=2.0\nSNR={snr_gauss2:.1f}dB')
plt.axis('off')

plt.subplot(3, 3, 7)
plt.imshow(median_3, cmap='gray')
plt.title(f'Median 3×3\nSNR={snr_med3:.1f}dB')
plt.axis('off')

plt.subplot(3, 3, 8)
plt.imshow(median_5, cmap='gray')
plt.title(f'Median 5×5\nSNR={snr_med5:.1f}dB')
plt.axis('off')

plt.suptitle('Smoothing Filters Comparison')
plt.tight_layout()
plt.savefig('filter_results.png')
plt.show()

# Test on salt & pepper noise too
salt_pepper = noisy_img.copy()
num_pixels = int(0.05 * salt_pepper.size)

# Add salt & pepper
for i in range(num_pixels // 2):
    row = np.random.randint(0, salt_pepper.shape[0])
    col = np.random.randint(0, salt_pepper.shape[1])
    salt_pepper[row, col] = 255 if np.random.random() > 0.5 else 0

# Test median filter on salt & pepper (should work better)
median_sp = cv2.medianBlur(salt_pepper, 5)
gauss_sp = cv2.GaussianBlur(salt_pepper, (5, 5), 1.5)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(salt_pepper, cmap='gray')
plt.title('Salt & Pepper Noise')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(median_sp, cmap='gray')
plt.title('Median Filter (Better)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(gauss_sp, cmap='gray')
plt.title('Gaussian Filter (Worse)')
plt.axis('off')

plt.savefig('salt_pepper_comparison.png')
plt.show()

print("Filter assignment done")