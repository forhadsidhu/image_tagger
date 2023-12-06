from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from .. import schemas
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from  db_utilities.database import get_db
from  db_utilities import models
from .. import utils
from .. import oauth2

router = APIRouter(tags=["Authentication"])



@router.post("/login",response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    
    # Creating bearer token here.
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")

    if not utils.verify(user_credentials.password ,user.password):
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail=f'invalid credentials')
    
    access_token = oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"username":user.full_name,"token_type":"bearer"}

