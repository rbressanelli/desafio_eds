from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from ....models.user import UserModel
from ....schemas.user_schema import UserSchema, UserCreateSchema
from ....core.database import get_db


api_router = APIRouter()


@api_router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserSchema)
async def create_user(
    user: UserCreateSchema,
    db: AsyncSession = Depends(get_db),
):
    db_user = UserModel(
        name=user.name, surname=user.surname, email=user.email, age=user.age
    )
    db.add(db_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado",
        )

    await db.refresh(db_user)
    return db_user
