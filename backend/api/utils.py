from passlib.context  import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")



# Its one way hashing,hashed the password then verify the plain password and hashed password
def hash(password:str):
    return pwd_context.hash(password)

def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
