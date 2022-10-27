from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.supplier as supplier_model
import api.schemas.supplier as supplier_schema

async def create_supplier(
    db: AsyncSession, supplier_create: supplier_schema.SupplierCreate
) -> supplier_model.Supplier:
    supplier = supplier_model.Supplier(**supplier_create.dict())
    db.add(supplier)
    await db.commit()
    await db.refresh(supplier)
    return supplier

async def get_suppliers(db: AsyncSession) -> List[Tuple[str]]:
    result: Result = await(
        db.execute(
            select(
                supplier_model.Supplier.id,
                supplier_model.Supplier.user_id,
                supplier_model.Supplier.project_id,
            )
        )
    )
    return result.all()

async def get_supplier(db: AsyncSession, supplier_id: int) -> Optional[supplier_model.Supplier]:
    result: Result = await db.execute(
        select(supplier_model.Supplier).filter(supplier_model.Supplier.id == supplier_id)
    )
    supplier: Optional[Tuple[supplier_model.Supplier]] = result.first()
    return supplier[0] if supplier is not None else None


async def update_supplier(
    db: AsyncSession, supplier_create: supplier_schema.SupplierCreate,
    original: supplier_model.Supplier
) -> supplier_model.Supplier:
    original.user_id = supplier_create.user_id
    original.project_id = supplier_create.project_id
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_supplier(db: AsyncSession, original: supplier_model.Supplier) -> None:
    await db.delete(original)
    await db.commit()