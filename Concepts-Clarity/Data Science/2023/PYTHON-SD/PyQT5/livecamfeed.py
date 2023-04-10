import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)

        while True:
            ret, cv_img = cap.read()
            if ret:
                # Convert the image to RGB
                cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                # Convert the image to a Qt-compatible format
                qt_img = QImage(
                    cv_img.data, cv_img.shape[1], cv_img.shape[0], QImage.Format_RGB888)
                # Emit the signal to update the pixmap
                self.change_pixmap_signal.emit(qt_img)
            # sleep to give the GUI time to update
            self.msleep(10)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQT5 Webcam'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.width-30, self.height-30)

        # create a button
        button = QPushButton('Play', self)
        button.move(0, self.height -20)
        button.clicked.connect(self.start_video)

        # layout = QVBoxLayout()
        # self.setLayout(self.layout)

        # layout.addWidget(self.image_label)
        # layout.addWidget(button)

        # # Set margins
        # self.layout.setContentsMargins(50, 20, 50, 20)

        self.show()

    def start_video(self):
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def update_image(self, qt_img):
        # display the image in the label
        self.image_label.setPixmap(QPixmap.fromImage(qt_img))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
