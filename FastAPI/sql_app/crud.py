from sqlalchemy.orm import Session

from . import models, schemas

#Consulta mentoria por id
def get_mentoria(db: Session, mentoria_id: int):
    return db.query(models.Mentoria).filter(models.Mentoria.id == mentoria_id).first()


#Consulta todas las mentorias
def get_mentorias(db: Session, skip: int = 0):
    return db.query(models.Mentoria).offset(skip).all()


#Consulta mentorias por nombre
def get_mentoria_by_name(db: Session, name: str):
    return db.query(models.Mentoria).filter(models.Mentoria.name == name).first()


#Creando mentoria
def create_mentoria(db: Session, mentoria: schemas.MentoriaCreate):
    db_mentoria = models.Mentoria(
        name=mentoria.name,
        duration=mentoria.duration,
        video=mentoria.video
    )
    db.add(db_mentoria)
    db.commit()
    db.refresh(db_mentoria)
    return db_mentoria


#Consulta temas por mentoria
def get_topic_by_mentoria(db: Session, id_mentoria: int):
    return db.query(models.Topic).filter(models.Topic.owner_id == id_mentoria).all()


#Consulta todos los temas
def get_topics(db: Session, skip: int = 0):
    return db.query(models.Topic).offset(skip).all()


#Creando tema
def create_mentoria_topic(db: Session, topic: schemas.TopicCreate, mentoria_id: int):
    db_topic = models.Topic(**topic.dict(), owner_id=mentoria_id)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic


#Consulta calendarios por mentorias
def get_calender_by_mentoria(db: Session, id_mentoria: int):
    return db.query(models.Calender).filter(models.Calender.owner_id == id_mentoria).all()


#Consulta Obteniendo todos los calendarios
def get_calenders(db: Session, skip: int = 0):
    return db.query(models.Calender).offset(skip).all()


#Creando calendario
def create_mentoria_calender(db: Session, calender: schemas.CalenderCreate, mentoria_id: int):
    db_calender = models.Calender(**calender.dict(), owner_id=mentoria_id)
    db.add(db_calender)
    db.commit()
    db.refresh(db_calender)
    return db_calender


#Consulta Obteniendo todos los comentarios
def get_comentary(db: Session, skip: int = 0):
    return db.query(models.Comentary).offset(skip).all()


#Creando comentarios
def create_mentoria_comentary(db: Session, comentary: schemas.ComentaryCreate, mentoria_id: int):
    db_comentary = models.Comentary(**comentary.dict(), owner_id=mentoria_id)
    db.add(db_comentary)
    db.commit()
    db.refresh(db_comentary)
    return db_comentary


#Consulta calendarios por mentorias
def get_comentary_by_mentoria(db: Session, id_mentoria: int):
    return db.query(models.Comentary).filter(models.Comentary.owner_id == id_mentoria).all()

