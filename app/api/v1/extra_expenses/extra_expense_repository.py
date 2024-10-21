from datetime import datetime

from sqlalchemy.orm import Session

from app.api.v1.extra_expenses.extra_expense_schemas import (
    PostExtraExpenseRequest,
    PutExtraExpenseRequest,
)
from app.database.models.extra_expense import ExtraExpense


class ExtraExpenseRepository:
    async def get_all_extra_expenses(self, user_id: int, db: Session):
        return (
            db.query(ExtraExpense)
            .filter(ExtraExpense.user_id == user_id, ExtraExpense.deleted_at == None)
            .all()
        )

    async def get_extra_expense_by_id(
        self, db: Session, user_id: int, extra_expense_id: int
    ):
        return (
            db.query(ExtraExpense)
            .filter(
                ExtraExpense.id == extra_expense_id,
                ExtraExpense.user_id == user_id,
                ExtraExpense.deleted_at == None,
            )
            .first()
        )

    async def post_extra_expense(
        self, db: Session, user_id: int, extra_expense: PostExtraExpenseRequest
    ):
        extra_expense = ExtraExpense(
            user_id=user_id,
            amount=extra_expense.amount,
            description=extra_expense.description,
            date=extra_expense.date,
            status="pending",
            created_at=datetime.now(),
            deleted_at=None,
            last_modified=datetime.now(),
        )
        db.add(extra_expense)
        db.commit()
        db.refresh(extra_expense)
        return extra_expense

    async def update_extra_expense(
        self,
        db: Session,
        existing_extra_expense: ExtraExpense,
        extra_expense: PutExtraExpenseRequest,
    ):
        existing_extra_expense.amount = extra_expense.amount if extra_expense.amount else existing_extra_expense.amount  # type: ignore
        existing_extra_expense.description = extra_expense.description if extra_expense.description else existing_extra_expense.description  # type: ignore
        existing_extra_expense.date = extra_expense.date if extra_expense.date else existing_extra_expense.date  # type: ignore
        existing_extra_expense.last_modified = datetime.now()  # type: ignore

        db.commit()
        db.refresh(existing_extra_expense)
        return existing_extra_expense

    async def delete_extra_expense(self, db: Session, extra_expense: ExtraExpense):
        extra_expense.deleted_at = datetime.now()  # type: ignore
        extra_expense.last_modified = datetime.now()  # type: ignore
        # db.delete(extra_expense)
        db.commit()
        return extra_expense
