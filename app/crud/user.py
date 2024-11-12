from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_user(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()

def create_user(user: UserCreate, db: Session):
    db_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    return db_user
