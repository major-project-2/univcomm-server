from typing import Optional, List

from pydantic import BaseModel

from .faculty_experience import FacultyExperience


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
    experiences: List[FacultyExperience]


# Properties stored in DB
class FacultyDataInDB(FacultyDataInDBBase):
    pass
