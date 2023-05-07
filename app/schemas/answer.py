from typing import Optional

from pydantic import BaseModel


# Shared properties
class AnswerBase(BaseModel):
    answer: Optional[str] = None


# Properties to receive on answer creation
class AnswerCreate(AnswerBase):
    answer: str


# Properties to receive on answer update
class AnswerUpdate(AnswerBase):
    pass


# Properties shared by models stored in DB
class AnswerInDBBase(AnswerBase):
    id: int
    answer: str
    question_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Answer(AnswerInDBBase):
    pass


# Properties stored in DB
class AnswerInDB(AnswerInDBBase):
    pass
