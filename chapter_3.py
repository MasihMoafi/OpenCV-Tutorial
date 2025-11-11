import cv2
import numpy as np
import matplotlib.pyplot as plt


def show(images: list[tuple[str, cv2.typing.MatLike]]):
    for title, img in images:
        cv2.imshow(title, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def plot(hists: list[tuple[str, str, str, np.ndarray, tuple]]):
    fig, axes = plt.subplots(1, len(hists), figsize=(6 * len(hists), 4))
    if len(hists) == 1:
        axes = [axes]

    for i, (title, xlabel, ylabel, hist, colors) in enumerate(hists):
        if colors:
            for j, c in enumerate(colors):
                axes[i].plot(np.arange(0, hist.shape[1]), hist[j], color=c)
        else:
            axes[i].plot(np.arange(0, len(hist)), hist, color="black")
        axes[i].set_title(title)
        axes[i].set_xlabel(xlabel)
        axes[i].set_ylabel(ylabel)

    plt.tight_layout()
    plt.show()


def compute_1D_histogram(image: np.ndarray, bins: int = 256) -> np.ndarray:
    """
    :param image: an ndarray of shape [height, width, channel]
    :return: an ndarray of shape [256]
    """
    factor = 256 // bins
    hist = np.zeros(bins, dtype=np.uint32)
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            intensity = image[row, col]
            quantized_index = intensity // factor
            hist[quantized_index] += 1

    # numpy solution
    # return np.histogram(image, bins=bins, range=(0, bins))[0]

    # open-cv solution
    # return cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[bins], ranges=[0, bins])

    return hist


def compute_3D_histogram(image: np.ndarray, bins: int = 256) -> np.ndarray:
    """
    :param image: an ndarray of shape [height, width, channel]
    :return: an ndarray of shape [3, 256]
    """
    factor = 256 // bins
    hist = np.zeros((3, bins), dtype=np.uint32)
    for chan in range(image.shape[2]):
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                intensity = image[row, col, chan]
                quantized_index = intensity // factor
                hist[chan][quantized_index] += 1

    # numpy solution
    # for chan in range(image.shape[2]):
    #     hist[chan] = np.histogram(image[:, :, chan], bins=bins, range=(0, bins))[0]
    # return hist

    # open-cv solution
    # for chan in range(image.shape[2]):
    #     hist[chan] = cv2.calcHist(images=[image], channels=[chan], mask=None, histSize=[bins], ranges=[0, bins]).flatten()
    # return hist

    return hist


def smoothed_histogram(image: np.ndarray) -> np.ndarray:
    hist = compute_1D_histogram(image)
    smoothed_hist = hist.copy()
    for i in range(1, len(hist) - 1):
        smoothed_hist[i] = (hist[i - 1] + hist[i] + hist[i + 1]) / 3

    return smoothed_hist


def histogram3D(image: np.ndarray):
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    bins = np.arange(8)
    b, g, r = np.meshgrid(bins, bins, bins)

    x = b.flatten()
    y = g.flatten()
    z = r.flatten()
    values = hist.flatten()
    values = values / values.max()
    colors = np.stack([r.flatten() / 7, g.flatten() / 7, b.flatten() / 7], axis=1)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x, y, z, c=colors, s=values * 500, alpha=0.6, edgecolors="none")
    ax.set_xlabel("Blue")
    ax.set_ylabel("Green")
    ax.set_zlabel("Red")
    ax.set_title("3D Color Histogram")

    plt.show()


def equalization(image: np.ndarray) -> np.ndarray:
    hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    output = hls_image.copy()
    luminance_hist = compute_1D_histogram(hls_image[:, :, 1])
    total_pixels_so_far = 0
    total_pixels = image.shape[0] * image.shape[1]
    output_gray_scale = 0
    lookup = {}
    for input_gray_scale in range(0, 256):
        total_pixels_so_far += luminance_hist[input_gray_scale]
        new_output_gray_scale = total_pixels_so_far * 256 / (total_pixels + 1)
        lookup[input_gray_scale] = ((output_gray_scale + 1 + new_output_gray_scale) / 2).astype(np.uint8)
        output_gray_scale = new_output_gray_scale

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            output[row, col, 1] = lookup[hls_image[row, col, 1]]

    # open-cv solution
    # hls_image = cv2.cvtColor(output, cv2.COLOR_BGR2HLS)
    # hls_image[:, :, 1] = cv2.equalizeHist(hls_image[:, :, 1])
    # return cv2.cvtColor(hls_image, cv2.COLOR_HLS2BGR)

    return cv2.cvtColor(output, cv2.COLOR_HLS2BGR)


def kmeans(image: np.ndarray, n_clusters: int = 10, max_iterations: int = 1000, random_state: int = 0):
    np.random.seed(random_state)

    def _compute_distance(inp1, inp2):
        return np.linalg.norm(inp1 - inp2, axis=2)

    pixels = image.reshape((-1, 3)).astype(np.float32)
    random_indices = np.random.permutation(pixels.shape[0])
    centroids = pixels[random_indices[:n_clusters]]
    labels = []

    for _ in range(max_iterations):
        distances = _compute_distance(pixels[:, np.newaxis], centroids)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([
            pixels[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
            for i in range(n_clusters)
        ])

        if np.all(new_centroids == centroids):
            break
        centroids = new_centroids

    return centroids, labels


gray_image = cv2.imread("/Users/mahyar/PycharmProjects/ML/images/chess.jpg", cv2.IMREAD_GRAYSCALE)
bgr_image = cv2.imread("/Users/mahyar/PycharmProjects/ML/images/lena.jpg")
dark_bgr_image = cv2.imread("/Users/mahyar/PycharmProjects/ML/images/dark-image.jpeg")
yuv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2YUV)
hls_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HLS)

centroids_, labels_ = kmeans(bgr_image, n_clusters=10, max_iterations=1000)
segmented_image = centroids_[labels_].reshape(bgr_image.shape).astype(np.uint8)

show([
    ("Main Image", bgr_image),
    ("Segmented Image", segmented_image),
])

plot(
    [
        ("Grayscale Histogram", "Intensity", "Number of Pixel", compute_1D_histogram(gray_image), ()),
        ("Grayscale Smoothed Histogram", "Intensity", "Number of Pixel", smoothed_histogram(gray_image), ()),
        ("BGR Histogram", "Intensity", "Number of Pixel", compute_3D_histogram(bgr_image), ("b", "g", "r")),
        ("YUV Histogram", "Intensity", "Number of Pixel", compute_3D_histogram(yuv_image), ("y", "c", "m")),
        ("HLS Histogram", "Intensity", "Number of Pixel", compute_3D_histogram(hls_image), ("g", "r", "black")),
        ("3D Histogram", "Intensity", "Number of Pixel", compute_3D_histogram(yuv_image), ("g", "r", "black")),
    ]
)

histogram3D(bgr_image)
