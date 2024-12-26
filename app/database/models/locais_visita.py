from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

class LocalVisita(Base):
    __tablename__ = 'locais_visita'

    id_local = Column(Integer, primary_key=True, autoincrement=True)
    id_visita = Column(Integer, ForeignKey('planejamentovisitas.id_visita', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_local = Column(Enum('Obra', 'Jazida', 'Bota-fora', name="tipo_local"), nullable=False)
    endereco = Column(Text, nullable=False)
    notas = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
