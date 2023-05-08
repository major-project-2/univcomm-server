from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class AlumniData(Base):
    __tablename__ = "alumni_data"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)
    branch = Column(String)
    batch = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="alumni_data")
    experiences = relationship(
        "AlumniExperience", back_populates="alumni_data", cascade="all, delete")
