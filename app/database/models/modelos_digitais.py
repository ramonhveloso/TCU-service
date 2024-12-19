from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.trechos import TrechosObra
from app.database.models.obras import Obras

class ModelosDigitais(Base):
    __tablename__ = 'modelosdigitais'

    id_modelo = Column(Integer, primary_key=True, autoincrement=True)
    id_trecho = Column(Integer, ForeignKey('trechosobra.id_trecho', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    TipoModelo = Column(Enum('Nuvem de Pontos', 'Modelo 3D'), nullable=False)
    CaminhoArquivo = Column(Text, nullable=False)
    DataGeracao = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    trecho = relationship('TrechosObra', backref='modelos_digitais')
    obra = relationship('Obras', backref='modelos_digitais')