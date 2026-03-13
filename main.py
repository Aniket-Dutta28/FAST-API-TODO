from fastapi import FastAPI
from database import Engine
import models


models.Base.metadata.create_all(bind=Engine)
app = FastAPI()

@app.get("/")
async def test_connection():
    return {"message":"Testing Connection"}
