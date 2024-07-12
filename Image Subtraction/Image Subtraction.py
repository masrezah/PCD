from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# Baca gambar
image1 = Image.open('gambar 1.jpg')
image2 = Image.open('gambar g.jpg')

# Pastikan kedua gambar memiliki ukuran yang sama
if image1.size != image2.size:
    raise ValueError("Kedua gambar harus memiliki ukuran yang sama untuk digabungkan.")

# Gabungkan gambar dengan pengurangan pixel-wise
subtracted_image = ImageChops.subtract(image1, image2)

# Tampilkan gambar asli dan gambar hasil pengurangan
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Gambar 1')
plt.imshow(image1)

plt.subplot(1, 3, 2)
plt.title('Gambar 2')
plt.imshow(image2)

plt.subplot(1, 3, 3)
plt.title('Gambar Hasil Pengurangan')
plt.imshow(subtracted_image)

plt.show()
