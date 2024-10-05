from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    joke_type = Column(String)
    joke = Column(String)
    setup = Column(String)
    delivery = Column(String)
    nsfw = Column(Boolean)
    political = Column(Boolean)
    sexist = Column(Boolean)
    safe = Column(Boolean)
    lang = Column(String)
