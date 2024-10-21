from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class HourlyRate(BaseModel):
    id: int
    user_id: int
    rate: float
    start_date: datetime
    end_date: Optional[datetime] = None
    status: str
    request_date: datetime
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


class GetHourlyRatesResponse(BaseModel):
    hourly_rates: List[HourlyRate]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetHourlyRateResponse(HourlyRate):
    pass


class PostHourlyRateRequest(BaseModel):
    rate: float
    start_date: datetime
    end_date: Optional[datetime] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostHourlyRatesRequest(BaseModel):
    hourly_rates: List[PostHourlyRateRequest]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostHourlyRateResponseData(HourlyRate):
    pass


class PostHourlyRateResponse(BaseModel):
    message: str
    response: PostHourlyRateResponseData


class PostHourlyRatesResponseData(HourlyRate):
    pass


class PostHourlyRatesResponseErrorData(BaseModel):
    error_message: str
    data: Optional[PostHourlyRatesResponseData]


class PostHourlyRatesResponse(BaseModel):
    message: str
    response: List[PostHourlyRatesResponseData]
    error: Optional[List[PostHourlyRatesResponseErrorData]] = None


class PutHourlyRateRequest(BaseModel):
    rate: float
    start_date: datetime
    end_date: Optional[datetime] = None
    status: str

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PutHourlyRateResponseData(HourlyRate):
    pass


class PutHourlyRateResponse(BaseModel):
    message: str
    response: PutHourlyRateResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class DeleteHourlyRateResponseData(HourlyRate):
    pass


class DeleteHourlyRateResponse(BaseModel):
    message: str
    response: DeleteHourlyRateResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
