from pydantic import BaseModel

class SupplierBase(BaseModel):
    user_id: int
    project_id: int

class SupplierCreate(SupplierBase):
    pass

class SupplierCreateResponse(SupplierCreate):
    id: int

    class Config:
        orm_mode = True

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True