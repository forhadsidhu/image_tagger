from sqlalchemy.orm import Session
from fastapi import status,HTTPException, Depends,APIRouter
from api import schemas,utils
from db_utilities.database import get_db
from db_utilities import models

router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db:Session = Depends(get_db)):

    # Check if user exists here
    db_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if db_user is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"User with email alrady registered")
    
    # hash the password
    user.password= utils.hash(user.password)

    #unpacking the dict and passing it as parameter
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
