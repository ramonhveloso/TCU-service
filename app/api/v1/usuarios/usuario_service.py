from fastapi import Depends, HTTPException
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
    Usuario,
)
from app.middleware.dependencies import AuthUser


class UsuarioService:
    def __init__(self, user_repository: UsuarioRepository = Depends()):
        self.user_repository = user_repository

    async def get_authenticated_user(
        self, db: Session, authuser: AuthUser
    ) -> GetUsersMeResponse:
        user = await self.user_repository.get_user_by_id(db, authuser.id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario not found")
        return GetUsersMeResponse(
            id=int(user.id),
            username=str(user.username),
            email=str(user.email),
            name=str(user.name),
            cpf=str(user.cpf) if user.cpf else None,
            cnpj=str(user.cnpj) if user.cnpj else None,
            telefone=str(user.telefone) if user.telefone else None,
            endereco=str(user.endereco) if user.endereco else None,
            chave_pix=str(user.chave_pix) if user.chave_pix else None,
        )

    async def update_user_profile(
        self, db: Session, authuser: AuthUser, data: PutUsersMeRequest
    ) -> PutUsersMeResponse:
        user = await self.user_repository.get_user_by_id(db, authuser.id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario not found")

        updated_user = await self.user_repository.update_user_profile(db, user, data)
        return PutUsersMeResponse(
            id=updated_user.id,
            username=updated_user.username,
            email=updated_user.email,
            name=updated_user.name,
            cpf=str(user.cpf) if user.cpf else None,
            cnpj=str(user.cnpj) if user.cnpj else None,
            telefone=str(user.telefone) if user.telefone else None,
            endereco=str(user.endereco) if user.endereco else None,
            chave_pix=str(user.chave_pix) if user.chave_pix else None,
        )

    async def get_all_users(self, db: Session) -> GetUsersResponse:
        users = await self.user_repository.get_all_users(db)
        users_list = [
            Usuario(
                id=user.id,
                email=user.email,
                name=user.name,
                username=user.username,
                is_superuser=user.is_superuser,
                cpf=str(user.cpf) if user.cpf else None,
                cnpj=str(user.cnpj) if user.cnpj else None,
                telefone=str(user.telefone) if user.telefone else None,
                endereco=str(user.endereco) if user.endereco else None,
                chave_pix=str(user.chave_pix) if user.chave_pix else None,
                is_active=user.is_active,
            )
            for user in users
        ]
        return GetUsersResponse(users=users_list)

    async def get_user_by_id(self, db: Session, id_usuario: int) -> GetUserResponse:
        user = await self.user_repository.get_user_by_id(db, id_usuario)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario not found")
        return GetUserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            name=user.name,
            cpf=str(user.cpf) if user.cpf else None,
            cnpj=str(user.cnpj) if user.cnpj else None,
            telefone=str(user.telefone) if user.telefone else None,
            endereco=str(user.endereco) if user.endereco else None,
            chave_pix=str(user.chave_pix) if user.chave_pix else None,
        )

    async def update_user(
        self, db: Session, id_usuario: int, data: PutUserRequest
    ) -> PutUserResponse:
        user = await self.user_repository.get_user_by_id(db, id_usuario)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario not found")

        updated_user = await self.user_repository.update_user(db, user, data)
        return PutUserResponse(
            id=updated_user.id,
            email=updated_user.email,
            name=updated_user.name,
            username=updated_user.username,
            cpf=str(user.cpf) if user.cpf else None,
            cnpj=str(user.cnpj) if user.cnpj else None,
            telefone=str(user.telefone) if user.telefone else None,
            endereco=str(user.endereco) if user.endereco else None,
            chave_pix=str(user.chave_pix) if user.chave_pix else None,
        )

    async def delete_user(self, db: Session, id_usuario: int) -> DeleteUserResponse:
        user = await self.user_repository.get_user_by_id(db, id_usuario)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario not found")

        deleted_user = await self.user_repository.delete_user(db, user)
        return DeleteUserResponse(
            id=deleted_user.id,
            email=deleted_user.email,
            name=deleted_user.name,
            username=deleted_user.username,
            cpf=str(user.cpf) if user.cpf else None,
            cnpj=str(user.cnpj) if user.cnpj else None,
            telefone=str(user.telefone) if user.telefone else None,
            endereco=str(user.endereco) if user.endereco else None,
            chave_pix=str(user.chave_pix) if user.chave_pix else None,
        )

    async def verify_is_superuser(self, db: Session, id_usuario: int) -> None:
        user = await self.user_repository.get_user_by_id(db, id_usuario)
        if not user or not user.is_superuser:
            raise HTTPException(
                status_code=403 if user else 404,
                detail="Usuario not found" if not user else "Usuario is not a superuser",
            )
