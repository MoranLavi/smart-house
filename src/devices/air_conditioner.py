from devices.device import Device


class AirConditioner(Device):
    degrees: int = 25

    def set_degrees(self, new_degrees: int):
        try:
            degrees_range = list(range(10, 31))
            if new_degrees not in degrees_range:
                raise ValueError()
            elif new_degrees:
                self.degrees = new_degrees
                print(self.device_name, "is set to", self.degrees, "℃")
        except ValueError("Input out of range"):
            print("Error, please enter numeric input from 10℃ to 30℃")
