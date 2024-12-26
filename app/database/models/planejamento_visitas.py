from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.trechos import TrechoObra
from app.database.models.obras import Obra

class PlanejamentoVisita(Base):
    __tablename__ = 'planejamentovisitas'

    id_visita = Column(Integer, primary_key=True, autoincrement=True)
    id_trecho = Column(Integer, ForeignKey('trechosobra.id_trecho', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    data_planejada = Column(Date, nullable=False)
    responsavel = Column(String(255), nullable=False)
    objetivo = Column(Enum('Inspeção Terrestre', 'Missão Drone', name="objetivo"), nullable=False)
    tipo_local = Column(Enum('Obra', 'Jazida', 'Bota-fora', name="tipo_local"), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
    
    trecho = relationship('TechoObra', backref='planejamentos_visitas')
    obra = relationship('Obra', backref='planejamentos_visitas')