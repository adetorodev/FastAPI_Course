from fastapi import FastAPI
from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()  # Create an instance of FastAPI



# @app.get("/")  # Define a GET endpoint
# def read_root():
#     return {"message": "Hello, World!"}


# Query parameters are used to send additional data to the API without including it in the URL path. They are
# appended to the URL after a ? and are separated by & for multiple parameters

# Optional by Default
# Validation with Type Hints
# Default Values
# Automatic Documentation

@app.get("/")
async def greet(name: str = "Guest", age: int = None):
    if age:
        return {"message": f"Hello, {name}! you are {age} year old"}
    return {"message": f"Hello, {name}!"}

@app.get("/products/")
async def filter_products(
    categories: Optional[List[str]] = Query(None, description="Filter by categories"),
    price_min: Optional[float] = Query(0.0, description="Minimum price filter"),
    price_max: Optional[float] = Query(None, description="Maximum price filter")
):
    return {
        "categories": categories,
        "price_range": {"min": price_min, "max": price_max},
        "products": [
            {"product_id": 1, "name": "Laptop", "category": "electronics"},
            {"product_id": 2, "name": "Smartphone", "category": "electronics"}
        ]
    }
