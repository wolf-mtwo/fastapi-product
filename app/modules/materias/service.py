from app.core.exceptions import InternalServerErrorException, NotFoundException

from .models import Materia
from .repository import MateriaRepository
from .schemas import MateriaCreate, MateriaUpdate


class MateriaService:
    no_materia: str = "Materia doesn't exits"

    def __init__(self, repository: MateriaRepository):
        self.repository = repository

    # CREATE
    # ----------------------
    def create_materia(self, item_data: MateriaCreate):
        # Validate Category
        if item_data.category_id:
            if not self.repository.check_category_exists(item_data.category_id):
                raise NotFoundException(
                    detail=f"Category Id:{item_data.category_id} doesn't exist"
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
        materia_db = self.repository.get_by_id_with_relations(item_id)

        if not materia_db:
            raise NotFoundException(detail=self.no_materia)
        return materia_db

    # UPDATE
    # ----------------------
    def update_materia(self, item_id: int, item_data: MateriaUpdate):
        item_data_dict = item_data.model_dump(exclude_unset=True)
        updated_materia = self.repository.update(item_id, item_data_dict)

        if not updated_materia:
            raise NotFoundException(detail=self.no_materia)
        return updated_materia

    # GET ALL PLANS
    # ----------------------
    def get_materias(self, offset: int = 0, limit: int = 100):
        return self.repository.get_all_with_relations(offset, limit)

    # DELETE
    # ----------------------
    def delete_materia(self, item_id: int):
        success = self.repository.delete(item_id)
        if not success:
            raise NotFoundException(detail=self.no_materia)
        return {"detail": "ok"}
