import traceback

from fastapi import FastAPI, HTTPException

from devices.computer import Computer
from devices.air_conditioner import AirConditioner
from devices.microwave import Microwave
from devices.tv import Tv
from utils.imput_helper import InputHelper


def init_devices():
    return [
        Tv("bedroom-tv", "Bedroom TV", "tv"),
        Tv("living-room-tv", "Living Room TV", "tv"),
        AirConditioner("air-conditioner", "Air Conditioner", "air_conditioner"),
        Microwave("microwave", "Microwave", "microwave"),
        Computer("computer", "Computer", "computer")
    ]


if __name__ == '__main__':
    devices = init_devices()
    InputHelper.user_interaction(devices)
