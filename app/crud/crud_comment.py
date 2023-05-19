from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def create_with_post_user(
        self, db: Session, *, obj_in: CommentCreate, post_id: int, user_id: int
    ) -> Comment:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, post_id=post_id, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, post_id: int, skip: int = 0, limit: int = 100
    ) -> List[Comment]:
        return (
            db.query(self.model)
            .filter(Comment.post_id == post_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_by_user(
        self, db: Session, *,  user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Comment]:
        return (
            db.query(self.model)
            .filter(Comment.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


comment = CRUDComment(Comment)
