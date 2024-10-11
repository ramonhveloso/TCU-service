from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    user_id: int
    start: datetime
    end: datetime
    hours_worked: float
    hourly_rate: float
    description: str
    created_at: datetime
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
    start: datetime
    end: datetime
    hours_worked: float
    hourly_rate: float
    description: str

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
    response: List[PostPaymentResponseData]


class PostPaymentsResponseData(Payment):
    pass


class PostPaymentsResponse(BaseModel):
    message: str
    response: PostPaymentsResponseData


class PutPaymentRequest(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    hours_worked: Optional[float] = None
    hourly_rate: Optional[float] = None
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
