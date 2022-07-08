from pydantic import BaseModel


class HtmlRequest(BaseModel):
    commend: str
