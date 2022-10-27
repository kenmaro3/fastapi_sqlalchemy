from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.buyer as buyer_model
import api.schemas.buyer as buyer_schema

async def create_buyer(
    db: AsyncSession, buyer_create: buyer_schema.BuyerCreate
) -> buyer_model.Buyer:
    buyer = buyer_model.Buyer(**buyer_create.dict())
    db.add(buyer)
    await db.commit()
    await db.refresh(buyer)
    return buyer

async def get_buyers(db: AsyncSession) -> List[Tuple[str]]:
    result: Result = await(
        db.execute(
            select(
                buyer_model.Buyer.id,
                buyer_model.Buyer.user_id,
                buyer_model.Buyer.project_id,
            )
        )
    )
    return result.all()

async def get_buyer(db: AsyncSession, buyer_id: int) -> Optional[buyer_model.Buyer]:
    result: Result = await db.execute(
        select(buyer_model.Buyer).filter(buyer_model.Buyer.id == buyer_id)
    )
    buyer: Optional[Tuple[buyer_model.Buyer]] = result.first()
    return buyer[0] if buyer is not None else None


async def update_buyer(
    db: AsyncSession, buyer_create: buyer_schema.BuyerCreate,
    original: buyer_model.Buyer
) -> buyer_model.Buyer:
    original.user_id = buyer_create.user_id
    original.project_id = buyer_create.project_id
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_buyer(db: AsyncSession, original: buyer_model.Buyer) -> None:
    await db.delete(original)
    await db.commit()