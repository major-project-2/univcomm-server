from typing import Optional

from pydantic import BaseModel

from datetime import datetime


# Shared properties
class QuestionBase(BaseModel):
    question: Optional[str] = None


# Properties to receive on question creation
class QuestionCreate(QuestionBase):
    question: str


# Properties to receive on question update
class QuestionUpdate(QuestionBase):
    pass


# Properties shared by models stored in DB
class QuestionInDBBase(QuestionBase):
    id: int
    question: str
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Question(QuestionInDBBase):
    pass


# Properties stored in DB
class QuestionInDB(QuestionInDBBase):
    pass
