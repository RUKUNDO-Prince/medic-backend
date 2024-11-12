# app/schemas/inventory.py
from pydantic import BaseModel

class InventoryBase(BaseModel):
    item_name: str
    quantity: int
    price: float

class InventoryCreate(InventoryBase):
    pass

class InventoryUpdate(InventoryBase):
    item_name: str | None = None
    quantity: int | None = None
    price: float | None = None

class InventoryOut(InventoryBase):
    id: int

    class Config:
        orm_mode = True
