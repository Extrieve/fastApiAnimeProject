import os
from typing import Optional
from fastapi import FastAPI
from Models import Anime, AnimeDb
from database import engine, SessionLocal
import uvicorn
import random

app = FastAPI()

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"Hello": "World from FastAPI"}

# get random number between min(default:0) and max(default:9)
@app.get("/random/")
def get_random(min: Optional[int] = 0, max: Optional[int] = 9):
    rval = random.randint(min, max)
    return { "value": rval }


@app.get("/anime")
def get_all_anime():
    return {"anime": ["One Piece", "Naruto", "Bleach"]}

if __name__ == "__main__":
    AnimeDb.Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info", reload=True)
