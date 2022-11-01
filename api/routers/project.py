from curses import intrflush
from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from api.schemas import project as project_schema
import api.cruds.project as project_crud
from api.schemas import intermediate_user_project as intermediate_user_project_schema
import api.cruds.intermediate_user_project as intermediate_user_project_crud
from api.db import get_db

from api.routers.base import router


@router.get("/projects", response_model=List[project_schema.Project])
async def list_projects(db: AsyncSession = Depends(get_db)):
    return await project_crud.get_projects(db)

@router.get("/projects/{project_id}", response_model=Optional[project_schema.Project])
async def get_project(
    project_id: int, db: AsyncSession = Depends(get_db)
):
    return await project_crud.get_project(db, project_id=project_id)

@router.post("/projects", response_model=project_schema.ProjectCreateResponse)
async def create_project(
    request_body: project_schema.ProjectCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    current_project = awai
    project = await project_crud.create_project(db, request_body)
    intermediate_to_create = intermediate_user_project_schema.IntermediateUserProjectCreateRequest(
        user_id = request_body.user_id,
        project_id = project.id,
        role = request_body.role
    )
    intermediate = intermediate_user_project_crud.create_intermediate_user_project(db, intermediate_to_create)
    return project

@router.post("/projects/{project_id}/join", response_model=project_schema.ProjectJoinResponse)
async def join_project(
    project_id: int,
    request_body: project_schema.ProjectJoinRequest,
    db: AsyncSession = Depends(get_db)
):
    project = await project_crud.get_project(db, project_id=project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    intermediate_current = await intermediate_user_project_crud.get_intermediate_user_project_by_user_and_project(
        db, user_id=request_body.user_id, project_id=project_id
    )
    if intermediate_current is not None:
        raise HTTPException(status_code=422, detail="This user already joined this project")

    intermediate_to_create = intermediate_user_project_schema.IntermediateUserProjectCreateRequest(
        user_id = request_body.user_id,
        project_id = project.id,
        role = request_body.role
    )
    intermediate = await intermediate_user_project_crud.create_intermediate_user_project(db, intermediate_to_create)
    return project


@router.put("/projects/{project_id}", response_model=project_schema.ProjectUpdateResponse)
async def update_project(
    project_id: int, project_body: project_schema.ProjectUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    project = await project_crud.get_project(db, project_id=project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return await project_crud.update_project(db, project_body, original=project)
    #return project_schema.ProjectCreateResponse(id=project_id, **project_body.dict())


@router.delete("/projects/{project_id}", response_model=None)
async def delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
    project = await project_crud.get_project(db, project_id=project_id)
    if project is None:
        raise HTTPException(status_code=404, detal="Project not fount")
    
    return await project_crud.delete_project(db, original=project)

