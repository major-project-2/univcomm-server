from pydantic import BaseModel

# Shared properties


class UpvoteBase(BaseModel):
    pass

# Properties to receive on upvote creation


class UpvoteCreate(UpvoteBase):
    pass


# Properties to receive on upvote update
class UpvoteUpdate(UpvoteBase):
    pass


# Properties shared by models stored in DB
class UpvoteInDBBase(UpvoteBase):
    post_id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Upvote(UpvoteInDBBase):
    pass


# Properties stored in DB
class UpvoteInDB(UpvoteInDBBase):
    pass
