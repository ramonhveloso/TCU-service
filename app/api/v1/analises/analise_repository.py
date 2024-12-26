from datetime import datetime

from sqlalchemy.orm import Session

from app.api.v1.analises.analise_schemas import PostJourneyRequest, PutJourneyRequest
from app.database.models.analises import Analise


class JourneyRepository:
    async def get_all_journeys(self, id_usuario: int, db: Session):
        return (
            db.query(Analise)
            .filter(Analise.id_usuario == id_usuario, Analise.deleted_at == None)
            .all()
        )

    async def get_journey_by_id(self, db: Session, id_usuario: int, journey_id: int):
        return (
            db.query(Analise)
            .filter(
                Analise.id == journey_id,
                Analise.id_usuario == id_usuario,
                Analise.deleted_at == None,
            )
            .first()
        )

    async def post_journey(
        self, db: Session, id_usuario: int, analise: PostJourneyRequest
    ):
        time_worked = analise.end - analise.start
        hours_worked = time_worked.total_seconds() / 3600
        analise = Analise(
            id_usuario=id_usuario,
            start=analise.start,
            end=analise.end,
            hours_worked=hours_worked,
            hourly_rate=analise.hourly_rate,
            description=analise.description,
            created_at=datetime.now(),
            deleted_at=None,
            last_modified=datetime.now(),
        )
        db.add(analise)
        db.commit()
        db.refresh(analise)
        return analise

    async def update_journey(
        self, db: Session, existing_journey: Analise, analise: PutJourneyRequest
    ):
        time_worked = analise.end - analise.start
        hours_worked = time_worked.total_seconds() / 3600

        existing_journey.start = (
            analise.start if analise.start else existing_journey.start  # type: ignore
        )
        existing_journey.end = analise.end if analise.end else existing_journey.end  # type: ignore
        existing_journey.hours_worked = hours_worked  # type: ignore
        existing_journey.hourly_rate = (
            analise.hourly_rate if analise.hourly_rate else existing_journey.hourly_rate  # type: ignore
        )
        existing_journey.description = (
            analise.description if analise.description else existing_journey.description  # type: ignore
        )
        existing_journey.last_modified = datetime.now()  # type: ignore

        db.commit()
        db.refresh(existing_journey)
        return existing_journey

    async def delete_journey(self, db: Session, analise: Analise):
        analise.deleted_at = datetime.now()  # type: ignore
        analise.last_modified = datetime.now()  # type: ignore
        # db.delete(analise)
        db.commit()
        return analise
