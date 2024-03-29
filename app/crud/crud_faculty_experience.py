from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.faculty_experience import FacultyExperience
from app.schemas.faculty_experience import FacultyExperienceCreate, FacultyExperienceUpdate


class CRUDFacultyExperience(CRUDBase[FacultyExperience, FacultyExperienceCreate, FacultyExperienceUpdate]):
    def create_with_faculty_data(
        self, db: Session, *, obj_in: FacultyExperienceCreate, faculty_data_id: int
    ) -> FacultyExperience:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, faculty_data_id=faculty_data_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_faculty_data(
            self, db: Session, *, faculty_data_id: int
    ) -> FacultyExperience:
        return db.query(self.model).filter(FacultyExperience.faculty_data_id == faculty_data_id).first()


faculty_experience = CRUDFacultyExperience(FacultyExperience)
