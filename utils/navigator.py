import os
import traceback

from utils.imput_helper import InputHelper

from devices.computer import Computer
from devices.air_conditioner import AirConditioner
from devices.microwave import Microwave
from devices.tv import Tv

from fastapi import FastAPI, HTTPException


app = FastAPI()


class Navigator:

    @staticmethod
    def user_interaction(object):
        devices = Navigator.init_devices()
        while True:
            if object:
                user_commend = object.lower()
            else:
                user_commend = input('Please enter your commend: ').lower()
            if user_commend == 'exit':
                break

            device_name = InputHelper.get_device_name(user_commend)
            for device in devices:
                if device_name == device.get_device_id():
                    if "turn" in user_commend.split():
                        return InputHelper.set_device_status(device, user_commend)
                    elif "query" in user_commend.split():
                        return InputHelper.query_device_status(device, user_commend)
                    elif "switch" in user_commend.split():
                        return InputHelper.switch_device_channel(device)
                    elif "degrees" in user_commend.split():
                        return InputHelper.set_device_degrees_timer(device)

    @staticmethod
    def init_devices():
        return [
            Tv("bedroom-tv", "Bedroom TV", "tv"),
            Tv("living-room-tv", "Living Room TV", "tv"),
            AirConditioner("air-conditioner", "Air Conditioner", "air_conditioner"),
            Microwave("microwave", "Microwave", "microwave"),
            Computer("computer", "Computer", "computer")
        ]