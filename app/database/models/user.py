from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.models.journey import Journey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String, unique=False, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True, index=True)
    cnpj = Column(String, unique=True, index=True, nullable=True)
    endereco = Column(String, unique=True, index=True, nullable=True)
    telefone = Column(String, unique=True, index=True, nullable=True)
    chave_pix = Column(String, unique=True, index=True, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    reset_pin = Column(String, nullable=True)
    reset_pin_expiration = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    journeys = relationship(Journey, back_populates="user")
