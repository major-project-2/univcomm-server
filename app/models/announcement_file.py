from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base


class AnnouncementFile(Base):
    __tablename__ = "announcement_files"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)

    announcement_id = Column(Integer, ForeignKey("announcements.id", ondelete="CASCADE"))

    announcement = relationship("Announcement", back_populates="announcement_files")

    created_at = Column(DateTime(timezone=True), default=datetime.now())
