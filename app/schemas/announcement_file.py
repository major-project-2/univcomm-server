from typing import Optional

from pydantic import BaseModel

# Shared properties
class AnnouncementFileBase(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


# Properties to receive on announcement_file creation
class AnnouncementFileCreate(AnnouncementFileBase):
    url: str
    name: str


# Properties to receive on announcement_file update
class AnnouncementFileUpdate(AnnouncementFileBase):
    pass


# Properties shared by models stored in DB
class AnnouncementFileInDBBase(AnnouncementFileBase):
    id: int
    url: str
    name: str
    announcement_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class AnnouncementFile(AnnouncementFileInDBBase):
    pass


# Properties stored in DB
class AnnouncementFileInDB(AnnouncementFileInDBBase):
    pass
