# Image Filtering - Quick Reference Guide

## Overview
Image filtering is used to remove noise, enhance features, or prepare images for further processing.

---

## 1. LINEAR FILTERS

### What are Linear Filters?
- Apply **weighted average** of neighboring pixels
- Output is a **linear combination** of input pixels
- Good for **Gaussian noise** (random variations)

### Key Concept: Convolution
```
Output(x,y) = Σ Σ Image(x+i, y+j) × Kernel(i,j)
```
- Slide a kernel (small matrix) over the image
- Multiply overlapping values
- Sum them up to get new pixel value

---

### A. Average/Mean Filter

**Purpose:** Simple noise reduction by averaging

**How it works:**
```
Kernel (3×3):
┌─────────┐
│ 1  1  1 │
│ 1  1  1 │  × (1/9)
│ 1  1  1 │
└─────────┘
```

**OpenCV:**
```python
cv2.blur(image, (kernel_size, kernel_size))
```

**Pros:** Simple, fast
**Cons:** Blurs edges, loses detail

---

### B. Gaussian Filter

**Purpose:** Better noise reduction that preserves edges better than average filter

**Formula:**
```
G(x,y) = (1/2πσ²) × exp(-(x²+y²)/2σ²)
```

**Key Parameters:**
- **σ (sigma)**: Standard deviation
  - Small σ → Sharp, less blur
  - Large σ → Smooth, more blur

**Kernel Example (3×3, σ=1):**
```
┌─────────────┐
│ 1   2   1  │
│ 2   4   2  │  × (1/16)
│ 1   2   1  │
└─────────────┘
```

**OpenCV:**
```python
cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
```

**Why Gaussian?**
- Center pixels have **more weight**
- Weights decrease smoothly (bell curve)
- Preserves edges better than average filter
- Mathematically optimal for many applications

---

### C. Averaging Multiple Images

**Purpose:** Reduce noise by combining multiple shots

**Formula:**
```
Result = (Image1 + Image2 + ... + ImageN) / N
```

**When to use:**
- Static scene (camera on tripod)
- Multiple captures available
- Very effective for random noise

**Key Point:** Noise is random, signal is consistent!

---

## 2. NON-LINEAR FILTERS

### What are Non-Linear Filters?
- Do **NOT** use weighted averages
- Apply non-linear operations (sorting, min/max, etc.)
- Better for **salt & pepper noise** (random black/white pixels)

---

### A. Median Filter

**Purpose:** Remove salt & pepper noise while preserving edges

**How it works:**
1. Take neighborhood pixels (e.g., 3×3 = 9 pixels)
2. **Sort** them: [0, 5, 10, 15, 20, 100, 120, 250, 255]
3. Pick the **middle value** (median): 20
4. Replace center pixel with median

**Example:**
```
Before:          After:
┌─────────┐     ┌─────────┐
│ 50  55  60│   │ 50  55  60│
│ 52  255 58│ → │ 52  55  58│  (255 replaced by median 55)
│ 54  56  62│   │ 54  56  62│
└─────────┘     └─────────┘
```

**OpenCV:**
```python
cv2.medianBlur(image, kernel_size)
```

**Why Median?**
- Outliers (noise) are ignored
- Edges stay sharp (no averaging)
- Perfect for salt & pepper noise

---

### B. Bilateral Filter

**Purpose:** Smooth image while **strongly preserving edges**

**Key Idea:** 
- Consider both **spatial distance** AND **intensity difference**
- Blur similar pixels, keep different pixels separate

**Two Parameters:**
1. **σ_space**: How far to look (spatial)
2. **σ_color**: How different pixels can be (intensity)

**OpenCV:**
```python
cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
```

**When to use:**
- Need smooth regions BUT sharp edges
- Portrait photography (smooth skin, keep features)
- Preprocessing for segmentation

---

## 3. COMPARISON TABLE

| Filter Type | Best For | Edge Preservation | Speed | Noise Type |
|-------------|----------|-------------------|-------|------------|
| **Average** | Quick smoothing | Poor | Fast | Gaussian |
| **Gaussian** | General denoising | Good | Fast | Gaussian |
| **Median** | Salt & pepper | Excellent | Medium | Impulse |
| **Bilateral** | Edge-aware smoothing | Excellent | Slow | Gaussian |

