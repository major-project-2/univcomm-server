from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401
    from .role import Role
    from .post import Post
    from .question import Question


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    roll_no = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_verified = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")
    student_data = relationship("StudentData", uselist=False, back_populates="user")
    faculty_data = relationship("FacultyData", uselist=False, back_populates="user")
    alumni_data = relationship("AlumniData", uselist=False, back_populates="user")
    posts = relationship("Post", back_populates="user")
    questions = relationship("Question", back_populates="user")
