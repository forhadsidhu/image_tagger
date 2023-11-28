from typing import Optional, Literal, List
from pydantic import BaseModel, EmailStr


class ResponseText(BaseModel):
    data:str
    