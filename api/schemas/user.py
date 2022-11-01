from pydantic import BaseModel
from typing import List, Optional

from api.schemas.project import Project

class UserBase(BaseModel):
    name: str

class UserCreateRequest(UserBase):
    name: str
    password: str

class UserUpdateRequest(UserBase):
    name: str
    password: str

class UserCreateResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserUpdateResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    name: str
    projects: Optional[List[Project]]

    class Config:
        orm_mode = True
