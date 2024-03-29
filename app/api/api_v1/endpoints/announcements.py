from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Announcement], dependencies=[Depends(deps.check_verified_user)])
def read_announcements(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve announcements.
    """
    announcements = crud.announcement.get_multi(db, skip=skip, limit=limit)
    return announcements


@router.post("/", response_model=schemas.Announcement)
def create_announcement(
    *,
    db: Session = Depends(deps.get_db),
    announcement_in: schemas.AnnouncementCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new announcement.
    """
    announcement = crud.announcement.create(db=db, obj_in=announcement_in)
    return announcement


@router.put("/{id}", response_model=schemas.Announcement)
def update_announcement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    announcement_in: schemas.AnnouncementUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an announcement.
    """
    announcement = crud.announcement.get(db=db, id=id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    announcement = crud.announcement.update(
        db=db, db_obj=announcement, obj_in=announcement_in)
    return announcement


@router.get("/{id}", response_model=schemas.Announcement, dependencies=[Depends(deps.check_verified_user)])
def read_announcement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get announcement by ID.
    """
    announcement = crud.announcement.get(db=db, id=id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    return announcement


@router.delete("/{id}", response_model=schemas.Announcement)
def delete_announcement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an announcement.
    """
    announcement = crud.announcement.get(db=db, id=id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    announcement = crud.announcement.remove(db=db, id=id)
    return announcement


@router.post('/{announcement_id}/files', response_model=schemas.AnnouncementFile)
def create_announcement_file(
    *,
    db: Session = Depends(deps.get_db),
    announcement_id: int,
    announcement_file_in: schemas.AnnouncementFileCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new announcement file.
    """
    announcement = crud.announcement.get(db=db, id=announcement_id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    announcement_file = crud.announcement_file.create_with_announcement(
        db=db, obj_in=announcement_file_in, announcement_id=announcement_id)
    return announcement_file
