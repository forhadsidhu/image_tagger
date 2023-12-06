from sqlalchemy import Column,ForeignKey,Integer,String,Boolean,TIMESTAMP,text,JSON,Computed,Text
from sqlalchemy.orm import relationship,column_property
from sqlalchemy.sql.expression import cast
from .database import Base






class ImageResponse(Base):
    __tablename__ = 'generated_image_tags'

    # Columns for storing image tags.
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("NOW()"))
    image_path = Column(String(1000),nullable=False)
    image_tags = Column(String(1000),nullable=False)


class Users(Base):
    __tablename__ = 'app_users'

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String(1000),nullable=False,unique=True)
    password = Column(String(1000),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("NOW()"))
    location = Column(String(1000),nullable=False,default="BD")
    user_type = Column(String(1000),nullable=False,default="User")