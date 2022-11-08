from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.schemas import optimization as optimization_schema
import api.cruds.optimization as optimization_crud
from api.db import get_db

from api.routers.base import router


@router.get("/optimizations", response_model=List[optimization_schema.Optimization])
async def list_optimizations(db: Session = Depends(get_db)):
    return await optimization_crud.get_optimizations(db)

@router.get("/optimizations/{optimization_id}", response_model=optimization_schema.Optimization)
async def get_optimization(optimization_id: int, db: Session = Depends(get_db)):
    return await optimization_crud.get_optimization(db, optimization_id=optimization_id)

@router.post("/optimizations", response_model=optimization_schema.OptimizationCreateResponse)
async def create_optimization(
    optimization_body: optimization_schema.OptimizationCreateRequest,
    db: Session = Depends(get_db)
):
    return await optimization_crud.create_optimization(db, optimization_body)


@router.put("/optimizations/{optimization_id}", response_model=optimization_schema.OptimizationUpdateResponse)
async def update_optimization(
    optimization_id: int, optimization_body: optimization_schema.OptimizationUpdateRequest,
    db: Session = Depends(get_db)
):
    optimization = await optimization_crud.get_optimization(db, optimization_id=optimization_id)
    if optimization is None:
        raise HTTPException(status_code=404, detail="Optimization not found")

    return await optimization_crud.update_optimization(db, optimization_body, original=optimization)
    #return optimization_schema.OptimizationCreateResponse(id=optimization_id, **optimization_body.dict())


@router.delete("/optimizations/{optimization_id}", response_model=None)
async def delete_optimization(optimization_id: int, db: Session = Depends(get_db)):
    optimization = await optimization_crud.get_optimization(db, optimization_id=optimization_id)
    if optimization is None:
        raise HTTPException(status_code=404, detal="Optimization not fount")
    
    return await optimization_crud.delete_optimization(db, original=optimization)

