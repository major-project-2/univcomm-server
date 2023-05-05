from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .alumni_data import AlumniData  # noqa: F401


class AlumniExperience(Base):
    __tablename__ = "alumni_experiences"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, index=True)
    organization = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    alumni_data_id = Column(Integer, primary_key=True)
    alumni_data_user_id = Column(Integer, primary_key=True)
    alumni_data_id = Column(Integer, ForeignKey("alumni_data.id"))
    alumni_data = relationship("AlumniData", back_populates="experiences")
