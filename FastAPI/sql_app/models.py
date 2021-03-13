from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Mentoria(Base):
    __tablename__ = "mentorias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    duration = Column(Integer, index=True)
    state = Column(Boolean, default=False)

    topics = relationship("Topic", back_populates="owner")


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("mentorias.id"))

    owner = relationship("Mentoria", back_populates="topics")
