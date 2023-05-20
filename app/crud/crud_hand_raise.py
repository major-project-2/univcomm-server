from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase

from app.models.hand_raise import HandRaise
from app.schemas.hand_raise import HandRaiseCreate, HandRaiseUpdate


class CRUDHandRaise(CRUDBase[HandRaise, HandRaiseCreate, HandRaiseUpdate]):
    def create_with_question_user(
        self, db: Session, question_id: int, user_id: int
    ) -> HandRaise:
        db_obj = self.model(question_id=question_id, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def get_by_question(
    #         self, db: Session, *, question_id: int
    # ) -> QuestionFile:
    #     return db.query(self.model).filter(QuestionFile.question_id == question_id).first()

    def get_by_question_user(
            self, db: Session, *, question_id: int, user_id: int
    ) -> HandRaise:
        return db.query(self.model).filter(HandRaise.question_id == question_id).filter(HandRaise.user_id == user_id).first()

    def remove_by_question_user(self, db: Session, *, question_id: int, user_id: int) -> HandRaise:
        obj = db.query(self.model).filter(HandRaise.question_id ==
                                          question_id).filter(HandRaise.user_id == user_id).first()
        db.delete(obj)
        db.commit()
        return obj


hand_raise = CRUDHandRaise(HandRaise)
