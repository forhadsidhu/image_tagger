from datetime import datetime,timedelta
from db_utilities.config import settings
from jose import JWSError,jwt
from . import schemas
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db_utilities import models,database


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Symmetrci encryption used here as for encoding and decoding same key is used here.
def create_access_token(data: dict):

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

# Verify the access token 
def verify_access_token(token:str,credentials_exceptions):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id = payload.get("user_id")
        if id is None:
            raise credentials_exceptions
        token_data = schemas.TokenData(id)
    except JWSError:
        raise credentials_exceptions
    return token_data


# Get the current user everytime for the seek of authentication
def get_current_user(token:str = Depends(oauth_scheme),db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate the credentials",headers={"WWW-Authenticate":"Bearer"})
    
    token = verify_access_token(token=token,credentials_exceptions=credentials_exception)
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
    return user