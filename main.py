from tinydb import TinyDB, Query
from device import Device

from devices.computer import Computer
from devices.air_conditioner import AirConditioner
from devices.microwave import Microwave
from devices.tv import Tv
from utils.imput_helper import InputHelper

db = TinyDB('db.json')

# devices = [
#     {
#         "identifier": "bedroom-tv",
#         "name": "Bedroom TV",
#         "device_type": "tv",
#         "state": False
#     },
#     {
#         "identifier": "living-room-tv",
#         "name": "Living Room TV",
#         "device_type": "tv",
#         "state": False
#     },
#     {
#         "identifier": "air-conditioner",
#         "name": "Air Conditioner",
#         "device_type": "air_conditioner",
#         "state": False
#     },
#     {
#         "identifier": "microwave",
#         "name": "Microwave",
#         "device_type": "microwave",
#         "state": False
#     },
#     {
#         "identifier": "computer",
#         "name": "Computer",
#         "device_type": "switch",
#         "state": False
#     }
# ]


def init_devices():
    devices = []
    bedroom_tv = Tv("bedroom-tv", "Bedroom TV", "tv")
    living_room_tv = Tv("living-room-tv", "Living Room TV", "tv")
    air_conditioner = AirConditioner("air-conditioner", "Air Conditioner", "air_conditioner")
    microwave = Microwave("microwave", "Microwave", "microwave")
    computer = Computer("computer", "Computer", "computer")
    devices.append(bedroom_tv)
    devices.append(living_room_tv)
    devices.append(air_conditioner)
    devices.append(microwave)
    devices.append(computer)
    return devices

def add_new_device():
    identifier = input('Identifier: ')
    device_name = input('Device name: ')
    device_type = input('Device type: ')
    device = Device(identifier, device_name, device_type)


if __name__ == '__main__':
    devices = init_devices()
    while True:
        user_commend = input('Please enter your commend: ').lower()
        if user_commend == 'exit':
            break

        device_name = InputHelper.get_device_name(user_commend)
        for device in devices:
            if device_name == device.get_device_id():
                if "turn" in user_commend.split():
                    if "on" in user_commend.split():
                        device.turn_on()
                        print(device.get_device_name(), 'is turned ', device.get_state())
                    elif "off" in user_commend.split():
                        device.turn_off()
                        print(device.get_device_name(), 'is turned ', device.get_state())

                elif "query" in user_commend.split():
                    if "status" in user_commend.split():
                        print('The', device.get_device_name(), 'is turned', device.get_state())
                    elif "degrees" in user_commend.split():
                        print(device.get_device_name(), 'is on', device.get_degrees(), 'degrees')
                    elif "channel" in user_commend.split():
                        print(device.get_device_name(), 'channel is on', device.get_chanel())

                elif "switch" in user_commend.split():
                    channel = input('Choose channel: ').lower()
                    device.set_chanel(channel)
                    print(device.get_device_name(), 'channel is set to ', channel)

                elif "degrees" in user_commend.split():
                    if device.get_device_name().lower() == 'microwave':
                        while True:
                            try:
                                degree = int(input('Set degrees to (Up to 30℃): ').lower())
                            except ValueError:
                                print("You have entered invalid value, please enter only digits up to 30")
                            else:
                                if 0 <= degree < 30:
                                    device.set_degrees(degree)
                                    break
                                else:
                                    print('Out of range. Try again')

                        while True:
                            try:
                                timer = int(input('Set timer to (Time in seconds): ').lower())
                            except ValueError:
                                print("You have entered invalid value, please enter only digits")
                            else:
                                if 0 <= timer <= 1000:
                                    device.set_timer(timer)
                                    print('Microwave is set to', degree, '℃ and the timer is set to', timer, 'seconds')
                                    break
                                else:
                                    print('Out of range. Try again')

                    elif device.get_device_name().lower() == 'air-conditioner':
                        while True:
                            try:
                                degree = int(input('Set degrees to (Up to 30℃): ').lower())
                            except ValueError:
                                print("You have entered invalid value, please enter only digits up to 30")
                            else:
                                if 0 <= degree < 30:
                                    device.set_degrees(degree)
                                    break
                                else:
                                    print('Out of range. Try again')

