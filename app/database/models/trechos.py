from sqlalchemy import DECIMAL, Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.obras import Obra

class TrechoObra(Base):
    __tablename__ = 'trechosobra'

    id_trecho = Column(Integer, primary_key=True, autoincrement=True)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    nome_trecho = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    tipo_infraestrutura = Column(Enum('TSD', 'TSS', 'CBUQ', 'BLOQUETE', 'CASCALHAMENTO', name="tipo_infraestrutura"), nullable=False)
    orcamento_trecho = Column(DECIMAL(18, 2), nullable=False)
    coordenadas_geograficas = Column(Text, nullable=False)
    situacao_fiscalizacao = Column(Enum(
        'Não fiscalizada', 'Obra em conformidade', 'Não-Conformidades leves', 'Não-Conformidades graves', name="situacao_fiscalizacao_status"
    ), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    obra = relationship('Obra', backref='trechos_obra')
