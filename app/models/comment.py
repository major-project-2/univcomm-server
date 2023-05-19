from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base

if TYPE_CHECKING:
    from .post import Post  # noqa: F401
    from .user import User


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments")
    user = relationship("User", back_populates="comments")

    created_at = Column(DateTime(timezone=True), default=datetime.now)
