from pydantic import BaseModel

from .currency import Code


class BalanceBase(BaseModel):
    code: Code
    amount: float


class BalanceCreate(BalanceBase):
    ...


class Balance(BalanceBase):
    id: int
    wallet_id: int

    class Config:
        orm_mode = True
