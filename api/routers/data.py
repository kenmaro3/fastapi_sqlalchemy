from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.schemas import supplier as supplier_schema
import api.cruds.supplier as supplier_crud
from api.db import get_db

from api.routers.base import router


@router.get("/datas", response_model=List[supplier_schema.Data])
async def list_datas(db: Session = Depends(get_db)):
    return await supplier_crud.get_datas(db)

@router.post("/datas", response_model=supplier_schema.DataCreateResponse)
async def create_supplier(
    supplier_body: supplier_schema.DataCreateRequest,
    db: Session = Depends(get_db)
):
    return await supplier_crud.create_supplier(db, supplier_body)


@router.put("/datas/{supplier_id}", response_model=supplier_schema.DataUpdateResponse)
async def update_supplier(
    supplier_id: int, supplier_body: supplier_schema.DataUpdateRequest,
    db: Session = Depends(get_db)
):
    supplier = await supplier_crud.get_supplier(db, supplier_id=supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detail="Data not found")

    return await supplier_crud.update_supplier(db, supplier_body, original=supplier)
    #return supplier_schema.DataCreateResponse(id=supplier_id, **supplier_body.dict())


@router.delete("/datas/{supplier_id}", response_model=None)
async def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = await supplier_crud.get_supplier(db, supplier_id=supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detal="Data not fount")
    
    return await supplier_crud.delete_supplier(db, original=supplier)

