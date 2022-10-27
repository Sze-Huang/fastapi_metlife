from sqlalchemy.orm import Session
from datetime import datetime

import models, schemas



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, business_id: int):
    db_item = models.Item(**item.dict(), business_id=business_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_business(db: Session, id: int):
    return db.query(models.Business).filter(models.Business.id == id).first()


def get_business_by_name(db: Session, name: str):
    return db.query(models.Business).filter(models.Business.name == name).first()


def get_businesses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Business).offset(skip).limit(limit).all()


def create_business(db: Session, business: schemas.BusinessCreate):
    db_business = models.Business(name=business.name, create_date=datetime.now(), longitude=business.longitude, latitude=business.latitude )
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business
