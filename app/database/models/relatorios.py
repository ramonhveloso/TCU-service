from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.analises import Analises

class Relatorios(Base):
    __tablename__ = 'relatorios'

    id_relatorio = Column(Integer, primary_key=True, autoincrement=True)
    id_analise = Column(Integer, ForeignKey('analises.id_analise', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_relatorio = Column(Enum('Alerta', 'Indicador', 'Gráfico'), nullable=False)
    caminho_arquivo = Column(Text, nullable=False)
    data_geracao = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
    
    analise = relationship('Analises', backref='relatorios')