from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY:str

    
    # Mapping env file environment variable to these values.
    class Config:
        env_file ="./.env"


settings = Settings()