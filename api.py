
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
        print (db)
    finally:
        db.close()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your food sharing api."}

@app.get("/business/", response_model=list[schemas.Business])
def get_business(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_businesses(db, skip=skip, limit=limit)
    return users

@app.get("/business/{business_id}", response_model=schemas.Business)
def get_business_by_id(business_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_business(db, id=business_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Business ID not found")
    return db_user


@app.get("/business/name/{name}", response_model=schemas.Business)
def get_business_by_name(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_business_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return db_user

@app.post("/business/", response_model=schemas.Business)
def create_business(business: schemas.BusinessCreate, db: Session = Depends(get_db)):
    db_user = crud.get_business_by_name(db, name=business.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Business Name already registered")
    return crud.create_business(db=db, business=business)




@app.post("/business/{business_id}/items/", response_model=schemas.Item)
def create_item_for_business(business_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, business_id=business_id)

@app.get("/items/", response_model=list[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
