from fastapi import FastAPI
from fastapi.responses import JSONResponse
import csv

app = FastAPI()

products = {}

with open("products.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products[row["product"].lower()] = float(row["price"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Shopping Agent!"}

@app.get("/check")
def check_product(name: str):
    name = name.lower()
    if name in products:
        price = products[name]
        return JSONResponse(content={"available": True, "product": name, "price": price})
    else:
        return JSONResponse(content={"available": False, "message": "Product not found."})
