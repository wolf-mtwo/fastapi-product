from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.core.db import get_session

from app.auth.permissions import PermissionAction, PermissionChecker
from app.auth.schemas import UserModulePermission
from .repository import DocenteRepository
from .schemas import Docente, DocenteCreate, DocenteRead, DocenteUpdate
from .service import DocenteService

router = APIRouter()


def get_service(session: Session = Depends(get_session)):
    repository = DocenteRepository(session)
    return DocenteService(repository)


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=DocenteRead, status_code=status.HTTP_201_CREATED)
async def create_docente(
    docente_data: DocenteCreate, service: DocenteService = Depends(get_service)
):
    return service.create_docente(docente_data)


# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{docente_id}", response_model=DocenteRead)
async def get_docente(
    docente_id: int,
    service: DocenteService = Depends(get_service),
    _: UserModulePermission = Depends(
        PermissionChecker(
            module_slug="docentes", required_permission=PermissionAction.CREATE
        )
    )
):
    return service.get_docente(docente_id)


# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch(
    "/{docente_id}", response_model=DocenteRead, status_code=status.HTTP_200_OK
)
async def update_docente(
    docente_id: int,
    docente_data: DocenteUpdate,
    service: DocenteService = Depends(get_service),
):
    return service.update_docente(docente_id, docente_data)


# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[DocenteRead])
async def get_docentes(
    service: DocenteService = Depends(get_service),
    offset: int = 0,
    limit: int = 100,
):
    return service.get_docentes(offset, limit)


# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{docente_id}", status_code=status.HTTP_200_OK)
async def delete_docente(
    docente_id: int, service: DocenteService = Depends(get_service)
):
    service.delete_docente(docente_id)
    return {"detail": "ok"}
