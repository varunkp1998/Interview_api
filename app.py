from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Joke
from schemas import JokeBase
from joke_fetcher import fetch_jokes

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database
@app.on_event("startup")
async def startup_event():
    init_db()

# Process the jokes and store them in the database
def process_and_store_jokes(jokes, db: Session):
    for joke in jokes:
        joke_data = {
            "category": joke["category"],
            "joke_type": joke["type"],
            "joke": joke.get("joke"),
            "setup": joke.get("setup"),
            "delivery": joke.get("delivery"),
            "nsfw": joke["flags"]["nsfw"],
            "political": joke["flags"]["political"],
            "sexist": joke["flags"]["sexist"],
            "safe": joke["safe"],
            "lang": joke["lang"]
        }

        joke_obj = Joke(**joke_data)
        db.add(joke_obj)
    db.commit()

@app.post("/fetch-jokes/")
async def fetch_and_store_jokes(db: Session = Depends(get_db)):
    jokes = await fetch_jokes()
    if jokes:
        process_and_store_jokes(jokes, db)
        return {"message": "Jokes fetched and stored successfully"}
    return {"message": "Failed to fetch jokes"}

@app.get("/jokes/", response_model=list[JokeBase])
def get_jokes(db: Session = Depends(get_db)):
    jokes = db.query(Joke).all()
    return jokes
