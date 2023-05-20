from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime


from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", order_by="desc(Comment.created_at)", cascade="all, delete")

    post_files = relationship(
        "PostFile", back_populates="post", cascade="all, delete")
    
    user_upvotes: Mapped[List["User"]] = relationship(
        secondary="upvotes", back_populates="post_upvotes", cascade="all, delete"
    )

    user_downvotes: Mapped[List["User"]] = relationship(
        secondary="downvotes", back_populates="post_downvotes", cascade="all, delete"
    )

    created_at = Column(DateTime(timezone=True), default=datetime.now)
