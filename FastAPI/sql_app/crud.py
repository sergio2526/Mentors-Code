from sqlalchemy.orm import Session

from . import models, schemas


def get_mentoria(db: Session, mentoria_id: int):
    return db.query(models.Mentoria).filter(models.Mentoria.id == mentoria_id).first()


def get_mentorias(db: Session, skip: int = 0):
    return db.query(models.Mentoria).offset(skip).all()


def get_mentoria_by_name(db: Session, name: str):
    return db.query(models.Mentoria).filter(models.Mentoria.name == name).first()


def create_mentoria(db: Session, mentoria: schemas.MentoriaCreate):
    db_mentoria = models.Mentoria(
        name=mentoria.name,
        duration=mentoria.duration,
    )
    db.add(db_mentoria)
    db.commit()
    db.refresh(db_mentoria)
    return db_mentoria


def get_topics(db: Session, skip: int = 0):
    return db.query(models.Topic).offset(skip).all()


def create_mentoria_topic(db: Session, topic: schemas.TopicCreate, mentoria_id: int):
    db_topic = models.Topic(**topic.dict(), owner_id=mentoria_id)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic
