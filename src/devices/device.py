from pydantic import BaseModel


class Device(BaseModel):
    device_id: str
    device_name: str
    device_type: str
    state: str = "Off"

    def turn_on(self):
        self.state = "On"

    def turn_off(self):
        self.state = "Off"
