import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('clouds-8420083_1280.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.figure(figsize=(20, 20))


plt.subplot(1,2,1)
plt.imshow(img,cmap="gray")
plt.subplot(1,2,2)
plt.imshow(img_gray,cmap="gray")
plt.show()