from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.improvements.improvement_repository import ImprovementRepository
from app.api.v1.improvements.improvement_schemas import (
    DeleteImprovementResponse,
    DeleteImprovementResponseData,
    GetImprovementResponse,
    GetImprovementsResponse,
    Improvement,
    PostImprovementRequest,
    PostImprovementResponse,
    PostImprovementResponseData,
    PostImprovementsRequest,
    PostImprovementsResponse,
    PostImprovementsResponseData,
    PostImprovementsResponseErrorData,
    PutImprovementRequest,
    PutImprovementResponse,
    PutImprovementResponseData,
)


class ImprovementService:
    def __init__(self, improvement_repository: ImprovementRepository = Depends()):
        self.improvement_repository = improvement_repository

    def _build_response_data(self, response_repository):
        return PostImprovementResponseData(
            id=int(response_repository.id),
            user_id=int(response_repository.user_id),
            description=response_repository.description,
            created_at=response_repository.created_at,
            deleted_at=response_repository.deleted_at,
            last_modified=response_repository.last_modified,
        )

    async def get_all_improvements(self, db: Session, user_id: int) -> GetImprovementsResponse:
        improvements = await self.improvement_repository.get_all_improvements(
            user_id=user_id, db=db
        )
        # if not improvements:
        #     raise HTTPException(status_code=404, detail="Improvements not found")
        improvements_list = [
            Improvement(
                id=improvement.id,
                user_id=improvement.user_id,
                description=improvement.description,
                created_at=improvement.created_at,
                deleted_at=improvement.deleted_at,
                last_modified=improvement.last_modified,
            )
            for improvement in improvements
        ]
        return GetImprovementsResponse(improvements=improvements_list)

    async def get_improvement_by_id(
        self, db: Session, user_id: int, improvement_id: int
    ) -> GetImprovementResponse:
        improvement = await self.improvement_repository.get_improvement_by_id(
            db=db, user_id=user_id, improvement_id=improvement_id
        )
        if not improvement:
            raise HTTPException(status_code=404, detail="Improvement not found")
        return GetImprovementResponse(
            id=improvement.id,
            user_id=improvement.user_id,
            description=improvement.description,
            created_at=improvement.created_at,
            deleted_at=improvement.deleted_at,
            last_modified=improvement.last_modified,
        )

    async def post_improvement(
        self, db: Session, user_id: int, improvement: PostImprovementRequest
    ) -> PostImprovementResponse:
        try:
            response_repository = await self.improvement_repository.post_improvement(
                db=db, user_id=user_id, improvement=improvement
            )
        except Exception:
            raise HTTPException(status_code=400, detail="Improvement not created")
        return PostImprovementResponse(
            message="Improvement created successfully",
            response=PostImprovementResponseData(
                id=int(response_repository.id),
                user_id=int(response_repository.user_id),
                description=response_repository.description,
                created_at=response_repository.created_at,
                deleted_at=response_repository.deleted_at,
                last_modified=response_repository.last_modified,
            ),
        )

    async def post_improvements(
        self, db: Session, user_id: int, improvements: PostImprovementsRequest
    ) -> PostImprovementsResponse:
        list_improvements: list[PostImprovementsResponseData] = []
        list_improvements_errors: list[PostImprovementsResponseErrorData] = []

        for improvement in improvements.improvements:
            try:
                response_repository = await self.improvement_repository.post_improvement(
                    db=db, user_id=user_id, improvement=improvement
                )
                list_improvements.append(self._build_response_data(response_repository))

            except Exception as e:
                list_improvements_errors.append(
                    PostImprovementsResponseErrorData(
                        error_message=str(e),
                        data=self._build_response_data(response_repository),
                    )
                )

        return PostImprovementsResponse(
            message=(
                "Improvements created with some errors"
                if list_improvements_errors
                else "Improvements created successfully"
            ),
            response=list_improvements,
            error=list_improvements_errors if list_improvements_errors else None,
        )

    async def update_improvement(
        self, db: Session, user_id: int, improvement_id: int, improvement: PutImprovementRequest
    ) -> PutImprovementResponse:
        existing_improvement = await self.improvement_repository.get_improvement_by_id(
            db=db, user_id=user_id, improvement_id=improvement_id
        )
        if not improvement:
            raise HTTPException(status_code=404, detail="Improvement not found")

        updated_improvement = await self.improvement_repository.update_improvement(
            db=db, existing_improvement=existing_improvement, improvement=improvement
        )
        return PutImprovementResponse(
            message="Improvement updated successfully",
            response=PutImprovementResponseData(
                id=updated_improvement.id,
                user_id=updated_improvement.user_id,
                description=updated_improvement.description,
                created_at=updated_improvement.created_at,
                deleted_at=updated_improvement.deleted_at,
                last_modified=updated_improvement.last_modified,
            ),
        )

    async def delete_improvement(
        self, db: Session, user_id: int, improvement_id: int
    ) -> DeleteImprovementResponse:
        improvement = await self.improvement_repository.get_improvement_by_id(
            db=db, user_id=user_id, improvement_id=improvement_id
        )
        if not improvement:
            raise HTTPException(status_code=404, detail="Improvement not found")

        deleted_improvement = await self.improvement_repository.delete_improvement(db, improvement)
        return DeleteImprovementResponse(
            message="Improvement deleted successfully",
            response=DeleteImprovementResponseData(
                id=deleted_improvement.id,
                user_id=deleted_improvement.user_id,
                description=deleted_improvement.description,
                created_at=deleted_improvement.created_at,
                deleted_at=deleted_improvement.deleted_at,
                last_modified=deleted_improvement.last_modified,
            ),
        )
