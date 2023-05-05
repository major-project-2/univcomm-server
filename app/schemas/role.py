from typing import Optional

from pydantic import BaseModel


# Shared properties
class RoleBase(BaseModel):
    role: Optional[int] = -1


# Properties to receive via API on creation
class RoleCreate(RoleBase):
    role: int


# Properties to receive via API on update
class RoleUpdate(RoleBase):
    role: int


class RoleInDBBase(RoleBase):
    id: Optional[int] = None
    role: Optional[int] = -1

    class Config:
        orm_mode = True


# Additional properties to return via API
class Role(RoleInDBBase):
    pass
