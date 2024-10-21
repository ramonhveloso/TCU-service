from sqlalchemy import Column, DateTime, String, func

from app.database.base import Base


class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"
    id = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
