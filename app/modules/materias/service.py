from app.core.exceptions import InternalServerErrorException, NotFoundException
from app.modules.docentes.repository import DocenteRepository

from .models import Materia
from .repository import MateriaRepository
from .schemas import MateriaCreate, MateriaUpdate


class MateriaService:
    no_materia: str = "Materia doesn't exits"

    def __init__(
        self, repository: MateriaRepository, docente_repository: DocenteRepository
    ):
        self.repository = repository
        self.docente_repository = docente_repository

    # CREATE
    # ----------------------
    def create_materia(self, item_data: MateriaCreate):
        # Validate Docente
        if item_data.docente_id:
            if not self.docente_repository.get_by_id(item_data.docente_id):
                raise NotFoundException(
                    detail=f"Docente Id:{item_data.docente_id} doesn't exist"
                )

        materia_db = Materia.model_validate(item_data.model_dump())

        try:
            return self.repository.create(materia_db)
        except Exception as e:
            raise InternalServerErrorException(
                detail="Internal Server error, create Materia"
            ) from e

    # GET ONE
    # ----------------------
    def get_materia(self, item_id: int):
        materia_db = self.repository.get_by_id(item_id)

        if not materia_db:
            raise NotFoundException(detail=self.no_materia)
        return materia_db

    # UPDATE
    # ----------------------
    def update_materia(self, item_id: int, item_data: MateriaUpdate):
        # Validate Docente
        if item_data.docente_id:
            if not self.docente_repository.get_by_id(item_data.docente_id):
                raise NotFoundException(
                    detail=f"Docente Id:{item_data.docente_id} doesn't exist"
                )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        updated_materia = self.repository.update(item_id, item_data_dict)

        if not updated_materia:
            raise NotFoundException(detail=self.no_materia)
        return updated_materia

    # GET ALL PLANS
    # ----------------------
    def get_materias(self, offset: int = 0, limit: int = 100):
        return self.repository.get_all(offset, limit)

    # DELETE
    # ----------------------
    def delete_materia(self, item_id: int):
        success = self.repository.delete(item_id)
        if not success:
            raise NotFoundException(detail=self.no_materia)
        return {"detail": "ok"}
