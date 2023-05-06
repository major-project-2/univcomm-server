from typing import Optional

from datetime import date

from pydantic import BaseModel


# Shared properties
class AlumniExperienceBase(BaseModel):
    department: Optional[str] = None
    organization: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


# Properties to receive on alumni experience creation
class AlumniExperienceCreate(AlumniExperienceBase):
    department: str
    organization: str
    start_date: str
    end_date: str


# Properties to receive on alumni experience update
class AlumniExperienceUpdate(AlumniExperienceBase):
    pass


# Properties shared by models stored in DB
class AlumniExperienceInDBBase(AlumniExperienceBase):
    id: int
    department: str
    organization: str
    start_date: date
    end_date: date
    alumni_data_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class AlumniExperience(AlumniExperienceInDBBase):
    pass


# Properties properties stored in DB
class AlumniExperienceInDB(AlumniExperienceInDBBase):
    pass
