from pydantic import BaseModel
from typing import List, Optional

from api.schemas.optimized_value import OptimizedValue

from api.schemas.preprocess_data import PreprocessData

class ModelBase(BaseModel):
    project_id: int
    ref: str
    status: str
    estimated_time: int
    train_start_ts: str
    train_finish_ts: str
    parameters: str


class ModelCreate(ModelBase):
    pass

class ModelCreateResponse(ModelBase):
    id: int

    class Config:
        orm_mode = True

class ModelInDB(ModelBase):
    id: int

    class Config:
        orm_mode = True

class Model(ModelInDB):
    preprocess_datas: List[PreprocessData]
    optimized_values: List[OptimizedValue]