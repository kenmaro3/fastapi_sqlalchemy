from pydantic import BaseModel

class OptimizedValueBase(BaseModel):
    model_id: int
    data_id: int
    parameters: str
    project_id: int

class OptimizedValueCreate(OptimizedValueBase):
    pass

class OptimizedValueCreateResponse(OptimizedValueCreate):
    id: int

    class Config:
        orm_mode = True

class OptimizedValue(OptimizedValueBase):
    id: int

    class Config:
        orm_mode = True
