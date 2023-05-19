from typing import Optional

from pydantic import BaseModel

# Shared properties


class PostFileBase(BaseModel):
    url: Optional[str] = None
    name: Optional[str] = None


# Properties to receive on post_file creation
class PostFileCreate(PostFileBase):
    url: str
    name: str


# Properties to receive on post_file update
class PostFileUpdate(PostFileBase):
    pass


# Properties shared by models stored in DB
class PostFileInDBBase(PostFileBase):
    id: int
    url: str
    name: str
    post_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class PostFile(PostFileInDBBase):
    pass


# Properties stored in DB
class PostFileInDB(PostFileInDBBase):
    pass
