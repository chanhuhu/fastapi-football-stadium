from fastapi import APIRouter, Depends, status

from app.api.api_v1.endpoints import items, users
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
