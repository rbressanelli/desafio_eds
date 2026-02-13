from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from ....models.user import UserModel
from ....schemas.user_schema import UserSchema, UserUpdateSchema
from ....core.database import get_db


api_router = APIRouter()


@api_router.patch(
    "/{user_id}", response_model=UserSchema, status_code=status.HTTP_202_ACCEPTED
)
async def update_user(
    user_id: int, user_data: UserUpdateSchema, db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(UserModel).where(UserModel.id == user_id))
    user = result.scalar_one_or_none()

    if user:
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)

        try:
            await db.commit()
        except IntegrityError:
            await db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email já cadastrado",
            )
        await db.refresh(user)

        return user

    raise HTTPException(detail="User not found!", status_code=status.HTTP_404_NOT_FOUND)
