from sqlalchemy.orm import Session

from . import models, schemas


def get_mentoria(db: Session, mentoria_id: int):
    return db.query(models.Mentoria).filter(models.Mentoria.id == mentoria_id).first()

def get_mentorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mentoria).offset(skip).limit(limit).all()

def get_mentoria_by_name(db: Session, name: str):
    return db.query(models.Mentoria).filter(models.Mentoria.name == name).first()


def create_mentoria(db: Session, mentoria: schemas.MentoriaCreate):
    db_mentoria = models.Mentoria(name=mentoria.name, topic=mentoria.topic)
    db.add(db_mentoria)
    db.commit()
    db.refresh(db_mentoria)
    return db_mentoria