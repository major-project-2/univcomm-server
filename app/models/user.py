from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime

from app.db.base_class import Base


if TYPE_CHECKING:
    from .role import Role
    from .post import Post


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    roll_no = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_verified = Column(Boolean(), default=False)

    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")
    student_data = relationship("StudentData", uselist=False, back_populates="user")
    faculty_data = relationship("FacultyData", uselist=False, back_populates="user")
    alumni_data = relationship("AlumniData", uselist=False, back_populates="user")
    posts = relationship("Post", back_populates="user")
    questions = relationship("Question", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    answers = relationship("Answer", back_populates="user")
    question_raises: Mapped[List["Question"]] = relationship(
        secondary="hand_raises", back_populates="user_raises"
    )
    post_upvotes: Mapped[List["Post"]] = relationship(
        secondary="upvotes", back_populates="user_upvotes"
    )
    post_downvotes: Mapped[List["Post"]] = relationship(
        secondary="downvotes", back_populates="user_downvotes"
    )

    created_at = Column(DateTime(timezone=True), default=datetime.now)
