from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class ProductIn(ProductSchema):
    id: int
