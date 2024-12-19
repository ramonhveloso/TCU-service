from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.journeys.journey_repository import JourneyRepository
from app.api.v1.journeys.journey_schemas import (
    DeleteJourneyResponse,
    DeleteJourneyResponseData,
    GetJourneyResponse,
    GetJourneysResponse,
    Journey,
    PostJourneyRequest,
    PostJourneyResponse,
    PostJourneyResponseData,
    PostJourneysRequest,
    PostJourneysResponse,
    PostJourneysResponseData,
    PostJourneysResponseErrorData,
    PutJourneyRequest,
    PutJourneyResponse,
    PutJourneyResponseData,
)


class JourneyService:
    def __init__(self, journey_repository: JourneyRepository = Depends()):
        self.journey_repository = journey_repository

    def _build_response_data(self, response_repository):
        return PostJourneyResponseData(
            id=int(response_repository.id),
            id_usuario=int(response_repository.id_usuario),
            start=response_repository.start,
            end=response_repository.end,
            hours_worked=float(response_repository.hours_worked),
            hourly_rate=float(response_repository.hourly_rate),
            description=response_repository.description,
            created_at=response_repository.created_at,
            deleted_at=response_repository.deleted_at,
            last_modified=response_repository.last_modified,
        )

    async def get_all_journeys(self, db: Session, id_usuario: int) -> GetJourneysResponse:
        journeys = await self.journey_repository.get_all_journeys(
            id_usuario=id_usuario, db=db
        )
        # if not journeys:
        #     raise HTTPException(status_code=404, detail="Journeys not found")
        journeys_list = [
            Journey(
                id=journey.id,
                id_usuario=journey.id_usuario,
                start=journey.start,
                end=journey.end,
                hours_worked=journey.hours_worked,
                hourly_rate=journey.hourly_rate,
                description=journey.description,
                created_at=journey.created_at,
                deleted_at=journey.deleted_at,
                last_modified=journey.last_modified,
            )
            for journey in journeys
        ]
        return GetJourneysResponse(journeys=journeys_list)

    async def get_journey_by_id(
        self, db: Session, id_usuario: int, journey_id: int
    ) -> GetJourneyResponse:
        journey = await self.journey_repository.get_journey_by_id(
            db=db, id_usuario=id_usuario, journey_id=journey_id
        )
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")
        return GetJourneyResponse(
            id=journey.id,
            id_usuario=journey.id_usuario,
            start=journey.start,
            end=journey.end,
            hours_worked=journey.hours_worked,
            hourly_rate=journey.hourly_rate,
            description=journey.description,
            created_at=journey.created_at,
            deleted_at=journey.deleted_at,
            last_modified=journey.last_modified,
        )

    async def post_journey(
        self, db: Session, id_usuario: int, journey: PostJourneyRequest
    ) -> PostJourneyResponse:
        try:
            response_repository = await self.journey_repository.post_journey(
                db=db, id_usuario=id_usuario, journey=journey
            )
        except Exception:
            raise HTTPException(status_code=400, detail="Journey not created")
        return PostJourneyResponse(
            message="Journey created successfully",
            response=PostJourneyResponseData(
                id=int(response_repository.id),
                id_usuario=int(response_repository.id_usuario),
                start=response_repository.start,
                end=response_repository.end,
                hours_worked=float(response_repository.hours_worked),
                hourly_rate=float(response_repository.hourly_rate),
                description=response_repository.description,
                created_at=response_repository.created_at,
                deleted_at=response_repository.deleted_at,
                last_modified=response_repository.last_modified,
            ),
        )

    async def post_journeys(
        self, db: Session, id_usuario: int, journeys: PostJourneysRequest
    ) -> PostJourneysResponse:
        list_journeys: list[PostJourneysResponseData] = []
        list_journeys_errors: list[PostJourneysResponseErrorData] = []

        for journey in journeys.journeys:
            try:
                response_repository = await self.journey_repository.post_journey(
                    db=db, id_usuario=id_usuario, journey=journey
                )
                list_journeys.append(self._build_response_data(response_repository))

            except Exception as e:
                list_journeys_errors.append(
                    PostJourneysResponseErrorData(
                        error_message=str(e),
                        data=self._build_response_data(response_repository),
                    )
                )

        return PostJourneysResponse(
            message=(
                "Journeys created with some errors"
                if list_journeys_errors
                else "Journeys created successfully"
            ),
            response=list_journeys,
            error=list_journeys_errors if list_journeys_errors else None,
        )

    async def update_journey(
        self, db: Session, id_usuario: int, journey_id: int, journey: PutJourneyRequest
    ) -> PutJourneyResponse:
        existing_journey = await self.journey_repository.get_journey_by_id(
            db=db, id_usuario=id_usuario, journey_id=journey_id
        )
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")

        updated_journey = await self.journey_repository.update_journey(
            db=db, existing_journey=existing_journey, journey=journey
        )
        return PutJourneyResponse(
            message="Journey updated successfully",
            response=PutJourneyResponseData(
                id=updated_journey.id,
                id_usuario=updated_journey.id_usuario,
                start=updated_journey.start,
                end=updated_journey.end,
                hours_worked=updated_journey.hours_worked,
                hourly_rate=updated_journey.hourly_rate,
                description=updated_journey.description,
                created_at=updated_journey.created_at,
                deleted_at=updated_journey.deleted_at,
                last_modified=updated_journey.last_modified,
            ),
        )

    async def delete_journey(
        self, db: Session, id_usuario: int, journey_id: int
    ) -> DeleteJourneyResponse:
        journey = await self.journey_repository.get_journey_by_id(
            db=db, id_usuario=id_usuario, journey_id=journey_id
        )
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")

        deleted_journey = await self.journey_repository.delete_journey(db, journey)
        return DeleteJourneyResponse(
            message="Journey deleted successfully",
            response=DeleteJourneyResponseData(
                id=deleted_journey.id,
                id_usuario=deleted_journey.id_usuario,
                start=deleted_journey.start,
                end=deleted_journey.end,
                hours_worked=deleted_journey.hours_worked,
                hourly_rate=deleted_journey.hourly_rate,
                description=deleted_journey.description,
                created_at=deleted_journey.created_at,
                deleted_at=deleted_journey.deleted_at,
                last_modified=deleted_journey.last_modified,
            ),
        )
