from fastapi import APIRouter, status, Depends, HTTPException
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import UserModel
from schemas.user_schema import UserSchema
from core.database import get_db


api_router = APIRouter()


@api_router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserSchema])
async def get_users(
    name: Optional[str] = None,
    email: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    query = select(UserModel)

    # Filtro por name (case insensitive)
    if name:
        query = query.where(UserModel.name.ilike(f"%{name}%"))

    # Filtro por email (case insensitive)
    if email:
        query = query.where(UserModel.email.ilike(f"%{email}%"))

    # Paginação
    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    users = result.scalars().all()

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuários não encontrados",
        )

    return users