from devices.air_conditioner import AirConditioner
from devices.computer import Computer
from devices.microwave import Microwave
from devices.tv import Tv


class DeviceInitializer:

    @staticmethod
    def init_devices():
        return [
            Tv("bedroom-tv", "Bedroom TV", "tv"),
            Tv("living-room-tv", "Living Room TV", "tv"),
            AirConditioner("air-conditioner", "Air Conditioner", "air_conditioner"),
            Microwave("microwave", "Microwave", "microwave"),
            Computer("computer", "Computer", "computer")
        ]