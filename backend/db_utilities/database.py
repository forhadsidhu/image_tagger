from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from .config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base




# Connecting database using sqlAlchemy.
DATABASE_URL = f'mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
engine = create_engine(DATABASE_URL,pool_size=20, max_overflow=10)

# Disabling by default characterisitics of database using sessionmaker factory method.
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Use declaritivebase class for converting python class to db table
Base = declarative_base()


# Crate get db function using context manager for memory efficiency and avoiding data leakage.
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()








