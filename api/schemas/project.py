from pydantic import BaseModel
from typing import List, Optional
from api.schemas import optimized_value

#from api.schemas.user import UserBase

#from api.schemas.model import Model
#from api.schemas.preprocess_data import PreprocessData
#from api.schemas.optimized_value import OptimizedValue
#from api.schemas.data import Data

class UserBase(BaseModel):
    name: Optional[str]
    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class ProjectCreateRequest(ProjectBase):
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
    id: int
    users: List[UserBase]
    #models: List[Model]
    #preprocess_datas: List[PreprocessData]
    #optimized_values: List[OptimizedValue]
    #datas: List[Data]
