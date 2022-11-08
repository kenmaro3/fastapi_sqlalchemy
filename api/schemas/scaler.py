from pydantic import BaseModel

class ScalerBase(BaseModel):
    preprocess_type: str
    #model_id: int
    data_id: int
    project_id: int
    pass
    class Config:
        orm_mode = True

class ScalerCreateRequest(ScalerBase):
    pass

class ScalerCreateResponse(ScalerBase):
    id: int

class ScalerUpdateRequest(ScalerBase):
    pass

class ScalerUpdateResponse(ScalerBase):
    id: int


class Scaler(ScalerBase):
    id: int

    class Config:
        orm_mode = True
