from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.get("/unverified", response_model=List[schemas.User])
def read_unverified_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve unverified users.
    """
    users = crud.user.get_unverified_multi(db, skip=skip, limit=limit)
    return users


@router.get("/inactive", response_model=List[schemas.User])
def read_inactive_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve inactive users.
    """
    users = crud.user.get_inactive_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.user.get_by_roll_no(db, roll_no=user_in.roll_no)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this roll number already exists in the system.",
        )
    user_in.is_verified = True
    user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud.user.get_by_roll_no(db, roll_no=user_in.roll_no)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this roll number already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user


@router.post("/data/student", response_model=schemas.StudentData, dependencies=[Depends(deps.check_verified_user)])
def create_student_data(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_student),
    student_data_in: schemas.StudentDataCreate,
) -> Any:
    """
    Create Student data.
    """
    student_data = crud.student_data.get_by_user(db, user_id=current_user.id)
    if student_data:
        raise HTTPException(
            status_code=400,
            detail="The user already has a student profile.",
        )
    student_data = crud.student_data.create_with_user(
        db, obj_in=student_data_in, user_id=current_user.id)
    return student_data


@router.post("/data/faculty", response_model=schemas.FacultyData, dependencies=[Depends(deps.check_verified_user)])
def create_faculty_data(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_faculty),
    faculty_data_in: schemas.FacultyDataCreate,
) -> Any:
    """
    Create Faculty data.
    """
    faculty_data = crud.faculty_data.get_by_user(db, user_id=current_user.id)
    if faculty_data:
        raise HTTPException(
            status_code=400,
            detail="The user already has a faculty profile.",
        )
    faculty_data = crud.faculty_data.create_with_user(
        db, obj_in=faculty_data_in, user_id=current_user.id)
    return faculty_data


@router.post("/data/alumni", response_model=schemas.AlumniData, dependencies=[Depends(deps.check_verified_user)])
def create_alumni_data(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_alumni),
    alumni_data_in: schemas.AlumniDataCreate,
) -> Any:
    """
    Create Alumni data.
    """
    alumni_data = crud.alumni_data.get_by_user(db, user_id=current_user.id)
    if alumni_data:
        raise HTTPException(
            status_code=400,
            detail="The user already has an alumni profile.",
        )
    alumni_data = crud.alumni_data.create_with_user(
        db, obj_in=alumni_data_in, user_id=current_user.id)
    return alumni_data


# @router.post("/data/faculty/experience", response_model=schemas.FacultyExperience)
# def create_faculty_experience(
#     *,
#     db: Session = Depends(deps.get_db),
#     current_user: models.User = Depends(deps.get_current_active_faculty),
#     faculty_experience_in: schemas.FacultyExperienceCreate,
# ) -> Any:
#     """
#     Create Faculty experience.
#     """
#     if not crud.user.is_verified(current_user):
#         raise HTTPException(
#             status_code=400, detail="Kindly verify your user account to create an alumni profile."
#         )
#     alumni_data = crud.alumni_data.get_by_user(db, user_id=current_user.id)
#     if alumni_data:
#         raise HTTPException(
#             status_code=400,
#             detail="The user already has an alumni profile.",
#         )
#     alumni_data = crud.alumni_data.create_with_user(
#         db, obj_in=alumni_data_in, user_id=current_user.id)
#     return alumni_data

# @router.post("/data/alumni/experience", response_model=schemas.AlumniExperience)
# def create_alumni_experience(
#     *,
#     db: Session = Depends(deps.get_db),
#     current_user: models.User = Depends(deps.get_current_active_alumni),
#     alumni_experience_in: schemas.AlumniExperienceCreate,
# ) -> Any:
#     """
#     Create Alumni experience.
#     """
#     if not crud.user.is_verified(current_user):
#         raise HTTPException(
#             status_code=400, detail="Kindly verify your user account to create an alumni profile."
#         )
#     alumni_data = crud.alumni_data.get_by_user(db, user_id=current_user.id)
#     if alumni_data:
#         raise HTTPException(
#             status_code=400,
#             detail="The user already has an alumni profile.",
#         )
#     alumni_data = crud.alumni_data.create_with_user(
#         db, obj_in=alumni_data_in, user_id=current_user.id)
#     return alumni_data


@router.patch('/verify/{user_id}')
async def verify_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Verify a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user does not exist in the system",
        )
    user = crud.user.verify(db, db_obj=user)
    return user


@router.patch('/activate/{user_id}')
async def activate_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Activate a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user does not exist in the system",
        )
    user = crud.user.activate(db, db_obj=user)
    return user


@router.patch('/deactivate/{user_id}')
async def deactivate_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Deactivate a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user does not exist in the system",
        )
    user = crud.user.deactivate(db, db_obj=user)
    return user
