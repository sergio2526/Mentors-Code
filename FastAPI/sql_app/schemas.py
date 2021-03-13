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


class MentoriaBase(BaseModel):
    name: str
    duration: int


class MentoriaCreate(MentoriaBase):
    pass


class Mentoria(MentoriaBase):
    id: int
    state: bool
    topics: List[Topic] = []

    class Config:
        orm_mode = True  # Configuration Pydantic
