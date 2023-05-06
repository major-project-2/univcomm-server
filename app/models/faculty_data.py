from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class FacultyData(Base):
    __tablename__ = "faculty_data"
    id = Column(Integer, primary_key=True, index=True,  autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, unique=True)
    designation = Column(String)
    user = relationship("User", back_populates="faculty_data")
    experiences = relationship("FacultyExperience", back_populates="faculty_data")

    
