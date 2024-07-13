import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('dataset/pexels-pixabay-67566.jpg', 0)
gamma = 2.5
img_power = img**gamma
plt.figure(figsize=(20, 20))
plt.subplot(1,2,1)
plt.imshow(img,cmap="gray")
plt.subplot(1,2,2)
plt.imshow(img_power,cmap="gray")
plt.show()