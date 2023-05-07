from typing import Optional

from pydantic import BaseModel


# Shared properties
class PostBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


# Properties to receive on post creation
class PostCreate(PostBase):
    title: str
    content: str


# Properties to receive on post update
class PostUpdate(PostBase):
    pass


# Properties shared by models stored in DB
class PostInDBBase(PostBase):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties stored in DB
class PostInDB(PostInDBBase):
    pass
