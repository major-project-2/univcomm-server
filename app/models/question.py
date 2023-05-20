from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime


from app.db.base_class import Base


if TYPE_CHECKING:
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

    user_raises: Mapped[List["User"]] = relationship(
        secondary="hand_raises", back_populates="question_raises", cascade="all, delete"
    )

    created_at = Column(DateTime(timezone=True), default=datetime.now)
