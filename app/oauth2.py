from jose import JWTError, jwt
from datetime import datetime,timedelta
from . import schema
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secrete_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    coded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return coded_jwt

def verify_access_token(token:str, credential_exception):
#    try:
         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
         id:str = payload.get("user_id")
         print(id)

         if id is None:
             raise credential_exception
         token_data = schema.TokenData(id= str(id))
         return token_data
 #   except JWTError:
#        raise credential_exception


 #   return token_data  

def get_current_user(token:str=Depends(oauth2_schema)):


    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"non authorizaton")
    return verify_access_token(token,credential_exception)
