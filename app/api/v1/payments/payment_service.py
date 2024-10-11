from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.payments.payment_repository import PaymentRepository
from app.api.v1.payments.payment_schemas import (
    DeletePaymentResponse,
    DeletePaymentResponseData,
    GetPaymentResponse,
    GetPaymentsResponse,
    PostPaymentRequest,
    PostPaymentResponse,
    PostPaymentResponseData,
    PostPaymentsRequest,
    PostPaymentsResponse,
    PutPaymentRequest,
    PutPaymentResponse,
    Payment,
    PutPaymentResponseData,
)

class PaymentService:
    def __init__(self, payment_repository: PaymentRepository = Depends()):
        self.payment_repository = payment_repository


    async def get_all_payments(self, db: Session, user_id: int) -> GetPaymentsResponse:
        payments = await self.payment_repository.get_all_payments(user_id=user_id, db=db)
        if not payments:
            raise HTTPException(status_code=404, detail="Payments not found")
        payments_list = [
            Payment(id=payment.id,
                    user_id=payment.user_id,
                    start=payment.start,
                    end=payment.end,
                    hours_worked=payment.hours_worked,
                    hourly_rate=payment.hourly_rate,
                    description=payment.description,
                    created_at=payment.created_at,
                    last_modified=payment.last_modified)
            for payment in payments
        ]
        return GetPaymentsResponse(payments=payments_list)

    async def get_payment_by_id(self, db: Session, user_id: int, payment_id: int) -> GetPaymentResponse:
        payment = await self.payment_repository.get_payment_by_id(db=db, user_id=user_id, payment_id=payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return GetPaymentResponse(id=payment.id, 
                                  user_id=payment.user_id, 
                                  start=payment.start, 
                                  end=payment.end,
                                  hours_worked=payment.hours_worked,
                                  hourly_rate=payment.hourly_rate,
                                  description=payment.description,
                                  created_at=payment.created_at,
                                  last_modified=payment.last_modified)
    
    async def post_payment(self, db: Session, user_id: int, payment: PostPaymentRequest) -> PostPaymentResponse:
        payment = await self.payment_repository.post_payment(db=db, user_id=user_id, payment=payment)
        return PostPaymentResponse(id=payment.id)
    
    async def post_payments(self, db: Session, user_id: int, payments: PostPaymentsRequest) -> PostPaymentsResponse:
        list_payments = []
        for payment in payments.payments:
            payment_response = await self.payment_repository.post_payment(db=db, user_id=user_id, payment=payment)
            list_payments.append(PostPaymentResponseData(
                id=payment_response.id,
                user_id=user_id,
                start=payment.start,
                end=payment.end,
                hours_worked=payment.hours_worked,
                hourly_rate=payment.hourly_rate,
                description=payment.description,
                created_at=payment_response.created_at,
                last_modified=payment_response.last_modified
            ))
        return PostPaymentsResponse(
            message="Payments created successfully",
            response=PostPaymentResponseData(
                payments=list_payments
            )
        )

    async def update_payment(
        self, db: Session, user_id: int, payment_id: int, payment: PutPaymentRequest
    ) -> PutPaymentResponse:
        existing_payment = await self.payment_repository.get_payment_by_id(db=db, user_id=user_id, payment_id=payment_id, payment=payment)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")

        updated_payment = await self.payment_repository.update_payment(db=db, existing_payment=existing_payment, payment=payment)
        return PutPaymentResponse(
            message="Payment updated successfully",
            response=PutPaymentResponseData(
                id=updated_payment.id,
                user_id=updated_payment.user_id,
                start=updated_payment.start,
                end=updated_payment.end,
                hours_worked=updated_payment.hours_worked,
                hourly_rate=updated_payment.hourly_rate,
                description=updated_payment.description,
                created_at=updated_payment.created_at,
                last_modified=updated_payment.last_modified
            )
        )

    async def delete_payment(self, db: Session, payment_id: int) -> DeletePaymentResponse:
        payment = await self.payment_repository.get_payment_by_id(db, payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")

        deleted_payment = await self.payment_repository.delete_payment(db, payment)
        return DeletePaymentResponse(
            message="Payment deleted successfully",
            response=DeletePaymentResponseData(
                id=deleted_payment.id,
                user_id=deleted_payment.user_id,
                start=deleted_payment.start,
                end=deleted_payment.end,
                hours_worked=deleted_payment.hours_worked,
                hourly_rate=deleted_payment.hourly_rate,
                description=deleted_payment.description,
                created_at=deleted_payment.created_at,
                last_modified=deleted_payment.last_modified
            )
        )
