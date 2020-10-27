from fastapi import APIRouter, Depends, status

from app.api.api_v1.endpoints import items, users, customers, entrepreneurs, football_fields, bookings
from app.api.deps import get_token_header

api_router = APIRouter()
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)
api_router.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
api_router.include_router(
    customers.router,
    prefix="/customers",
    tags=["customers"],
)
api_router.include_router(
    entrepreneurs.router,
    prefix="/items",
    tags=["items"],
)
api_router.include_router(
    football_fields.router,
    prefix="/football_fields",
    tags=["football_fields"],
)
api_router.include_router(
    bookings.router,
    prefix="/bookings",
    tags=["bookings"],
)