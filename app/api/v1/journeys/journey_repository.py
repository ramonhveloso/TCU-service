from datetime import datetime
from sqlalchemy.orm import Session

from app.api.v1.hourly_rates.hourly_rate_schemas import PostHourlyRateRequest, PostHourlyRatesRequest, PutHourlyRateRequest
from app.database.models.hourly_rate import HourlyRate


class HourlyRateRepository:
    async def get_all_hourly_rates(self, user_id: int, db: Session):
        return db.query(HourlyRate).filter(HourlyRate.user_id == user_id).all()
    
    async def get_hourly_rate_by_id(self, db: Session, user_id: int, hourly_rate_id: int):
        return db.query(HourlyRate).filter(HourlyRate.id == hourly_rate_id, HourlyRate.user_id == user_id).first()

    async def post_hourly_rate(self, db: Session, user_id: int, hourly_rate: PostHourlyRateRequest):
        hourly_rate = HourlyRate(
            user_id=user_id,
            start=hourly_rate.start,
            end=hourly_rate.end,
            hours_worked=hourly_rate.hours_worked,
            hourly_rate=hourly_rate.hourly_rate,
            description=hourly_rate.description,
            created_at=datetime.now(),
            last_modified=datetime.now()
        )
        db.add(hourly_rate)
        db.commit()
        db.refresh(hourly_rate)
        return hourly_rate

    async def update_hourly_rate(self, db: Session, existing_hourly_rate: HourlyRate, hourly_rate: PutHourlyRateRequest):
        existing_hourly_rate.start = hourly_rate.start if hourly_rate.start else existing_hourly_rate.start # type: ignore
        existing_hourly_rate.end = hourly_rate.end if hourly_rate.end else existing_hourly_rate.end # type: ignore
        existing_hourly_rate.hours_worked = hourly_rate.hours_worked if hourly_rate.hours_worked else existing_hourly_rate.hours_worked # type: ignore
        existing_hourly_rate.hourly_rate = hourly_rate.hourly_rate if hourly_rate.hourly_rate else existing_hourly_rate.hourly_rate # type: ignore
        existing_hourly_rate.description = hourly_rate.description if hourly_rate.description else existing_hourly_rate.description # type: ignore
        existing_hourly_rate.last_modified = datetime.now()

        db.commit()
        db.refresh(existing_hourly_rate)
        return existing_hourly_rate

    async def delete_hourly_rate(self, db: Session, hourly_rate: HourlyRate):
        db.delete(hourly_rate)
        db.commit()
        return hourly_rate

