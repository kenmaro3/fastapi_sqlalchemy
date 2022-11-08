from typing import List, Tuple, Optional
#from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload

import api.models.data as data_model
import api.schemas.data as data_schema

import api.cruds.user as user_cruds
import api.cruds.project as project_cruds



async def create_data(
    db: Session, data_create: data_schema.DataCreateRequest
) -> data_model.Data:
    data = data_model.Data(**data_create.dict())
    db.add(data)
    db.commit()

    user = await user_cruds.get_user(db, data_create.user_id)
    user.datas.append(data)
    project = await project_cruds.get_project(db, data_create.project_id)
    project.datas.append(data)

    db.add(user)
    db.add(project)
    db.commit()

    db.refresh(data) 
    return data


async def get_datas(db: Session) -> List[data_model.Data]:
    # result: Result = await(
    #     db.execute(
    #         select(
    #             data_model.Data
    #             #data_model.Data.id,
    #             #data_model.Data.name,
    #             #data_model.Data.projects
    #         )
    #         .options(joinedload(data_model.Data.projects))
    #     )
    # )

    #datas = db.query(data_model.Data).options(joinedload(data_model.Data.projects))
    datas = db.query(data_model.Data)
    # result: Result = db.execute(
    #     select(data_model.Data)
    #     .options(joinedload(data_model.Data.projects))
    # )

    return datas.all()


async def get_data(db: Session, data_id: int) -> Optional[data_model.Data]:
    # result: Result = db.execute(
    #     select(data_model.Data).filter(data_model.Data.id == data_id)
    #     .options(joinedload(data_model.Data.projects))
    # )
    #result = db.query(data_model.Data).filter(data_model.Data.id == data_id)\
    #.options(joinedload(data_model.Data.projects).options(joinedload(data_project_model.DataProject.project)))
    
    result = db.query(data_model.Data).filter(data_model.Data.id == data_id)

    data: Optional[Tuple[data_model.Data]] = result.first()
    return data if data is not None else None


async def update_data(
    db: Session, data_update: data_schema.DataUpdateRequest,
    original: data_model.Data
) -> data_model.Data:
    original.name = data_update.name
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


async def delete_data(db: Session, original: data_model.Data) -> None:
    db.delete(original)
    db.commit()