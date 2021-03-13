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
def read_mentorias(skip: int = 0, db: Session = Depends(get_db)):
    mentorias = crud.get_mentorias(db, skip=skip)
    return mentorias


@app.get("/mentoria/{id}", response_model=schemas.Mentoria)
def read_mentoria(mentoria_id: int, db: Session = Depends(get_db)):
    db_mentoria = crud.get_mentoria(db, mentoria_id=mentoria_id)
    if db_mentoria is None:
        raise HTTPException(status_code=404, detail="La mentoria no existe")
    return db_mentoria


@app.post("/mentorias/{mentoria_id}/topics/", response_model=schemas.Topic)
def create_topic_for_mentoria(
    mentoria_id: int, topic: schemas.TopicCreate, db: Session = Depends(get_db)
):
    create_mentoria = crud.create_mentoria_topic(
        db=db, topic=topic, mentoria_id=mentoria_id
    )
    return create_mentoria


@app.get("/topics/", response_model=List[schemas.Topic])
def read_topics(skip: int = 0, db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip)
    return topics
