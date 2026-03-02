from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.core.db import get_session
from app.modules.docentes.repository import DocenteRepository

from .repository import MateriaRepository
from .schemas import MateriaCreate, MateriaRead, MateriaUpdate
from .service import MateriaService

router = APIRouter()


def get_service(session: Session = Depends(get_session)):
    materia_repository = MateriaRepository(session)
    docente_repository = DocenteRepository(session)
    return MateriaService(materia_repository, docente_repository)


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=MateriaRead, status_code=status.HTTP_201_CREATED)
async def create_materia(
    materia_data: MateriaCreate, service: MateriaService = Depends(get_service)
):
    return service.create_materia(materia_data)


# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{materia_id}", response_model=MateriaRead)
async def get_materia(materia_id: int, service: MateriaService = Depends(get_service)):
    return service.get_materia(materia_id)


# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch(
    "/{materia_id}", response_model=MateriaRead, status_code=status.HTTP_200_OK
)
async def update_materia(
    materia_id: int,
    materia_data: MateriaUpdate,
    service: MateriaService = Depends(get_service),
):
    return service.update_materia(materia_id, materia_data)


# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[MateriaRead])
async def get_materias(
    service: MateriaService = Depends(get_service),
    offset: int = 0,
    limit: int = 100,
):
    return service.get_materias(offset, limit)


# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{materia_id}", status_code=status.HTTP_200_OK)
async def delete_materia(
    materia_id: int, service: MateriaService = Depends(get_service)
):
    service.delete_materia(materia_id)
    return {"detail": "ok"}
