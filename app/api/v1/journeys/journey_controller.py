from typing import Annotated

from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from app.api.v1.journeys.journey_repository import JourneyRepository
from app.api.v1.journeys.journey_schemas import (
    DeleteJourneyResponse,
    GetJourneyResponse,
    GetJourneysResponse,
    PostJourneyRequest,
    PostJourneyResponse,
    PostJourneysRequest,
    PostJourneysResponse,
    PutJourneyRequest,
    PutJourneyResponse
)
from app.api.v1.journeys.journey_service import JourneyService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
journey_service = JourneyService(JourneyRepository())


@router.get("/")
async def get_journeys(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetJourneysResponse:
    response_service = await journey_service.get_all_journeys(db=db, user_id=AuthUser.id)
    return GetJourneysResponse.model_validate(response_service)


@router.get("/{journey_id}")
async def get_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey_id: int,
    db: Session = Depends(get_db),
) -> GetJourneyResponse:
    response_service = await journey_service.get_journey_by_id(db=db, user_id=AuthUser.id, journey_id=journey_id)
    return GetJourneyResponse.model_validate(response_service)


@router.post("/")
async def post_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey: PostJourneyRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostJourneyResponse:
    response_service = await journey_service.post_journey(db=db, user_id=AuthUser.id, journey=journey)
    return PostJourneyResponse.model_validate(response_service)


@router.post("/several")
async def post_journeys(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journeys: PostJourneysRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostJourneysResponse:
    response_service = await journey_service.post_journeys(db=db, user_id=AuthUser.id, journeys=journeys)
    return PostJourneysResponse.model_validate(response_service)


@router.put("/{journey_id}")
async def put_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey: PutJourneyRequest,
    journey_id: int,
    db: Session = Depends(get_db),
) -> PutJourneyResponse:
    response_service = await journey_service.update_journey(db=db, user_id=AuthUser.id, journey_id=journey_id, journey=journey)
    return PutJourneyResponse.model_validate(response_service)


@router.delete("/{journey_id}")
async def delete_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey_id: int,
    db: Session = Depends(get_db),
) -> DeleteJourneyResponse:
    response_service = await journey_service.delete_journey(db=db, user_id=AuthUser.id, journey_id=journey_id)
    return DeleteJourneyResponse.model_validate(response_service)
