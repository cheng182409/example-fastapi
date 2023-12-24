from fastapi import FastAPI,APIRouter
from fastapi import HTTPException,status,Depends
from .. import models,schema,utils
from sqlalchemy.orm import Session
from ..database import  get_db

router = APIRouter(

    tags=['Users']
)

@router.post("/users")
def create_users(payload: schema.UserCreate,db: Session = Depends(get_db)):
    hased_pw=utils.pwd_context.hash(payload.password)
    payload.password=hased_pw
    new_user=models.Users(** payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user