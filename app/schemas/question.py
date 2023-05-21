from typing import Optional, List

from pydantic import BaseModel

from datetime import datetime

from .question_file import QuestionFile
from .answer import Answer
from .user import User


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
    question_files: List[QuestionFile]
    answers: List[Answer]
    user_raises: List[User]

# Properties to return to client


class Questions(QuestionInDBBase):
    question_files: List[QuestionFile]
    answers: List[Answer]
    user_raises: List[User]
    user_hand_raised: bool


# Properties stored in DB
class QuestionInDB(QuestionInDBBase):
    pass
