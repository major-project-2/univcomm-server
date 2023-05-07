from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Question], dependencies=[Depends(deps.check_verified_user)])
def read_questions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve questions.
    """
    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if crud.user.is_superuser(role=role_obj.role):
        questions = crud.question.get_multi(db, skip=skip, limit=limit)
    else:
        questions = crud.question.get_multi_by_user(
            db=db, user_id=current_user.id, skip=skip, limit=limit
        )
    return questions


@router.post("/", response_model=schemas.Question, dependencies=[Depends(deps.check_verified_user)])
def create_question(
    *,
    db: Session = Depends(deps.get_db),
    question_in: schemas.QuestionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new question.
    """
    question = crud.question.create_with_user(
        db=db, obj_in=question_in, user_id=current_user.id)
    return question


@router.put("/{id}", response_model=schemas.Question, dependencies=[Depends(deps.check_verified_user)])
def update_question(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    question_in: schemas.QuestionUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a question.
    """
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    if question.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    question = crud.question.update(db=db, db_obj=question, obj_in=question_in)
    return question


@router.get("/{id}", response_model=schemas.Question, dependencies=[Depends(deps.check_verified_user)])
def read_question(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get question by ID.
    """
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (question.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return question


@router.delete("/{id}", response_model=schemas.Question, dependencies=[Depends(deps.check_verified_user)])
def delete_question(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a question.
    """
    question = crud.question.get(db=db, id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (question.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    question = crud.question.remove(db=db, id=id)
    return question
