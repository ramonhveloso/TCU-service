from typing import Annotated

from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session

from app.api.v1.hourly_rates.hourly_rate_repository import HourlyRateRepository
from app.api.v1.hourly_rates.hourly_rate_schemas import (
    DeleteHourlyRateResponse,
    GetHourlyRateResponse,
    GetHourlyRatesResponse,
    PostHourlyRateRequest,
    PostHourlyRateResponse,
    PostHourlyRatesRequest,
    PostHourlyRatesResponse,
    PutHourlyRateRequest,
    PutHourlyRateResponse,
)
from app.api.v1.hourly_rates.hourly_rate_service import HourlyRateService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
hourly_rate_service = HourlyRateService(HourlyRateRepository())


@router.get("/")
async def get_hourly_rates(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetHourlyRatesResponse:
    response_service = await hourly_rate_service.get_all_hourly_rates(
        db=db, user_id=AuthUser.id
    )
    return GetHourlyRatesResponse.model_validate(response_service)


@router.get("/by_user/{user_id}")
async def get_hourly_rates_by_user(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    user_id: int,
    db: Session = Depends(get_db),
) -> GetHourlyRatesResponse:
    response_service = await hourly_rate_service.get_all_hourly_rates(
        db=db, user_id=user_id
    )
    return GetHourlyRatesResponse.model_validate(response_service)


@router.get("/{hourly_rate_id}")
async def get_hourly_rate(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    hourly_rate_id: int,
    db: Session = Depends(get_db),
) -> GetHourlyRateResponse:
    response_service = await hourly_rate_service.get_hourly_rate_by_id(
        db=db, user_id=AuthUser.id, hourly_rate_id=hourly_rate_id
    )
    return GetHourlyRateResponse.model_validate(response_service)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_hourly_rate(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    hourly_rate: PostHourlyRateRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostHourlyRateResponse:
    response_service = await hourly_rate_service.post_hourly_rate(
        db=db, user_id=AuthUser.id, hourly_rate=hourly_rate
    )
    return PostHourlyRateResponse.model_validate(response_service)


@router.post("/multiple", status_code=status.HTTP_201_CREATED)
async def post_hourly_rates(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    hourly_rates: PostHourlyRatesRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostHourlyRatesResponse:
    response_service = await hourly_rate_service.post_hourly_rates(
        db=db, user_id=AuthUser.id, hourly_rates=hourly_rates
    )
    return PostHourlyRatesResponse.model_validate(response_service)


@router.put("/{hourly_rate_id}")
async def put_hourly_rate(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    hourly_rate: PutHourlyRateRequest,
    hourly_rate_id: int,
    db: Session = Depends(get_db),
) -> PutHourlyRateResponse:
    response_service = await hourly_rate_service.update_hourly_rate(
        db=db,
        user_id=AuthUser.id,
        hourly_rate_id=hourly_rate_id,
        hourly_rate=hourly_rate,
    )
    return PutHourlyRateResponse.model_validate(response_service)


@router.delete("/{hourly_rate_id}")
async def delete_hourly_rate(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    hourly_rate_id: int,
    db: Session = Depends(get_db),
) -> DeleteHourlyRateResponse:
    response_service = await hourly_rate_service.delete_hourly_rate(
        db=db, user_id=AuthUser.id, hourly_rate_id=hourly_rate_id
    )
    return DeleteHourlyRateResponse.model_validate(response_service)
