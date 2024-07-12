import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
image1 = cv2.imread('gambar 1.jpg')
image2 = cv2.imread('gambar g.jpg')

# Pastikan kedua gambar memiliki ukuran yang sama
if image1.shape != image2.shape:
    raise ValueError("Kedua gambar harus memiliki ukuran yang sama untuk digabungkan.")

# Tentukan bobot untuk blending
alpha = 0.5  # Bobot untuk gambar pertama
beta = 1 - alpha  # Bobot untuk gambar kedua

# Gabungkan gambar dengan blending
blended_image = cv2.addWeighted(image1, alpha, image2, beta, 0)

# Tampilkan gambar asli dan gambar hasil penggabungan
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Gambar 1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Gambar 2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 3)
plt.title('Gambar Hasil Blending')
plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))

plt.show()

