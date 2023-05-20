from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User
    from .question import Question


class HandRaise(Base):
    __tablename__ = "hand_raises"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"),
                         primary_key=True)
