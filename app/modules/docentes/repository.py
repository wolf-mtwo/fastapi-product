from sqlmodel import Session

from app.core.repository import BaseRepository
from app.modules.docentes.models import Docente


class DocenteRepository(BaseRepository[Docente]):
    def __init__(self, session: Session):
        super().__init__(session, Docente)
