import sys
from Info_util import info_device
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Global import *

form_class = uic.loadUiType("UI/frida_main.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_Searchdevice.clicked.connect(self.getDevices)  # [select/refresh btn]
        self.btn_Searchdevice.clicked.connect(self.listDevices)



    def getDevices(self):
        info_device.getDevices(self)

    def listDevices(self):
        info_device.listDevices(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
