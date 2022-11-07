from typing import List, Tuple, Optional
from sqlalchemy.orm import Session

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload

import api.models.project as project_model
import api.schemas.project as project_schema

import api.models.user_project as user_project_model

import api.cruds.user as user_cruds


async def create_project(
    db: Session, project_create: project_schema.ProjectCreateRequest
) -> project_model.Project:
    #project = project_model.Project(**project_create.dict())
    user = await user_cruds.get_user(db, project_create.user_id)
    project = project_model.Project(
        name=project_create.name
    )
    #project.users.append(user)
    db.add(project)
    db.commit()

    user_project = user_project_model.UserProject(
        user_id=user.id, project_id=project.id,
        role=project_create.role
    )

    db.add(user_project)
    db.commit()
    #db.refresh(project) 
    return project


async def get_projects(db: Session) -> List[Tuple[str]]:
    # result: Result = db.execute(
    #         select(
    #             project_model.Project
    #             # project_model.Project.id,
    #             # project_model.Project.name,
    #         )
    #         .options(joinedload(project_model.Project.users))
    #     )
    result = db.query(project_model.Project)\
        .options(joinedload(project_model.Project.users))
    
    return result.all()



async def get_project(db: Session, project_id: int) -> Optional[project_model.Project]:
    result = db.query(project_model.Project).filter(project_model.Project.id == project_id)\
        .options(joinedload(project_model.Project.users))
    project: Optional[Tuple[project_model.Project]] = result.first()
    
    return project if project is not None else None

async def get_project_by_user_id(db: Session, user_id: int) -> List[Tuple[project_model.Project]]:
    projects = await get_projects(db)
    res = []
    for project in projects:
        for user in project.users:
            if user.user.id == user_id:
                res.append(project)
                continue
    return res


async def update_project(
    db: Session, project_create: project_schema.ProjectUpdateRequest,
    original: project_model.Project
) -> project_model.Project:
    original.name = project_create.name
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

async def add_user_to_project(
    db: Session, project_join: project_schema.ProjectJoinRequest,
    original: project_model.Project
    ) -> project_model.Project:
    
    user = await user_cruds.get_user(db, project_join.user_id)
    original.users.append(user)
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

async def delete_project(db: Session, original: project_model.Project) -> None:
    db.delete(original)
    db.commit()