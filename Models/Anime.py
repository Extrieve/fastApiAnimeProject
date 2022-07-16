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


class Manga(BaseModel):
    id: int
    name: str
    description: str
    chapters: int
    volumes: int
    rating: float
    image: str
    studio: str
    genre: str


class Character(BaseModel):
    id: int
    name: str
    description: str
    image: str
    anime: str
    manga: str


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    anime: str
    manga: str
    characters: str

