from datetime import datetime

from sqlalchemy.orm import Session

from app.api.v1.hourly_rates.hourly_rate_schemas import (
    PostHourlyRateRequest,
    PutHourlyRateRequest,
)
from app.database.models.hourly_rate import HourlyRate


class HourlyRateRepository:
    async def get_all_hourly_rates(self, user_id: int, db: Session):
        return (
            db.query(HourlyRate)
            .filter(HourlyRate.user_id == user_id, HourlyRate.deleted_at == None)
            .all()
        )

    async def get_hourly_rate_by_id(
        self, db: Session, user_id: int, hourly_rate_id: int
    ):
        return (
            db.query(HourlyRate)
            .filter(
                HourlyRate.id == hourly_rate_id,
                HourlyRate.user_id == user_id,
                HourlyRate.deleted_at == None,
            )
            .first()
        )

    async def post_hourly_rate(
        self, db: Session, user_id: int, hourly_rate: PostHourlyRateRequest
    ):
        hourly_rate = HourlyRate(
            user_id=user_id,
            rate=hourly_rate.rate,
            start_date=hourly_rate.start_date,
            end_date=hourly_rate.end_date,
            status="pending",
            request_date=datetime.now(),
            created_at=datetime.now(),
            deleted_at=None,
            last_modified=datetime.now(),
        )
        db.add(hourly_rate)
        db.commit()
        db.refresh(hourly_rate)
        return hourly_rate

    async def update_hourly_rate(
        self,
        db: Session,
        existing_hourly_rate: HourlyRate,
        hourly_rate: PutHourlyRateRequest,
    ):
        existing_hourly_rate.rate = (
            hourly_rate.rate if hourly_rate.rate else existing_hourly_rate.rate  # type: ignore
        )
        existing_hourly_rate.start_date = (
            hourly_rate.start_date  # type: ignore
            if hourly_rate.start_date
            else existing_hourly_rate.start_date
        )
        existing_hourly_rate.end_date = (
            hourly_rate.end_date  # type: ignore
            if hourly_rate.end_date
            else existing_hourly_rate.end_date
        )
        existing_hourly_rate.status = (
            hourly_rate.status if hourly_rate.status else existing_hourly_rate.status  # type: ignore
        )
        existing_hourly_rate.last_modified = datetime.now()  # type: ignore

        db.commit()
        db.refresh(existing_hourly_rate)
        return existing_hourly_rate

    async def delete_hourly_rate(self, db: Session, hourly_rate: HourlyRate):
        hourly_rate.deleted_at = datetime.now()  # type: ignore
        hourly_rate.last_modified = datetime.now()  # type: ignore
        # db.delete(hourly_rate)
        db.commit()
        return hourly_rate
