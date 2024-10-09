from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class HourlyRate(Base):
    __tablename__ = "hourly_rates"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    rate = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)  # 'active', 'inactive', 'pending', 'rejected'
    request_date = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="hourly_rates")