from typing import Annotated

from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session

from app.api.v1.payments.payment_repository import PaymentRepository
from app.api.v1.payments.payment_schemas import (
    DeletePaymentResponse,
    GetPaymentResponse,
    GetPaymentsResponse,
    PostPaymentRequest,
    PostPaymentResponse,
    PostPaymentsRequest,
    PostPaymentsResponse,
    PutPaymentRequest,
    PutPaymentResponse,
)
from app.api.v1.payments.payment_service import PaymentService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
payment_service = PaymentService(PaymentRepository())


@router.get("/")
async def get_payments(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetPaymentsResponse:
    response_service = await payment_service.get_all_payments(
        db=db, user_id=AuthUser.id
    )
    return GetPaymentsResponse.model_validate(response_service)


@router.get("/by_user/{user_id}")
async def get_payments_by_users(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    user_id: int,
    db: Session = Depends(get_db),
) -> GetPaymentsResponse:
    response_service = await payment_service.get_all_payments(db=db, user_id=user_id)
    return GetPaymentsResponse.model_validate(response_service)


@router.get("/{payment_id}")
async def get_payment(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    payment_id: int,
    db: Session = Depends(get_db),
) -> GetPaymentResponse:
    response_service = await payment_service.get_payment_by_id(
        db=db, user_id=AuthUser.id, payment_id=payment_id
    )
    return GetPaymentResponse.model_validate(response_service)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_payment(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    payment: PostPaymentRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostPaymentResponse:
    response_service = await payment_service.post_payment(
        db=db, user_id=AuthUser.id, payment=payment
    )
    return PostPaymentResponse.model_validate(response_service)


@router.post("/multiple", status_code=status.HTTP_201_CREATED)
async def post_payments(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    payments: PostPaymentsRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostPaymentsResponse:
    response_service = await payment_service.post_payments(
        db=db, user_id=AuthUser.id, payments=payments
    )
    return PostPaymentsResponse.model_validate(response_service)


@router.put("/{payment_id}")
async def put_payment(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    payment: PutPaymentRequest,
    payment_id: int,
    db: Session = Depends(get_db),
) -> PutPaymentResponse:
    response_service = await payment_service.update_payment(
        db=db, user_id=AuthUser.id, payment_id=payment_id, payment=payment
    )
    return PutPaymentResponse.model_validate(response_service)


@router.delete("/{payment_id}")
async def delete_payment(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    payment_id: int,
    db: Session = Depends(get_db),
) -> DeletePaymentResponse:
    response_service = await payment_service.delete_payment(
        db=db, user_id=AuthUser.id, payment_id=payment_id
    )
    return DeletePaymentResponse.model_validate(response_service)
