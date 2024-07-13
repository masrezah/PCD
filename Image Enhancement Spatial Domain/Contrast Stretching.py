import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar dan konversi ke grayscale
img = cv2.imread('dataset/clouds-8420083_1280.jpg', cv2.IMREAD_GRAYSCALE)

# Tentukan nilai minimum dan maksimum intensitas piksel
min_intensity = np.min(img)
max_intensity = np.max(img)

# Tentukan nilai minimum dan maksimum intensitas piksel baru
new_min = 0
new_max = 255

# Kontras Stretching
img_cs = (img - min_intensity) * ((new_max - new_min) / (max_intensity - min_intensity)) + new_min
img_cs = np.array(img_cs, dtype=np.uint8)

# Tampilkan gambar asli dan gambar dengan kontras stretching
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_cs, cmap='gray')
plt.title('Gambar dengan Kontras Stretching')
plt.axis('off')

plt.tight_layout()
plt.show()
