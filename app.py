import csv
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel

TOKEN = "secret-token"

app = FastAPI(title="CSV REST API")

class Item(BaseModel):
    id: int
    name: str
    value: int

# Load CSV data once at startup
items: List[Item] = []
with open("data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        items.append(Item(id=int(row["id"]), name=row["name"], value=int(row["value"])))

def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token and token.startswith("Bearer "):
        token = token.split(" ", 1)[1]
    else:
        token = request.query_params.get("token")
    if token != TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/items", response_model=List[Item])
async def get_items(dep=Depends(verify_token)):
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int, dep=Depends(verify_token)):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

