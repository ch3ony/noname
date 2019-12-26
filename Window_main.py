import sys
from Info_util import info_device
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("UI/frida_main.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnRefDevices.clicked.connect(self.getDevices)

    def getDevices(self):
        info_device.getDevices(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()