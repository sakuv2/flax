from pydantic import BaseModel

from .wallet import Wallet


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    wallet: Wallet

    class Config:
        orm_mode = True
