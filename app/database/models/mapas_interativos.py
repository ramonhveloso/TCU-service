from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.obras import Obras

class MapasInterativos(Base):
    __tablename__ = 'mapasinterativos'

    id_mapa = Column(Integer, primary_key=True, autoincrement=True)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    camadas = Column(Text, nullable=False)
    caminho_arquivo = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    obra = relationship('Obras', backref='mapas_interativos')
