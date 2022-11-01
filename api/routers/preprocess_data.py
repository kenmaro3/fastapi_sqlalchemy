from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from api.schemas import supplier as supplier_schema
import api.cruds.supplier as supplier_crud
from api.db import get_db

from api.routers.base import router


@router.get("/preprocess_datas", response_model=List[supplier_schema.PreprocessData])
async def list_preprocess_datas(db: AsyncSession = Depends(get_db)):
    return await supplier_crud.get_preprocess_datas(db)

@router.post("/preprocess_datas", response_model=supplier_schema.PreprocessDataCreateResponse)
async def create_supplier(
    supplier_body: supplier_schema.PreprocessDataCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    return await supplier_crud.create_supplier(db, supplier_body)


@router.put("/preprocess_datas/{supplier_id}", response_model=supplier_schema.PreprocessDataUpdateResponse)
async def update_supplier(
    supplier_id: int, supplier_body: supplier_schema.PreprocessDataUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    supplier = await supplier_crud.get_supplier(db, supplier_id=supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detail="PreprocessData not found")

    return await supplier_crud.update_supplier(db, supplier_body, original=supplier)
    #return supplier_schema.PreprocessDataCreateResponse(id=supplier_id, **supplier_body.dict())


@router.delete("/preprocess_datas/{supplier_id}", response_model=None)
async def delete_supplier(supplier_id: int, db: AsyncSession = Depends(get_db)):
    supplier = await supplier_crud.get_supplier(db, supplier_id=supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detal="PreprocessData not fount")
    
    return await supplier_crud.delete_supplier(db, original=supplier)

