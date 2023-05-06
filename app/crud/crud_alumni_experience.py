from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.alumni_experience import AlumniExperience
from app.schemas.alumni_experience import AlumniExperienceCreate, AlumniExperienceUpdate


class CRUDAlumniExperience(CRUDBase[AlumniExperience, AlumniExperienceCreate, AlumniExperienceUpdate]):
    def create_with_alumni_data(
        self, db: Session, *, obj_in: AlumniExperienceCreate, alumni_data_id: int
    ) -> AlumniExperience:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, alumni_data_id=alumni_data_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_alumni_data(
            self, db: Session, *, alumni_data_id: int
    ) -> AlumniExperience:
        return db.query(self.model).filter(AlumniExperience.alumni_data_id == alumni_data_id).first()


alumni_experience = CRUDAlumniExperience(AlumniExperience)
