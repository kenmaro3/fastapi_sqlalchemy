from pydantic import BaseModel

class DataBase(BaseModel):
    ref_x: str
    ref_y: str
    user_id: int
    project_id: int
    class Config:
        orm_mode = True

class DataCreateRequest(DataBase):
    pass

class DataCreateResponse(DataBase):
    id: int

class DataUpdateRequest(DataBase):
    pass

class DataUpdateResponse(DataBase):
    id: int



class Data(DataBase):
    id: int

    class Config:
        orm_mode = True
