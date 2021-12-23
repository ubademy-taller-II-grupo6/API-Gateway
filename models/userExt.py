from pydantic import BaseModel


class UserExt(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    latitude: str
    longitude: str
    blocked: bool
