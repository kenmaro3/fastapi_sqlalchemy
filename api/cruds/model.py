from typing import List, Tuple, Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.model as model_model
import api.schemas.model as model_schema

import api.cruds.project as project_cruds

import api.models.project as project_model


async def create_model(
    db: Session, model_create: model_schema.ModelCreateRequest
) -> model_model.Model:
    #model = model_model.Model(**model_create.dict())

    project = await project_cruds.get_project(db, model_create.project_id)

    model = model_model.Model(
        scaler_id = model_create.scaler_id,
        project_id = model_create.project_id,

        ref = model_create.ref,
        status = model_create.status,
        estimated_time = model_create.estimated_time,
        train_start_ts = model_create.train_start_ts,
        train_finish_ts = model_create.train_finish_ts,
        parameters = model_create.parameters,


    )

    #db.add(model)
    #db.commit()

    project.models.append(model)
    db.add(project)
    db.commit()

    return model


async def get_models(db: Session) -> List[Tuple[model_model.Model]]:
    # result: Result = await(
    #     db.execute(
    #         select(
    #             model_model.Model.id,
    #             model_model.Model.project_id,
    #             model_model.Model.project_id,
    #         )
    #     )
    # )
    models = db.query(model_model.Model).options(joinedload(model_model.Model.project))
    print("\n\nhere model!")
    print(models)
    return models.all()


async def get_model(db: Session, model_id: int) -> Optional[model_model.Model]:
    # result: Result = await db.execute(
    #     select(model_model.Model).filter(model_model.Model.id == model_id) \
    # )
    model = db.query(model_model.Model).filter(model_model.Model.id == model_id).options(joinedload(model_model.Model.project))
    #model: Optional[Tuple[model_model.Model]] = result.first()
    return model.first()


async def update_model(
    db: Session, model_create: model_schema.ModelCreateRequest,
    original: model_model.Model
) -> model_model.Model:
    original.name = model_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_model(db: Session, original: model_model.Model) -> None:
    await db.delete(original)
    await db.commit()