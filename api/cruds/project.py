from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.project as project_model
import api.schemas.project as project_schema


async def create_project(
    db: AsyncSession, project_create: project_schema.ProjectCreate
) -> project_model.Project:
    project = project_model.Project(**project_create.dict())
    db.add(project)
    await db.commit()
    await db.refresh(project) 
    return project


async def get_projects(db: AsyncSession) -> List[Tuple[str]]:
    result: Result = await(
        db.execute(
            select(
                project_model.Project.id,
                project_model.Project.name,
            )
        )
    )
    return result.all()


async def get_project(db: AsyncSession, project_id: int) -> Optional[project_model.Project]:
    result: Result = await db.execute(
        select(project_model.Project).filter(project_model.Project.id == project_id)
    )
    project: Optional[Tuple[project_model.Project]] = result.first()
    return project[0] if project is not None else None


async def update_project(
    db: AsyncSession, project_create: project_schema.ProjectCreate,
    original: project_model.Project
) -> project_model.Project:
    original.name = project_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_project(db: AsyncSession, original: project_model.Project) -> None:
    await db.delete(original)
    await db.commit()