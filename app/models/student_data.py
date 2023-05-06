from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class StudentData(Base):
    __tablename__ = "student_data"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, unique=True)
    branch = Column(String)
    semester = Column(String)
    department = Column(String)
    user = relationship("User", back_populates="student_data")
