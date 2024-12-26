from fastapi import APIRouter

from app.api.v1.auth.auth_controller import router as auth_router
from app.api.v1.analises.analise_controller import router as analises_router
from app.api.v1.usuarios.usuario_controller import router as usuarios_router
from app.api.v1.server_remote.server_remote_controller import router as server_remote_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(usuarios_router, prefix="/usuarios", tags=["Usuarios"])
router.include_router(analises_router, prefix="/analises", tags=["Analises"])
router.include_router(server_remote_router, prefix="/server_remote", tags=["Server Remote"])
