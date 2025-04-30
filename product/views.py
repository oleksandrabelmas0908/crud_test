from fastapi import APIRouter, HTTPException, status, Depends

from .crud import create, get_by_id, update_item, delete_item, get_all
from .schemas import ProductSchema
from src.models import db_helper

from sqlalchemy.ext.asyncio import AsyncSession


product_router = APIRouter(prefix="/product")


@product_router.get("/{product_id}", response_model=ProductSchema)
async def get_product(
        product_id: int,
        session:AsyncSession = Depends(db_helper.session_dependency),
):
    product = await get_by_id(session=session, item_id=product_id)
    if product:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
    )


@product_router.get("/", response_model=list[ProductSchema])
async def get_all_products(
        session:AsyncSession = Depends(db_helper.session_dependency),
):
    return await get_all(session=session)


@product_router.post("/", response_model=ProductSchema)
async def create_product(
        product: ProductSchema,
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await create(session=session, product=product)


@product_router.put("/")
async def update_product(
        product_id: int,
        name: str,
        session: AsyncSession = Depends(db_helper.session_dependency),
):

    return await update_item(session=session, item_id=product_id, new_name=name)


@product_router.delete("/")
async def delete_product(
        product_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await delete_item(session=session, item_id=product_id)





