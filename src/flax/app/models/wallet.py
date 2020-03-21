from typing import List

from pydantic import BaseModel

from .balance import Balance


class WalletBase(BaseModel):
    balancies: List[Balance]


class WalletCreate(WalletBase):
    ...


class Wallet(WalletBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
