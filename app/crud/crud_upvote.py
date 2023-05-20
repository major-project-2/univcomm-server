from typing import List


from sqlalchemy.orm import Session

from app.crud.base import CRUDBase

from app.models.upvote import Upvote
from app.schemas.upvote import UpvoteCreate, UpvoteUpdate


class CRUDUpvote(CRUDBase[Upvote, UpvoteCreate, UpvoteUpdate]):
    def create_with_post_user(
        self, db: Session, post_id: int, user_id: int
    ) -> Upvote:
        db_obj = self.model(post_id=post_id, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_post_user(
            self, db: Session, *, post_id: int, user_id: int
    ) -> Upvote:
        return db.query(self.model).filter(Upvote.post_id == post_id).filter(Upvote.user_id == user_id).first()

    def remove_by_post_user(self, db: Session, *, post_id: int, user_id: int) -> Upvote:
        obj = db.query(self.model).filter(Upvote.post_id ==
                                          post_id).filter(Upvote.user_id == user_id).first()
        db.delete(obj)
        db.commit()
        return obj


upvote = CRUDUpvote(Upvote)
