from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate, AnswerUpdate


class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    def create_with_question_user(
        self, db: Session, *, obj_in: AnswerCreate, question_id: int, user_id: int
    ) -> Answer:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, question_id=question_id, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, question_id: int, skip: int = 0, limit: int = 100
    ) -> List[Answer]:
        return (
            db.query(self.model)
            .filter(Answer.question_id == question_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Answer]:
        return (
            db.query(self.model)
            .filter(Answer.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


answer = CRUDAnswer(Answer)
