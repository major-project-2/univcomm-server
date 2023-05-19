from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class QuestionFile(Base):
    __tablename__ = "question_files"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    name = Column(String)

    question_id = Column(Integer, ForeignKey(
        "questions.id", ondelete="CASCADE"))

    question = relationship("Question", back_populates="question_files")
