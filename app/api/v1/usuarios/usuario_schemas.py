from typing import List, Optional

from pydantic import BaseModel, EmailStr


# Obter perfil do usuário autenticado
class GetUsersMeResponse(BaseModel):
    id: int
    username: Optional[str]
    email: EmailStr
    name: str
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


# Atualizar perfil do usuário autenticado
class PutUsersMeRequest(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PutUsersMeResponse(BaseModel):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    username: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class Usuario(BaseModel):
    id: int
    username: str
    email: EmailStr
    name: str
    is_superuser: bool
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetUsersResponse(BaseModel):
    users: Optional[List[Usuario]] = []

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


# Ver perfil de um usuário específico
class GetUserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    name: str
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


# Atualizar dados de um usuário específico
class PutUserRequest(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    username: Optional[str]
    is_active: Optional[bool] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PutUserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    username: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


# Excluir um usuário específico
class DeleteUserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    username: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    chave_pix: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
