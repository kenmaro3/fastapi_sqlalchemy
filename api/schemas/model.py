from pydantic import BaseModel
from typing import List, Optional

from api.schemas.project import Project, ProjectBase
from api.schemas.scaler import ScalerBase
#from api.schemas.optimized_value import OptimizedValue

#from api.schemas.preprocess_data import PreprocessData

class ModelBase(BaseModel):
    ref: Optional[str]
    status: Optional[str]
    estimated_time: Optional[int]
    train_start_ts: Optional[str]
    train_finish_ts: Optional[str]
    parameters: Optional[str]

    class Config:
        orm_mode = True

class ModelCreateRequest(ModelBase):
    #data_id: int
    scaler_id: int
    project_id: int
    pass

class ModelCreateResponse(BaseModel):
    id: int
    class Config:
        orm_mode = True

class ModelUpdateRequest(ModelBase):
    pass

class ModelUpdateResponse(BaseModel):
    id: int

class Model(ModelBase):
    id: int
    project_id: int
    scaler: Optional[ScalerBase]
    #projects: Optional[List[ProjectBase]]
