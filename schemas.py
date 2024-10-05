from pydantic import BaseModel

class JokeBase(BaseModel):
    category: str
    joke_type: str
    joke: str = None
    setup: str = None
    delivery: str = None
    nsfw: bool
    political: bool
    sexist: bool
    safe: bool
    lang: str

    class Config:
        orm_mode = True
