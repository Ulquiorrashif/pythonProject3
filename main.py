from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sys
class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set()
    def set(self):
        self.wroot=uic.loadUi('untitled.ui')
        self.wroot.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    app.exec_()
    print("qwe")

    print("еще")

# dsfl's;'f