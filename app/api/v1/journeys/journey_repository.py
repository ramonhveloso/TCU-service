from datetime import datetime

from sqlalchemy.orm import Session

from app.api.v1.journeys.journey_schemas import PostJourneyRequest, PutJourneyRequest
from app.database.models.journey import Journey


class JourneyRepository:
    async def get_all_journeys(self, id_usuario: int, db: Session):
        return (
            db.query(Journey)
            .filter(Journey.id_usuario == id_usuario, Journey.deleted_at == None)
            .all()
        )

    async def get_journey_by_id(self, db: Session, id_usuario: int, journey_id: int):
        return (
            db.query(Journey)
            .filter(
                Journey.id == journey_id,
                Journey.id_usuario == id_usuario,
                Journey.deleted_at == None,
            )
            .first()
        )

    async def post_journey(
        self, db: Session, id_usuario: int, journey: PostJourneyRequest
    ):
        time_worked = journey.end - journey.start
        hours_worked = time_worked.total_seconds() / 3600
        journey = Journey(
            id_usuario=id_usuario,
            start=journey.start,
            end=journey.end,
            hours_worked=hours_worked,
            hourly_rate=journey.hourly_rate,
            description=journey.description,
            created_at=datetime.now(),
            deleted_at=None,
            last_modified=datetime.now(),
        )
        db.add(journey)
        db.commit()
        db.refresh(journey)
        return journey

    async def update_journey(
        self, db: Session, existing_journey: Journey, journey: PutJourneyRequest
    ):
        time_worked = journey.end - journey.start
        hours_worked = time_worked.total_seconds() / 3600

        existing_journey.start = (
            journey.start if journey.start else existing_journey.start  # type: ignore
        )
        existing_journey.end = journey.end if journey.end else existing_journey.end  # type: ignore
        existing_journey.hours_worked = hours_worked  # type: ignore
        existing_journey.hourly_rate = (
            journey.hourly_rate if journey.hourly_rate else existing_journey.hourly_rate  # type: ignore
        )
        existing_journey.description = (
            journey.description if journey.description else existing_journey.description  # type: ignore
        )
        existing_journey.last_modified = datetime.now()  # type: ignore

        db.commit()
        db.refresh(existing_journey)
        return existing_journey

    async def delete_journey(self, db: Session, journey: Journey):
        journey.deleted_at = datetime.now()  # type: ignore
        journey.last_modified = datetime.now()  # type: ignore
        # db.delete(journey)
        db.commit()
        return journey
