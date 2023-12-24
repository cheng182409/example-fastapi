from fastapi import FastAPI,APIRouter
from fastapi import HTTPException,status,Depends
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database , schema,models,utils,oauth2

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_credential: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.email==user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=("NO Valid Credential"))
    
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=("NO Valid Credential"))
    
    access_token = oauth2.create_token(data={"user_id":user.id})
    return {"token":access_token, "token_type":"bearer"}
