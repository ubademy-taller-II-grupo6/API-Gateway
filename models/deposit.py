from pydantic import BaseModel
from typing import Optional


class Deposit(BaseModel):
    senderId: str
    amountInEthers: str
