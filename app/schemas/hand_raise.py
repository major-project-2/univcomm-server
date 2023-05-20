from typing import Optional

from pydantic import BaseModel

# Shared properties


class HandRaiseBase(BaseModel):
    pass

# Properties to receive on hand_raise creation


class HandRaiseCreate(HandRaiseBase):
    pass


# Properties to receive on hand_raise update
class HandRaiseUpdate(HandRaiseBase):
    pass


# Properties shared by models stored in DB
class HandRaiseInDBBase(HandRaiseBase):
    question_id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class HandRaise(HandRaiseInDBBase):
    pass


# Properties stored in DB
class HandRaiseInDB(HandRaiseInDBBase):
    pass
