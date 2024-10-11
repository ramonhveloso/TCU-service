from typing import Annotated

from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from app.api.v1.extra_expenses.extra_expense_repository import ExtraExpenseRepository
from app.api.v1.extra_expenses.extra_expense_schemas import (
    DeleteExtraExpenseResponse,
    GetExtraExpenseResponse,
    GetExtraExpensesResponse,
    PostExtraExpenseRequest,
    PostExtraExpenseResponse,
    PostExtraExpensesRequest,
    PostExtraExpensesResponse,
    PutExtraExpenseRequest,
    PutExtraExpenseResponse
)
from app.api.v1.extra_expenses.extra_expense_service import ExtraExpenseService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
extra_expense_service = ExtraExpenseService(ExtraExpenseRepository())


@router.get("/")
async def get_extra_expenses(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetExtraExpensesResponse:
    response_service = await extra_expense_service.get_all_extra_expenses(db=db, user_id=AuthUser.id)
    return GetExtraExpensesResponse.model_validate(response_service)


@router.get("/{extra_expense_id}")
async def get_extra_expense(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    extra_expense_id: int,
    db: Session = Depends(get_db),
) -> GetExtraExpenseResponse:
    response_service = await extra_expense_service.get_extra_expense_by_id(db=db, user_id=AuthUser.id, extra_expense_id=extra_expense_id)
    return GetExtraExpenseResponse.model_validate(response_service)


@router.post("/")
async def post_extra_expense(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    extra_expense: PostExtraExpenseRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostExtraExpensesResponse:
    response_service = await extra_expense_service.post_extra_expense(db=db, user_id=AuthUser.id, extra_expense=extra_expense)
    return PostExtraExpenseResponse.model_validate(response_service)
           
           
@router.post("/multiple")
async def post_extra_expenses(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    extra_expenses: PostExtraExpensesRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostExtraExpensesResponse:
    response_service = await extra_expense_service.post_extra_expenses(db=db, user_id=AuthUser.id, extra_expenses=extra_expenses)
    return PostExtraExpensesResponse.model_validate(response_service)


@router.put("/{extra_expense_id}")
async def put_extra_expense(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    extra_expense: PutExtraExpenseRequest,
    extra_expense_id: int,
    db: Session = Depends(get_db),
) -> PutExtraExpenseResponse:
    response_service = await extra_expense_service.update_extra_expense(db=db, user_id=AuthUser.id, extra_expense_id=extra_expense_id, extra_expense=extra_expense)
    return PutExtraExpenseResponse.model_validate(response_service)


@router.delete("/{extra_expense_id}")
async def delete_extra_expense(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    extra_expense_id: int,
    db: Session = Depends(get_db),
) -> DeleteExtraExpenseResponse:
    response_service = await extra_expense_service.delete_extra_expense(db=db, user_id=AuthUser.id, extra_expense_id=extra_expense_id)
    return DeleteExtraExpenseResponse.model_validate(response_service)