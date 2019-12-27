import frida
from Global import *

class info_device:
    def getDevices(self):
        try:
            device_manager = frida.get_device_manager()
            device_list = device_manager.enumerate_devices()
            glob.device = []
            glob.device.append(device_list)
            print(glob.device)
        except Exception as e:
            print(str(e))
