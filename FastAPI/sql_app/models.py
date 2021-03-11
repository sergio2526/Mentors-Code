from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Mentoria(Base):
    __tablename__ = "mentorias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    topic = Column(String, index= True)
    state = Column(Boolean, default=True)