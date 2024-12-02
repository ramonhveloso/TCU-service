from typing import Annotated

from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.orm import Session

from app.api.v1.improvements.improvement_repository import ImprovementRepository
from app.api.v1.improvements.improvement_schemas import (
    DeleteImprovementResponse,
    GetImprovementResponse,
    GetImprovementsResponse,
    PostImprovementRequest,
    PostImprovementResponse,
    PostImprovementsRequest,
    PostImprovementsResponse,
    PutImprovementRequest,
    PutImprovementResponse,
)
from app.api.v1.improvements.improvement_service import ImprovementService
from app.api.v1.users.user_repository import UserRepository
from app.api.v1.users.user_service import UserService
from app.middleware.dependencies import AuthUser, get_db, jwt_middleware

router = APIRouter()
improvement_service = ImprovementService(ImprovementRepository())
user_service = UserService(UserRepository())


@router.get("/")
async def get_improvements(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    db: Session = Depends(get_db),
) -> GetImprovementsResponse:
    response_service = await improvement_service.get_all_improvements(
        db=db, user_id=AuthUser.id
    )
    return GetImprovementsResponse.model_validate(response_service)


@router.get("/by_user/{user_id}")
async def get_improvements_by_user(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    user_id: int,
    db: Session = Depends(get_db),
) -> GetImprovementsResponse:
    await user_service.verify_is_superuser(db=db, user_id=AuthUser.id)
    response_service = await improvement_service.get_all_improvements(
        db=db, user_id=user_id
    )
    return GetImprovementsResponse.model_validate(response_service)


@router.get("/{improvement_id}")
async def get_improvement(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    improvement_id: int,
    db: Session = Depends(get_db),
) -> GetImprovementResponse:
    response_service = await improvement_service.get_improvement_by_id(
        db=db, user_id=AuthUser.id, improvement_id=improvement_id
    )
    return GetImprovementResponse.model_validate(response_service)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_improvement(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    improvement: PostImprovementRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostImprovementResponse:
    response_service = await improvement_service.post_improvement(
        db=db, user_id=AuthUser.id, improvement=improvement
    )
    return PostImprovementResponse.model_validate(response_service)


@router.post("/multiple", status_code=status.HTTP_201_CREATED)
async def post_improvements(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    improvements: PostImprovementsRequest = Depends(),
    db: Session = Depends(get_db),
) -> PostImprovementsResponse:
    response_service = await improvement_service.post_improvements(
        db=db, user_id=AuthUser.id, improvements=improvements
    )
    return PostImprovementsResponse.model_validate(response_service)


@router.put("/{improvement_id}")
async def put_improvement(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    improvement: PutImprovementRequest,
    improvement_id: int,
    db: Session = Depends(get_db),
) -> PutImprovementResponse:
    response_service = await improvement_service.update_improvement(
        db=db,
        user_id=AuthUser.id,
        improvement_id=improvement_id,
        improvement=improvement,
    )
    return PutImprovementResponse.model_validate(response_service)


@router.delete("/{improvement_id}")
async def delete_improvement(
    AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
    improvement_id: int,
    db: Session = Depends(get_db),
) -> DeleteImprovementResponse:
    response_service = await improvement_service.delete_improvement(
        db=db, user_id=AuthUser.id, improvement_id=improvement_id
    )
    return DeleteImprovementResponse.model_validate(response_service)
