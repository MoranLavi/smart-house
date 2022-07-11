
class Switch:
    @staticmethod
    def switch_device_channel(device):
        channel = input('Choose channel: ').lower()
        device.set_chanel(channel)
        print(device.device_name, 'channel is set to ', channel)
