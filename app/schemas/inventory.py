from pydantic import BaseModel

class InventoryBase(BaseModel):
    item_name: str
    quantity: int
    price: float

class InventoryCreate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    id: int

    class Config:
        orm_mode = True
