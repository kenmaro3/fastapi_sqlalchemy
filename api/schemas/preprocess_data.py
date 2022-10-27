from pydantic import BaseModel

class PreprocessDataBase(BaseModel):
    model_id: int
    data_id: int
    preprocess_type: str
    project_id: int

class PreprocessDataCreate(PreprocessDataBase):
    pass

class PreprocessDataCreateResponse(PreprocessDataCreate):
    id: int

    class Config:
        orm_mode = True

class PreprocessData(PreprocessDataBase):
    id: int

    class Config:
        orm_mode = True
