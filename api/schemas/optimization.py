from pydantic import BaseModel

class OptimizationBase(BaseModel):
    parameters: str
    project_id: int

    class Config:
        orm_mode = True

class OptimizationCreateRequest(OptimizationBase):
    pass

class OptimizationCreateResponse(OptimizationBase):
    id: int

class OptimizationUpdateRequest(OptimizationBase):
    optimized_xs_ref: str
    pass

class OptimizationUpdateResponse(BaseModel):
    id: int


class Optimization(OptimizationBase):
    id: int

