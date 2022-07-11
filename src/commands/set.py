from utils.text_helper import DeviceStatus


class Set:
    @staticmethod
    def set_device_status(device, command):
        if DeviceStatus.ON in command.split():
            device.turn_on()
            print(device.device_name, "is turned ", device.state)
        elif DeviceStatus.OFF in command.split():
            device.turn_off()
            print(device.device_name, "is turned ", device.state)
