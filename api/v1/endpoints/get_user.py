from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import UserModel
from schemas.user_schema import UserSchema
from core.database import get_db


api_router = APIRouter()


@api_router.get("/{user_id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado",
        )

    return user
