from pydantic import BaseModel

class DataBase(BaseModel):
    ref: str
    user_id: int
    project_id: int

class DataCreate(DataBase):
    pass

class DataCreateResponse(DataCreate):
    id: int

    class Config:
        orm_mode = True

class Data(DataBase):
    id: int

    class Config:
        orm_mode = True
