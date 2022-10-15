from typing import Union

from pydantic import BaseModel

class ItemBase(BaseModel):
    item: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    is_halal: str
    is_raw: str
    charges: str
    quantity: str
    created_date: str
    expired_date: str

class Item(ItemBase):
    id: int
    business_id: int
    is_halal: str
    is_raw: str
    charges: str
    quantity: str
    created_date: str
    expired_date: str

    class Config:
        orm_mode = True


class BusinessBase(BaseModel):
    name: str

class BusinessCreate(BusinessBase):
    name: str
    create_date: str
    longitude: str
    latitude: str

class Business(BusinessBase):
    id: int
    create_date: str
    longitude: str
    latitude: str

    class Config:
        orm_mode = True
