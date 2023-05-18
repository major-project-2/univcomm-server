from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base

if TYPE_CHECKING:
    from .question import Question  # noqa: F401
    from .user import User


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String)

    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id"))

    question = relationship("Question", back_populates="answers")
    user = relationship("User", back_populates="answers")

    created_at = Column(DateTime(timezone=True), default=datetime.now())
