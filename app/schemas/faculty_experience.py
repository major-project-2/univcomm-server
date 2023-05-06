from typing import Optional

from datetime import date

from pydantic import BaseModel


# Shared properties
class FacultyExperienceBase(BaseModel):
    department: Optional[str] = None
    organization: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


# Properties to receive on faculty experience creation
class FacultyExperienceCreate(FacultyExperienceBase):
    department: str
    organization: str
    start_date: str
    end_date: str


# Properties to receive on faculty experience update
class FacultyExperienceUpdate(FacultyExperienceBase):
    pass


# Properties shared by models stored in DB
class FacultyExperienceInDBBase(FacultyExperienceBase):
    id: int
    department: str
    organization: str
    start_date: date
    end_date: date
    faculty_data_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class FacultyExperience(FacultyExperienceInDBBase):
    pass


# Properties properties stored in DB
class FacultyExperienceInDB(FacultyExperienceInDBBase):
    pass
