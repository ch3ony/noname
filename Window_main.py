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
        info_device.initConfig(self)    # 200102. initConfig
        self.btn_Searchdevice.clicked.connect(self.getDevices)  # [select/refresh btn]
        self.btn_Selectdevice.clicked.connect(self.selDevice)
        self.listDevice.itemClicked.connect(self.currentDevice)



    def getDevices(self):
        info_device.getDevices(self)
        info_device.listDevices(self)   # move listDevices > [+]getDevices

    def currentDevice(self):
        glob.selectDevice = glob.deviceList[self.listDevice.currentRow()]
        print(glob.selectDevice)

    def selDevice(self):
        info_device.selectDevice(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
