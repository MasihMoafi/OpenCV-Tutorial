import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread('how-many-horses.webp', cv2.IMREAD_GRAYSCALE)

# WRONG - shows blue
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(img)  # No cmap specified - shows blue!
plt.title('WRONG: Blue tint')

# CORRECT - grayscale
plt.subplot(132)
plt.imshow(img, cmap='gray')  # Specify grayscale colormap
plt.title('CORRECT: Grayscale')

# For color images - convert BGR to RGB
img_color = cv2.imread('how-many-horses.webp', cv2.IMREAD_COLOR)
plt.subplot(133)
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))  # Convert BGR→RGB
plt.title('CORRECT: Color')

plt.tight_layout()
plt.show()

print("Always use cmap='gray' for grayscale images!")
print("Always convert BGR→RGB for color images!")