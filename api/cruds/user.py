from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.user as user_model
import api.schemas.user as user_schema


async def create_user(
    db: AsyncSession, user_create: user_schema.UserCreate
) -> user_model.User:
    user = user_model.User(**user_create.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user) 
    return user


async def get_users(db: AsyncSession) -> List[Tuple[str]]:
    result: Result = await(
        db.execute(
            select(
                user_model.User.id,
                user_model.User.name,
            )
        )
    )
    return result.all()


async def get_user(db: AsyncSession, user_id: int) -> Optional[user_model.User]:
    result: Result = await db.execute(
        select(user_model.User).filter(user_model.User.id == user_id)
    )
    user: Optional[Tuple[user_model.User]] = result.first()
    return user[0] if user is not None else None


async def update_user(
    db: AsyncSession, user_create: user_schema.UserCreate,
    original: user_model.User
) -> user_model.User:
    original.name = user_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_user(db: AsyncSession, original: user_model.User) -> None:
    await db.delete(original)
    await db.commit()