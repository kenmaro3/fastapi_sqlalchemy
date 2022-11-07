from typing import List, Tuple, Optional
from sqlalchemy.orm import Session

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.intermediate_user_project as intermediate_user_project_model
import api.schemas.intermediate_user_project as intermediate_user_project_schema

async def create_intermediate_user_project(
    db: Session, intermediate_user_project_create: intermediate_user_project_schema.IntermediateUserProjectCreateRequest
) -> intermediate_user_project_model.IntermediateUserProject:
    intermediate_user_project = intermediate_user_project_model.IntermediateUserProject(
        user_id=intermediate_user_project_create.user_id,
        project_id=intermediate_user_project_create.project_id
    )
    
    db.add(intermediate_user_project)
    await db.commit()
    await db.refresh(intermediate_user_project)
    return intermediate_user_project


async def get_intermediate_user_projects(db: Session) -> List[Tuple[str]]:
    result: Result = await(
        db.execute(
            select(
                intermediate_user_project_model.IntermediateUserProject.id,
                intermediate_user_project_model.IntermediateUserProject.user_id,
                intermediate_user_project_model.IntermediateUserProject.project_id,
            )
        )
    )
    return result.all()


async def get_intermediate_user_project(db: Session, intermediate_user_project_id: int) -> Optional[intermediate_user_project_model.IntermediateUserProject]:
    result: Result = await db.execute(
        select(intermediate_user_project_model.IntermediateUserProject).filter(intermediate_user_project_model.IntermediateUserProject.id == intermediate_user_project_id)
    )
    intermediate_user_project: Optional[Tuple[intermediate_user_project_model.IntermediateUserProject]] = result.first()
    return intermediate_user_project[0] if intermediate_user_project is not None else None

async def get_intermediate_user_project_by_user_and_project(db: Session, user_id: int, project_id) -> Optional[intermediate_user_project_model.IntermediateUserProject]:
    result: Result = await db.execute(
        select(intermediate_user_project_model.IntermediateUserProject)
        .filter(intermediate_user_project_model.IntermediateUserProject.user_id == user_id)
        .filter(intermediate_user_project_model.IntermediateUserProject.project_id == project_id)
    )
    intermediate_user_project: Optional[Tuple[intermediate_user_project_model.IntermediateUserProject]] = result.first()
    return intermediate_user_project[0] if intermediate_user_project is not None else None


async def update_intermediate_user_project(
    db: Session, intermediate_user_project_create: intermediate_user_project_schema.IntermediateUserProjectUpdateRequest,
    original: intermediate_user_project_model.IntermediateUserProject
) -> intermediate_user_project_model.IntermediateUserProject:
    original.user_id = intermediate_user_project_create.user_id
    original.project_id = intermediate_user_project_create.project_id
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_intermediate_user_project(db: Session, original: intermediate_user_project_model.IntermediateUserProject) -> None:
    await db.delete(original)
    await db.commit()