---

## 4. QUALITY METRICS

### PSNR (Peak Signal-to-Noise Ratio)
```
PSNR = 10 × log₁₀(255² / MSE)
```
- **Higher is better** (less noise)
- Typical values: 30-50 dB
- MSE = Mean Squared Error

### SNR (Signal-to-Noise Ratio)
```
SNR = 10 × log₁₀(Signal_Power / Noise_Power)
```
- Measures signal strength vs noise
- Higher = cleaner image

---

## 5. PRACTICAL TIPS

### Choosing Kernel Size:
- **Small (3×3, 5×5)**: Subtle smoothing, faster
- **Large (7×7, 9×9)**: Strong smoothing, slower
- **Must be odd** (3, 5, 7, 9...) to have a center pixel

### Choosing σ (Sigma) for Gaussian:
- **σ = 0**: OpenCV calculates automatically
- **σ = 1**: Mild blur
- **σ = 3-5**: Moderate blur
- **σ > 5**: Strong blur

### When to Use Each Filter:

**Use Average Filter:**
- Quick prototyping
- Speed is critical
- Edges not important

**Use Gaussian Filter:**
- General-purpose denoising
- Preprocessing for edge detection
- Natural-looking blur

**Use Median Filter:**
- Salt & pepper noise visible
- Need to preserve edges
- Removing outliers

**Use Bilateral Filter:**
- Portrait/face images
- Need smooth regions + sharp edges
- Quality more important than speed

---

## 6. COMMON MISTAKES TO AVOID

1. **Too large kernel** → Over-smoothing, loss of detail
2. **Wrong filter for noise type** → Median for Gaussian noise won't work well
3. **Forgetting to convert image type** → Some filters need specific formats
4. **Not checking PSNR** → Can't measure improvement

---

## 7. CODE PATTERNS

### Basic Filtering Pattern:
```python
# 1. Read image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 2. Add noise (for testing)
noisy = add_noise(image)

# 3. Apply filter
filtered = cv2.GaussianBlur(noisy, (5, 5), 0)

# 4. Measure quality
psnr = calculate_psnr(image, filtered)
print(f"PSNR: {psnr:.2f} dB")

# 5. Display
display_images([image, noisy, filtered], 
               ['Original', 'Noisy', 'Filtered'])
```

---

## 8. PRESENTATION TIPS

### Demo Flow:
1. Show original clean image
2. Add noise (Gaussian or salt & pepper)
3. Apply different filters
4. Compare results side-by-side
5. Show PSNR values

### Key Points to Emphasize:
- **Linear vs Non-linear** distinction
- **Why median works for salt & pepper**
- **Gaussian bell curve** visualization
- **Trade-off**: smoothing vs edge preservation

### Interactive Elements:
- Adjust kernel size live
- Change sigma values
- Switch between filter types
- Show before/after with metrics

---

## 9. MATHEMATICAL INTUITION

### Why Gaussian is Special:
- **Central Limit Theorem**: Many random processes → Gaussian
- **Separable**: Can apply in X then Y (faster!)
- **Rotation invariant**: Same in all directions
- **Smooth**: No sudden jumps in weights

### Why Median Works:
- **Robust statistic**: Not affected by outliers
- **Order-based**: Sorting removes extremes
- **Non-linear**: Can't be expressed as weighted sum

---

## 10. QUICK FORMULAS CHEAT SHEET

```
Convolution:        Output = Σ Image × Kernel

Gaussian:           G(x,y) = (1/2πσ²) × exp(-(x²+y²)/2σ²)

MSE:                MSE = (1/N) Σ(Original - Processed)²

PSNR:               PSNR = 10 × log₁₀(255² / MSE)

SNR:                SNR = 10 × log₁₀(Signal² / Noise²)
```

---

## REMEMBER:
- **Linear filters** = weighted averages (blur everything)
- **Non-linear filters** = special operations (smart about edges)
- **Gaussian noise** → Use Gaussian filter
- **Salt & pepper** → Use median filter
- **Need edges** → Use bilateral or median
- **Higher PSNR** = Better quality

Good luck with your presentation! 🎓
