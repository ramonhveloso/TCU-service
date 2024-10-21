from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.hourly_rates.hourly_rate_repository import HourlyRateRepository
from app.api.v1.hourly_rates.hourly_rate_schemas import (
    DeleteHourlyRateResponse,
    DeleteHourlyRateResponseData,
    GetHourlyRateResponse,
    GetHourlyRatesResponse,
    HourlyRate,
    PostHourlyRateRequest,
    PostHourlyRateResponse,
    PostHourlyRateResponseData,
    PostHourlyRatesRequest,
    PostHourlyRatesResponse,
    PostHourlyRatesResponseErrorData,
    PutHourlyRateRequest,
    PutHourlyRateResponse,
    PutHourlyRateResponseData,
)


class HourlyRateService:
    def __init__(self, hourly_rate_repository: HourlyRateRepository = Depends()):
        self.hourly_rate_repository = hourly_rate_repository

    def _build_response_data(self, response_repository):
        return PostHourlyRateResponseData(
            id=int(response_repository.id),
            user_id=int(response_repository.user_id),
            rate=float(response_repository.rate),
            start_date=response_repository.start_date,
            end_date=response_repository.end_date,
            status=str(response_repository.status),
            request_date=response_repository.request_date,
            created_at=response_repository.created_at,
            deleted_at=response_repository.deleted_at,
            last_modified=response_repository.last_modified,
        )

    async def get_all_hourly_rates(
        self, db: Session, user_id: int
    ) -> GetHourlyRatesResponse:
        hourly_rates = await self.hourly_rate_repository.get_all_hourly_rates(
            user_id=user_id, db=db
        )
        if not hourly_rates:
            raise HTTPException(status_code=404, detail="Hourly rates not found")
        hourly_rates_list = [
            HourlyRate(
                id=hourly_rate.id,
                user_id=hourly_rate.user_id,
                rate=hourly_rate.rate,
                start_date=hourly_rate.start_date,
                end_date=hourly_rate.end_date,
                status=hourly_rate.status,
                request_date=hourly_rate.request_date,
                created_at=hourly_rate.created_at,
                deleted_at=hourly_rate.deleted_at,
                last_modified=hourly_rate.last_modified,
            )
            for hourly_rate in hourly_rates
        ]
        return GetHourlyRatesResponse(hourly_rates=hourly_rates_list)

    async def get_hourly_rate_by_id(
        self, db: Session, user_id: int, hourly_rate_id: int
    ) -> GetHourlyRateResponse:
        hourly_rate = await self.hourly_rate_repository.get_hourly_rate_by_id(
            db=db, user_id=user_id, hourly_rate_id=hourly_rate_id
        )
        if not hourly_rate:
            raise HTTPException(status_code=404, detail="Hourly rate not found")
        return GetHourlyRateResponse(
            id=hourly_rate.id,
            user_id=hourly_rate.user_id,
            rate=hourly_rate.rate,
            start_date=hourly_rate.start_date,
            end_date=hourly_rate.end_date,
            status=hourly_rate.status,
            request_date=hourly_rate.request_date,
            created_at=hourly_rate.created_at,
            deleted_at=hourly_rate.deleted_at,
            last_modified=hourly_rate.last_modified,
        )

    async def post_hourly_rate(
        self, db: Session, user_id: int, hourly_rate: PostHourlyRateRequest
    ) -> PostHourlyRateResponse:
        try:
            response_repository = await self.hourly_rate_repository.post_hourly_rate(
                db=db, user_id=user_id, hourly_rate=hourly_rate
            )
        except Exception:
            raise HTTPException(status_code=400, detail="Hourly rate not created")
        return PostHourlyRateResponse(
            message="Hourly rate created successfully",
            response=PostHourlyRateResponseData(
                id=int(response_repository.id),
                user_id=int(response_repository.user_id),
                rate=float(response_repository.rate),
                start_date=response_repository.start_date,
                end_date=response_repository.end_date,
                status=str(response_repository.status),
                request_date=response_repository.request_date,
                created_at=response_repository.created_at,
                deleted_at=response_repository.deleted_at,
                last_modified=response_repository.last_modified,
            ),
        )

    async def post_hourly_rates(
        self, db: Session, user_id: int, hourly_rates: PostHourlyRatesRequest
    ) -> PostHourlyRatesResponse:
        list_hourly_rates = []
        list_hourly_rates_errors: list[PostHourlyRatesResponseErrorData] = []

        for hourly_rate in hourly_rates.hourly_rates:
            try:
                response_repository = (
                    await self.hourly_rate_repository.post_hourly_rate(
                        db=db, user_id=user_id, hourly_rate=hourly_rate
                    )
                )
                list_hourly_rates.append(self._build_response_data(response_repository))

            except Exception as e:
                list_hourly_rates_errors.append(
                    PostHourlyRatesResponseErrorData(
                        error_message=str(e),
                        data=self._build_response_data(response_repository),
                    )
                )

        return PostHourlyRatesResponse(
            message=(
                "HourlyRates created with some errors"
                if list_hourly_rates_errors
                else "HourlyRates created successfully"
            ),
            response=list_hourly_rates,
            error=list_hourly_rates_errors if list_hourly_rates_errors else None,
        )

    async def update_hourly_rate(
        self,
        db: Session,
        user_id: int,
        hourly_rate_id: int,
        hourly_rate: PutHourlyRateRequest,
    ) -> PutHourlyRateResponse:
        existing_hourly_rate = await self.hourly_rate_repository.get_hourly_rate_by_id(
            db=db, user_id=user_id, hourly_rate_id=hourly_rate_id
        )
        if not hourly_rate:
            raise HTTPException(status_code=404, detail="Hourly rate not found")

        updated_hourly_rate = await self.hourly_rate_repository.update_hourly_rate(
            db=db, existing_hourly_rate=existing_hourly_rate, hourly_rate=hourly_rate
        )
        return PutHourlyRateResponse(
            message="HourlyRate updated successfully",
            response=PutHourlyRateResponseData(
                id=updated_hourly_rate.id,
                user_id=updated_hourly_rate.user_id,
                rate=updated_hourly_rate.rate,
                start_date=updated_hourly_rate.start_date,
                end_date=updated_hourly_rate.end_date,
                status=updated_hourly_rate.status,
                request_date=updated_hourly_rate.request_date,
                created_at=updated_hourly_rate.created_at,
                deleted_at=updated_hourly_rate.deleted_at,
                last_modified=updated_hourly_rate.last_modified,
            ),
        )

    async def delete_hourly_rate(
        self, db: Session, user_id: int, hourly_rate_id: int
    ) -> DeleteHourlyRateResponse:
        hourly_rate = await self.hourly_rate_repository.get_hourly_rate_by_id(
            db=db, user_id=user_id, hourly_rate_id=hourly_rate_id
        )
        if not hourly_rate:
            raise HTTPException(status_code=404, detail="Hourly rate not found")

        deleted_hourly_rate = await self.hourly_rate_repository.delete_hourly_rate(
            db, hourly_rate
        )
        return DeleteHourlyRateResponse(
            message="HourlyRate deleted successfully",
            response=DeleteHourlyRateResponseData(
                id=deleted_hourly_rate.id,
                user_id=deleted_hourly_rate.user_id,
                rate=deleted_hourly_rate.rate,
                start_date=deleted_hourly_rate.start_date,
                end_date=deleted_hourly_rate.end_date,
                status=deleted_hourly_rate.status,
                request_date=deleted_hourly_rate.request_date,
                created_at=deleted_hourly_rate.created_at,
                deleted_at=deleted_hourly_rate.deleted_at,
                last_modified=deleted_hourly_rate.last_modified,
            ),
        )
