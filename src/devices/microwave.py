from devices.device import Device


class Microwave(Device):
    degrees: int = 0
    timer: int = 0

    def set_degrees(self, new_degrees: int):
        try:
            degrees_range = list(range(0, 31))
            if new_degrees not in degrees_range:
                raise ValueError()
            elif new_degrees:
                self.degrees = new_degrees
                print(self.device_name, "is set to", self.degrees, "℃")
        except ValueError("Input out of range"):
            print("Error, please enter numeric up to 30℃")

    def set_timer(self, time: int):
        if time:
            self.timer = time

