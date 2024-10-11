from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.database.base import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    user = relationship('User', back_populates="payments", lazy='joined')