from typing import List, Tuple, Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.scaler as scaler_model
import api.schemas.scaler as scaler_schema

import api.cruds.project as project_cruds

import api.models.project as project_model


async def create_scaler(
    db: Session, scaler_create: scaler_schema.ScalerCreateRequest
) -> scaler_model.Scaler:
    #scaler = scaler_scaler.scaler(**scaler_create.dict())

    project = await project_cruds.get_project(db, scaler_create.project_id)

    scaler = scaler_model.Scaler(
        data_id = scaler_create.data_id,
        preprocess_type = scaler_create.preprocess_type,
        project_id = scaler_create.project_id
    )

    db.add(scaler)
    db.commit()

    project.scalers.append(scaler)
    db.add(project)
    db.commit()

    return scaler


async def get_scalers(db: Session) -> List[Tuple[scaler_model.Scaler]]:
    # result: Result = await(
    #     db.execute(
    #         select(
    #             scaler_scaler.scaler.id,
    #             scaler_scaler.scaler.project_id,
    #             scaler_scaler.scaler.project_id,
    #         )
    #     )
    # )
    scalers = db.query(scaler_model.Scaler).options(joinedload(scaler_model.Scaler.project))
    return scalers.all()


async def get_scaler(db: Session, scaler_id: int) -> Optional[scaler_model.Scaler]:
    result: Result = await db.execute(
        select(scaler_model.Scaler).filter(scaler_model.Scaler.id == scaler_id)
    )
    scaler: Optional[Tuple[scaler_model.Scaler]] = result.first()
    return scaler[0] if scaler is not None else None


async def update_scaler(
    db: Session, scaler_create: scaler_schema.ScalerCreateRequest,
    original: scaler_model.Scaler
) -> scaler_model.Scaler:
    original.name = scaler_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_scaler(db: Session, original: scaler_model.Scaler) -> None:
    await db.delete(original)
    await db.commit()