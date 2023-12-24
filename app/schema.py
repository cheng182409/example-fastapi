from typing import Optional

from pydantic import BaseModel, EmailStr
class Post (BaseModel):
    title: str
    content: str
    published: bool = True

class Resp(BaseModel):
        title: str
        content: str
        published: bool

        class Config:
          orm_mode = True

class UserCreate(BaseModel):
     email: EmailStr
     password: str

class UserLogin(BaseModel): 
     email: EmailStr
     password: str

class Token(BaseModel):
     access_token: str
     token_type: str

class TokenData(BaseModel):
     id: Optional[str]=None