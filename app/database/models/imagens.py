from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.planejamento_visitas import PlanejamentoVisita

class Imagem(Base):
    __tablename__ = 'imagens'

    id_imagem = Column(Integer, primary_key=True, autoincrement=True)
    id_visita = Column(Integer, ForeignKey('planejamentovisitas.id_visita', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_imagem = Column(Enum('Aérea', 'Solo', 'Gêmeo Digital', name="tipo_imagem"), nullable=False)
    formato = Column(Enum('JPG', 'TIF', 'PNG', name="formato_status"), nullable=False)
    caminho_arquivo = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
    
    visita = relationship('PlanejamentoVisita', backref='imagens')
