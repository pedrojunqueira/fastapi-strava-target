from pydantic import BaseModel


class KilometerRequest(BaseModel):
    target: int
    kilometers: int