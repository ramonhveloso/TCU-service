from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.trechos import TrechoObra

class ElementoInfraestrutura(Base):
    __tablename__ = 'elementos_insfraestrutura'

    id_elemento = Column(Integer, primary_key=True, autoincrement=True)
    id_trecho = Column(Integer, ForeignKey('trechosobra.id_trecho', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_elemento = Column(Enum('Calçada', 'Meio-fio', 'Placa de Sinalização', 'Pintura', 'Boca de Lobo', 'Rampa', name="tipo_elemento"), nullable=False)
    descricao = Column(Text, nullable=False)
    dimensoes = Column(Text, nullable=False)
    material = Column(String(255), nullable=False)
    condicao_prevista = Column(Enum('Novo', 'Reciclado', name="condicao_status"), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    trecho = relationship('TrechoObra', backref='elementos_infraestrutura')
