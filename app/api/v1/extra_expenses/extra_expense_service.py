from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.extra_expenses.extra_expense_repository import ExtraExpenseRepository
from app.api.v1.extra_expenses.extra_expense_schemas import (
    DeleteExtraExpenseResponse,
    DeleteExtraExpenseResponseData,
    GetExtraExpenseResponse,
    GetExtraExpensesResponse,
    PostExtraExpenseRequest,
    PostExtraExpenseResponse,
    PostExtraExpenseResponseData,
    PostExtraExpensesRequest,
    PostExtraExpensesResponse,
    PutExtraExpenseRequest,
    PutExtraExpenseResponse,
    ExtraExpense,
    PutExtraExpenseResponseData,
)

class ExtraExpenseService:
    def __init__(self, extra_expense_repository: ExtraExpenseRepository = Depends()):
        self.extra_expense_repository = extra_expense_repository


    async def get_all_extra_expenses(self, db: Session, user_id: int) -> GetExtraExpensesResponse:
        extra_expenses = await self.extra_expense_repository.get_all_extra_expenses(user_id=user_id, db=db)
        if not extra_expenses:
            raise HTTPException(status_code=404, detail="Extra expenses not found")
        extra_expenses_list = [
            ExtraExpense(id=extra_expense.id,
                         user_id=extra_expense.user_id,
                         amount=extra_expense.amount,
                         description=extra_expense.description,
                         date=extra_expense.date,
                         status=extra_expense.status,
                         created_at=extra_expense.created_at,
                         deleted_at=extra_expense.deleted_at,
                         last_modified=extra_expense.last_modified)
            for extra_expense in extra_expenses
        ]
        return GetExtraExpensesResponse(extra_expenses=extra_expenses_list)

    async def get_extra_expense_by_id(self, db: Session, user_id: int, extra_expense_id: int) -> GetExtraExpenseResponse:
        extra_expense = await self.extra_expense_repository.get_extra_expense_by_id(db=db, user_id=user_id, extra_expense_id=extra_expense_id)
        if not extra_expense:
            raise HTTPException(status_code=404, detail="Extra expense not found")
        return GetExtraExpenseResponse(id=extra_expense.id,
                                       user_id=extra_expense.user_id,
                                       amount=extra_expense.amount,
                                       description=extra_expense.description,
                                       date=extra_expense.date,
                                       status=extra_expense.status,
                                       created_at=extra_expense.created_at,
                                       deleted_at=extra_expense.deleted_at,
                                       last_modified=extra_expense.last_modified)
    
    async def post_extra_expense(self, db: Session, user_id: int, extra_expense: PostExtraExpenseRequest) -> PostExtraExpenseResponse:
        try:
            response_repository = await self.extra_expense_repository.post_extra_expense(db=db, user_id=user_id, extra_expense=extra_expense)
        except Exception:
            raise HTTPException(status_code=400, detail="Extra expense not created")
        return PostExtraExpenseResponse(message="Extra expense created successfully",
                                        response=PostExtraExpenseResponseData(
                                            id=int(response_repository.id),
                                            user_id=int(response_repository.user_id),
                                            amount=float(response_repository.amount),
                                            description=str(response_repository.description),
                                            date=response_repository.date,
                                            status=str(response_repository.status),
                                            created_at=response_repository.created_at,
                                            deleted_at=response_repository.deleted_at,
                                            last_modified=response_repository.last_modified
                                        ))
    
    async def post_extra_expenses(self, db: Session, user_id: int, extra_expenses: PostExtraExpensesRequest) -> PostExtraExpensesResponse:
        list_extra_expenses = []
        for extra_expense in extra_expenses.extra_expenses:
            extra_expense_response = await self.extra_expense_repository.post_extra_expense(db=db, user_id=user_id, extra_expense=extra_expense)
            list_extra_expenses.append(PostExtraExpenseResponseData(
                id=extra_expense_response.id,
                user_id=user_id,
                start=extra_expense.start,
                end=extra_expense.end,
                hours_worked=extra_expense.hours_worked,
                hourly_rate=extra_expense.hourly_rate,
                description=extra_expense.description,
                created_at=extra_expense_response.created_at,
                last_modified=extra_expense_response.last_modified
            ))
        return PostExtraExpensesResponse(
            message="ExtraExpenses created successfully",
            response=PostExtraExpenseResponseData(
                extra_expenses=list_extra_expenses
            )
        )

    async def update_extra_expense(
        self, db: Session, user_id: int, extra_expense_id: int, extra_expense: PutExtraExpenseRequest
    ) -> PutExtraExpenseResponse:
        existing_extra_expense = await self.extra_expense_repository.get_extra_expense_by_id(db=db, user_id=user_id, extra_expense_id=extra_expense_id, extra_expense=extra_expense)
        if not extra_expense:
            raise HTTPException(status_code=404, detail="ExtraExpense not found")

        updated_extra_expense = await self.extra_expense_repository.update_extra_expense(db=db, existing_extra_expense=existing_extra_expense, extra_expense=extra_expense)
        return PutExtraExpenseResponse(
            message="ExtraExpense updated successfully",
            response=PutExtraExpenseResponseData(
                id=updated_extra_expense.id,
                user_id=updated_extra_expense.user_id,
                start=updated_extra_expense.start,
                end=updated_extra_expense.end,
                hours_worked=updated_extra_expense.hours_worked,
                hourly_rate=updated_extra_expense.hourly_rate,
                description=updated_extra_expense.description,
                created_at=updated_extra_expense.created_at,
                last_modified=updated_extra_expense.last_modified
            )
        )

    async def delete_extra_expense(self, db: Session, extra_expense_id: int) -> DeleteExtraExpenseResponse:
        extra_expense = await self.extra_expense_repository.get_extra_expense_by_id(db, extra_expense_id)
        if not extra_expense:
            raise HTTPException(status_code=404, detail="ExtraExpense not found")

        deleted_extra_expense = await self.extra_expense_repository.delete_extra_expense(db, extra_expense)
        return DeleteExtraExpenseResponse(
            message="ExtraExpense deleted successfully",
            response=DeleteExtraExpenseResponseData(
                id=deleted_extra_expense.id,
                user_id=deleted_extra_expense.user_id,
                start=deleted_extra_expense.start,
                end=deleted_extra_expense.end,
                hours_worked=deleted_extra_expense.hours_worked,
                hourly_rate=deleted_extra_expense.hourly_rate,
                description=deleted_extra_expense.description,
                created_at=deleted_extra_expense.created_at,
                last_modified=deleted_extra_expense.last_modified
            )
        )
