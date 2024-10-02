from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    title: str
    description: str = None

items = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    for idx, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for idx, existing_item in enumerate(items):
        if existing_item.id == item_id:
            del items[idx]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
