import cv2
import matplotlib.pyplot as plt
import numpy as np

def convert_to_negative(file_path):
    if file_path:

        img = cv2.imread(file_path)
        img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_negative = 255 - img_cvt

        plt.figure(figsize=(15, 15))

        plt.subplot(1, 2, 1)
        plt.title('Original Image')
        plt.imshow(img_cvt)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title('Negative Image')
        plt.imshow(img_negative)
        plt.axis('off')

        plt.show()