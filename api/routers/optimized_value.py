from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.schemas import supplier as supplier_schema
import api.cruds.supplier as supplier_crud
from api.db import get_db

from api.routers.base import router


@router.get("/optimized_values", response_model=List[supplier_schema.OptimizedValue])
async def list_optimized_values(db: Session = Depends(get_db)):
    return await supplier_crud.get_optimized_values(db)

@router.post("/optimized_values", response_model=supplier_schema.OptimizedValueCreateResponse)
async def create_supplier(
    supplier_body: supplier_schema.OptimizedValueCreateRequest,
    db: Session = Depends(get_db)
):
    return await supplier_crud.create_supplier(db, supplier_body)


@router.put("/optimized_values/{supplier_id}", response_model=supplier_schema.OptimizedValueUpdateResponse)
async def update_supplier(
    supplier_id: int, supplier_body: supplier_schema.OptimizedValueUpdateRequest,
    db: Session = Depends(get_db)
):
    supplier = await supplier_crud.get_supplier(db, supplier_id=supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detail="OptimizedValue not found")

    return await supplier_crud.update_supplier(db, supplier_body, original=supplier)
    #return supplier_schema.OptimizedValueCreateResponse(id=supplier_id, **supplier_body.dict())


@router.delete("/optimized_values/{supplier_id}", response_model=None)
async def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = await supplier_crud.get_supplier(db, supplier_id=supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detal="OptimizedValue not fount")
    
    return await supplier_crud.delete_supplier(db, original=supplier)

