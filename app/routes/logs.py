from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from app.database import get_db
from app.models.logs import Log

router = APIRouter()

@router.get("/")
async def get_logs(
    skip: int = 0,
    limit: int = 100,
    level: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    try:
        query = db.query(Log)
        
        if level:
            query = query.filter(Log.level == level.upper())
        
        if start_date:
            query = query.filter(Log.timestamp >= start_date)
        
        if end_date:
            query = query.filter(Log.timestamp <= end_date)
        
        total = query.count()
        logs = query.offset(skip).limit(limit).all()
        
        return {
            "total": total,
            "logs": logs
        }
    except Exception as e:
        print(f"Error in get_logs: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 