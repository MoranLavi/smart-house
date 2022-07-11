
import typer
from utils.devices_starter import DeviceInitializer
from utils.imput_helper import CliInput

app = typer.Typer()


@app.command()
def enter_command(command: str = typer.Argument(..., help="The command you wish to enter")):
    devices = DeviceInitializer.init_devices()
    CliInput.user_interaction(devices, command)


if __name__ == "__main__":
    app()
