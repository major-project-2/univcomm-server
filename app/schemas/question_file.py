from typing import Optional

from pydantic import BaseModel

# Shared properties


class QuestionFileBase(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


# Properties to receive on question_file creation
class QuestionFileCreate(QuestionFileBase):
    url: str
    name: str


# Properties to receive on question_file update
class QuestionFileUpdate(QuestionFileBase):
    pass


# Properties shared by models stored in DB
class QuestionFileInDBBase(QuestionFileBase):
    id: int
    url: str
    name: str
    question_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class QuestionFile(QuestionFileInDBBase):
    pass


# Properties stored in DB
class QuestionFileInDB(QuestionFileInDBBase):
    pass
