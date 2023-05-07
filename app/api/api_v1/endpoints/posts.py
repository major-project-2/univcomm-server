from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Post], dependencies=[Depends(deps.check_verified_user)])
def read_posts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve posts.
    """
    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if crud.user.is_superuser(role=role_obj.role):
        posts = crud.post.get_multi(db, skip=skip, limit=limit)
    else:
        posts = crud.post.get_multi_by_user(
            db=db, user_id=current_user.id, skip=skip, limit=limit
        )
    return posts


@router.post("/", response_model=schemas.Post, dependencies=[Depends(deps.check_verified_user)])
def create_post(
    *,
    db: Session = Depends(deps.get_db),
    post_in: schemas.PostCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new post.
    """
    post = crud.post.create_with_user(db=db, obj_in=post_in, user_id=current_user.id)
    return post


@router.put("/{id}", response_model=schemas.Post, dependencies=[Depends(deps.check_verified_user)])
def update_post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    post_in: schemas.PostUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a post.
    """
    post = crud.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")

    post = crud.post.update(db=db, db_obj=post, obj_in=post_in)
    return post


@router.get("/{id}", response_model=schemas.Post, dependencies=[Depends(deps.check_verified_user)])
def read_post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get post by ID.
    """
    post = crud.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (post.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return post


@router.delete("/{id}", response_model=schemas.Post, dependencies=[Depends(deps.check_verified_user)])
def delete_post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a post.
    """
    post = crud.post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    role_obj = crud.role.get_current_user_role(db, user=current_user)
    if not crud.user.is_superuser(role=role_obj.role) and (post.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    post = crud.post.remove(db=db, id=id)
    return post
