from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
#from sqlalchemy.ext.asyncio import Session
from sqlalchemy.orm import Session
from typing import List, Optional

from api.schemas import user as user_schema
import api.cruds.user as user_crud
from api.db import get_db

from api.routers.base import router


@router.get("/users", response_model=List[user_schema.User])
async def list_users(db: Session = Depends(get_db)):
    return await user_crud.get_users(db)

@router.get("/users/{user_id}", response_model=Optional[user_schema.User])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return await user_crud.get_user(db, user_id=user_id)


@router.post("/users", response_model=user_schema.UserCreateResponse)
async def create_user(
    user_body: user_schema.UserCreateRequest,
    db: Session = Depends(get_db)
):
    return await user_crud.create_user(db, user_body)


@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(
    user_id: int, user_body: user_schema.UserUpdateRequest,
    db: Session = Depends(get_db)
):
    user = await user_crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_crud.update_user(db, user_body, original=user)
    #return user_schema.UserCreateResponse(id=user_id, **user_body.dict())


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = await user_crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return await user_crud.delete_user(db, original=user)

