from typing import List

from pydantic import BaseModel

from .user import User
from .permission import Permission, PermissionCreate


class AccountBase(BaseModel):
    name: str


class AccountCreate(AccountBase):
    password: str
    permissions: List[PermissionCreate]


class Account(AccountBase):
    id: int
    hashed_password: str
    users: List[User]
    permissions: List[Permission]

    class Config:
        orm_mode = True
