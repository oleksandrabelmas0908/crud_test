from fastapi import FastAPI
from product import product_router


app = FastAPI()
app.include_router(product_router)

@app.get("/")
async def root():
    return {"message": "Hello its test api"}