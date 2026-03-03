from typing import Optional

from sqlmodel import Field

from app.models.base_model import BaseModel


class Docente(BaseModel, table=True):
    """
    Docente model that represents a docente in the database.
    """

    __tablename__ = "docente"
    nombre: str = Field(default=None)
    apellido_paterno: str = Field(default=None)
    apellido_materno: str = Field(default=None)
    ci: int = 0
    email: Optional[str] = Field(default=None)
    celular: str = Field(default=None)
    profesion: str = Field(default=None)

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
