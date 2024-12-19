from sqlalchemy import DECIMAL, Column, Date, DateTime, Integer, String, Text, Enum, func
from app.database.base import Base

    
class Obras(Base):
    __tablename__ = 'obras'

    id_obra = Column(Integer, primary_key=True, autoincrement=True)
    nome_obra = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    orcamento_total = Column(DECIMAL(18, 2), nullable=False)
    data_inicio_prevista = Column(Date, nullable=False)
    data_termino_prevista = Column(Date, nullable=False)
    status = Column(Enum('Planejada', 'Em Execução', 'Concluída', 'Paralisada'), nullable=False)
    localizacao_principal = Column(String(255), nullable=False)
    fonte_recursos = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    created_by = Column(String, unique=False, index=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, unique=False, index=True, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    last_modified_by = Column(String, unique=False, index=True, nullable=True)
