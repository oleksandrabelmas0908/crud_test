from fastapi import APIRouter

from .crud import create, get_by_id, update, delete_item


product_router = APIRouter(prefix="/product")


@product_router.get("/get/{product_id}")
def get_product(product_id: int):
    products = [
        {"id": 1, "name": "Kolbasa"},
        {"id": 2, "name": "Syr"},
        {"id": 3, "name": "Chleb"},
    ]

    respond = {}
    try:
        for el in products:
            if el["id"] == product_id:
                respond = el
                break
    except Exception as ex:
        respond = {"message": ex}

    return respond


@product_router.get("/create")
def create_product(name: str):
    return


@product_router.get("/update")
def update_product(product_id: int, name: str):
    return


@product_router.get("/delete")
def delete_product(product_id: int):
    return





