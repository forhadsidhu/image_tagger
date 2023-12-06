from typing import Optional, Literal, List
from pydantic import BaseModel, EmailStr
from datetime import datetime


class ResponseText(BaseModel):
    data:str

class tagGenerationOut(BaseModel):
    image_path: str
    image_tags: str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str]


class UserOut(BaseModel):
    id:str
    email:EmailStr
    created_at:datetime

    # For mapping with sqlORM we need this
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email :EmailStr
    password: str
    location: Optional[str]