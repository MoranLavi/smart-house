from devices.device import Device


class Microwave(Device):
    def __init__(self, device_id: str, device_name: str, device_type: str):
        super().__init__(device_id, device_name, device_type)
        self.degrees: str = ""
        self.timer: str = ""

    def get_degrees(self):
        return self.degrees

    def set_degrees(self, new_degrees):
        try:
            degrees_range = list(range(0, 31))
            if new_degrees not in degrees_range:
                raise ValueError()
            elif new_degrees:
                self.degrees = new_degrees
                print(self.get_device_name(), 'is set to', self.degrees, '℃')
        except ValueError:
            print("Error, please enter numeric up to 30℃")

    def get_timer(self):
        return self.timer

    def set_timer(self, time):
        if time:
            self.timer = time
