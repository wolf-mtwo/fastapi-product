from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator
from sqlmodel import Session, select

from app.core.db import engine

class DocenteBase(BaseModel):
    nombre: str = Field(default=None)
    apellido_paterno: str = Field(default=None)
    apellido_materno: str = Field(default=None)
    ci: int = 0
    email: Optional[str] = Field(default=None)
    celular: str = Field(default=None)
    profesion: str = Field(default=None)

class CustomerCreate(DocenteBase):
    pass


class CustomerUpdate(DocenteBase):
    pass
