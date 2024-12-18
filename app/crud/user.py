from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.auth import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    # Hash the password before saving the user
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email if hasattr(user, 'email') else None,  # Optional email handling
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
