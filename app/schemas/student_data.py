from typing import Optional

from pydantic import BaseModel

# Shared properties


class StudentDataBase(BaseModel):
    branch: Optional[str] = None
    semester: Optional[str] = None
    department: Optional[str] = None


# Properties to receive on student data creation
class StudentDataCreate(StudentDataBase):
    branch: str
    semester: str
    department: str


# Properties to receive on student data update
class StudentDataUpdate(StudentDataBase):
    pass


# Properties shared by models stored in DB
class StudentDataInDBBase(StudentDataBase):
    id: int
    branch: str
    semester: str
    department: str
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class StudentData(StudentDataInDBBase):
    pass


# Properties stored in DB
class StudentDataInDB(StudentDataInDBBase):
    pass
