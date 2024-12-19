from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.trechos import TrechosObra
from app.database.models.obras import Obras

class PlanejamentoVisitas(Base):
    __tablename__ = 'planejamentovisitas'

    id_visita = Column(Integer, primary_key=True, autoincrement=True)
    id_trecho = Column(Integer, ForeignKey('trechosobra.id_trecho', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    data_planejada = Column(Date, nullable=False)
    responsavel = Column(String(255), nullable=False)
    objetivo = Column(Enum('Inspeção Terrestre', 'Missão Drone'), nullable=False)
    tipo_local = Column(Enum('Obra', 'Jazida', 'Bota-fora'), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
    
    trecho = relationship('TrechosObra', backref='planejamentos_visitas')
    obra = relationship('Obras', backref='planejamentos_visitas')