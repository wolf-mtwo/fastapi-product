from sqlmodel import Session

from app.core.repository import BaseRepository
from app.modules.materias.models import Materia


class MateriaRepository(BaseRepository[Materia]):
    def __init__(self, session: Session):
        super().__init__(session, Materia)
