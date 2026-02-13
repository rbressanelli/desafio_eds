from fastapi import APIRouter

from api.v1.endpoints import (
    get_users,
    create_user,
    get_user,
    update_user,
    delete_user,
)

api_router = APIRouter()
api_router.include_router(get_users.api_router, prefix="/users", tags=["users"])
api_router.include_router(create_user.api_router, prefix="/users", tags=["users"])
api_router.include_router(get_user.api_router, prefix="/users", tags=["users"])
api_router.include_router(update_user.api_router, prefix="/users", tags=["users"])
api_router.include_router(delete_user.api_router, prefix="/users", tags=["users"])
