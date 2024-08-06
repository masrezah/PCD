import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtCore import Qt
import cv2
import numpy as np


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Processor")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #2e2e2e; color: #f0f0f0;")

        self.image_path = None
        self.image = None
        self.original_image = None  # To store the original image

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Image Processor")
        self.title.setFont(QFont("Arial", 24, QFont.Bold))
        self.title.setStyleSheet("color: #4caf50; margin-bottom: 20px;")
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.load_button = QPushButton("Load Image")
        self.load_button.setStyleSheet("background-color: #4caf50; font-size: 16px; padding: 10px;")
        self.load_button.clicked.connect(self.load_image)
        self.button_layout.addWidget(self.load_button)

        self.save_button = QPushButton("Save Image")
        self.save_button.setStyleSheet("background-color: #4caf50; font-size: 16px; padding: 10px;")
        self.save_button.clicked.connect(self.save_image)
        self.button_layout.addWidget(self.save_button)

        self.contrast_button = QPushButton("Contrast Enhancement")
        self.contrast_button.setStyleSheet("background-color: #4caf50; font-size: 16px; padding: 10px;")
        self.contrast_button.clicked.connect(self.contrast_enhancement)
        self.button_layout.addWidget(self.contrast_button)

        self.sharpness_button = QPushButton("Increased Sharpness")
        self.sharpness_button.setStyleSheet("background-color: #4caf50; font-size: 16px; padding: 10px;")
        self.sharpness_button.clicked.connect(self.increased_sharpness)
        self.button_layout.addWidget(self.sharpness_button)

        self.noise_button = QPushButton("Noise Reduction")
        self.noise_button.setStyleSheet("background-color: #4caf50; font-size: 16px; padding: 10px;")
        self.noise_button.clicked.connect(self.noise_reduction)
        self.button_layout.addWidget(self.noise_button)

        self.brightness_button = QPushButton("Brightness")
        self.brightness_button.setStyleSheet("background-color: #4caf50; font-size: 16px; padding: 10px;")
        self.brightness_button.clicked.connect(self.brightness_and_color_adjustment)
        self.button_layout.addWidget(self.brightness_button)

        self.reset_button = QPushButton("Reset Image")
        self.reset_button.setStyleSheet("background-color: #ff5722; font-size: 16px; padding: 10px;")
        self.reset_button.clicked.connect(self.reset_image)
        self.button_layout.addWidget(self.reset_button)

        self.image_frame = QFrame()
        self.image_frame.setStyleSheet("background-color: #404040; border: 2px solid #4caf50;")
        self.image_frame.setLayout(QVBoxLayout())
        self.layout.addWidget(self.image_frame)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_label)

    def load_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName()
        self.image = cv2.imread(self.image_path)
        self.original_image = self.image.copy()  # Save a copy of the original image
        self.display_image()

    def save_image(self):
        if self.image is not None:
            filename, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.jpg *.jpeg *.png)")
            if filename:
                cv2.imwrite(filename, self.image)

    def contrast_enhancement(self):
        if self.image is not None:
            self.image = cv2.convertScaleAbs(self.image, alpha=1.5, beta=0)
            self.display_image()

    def increased_sharpness(self):
        if self.image is not None:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            self.image = cv2.filter2D(self.image, -1, kernel)
            self.display_image()

    def noise_reduction(self):
        if self.image is not None:
            self.image = cv2.GaussianBlur(self.image, (5, 5), 0)
            self.display_image()

    def brightness_and_color_adjustment(self):
        if self.image is not None:
            self.image = cv2.convertScaleAbs(self.image, alpha=1, beta=50)
            self.display_image()

    def reset_image(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.display_image()

    def display_image(self):
        height, width, channel = self.image.shape
        bytes_per_line = 3 * width
        qImg = QImage(self.image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.image_label.setPixmap(QPixmap.fromImage(qImg).scaled(800, 400))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
