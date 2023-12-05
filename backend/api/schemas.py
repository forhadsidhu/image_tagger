from typing import Optional, Literal, List
from pydantic import BaseModel, EmailStr


class ResponseText(BaseModel):
    data:str



class tagGenerationOut(BaseModel):
    image_path: str
    image_tags: str