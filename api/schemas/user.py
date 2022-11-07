from pydantic import BaseModel, Field
from typing import List, Optional

from api.schemas.project import Project, ProjectBase

class UserBase(BaseModel):
    id: int = Field(alias="user_id")
    name: str = Field(alias="user_name")
    role: Optional[str]
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class UserCreateRequest(BaseModel):
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
    projects: Optional[List[ProjectBase]]

    class Config:
        orm_mode = True
