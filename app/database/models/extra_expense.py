from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class ExtraExpense(Base):
    __tablename__ = "extra_expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)  # 'pending', 'approved', 'rejected'
    user = relationship("User", back_populates="extra_expenses")