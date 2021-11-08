from pydantic import BaseModel
from typing import Optional


class Register(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    email: str
    password: str
    profile: str
