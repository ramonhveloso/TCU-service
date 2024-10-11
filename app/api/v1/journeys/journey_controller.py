from typing import Annotated

from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from app.api.v1.journeys.journey_repository import HourlyRateRepository
from app.api.v1.journeys.journey_schemas import (
    DeleteHourlyRateResponse,
    GetHourlyRateResponse,
    GetHourlyRatesResponse,
    PostHourlyRateRequest,
    PostHourlyRatesRequest,
    PostHourlyRatesResponse,
    PutHourlyRateRequest,
    PutHourlyRateResponse
)
from app.api.v1.journeys.journey_service import HourlyRateService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
journey_service = HourlyRateService(HourlyRateRepository())


@router.get("/")
async def get_journeys(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetHourlyRatesResponse:
    response_service = await journey_service.get_all_journeys(db=db, user_id=AuthUser.id)
    return GetHourlyRatesResponse.model_validate(response_service)


@router.get("/{journey_id}")
async def get_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey_id: int,
    db: Session = Depends(get_db),
) -> GetHourlyRateResponse:
    response_service = await journey_service.get_journey_by_id(db=db, user_id=AuthUser.id, journey_id=journey_id)
    return GetHourlyRateResponse.model_validate(response_service)


@router.post("/")
async def post_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey: PostHourlyRateRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostHourlyRatesResponse:
    response_service = await journey_service.post_journey(db=db, user_id=AuthUser.id, journey=journey)
    return PostHourlyRatesResponse.model_validate(response_service)


@router.post("/")
async def post_journeys(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journeys: PostHourlyRatesRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostHourlyRatesResponse:
    response_service = await journey_service.post_journeys(db=db, user_id=AuthUser.id, journeys=journeys)
    return PostHourlyRatesResponse.model_validate(response_service)


@router.put("/{journey_id}")
async def put_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey: PutHourlyRateRequest,
    journey_id: int,
    db: Session = Depends(get_db),
) -> PutHourlyRateResponse:
    response_service = await journey_service.update_journey(db=db, user_id=AuthUser.id, journey_id=journey_id, journey=journey)
    return PutHourlyRateResponse.model_validate(response_service)


@router.delete("/{journey_id}")
async def delete_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey_id: int,
    db: Session = Depends(get_db),
) -> DeleteHourlyRateResponse:
    response_service = await journey_service.delete_journey(db=db, user_id=AuthUser.id, journey_id=journey_id)
    return DeleteHourlyRateResponse.model_validate(response_service)
