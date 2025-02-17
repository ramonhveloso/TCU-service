from datetime import datetime

from sqlalchemy.orm import Session

from app.api.v1.usuarios.usuario_schemas import PutUserRequest, PutUsersMeRequest
from app.database.models.usuarios import Usuario


class UsuarioRepository:
    async def get_user_by_id(self, db: Session, id_usuario: int):
        """Obtém o usuário pelo ID."""
        return (
            db.query(Usuario).filter(Usuario.id == id_usuario, Usuario.deleted_at == None).first()
        )

    async def get_user_by_email(self, db: Session, email: str):
        """Obtém o usuário pelo email."""
        return (
            db.query(Usuario).filter(Usuario.email == email, Usuario.deleted_at == None).first()
        )

    async def update_user_profile(
        self, db: Session, user: Usuario, data: PutUsersMeRequest
    ):
        """Atualiza o perfil do usuário autenticado."""
        user.name = data.name if data.name else user.name  # type: ignore
        user.email = data.email if data.email else user.email  # type: ignore
        user.username = data.username if data.username else user.username  # type: ignore
        user.is_active = data.is_active if data.is_active else user.is_active  # type: ignore
        user.cpf = data.cpf if data.cpf else user.cpf  # type: ignore
        user.cnpj = data.cnpj if data.cnpj else user.cnpj  # type: ignore
        user.telefone = data.telefone if data.telefone else user.telefone  # type: ignore
        user.endereco = data.endereco if data.endereco else user.endereco  # type: ignore
        user.chave_pix = data.chave_pix if data.chave_pix else user.chave_pix  # type: ignore

        db.commit()
        db.refresh(user)
        return user

    async def update_user(self, db: Session, user: Usuario, data: PutUserRequest):
        """Atualiza os dados de um usuário específico."""
        user.name = data.name if data.name else user.name  # type: ignore
        user.email = data.email if data.email else user.email  # type: ignore
        user.username = data.username if data.username else user.username  # type: ignore
        user.is_active = data.is_active if data.is_active else user.is_active  # type: ignore
        user.cpf = data.cpf if data.cpf else user.cpf  # type: ignore
        user.cnpj = data.cnpj if data.cnpj else user.cnpj  # type: ignore
        user.telefone = data.telefone if data.telefone else user.telefone  # type: ignore
        user.endereco = data.endereco if data.endereco else user.endereco  # type: ignore
        user.chave_pix = data.chave_pix if data.chave_pix else user.chave_pix  # type: ignore
        db.commit()
        db.refresh(user)
        return user

    async def delete_user(self, db: Session, user: Usuario):
        """Exclui um usuário do banco de dados."""
        user.deleted_at = datetime.now()  # type: ignore
        user.last_modified = datetime.now()  # type: ignore
        # db.delete(user)
        db.commit()
        return user

    async def get_all_users(self, db: Session):
        """Retorna todos os usuários no banco de dados."""
        return db.query(Usuario).all()
