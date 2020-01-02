import frida
from Global import *

class info_device:

    def initConfig(self):
        try:
            glob.device_manager = frida.get_device_manager()
            glob.device_manager.enumerate_devices()
        except Exception as e:
            print(str(e))

    def getDevices(self):
        try:
            # device_manager = frida.get_device_manager() / 200102. move initConfig
            device_list = glob.device_manager.enumerate_devices()
            glob.device = []
            for i in device_list:
                glob.device.append(i)

        except Exception as e:
            print(str(e))

    def listDevices(self):
        try:
            self.listDevice.clear()
            for i in glob.device:
                i_list = str(i)[str(i).find('(') + 1:str(i).find(')')].split(',')
                device_ID = i_list[0][i_list[0].find('"') + 1:-1]
                device_HOST = i_list[1][i_list[1].find('"') + 1:-1]
                device_TYPE = i_list[2][i_list[2].find('\'') + 1:-1]
                y = device_ID + " " + device_HOST + " " + device_TYPE
                y = y.split(' ')
                strFormat = '%20s%20s%20s'
                strOut = ""
                strOut += strFormat % (y[0], y[1], y[2])
                print(strOut)
                self.listDevice.addItem(strOut)
        except Exception as e:
            print(str(e))
