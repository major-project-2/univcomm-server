from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase

from app.models.downvote import Downvote
from app.schemas.downvote import DownvoteCreate, DownvoteUpdate


class CRUDDownvote(CRUDBase[Downvote, DownvoteCreate, DownvoteUpdate]):
    def create_with_post_user(
        self, db: Session, post_id: int, user_id: int
    ) -> Downvote:
        db_obj = self.model(post_id=post_id, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_post_user(
            self, db: Session, *, post_id: int, user_id: int
    ) -> Downvote:
        return db.query(self.model).filter(Downvote.post_id == post_id).filter(Downvote.user_id == user_id).first()

    def remove_by_post_user(self, db: Session, *, post_id: int, user_id: int) -> Downvote:
        obj = db.query(self.model).filter(Downvote.post_id ==
                                          post_id).filter(Downvote.user_id == user_id).first()
        db.delete(obj)
        db.commit()
        return obj


downvote = CRUDDownvote(Downvote)
