from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.student_data import StudentData
from app.schemas.student_data import StudentDataCreate, StudentDataUpdate


class CRUDStudentData(CRUDBase[StudentData, StudentDataCreate, StudentDataUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: StudentDataCreate, user_id: int
    ) -> StudentData:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user(
            self, db: Session, *, user_id: int
    ) -> StudentData:
       return db.query(self.model).filter(StudentData.user_id == user_id).first()


student_data = CRUDStudentData(StudentData)
