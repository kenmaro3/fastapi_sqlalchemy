from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.models import model as model_model
import api.cruds.model as model_crud 
import api.schemas.model as model_schema
from api.db import get_db

from api.routers.base import router


@router.get("/models", response_model=List[model_schema.Model])
async def list_models(db: Session = Depends(get_db)):
    return await model_crud.get_models(db)

@router.get("/models/{model_id}", response_model=model_schema.Model)
async def get_model(model_id: int, db: Session = Depends(get_db)):
    return await model_crud.get_model(db, model_id=model_id)

@router.post("/models", response_model=model_schema.ModelCreateResponse)
async def create_model(
    request_body: model_schema.ModelCreateRequest,
    db: Session = Depends(get_db)
):
    return await model_crud.create_model(db, request_body)


@router.put("/models/{model_id}", response_model=model_schema.ModelUpdateResponse)
async def update_model(
    model_id: int, model_body: model_schema.ModelUpdateRequest,
    db: Session = Depends(get_db)
):
    model = await model_crud.get_model(db, model_id=model_id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")

    return await model_crud.update_model(db, model_body, original=model)
    #return model_schema.ModelCreateResponse(id=model_id, **model_body.dict())


@router.delete("/models/{model_id}", response_model=None)
async def delete_model(model_id: int, db: Session = Depends(get_db)):
    model = await model_crud.get_model(db, model_id=model_id)
    if model is None:
        raise HTTPException(status_code=404, detal="Model not fount")
    
    return await model_crud.delete_model(db, original=model)

