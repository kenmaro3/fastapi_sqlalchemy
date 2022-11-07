from typing import List, Tuple, Optional
#from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload

import api.models.user as user_model
import api.schemas.user as user_schema


async def create_user(
    db: Session, user_create: user_schema.UserCreateRequest
) -> user_model.User:
    user = user_model.User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user) 
    return user


async def get_users(db: Session) -> List[user_model.User]:
    # result: Result = await(
    #     db.execute(
    #         select(
    #             user_model.User
    #             #user_model.User.id,
    #             #user_model.User.name,
    #             #user_model.User.projects
    #         )
    #         .options(joinedload(user_model.User.projects))
    #     )
    # )

    users = db.query(user_model.User).options(joinedload(user_model.User.projects))
    # result: Result = db.execute(
    #     select(user_model.User)
    #     .options(joinedload(user_model.User.projects))
    # )

    return users.all()


async def get_user(db: Session, user_id: int) -> Optional[user_model.User]:
    # result: Result = db.execute(
    #     select(user_model.User).filter(user_model.User.id == user_id)
    #     .options(joinedload(user_model.User.projects))
    # )
    result = db.query(user_model.User).filter(user_model.User.id == user_id)\
    .options(joinedload(user_model.User.projects))

    user: Optional[Tuple[user_model.User]] = result.first()
    return user if user is not None else None


async def update_user(
    db: Session, user_update: user_schema.UserUpdateRequest,
    original: user_model.User
) -> user_model.User:
    original.name = user_update.name
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


async def delete_user(db: Session, original: user_model.User) -> None:
    db.delete(original)
    db.commit()