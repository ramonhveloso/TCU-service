from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.database.base import Base


class ExtraExpense(Base):
    __tablename__ = "extra_expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(  # type: ignore
        Enum("pending", "approved", "rejected", name="expense_status"), nullable=False
    )
    created_at = Column(DateTime, default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now())
    user = relationship("User", back_populates="extra_expenses")
