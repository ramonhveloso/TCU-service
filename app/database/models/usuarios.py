from sqlalchemy import Column, DateTime, Integer, String, Text, Enum, func
from app.database.base import Base

    
class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    usuario = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    senha = Column(Text, nullable=False)
    papel = Column(Enum('Admin', 'Operador', 'Consultor', name="papel_cargo"), nullable=False)
    certificacoes = Column(Text, nullable=False)
    status = Column(String(15), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    ultimo_registro = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
