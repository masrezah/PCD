import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca gambar dan konversi ke RGB
img = cv2.imread('dataset/pexels-pixabay-67566.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Konversi ke tipe float untuk operasi yang lebih tepat
img_float = img.astype(float)

# Mencerahkan gambar dengan menambahkan nilai ke setiap kanal warna
brightness_factor = 1.5  # Faktor pencerahan, bisa disesuaikan
brightened_img_float = img_float * brightness_factor

# Pastikan nilai piksel tetap di dalam rentang 0-255
brightened_img_float[brightened_img_float > 255] = 255
brightened_img = np.array(brightened_img_float, dtype=np.uint8)

# Tampilkan gambar asli dan gambar yang telah dicerahkan
plt.figure(figsize=(20, 10))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(brightened_img)
plt.title('Gambar yang Telah Dicerahkan')
plt.axis('off')

plt.show()
