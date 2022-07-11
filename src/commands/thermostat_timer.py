

class ThermostatAndTimer:

    @staticmethod
    def set_device_degrees_timer(device):
        if device.device_id.lower() == 'microwave':
            ThermostatAndTimer.set_device_degrees(device)
            while True:
                try:
                    timer = int(input('Set timer to (Time in seconds): ').lower())
                except ValueError:
                    print("You have entered invalid value, please enter only digits")
                else:
                    if 0 <= timer <= 1000:
                        device.timer = timer
                        print(device.device_name, 'is set to', device.degrees, '℃ and the timer is set to',
                              timer, 'seconds')
                        break
                    else:
                        print('Out of range. Try again')

        elif device.device_id.lower() == 'air-conditioner':
            ThermostatAndTimer.set_device_degrees(device)
            print(device.device_name, 'is set to', device.degrees)

    @staticmethod
    def set_device_degrees(device):
        while True:
            try:
                degree = int(input('Set degrees to (Up to 30℃): '))
            except ValueError:
                print("You have entered invalid value, please enter only digits up to 30")
            else:
                if 0 <= degree < 30:
                    device.set_degrees(degree)
                    break
                else:
                    print('Out of range. Try again')

    @staticmethod
    def set_device_timer(device):
        while True:
            try:
                timer = int(input('Set timer to (Time in seconds): '))
            except ValueError:
                print("You have entered invalid value, please enter only digits")
            else:
                if 0 <= timer <= 1000:

                    device.set_timer(timer)
                    break
                else:
                    print('Out of range. Try again')
