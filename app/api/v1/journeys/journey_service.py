from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.hourly_rates.hourly_rate_repository import HourlyRateRepository
from app.api.v1.hourly_rates.hourly_rate_schemas import (
    DeleteHourlyRateResponse,
    DeleteHourlyRateResponseData,
    GetHourlyRateResponse,
    GetHourlyRatesResponse,
    PostHourlyRateRequest,
    PostHourlyRateResponse,
    PostHourlyRateResponseData,
    PostHourlyRatesRequest,
    PostHourlyRatesResponse,
    PutHourlyRateRequest,
    PutHourlyRateResponse,
    HourlyRate,
    PutHourlyRateResponseData,
)

class HourlyRateService:
    def __init__(self, hourly_rate_repository: HourlyRateRepository = Depends()):
        self.hourly_rate_repository = hourly_rate_repository


    async def get_all_hourly_rates(self, db: Session, user_id: int) -> GetHourlyRatesResponse:
        hourly_rates = await self.hourly_rate_repository.get_all_hourly_rates(user_id=user_id, db=db)
        if not hourly_rates:
            raise HTTPException(status_code=404, detail="HourlyRates not found")
        hourly_rates_list = [
            HourlyRate(id=hourly_rate.id,
                    user_id=hourly_rate.user_id,
                    start=hourly_rate.start,
                    end=hourly_rate.end,
                    hours_worked=hourly_rate.hours_worked,
                    hourly_rate=hourly_rate.hourly_rate,
                    description=hourly_rate.description,
                    created_at=hourly_rate.created_at,
                    last_modified=hourly_rate.last_modified)
            for hourly_rate in hourly_rates
        ]
        return GetHourlyRatesResponse(hourly_rates=hourly_rates_list)

    async def get_hourly_rate_by_id(self, db: Session, user_id: int, hourly_rate_id: int) -> GetHourlyRateResponse:
        hourly_rate = await self.hourly_rate_repository.get_hourly_rate_by_id(db=db, user_id=user_id, hourly_rate_id=hourly_rate_id)
        if not hourly_rate:
            raise HTTPException(status_code=404, detail="HourlyRate not found")
        return GetHourlyRateResponse(id=hourly_rate.id, 
                                  user_id=hourly_rate.user_id, 
                                  start=hourly_rate.start, 
                                  end=hourly_rate.end,
                                  hours_worked=hourly_rate.hours_worked,
                                  hourly_rate=hourly_rate.hourly_rate,
                                  description=hourly_rate.description,
                                  created_at=hourly_rate.created_at,
                                  last_modified=hourly_rate.last_modified)
    
    async def post_hourly_rate(self, db: Session, user_id: int, hourly_rate: PostHourlyRateRequest) -> PostHourlyRateResponse:
        hourly_rate = await self.hourly_rate_repository.post_hourly_rate(db=db, user_id=user_id, hourly_rate=hourly_rate)
        return PostHourlyRateResponse(id=hourly_rate.id)
    
    async def post_hourly_rates(self, db: Session, user_id: int, hourly_rates: PostHourlyRatesRequest) -> PostHourlyRatesResponse:
        list_hourly_rates = []
        for hourly_rate in hourly_rates.hourly_rates:
            hourly_rate_response = await self.hourly_rate_repository.post_hourly_rate(db=db, user_id=user_id, hourly_rate=hourly_rate)
            list_hourly_rates.append(PostHourlyRateResponseData(
                id=hourly_rate_response.id,
                user_id=user_id,
                start=hourly_rate.start,
                end=hourly_rate.end,
                hours_worked=hourly_rate.hours_worked,
                hourly_rate=hourly_rate.hourly_rate,
                description=hourly_rate.description,
                created_at=hourly_rate_response.created_at,
                last_modified=hourly_rate_response.last_modified
            ))
        return PostHourlyRatesResponse(
            message="HourlyRates created successfully",
            response=PostHourlyRateResponseData(
                hourly_rates=list_hourly_rates
            )
        )

    async def update_hourly_rate(
        self, db: Session, user_id: int, hourly_rate_id: int, hourly_rate: PutHourlyRateRequest
    ) -> PutHourlyRateResponse:
        existing_hourly_rate = await self.hourly_rate_repository.get_hourly_rate_by_id(db=db, user_id=user_id, hourly_rate_id=hourly_rate_id, hourly_rate=hourly_rate)
        if not hourly_rate:
            raise HTTPException(status_code=404, detail="HourlyRate not found")

        updated_hourly_rate = await self.hourly_rate_repository.update_hourly_rate(db=db, existing_hourly_rate=existing_hourly_rate, hourly_rate=hourly_rate)
        return PutHourlyRateResponse(
            message="HourlyRate updated successfully",
            response=PutHourlyRateResponseData(
                id=updated_hourly_rate.id,
                user_id=updated_hourly_rate.user_id,
                start=updated_hourly_rate.start,
                end=updated_hourly_rate.end,
                hours_worked=updated_hourly_rate.hours_worked,
                hourly_rate=updated_hourly_rate.hourly_rate,
                description=updated_hourly_rate.description,
                created_at=updated_hourly_rate.created_at,
                last_modified=updated_hourly_rate.last_modified
            )
        )

    async def delete_hourly_rate(self, db: Session, hourly_rate_id: int) -> DeleteHourlyRateResponse:
        hourly_rate = await self.hourly_rate_repository.get_hourly_rate_by_id(db, hourly_rate_id)
        if not hourly_rate:
            raise HTTPException(status_code=404, detail="HourlyRate not found")

        deleted_hourly_rate = await self.hourly_rate_repository.delete_hourly_rate(db, hourly_rate)
        return DeleteHourlyRateResponse(
            message="HourlyRate deleted successfully",
            response=DeleteHourlyRateResponseData(
                id=deleted_hourly_rate.id,
                user_id=deleted_hourly_rate.user_id,
                start=deleted_hourly_rate.start,
                end=deleted_hourly_rate.end,
                hours_worked=deleted_hourly_rate.hours_worked,
                hourly_rate=deleted_hourly_rate.hourly_rate,
                description=deleted_hourly_rate.description,
                created_at=deleted_hourly_rate.created_at,
                last_modified=deleted_hourly_rate.last_modified
            )
        )
