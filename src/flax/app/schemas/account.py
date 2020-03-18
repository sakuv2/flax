from typing import List

from pydantic import BaseModel

from .user import User


class AccountBase(BaseModel):
    name: str


class AccountCreate(AccountBase):
    password: str


class Account(AccountBase):
    id: int
    users: List[User]

    class Config:
        orm_mode = True
