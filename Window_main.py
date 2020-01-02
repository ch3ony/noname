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



    def getDevices(self):
        info_device.getDevices(self)
        self.listDevice.clear()
        for i in glob.device:
            i_list = str(i)[str(i).find('(')+1:str(i).find(')')].split(',')
            device_ID = i_list[0][i_list[0].find('"')+1:-1]
            device_HOST = i_list[1][i_list[1].find('"') + 1:-1]
            device_TYPE = i_list[2][i_list[2].find('\'') + 1:-1]
            y = device_ID +" "+ device_HOST+" " + device_TYPE
            y = y.split(' ')
            strFormat = '%20s%20s%20s'
            strOut = ""
            strOut += strFormat % (y[0], y[1], y[2])
            print(strOut)
            self.listDevice.addItem(strOut)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
