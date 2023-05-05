from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .faculty_data import FacultyData  # noqa: F401


class FacultyExperience(Base):
    __tablename__ = "faculty_experiences"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, index=True)
    organization = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    faculty_data_id = Column(Integer, primary_key=True)
    faculty_data_user_id = Column(Integer, primary_key=True)
    faculty_data_id = Column(Integer, ForeignKey("faculty_data.id"))
    faculty_data = relationship("FacultyData", back_populates="experiences")