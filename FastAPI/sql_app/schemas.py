from datetime import date, time
from typing import List, Optional

from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str
    description: Optional[str] = None


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CalendarBase(BaseModel):
    date: date
    hour: str


class CalenderCreate(CalendarBase):
    pass


class Calender(CalendarBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ComentaryBase(BaseModel):
    comentary: str


class ComentaryCreate(ComentaryBase):
    pass


class Comentary(ComentaryBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class MentoriaBase(BaseModel):
    name: str
    duration: int
    video: str


class MentoriaCreate(MentoriaBase):
    pass


class Mentoria(MentoriaBase):
    id: int
    state: bool
    calender: List[Calender] = []
    topics: List[Topic] = []
    comentary: List[Comentary] = []
    

    class Config:
        orm_mode = True  # Configuration Pydantic
