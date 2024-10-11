from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, func
from sqlalchemy.orm import relationship
from sqlalchemy import Enum

from app.database.base import Base


class HourlyRate(Base):
    __tablename__ = "hourly_rates"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    rate = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)
    status = Column(Enum('active', 'inactive', 'pending', 'rejected', name='rate_status'), nullable=False)
    request_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    user = relationship('User', back_populates="hourly_rates")