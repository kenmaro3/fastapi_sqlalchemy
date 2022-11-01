from pydantic import BaseModel
from typing import List

from api.schemas.user import User
from api.schemas.project import Project


class IntermediateUserProjectBase(BaseModel):
    user_id: int
    project_id: int

class IntermediateUserProjectCreateRequest(IntermediateUserProjectBase):
    role: str

class IntermediateUserProjectCreateResponse(IntermediateUserProjectBase):
    id: int

    class Config:
        orm_mode = True

class IntermediateUserProjectUpdateRequest(IntermediateUserProjectBase):
    role: str


class IntermediateUserProjectUpdateResponse(IntermediateUserProjectBase):
    id: int

    class Config:
        orm_mode = True


class IntermediateUserProjectInDB(IntermediateUserProjectBase):
    id: int

    class Config:
        orm_mode = True


class IntermediateUserProject(IntermediateUserProjectInDB):
    users: List[User]
    projects: List[Project]