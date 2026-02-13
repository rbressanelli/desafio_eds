from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ....models.user import UserModel
from ....core.database import get_db


api_router = APIRouter()


@api_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = result.scalar_one_or_none()

    if user:
        await db.delete(user)
        await db.commit()

        return

    raise HTTPException(detail="User not found!", status_code=status.HTTP_404_NOT_FOUND)
