from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    latitude: str
    longitude: str
