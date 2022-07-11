from devices.device import Device


class Tv(Device):
    channel: str = ""

    def set_chanel(self, new_channel: str):
        if new_channel:
            self.channel = new_channel
