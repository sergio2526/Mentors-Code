from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Mentoria(Base):
    __tablename__ = "mentorias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True)
    duration = Column(Integer, index=True)
    state = Column(Boolean, default=False)
    video = Column(String(128), index= True)

    topics = relationship("Topic", back_populates="owner")
    calender = relationship("Calender", back_populates="owner")
    comentary = relationship("Comentary", back_populates="owner")


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    description = Column(String(254), index=True)
    owner_id = Column(Integer, ForeignKey("mentorias.id"))

    owner = relationship("Mentoria", back_populates="topics")


class Calender(Base):
    __tablename__ = "calender"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index= True)
    hour = Column(String(45), index=True)
    owner_id = Column(Integer, ForeignKey("mentorias.id"))

    owner = relationship("Mentoria", back_populates="calender")


class Comentary(Base):
    __tablename__ = "comentary"

    id = Column(Integer, primary_key=True, index=True)
    comentary = Column(String(256), index=True)
    owner_id = Column(Integer, ForeignKey("mentorias.id"))

    owner = relationship("Mentoria", back_populates="comentary")