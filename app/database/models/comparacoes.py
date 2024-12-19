from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from app.database.base import Base

from sqlalchemy.orm import relationship

from app.database.models.analises import Analises
from app.database.models.subanalises_riscos import SubAnalisesRiscos 

class Comparacoes(Base):
    __tablename__ = 'comparacoes'

    id_comparacao = Column(Integer, primary_key=True, autoincrement=True)
    id_analise = Column(Integer, ForeignKey('analises.id_analise', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    id_subanalise = Column(Integer, ForeignKey('subanalisesriscos.id_subanalise', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    previsto = Column(Text, nullable=False)
    realizado = Column(Text, nullable=False)
    desvio = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)

    analise = relationship('Analises', backref='comparacoes')
    sub_analise = relationship('SubAnalisesRiscos', backref='comparacoes')