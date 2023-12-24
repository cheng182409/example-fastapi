from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException,status,Depends
from fastapi.params import Body
from pydantic import BaseModel
from . import models,schema,utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post,users,auth
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins=["https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)




