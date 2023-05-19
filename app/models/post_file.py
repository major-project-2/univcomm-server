from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class PostFile(Base):
    __tablename__ = "post_files"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    name = Column(String)

    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"))

    post = relationship("Post", back_populates="post_files")
