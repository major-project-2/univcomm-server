from typing import Optional

from pydantic import BaseModel, EmailStr

from datetime import datetime


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    roll_no: Optional[str] = None
    role_id: Optional[int] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    confirm_password: str
    first_name: str
    last_name: str
    roll_no: str
    role_id: int


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None



class UserInDBBase(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
