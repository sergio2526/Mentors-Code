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

#Mentorias
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

#Temas
@app.post("/temas/{mentoria_id}", response_model=schemas.Topic)
def create_topic_for_mentoria(
    mentoria_id: int, topic: schemas.TopicCreate, db: Session = Depends(get_db)
):
    create_topic = crud.create_mentoria_topic(
        db=db, topic=topic, mentoria_id=mentoria_id
    )
    return create_topic


@app.get("/temas/", response_model=List[schemas.Topic])
def read_topics(skip: int = 0, db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip)
    return topics


@app.get("/tema/{id_mentoria}", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session= Depends(get_db)):
    db_topic = crud.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="El id del tema no existe")
    return db_topic


#Calendario
@app.post("/calendario/{mentoria_id}", response_model=schemas.Calender)
def create_calender_for_mentoria(
    mentoria_id: int, calender: schemas.CalenderCreate, db: Session = Depends(get_db)
):
    create_calender = crud.create_mentoria_calender(
        db=db, calender=calender, mentoria_id=mentoria_id
    )
    return create_calender


@app.get("/calendarios/", response_model=List[schemas.Calender])
def read_calender(skip: int = 0, db: Session = Depends(get_db)):
    calender = crud.get_calenders(db, skip=skip)
    return calender


@app.get("/calendario/{id_mentoria}", response_model=schemas.Calender)
def read_topic(calender_id: int, db: Session= Depends(get_db)):
    db_calender = crud.get_calender(db, calender_id=calender_id)
    if db_calender is None:
        raise HTTPException(status_code=404, detail="El id del calendario no existe")
    return db_calender


#Comentarios
@app.post("/comentarios/{mentoria_id}", response_model=schemas.Comentary)
def create_comentary_for_mentoria(
    mentoria_id: int, comentary: schemas.ComentaryCreate, db: Session = Depends(get_db)
):
    create_comentary = crud.create_mentoria_comentary(
        db=db, comentary=comentary, mentoria_id=mentoria_id
    )
    return create_comentary


@app.get("/comentarios/", response_model=List[schemas.Comentary])
def read_comentary(skip: int = 0, db: Session = Depends(get_db)):
    comentary = crud.get_comentary(db, skip=skip)
    return comentary