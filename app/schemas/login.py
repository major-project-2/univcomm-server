from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class LoginBase(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None


# Properties to receive via API on login
class LoginIn(LoginBase):
    email: EmailStr
    password: str
