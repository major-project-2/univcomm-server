from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.alumni_data import AlumniData
from app.schemas.alumni_data import AlumniDataCreate, AlumniDataUpdate


class CRUDAlumniData(CRUDBase[AlumniData, AlumniDataCreate, AlumniDataUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: AlumniDataCreate, user_id: int
    ) -> AlumniData:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user(
            self, db: Session, *, user_id: int
    ) -> AlumniData:
        return db.query(self.model).filter(AlumniData.user_id == user_id).first()


alumni_data = CRUDAlumniData(AlumniData)
