from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from app.api.v1.usuarios.usuario_repository import UsuarioRepository
from app.api.v1.usuarios.usuario_schemas import (
    DeleteUserResponse,
    GetUserResponse,
    GetUsersMeResponse,
    GetUsersResponse,
    PutUserRequest,
    PutUserResponse,
    PutUsersMeRequest,
    PutUsersMeResponse,
)
from app.api.v1.usuarios.usuario_service import UsuarioService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
user_service = UsuarioService(UsuarioRepository())


# Obter perfil do usuário autenticado
@router.get("/me")
async def get_users_me(
    authuser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetUsersMeResponse:
    response_service = await user_service.get_authenticated_user(
        db=db, authuser=authuser
    )
    return GetUsersMeResponse.model_validate(response_service)


# Atualizar perfil do usuário autenticado
@router.put("/me")
async def put_users_me(
    data: PutUsersMeRequest,
    authuser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> PutUsersMeResponse:
    response_service = await user_service.update_user_profile(
        db=db, authuser=authuser, data=data
    )
    return PutUsersMeResponse.model_validate(response_service)


# (Admin) Listar usuários
@router.get("/")
async def get_users(
    authuser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetUsersResponse:
    response_service = await user_service.get_all_users(db)
    return GetUsersResponse.model_validate(response_service)


# Ver perfil de um usuário específico
@router.get("/{id_usuario}")
async def get_user(
    authuser: Annotated[AuthUser, Security(jwt_middleware)],
    id_usuario: int,
    db: Session = Depends(get_db),
) -> GetUserResponse:
    response_service = await user_service.get_user_by_id(db=db, id_usuario=id_usuario)
    if not response_service:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return GetUserResponse.model_validate(response_service)


# Atualizar dados de um usuário específico
@router.put("/{id_usuario}")
async def put_user(
    authuser: Annotated[AuthUser, Security(jwt_middleware)],
    data: PutUserRequest,
    id_usuario: int,
    db: Session = Depends(get_db),
) -> PutUserResponse:
    response_service = await user_service.update_user(db=db, id_usuario=id_usuario, data=data)
    return PutUserResponse.model_validate(response_service)


# Excluir um usuário específico
@router.delete("/{id_usuario}")
async def delete_user(
    authuser: Annotated[AuthUser, Security(jwt_middleware)],
    id_usuario: int,
    db: Session = Depends(get_db),
) -> DeleteUserResponse:
    response_service = await user_service.delete_user(db=db, id_usuario=id_usuario)
    if not response_service:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return DeleteUserResponse.model_validate(response_service)
