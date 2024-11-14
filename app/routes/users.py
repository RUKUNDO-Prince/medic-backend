from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import user as models
from app.schemas import user as schemas
from app.utils.auth import get_current_user
from app.utils.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
async def read_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
):
    logger.info(f"Fetching users list. skip={skip}, limit={limit}")
    try:
        users = db.query(models.User).offset(skip).limit(limit).all()
        logger.info(f"Found {len(users)} users")
        return users
    except Exception as e:
        logger.error(f"Failed to fetch users: {str(e)}", exc_info=True)
        raise

@router.get("/{user_id}", response_model=schemas.User)
async def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    logger.info(f"Fetching user with id={user_id}")
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            logger.warning(f"User with id={user_id} not found")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"Found user: {user.username}")
        return user
    except Exception as e:
        logger.error(f"Failed to fetch user with id={user_id}: {str(e)}", exc_info=True)
        raise

# Add other endpoints as needed...