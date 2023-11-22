import json
import requests
from fastapi import status,HTTPException,Depends,APIRouter,UploadFile,File
from typing import List,Optional









router = APIRouter(prefix='/generation',tags=['Generate'])

@router.post("/upload",status_code=status.HTTP_201_CREATED)
def upload(input_file:UploadFile=File(...)):
    
    # Getting input image from client side
    input_image = input_file.read()