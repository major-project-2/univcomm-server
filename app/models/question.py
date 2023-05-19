from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .answer import Answer


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="questions")
    answers = relationship("Answer", back_populates="question",
                           order_by="desc(Answer.created_at)",  cascade="all, delete")

    question_files = relationship(
        "QuestionFile", back_populates="question", cascade="all, delete")

    created_at = Column(DateTime(timezone=True), default=datetime.now)
