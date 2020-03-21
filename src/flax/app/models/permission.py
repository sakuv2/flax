from pydantic import BaseModel


class PermissionBase(BaseModel):
    name: str


class PermissionCreate(PermissionBase):
    ...


class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True
