from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class HourlyRate(BaseModel):
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
    response: List[PostHourlyRateResponseData]


class PostHourlyRatesResponseData(HourlyRate):
    pass


class PostHourlyRatesResponse(BaseModel):
    message: str
    response: PostHourlyRatesResponseData


class PutHourlyRateRequest(BaseModel):
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
