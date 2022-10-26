from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import user as user_schema
from typing import List

import cruds.user as user_crud
from db import get_db

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users():
    return [user_schema.User(id=1, name="test_user1")]


@router.post("/users", response_model=user_schema.UserCreateResponse)
async def create_user(
    user_body: user_schema.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await user_crud.create_user(db, user_body)


@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(user_id: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=user_id, **user_body.dict())


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return
