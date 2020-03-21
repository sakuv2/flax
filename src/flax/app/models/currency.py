from typing import NewType

from pydantic import BaseModel

Code = NewType("Code", str)


class CurrencyBase(BaseModel):
    code: Code


class CurrencyCreate(CurrencyBase):
    ...


class Currency(CurrencyBase):
    id: int

    class Config:
        orm_mode = True
