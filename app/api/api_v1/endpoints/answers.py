from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Answer], dependencies=[Depends(deps.check_verified_user)])
def read_answers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    *,
    question_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve answers.
    """
    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if crud.user.is_superuser(role=role_obj.role):
        answers = crud.answer.get_multi(
            db, question_id=question_id, skip=skip, limit=limit)
    else:
        answers = crud.answer.get_multi_by_user(
            db=db, question_id=question_id, user_id=current_user.id, skip=skip, limit=limit
        )
    return answers


@router.post("/", response_model=schemas.Answer, dependencies=[Depends(deps.check_verified_user)])
def create_answer(
    *,
    db: Session = Depends(deps.get_db),
    question_id: int,
    answer_in: schemas.AnswerCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new answer.
    """
    question = crud.question.get(db, id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    answer = crud.answer.create_with_question_user(
        db=db, obj_in=answer_in, question_id=question_id, user_id=current_user.id)
    return answer


@router.put("/{id}", response_model=schemas.Answer, dependencies=[Depends(deps.check_verified_user)])
def update_answer(
    *,
    db: Session = Depends(deps.get_db),
    question_id: int,
    id: int,
    answer_in: schemas.AnswerUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a answer.
    """
    answer = crud.answer.get(db=db, id=id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    if answer.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    answer = crud.answer.update(db=db, db_obj=answer, obj_in=answer_in)
    return answer


@router.get("/{id}", response_model=schemas.Answer, dependencies=[Depends(deps.check_verified_user)])
def read_answer(
    *,
    db: Session = Depends(deps.get_db),
    question_id: int,
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get answer by ID.
    """
    answer = crud.answer.get(db=db, id=id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (answer.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return answer


@router.delete("/{id}", response_model=schemas.Answer, dependencies=[Depends(deps.check_verified_user)])
def delete_answer(
    *,
    db: Session = Depends(deps.get_db),
    question_id: int,
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an answer.
    """
    answer = crud.answer.get(db=db, id=id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (answer.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    answer = crud.answer.remove(db=db, id=id)
    return answer
