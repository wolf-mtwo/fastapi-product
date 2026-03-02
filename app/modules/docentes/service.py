from app.core.exceptions import InternalServerErrorException, NotFoundException

from .models import Docente
from .repository import DocenteRepository
from .schemas import DocenteCreate, DocenteUpdate


class DocenteService:
    no_docente: str = "Docente doesn't exits"

    def __init__(self, repository: DocenteRepository):
        self.repository = repository

    # CREATE
    # ----------------------
    def create_docente(self, item_data: DocenteCreate):
        docente_db = Docente.model_validate(item_data.model_dump())

        try:
            return self.repository.create(docente_db)
        except Exception as e:
            raise InternalServerErrorException(
                detail="Internal Server error, create Docente"
            ) from e

    # GET ONE
    # ----------------------
    def get_docente(self, item_id: int):
        docente_db = self.repository.get_by_id(item_id)

        if not docente_db:
            raise NotFoundException(detail=self.no_docente)
        return docente_db

    # UPDATE
    # ----------------------
    def update_docente(self, item_id: int, item_data: DocenteUpdate):
        item_data_dict = item_data.model_dump(exclude_unset=True)
        updated_docente = self.repository.update(item_id, item_data_dict)

        if not updated_docente:
            raise NotFoundException(detail=self.no_docente)
        return updated_docente

    # GET ALL PLANS
    # ----------------------
    def get_docentes(self, offset: int = 0, limit: int = 100):
        return self.repository.get_all(offset, limit)

    # DELETE
    # ----------------------
    def delete_docente(self, item_id: int):
        success = self.repository.delete(item_id)
        if not success:
            raise NotFoundException(detail=self.no_docente)
        return {"detail": "ok"}
