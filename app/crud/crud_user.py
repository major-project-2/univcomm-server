from typing import Any, Dict, Optional, Union, List

from app import constants

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_roll_no(self, db: Session, *, roll_no: str) -> Optional[User]:
        return db.query(User).filter(User.roll_no == roll_no).first()

    def get_unverified_multi(self, db: Session, *, skip: int, limit: int) -> List[User]:
        return db.query(User).filter(User.is_verified == False).offset(skip).limit(limit).all()

    def get_inactive_multi(self, db: Session, *, skip: int, limit: int) -> List[User]:
        return db.query(User).filter(User.is_active == False).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            roll_no=obj_in.roll_no,
            role_id=obj_in.role_id,
            is_verified=obj_in.is_verified
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def verify(
        self, db: Session, *, db_obj: User
    ) -> User:
        db_obj.is_verified = True
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def activate(
        self, db: Session, *, db_obj: User
    ) -> User:
        db_obj.is_active = True
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def deactivate(
        self, db: Session, *, db_obj: User
    ) -> User:
        db_obj.is_active = False
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def set_is_profile_created(self, db: Session, *, db_obj: User) -> User:
        db_obj.is_profile_created = True
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_verified(self, user: User) -> bool:
        return user.is_verified

    def is_superuser(self, role: int) -> bool:
        return role == constants.ACTOR_SUPERUSER

    def is_student(self, role: int) -> bool:
        return role == constants.ACTOR_STUDENT

    def is_faculty(self, role: int) -> bool:
        return role == constants.ACTOR_FACULTY

    def is_alumni(self, role: int) -> bool:
        return role == constants.ACTOR_ALUMNI


user = CRUDUser(User)
