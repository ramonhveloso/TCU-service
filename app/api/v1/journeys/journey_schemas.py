from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Journey(BaseModel):
    id: int
    user_id: int
    start: datetime
    end: datetime
    hours_worked: float
    hourly_rate: float
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


class GetJourneysResponse(BaseModel):
    journeys: Optional[List[Journey]] = []

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetJourneyResponse(Journey):
    pass


class PostJourneyRequest(BaseModel):
    start: datetime
    end: datetime
    hourly_rate: float
    description: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostJourneysRequest(BaseModel):
    journeys: List[PostJourneyRequest]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostJourneyResponseData(Journey):
    pass


class PostJourneyResponse(BaseModel):
    message: str
    response: PostJourneyResponseData


class PostJourneysResponseData(Journey):
    pass


class PostJourneysResponseErrorData(BaseModel):
    error_message: str
    data: Optional[PostJourneysResponseData]


class PostJourneysResponse(BaseModel):
    message: str
    response: List[PostJourneysResponseData]
    error: Optional[List[PostJourneysResponseErrorData]] = None


class PutJourneyRequest(BaseModel):
    start: datetime
    end: datetime
    hourly_rate: float
    description: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PutJourneyResponseData(Journey):
    pass


class PutJourneyResponse(BaseModel):
    message: str
    response: PutJourneyResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class DeleteJourneyResponseData(Journey):
    pass


class DeleteJourneyResponse(BaseModel):
    message: str
    response: DeleteJourneyResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
