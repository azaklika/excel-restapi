import csv
import os
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
import openpyxl

TOKEN = "secret-token"

app = FastAPI(title="CSV REST API")

class Item(BaseModel):
    id: int
    name: str
    value: int

# Load data once at startup. Prefer CSV, but also handle XLSX files.
items: List[Item] = []
if os.path.exists("data.csv"):
    with open("data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(
                Item(
                    id=int(row["id"]),
                    name=row["name"],
                    value=int(row["value"]),
                )
            )
elif os.path.exists("data.xlsx"):
    wb = openpyxl.load_workbook("data.xlsx", read_only=True)
    sheet = wb.active
    rows = sheet.iter_rows(values_only=True)
    headers = next(rows)
    header_map = {name: idx for idx, name in enumerate(headers)}
    for row in rows:
        items.append(
            Item(
                id=int(row[header_map["id"]]),
                name=row[header_map["name"]],
                value=int(row[header_map["value"]]),
            )
        )
else:
    raise FileNotFoundError("Neither data.csv nor data.xlsx found")

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

