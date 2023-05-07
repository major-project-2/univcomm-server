from typing import Optional

from pydantic import BaseModel


# Shared properties
class CommentBase(BaseModel):
    comment: Optional[str] = None


# Properties to receive on comment creation
class CommentCreate(CommentBase):
    comment: str


# Properties to receive on comment update
class CommentUpdate(CommentBase):
    pass


# Properties shared by models stored in DB
class CommentInDBBase(CommentBase):
    id: int
    comment: str
    post_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Comment(CommentInDBBase):
    pass


# Properties stored in DB
class CommentInDB(CommentInDBBase):
    pass
