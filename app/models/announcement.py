from typing import TYPE_CHECKING

from sqlalchemy import Column,  Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


from app.db.base_class import Base


class Announcement(Base):
    __tablename__ = "announcements"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

    announcement_files = relationship(
        "AnnouncementFile", back_populates="announcement", cascade="all, delete")

    created_at = Column(DateTime(timezone=True), default=datetime.now())
