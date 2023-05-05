from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .post import Post  # noqa: F401


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    post_id = Column(Integer, primary_key=True)
    post_user_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")
