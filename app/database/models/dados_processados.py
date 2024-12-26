from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Text, Enum, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.obras import Obra

class DadoProcessado(Base):
    __tablename__ = 'dadosprocessados'

    id_dados = Column(Integer, primary_key=True, autoincrement=True)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_dado = Column(Enum('Medições', 'Modelos 3D', 'Parâmetros Analíticos', name="tipo_dado"), nullable=False)
    descricao = Column(Text, nullable=False)
    caminho_arquivo = Column(Text, nullable=False)
    data_processamento = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    obra = relationship('Obra', backref='dados_processados')
