# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\08_multiplecamfeed.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap


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
                cv_img= cv2.resize(cv_img, (600, 300)) # resize
                # Convert the image to a Qt-compatible format
                qt_img = QImage(
                    cv_img.data, cv_img.shape[1], cv_img.shape[0], QImage.Format_RGB888)
                # Emit the signal to update the pixmap
                self.change_pixmap_signal.emit(qt_img)
            # sleep to give the GUI time to update
            self.msleep(10)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 791, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cam1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cam1.setFont(font)
        self.cam1.setAutoFillBackground(True)
        self.cam1.setFrameShape(QtWidgets.QFrame.Box)
        self.cam1.setScaledContents(True)
        self.cam1.setObjectName("cam1")
        self.horizontalLayout.addWidget(self.cam1)
        self.cam2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cam2.setFont(font)
        self.cam2.setAutoFillBackground(True)
        self.cam2.setFrameShape(QtWidgets.QFrame.Box)
        self.cam2.setScaledContents(True)
        self.cam2.setObjectName("cam2")
        self.horizontalLayout.addWidget(self.cam2)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(250, 350, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.button.setFont(font)
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.clicked.connect(self.start_video)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cam1.setText(_translate("MainWindow", "Cam1"))
        self.cam2.setText(_translate("MainWindow", "Cam2"))
        self.button.setText(_translate("MainWindow", "Start Feed"))

    def start_video(self):
        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def update_image(self, qt_img):
        # display the image in the label
        self.cam1.setPixmap(QPixmap.fromImage(qt_img))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())