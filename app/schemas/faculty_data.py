from typing import Optional

from pydantic import BaseModel


# Shared properties
class FacultyDataBase(BaseModel):
    designation: Optional[str] = None


# Properties to receive on faculty data creation
class FacultyDataCreate(FacultyDataBase):
    designation: str


# Properties to receive on faculty data update
class FacultyDataUpdate(FacultyDataBase):
    pass


# Properties shared by models stored in DB
class FacultyDataInDBBase(FacultyDataBase):
    id: int
    designation: str
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class FacultyData(FacultyDataInDBBase):
    pass


# Properties stored in DB
class FacultyDataInDB(FacultyDataInDBBase):
    pass
