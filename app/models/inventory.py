from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
