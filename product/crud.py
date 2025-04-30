from typing import Any, Type, Coroutine

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from src.models import Product
from .schemas import ProductSchema, ProductIn


async def get_all(session: AsyncSession) -> list[ProductSchema]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)



async def get_by_id(session: AsyncSession, item_id: int) -> ProductSchema | None:
    return await session.get(Product, item_id)


async def create(session: AsyncSession, product: ProductSchema) -> Product:
    new_product = Product(**product.model_dump())
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product



async def update_item(session: AsyncSession, item_id: int, new_name: str) -> Type[Product] | None:
    product = await session.get(Product, item_id)
    if product:
        product.name = new_name
        await session.commit()
        await session.refresh(product)
        return product

    else:
        return None


async def delete_item(session: AsyncSession, item_id: int) -> bool:
    product = await session.get(Product, item_id)
    if product:
        await session.delete(product)
        await session.commit()
        return True

    else:
        return False


