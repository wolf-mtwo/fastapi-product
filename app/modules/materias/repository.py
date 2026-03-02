from typing import Optional, Sequence

from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.core.repository import BaseRepository
from app.modules.materias.models import Materia

from ..catalog.materias_category.models import MateriaCategory


class MateriaRepository(BaseRepository[Materia]):
    def __init__(self, session: Session):
        super().__init__(session, Materia)

    def get_all_with_relations(
        self, offset: int = 0, limit: int = 100
    ) -> Sequence[Materia]:
        statement = (
            select(Materia)
            .options(selectinload(Materia.category))  # type: ignore
            .options(selectinload(Materia.brand))  # type: ignore
            .offset(offset)
            .limit(limit)
        )
        return self.session.exec(statement).all()

    def get_by_id_with_relations(self, id: int) -> Optional[Materia]:
        statement = (
            select(Materia)
            .where(Materia.id == id)
            .options(selectinload(Materia.category))  # type: ignore
            .options(selectinload(Materia.brand))  # type: ignore
        )
        return self.session.exec(statement).first()

    def check_category_exists(self, category_id: int) -> bool:
        return self.session.get(MateriaCategory, category_id) is not None
