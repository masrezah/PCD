import cv2
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread("dataset/clouds-8420083_1280.jpg")

# Tampilkan gambar asli (dalam format BGR)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Gambar Asli (BGR)')
plt.imshow(img)
plt.axis('off')

# Konversi gambar ke format RGB
img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Tampilkan gambar yang telah dikonversi ke RGB
plt.subplot(1, 2, 2)
plt.title('Gambar yang Telah Dikoversi ke RGB')
plt.imshow(img_cvt)
plt.axis('off')

plt.show()