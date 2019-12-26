import frida

class info_device:
    def getDevices(self):
        try:
            device_manager = frida.get_device_manager()
            device_list = device_manager.enumerate_devices()
            print(device_list)
            print("testtesttest")
        except Exception as e:
            print(str(e))
