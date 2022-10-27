from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.preprocess_data as preprocess_data_model
import api.schemas.preprocess_data as preprocess_data_schema


async def create_preprocess_data(
    db: AsyncSession, preprocess_data_create: preprocess_data_schema.PreprocessDataCreate
) -> preprocess_data_model.PreprocessData:
    preprocess_data = preprocess_data_model.PreprocessData(**preprocess_data_create.dict())
    db.add(preprocess_data)
    await db.commit()
    await db.refresh(preprocess_data) 
    return preprocess_data


async def get_preprocess_datas(db: AsyncSession) -> List[Tuple[str]]:
    result: Result = await(
        db.execute(
            select(
                preprocess_data_model.PreprocessData.id,
                preprocess_data_model.PreprocessData.project_id,
                preprocess_data_model.PreprocessData.project_id,
            )
        )
    )
    return result.all()


async def get_preprocess_data(db: AsyncSession, preprocess_data_id: int) -> Optional[preprocess_data_model.PreprocessData]:
    result: Result = await db.execute(
        select(preprocess_data_model.PreprocessData).filter(preprocess_data_model.PreprocessData.id == preprocess_data_id)
    )
    preprocess_data: Optional[Tuple[preprocess_data_model.PreprocessData]] = result.first()
    return preprocess_data[0] if preprocess_data is not None else None


async def update_preprocess_data(
    db: AsyncSession, preprocess_data_create: preprocess_data_schema.PreprocessDataCreate,
    original: preprocess_data_model.PreprocessData
) -> preprocess_data_model.PreprocessData:
    original.name = preprocess_data_create.name
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_preprocess_data(db: AsyncSession, original: preprocess_data_model.PreprocessData) -> None:
    await db.delete(original)
    await db.commit()