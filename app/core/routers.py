from fastapi import APIRouter

from app.auth import routers as Auth
from app.modules.customers import routers as Customer
from app.modules.docentes import routers as Docente
from app.modules.materias import routers as Materia
from app.modules.products import routers as Product
from app.modules.tasks import routers as Task

router = APIRouter()
# Core
router.include_router(Auth.router, prefix="/auth", tags=["Auth"])
# Modules
router.include_router(Task.router, prefix="/tasks", tags=["Tasks"])
router.include_router(Product.router, prefix="/products", tags=["Products"])
router.include_router(Customer.router, prefix="/customers", tags=["Customers"])
router.include_router(Docente.router, prefix="/docentes", tags=["Docentes"])
router.include_router(Materia.router, prefix="/materias", tags=["Materias"])
