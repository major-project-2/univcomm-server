from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.post_file import PostFile
from app.schemas.post_file import PostFileCreate, PostFileUpdate


class CRUDPostFile(CRUDBase[PostFile, PostFileCreate, PostFileUpdate]):
    def create_with_post(
        self, db: Session, *, obj_in: PostFileCreate, post_id: int
    ) -> PostFile:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, post_id=post_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_post(
            self, db: Session, *, post_id: int
    ) -> PostFile:
        return db.query(self.model).filter(PostFile.post_id == post_id).first()


post_file = CRUDPostFile(PostFile)
