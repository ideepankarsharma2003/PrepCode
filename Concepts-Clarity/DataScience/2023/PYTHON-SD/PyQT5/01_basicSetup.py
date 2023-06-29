from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

app = QApplication(sys.argv)
win = QMainWindow()
label = QtWidgets.QLabel(win)





def buttonClick():
    print("Button Clicked")
    label.setText("This is great !!!"*10)
    # label.adjustSize()
    # label.layout()








def window():
    
    win.setGeometry(200, 200, 800, 600)
    win.setWindowTitle("PyQt5 Tutorial")

    label.setText("Hello World!")
    label.move(50, 50)


    b= QtWidgets.QPushButton(win)
    b.setText("Click me")
    b.move(100, 100)
    b.clicked.connect(buttonClick)

    win.show()
    sys.exit(app.exec_())


window()