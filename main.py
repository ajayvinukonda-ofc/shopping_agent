from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import csv

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

products = {}

# Load products from CSV
with open("products.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products[row["product"].lower()] = float(row["price"])

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/check")
def check_product(name: str):
    name = name.lower()
    if name in products:
        return JSONResponse(content={"available": True, "product": name, "price": products[name]})
    else:
        return JSONResponse(content={"available": False, "message": "Product not found."})

@app.post("/buy")
def buy_product(name: str):
    name = name.lower()
    if name in products:
        del products[name]
        return JSONResponse(content={"message": f"Product '{name}' bought successfully.", "updated_products": products})
    else:
        return JSONResponse(content={"message": "Product not found. Cannot buy."})



