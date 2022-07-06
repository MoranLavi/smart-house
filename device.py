

class Device:

    def __init__(self, device_id, device_name, device_type):
        self.device_id = device_id
        self.device_name = device_name
        self.device_type = device_type
        self.state = 'Off'

    def get_device_id(self):
        return self.device_id

    def get_device_name(self):
        return self.device_name

    def get_device_type(self):
        return self.device_type

    def get_state(self):
        return self.state

    def set_state(self, state_status):
        if state_status:
            self.state = state_status

    def turn_on(self):
        self.set_state('On')

    def turn_off(self):
        self.set_state('Off')
