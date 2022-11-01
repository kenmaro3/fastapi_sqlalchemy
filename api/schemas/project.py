from pydantic import BaseModel
from typing import List, Optional
from api.schemas import optimized_value

#from api.schemas.model import Model
#from api.schemas.preprocess_data import PreprocessData
#from api.schemas.optimized_value import OptimizedValue
#from api.schemas.data import Data

class ProjectBase(BaseModel):
    name: str

class ProjectCreateRequest(ProjectBase):
    user_id: int
    role: str

class ProjectCreateResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True


class ProjectJoinRequest(ProjectBase):
    user_id: int
    role: str

class ProjectJoinResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True


class ProjectUpdateRequest(ProjectBase):
    pass


class ProjectUpdateResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True


class ProjectInDB(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class Project(ProjectInDB):
    id: int
    pass
    #models: List[Model]
    #preprocess_datas: List[PreprocessData]
    #optimized_values: List[OptimizedValue]
    #datas: List[Data]
