from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.trechos import TrechosObra
from app.database.models.obras import Obras

class Documentos(Base):
    __tablename__ = 'documentos'

    id_documento = Column(Integer, primary_key=True, autoincrement=True)
    id_trecho = Column(Integer, ForeignKey('trechosobra.id_trecho', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_obra = Column(Integer, ForeignKey('obras.id_obra', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tipo_documento = Column(Enum('', 'Contrato', 'Projeto', 'Relatório', 'Imagem', 'ART', 'Memorial Descritivo', 'Planilha', 'Outro'), nullable=False)
    fonte = Column(String(255), nullable=False)
    formato = Column(Enum('', 'PDF', 'CAD', 'Imagem', 'Outro'), nullable=False)
    arquivo = Column(Text, nullable=False)
    tipo_conteudo = Column(String(150), nullable=False)
    data_arquivo = Column(DateTime, nullable=False)
    data_insercao = Column(DateTime, nullable=False)
    tamanho = Column(Integer, nullable=False)
    resumo = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    trecho = relationship('TrechosObra', backref='documentos')
    obra = relationship('Obras', backref='documentos')
