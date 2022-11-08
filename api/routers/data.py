from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.schemas import data as data_schema
import api.cruds.data as data_crud
from api.db import get_db

from api.routers.base import router


@router.get("/datas", response_model=List[data_schema.Data])
async def list_datas(db: Session = Depends(get_db)):
    return await data_crud.get_datas(db)

@router.post("/datas", response_model=data_schema.DataCreateResponse)
async def create_data(
    data_body: data_schema.DataCreateRequest,
    db: Session = Depends(get_db)
):
    return await data_crud.create_data(db, data_body)


@router.put("/datas/{data_id}", response_model=data_schema.DataUpdateResponse)
async def update_data(
    data_id: int, data_body: data_schema.DataUpdateRequest,
    db: Session = Depends(get_db)
):
    data = await data_crud.get_data(db, data_id=data_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")

    return await data_crud.update_data(db, data_body, original=data)
    #return data_schema.DataCreateResponse(id=data_id, **data_body.dict())


@router.delete("/datas/{data_id}", response_model=None)
async def delete_data(data_id: int, db: Session = Depends(get_db)):
    data = await data_crud.get_data(db, data_id=data_id)
    if data is None:
        raise HTTPException(status_code=404, detal="Data not fount")
    
    return await data_crud.delete_data(db, original=data)

