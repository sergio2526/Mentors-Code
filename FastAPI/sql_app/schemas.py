from typing import List, Optional

from pydantic import BaseModel

class MentoriaBase(BaseModel):
    name: str
    topic: str


class MentoriaCreate(MentoriaBase):
    pass


class Mentoria(MentoriaBase):
    id: int
    state: bool

    class Config:
        orm_mode = True #Configuration Pydantic