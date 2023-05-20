from pydantic import BaseModel

# Shared properties


class DownvoteBase(BaseModel):
    pass

# Properties to receive on downvote creation


class DownvoteCreate(DownvoteBase):
    pass


# Properties to receive on downvote update
class DownvoteUpdate(DownvoteBase):
    pass


# Properties shared by models stored in DB
class DownvoteInDBBase(DownvoteBase):
    post_id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Downvote(DownvoteInDBBase):
    pass


# Properties stored in DB
class DownvoteInDB(DownvoteInDBBase):
    pass
