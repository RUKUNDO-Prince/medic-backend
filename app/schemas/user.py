from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    username: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

