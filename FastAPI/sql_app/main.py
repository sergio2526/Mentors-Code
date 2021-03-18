from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependencia 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Creando mentoria
@app.post("/mentorias/", response_model=schemas.Mentoria)
def create_mentoria(mentoria: schemas.MentoriaCreate, db: Session = Depends(get_db)):
    db_mentoria = crud.get_mentoria_by_name(db, name=mentoria.name)
    return crud.create_mentoria(db=db, mentoria=mentoria)


#Obteniendo todas las mentorias registradas
@app.get("/mentorias/", response_model=List[schemas.Mentoria])
def read_mentorias(skip: int = 0, db: Session = Depends(get_db)):
    mentorias = crud.get_mentorias(db, skip=skip)
    return mentorias


#Obteniendo mentoria por id
@app.get("/mentorias/{id}", response_model=schemas.Mentoria)
def read_mentoria(mentoria_id: int, db: Session = Depends(get_db)):
    db_mentoria = crud.get_mentoria(db, mentoria_id=mentoria_id)
    if db_mentoria is None:
        raise HTTPException(status_code=404, detail="La mentoria no existe")
    return db_mentoria


#Creando temas por id de mentoria
@app.post("/temas/{id_mentoria}", response_model=schemas.Topic)
def create_topic_by_mentoria(
    mentoria_id: int, topic: schemas.TopicCreate, db: Session = Depends(get_db)
):
    create_topic = crud.create_mentoria_topic(
        db=db, topic=topic, mentoria_id=mentoria_id
    )
    return create_topic


#Obteniendo todas los temas registrados
@app.get("/temas/", response_model=List[schemas.Topic])
def read_topics(skip: int = 0, db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip)
    return topics


#Obteniendo temas por id de mentoria
@app.get("/temas/{id_mentoria}", response_model=List[schemas.Topic])
def read_topic_by_mentoria(id_mentoria: int, db: Session= Depends(get_db)):
    db_topic = crud.get_topic_by_mentoria(db, id_mentoria=id_mentoria)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="El id del tema no existe")
    return db_topic


#Creando los calendarios relacionados al id mentoria
@app.post("/calendarios/{id_mentoria}", response_model=schemas.Calender)
def create_calender_by_mentoria(
    mentoria_id: int, calender: schemas.CalenderCreate, db: Session = Depends(get_db)
):
    create_calender = crud.create_mentoria_calender(
        db=db, calender=calender, mentoria_id=mentoria_id
    )
    return create_calender


#Obteniendo todos los calendarios
@app.get("/calendarios/", response_model=List[schemas.Calender])
def read_calender(skip: int = 0, db: Session = Depends(get_db)):
    calender = crud.get_calenders(db, skip=skip)
    return calender


#Obteniendo calendarios por id mentoria
@app.get("/calendarios/{id_mentoria}", response_model = List[schemas.Calender])
def read_calender_by_mentoria(id_mentoria: int, db: Session = Depends(get_db)):
    db_calender = crud.get_calender_by_mentoria(db, id_mentoria = id_mentoria)
    if db_calender is None:
        raise HTTPException(status_code = 404, detail = "El id del calendario no existe")
    return db_calender


#Creando comentarios por id de mentoria
@app.post("/comentarios/{id_mentoria}", response_model = schemas.Comentary)
def create_comentary_by_mentoria(
    mentoria_id: int, comentary: schemas.ComentaryCreate, db: Session = Depends(get_db)
):
    create_comentary = crud.create_mentoria_comentary(
        db = db, comentary = comentary, mentoria_id = mentoria_id
    )
    return create_comentary


#Obteniendo todos los comentarios
@app.get("/comentarios/", response_model = List[schemas.Comentary])
def read_comentary(skip: int = 0, db: Session = Depends(get_db)):
    comentary = crud.get_comentary(db, skip = skip)
    return comentary


#Obteniendo comenatarios por id de mentoria
@app.get("/comentarios/{id_mentoria}", response_model = List[schemas.Comentary])
def read_comentary_by_mentoria(id_mentoria: int, db: Session = Depends(get_db)):
    db_comentary = crud.get_comentary_by_mentoria(db, id_mentoria = id_mentoria)
    if db_comentary is None:
        raise HTTPException(status_code = 404, detail = "El id de la mentoria no existe")
    return db_comentary