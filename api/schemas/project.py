from pydantic import BaseModel
from typing import List, Optional
from api.schemas import optimized_value

from api.schemas.model import Model
from api.schemas.preprocess_data import PreprocessData
from api.schemas.optimized_value import OptimizedValue

class ProjectBase(BaseModel):
    name: str

class ProjectCreateRequest(ProjectBase):
    pass

class ProjectCreateResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class ProjectInDB(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class Project(ProjectInDB):
    models: List[Model]
    preprocess_datas: List[PreprocessData]
    optimized_values: List[OptimizedValue]
