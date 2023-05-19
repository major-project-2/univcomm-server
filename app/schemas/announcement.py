from typing import Optional, List

from pydantic import BaseModel

from datetime import datetime

from .announcement_file import AnnouncementFile

# Shared properties


class AnnouncementBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


# Properties to receive on announcement creation
class AnnouncementCreate(AnnouncementBase):
    title: str
    content: str


# Properties to receive on announcement update
class AnnouncementUpdate(AnnouncementBase):
    pass


# Properties shared by models stored in DB
class AnnouncementInDBBase(AnnouncementBase):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Announcement(AnnouncementInDBBase):
    announcement_files: List[AnnouncementFile]


# Properties stored in DB
class AnnouncementInDB(AnnouncementInDBBase):
    pass
