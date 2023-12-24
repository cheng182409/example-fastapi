from .database import Base
from sqlalchemy import Column, Integer,String,Boolean,ForeignKey

class Post(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True,nullable=False)
    title =Column(String,nullable=False)
    content =Column(String,nullable=False)
    published=Column(Boolean,nullable=True,server_default='TRUE')
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

class Users(Base):
    __tablename__ = "users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String, nullable=False,unique=True)
    password = Column(String,nullable=False)