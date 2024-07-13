import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('clouds-8420083_1280.jpg')
img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_negative = 255 - img_cvt
plt.figure(figsize=(15, 15))
plt.subplot(1,2,1)
plt.imshow(img_cvt)
plt.subplot(1,2,2)
plt.imshow(img_negative)
plt.show()



