from typing import Optional

from pydantic import BaseModel, Field


class DocenteBase(BaseModel):
    nombre: str = Field(default=None)
    apellido_paterno: str = Field(default=None)
    apellido_materno: str = Field(default=None)
    ci: int = 0
    email: Optional[str] = Field(default=None)
    celular: str = Field(default=None)
    profesion: str = Field(default=None)


class DocenteCreate(DocenteBase):
    pass


class DocenteUpdate(DocenteBase):
    pass


class DocenteRead(DocenteBase):
    id: int


class Docente(DocenteBase):
    id: int

    class Config:
        orm_mode = True
