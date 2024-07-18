import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

def input_gamma(file_path):
    if file_path:

        # Membuat GUI menggunakan Tkinter
        root = tk.Tk()
        root.title("Gamma Correction Demo")

        # Label dan kotak teks untuk input gamma
        label_gamma = tk.Label(root, width=60, text="Enter gamma value (0.0 - 2.0) :")
        label_gamma.pack()

        entry_gamma = tk.Entry(root, width=50)
        entry_gamma.pack()


        def on_convert():
            gamma_value = float(entry_gamma.get())
            convert_gamma(file_path, gamma_value)

        # Tombol untuk melakukan konversi
        btn_convert = tk.Button(root, text="Convert", command=on_convert)
        btn_convert.pack()

        root.mainloop()
def convert_gamma(file_path, entry_gamma):
    if file_path:

        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_float = img.astype(np.float64)

        gamma = (entry_gamma)
        img_gamma = np.power(img_float / 255.0, gamma) * 255.0
        img_gamma = np.array(img_gamma, dtype=np.uint8)

        # Menampilkan gambar asli dan transformasi gamma
        plt.figure(figsize=(20, 20))

        plt.subplot(1, 2, 1)
        plt.title('Original Image')
        plt.imshow(img)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title(f'Gamma Transformed Image (gamma = {gamma})')
        plt.imshow(img_gamma)
        plt.axis('off')

        plt.show()

