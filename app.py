from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/", response_model=schemas.Item)
async def add_item(item: schemas.Item, db: Session = Depends(get_db)):
    item = crud.get_item_by_title(db, title=item.title)
    if item:
        raise HTTPException(status_code=400, detail="Item already exists")
    return crud.add_item(db=db, item=item)


@app.get("/", response_model=List[schemas.Item])
async def root(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items
