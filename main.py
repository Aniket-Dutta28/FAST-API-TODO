from fastapi import FastAPI,Depends,Path,HTTPException
from typing import Annotated
from database import Engine
import models
from pydantic import BaseModel,Field
from database import session_local
from sqlalchemy.orm import Session
from models import todo
from starlette import status



models.Base.metadata.create_all(bind=Engine)
app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close

db_dependency = Annotated[Session,Depends(get_db)]

class task_request(BaseModel):
    Task : str = Field(min_length=3)
    Description : str = Field(min_length=3,max_length=100)
    Priority : int = Field(gt=0)
    Completed : bool    

@app.get("/task/")
async def get_task(db:db_dependency):
    return db.query(todo).all()

@app.get("/task/{task_id}")
async def task_by_id(db:db_dependency,task_id:int = Path(gt=0)):
    found_task = db.query(todo).filter(task_id == todo.id).first()
    if found_task is not None:
        return found_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/add_task/")
async def add_task(db:db_dependency,task_request:task_request):
    task = todo(**task_request.dict())

    db.add(task)
    db.commit()

@app.put ("/task_update/{task_id}")
async def update_task(db:db_dependency,task_request:task_request,task_id:int = Path(gt=0)):
    task_to_update = db.query(todo).filter(task_id == todo.id).first()
    if task_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    task_to_update.Task = task_request.Task
    task_to_update.Description = task_request.Description
    task_to_update.Priority = task_request.Priority
    task_to_update.Completed = task_request.Completed
    
    db.add(task_to_update)
    db.commit()

@app.delete("/task_delete/{task_id}",status_code=status.HTTP_200_OK)
async def delete_task(db:db_dependency,task_id:int=Path(gt=0)):
    task = db.query(todo).filter(todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    db.query(todo).filter(todo.id == task_id).delete()
    db.commit()