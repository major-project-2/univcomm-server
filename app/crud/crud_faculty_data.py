from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.faculty_data import FacultyData
from app.schemas.faculty_data import FacultyDataCreate, FacultyDataUpdate


class CRUDFacultyData(CRUDBase[FacultyData, FacultyDataCreate, FacultyDataUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: FacultyDataCreate, user_id: int
    ) -> FacultyData:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user(
            self, db: Session, *, user_id: int
    ) -> FacultyData:
       return db.query(self.model).filter(FacultyData.user_id == user_id).first()


faculty_data = CRUDFacultyData(FacultyData)
