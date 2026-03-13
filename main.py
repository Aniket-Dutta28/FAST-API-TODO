from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test_connection():
    return {"message":"Testing Connection"}
