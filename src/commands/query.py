from utils.text_helper import CommandNames


class Query:
    @staticmethod
    def query_device_status(device, command: str):
        if CommandNames.STATUS in command.split():
            print("The", device.device_name, "is turned", device.state)
        elif CommandNames.DEGREES in command.split():
            print(device.device_name, "is set to", device.degrees, "degrees")
        elif CommandNames.CHANNEL in command.split():
            print(device.device_name, "channel is on", device.channel)
