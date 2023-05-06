from typing import Optional

from pydantic import BaseModel


# Shared properties
class AlumniDataBase(BaseModel):
    department: Optional[str] = None
    branch: Optional[str] = None
    batch: Optional[str] = None


# Properties to receive on alumni data creation
class AlumniDataCreate(AlumniDataBase):
    department: str
    branch: str
    batch: str


# Properties to receive on alumni data update
class AlumniDataUpdate(AlumniDataBase):
    pass


# Properties shared by models stored in DB
class AlumniDataInDBBase(AlumniDataBase):
    id: int
    department: str
    branch: str
    batch: str
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class AlumniData(AlumniDataInDBBase):
    pass


# Properties properties stored in DB
class AlumniDataInDB(AlumniDataInDBBase):
    pass
