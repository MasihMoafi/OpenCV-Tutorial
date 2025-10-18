# Assignment 4: Adding Noise to Images  
# Masih Moafi - Computer Vision Course
# Dr. Mohammad Davarpanah Jazi

import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, sigma=20):
    # Convert to 16-bit signed to handle negative values
    img_16 = image.astype(np.int16)
    
    # Generate Gaussian noise
    noise = np.random.normal(mean, sigma, image.shape).astype(np.int16)
    
    # Add noise and clip to valid range
    noisy = img_16 + noise
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    
    return noisy

def add_salt_pepper_noise(image, amount=0.05):
    noisy = image.copy()
    num_pixels = int(amount * image.size)
    
    # Add salt (white pixels)
    for i in range(num_pixels // 2):
        row = np.random.randint(0, image.shape[0])
        col = np.random.randint(0, image.shape[1])
        noisy[row, col] = 255
    
    # Add pepper (black pixels)  
    for i in range(num_pixels // 2):
        row = np.random.randint(0, image.shape[0])
        col = np.random.randint(0, image.shape[1])
        noisy[row, col] = 0
    
    return noisy

def calculate_snr(original, noisy):
    signal_power = np.sum(original.astype(float) ** 2)
    noise_power = np.sum((original.astype(float) - noisy.astype(float)) ** 2)
    
    if noise_power == 0:
        return float('inf')
    
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Load test image
img = cv2.imread('how-many-horses.webp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Creating test image")
    img = np.ones((200, 200), dtype=np.uint8) * 128
    cv2.rectangle(img, (50, 50), (150, 150), 255, -1)
    cv2.rectangle(img, (75, 75), (125, 125), 64, -1)

print(f"Original image shape: {img.shape}")

# Add different types of noise
gaussian_sigma20 = add_gaussian_noise(img, sigma=20)
gaussian_sigma30 = add_gaussian_noise(img, sigma=30)
salt_pepper_5 = add_salt_pepper_noise(img, amount=0.05)
salt_pepper_10 = add_salt_pepper_noise(img, amount=0.10)

# Calculate SNR values
snr_g20 = calculate_snr(img, gaussian_sigma20)
snr_g30 = calculate_snr(img, gaussian_sigma30)
snr_sp5 = calculate_snr(img, salt_pepper_5)
snr_sp10 = calculate_snr(img, salt_pepper_10)

print(f"SNR Gaussian σ=20: {snr_g20:.2f} dB")
print(f"SNR Gaussian σ=30: {snr_g30:.2f} dB")
print(f"SNR Salt&Pepper 5%: {snr_sp5:.2f} dB")
print(f"SNR Salt&Pepper 10%: {snr_sp10:.2f} dB")

# Display results
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(gaussian_sigma20, cmap='gray')
plt.title(f'Gaussian σ=20\nSNR={snr_g20:.1f}dB')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(gaussian_sigma30, cmap='gray')
plt.title(f'Gaussian σ=30\nSNR={snr_g30:.1f}dB')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(salt_pepper_5, cmap='gray')
plt.title(f'Salt&Pepper 5%\nSNR={snr_sp5:.1f}dB')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(salt_pepper_10, cmap='gray')
plt.title(f'Salt&Pepper 10%\nSNR={snr_sp10:.1f}dB')
plt.axis('off')

plt.suptitle('Noise Addition Effects')
plt.tight_layout()
plt.savefig('noise_results.png')
plt.show()

print("Noise assignment done")