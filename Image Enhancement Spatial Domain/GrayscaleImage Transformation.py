import cv2
import matplotlib.pyplot as plt
import numpy as np

# Gray Images

# Membaca gambar
img = cv2.imread('dataset/fotbar.jpg')

# Mengubah
img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mengubah warna dari BGR ke RGB
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menampilkan Gambar

plt.figure(figsize=(20, 20))
plt.subplot(1,2,1)
plt.imshow(img_cvt)
plt.subplot(1,2,2)
plt.imshow(img_gray, cmap="gray")
plt.show()
