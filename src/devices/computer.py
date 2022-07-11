from devices.device import Device


class Computer(Device):
    def __init__(self, device_id: str, device_name: str, device_type: str):
        super().__init__(device_id, device_name, device_type)
