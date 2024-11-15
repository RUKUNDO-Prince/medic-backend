from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import user as models
from app.schemas import user as schemas
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
async def read_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
):
    logger = DatabaseLogger(db)
    logger.info(
        f"Fetching users list",
        user_id=current_user.id,
        method="GET",
        path="/users"
    )
    
    users = db.query(models.User).offset(skip).limit(limit).all()
    
    logger.info(
        f"Found {len(users)} users",
        user_id=current_user.id,
        method="GET",
        path="/users"
    )
    return users

@router.get("/{user_id}", response_model=schemas.User)
async def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    logger = DatabaseLogger(db)
    logger.info(
        f"Fetching user details",
        user_id=current_user.id,
        method="GET",
        path=f"/users/{user_id}"
    )
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        logger.warning(
            f"User not found",
            user_id=current_user.id,
            method="GET",
            path=f"/users/{user_id}"
        )
        raise HTTPException(status_code=404, detail="User not found")
        
    logger.info(
        f"User details retrieved successfully",
        user_id=current_user.id,
        method="GET",
        path=f"/users/{user_id}"
    )
    return user

# Add other endpoints as needed...