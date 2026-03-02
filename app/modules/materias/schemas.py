from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator
from sqlmodel import Session, select

from app.core.db import engine

from ..catalog.materias_brand.models import MateriaBrand
from ..catalog.materias_brand.schemas import MateriaBrandRead
from ..catalog.materias_category.schemas import MateriaCategoryRead


class MateriaBase(BaseModel):
    title: str | None = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None


# Modelo para crear una nueva tarea (hereda de TaskBase)
class MateriaCreate(MateriaBase):
    category_id: Optional[int] = None
    brand_id: Optional[int] = None

    @field_validator("brand_id")
    @classmethod
    def validate_brand(cls, value):
        session = Session(engine)
        query = select(MateriaBrand).where(MateriaBrand.id == value)
        result = session.exec(query).first()
        if not result:
            raise ValueError(f"Brand Id:{value} doesn't exist")
        return value


class MateriaUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None


class MateriaRead(MateriaBase):
    id: int = Field(description="The primary key")
    created_at: Optional[datetime] = Field(
        None, description="The timestamp when the data was created"
    )
    category: Optional[MateriaCategoryRead] = None  # Relación con la categoría
    brand: Optional[MateriaBrandRead] = None  # Relación con la categoría
    model_config = {"from_attributes": True}
