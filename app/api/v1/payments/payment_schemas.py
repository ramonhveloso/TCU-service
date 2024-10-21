from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    user_id: int
    amount: float
    date: datetime
    description: Optional[str] = None
    created_at: datetime
    deleted_at: Optional[datetime] = None
    last_modified: datetime

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetPaymentsResponse(BaseModel):
    payments: List[Payment]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetPaymentResponse(Payment):
    pass


class PostPaymentRequest(BaseModel):
    amount: float
    date: datetime
    description: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostPaymentsRequest(BaseModel):
    payments: List[PostPaymentRequest]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostPaymentResponseData(Payment):
    pass


class PostPaymentResponse(BaseModel):
    message: str
    response: PostPaymentResponseData


class PostPaymentsResponseData(Payment):
    pass


class PostPaymentsResponseErrorData(BaseModel):
    error_message: str
    data: Optional[PostPaymentsResponseData]


class PostPaymentsResponse(BaseModel):
    message: str
    response: List[PostPaymentsResponseData]
    error: Optional[List[PostPaymentsResponseErrorData]] = None


class PutPaymentRequest(BaseModel):
    amount: float
    date: datetime
    description: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PutPaymentResponseData(Payment):
    pass


class PutPaymentResponse(BaseModel):
    message: str
    response: PutPaymentResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class DeletePaymentResponseData(Payment):
    pass


class DeletePaymentResponse(BaseModel):
    message: str
    response: DeletePaymentResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
