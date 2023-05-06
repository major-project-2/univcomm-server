from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base

if TYPE_CHECKING:
    from .faculty_data import FacultyData  # noqa: F401


class FacultyExperience(Base):
    __tablename__ = "faculty_experiences"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    department = Column(String)
    organization = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    faculty_data_id = Column(Integer, ForeignKey("faculty_data.id"), primary_key=True)
    faculty_data_user_id = Column(Integer,  ForeignKey(
        "faculty_data.user_id"), primary_key=True)
    faculty_data = relationship(
        "FacultyData", backref=backref("experiences"), foreign_keys=[faculty_data_id])
