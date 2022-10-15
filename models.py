from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base



class Business(Base):
    __tablename__ = "tbl_business"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    create_date = Column(String)
    longitude = Column(String)
    latitude = Column(String)

class Item(Base):
    __tablename__ = "tbl_item"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer)
    item = Column(String)
    description = Column(String)
    is_halal = Column(String)
    is_raw = Column(String)
    charges = Column(String)
    quantity = Column(String)
    created_date = Column(String)
    expired_date = Column(String)
