from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.usuarios import Usuario
from app.database.models.missoes_drones import MissaoDrone

class AvaliacaoProfissional(Base):
    __tablename__ = 'avaliacao_profissionais'

    id_avaliacao = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    data = Column(Integer, nullable=False) #TODO: campo data do tipo inteiro, descobrir o motivo
    missao_avaliada = Column(Integer, ForeignKey('missoesdrones.id_missao', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    nota = Column(Integer, nullable=False)
    comentarios = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    usuario = relationship('Usuario', backref='avaliacao_profissionais')
    missao = relationship('MissaoDrone', backref='avaliacao_profissionais')