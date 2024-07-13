import cv2
import matplotlib.pyplot as plt
import numpy as np

gambar_a = cv2.imread('gambar 1.jpg',1)
gambar_a = cv2.cvtColor(gambar_a, cv2.COLOR_BGR2RGB)
gambar_b = cv2.imread('gambar g.jpg',1)
gambar_b = cv2.cvtColor(gambar_b, cv2.COLOR_BGR2RGB)

gambar_add = cv2.add(gambar_a, gambar_b)
plt.figure(figsize=(20, 20))
plt.subplot(1,3,1)
plt.imshow(gambar_a)
plt.subplot(1,3,2)
plt.imshow(gambar_b)
plt.subplot(1,3,3)
plt.imshow(gambar_add)
plt.show()

print(gambar_a.shape)
print(gambar_b.shape)
# print(gambar_c.shape)