from pydantic import BaseModel

class BuyerBase(BaseModel):
    user_id: int
    project_id: int

class BuyerCreate(BuyerBase):
    pass

class BuyerCreateResponse(BuyerCreate):
    id: int

    class Config:
        orm_mode = True

class Buyer(BuyerBase):
    id: int

    class Config:
        orm_mode = True