from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database config
DATABASE_URL = "postgresql://username:password@127.0.0.1:8000/userdriventube"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class Suggestion(Base):
    __tablename__ = "suggestions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    votes = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)

# Pydantic schemas
class SuggestionSchema(BaseModel):
    title: str
    votes: int = 0

    class Config:
        orm_mode = True

# App
app = FastAPI()

@app.get("/suggestions")
def get_suggestions():
    db = SessionLocal()
    suggestions = db.query(Suggestion).all()
    db.close()
    return suggestions

@app.post("/suggestions")
def add_suggestion(s: SuggestionSchema):
    db = SessionLocal()
    new_s = Suggestion(title=s.title, votes=s.votes)
    db.add(new_s)
    db.commit()
    db.refresh(new_s)
    db.close()
    return new_s

@app.post("/suggestions/{id}/vote")
def vote_suggestion(id: int):
    db = SessionLocal()
    suggestion = db.query(Suggestion).filter(Suggestion.id == id).first()
    if not suggestion:
        db.close()
        raise HTTPException(status_code=404, detail="Suggestion not found")
    suggestion.votes += 1
    db.commit()
    db.refresh(suggestion)
    db.close()
    return suggestion
