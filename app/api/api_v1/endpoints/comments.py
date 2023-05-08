from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Comment], dependencies=[Depends(deps.check_verified_user)])
def read_comments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    *,
    post_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve comments.
    """
    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if crud.user.is_superuser(role=role_obj.role):
        comments = crud.comment.get_multi(db, post_id=post_id, skip=skip, limit=limit)
    else:
        comments = crud.comment.get_multi_by_user(
            db=db, post_id=post_id, user_id=current_user.id, skip=skip, limit=limit
        )
    return comments


@router.post("/", response_model=schemas.Comment, dependencies=[Depends(deps.check_verified_user)])
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    post_id: int,
    comment_in: schemas.CommentCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new comment.
    """
    post = crud.post.get(db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    comment = crud.comment.create_with_post_user(
        db=db, obj_in=comment_in, post_id=post_id, user_id=current_user.id)
    return comment


@router.put("/{id}", response_model=schemas.Comment, dependencies=[Depends(deps.check_verified_user)])
def update_comment(
    *,
    db: Session = Depends(deps.get_db),
    post_id: int,
    id: int,
    comment_in: schemas.CommentUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a comment.
    """
    comment = crud.comment.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    comment = crud.comment.update(db=db, db_obj=comment, obj_in=comment_in)
    return comment


@router.get("/{id}", response_model=schemas.Comment, dependencies=[Depends(deps.check_verified_user)])
def read_comment(
    *,
    db: Session = Depends(deps.get_db),
    post_id: int,
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get comment by ID.
    """
    comment = crud.comment.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (comment.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return comment


@router.delete("/{id}", response_model=schemas.Comment, dependencies=[Depends(deps.check_verified_user)])
def delete_comment(
    *,
    db: Session = Depends(deps.get_db),
    post_id: int,
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a comment.
    """
    comment = crud.comment.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (comment.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    comment = crud.comment.remove(db=db, id=id)
    return comment
