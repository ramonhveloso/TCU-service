from typing import Annotated

from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session

from app.api.v1.analises.analise_repository import JourneyRepository
from app.api.v1.analises.analise_schemas import (
    DeleteJourneyResponse,
    GetJourneyResponse,
    GetJourneysResponse,
    PostJourneyRequest,
    PostJourneyResponse,
    PostJourneysRequest,
    PostJourneysResponse,
    PutJourneyRequest,
    PutJourneyResponse,
)
from app.api.v1.analises.analise_service import JourneyService
from app.api.v1.usuarios.usuario_repository import UsuarioRepository
from app.api.v1.usuarios.usuario_service import UsuarioService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
journey_service = JourneyService(JourneyRepository())
user_service = UsuarioService(UsuarioRepository())


@router.get("/")
async def get_journeys(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetJourneysResponse:
    response_service = await journey_service.get_all_journeys(
        db=db, id_usuario=AuthUser.id
    )
    return GetJourneysResponse.model_validate(response_service)


@router.get("/by_user/{id_usuario}")
async def get_journeys_by_user(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    id_usuario: int,
    db: Session = Depends(get_db),
) -> GetJourneysResponse:
    await user_service.verify_is_superuser(db=db, id_usuario=AuthUser.id)
    response_service = await journey_service.get_all_journeys(db=db, id_usuario=id_usuario)
    return GetJourneysResponse.model_validate(response_service)


@router.get("/{journey_id}")
async def get_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey_id: int,
    db: Session = Depends(get_db),
) -> GetJourneyResponse:
    response_service = await journey_service.get_journey_by_id(
        db=db, id_usuario=AuthUser.id, journey_id=journey_id
    )
    return GetJourneyResponse.model_validate(response_service)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    analise: PostJourneyRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostJourneyResponse:
    response_service = await journey_service.post_journey(
        db=db, id_usuario=AuthUser.id, analise=analise
    )
    return PostJourneyResponse.model_validate(response_service)


@router.post("/multiple", status_code=status.HTTP_201_CREATED)
async def post_journeys(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    analises: PostJourneysRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostJourneysResponse:
    response_service = await journey_service.post_journeys(
        db=db, id_usuario=AuthUser.id, analises=analises
    )
    return PostJourneysResponse.model_validate(response_service)


@router.put("/{journey_id}")
async def put_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    analise: PutJourneyRequest,
    journey_id: int,
    db: Session = Depends(get_db),
) -> PutJourneyResponse:
    response_service = await journey_service.update_journey(
        db=db, id_usuario=AuthUser.id, journey_id=journey_id, analise=analise
    )
    return PutJourneyResponse.model_validate(response_service)


@router.delete("/{journey_id}")
async def delete_journey(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    journey_id: int,
    db: Session = Depends(get_db),
) -> DeleteJourneyResponse:
    response_service = await journey_service.delete_journey(
        db=db, id_usuario=AuthUser.id, journey_id=journey_id
    )
    return DeleteJourneyResponse.model_validate(response_service)
