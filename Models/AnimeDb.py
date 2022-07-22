from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class AnimeDb(Base):
    __tablename__ = "Anime"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    description = Column(Text())
    episodes = Column(Integer)
    image = Column(String(120))
    studio = Column(String(100))
    genre = Column(String(100))