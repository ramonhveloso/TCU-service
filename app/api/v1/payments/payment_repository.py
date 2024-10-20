from datetime import datetime
from sqlalchemy.orm import Session

from app.api.v1.payments.payment_schemas import PostPaymentRequest, PutPaymentRequest
from app.database.models.payment import Payment


class PaymentRepository:
    async def get_all_payments(self, user_id: int, db: Session):
        return db.query(Payment).filter(Payment.user_id == user_id, Payment.deleted_at == None).all()
    
    async def get_payment_by_id(self, db: Session, user_id: int, payment_id: int):
        return db.query(Payment).filter(Payment.id == payment_id, Payment.user_id == user_id, Payment.deleted_at == None).first()

    async def post_payment(self, db: Session, user_id: int, payment: PostPaymentRequest):
        payment = Payment(
            user_id=user_id,
            amount=payment.amount,
            date=payment.date,
            description=payment.description,
            created_at=datetime.now(),
            deleted_at=None,
            last_modified=datetime.now(),

        )
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment

    async def update_payment(self, db: Session, existing_payment: Payment, payment: PutPaymentRequest):
        existing_payment.amount = payment.amount if payment.amount else existing_payment.amount
        existing_payment.date = payment.date if payment.date else existing_payment.date
        existing_payment.description = payment.description if payment.description else existing_payment.description
        existing_payment.last_modified = datetime.now()

        db.commit()
        db.refresh(existing_payment)
        return existing_payment

    async def delete_payment(self, db: Session, payment: Payment):
        payment.deleted_at = datetime.now()
        payment.last_modified = datetime.now()
        # db.delete(payment)
        db.commit()
        return payment

