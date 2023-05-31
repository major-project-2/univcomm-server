from typing import Optional, List

from pydantic import BaseModel

from datetime import datetime

from .post_file import PostFile
from .comment import Comment
from .user import User

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
    created_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    post_files: List[PostFile]
    comments: List[Comment]
    user_upvotes: List[User]
    user_downvotes: List[User]
    user: User

# Properties to return to client


class Posts(PostInDBBase):
    post_files: List[PostFile]
    comments: List[Comment]
    user_upvotes: List[User]
    user_downvotes: List[User]
    user_upvoted: bool
    user_downvoted: bool
    user: User


# Properties stored in DB
class PostInDB(PostInDBBase):
    pass
