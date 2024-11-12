from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate, InventoryUpdate

def create_inventory_item(db: Session, item: InventoryCreate):
    db_item = Inventory(item_name=item.item_name, quantity=item.quantity, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_inventory_item(db: Session, item_id: int, item: InventoryUpdate):
    db_item = db.query(Inventory).filter(Inventory.id == item_id).first()
    if db_item:
        db_item.quantity = item.quantity
        db_item.price = item.price
        db.commit()
        db.refresh(db_item)
    return db_item
