import re


class InputHelper:

    @staticmethod
    def user_interaction(devices):
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
                                        print('Microwave is set to', degree, '℃ and the timer is set to', timer,
                                              'seconds')
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

    @staticmethod
    def get_device_name(text):
        if text:
            if "turn" in text.split():
                device_temp_name = None
                if "on" in text.split():
                    device_temp_name = text.replace("turn on", "")
                elif "off" in text.split():
                    device_temp_name = text.replace("turn off", "")
                if device_temp_name:
                    return device_temp_name.strip().replace(' ', '-')
            if "query" in text.split():
                result = re.search('query(.*)status', text) or re.search('query(.*)channel', text) \
                         or re.search('query(.*)degrees', text)
                if result:
                    device_temp_name = result.group(1)
                    return device_temp_name.strip().replace(' ', '-')
            if 'switch' in text.split():
                result = re.search(' in (.*)', text)
                if result:
                    device_temp_name = result.group(1)
                    return device_temp_name.strip().replace(' ', '-')
            if 'set degrees' in text:
                result = re.search(' to (.*)', text)
                if result:
                    device_temp_name = result.group(1)
                    return device_temp_name.strip().replace(' ', '-')

