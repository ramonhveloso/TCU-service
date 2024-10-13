from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ExtraExpense(BaseModel):
    id: int
    user_id: int
    amount: float
    description: str
    date: datetime
    status: str
    created_at: datetime
    deleted_at: Optional[datetime]
    last_modified: datetime

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetExtraExpensesResponse(BaseModel):
    extra_expenses: List[ExtraExpense]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetExtraExpenseResponse(ExtraExpense):
    pass
    

class PostExtraExpenseRequest(BaseModel):
    amount: float
    description: str
    date: datetime
    

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
    

class PostExtraExpensesRequest(BaseModel):
    extra_expenses: List[PostExtraExpenseRequest]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
    

class PostExtraExpenseResponseData(ExtraExpense):
    pass
    

class PostExtraExpenseResponse(BaseModel):
    message: str
    response: PostExtraExpenseResponseData


class PostExtraExpensesResponseData(ExtraExpense):
    pass


class PostExtraExpensesResponseErrorData(BaseModel):
    error_message: str
    data: Optional[PostExtraExpensesResponseData]


class PostExtraExpensesResponse(BaseModel):
    message: str
    response: List[PostExtraExpensesResponseData]
    error: Optional[List[PostExtraExpensesResponseErrorData]] = None


class PutExtraExpenseRequest(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[datetime] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
    

class PutExtraExpenseResponseData(ExtraExpense):
    pass


class PutExtraExpenseResponse(BaseModel):
    message: str
    response: PutExtraExpenseResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class DeleteExtraExpenseResponseData(ExtraExpense):
    pass


class DeleteExtraExpenseResponse(BaseModel):
    message: str
    response: DeleteExtraExpenseResponseData


    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
