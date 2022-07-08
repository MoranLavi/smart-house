import re
from fastapi import FastAPI, HTTPException

app = FastAPI()


class InputHelper:

    @staticmethod
    def set_device_status(device, user_commend):
        if "on" in user_commend.split():
            device.turn_on()
            response = {
                "data": user_commend,
                "message": device.get_device_name() + ' is turned ' + device.get_state()
            }
            return response
        elif "off" in user_commend.split():
            device.turn_off()
            response = {
                "data": user_commend,
                "message": device.get_device_name() + ' is turned ' + device.get_state()
            }
            return response

    @staticmethod
    def query_device_status(device, user_commend):
        if "status" in user_commend.split():
            response = {
                "data": user_commend,
                "message": 'The ' + device.get_device_name() + ' is turned ' + device.get_state()
            }
            return response
        elif "degrees" in user_commend.split():
            response = {
                "data": user_commend,
                "message": device.get_device_name() + ' is on ' + device.get_degrees() + 'degrees'
            }
            return response
        elif "channel" in user_commend.split():
            response = {
                "data": user_commend,
                "message": device.get_device_name() + ' channel is on ' + device.get_chanel()
            }
            return response

    @staticmethod
    def switch_device_channel(device):
        channel = input('Choose channel: ').lower()
        device.set_chanel(channel)
        print(device.get_device_name(), ' channel is set to ', channel)

    @staticmethod
    def set_device_degrees_timer(device):
        if device.get_device_name().lower() == 'microwave':
            InputHelper.set_device_degrees(device)
            while True:
                try:
                    timer = int(input('Set timer to (Time in seconds): ').lower())
                except ValueError:
                    print("You have entered invalid value, please enter only digits")
                else:
                    if 0 <= timer <= 1000:
                        device.set_timer(timer)
                        print(device.get_device_name(), 'is set to', device.get_degrees(), '℃ and the timer is set to',
                              timer, 'seconds')
                        break
                    else:
                        print('Out of range. Try again')

        elif device.get_device_name().lower() == 'air-conditioner':
            InputHelper.set_device_degrees(device)
            InputHelper.set_device_timer(device)
            print(device.get_device_name(), 'is set to', device.get_degrees(), '℃ and the timer is set to',
                  device.get_timer(), 'seconds')

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
