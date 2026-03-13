from fastapi import FastAPI,Depends
from typing import Annotated
from database import Engine
import models
from pydantic import BaseModel,Field
from database import session_local
from sqlalchemy.orm import Session
from models import todo



models.Base.metadata.create_all(bind=Engine)
app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close

db_dependency = Annotated[Session,Depends(get_db)]

@app.get("/")
async def get_task(db:db_dependency):
    return db.query(todo).all()
