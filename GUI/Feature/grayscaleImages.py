import cv2
import matplotlib.pyplot as plt
import numpy as np

def convert_to_grayscale(file_path):
    if file_path:

        img = cv2.imread(file_path)
        img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plt.figure(figsize=(20, 20))

        plt.subplot(1, 2, 1)
        plt.title('Original Image')
        plt.imshow(img_cvt)

        plt.subplot(1, 2, 2)
        plt.title('Grayscale Image')
        plt.imshow(img_gray, cmap="gray")
        plt.show()