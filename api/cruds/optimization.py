from typing import List, Tuple, Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.optimization as optimization_model
import api.schemas.optimization as optimization_schema

import api.cruds.project as project_cruds

import api.models.project as project_model


async def create_optimization(
    db: Session, optimization_create: optimization_schema.OptimizationCreateRequest
) -> optimization_model.Optimization:
    #optimization = optimization_optimization.optimization(**optimization_create.dict())

    project = await project_cruds.get_project(db, optimization_create.project_id)

    optimization = optimization_model.Optimization(
        parameters = optimization_create.parameters,
        project_id = project.id
    )

    db.add(optimization)
    db.commit()

    project.optimizations.append(optimization)
    db.add(project)
    db.commit()

    return optimization


async def get_optimizations(db: Session) -> List[Tuple[optimization_model.Optimization]]:
    # result: Result = await(
    #     db.execute(
    #         select(
    #             optimization_optimization.optimization.id,
    #             optimization_optimization.optimization.project_id,
    #             optimization_optimization.optimization.project_id,
    #         )
    #     )
    # )
    optimizations = db.query(optimization_model.Optimization).options(joinedload(optimization_model.Optimization.project))
    return optimizations.all()


async def get_optimization(db: Session, optimization_id: int) -> Optional[optimization_model.Optimization]:
    optimization = db.query(optimization_model.Optimization).filter(optimization_model.Optimization.id == optimization_id)\
        .options(joinedload(optimization_model.Optimization.project))
    return optimization.first()


async def update_optimization(
    db: Session, optimization_create: optimization_schema.OptimizationCreateRequest,
    original: optimization_model.Optimization
) -> optimization_model.Optimization:
    original.name = optimization_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_optimization(db: Session, original: optimization_model.Optimization) -> None:
    await db.delete(original)
    await db.commit()