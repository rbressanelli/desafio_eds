from fastapi import APIRouter, status, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import select, func
from fastapi import Query
from ....models.user import UserModel
from ....schemas.user_schema import UserSchema
from ....core.database import get_db

from ....schemas.page_schema import Page


api_router = APIRouter()


@api_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=Page[UserSchema],
)
async def get_users(
    name: Optional[str] = None,
    email: Optional[str] = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    query = select(UserModel)

    if name:
        query = query.where(func.lower(UserModel.name).like(f"{name.lower()}%"))

    if email:
        query = query.where(func.lower(UserModel.email).like(f"{email.lower()}%"))

    total_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(total_query)
    total = total_result.scalar_one()

    offset = (page - 1) * size
    query = query.offset(offset).limit(size)

    result = await db.execute(query)
    users = result.scalars().all()

    total_pages = (total + size - 1) // size

    return {
        "items": users,
        "total": total,
        "page": page,
        "size": size,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_previous": page > 1,
    }
