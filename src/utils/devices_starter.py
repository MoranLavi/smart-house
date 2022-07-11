from devices.air_conditioner import AirConditioner
from devices.computer import Computer
from devices.microwave import Microwave
from devices.tv import Tv


class DeviceInitializer:

    @staticmethod
    def init_devices():
        return [
            Tv(device_id="bedroom-tv", device_name="Bedroom TV", device_type="tv"),
            Tv(device_id="living-room-tv", device_name="Living Room TV", device_type="tv"),
            AirConditioner(device_id="air-conditioner", device_name="Air Conditioner", device_type="air_conditioner"),
            Microwave(device_id="microwave", device_name="Microwave", device_type="microwave"),
            Computer(device_id="computer", device_name="Computer", device_type="computer")
        ]