from fastapi import APIRouter

from app.api.v1.auth.auth_controller import router as auth_router
from app.api.v1.extra_expenses.extra_expense_controller import (
    router as extra_expenses_router,
)
from app.api.v1.hourly_rates.hourly_rate_controller import router as hourly_rates_router
from app.api.v1.improvements.improvement_controller import router as improvements_router
from app.api.v1.journeys.journey_controller import router as journeys_router
from app.api.v1.payments.payment_controller import router as payments_router
from app.api.v1.users.user_controller import router as users_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(users_router, prefix="/users", tags=["Users"])
router.include_router(
    extra_expenses_router, prefix="/extra-expenses", tags=["ExtraExpenses"]
)
router.include_router(hourly_rates_router, prefix="/hourly-rates", tags=["HourlyRates"])
router.include_router(journeys_router, prefix="/journeys", tags=["Journeys"])
router.include_router(payments_router, prefix="/payments", tags=["Payments"])
router.include_router(
    improvements_router, prefix="/improvements", tags=["Improvements"]
)
