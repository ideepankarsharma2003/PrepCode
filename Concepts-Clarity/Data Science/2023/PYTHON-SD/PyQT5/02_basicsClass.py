from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os



class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("PyQt5 Tutorial")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World!")
        self.label.move(50, 50)

        self.b = QtWidgets.QPushButton(self)
        self.b.setText("Click me")
        self.b.move(100, 100)
        self.b.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app= QApplication(sys.argv)
    win= MyWindow()
    win.show()
    sys.exit(app.exec_())

window()