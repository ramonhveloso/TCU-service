from datetime import datetime
from sqlalchemy.orm import Session

from app.api.v1.payments.payment_schemas import PostPaymentRequest, PostPaymentsRequest, PutPaymentRequest
from app.database.models.payment import Payment


class PaymentRepository:
    async def get_all_payments(self, user_id: int, db: Session):
        return db.query(Payment).filter(Payment.user_id == user_id).all()
    
    async def get_payment_by_id(self, db: Session, user_id: int, payment_id: int):
        return db.query(Payment).filter(Payment.id == payment_id, Payment.user_id == user_id).first()

    async def post_payment(self, db: Session, user_id: int, payment: PostPaymentRequest):
        payment = Payment(
            user_id=user_id,
            start=payment.start,
            end=payment.end,
            hours_worked=payment.hours_worked,
            hourly_rate=payment.hourly_rate,
            description=payment.description,
            created_at=datetime.now(),
            last_modified=datetime.now()
        )
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment

    async def update_payment(self, db: Session, existing_payment: Payment, payment: PutPaymentRequest):
        existing_payment.start = payment.start if payment.start else existing_payment.start # type: ignore
        existing_payment.end = payment.end if payment.end else existing_payment.end # type: ignore
        existing_payment.hours_worked = payment.hours_worked if payment.hours_worked else existing_payment.hours_worked # type: ignore
        existing_payment.hourly_rate = payment.hourly_rate if payment.hourly_rate else existing_payment.hourly_rate # type: ignore
        existing_payment.description = payment.description if payment.description else existing_payment.description # type: ignore
        existing_payment.last_modified = datetime.now()

        db.commit()
        db.refresh(existing_payment)
        return existing_payment

    async def delete_payment(self, db: Session, payment: Payment):
        db.delete(payment)
        db.commit()
        return payment

