import re


class InputHelper:

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

