from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.analises import Analise

class SubAnaliseRisco(Base):
    __tablename__ = 'subanalisesriscos'

    id_subanalise = Column(Integer, primary_key=True, autoincrement=True)
    id_analise = Column(Integer, ForeignKey('analises.id_analise', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_risco = Column(String(255), nullable=False)
    descricao_detalhada = Column(Text, nullable=False)
    resultado = Column(Enum('Atendido', 'Não Atendido', name="resultado_status"), nullable=False)
    evidencias = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
    
    analise = relationship('Analise', backref='sub_analises')