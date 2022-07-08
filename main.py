import traceback
from fastapi import FastAPI, HTTPException, requests

from entities.activator import Activator
from entities.html_request import HtmlRequest

app = FastAPI()


@app.post("/command_activator")
def command_activator(html_request: HtmlRequest):
    try:
        response = Activator.command_activator(html_request)
    except Exception as e:
        err = traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)
        msg = {
            "message": str(e),
            "Error": "Method error",
            "traceback": err,
            "success": False,
            "Method": 'command_activator',
            "Class": "Activator"
        }
        print(msg)
        raise HTTPException(status_code=422, detail=msg)

    return response
