from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.announcement_file import AnnouncementFile
from app.schemas.announcement_file import AnnouncementFileCreate, AnnouncementFileUpdate


class CRUDAnnouncementFile(CRUDBase[AnnouncementFile, AnnouncementFileCreate, AnnouncementFileUpdate]):
    def create_with_announcement(
        self, db: Session, *, obj_in: AnnouncementFileCreate, announcement_id: int
    ) -> AnnouncementFile:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, announcement_id=announcement_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_announcement(
            self, db: Session, *, announcement_id: int
    ) -> AnnouncementFile:
        return db.query(self.model).filter(AnnouncementFile.announcement_id == announcement_id).first()


announcement_file = CRUDAnnouncementFile(AnnouncementFile)
