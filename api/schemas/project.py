from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class ProjectCreateResponse(ProjectCreate):
    id: int

    class Config:
        orm_mode = True

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
