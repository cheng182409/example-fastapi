from fastapi import FastAPI,APIRouter
from fastapi import HTTPException,status,Depends,responses
from .. import models,schema,oauth2
from sqlalchemy.orm import Session
from ..database import  get_db

router = APIRouter(
    prefix='/sci',
    tags=['Posts']
)

@router.get("/")

async def root(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()

    return {"message": posts}

@router.get("/sqlalchemy")
def test_sqlalchemy(db: Session = Depends(get_db)):
    return {"status":"good"}


@router.get("/posts/{id}")
def get_posts(id:int,db: Session = Depends(get_db),get_current_user:int = Depends(oauth2.get_current_user)):
    one_post=db.query(models.Post).filter(models.Post.id == id).first()
    if not one_post:
      raise HTTPException (status_code = status.HTTP_404_NOT_FOUND,detail="NOT FOUND")              
    return {"tata": one_post}

@router.post("/posts",response_model=schema.Resp)
def create_posts(payload: schema.Post,db: Session = Depends(get_db)):
    new_post=models.Post(title=payload.title,content=payload.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/posts/{id}")
def delete_post(id:int,db: Session = Depends(get_db)):
    post_query=db.query(models.Post).filter(models.Post.id == id)
    post_query.delete(synchronize_session=False)
    db.commit()
    return {"message":"deleted"}