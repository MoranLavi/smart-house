from device import Device


class Tv(Device):
    def __init__(self, device_id: str, device_name: str, device_type: str):
        super().__init__(device_id, device_name,  device_type)
        self.chanel: str = ""

    def get_chanel(self):
        return self.chanel

    def set_chanel(self, new_chanel):
        if new_chanel:
            self.chanel = new_chanel
