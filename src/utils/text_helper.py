from enum import Enum


class CommandNames(Enum):
    TURN = "turn"
    QUERY = "query"
    SWITCH = "switch"
    DEGREES = "degrees"
    STATUS = "status"
    CHANNEL = "channel"


class DeviceStatus(Enum):
    ON = "on"
    OFF = "off"
