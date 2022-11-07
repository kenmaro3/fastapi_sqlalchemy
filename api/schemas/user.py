from pydantic import BaseModel
from typing import List, Optional

from api.schemas.project import Project, ProjectBase

class UserBase(BaseModel):
    name: str
    class Config:
        orm_mode = True

class UserCreateRequest(UserBase):
    name: str
    password: str

class UserUpdateRequest(UserBase):
    name: str
    password: str

class UserCreateResponse(UserBase):
    id: int

class UserUpdateResponse(UserBase):
    id: int

class User(UserBase):
    id: int
    projects: Optional[List[ProjectBase]]

    class Config:
        orm_mode = True
