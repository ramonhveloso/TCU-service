from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.payments.payment_repository import PaymentRepository
from app.api.v1.payments.payment_schemas import (
    DeletePaymentResponse,
    DeletePaymentResponseData,
    GetPaymentResponse,
    GetPaymentsResponse,
    Payment,
    PostPaymentRequest,
    PostPaymentResponse,
    PostPaymentResponseData,
    PostPaymentsRequest,
    PostPaymentsResponse,
    PostPaymentsResponseErrorData,
    PutPaymentRequest,
    PutPaymentResponse,
    PutPaymentResponseData,
)


class PaymentService:
    def __init__(self, payment_repository: PaymentRepository = Depends()):
        self.payment_repository = payment_repository

    def _build_response_data(self, response_repository):
        return PostPaymentResponseData(
            id=int(response_repository.id),
            user_id=int(response_repository.user_id),
            amount=float(response_repository.amount),
            date=response_repository.date,
            description=response_repository.description,
            created_at=response_repository.created_at,
            deleted_at=response_repository.deleted_at,
            last_modified=response_repository.last_modified,
        )

    async def get_all_payments(self, db: Session, user_id: int) -> GetPaymentsResponse:
        payments = await self.payment_repository.get_all_payments(
            user_id=user_id, db=db
        )
        # if not payments:
        #     raise HTTPException(status_code=404, detail="Payments not found")
        payments_list = [
            Payment(
                id=payment.id,
                user_id=payment.user_id,
                amount=payment.amount,
                date=payment.date,
                description=payment.description,
                created_at=payment.created_at,
                deleted_at=payment.deleted_at,
                last_modified=payment.last_modified,
            )
            for payment in payments
        ]
        return GetPaymentsResponse(payments=payments_list)

    async def get_payment_by_id(
        self, db: Session, user_id: int, payment_id: int
    ) -> GetPaymentResponse:
        payment = await self.payment_repository.get_payment_by_id(
            db=db, user_id=user_id, payment_id=payment_id
        )
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return GetPaymentResponse(
            id=payment.id,
            user_id=payment.user_id,
            amount=payment.amount,
            date=payment.date,
            description=payment.description,
            created_at=payment.created_at,
            deleted_at=payment.deleted_at,
            last_modified=payment.last_modified,
        )

    async def post_payment(
        self, db: Session, user_id: int, payment: PostPaymentRequest
    ) -> PostPaymentResponse:
        try:
            response_repository = await self.payment_repository.post_payment(
                db=db, user_id=user_id, payment=payment
            )
        except Exception:
            raise HTTPException(status_code=400, detail="Payment not created")
        return PostPaymentResponse(
            message="Payment created successfully",
            response=PostPaymentResponseData(
                id=int(response_repository.id),
                user_id=int(response_repository.user_id),
                amount=float(response_repository.amount),
                date=response_repository.date,
                description=response_repository.description,
                created_at=response_repository.created_at,
                deleted_at=response_repository.deleted_at,
                last_modified=response_repository.last_modified,
            ),
        )

    async def post_payments(
        self, db: Session, user_id: int, payments: PostPaymentsRequest
    ) -> PostPaymentsResponse:
        list_payments = []
        list_payments_errors: list[PostPaymentsResponseErrorData] = []

        for payment in payments.payments:
            try:
                response_repository = await self.payment_repository.post_payment(
                    db=db, user_id=user_id, payment=payment
                )
                list_payments.append(self._build_response_data(response_repository))

            except Exception as e:
                list_payments_errors.append(
                    PostPaymentsResponseErrorData(
                        error_message=str(e),
                        data=self._build_response_data(response_repository),
                    )
                )

        return PostPaymentsResponse(
            message=(
                "Payments created with some errors"
                if list_payments_errors
                else "Payments created successfully"
            ),
            response=list_payments,
            error=list_payments_errors if list_payments_errors else None,
        )

    async def update_payment(
        self, db: Session, user_id: int, payment_id: int, payment: PutPaymentRequest
    ) -> PutPaymentResponse:
        existing_payment = await self.payment_repository.get_payment_by_id(
            db=db, user_id=user_id, payment_id=payment_id
        )
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")

        updated_payment = await self.payment_repository.update_payment(
            db=db, existing_payment=existing_payment, payment=payment
        )
        return PutPaymentResponse(
            message="Payment updated successfully",
            response=PutPaymentResponseData(
                id=updated_payment.id,
                user_id=updated_payment.user_id,
                amount=updated_payment.amount,
                date=updated_payment.date,
                description=updated_payment.description,
                created_at=updated_payment.created_at,
                deleted_at=updated_payment.deleted_at,
                last_modified=updated_payment.last_modified,
            ),
        )

    async def delete_payment(
        self, db: Session, user_id: int, payment_id: int
    ) -> DeletePaymentResponse:
        payment = await self.payment_repository.get_payment_by_id(
            db=db, user_id=user_id, payment_id=payment_id
        )
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")

        deleted_payment = await self.payment_repository.delete_payment(db, payment)
        return DeletePaymentResponse(
            message="Payment deleted successfully",
            response=DeletePaymentResponseData(
                id=deleted_payment.id,
                user_id=deleted_payment.user_id,
                amount=deleted_payment.amount,
                date=deleted_payment.date,
                description=deleted_payment.description,
                created_at=deleted_payment.created_at,
                deleted_at=deleted_payment.deleted_at,
                last_modified=deleted_payment.last_modified,
            ),
        )
