from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from product import product_router

from src.models import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "Hello it's test api"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)