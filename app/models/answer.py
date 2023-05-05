from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .question import Question  # noqa: F401


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String)
    question_id = Column(Integer, primary_key=True)
    question_user_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="answers")
