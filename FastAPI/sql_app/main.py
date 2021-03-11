from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/mentorias/", response_model=schemas.Mentoria)
def create_mentoria(mentoria: schemas.MentoriaCreate, db: Session = Depends(get_db)):
    db_mentoria = crud.get_mentoria_by_name(db, name=mentoria.name)
    return crud.create_mentoria(db=db, mentoria=mentoria)


@app.get("/mentorias/", response_model=List[schemas.Mentoria])
def read_mentroias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mentorias = crud.get_mentorias(db, skip=skip, limit=limit)
    return mentorias


@app.get("/mentoria/{id}", response_model=schemas.Mentoria)
def read_mentoria(mentoria_id: int, db: Session = Depends(get_db)):
    db_mentoria = crud.get_mentoria(db, mentoria_id=mentoria_id)
    if db_mentoria is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_mentoria

