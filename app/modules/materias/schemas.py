from typing import Optional

from pydantic import BaseModel, Field


class MateriaBase(BaseModel):
    nombre: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    carrera: str = Field(default=None)
    docente_id: Optional[int] = Field(default=None)

class MateriaCreate(MateriaBase):
    pass

class MateriaUpdate(MateriaBase):
    pass

class MateriaRead(MateriaBase):
    id: int

class Materia(MateriaBase):
    id: int

    class Config:
        orm_mode = True
