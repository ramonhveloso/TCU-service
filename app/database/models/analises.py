from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.trechos import TrechoObra
from app.database.models.obras import Obra

class Analise(Base):
    __tablename__ = 'analises'

    id_analise = Column(Integer, primary_key=True, autoincrement=True)
    id_trecho = Column(Integer, ForeignKey('trechosobra.id_trecho', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_analise = Column(Enum('Simples', 'Médio', 'Complexo', name="tipo_analise"), nullable=False)
    descricao = Column(Text, nullable=False)
    perguntas = Column(Text, nullable=False)
    comparativo_previsto_realizado = Column(Text, nullable=False)
    conclusao = Column(Enum('Aprovada', 'Irregularidade', name="conclusao_status"), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    trecho = relationship('TechoObra', backref='analises')
    obra = relationship('Obra', backref='analises')
