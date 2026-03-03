from typing import TYPE_CHECKING, Optional

from sqlmodel import Field

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    pass


class Materia(BaseModel, table=True):
    """
    Materia model that represents a materia in the database.
    """

    __tablename__ = "materia"
    nombre: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    carrera: str = Field(default=None)

    docente_id: Optional[int] = Field(default=None, foreign_key="docente.id")
    # category: Optional["MateriaCategory"] = Relationship(back_populates="materias")

    # brand_id: Optional[int] = Field(default=None, foreign_key="materia_brand.id")
    # brand: Optional["MateriaBrand"] = Relationship(back_populates="materias")

    # created_at: Optional[datetime] = Field(
    #     default_factory=get_current_time,
    #     sa_column=Column(DateTime(timezone=False), nullable=True),
    #     description="The timestamp when the data was created",
    # )
    # updated_at: Optional[datetime] = Field(
    #     default=None,
    #     sa_column=Column(
    #         DateTime(timezone=False), onupdate=get_current_time, nullable=True
    #     ),
    #     description="The timestamp when the data was last updated",
    # )
