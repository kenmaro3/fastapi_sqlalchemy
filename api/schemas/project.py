from pydantic import BaseModel, Field
from typing import List, Optional

#from api.schemas.user import UserBase

#from api.schemas.model import Model
#from api.schemas.preprocess_data import PreprocessData
#from api.schemas.optimized_value import OptimizedValue
#from api.schemas.data import Data

class OptimizationBase(BaseModel):
    parameters: str
    project_id: int

    class Config:
        orm_mode = True

class DataBase(BaseModel):
    ref_x: str
    ref_y: str
    user_id: int
    project_id: int
    class Config:
        orm_mode = True
class ModelBase(BaseModel):
    project_id: int
    ref: Optional[str]
    status: Optional[str]
    estimated_time: Optional[int]
    train_start_ts: Optional[str]
    train_finish_ts: Optional[str]
    parameters: Optional[str]

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    id: int = Field(alias="user_id")
    name: str = Field(alias="user_name")
    role: Optional[str]
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class ProjectBase(BaseModel):
    id: int = Field(alias="project_id")
    name: str = Field(alias="project_name")
    role: Optional[str]
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class ProjectCreateRequest(BaseModel):
    name: str
    user_id: int
    role: str

class ProjectCreateResponse(ProjectBase):
    id: int



class ProjectJoinRequest(BaseModel):
    user_id: int
    role: str

class ProjectJoinResponse(ProjectBase):
    id: int



class ProjectUpdateRequest(ProjectBase):
    pass


class ProjectUpdateResponse(ProjectBase):
    id: int



class Project(ProjectBase):
    users: List[UserBase]
    models: List[ModelBase]
    #preprocess_datas: List[PreprocessData]
    optimizations: List[OptimizationBase]
    datas: List[DataBase]
