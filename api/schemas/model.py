from pydantic import BaseModel

class ModelBase(BaseModel):
    project_id: int
    ref: str
    status: str
    estimated_time: int
    train_start_ts: str
    train_finish_ts: str
    parameters: str


class ModelCreate(ModelBase):
    pass

class ModelCreateResponse(ModelCreate):
    id: int

    class Config:
        orm_mode = True

class Model(ModelBase):
    id: int

    class Config:
        orm_mode = True
