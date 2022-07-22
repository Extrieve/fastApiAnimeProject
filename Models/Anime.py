from pydantic import BaseModel

class Anime(BaseModel):
    id: int
    name: str
    description: str
    episodes: int
    rating: float
    image: str
    studio: str
    genre: str

    class Config:
        orm_mode = True
        