from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Inventory, User
from app.schemas import ReportOut
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("/inventory-summary", response_model=ReportOut)
def inventory_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    total_items = db.query(Inventory).count()
    out_of_stock_items = db.query(Inventory).filter(Inventory.quantity == 0).count()
    report = {
        "total_items": total_items,
        "out_of_stock_items": out_of_stock_items,
    }
    return report
