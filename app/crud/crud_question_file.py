from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.question_file import QuestionFile
from app.schemas.question_file import QuestionFileCreate, QuestionFileUpdate


class CRUDQuestionFile(CRUDBase[QuestionFile, QuestionFileCreate, QuestionFileUpdate]):
    def create_with_question(
        self, db: Session, *, obj_in: QuestionFileCreate, question_id: int
    ) -> QuestionFile:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, question_id=question_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_question(
            self, db: Session, *, question_id: int
    ) -> QuestionFile:
        return db.query(self.model).filter(QuestionFile.question_id == question_id).first()


question_file = CRUDQuestionFile(QuestionFile)
