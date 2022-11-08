from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.schemas import scaler as scaler_schema
import api.cruds.scaler as scaler_crud
from api.db import get_db

from api.routers.base import router


@router.get("/scalers", response_model=List[scaler_schema.Scaler])
async def list_scalers(db: Session = Depends(get_db)):
    return await scaler_crud.get_scalers(db)

@router.post("/scalers", response_model=scaler_schema.ScalerCreateResponse)
async def create_scaler(
    scaler_body: scaler_schema.ScalerCreateRequest,
    db: Session = Depends(get_db)
):
    return await scaler_crud.create_scaler(db, scaler_body)


@router.put("/scalers/{scaler_id}", response_model=scaler_schema.ScalerUpdateResponse)
async def update_scaler(
    scaler_id: int, scaler_body: scaler_schema.ScalerUpdateRequest,
    db: Session = Depends(get_db)
):
    scaler = await scaler_crud.get_scaler(db, scaler_id=scaler_id)
    if scaler is None:
        raise HTTPException(status_code=404, detail="Scaler not found")

    return await scaler_crud.update_scaler(db, scaler_body, original=scaler)
    #return scaler_schema.ScalerCreateResponse(id=scaler_id, **scaler_body.dict())


@router.delete("/scalers/{scaler_id}", response_model=None)
async def delete_scaler(scaler_id: int, db: Session = Depends(get_db)):
    scaler = await scaler_crud.get_scaler(db, scaler_id=scaler_id)
    if scaler is None:
        raise HTTPException(status_code=404, detal="Scaler not fount")
    
    return await scaler_crud.delete_scaler(db, original=scaler)

