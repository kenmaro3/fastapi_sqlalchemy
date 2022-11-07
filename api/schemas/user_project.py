from pydantic import BaseModel
from typing import List

#from api.schemas.user import User
from api.schemas.user import Project


class UserProjectBase(BaseModel):
    user_id: int
    project_id: int

class UserProjectCreateRequest(UserProjectBase):
    pass
    #role: str

class UserProjectCreateResponse(UserProjectBase):
    id: int

    class Config:
        orm_mode = True

class UserProjectUpdateRequest(UserProjectBase):
    pass
    #role: str


class UserProjectUpdateResponse(UserProjectBase):
    id: int

    class Config:
        orm_mode = True


class UserProjectInDB(UserProjectBase):
    id: int

    class Config:
        orm_mode = True


class UserProject(UserProjectInDB):
    #users: List[User]
    projects: List[Project]