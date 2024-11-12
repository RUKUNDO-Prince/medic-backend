from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, Token
from app.crud.user import get_user, create_user
from app.utils.jwt import create_access_token

router = APIRouter()

@router.post("/token", response_model=Token)
async def login(user: UserCreate):
    db_user = get_user(user.username)
    if db_user and verify_password(user.password, db_user.hashed_password):
        access_token = create_access_token(data={"sub": db_user.username})
        return {"access_token": access_token, "token_type": "bearer"}
