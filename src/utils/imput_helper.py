import re

from commands.query import Query
from commands.set import Set
from commands.switch import Switch
from commands.thermostat_timer import ThermostatAndTimer
from utils.text_helper import CommandNames, DeviceStatus


class CliInput:
    @staticmethod
    def user_interaction(devices, command: str):
        command = command.lower()
        device_name = CliInput.get_device_name(command)
        for device in devices:
            if device_name == device.device_id:
                if CommandNames.TURN.value in command.split():
                    Set.set_device_status(device, command)
                elif CommandNames.QUERY.value in command.split():
                    Query.query_device_status(device, command)
                elif CommandNames.SWITCH.value in command.split():
                    Switch.switch_device_channel(device)
                elif CommandNames.DEGREES.value in command.split():
                    ThermostatAndTimer.set_device_degrees_timer(device)

    @staticmethod
    def get_device_name(text):
        if text:
            if CommandNames.TURN.value in text.split():
                device_temp_name = None
                if DeviceStatus.ON.value in text.split():
                    device_temp_name = text.replace("turn on", "")
                elif DeviceStatus.OFF.value in text.split():
                    device_temp_name = text.replace("turn off", "")
                if device_temp_name:
                    return device_temp_name.strip().replace(" ", "-")
            if CommandNames.QUERY.value in text.split():
                result = (
                    re.search("query(.*)status", text)
                    or re.search("query(.*)channel", text)
                    or re.search("query(.*)degrees", text)
                )
                if result:
                    device_temp_name = result.group(1)
                    return device_temp_name.strip().replace(" ", "-")
            if CommandNames.SWITCH.value in text.split():
                result = re.search(" in (.*)", text)
                if result:
                    device_temp_name = result.group(1)
                    return device_temp_name.strip().replace(" ", "-")
            if "set degrees" in text:
                result = re.search(" to (.*)", text)
                if result:
                    device_temp_name = result.group(1)
                    return device_temp_name.strip().replace(" ", "-")
