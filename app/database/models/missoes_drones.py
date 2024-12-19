from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.planejamento_visitas import PlanejamentoVisitas

class MissoesDrones(Base):
    __tablename__ = 'missoesdrones'

    id_missao = Column(Integer, primary_key=True, autoincrement=True)
    id_visita = Column(Integer, ForeignKey('planejamentovisitas.id_visita', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    waypoints = Column(Text, nullable=False)
    status = Column(Enum('Planejada', 'Em Execução', 'Concluída'), nullable=False)
    responsavel = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    visita = relationship('PlanejamentoVisitas', backref='missoes_drones')