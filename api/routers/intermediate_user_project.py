from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.schemas import intermediate_user_project as intermediate_user_project_schema
import api.cruds.intermediate_user_project as intermediate_user_project_crud
from api.db import get_db

from api.routers.base import router


@router.get("/intermediate_user_projects", response_model=List[intermediate_user_project_schema.IntermediateUserProject])
async def list_intermediate_user_projects(db: AsyncSession = Depends(get_db)):
    return await intermediate_user_project_crud.get_intermediate_user_projects(db)

@router.post("/intermediate_user_projects", response_model=intermediate_user_project_schema.IntermediateUserProject)
async def create_intermediate_user_project(
    intermediate_user_project_body: intermediate_user_project_schema.IntermediateUserProjectCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    return await intermediate_user_project_crud.create_intermediate_user_project(db, intermediate_user_project_body)


@router.put("/intermediate_user_projects/{intermediate_user_project_id}", response_model=intermediate_user_project_schema.IntermediateUserProjectUpdateResponse)
async def update_intermediate_user_project(
    intermediate_user_project_id: int, intermediate_user_project_body: intermediate_user_project_schema.IntermediateUserProjectUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    intermediate_user_project = await intermediate_user_project_crud.get_intermediate_user_project(db, intermediate_user_project_id=intermediate_user_project_id)
    if intermediate_user_project is None:
        raise HTTPException(status_code=404, detail="intermediate_user_project not found")

    return await intermediate_user_project_crud.update_intermediate_user_project(db, intermediate_user_project_body, original=intermediate_user_project)
    #return intermediate_user_project_schema.intermediate_user_projectCreateResponse(id=intermediate_user_project_id, **intermediate_user_project_body.dict())


@router.delete("/intermediate_user_projects/{intermediate_user_project_id}", response_model=None)
async def delete_intermediate_user_project(intermediate_user_project_id: int, db: AsyncSession = Depends(get_db)):
    intermediate_user_project = await intermediate_user_project_crud.get_intermediate_user_project(db, intermediate_user_project_id=intermediate_user_project_id)
    if intermediate_user_project is None:
        raise HTTPException(status_code=404, detal="intermediate_user_project not fount")
    
    return await intermediate_user_project_crud.delete_intermediate_user_project(db, original=intermediate_user_project)

