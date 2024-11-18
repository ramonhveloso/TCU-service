from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Improvement(BaseModel):
    id: int
    user_id: int
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


class GetImprovementsResponse(BaseModel):
    improvements: Optional[List[Improvement]] = []

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class GetImprovementResponse(Improvement):
    pass


class PostImprovementRequest(BaseModel):
    description: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostImprovementsRequest(BaseModel):
    improvements: List[PostImprovementRequest]

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PostImprovementResponseData(Improvement):
    pass


class PostImprovementResponse(BaseModel):
    message: str
    response: PostImprovementResponseData


class PostImprovementsResponseData(Improvement):
    pass


class PostImprovementsResponseErrorData(BaseModel):
    error_message: str
    data: Optional[PostImprovementsResponseData]


class PostImprovementsResponse(BaseModel):
    message: str
    response: List[PostImprovementsResponseData]
    error: Optional[List[PostImprovementsResponseErrorData]] = None


class PutImprovementRequest(BaseModel):
    description: Optional[str] = None

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class PutImprovementResponseData(Improvement):
    pass


class PutImprovementResponse(BaseModel):
    message: str
    response: PutImprovementResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)


class DeleteImprovementResponseData(Improvement):
    pass


class DeleteImprovementResponse(BaseModel):
    message: str
    response: DeleteImprovementResponseData

    class Config:
        from_attributes = True

    @classmethod
    def model_validate(cls, data):
        if isinstance(data, cls):
            data = data.model_dump()
        return cls(**data)
